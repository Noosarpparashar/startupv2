Certainly! Here's the complete README.md file:

```markdown
# E-Cart Data Generator

This repository contains a Python script for generating data for an e-commerce application. The data generator can be Dockerized and run using Docker Compose. The only difference between `ecart` and `ecart_v2` is that `ecart_v2` has Postgres set up on a server rather than locally.

## Prerequisites

- Docker
- Docker Compose
```

## Getting Started

1. Once the database is up and running, create the necessary database tables by executing the DDL scripts provided in the previous folder. These scripts should start with "db" and include the schema creation.

   - Create a database named `PINNACLEDB` and grant replication access to user postgres.
   ```bash
   create DATABASE PINNACLEDB;
   ALTER USER postgres WITH REPLICATION;
   ```

   - Create a schema named `ecart` within the `PINNACLEDB` database.
   ```bash
   create SCHEMA ECART;
   ```

2. Once the services are up and running, the database and schema are created, create tables using the following DDL script. Make sure you are creating inside `pinnacledb` only.

   ```bash
   create table ECART.CUSTOMER (
     CUSTID VARCHAR(50),
     CUSTNAME VARCHAR(100),
     CUSTADD VARCHAR(400)
   ); 

   create table ECART.PRODUCTINFO (
     PRODUCTID INTEGER,
     PRODUCTNAME VARCHAR(150),
     PRODCAT VARCHAR(400),
     STOREID varchar(70)
   );

   create table ECART.STOREINFO (
     STOREID varchar(70),
     STORENAME VARCHAR(150),
     STOREADD VARCHAR(400)
   );

   create table ECART.FACT_ORDER (
     ORDERID SERIAL PRIMARY key,
     CUSTID VARCHAR(50),
     PRODUCTID INTEGER,
     PURCHASETIMESTAMP TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
   );
   ```

3. Clone this repository:

   ```bash
   git clone https://github.com/Noosarpparashar/startupv2.git
   ```

4. Go to the cloned directory and here you  have to change hostname, user and password to whatever you set in google cloud and also you can change speed here in dataGenerator.py file

   ```bash
   cd startupv2/python/dataGenerator/ecart_v2
   ```

5. Dockerize the Python code by building the Docker image. Run the following command:

   ```bash
   docker build -t my-ecart-data-generator .
   ```
6. Switch to infra directory and run docker compose command to setup kafka, kafka connect, schema registry and  kafka ui

   ```bash
   cd startupv2/infra
   docker-compose up
   ```
7. Run the Docker container containing the data generator:

   ```bash
   docker run my-ecart-data-generator
   ```

8. [**Optional**] The data generator will start generating data for the e-commerce application based on the defined logic. If you wish to increase the rate of data generation, go to `dataGenerator.py` and increase [speed](https://github.com/Noosarpparashar/startupv2/blame/master/python/dataGenerator/ecart_v2/dataGenerator.py#:~:text=speed,150) then rerun the following commands:

   ```bash
   docker build -t my-ecart-data-generator .
   docker run my-ecart-data-generator
   ```

8. Connect pgadmin and run the following commands to check if data is coming. Make sure your database is `pinnacledb` only.

   ```bash
   Host: 32.24.48.53
   Port: 5432
   Database: pinnacledb
   Password: 9473
   ```

   ```bash
   select * from ECART.CUSTOMER
   select * from ECART.PRODUCTINFO
   select * from ECART.FACT_ORDER
   select * from ECART.STOREINFO
   ```

9. Create Connector and Send Data to Kafka Topic
Open a tool like Postman or cURL to make a POST request to the Kafka Connect REST API by setting up the endpoint URL to `http://localhost:8083/connectors`.

Replace the request body parameters with the appropriate values and send the POST request. Use the following example as a template, adjusting the values as needed:

```json
{
  "name": "inventory-connector1",
  "config": {
    "connector.class": "io.debezium.connector.postgresql.PostgresConnector",
    "database.hostname": "34.012.345.678",
    "database.port": "5432",
    "database.user": "postgres",
    "database.password": "1234",
    "database.dbname": "pinnacledb",
    "database.server.name": "fullfillment",
    "table.whitelist": "ECART.STOREINFO",
    "topic.prefix": "mysecondtopic"
  }
}
```
11. To verify the connector, open Kafka UI in your browser and navigate to the Kafka Connect section.

In the Kafka Connect section, you will see the newly created connectors listed. Click on the relevant connector, such as "inventory-connector1," to view its details.

Explore the created Kafka topics, and click on any of them to access the "Messages" section.

This completes the process of creating a connector and sending data to a Kafka topic. You can now proceed to consume these messages from Kafka or perform any other desired actions.

Note: For a visual demonstration of this process, refer to the accompanying YouTube video [insert your YouTube video link here]."


## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [Faker](https://faker.readthedocs.io) - Python library for generating fake data.
- [Psycopg](https://www.psycopg.org) - PostgreSQL adapter for Python.

Feel free to modify the instructions based on your specific requirements or provide additional information as needed.
```
```

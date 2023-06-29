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

   - Create a database named `PINNACLEDB`.
   ```bash
   create DATABASE PINNACLEDB;
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

4. Change into the cloned directory:

   ```bash
   cd startupv2/python/dataGenerator/ecart_v2
   ```

5. Dockerize the Python code by building the Docker image. Run the following command:

   ```bash
   docker build -t my-ecart-data-generator .
   ```

6. Run the Docker container containing the data generator:

   ```bash
   docker run my-ecart-data-generator
   ```

7. [**Optional**] The data generator will start generating data for the e-commerce application based on the defined logic. If you wish to increase the rate of data generation, go to `dataGenerator.py` and increase [speed](https://github.com/Noosarpparashar/startupv2/blame/master/python/dataGenerator/ecart/dataGenerator.py#:~:text=speed,150), then rerun the following commands:

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

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [Faker](https://faker.readthedocs.io) - Python library for generating fake data.
- [Psycopg](https://www.psycopg.org) - PostgreSQL adapter for Python.

Feel free to modify the instructions based on your specific requirements or provide additional information as needed.
```
```

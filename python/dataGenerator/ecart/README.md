```markdown
# E-Cart Data Generator

This repository contains a Python script for generating data for an e-commerce application. The data generator can be Dockerized and run using Docker Compose.

## Prerequisites

- Docker
- Docker Compose

## Getting Started

```
1. Clone this repository:
   ```bash
   git clone https://github.com/Noosarpparashar/startupv2.git
   ```

2. Change into the cloned directory:
   ```bash
   cd startupv2/python/dataGenerator/ecart
   

3. Run the following command to start the application using Docker Compose:
   ```bash
   docker-compose up -d
   ```

   This command will start  the PostgreSQL database.
   You can use pgadmin or dbeaver to connect to the PostgreSQL database by providing the following details:

    Host: localhost
    Port: 5433
    Database: postgres
    Password: 9473


4. Once the services are up and running, create the necessary database tables by executing the DDL scripts provided in the previous folder. These scripts should start with "db" and include the schema creation.
   - Create a database named `PINNACLEDB`. 
   - ```bash
        create DATABASE PINNACLEDB
   - Create a schema named `ecart` within the `PINNACLEDB` database.
   - ```bash
        create SCHEMA ECART
5.   Once the services are up and running, database and schema is created, create tables using following script the following DDL script:

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

6. Dockerize the Python code by building the Docker image. Run the following command:
   ```bash
   docker build -t my-ecart-data-generator .
   ```

7. Create a Docker network to allow communication between containers:
   ```bash
   docker network create my-network
   ```

8. Connect the PostgreSQL container to the Docker network. Replace `my-postgres` with the name of your PostgreSQL Docker container:
   ```bash
   docker network connect my-network my-postgres
   ```

9. Run the Docker container containing the data generator:
   ```bash
   docker run --network=my-network my-ecart-data-generator
   ```

   Note: If you are running the Python script outside of Docker, make sure to use port 5433 for the PostgreSQL connection. If running the script inside Docker, use port 5432. Modify the necessary code accordingly.Or don't do anything if you wish to go by default

10. The data generator will start generating data for the e-commerce application based on the defined logic.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [Faker](https://faker.readthedocs.io) - Python library for generating fake data.
- [Psycopg](https://www.psycopg.org) - PostgreSQL adapter for Python.

Feel free to modify the instructions based on your specific requirements or provide additional information as needed.
```
```

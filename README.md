
## Chapter 1: Generate data in your local Postgres

To generate data in your local Postgres database, you can refer to the [Chapter 1 repository](https://github.com/Noosarpparashar/startupv2/tree/master/python/dataGenerator/ecart).

## Chapter 2: Setup Postgres on Google Cloud | Generate Streaming Data | Set up Kafka-Kraft Cluster | Set up Kafka UI | Set up Debezium Connect

In this chapter, we will cover the following topics:

1. Setting up Postgres on Google Cloud.
2. Generating streaming data.
3. Setting up a Kafka-Kraft cluster.
4. Configuring Kafka UI.
5. Setting up Debezium Connect.

For detailed instructions and code examples, please refer to the [Chapter 2 repository](https://github.com/Noosarpparashar/startupv2/tree/master/python/dataGenerator/ecart_v2).

Feel free to explore each chapter's repository for more information and code implementation.

## Chapter 3: Building a Data Lake: Kafka Consumer in Spark-Scala | From Kafka to AWS S3 | Deploying on Container

This project demonstrates how to create a data lake and containerize a multi-node Spark cluster using Docker and run your Spark code within the containers.

Using this code, we read data from the Kafka topic in JSON format. The JSON data is then parsed using Spark SQL's json_tuple function to create a DataFrame with relevant columns. The processed data is written to a Parquet file format. The output is appended to a specific path in the S3 bucket, created based on the current timestamp.

For detailed instructions and code examples, please refer to the [Chapter 3 repository](https://github.com/Noosarpparashar/ecart-migration)https://github.com/Noosarpparashar/ecart-migration


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

For detailed instructions and code examples, please refer to the [Chapter 3 repository](https://github.com/Noosarpparashar/ecart-migration)

Above repo might have been upgraded, Use this commit ID if you want to go to exact same date c3e227c61b13347c888c5201c16e8f7ec8387bac
git checkout c3e227c61b13347c888c5201c16e8f7ec8387bac
## Chapter 4: Give Policy based access control to s3 Bucket

This project demonstrates how to  secure your s3 data  while allowing the right individuals to access it.
It deals with getObject, putObject, listBucketsObjects,Delete Objects, Sync Bucket with local, Restrict access using IP

For detailed instruction please follow [Chapter4 repo](https://github.com/Noosarpparashar/howTo/blob/main/AttachPolicyIns3.txt)

## Chapter 5:Lambda Function to organise s3 files bsed on the time and time zone the data came

This project demonstrates how AWS Lambda works to transfer files to another bucket while categorizing them based on their timestamps in your chosen time zone

For detailed instruction please follow [Chapter5 repo](https://github.com/Noosarpparashar/howTo/blob/main/TransferAndCategoriseFilesUsingLambda.txt)


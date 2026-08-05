# E-Commerce Data ETL Pipeline using Spark, Hadoop, Airflow, Snowflake, PowerBI

This project demonstrates an end-to-end E-Commerce Data ETL Pipeline for processing large-scale e-commerce data using modern Data Engineering tools.

The pipeline automates the complete workflow from data generation to cloud data warehousing using a Medallion Architecture (Bronze, Silver, Gold).

### Bronze Layer:
Raw JSON files are ingested into Hadoop HDFS using Apache Spark.

### Silver Layer: 
PySpark performs data cleaning, preprocessing.

### Gold Layer: 
The processed data is transformed into (Fact & Dimension tables) and stored as Parquet files.

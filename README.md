# E-Commerce Data ETL Pipeline using Spark, Hadoop, Airflow, Snowflake, PowerBI

This project demonstrates an end-to-end E-Commerce Data ETL Pipeline for processing large-scale e-commerce data using modern Data Engineering tools.

The pipeline automates the complete workflow from data generation to cloud data warehousing using a Medallion Architecture (Bronze, Silver, Gold).

---------------------------------------------------------------------------------------------------------------------------------------------------
## System Architecture
![Uploading WhatsApp Image 2026-08-05 at 9.39.59 PM.jpeg…]()



### - Bronze Layer:
- Raw JSON files are ingested into Hadoop HDFS using Apache Spark.

### - Silver Layer: 
- PySpark performs data cleaning, preprocessing.

### - Gold Layer: 
- The processed data is transformed into (Fact & Dimension tables) and stored as Parquet files.


---------------------------------------------------------------------------------------------------------------------------------------

## Pipeline Workflow
```text
Upload Raw Data to HDFS
          │
          ▼
   Raw CSV Data
          │
          ▼
Bronze Layer (HDFS Ingestion)
          │
          ▼
Silver Layer (Cleaning & Preprocessing)
          │
          ▼
Gold Layer (Stored as Parquet Files)
          │
          ▼
Snowflake Data Warehouse

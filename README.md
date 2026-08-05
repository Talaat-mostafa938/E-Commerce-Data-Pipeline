# E-Commerce Data ETL Pipeline using Spark, Hadoop, Airflow, Snowflake, PowerBI

This project demonstrates an end-to-end E-Commerce Data ETL Pipeline for processing large-scale e-commerce data using modern Data Engineering tools.

The pipeline automates the complete workflow from data generation to cloud data warehousing using a Medallion Architecture (Bronze, Silver, Gold).

---------------------------------------------------------------------------------------------------------------------------------------------------
## System Architecture
![image](https://github.com/Talaat-mostafa938/E-Commerce-Data-Pipeline/blob/main/Media/System%20Architecture.jpg)

---------------------------------------------------------------------------------------------------------------------------------------------------
### - Bronze Layer:
- Raw CSVs files are ingested into Hadoop HDFS using Apache Spark.

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
```

---

# Tech Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Apache Spark | Distributed data processing |
| Hadoop HDFS | Distributed storage |
| Apache Airflow | Workflow orchestration |
| Snowflake | Cloud data warehouse |
| Docker | Containerization |
| PySpark | Spark API for Python |
| YARN | Cluster resource management |

---

# Airflow DAG Workflow

The pipeline is orchestrated using Apache Airflow with the following tasks:

1. Bronze Layer
2. Silver Layer
3. Gold Layer


---

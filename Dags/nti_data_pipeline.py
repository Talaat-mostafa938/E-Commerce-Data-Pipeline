from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2025, 1, 1)
}

with DAG(
    dag_id="nti_data_pipeline",
    default_args=default_args,
    description="A simple data pipeline DAG",
    schedule_interval="@daily",
    catchup=False,
    tags=["data", "pipeline"],
) as dag:

    read_from_hdfs = BashOperator(
        task_id = 'read_from_hdfs',
        bash_command = 'docker exec spark-jupyter spark-submit /home/jovyan/work/Bronze.py'
    )
    
    cleaning_data = BashOperator(
        task_id = 'cleaning_data',
        bash_command = 'docker exec spark-jupyter spark-submit /home/jovyan/work/Silver.py'
    )
    
    load_to_snowflake = BashOperator(
        task_id = 'load_to_snowflake',
        bash_command = 'docker exec spark-jupyter spark-submit '
        '--packages net.snowflake:spark-snowflake_2.12:2.15.0-spark_3.4,net.snowflake:snowflake-jdbc:3.14.4 '
        '/home/jovyan/work/Gold.py'
    )
    
    read_from_hdfs >> cleaning_data >> load_to_snowflake


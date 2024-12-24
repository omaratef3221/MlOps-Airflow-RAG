from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from scripts.process_csv import download_csv_from_s3
from scripts.create_rag import create_rag_file
import boto3 
import pandas as pd
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='rag_pipeline',
    default_args=default_args,
    description='Pipeline to create RAG files from S3 data',
    start_date=datetime(2024, 1, 1),
    catchup=False,
    schedule_interval=timedelta(minutes=5),
) as dag:
    fetch_csv = PythonOperator(
        task_id='fetch_csv_from_s3',
        python_callable=download_csv_from_s3,
    )

    generate_rag = PythonOperator(
        task_id='generate_rag',
        python_callable=create_rag_file,
    )

    fetch_csv >> generate_rag

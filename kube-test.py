import airflow
from airflow import DAG
from datetime import datetime
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator

default_args = {
    'owner': 'devops',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(1),
    'retries': 0
}

dag = DAG(
    'run_container',
    schedule_interval='*/30 * * * *',
    default_args=default_args
)


with dag:
    k = KubernetesPodOperator(
        name="my-container",
        image=hello-world:latest,
        namespace="airflow",
        env_vars={
            "RULES": "Testing"
        },
        task_id="run_container",
        get_logs=True,
        in_cluster=False,
        xcom_push=False
    )

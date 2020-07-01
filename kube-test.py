from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from datetime import datetime
from airflow.utils.dates import days_ago

default_args = {
    "owner": "airflow",
    "start_date": days_ago(2),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
}

dag = DAG("foobar", default_args=default_args, schedule_interval=None, catchup=False)

t1 = BashOperator(task_id="foo", bash_command="echo 'foo'", dag=dag)
t2 = BashOperator(task_id="bar", bash_command="echo 'bar'", dag=dag)

t3 = KubernetesPodOperator(
    namespace="default",
    image="busybox:latest",
    image_pull_policy="IfNotPresent",
    arguments=["sleep", "25"],
    name="busybox-test",
    task_id="pod_foo",
    is_delete_operator_pod=True,
    get_logs=True,
    in_cluster=True,
    dag=dag,
)

t2.set_upstream(t1)
t3.set_upstream(t2)

from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    "owner": "bakdata",
    "depends_on_past": False,
    "start_date": datetime(2018, 10, 1),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
    "retry_delay": timedelta(minutes=1)
}

with DAG('connection_plugin_demo', default_args=default_args, schedule_interval=None) as dag:
    print_conn_type = BashOperator(
        task_id='print_conn_type',
        bash_command="echo '{{ macros.connection_plugin.get_conn('metastore_default').conn_type }}'"
    )

    print_host = BashOperator(
        task_id='print_host',
        bash_command="echo '{{ macros.connection_plugin.get_conn('airflow_db').host }}'"
    )

    print_schema = BashOperator(
        task_id='print_schema',
        bash_command="echo '{{ macros.connection_plugin.get_conn('postgres_default').schema }}'"
    )

    print_login = BashOperator(
        task_id='print_login',
        bash_command="echo '{{ macros.connection_plugin.get_conn('postgres_default').login }}'"
    )

    # be especially careful when using passwords in templates
    print_password = BashOperator(
        task_id='print_password',
        bash_command="echo '{{ macros.connection_plugin.get_conn('airflow_db').password }}'"
    )

    print_port = BashOperator(
        task_id='print_port',
        bash_command="echo '{{ macros.connection_plugin.get_conn('metastore_default').port }}'"
    )

    print_extra = BashOperator(
        task_id='print_extra',
        bash_command="echo '{{ macros.connection_plugin.get_conn('aws_default').extra }}'"
    )

    print_extra_dejson = BashOperator(
        task_id='print_extra_dejson',
        bash_command="echo '{{ macros.connection_plugin.get_conn('aws_default').extra_dejson.region_name }}'"
    )

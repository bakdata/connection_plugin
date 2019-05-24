from airflow.hooks.base_hook import BaseHook


def get_conn(conn_name):
    # get connection by name from BaseHook
    conn = BaseHook.get_connection(conn_name)

    return conn

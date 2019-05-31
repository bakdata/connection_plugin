from airflow.hooks.base_hook import BaseHook


def get_conn(conn_id):
    # get connection by name from BaseHook
    conn = BaseHook.get_connection(conn_id)

    return conn

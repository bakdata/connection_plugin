from airflow.plugins_manager import AirflowPlugin

from connection_plugin.macros import get_conn


class ConnectionPlugin(AirflowPlugin):
    name = "connection_plugin"
    operators = []
    macros = [get_conn]

# Templating for Airflow connections
[![PyPI version](https://badge.fury.io/py/airflow-connection-plugin.svg)](https://badge.fury.io/py/airflow-connection-plugin)

The connection plugin contains an [Airflow](https://airflow.apache.org/) macro for [templating](https://airflow.apache.org/concepts.html#id1) connections in tasks. You can use it like this:

```
{{ macros.connection_plugin.get_conn('airflow_db').host }}
```
`connection_plugin.get_conn` returns the [Connection object](https://airflow.apache.org/_api/airflow/models/connection/index.html#airflow.models.connection.Connection) 
that you can interact with like it is described in the documentation.

## Installation
```
pip install airflow-connection-plugin
```

## Demo
To start the docker container simply run the following command in the root directory:
```
cd example && docker-compose up
```

After that you can reach the airflow frontend via [http://localhost:8080](http://localhost:8080). You will find an
example DAG that demonstrates how to retrieve different connection information.

**Attention**: Be especially careful when using passwords in templates.

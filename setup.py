from setuptools import setup, find_packages

setup(
    name="airflow-connection-plugin",
    version="0.0.1",
    packages=find_packages(),
    python_requires="==3.6.*",
    install_requires=[
        "apache-airflow >=1.10.2"
    ],
    entry_points={
        "airflow.plugins": [
            "connection_plugin = connection_plugin:ConnectionPlugin",
        ],
    },
)
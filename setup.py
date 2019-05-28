import pathlib

from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="airflow-connection-plugin",
    version="1.0.0rc2",
    description="Templating for Airflow connections",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/bakdata/connection_plugin",
    author="bakdata",
    author_email="info@bakdata.com",
    license="MIT",
    classifiers=[
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.6",
        ],
    packages=find_packages(),
    include_package_data=True,
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
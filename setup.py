import pathlib

from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="airflow-connection-plugin",
    version="1.0.0",
    description="Templating for Airflow connections",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/bakdata/connection_plugin",
    author="bakdata",
    author_email="opensource@bakdata.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    packages=find_packages(),
    python_requires=">=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*",
    install_requires=[
        "apache-airflow >=1.10.2"
    ],
    entry_points={
        "airflow.plugins": [
            "connection_plugin = connection_plugin:ConnectionPlugin",
        ],
    },
)
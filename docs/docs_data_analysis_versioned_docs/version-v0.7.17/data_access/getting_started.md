---
toc_max_heading_level: 4
sidebar_label: 'Getting Started'
hide_title: true
description: 'Getting started'
sidebar_position: 1
---
# Getting Started

In order to get information about the data of the specific table in the database, to look through the main features and to query the selected parts the module **data_access** from the package **citros_data_analysis** is used. Module is imported by:

```python
from citros_data_analysis import data_access as da
```
To obtain the current package version number, execute the following:
```python
>>> import citros_data_analysis
>>> print(citros_data_analysis.__version__)
```

## Connection to the Database

To connect to the database [**CitrosDB**](../documentation/data_access/citros_db.md#citros_data_analysis.data_access.citros_db.CitrosDB) object is created:
```python
>>> citros = da.CitrosDB()
```

When working in the [web](https://citros.io/) or with cloud data locally using [CITROS CLI](https://citros.io/doc/docs_cli), you typically don't need to pass any arguments. In the latter case, you need to be [logged in](https://citros.io/doc/docs_tutorials#logging-in) first.

<details>
  <summary>Advanced CitrosDB parameters</summary>

If no parameters are passed, the following predefined ENV variables are used:
 - host: 'PG_HOST'
 - user: 'PG_USER',
 - password: 'PG_PASSWORD',
 - database: 'PG_DATABASE',
 - schema: 'PG_SCHEMA' or 'data_bucket' if 'PG_SCHEMA' is not specified,
 - repo: 'CITROS_REPO'
 - batch: 'bid', 
 - simulation: 'CITROS_SIMULATION'
 - sid: 'CITROS_SIMULATION_RUN_ID'
 - port: 'PG_PORT', or '5432' if 'PG_PORT' is not specified,
 - sid: 'CITROS_SIMULATION_RUN_ID'

When working from a local environment and user, password, database ENV variables are not defined, they are set using CITROS CLI authentication; if repo ENV variable is not set, it is retried from 'name' field of the '.citros/project.json' file.

Say, we would like to connect to a database "myDatabase" with the user name "user" and password "myPassword", to work with batch "batchName" which is located in the schema "mySchema", using port '5432':

```python
>>> citros = da.CitrosDB(host = 'hostName',
                         user = 'user',
                         password = 'myPassword',
                         database = 'myDatabase',
                         schema = 'mySchema',
                         batch = 'batchName',
                         port = '5432',
                         debug_flag = False)
```
When `debug_flag` is set to True, that will lead to code interruption if an error occurs, while with `debug_flag` turned to False program will try to handle errors and only print error messages without code breaking. By default, debug_flag = False.

</details>

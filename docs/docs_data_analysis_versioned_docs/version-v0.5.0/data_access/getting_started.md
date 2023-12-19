---
toc_max_heading_level: 4
sidebar_label: 'Getting started'
hide_title: true
# description: Examples of the data_access module
sidebar_position: 1
---

## Data Access

In order to get information about the data of the specific table in the database, to look through the main features and to query the selected parts the module **data_access** from the package **citros_data_analysis** is used. Module is imported by:

```python
from citros_data_analysis import data_access as da
```
To obtain the current package version number, execute the following:
```python
>>> import citros_data_analysis
>>> print(citros_data_analysis.__version__)
```
## Connection to the database

To connect to the database [**CitrosDB**](../documentation/data_access/citros_db.md#citros_data_analysis.data_access.citros_db.CitrosDB) object is created:
```python
>>> citros = da.CitrosDB()
```
<details>
  <summary>Advanced CitrosDB parameters</summary>

If no parameters are passed, the following predefined ENV parameters are used:
 - host: 'PG_HOST'
 - user: 'PG_USER',
 - password: 'PG_PASSWORD',
 - database: 'PG_DATABASE',
 - schema: 'PG_SCHEMA' or 'data_bucket' if 'PG_SCHEMA' not specified,
 - batch: 'bid', 
 - port: 'PG_PORT', or '5432' if 'PG_PORT' is not specified,
 - sid: 'CITROS_SIMULATION_RUN_ID'

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

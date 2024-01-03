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
>>> from citros.citros_data_analysis import data_access as da
```
To obtain the current package version number, execute the following:
```python
>>> import citros.citros_data_analysis
>>> print(citros_data_analysis.__version__)
```

## Connection to the Database

To connect to the database [**CitrosDB**](../documentation/data_access/citros_db.md#citros_data_analysis.data_access.citros_db.CitrosDB) object is created:
```python
>>> citros = da.CitrosDB()
```

You can define simulation and/or batch you will work with:

```python
>>> citros = da.CitrosDB(simulation = 'simulation_name', batch = 'batch_name')
```

or set them up later.

<details>
  <summary>Advanced CitrosDB parameters</summary>

 - simulation : name of the simulation. Default is ENV variable "CITROS_SIMULATION" if it is set or None if the variable is not defined.
 - batch : batch name.
 - sid : simulation run id. Default is ENV variable "CITROS_SIMULATION_RUN_ID" if it is set or None if the variable is not defined.
 - host : database host address. Default is citros.database.CitrosDB.db_host.
 - port : default is citros.database.CitrosDB.db_port.
 - database : database name. Default is citros.database.CitrosDB.db_name.
 - user : user name. Default is citros.database.CitrosDB.db_user.
 - password : password. Default is citros.database.CitrosDB.db_password.
 - debug : if `True`, the number of connections and queries which were done by all CitrosDB objects with `debug` set `True` existing in the current session is recorded. The information is recorded to the _stat.Stat() object. Default is `False`.

Say, we would like to connect to a database "myDatabase" with the user name "user" and password "myPassword", to work with batch "batchName" which is located in the schema "mySchema", using port '5432'. Also we would like to check how many connections and queries we are making during the session:

```python
>>> citros = da.CitrosDB(host = 'hostName',
                         user = 'user',
                         password = 'myPassword',
                         database = 'myDatabase',
                         schema = 'mySchema',
                         batch = 'batchName',
                         port = '5432',
                         debug = True)
>>> import citros.citros_data_analysis.data_access._stat as st
>>> stat = st.Stat()
>>> stat.print_stat()
{
 'n_pg_connections': 0,
 'n_pg_queries': 0,
 'pg_calls': {
 }
}
```
</details>

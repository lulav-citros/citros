---
toc_max_heading_level: 4
sidebar_label: 'Getting Started'
hide_title: true
description: 'Getting started'
sidebar_position: 1
---
# Getting Started

In order to get information about the data of the specific table in the database, to look through the main features and to query the selected parts the class **CitrosDB** from the package **citros** is used:

```python
>>> from citros import CitrosDB
```

## Connection to the Database

To connect to the database [**CitrosDB**](../documentation/access/citros_db.md#access.citros_db.CitrosDB) object is created:
```python
>>> citros = CitrosDB()
```

You can define simulation and/or batch you will work with:

```python
>>> citros = CitrosDB(simulation = 'simulation_name', batch = 'batch_name')
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
 - debug_connect : if `True`, the number of connections and queries which were done by all CitrosDB objects with `debug_connect` set `True` existing in the current session is recorded. The information is recorded to the _stat.Stat() object. Default is `False`.
 - log : Logger to record log. By default, then the new logger is created.

Say, we would like to connect to a database "myDatabase" with the user name "user" and password "myPassword", to work with batch "batchName" which is located in the schema "mySchema", using port '5432'. Also we would like to check how many connections and queries we are making during the session:

```python
>>> citros = CitrosDB(host = 'hostName',
                      user = 'user',
                      password = 'myPassword',
                      database = 'myDatabase',
                      schema = 'mySchema',
                      batch = 'batchName',
                      port = '5432',
                      debug_connect = True)
>>> from citros.data.access._stat import Stat
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

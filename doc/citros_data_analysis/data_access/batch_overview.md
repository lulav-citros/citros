---
toc_max_heading_level: 4
hide_title: true
sidebar_position: 3
sidebar_label: 'Setting the Simulation and the Batch'
description: 'Setting the Simulation and the Batch'
---
# Setting the Simulation and the Batch

*Batches* (tables with data) are created by various *simulation* scenarios and stored in the database under corresponding *simulation* names. To access a specific batch, both its name and the name of the simulation are needed.

## Setting Simulation

Simulation name can be set when the [**CitrosDB**](getting_started.md#connection-to-the-database) object is created:

```python
>>> citros = da.CitrosDB(simulation = 'simulation_name')
```

or by the method [**simulation()**](../documentation/data_access/citros_db.md#citros_data_analysis.data_access.citros_db.CitrosDB.simulation), like in the following example:
```python
>>> citros.simulation('simulation_name').batch('batch_name').data()
```

If the simulation is specified during the creation of the [**CitrosDB**](getting_started.md#connection-to-the-database) object, the simulation name will be saved and used in all subsequent queries. The [**simulation()**](../documentation/data_access/citros_db.md#citros_data_analysis.data_access.citros_db.CitrosDB.simulation) method does not save the simulation name. This option can be beneficial if you plan to work with batches from different simulations and want to explicitly specify which one you are using each time. However, it is possible to set the simulation name for an existing [**CitrosDB**](getting_started.md#connection-to-the-database) object by passing the parameter `inplace` = True. Observe the differences between using the [**simulation()**](../documentation/data_access/citros_db.md#citros_data_analysis.data_access.citros_db.CitrosDB.simulation) method with and without the `inplace` = True parameter:

```python
>>> citros.simulation('simulation_name')
>>> print(f"simulation name: {citros.get_simulation_name()}")
```
```text
simulation name: None
```

```python
>>> citros.simulation('simulation_name', inplace = True)
>>> print(f"simulation name: {citros.get_simulation_name()}")
```
```text
simulation name: simulation_name
```

Method [**get_simulation_name**](../documentation/data_access/citros_db.md#citros_data_analysis.data_access.citros_db.CitrosDB.get_simulation_name) returns the name of the set simulation.

## Setting Batch

The batch is set either when [**CitrosDB**](getting_started.md#connection-to-the-database) object is created by passing a batch name by `batch` argument:

```python
>>> citros = da.CitrosDB(batch = 'batch_name')
```

or later, for example before [querying data](query_data.md#query-data), by method [**batch()**](../documentation/data_access/citros_db.md#citros_data_analysis.data_access.citros_db.CitrosDB.batch):
```python
>>> citros = da.CitrosDB()
>>> citros.simulation('simulation_name').batch('batch_name').data()
```

The difference between these two approaches is the same as in [Setting Simulation](#setting-simulation):

- In the first case, the [**CitrosDB**](getting_started.md#connection-to-the-database) object saves the `batch` name, so you do not need to specify it each time you access the batch.
- In the second option, the batch name is not saved; the method [**batch()**](../documentation/data_access/citros_db.md#citros_data_analysis.data_access.citros_db.CitrosDB.batch) simply returns a new [**CitrosDB**](getting_started.md#connection-to-the-database) object with the `batch` parameter set, that can be used further in a chain of methods, for example, to query data, as shown in the example above. The batch name can still be set to the existing [**CitrosDB**](getting_started.md#connection-to-the-database) object if the parameter `inplace` = True is used. Without the `inplace` parameter, the batch name will not be saved to the current CitrosDB object, enhancing readability by always making clear which batch you are currently using and ensuring that previous settings do not affect your future work:

```python
>>> citros = da.CitrosDB()
>>> citros.batch('batch_name').data()
>>> #some steps...
>>> print(f"current batch name: {citros.get_batch_name()}")
```
```text
current batch name: None
```
However, if you prefer to work with just one batch and don't want to specify it every time, set `inplace` to True. This will save the batch id and batch name in the settings of the current `CitrosDB` object:
```python
>>> citros.batch('batch_name', inplace = True)
>>> print(f"current batch name: {citros.get_batch_name()}")
```
```text
current batch name: batch_name
```

The method [**get_batch_name()**](../documentation/data_access/citros_db.md#citros_data_analysis.data_access.citros_db.CitrosDB.get_batch_name) returns the name of the batch.
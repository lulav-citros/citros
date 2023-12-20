---
toc_max_heading_level: 4
hide_title: true
sidebar_position: 3
sidebar_label: 'Batch Overview'
description: 'Information about batches'
---
# Batch Overview

Different simulations are identified by their *sid* numbers, with each step of the simulation being sequentially numbered by *rid*. Batches typically contain multiple topics that encapsulate related datasets.

To get the information about all the existing batches the method [**search_batch**](#batch-information) is used. The batch is set when the [**CitrosDB**](getting_started.md#connection-to-the-database) object is created or by [**batch()**](#setting-batch) method. Methods [**get_batch()**, **get_batch_name()** and **get_batch_id()**](#current-batch) return the general information of the current batch, if it was set previously.

Each batch contains the following columns:

||user\_id | sid | rid | time | topic | type| data |
|--|--|--|--|--|--|--|--|
|description |user name | simulation id| run id| ros time message | topic name| type name | json-format data|
|type| uuid | int | int | big int | str | str | jsonb|

Batch may have several *topic*s - to list them along with structure of the json-data column for the current batch the method [**get_data_structure()**](batch_content.md#data-structure) or [**info()**](batch_content.md#data-overview) is used. Initial parameters of the simulation are usually written under the topic '/config'.

Each simulation in the batch has its own id - *sid*, and each message in the simulation is enumerated by run id - *rid*.

If there are infinite values in the data, they are stored as $\pm 10^{308}$.

## Batch Information

Method [**search_batch**](../documentation/data_access/citros_db.md#citros_data_analysis.data_access.citros_db.CitrosDB.search_batch) is applied to show the general information about batches: its name, batch id, list of simulation ids (sids) and when the batch was created. The result is a [**CitrosDict**](../documentation/data_access/citros_dict.md#citros_data_analysis.data_access.citros_dict.CitrosDict) object, that inherits behavior of an ordinary python dictionary, but has some additional methods, like [**print()**](../documentation/data_access/citros_dict.md#citros_data_analysis.data_access.citros_dict.CitrosDict.print) method. To display the information about all the existing batches adopt the following:

```python
>>> citros.search_batch().print()
```
```js
{
  'kinematics': {
    'id': '00000000-aaaa-1111-2222-333333333333',
    'sid': [1, 2, 3, 4, 5],
    'created_at': '2023-06-14T11:44:31.728585+00:00',
    'updated_at': '2023-06-14T11:44:31.728585+00:00',
    'status': 'DONE',
    'data_status': 'LOADED',
    'data_last_access': '2023-06-15T13:24:0.368282+00:00',
    'tag': 'latest',
    'simulation': 'simulation_parameters',
    'message': 'launch_params',
    'parallelism': 1,
    'completions': 1,
    'cpu': 2,
    'gpu': 0,
    'memory': '265',
    'repo': 'citros_project',
    'link': https://citros.io/...
  },
  'kinematics_2': {
    'id': '00000000-bbbb-1111-2222-333333333333',
    'sid': [0, 1, 2, 3],
    'created_at': '2023-06-21T13:51:47.29987+00:00',
    ...
  },
  'dynamics': {
    'id': '00000000-dddd-1111-2222-333333333333',
    'sid': [1, 3, 2],
    'created_at': '2023-06-21T15:03:07.308498+00:00',
    ...
  }
}
```

<details>
  <summary>more about CitrosDict</summary>

`print()` method allows to print the output with proper indents, enhancing readability. However, it is always an option to display the result using the standard Python print method, displaying it as a regular dictionary:

```python
>>> print(citros.search_batch())
{'kinematics': {'id': ...}, 'kinematics_2': {'id': ...}, 'dynamics': {'id': ...}}
```

[**CitrosDict**](../documentation/data_access/citros_dict.md#citros_data_analysis.data_access.citros_dict.CitrosDict) object can be converted to json string by the method [**to_json()**](../documentation/data_access/citros_dict.md#citros_data_analysis.data_access.citros_dict.CitrosDict.to_json):
```python
>>> print(citros.search_batch().to_json())
```
```js
{
  "kinematics": {
    "id": "00000000-aaaa-1111-2222-333333333333",
    "sid": [
      1,
      2,
      3,
      4,
      5
    ],
    "created_at": "2023-06-14T11:44:31.728585+00:00",
    ...
  },
  "kinematics_2": {
    "id": "00000000-bbbb-1111-2222-333333333333",
    "sid": [
      0,
      1,
      2,
      3
    ],
    "created_at": "2023-06-21T13:51:47.29987+00:00",
    ...
  },
  "dynamics": {
    "id": "00000000-dddd-1111-2222-333333333333",
    "sid": [
    ...
    ],
    ...
  }
}
```
or printed by the method [**print()**](../documentation/data_access/citros_dict.md#citros_data_analysis.data_access.citros_dict.CitrosDict.print) as it was shown above.

</details>

Simulation have different statuses: 'DONE', 'SCHEDULE', 'ERROR', 'CREATING', 'INIT', 'STARTING', 'RUNNING', 'TERMINATING' or 'STOPPING'.
To select only batches with the exact status of their simulations, pass the `sid_status` argument:

```python
>>> citros.search_batch(sid_status = 'DONE')
```

There are several options that allows to search for the exact batch. Passing a string that matches the batch name, the search will yield all batches whose names correspond to the provided string:

```python
>>> citros.search_batch('kinematics').print()
```
```js
{
  'kinematics': {
    'id': '00000000-aaaa-1111-2222-333333333333',
    'sid': [1, 2, 3, 4, 5],
    'created_at': '2023-06-14T11:44:31.728585+00:00',
    ...
  },
  'kinematics_2': {
    'id': '00000000-bbbb-1111-2222-333333333333',
    'sid': [0, 1, 2, 3],
    'created_at': '2023-06-21T13:51:47.29987+00:00',
    ...
  },
}
```

If the batch id is know, it can be provided as an argument to query information about this exact batch:

```python
>>> citros.search_batch('00000000-dddd-1111-2222-333333333333').print()
```
```js
{
  'dynamics': {
    'id': '00000000-dddd-1111-2222-333333333333',
    'sid': [1, 3, 2],
    'created_at': '2023-06-21T15:03:07.308498+00:00',
    ...
  }
}
```

Or it is possible to select the last created batch by passing int value -1:

```python
>>> citros.search_batch(-1).print()
```
```js
{
  'dynamics': {
    'id': '00000000-dddd-1111-2222-333333333333',
    'sid': [1, 3, 2],
    'created_at': '2023-06-21T15:03:07.308498+00:00',
    ...
  }
}
```

To retrieve the second-to-last created batch, provide -2 as an argument. Similarly, to select the batch created first, use 0; for the second batch created, use 1, and so forth.

To search by another field, provide it in `search_by` field along with the appropriate format for the `search` argument. To find batches with an exact match in the 'simulation', 'status', 'tag', and 'message' fields, simply provide the word as a string:

```python
>>> citros.search_batch('launch', search_by = 'message').print()
```
```js
{
  'kinematics': {
    'id': '00000000-aaaa-1111-2222-333333333333',
    'sid': [1, 2, 3, 4, 5],
    'created_at': '2023-06-14T11:44:31.728585+00:00',
    'updated_at': '2023-06-14T11:44:31.728585+00:00',
    'status': 'DONE',
    'data_status': 'LOADED',
    'data_last_access': '2023-06-15T13:24:0.368282+00:00',
    'tag': 'latest',
    'simulation': 'simulation_parameters',
    'message': 'launch_params',
    'parallelism': 1,
    'completions': 1,
    'cpu': 2,
    'gpu': 0,
    'memory': '265',
    'repo': 'citros_project',
    'link': https://citros.io/...
  }
}
```

Similarly, provide `search` argument as int for 'parallelism', 'completions' and 'memory' fields and as float for 'cpu' and 'gpu' fields:

```python
>>> citros.search_batch(2, search_by = 'parallelism').print()
```
```js
{
 'kinematics_2': {
  'id': '00000000-bbbb-1111-2222-333333333333',
  'sid': [0, 1, 2, 3],
  'created_at': '2023-06-21T13:51:47.29987+00:00',
  'updated_at': '2023-06-21T13:51:47.29987+00:00',
  'status': 'DONE',
  'data_status': 'LOADED',
  'data_last_access': '2023-07-15T13:24:0.368282+00:00',
  'tag': 'latest',
  'simulation': 'simulation_parameters_2',
  'message': 'recalculation',
  'parallelism': 2,
  ...
  }
}
```

To perform a search based on date fields, select a keyword for the `search_by` field: 'created_after', 'created_before', 'updated_after', or 'updated_before'. Then, provide the date in the `search` argument using one of the following formats:
- 'dd-mm-yyyy hh:mm:ss +hh:mm' - the full date, time and time zone: 
- 'dd-mm-yyyy hh:mm:ss' - date and time without time zone (by default timezone +00:00)
- 'dd-mm-yyyy' / 'dd-mm' / 'dd' - only date. This way, time in the search is set to be 00:00:00
- 'hh:mm:ss' / 'hh:mm' - only time, in this case the date is set as today.

For example, to display all the batches that were created after 20 June:

```python
>>> citros.search_batch('20-06', search_by = 'created_after').print()
```
```js
{
 'kinematics_2': {
    'id': '00000000-bbbb-1111-2222-333333333333',
    'sid': [0, 1, 2, 3],
    'created_at': '2023-06-21T13:51:47.29987+00:00',
    ...
  },
  'dynamics': {
    'id': '00000000-dddd-1111-2222-333333333333',
    'sid': [1, 3, 2],
    'created_at': '2023-06-21T15:03:07.308498+00:00',
    ...
  }
}
```

To get the information about the batches that were updated before 9:00 today, do the following:

```python
>>> citros.search_batch('9:00', search_by = 'updated_before').print()
```
```js
{
  'kinematics': {
    'id': '00000000-aaaa-1111-2222-333333333333',
    'sid': [1, 2, 3, 4, 5],
    'created_at': '2023-06-14T11:44:31.728585+00:00',
    ...
  },
  'kinematics_2': {
    'id': '00000000-bbbb-1111-2222-333333333333',
    'sid': [0, 1, 2, 3],
    'created_at': '2023-06-21T13:51:47.29987+00:00',
    ...
  },
  'dynamics': {
    'id': '00000000-dddd-1111-2222-333333333333',
    'sid': [1, 3, 2],
    'created_at': '2023-06-21T15:03:07.308498+00:00',
    ...
  }
}
```

The `order_by` argument enables to choose the order of the output by one of the field. To display the output in ascending order by one or more fields, list them in `order_by` argument. If the field is the only one, it may be passed directly as a str, for example, to order the output of the previous example in ascending order by name of the batches:

```python
>>> citros.search_batch('9:00', search_by = 'updated_before', order_by = 'name').print()
```
```js
{
  'dynamics': {
    'id': '00000000-dddd-1111-2222-333333333333',
    'sid': [1, 3, 2],
    'created_at': '2023-06-21T15:03:07.308498+00:00',
    ...
  },
  'kinematics': {
    'id': '00000000-aaaa-1111-2222-333333333333',
    'sid': [1, 2, 3, 4, 5],
    'created_at': '2023-06-14T11:44:31.728585+00:00',
    ...
  },
  'kinematics_2': {
    'id': '00000000-bbbb-1111-2222-333333333333',
    'sid': [0, 1, 2, 3],
    'created_at': '2023-06-21T13:51:47.29987+00:00',
    ...
  }
}
```

To indicate the desired order, whether descending or ascending, you can pass an argument as a dictionary. For instance, to arrange the output based on the creation time in descending order, placing the most recent first, use the following:

```python
>>> citros.search_batch('11:00', search_by = 'updated_before', order_by = {'created_at': 'desc'}).print()
```
```js
{
  'dynamics': {
    'id': '00000000-dddd-1111-2222-333333333333',
    'sid': [1, 3, 2],
    'created_at': '2023-06-21T15:03:07.308498+00:00',
    ...
  },
   'kinematics_2': {
    'id': '00000000-bbbb-1111-2222-333333333333',
    'sid': [0, 1, 2, 3],
    'created_at': '2023-06-21T13:51:47.29987+00:00',
    ...
  }
  'kinematics': {
    'id': '00000000-aaaa-1111-2222-333333333333',
    'sid': [1, 2, 3, 4, 5],
    'created_at': '2023-06-14T11:44:31.728585+00:00',
    ...
  }
}
```

By default, the displayed batches include all batches, regardless of their creator. You can limit the display to only show batches that belong to you by setting `user`` to 'me':

```python
>>> citros.search_batch('kinematics', user = 'me').print()
```
```js
{
  'kinematics': {
    'id': '00000000-aaaa-1111-2222-333333333333',
    'sid': [1, 2, 3, 4, 5],
    'created_at': '2023-06-14T11:44:31.728585+00:00',
    ...
  }
}
```

## Setting Batch

The batch is set either when [**CitrosDB**](getting_started.md#connection-to-the-database) object is created (by passing an argument `batch` or automatically, getting id from the environment variable `bid`) or by method [**batch()**](../documentation/data_access/citros_db.md#citros_data_analysis.data_access.citros_db.CitrosDB.batch). 

If the exact batch id is known, it may be passed in the following way:

```python
>>> citros = da.CitrosDB()
>>> citros = citros.batch('00000000-1111-2222-3333-444444444444')
```

By default, method [**batch()**](../documentation/data_access/citros_db.md#citros_data_analysis.data_access.citros_db.CitrosDB.batch) returns [**CitrosDB**](getting_started.md#connection-to-the-database) object with set `batch` parameter, which then can be used in a chain, for example, to [query data](query_data.md#query-data). Alternatively, the batch may be set to the existing [**CitrosDB**](getting_started.md#connection-to-the-database) object if the parameter `inplace` = True. Without the `inplace` parameter, the batch name or id won't be saved to the current CitrosDB object, enhancing readability since you always see which batch you're currently using, ensuring that old settings won't impact your future work:

```python
>>> citros = da.CitrosDB()
>>> citros.batch('00000000-1111-2222-3333-444444444444').data()
>>> #some steps...
>>> print(f"current batch name: {citros.get_batch_name()}")
>>> print(f"current batch id: {citros.get_batch_id()}")
```
```text
current batch name: None
current batch id: None
```
However, if you prefer to work with just one batch and don't want to specify it every time, set `inplace` to True. This will save the batch id and batch name in the settings of the current `CitrosDB` object:
```python
>>> citros.batch('00000000-1111-2222-3333-444444444444', inplace = True)
>>> print(f"current batch name: {citros.get_batch_name()}")
>>> print(f"current batch id: {citros.get_batch_id()}")
```
```text
current batch name: spectroscopy
current batch id: 00000000-1111-2222-3333-444444444444
```

The name and the id of the current batch may be obtained by **get_batch_name()** and **get_batch_id()** [methods](#current-batch).

Similar to the [**search_batch**](#batch-information), you can also set the batch using its name:

```python
>>> citros = citros.batch('kinematics')
```

Batch may be set by its order of the creation as in the [**search_batch**](#batch-information) method:

```python
>>> citros = citros.batch(-1)
```
In the above example, the most recently created batch is assigned.

## Setting Repository and Simulation of the Batch

By default, search by name is looking not for the exact name, but for the occurrence of the given words in batch name. So if there are two batches 'kinematics' and 'kinematics_1', attempt to set batch by 'kinematics' will result in warning that the batch is not set:
```python
>>> citros = citros.batch('kinematics')
```
```text
batch is not set: there is more than one batch with "kinematics" in the name,
provide one of the following options to `batch()` method with `exact_match` = True:
['kinematics', 'kinematics_1']
or try `search_batch()` method'
```

So, if the the provided batch name has multiple matches, the clarification may be needed.
This can be easily achieved by setting one of the constraints:

- follow the warning's suggestion and set `exact_match` to True. This will select the batch with the exact name provided (if it exists):
```python
>>> citros = citros.batch('kinematics', exact_match = True)
```
- set repository
Setting repository will narrow the search to the batches from the given repository:
```python
>>> citros.repo('citros_project').batch('kinematics')
```
See [setting repository](repository_overview.md#setting-repository)

- set simulation
Set the simulation in which the batch was created by [**simulation()**](../documentation/data_access/citros_db.md#citros_data_analysis.data_access.citros_db.CitrosDB.simulation) method:
```python
>>> citros.simulation('simulation_parameters').batch('kinematics')
```

- combine all the above:
```python
>>> citros.repo('citros_project').simulation('simulation_parameters').batch('kinematics', exact_match = True)
```

You can get the information of the previously set simulation by [**get_simulation**](../documentation/data_access/citros_db.md#citros_data_analysis.data_access.citros_db.CitrosDB.get_simulation) method:

```python
citros.simulation('simulation_parameters').get_simulation().print()
```
```js
{
 'name': 'simulation_parameters'
}
```

Or get just simulation name by [**get_simulation_name**](../documentation/data_access/citros_db.md#citros_data_analysis.data_access.citros_db.CitrosDB.get_simulation_name) method:

```python
citros.simulation('simulation_parameters').get_simulation_name()
```
```js
'simulation_parameters'
```

:::note
The mentioned constraints may be applied before [**search_batch**](#batch-information) method too. Then the information only for batch that meets all the conditions will be shown:
```python
>>> citros.repo('citros_project').simulation('simulation_parameters').search_batch('kinematics', exact_match = True).print()
```
```js
{
 'kinematics': {
   'id': '00000000-aaaa-1111-2222-333333333333',
   'sid': [0],
   'created_at': '2023-10-03T12:03:47.055638+00:00',
   'updated_at': '2023-10-17T20:00:00.023471+00:00',
   'status': 'DONE',
   'data_status': 'LOADED',
   'data_last_access': '2023-10-15T13:24:0.368282+00:00',
   'tag': 'latest',
   'simulation': 'simulation_parameters',
   'message': '',
   'parallelism': 1,
   'completions': 1,
   'cpu': 2,
   'gpu': 0,
   'memory': '265',
   'repo': 'citros_project',
   'link': https://citros.io/...
 }
}
```
:::

## Current Batch

If the batch is set during initialization of [**CitrosDB**](getting_started.md#connection-to-the-database) object by [**batch()**](#setting-batch) method, the general information about it can be obtained by  [**get_batch()**](../documentation/data_access/citros_db.md#citros_data_analysis.data_access.citros_db.CitrosDB.get_batch) method:

```python
>>> citros.batch('spectroscopy').get_batch()
```
```js
{
  'name': 'spectroscopy',
  'id': '00000000-1111-2222-3333-444444444444',
  'sid': [1, 2, 3, 4, 5],
  'created_at': '2023-08-14T11:44:31.728585+00:00',
  'updated_at': '2023-08-14T11:44:31.728585+00:00',
  'status': 'DONE',
  'data_status': 'LOADED',
  'data_last_access': '2023-09-15T13:24:0.368282+00:00',
  'tag': 'latest',
  'simulation': 'galaxy',
  'message': 'test_parameters',
  'parallelism': 1,
  'completions': 1,
  'cpu': 2,
  'gpu': 0,
  'memory': '265',
  'repo': 'galaxy_dynamics',
  'link': https://citros.io/...
}
```

Name of the current batch and its id may be retrieved by [**get_batch_name()**](../documentation/data_access/citros_db.md#citros_data_analysis.data_access.citros_db.CitrosDB.get_batch_name) and [**get_batch_id()**](../documentation/data_access/citros_db.md#citros_data_analysis.data_access.citros_db.CitrosDB.get_batch_id) methods correspondingly:

```python
>>> citros.batch('spectroscopy', inplace = True)
>>> print(f"current batch name: {citros.get_batch_name()}")
>>> print(f"current batch id: {citros.get_batch_id()}")
```
```text
current batch name: spectroscopy
current batch id: 00000000-1111-2222-3333-444444444444
```
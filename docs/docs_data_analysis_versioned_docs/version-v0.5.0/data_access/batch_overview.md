---
toc_max_heading_level: 4
hide_title: true
sidebar_position: 3
sidebar_label: 'Batch overview'
---

## Batch overview

Different simulations are identified by their *sid* numbers, with each step of the simulation being sequentially numbered by *rid*. Batches typically containe multiple topics that encapsulate related datasets.

To get the information about all the existing batches the method [**batch_info**](#batch-information) is used. The batch is set when the [**CitrosDB**](getting_started.md#connection-to-the-database) object is created or by [**batch()**](#setting-batch) method. To display the sizes of all batches within the database or the size of the current batch, the methods [**get_batch_size()**](#batch-size) and [**get_current_batch_size**](#current-batch-size) are employed, respectively. Methods [**get_batch()** and **get_batch_id()**](#current-batch-name-and-id) return the name and the id of the current batch, if it was set previously.

Each batch contains the following columns:

||user\_id | sid | rid | time | topic | type| data |
|--|--|--|--|--|--|--|--|
|description |user name | simulation id| run id| ros time message | topic name| type name | json-format data|
|type| uuid | int | int | big int | str | str | jsonb|

Batch may have several *topic*s - to list them along with structure of the json-data column for the current batch the method [**get_data_structure()**](batch_content.md#data-structure) is used.

Each simulation in the batch has its own id - *sid*, and each message in the simulation is enumerated by run id - *rid*.

If there are infinite values in the data, they are stored as $\pm 10^{308}$.

### Batch information

Method [**batch_info**](../documentation/data_access/citros_db.md#citros_data_analysis.data_access.citros_db.CitrosDB.batch_info) is applied to show the general information about batches: its name, batch id, list of simulation ids (sids) and when the batch was created. The result is a [**CitrosDict**](../documentation/data_access/citros_dict.md#citros_data_analysis.data_access.citros_dict.CitrosDict) object, that inherits behaviour of an ordinary python dictionary, but has some additional methods, like [**print()**](../documentation/data_access/citros_dict.md#citros_data_analysis.data_access.citros_dict.CitrosDict.print) method. To display the information about all the existing batches adopt the following:

```python
>>> citros.batch_info().print()
```
```js
{
  'kinematics': {
    'batch_id': '00000000-aaaa-1111-2222-333333333333',
    'sid': [1, 2, 3, 4, 5],
    'created_at': '2023-06-14T11:44:31.728585+00:00',
    'updated_at': '2023-06-14T11:44:31.728585+00:00',
    'status': 'DONE',
    'tag': 'latest',
    'simulation': 'simulation_parameters',
    'message': 'launch_params',
    'parallelism': 1,
    'completions': 1,
    'cpu': 2,
    'gpu': 0,
    'memory': '265',
    'repo': 'citros_project'
  },
  'kinematics_2': {
    'batch_id': '00000000-bbbb-1111-2222-333333333333',
    'sid': [0, 1, 2, 3],
    'created_at': '2023-06-21T13:51:47.29987+00:00',
    ...
  },
  'dynamics': {
    'batch_id': '00000000-dddd-1111-2222-333333333333',
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
>>> print(citros.batch_info())
{'kinematics': {'batch_id': ...}, 'kinematics_2': {'batch_id': ...}, 'dynamics': {'batch_id': ...}}
```

[**CitrosDict**](../documentation/data_access/citros_dict.md#citros_data_analysis.data_access.citros_dict.CitrosDict) object can be converted to json string by the method [**to_json()**](../documentation/data_access/citros_dict.md#citros_data_analysis.data_access.citros_dict.CitrosDict.to_json):
```python
>>> print(citros.batch_info().to_json())
```
```js
{
  "kinematics": {
    "batch_id": "00000000-aaaa-1111-2222-333333333333",
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
    "batch_id": "00000000-bbbb-1111-2222-333333333333",
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
    "batch_id": "00000000-dddd-1111-2222-333333333333",
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
>>> citros.batch_info(sid_status = 'DONE')
```

There are several options that allows to search for the exact batch. Passing a string that matches the batch name, the search will yield all batches whose names correspond to the provided string:

```python
>>> citros.batch_info('kinematics').print()
```
```js
{
  'kinematics': {
    'batch_id': '00000000-aaaa-1111-2222-333333333333',
    'sid': [1, 2, 3, 4, 5],
    'created_at': '2023-06-14T11:44:31.728585+00:00',
    ...
  },
  'kinematics_2': {
    'batch_id': '00000000-bbbb-1111-2222-333333333333',
    'sid': [0, 1, 2, 3],
    'created_at': '2023-06-21T13:51:47.29987+00:00',
    ...
  },
}
```

If the batch id is know, it can be provided as an argument to query information about this exact batch:

```python
>>> citros.batch_info('00000000-dddd-1111-2222-333333333333').print()
```
```js
{
  'dynamics': {
    'batch_id': '00000000-dddd-1111-2222-333333333333',
    'sid': [1, 3, 2],
    'created_at': '2023-06-21T15:03:07.308498+00:00',
    ...
  }
}
```

Or it is possible to select the last created batch by passing int value -1:

```python
>>> citros.batch_info(-1).print()
```
```js
{
  'dynamics': {
    'batch_id': '00000000-dddd-1111-2222-333333333333',
    'sid': [1, 3, 2],
    'created_at': '2023-06-21T15:03:07.308498+00:00',
    ...
  }
}
```

To retrieve the second-to-last created batch, provide -2 as an argument. Similarly, to select the batch created first, use 0; for the second batch created, use 1, and so forth.

To search by another field, provide it in `search_by` field along with the appropriate format for the `search` argument. To find batches with an exact match in the 'simulation', 'status', 'tag', and 'message' fields, simply provide the word as a string:

```python
>>> citros.batch_info('launch', search_by = 'message').print()
```
```js
{
  'kinematics': {
    'batch_id': '00000000-aaaa-1111-2222-333333333333',
    'sid': [1, 2, 3, 4, 5],
    'created_at': '2023-06-14T11:44:31.728585+00:00',
    'updated_at': '2023-06-14T11:44:31.728585+00:00',
    'status': 'DONE',
    'tag': 'latest',
    'simulation': 'simulation_parameters',
    'message': 'launch_params',
    'parallelism': 1,
    'completions': 1,
    'cpu': 2,
    'gpu': 0,
    'memory': '265',
    'repo': 'citros_project'
  }
}
```

Similarly, provide `search` argument as int for 'parallelism', 'completions' and 'memory' fields and as float for 'cpu' and 'gpu' fields:

```python
>>> citros.batch_info(2, search_by = 'parallelism').print()
```
```js
{
 'kinematics_2': {
  'batch_id': '00000000-bbbb-1111-2222-333333333333',
  'sid': [0, 1, 2, 3],
  'created_at': '2023-06-21T13:51:47.29987+00:00',
  'updated_at': '2023-06-21T13:51:47.29987+00:00',
  'status': 'DONE',
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
>>> citros.batch_info('20-06', search_by = 'created_after').print()
```
```js
{
 'kinematics_2': {
    'batch_id': '00000000-bbbb-1111-2222-333333333333',
    'sid': [0, 1, 2, 3],
    'created_at': '2023-06-21T13:51:47.29987+00:00',
    ...
  },
  'dynamics': {
    'batch_id': '00000000-dddd-1111-2222-333333333333',
    'sid': [1, 3, 2],
    'created_at': '2023-06-21T15:03:07.308498+00:00',
    ...
  }
}
```

To get the information about the batches that were updated before 9:00 today, do the following:

```python
>>> citros.batch_info('9:00', search_by = 'updated_before').print()
```
```js
{
  'kinematics': {
    'batch_id': '00000000-aaaa-1111-2222-333333333333',
    'sid': [1, 2, 3, 4, 5],
    'created_at': '2023-06-14T11:44:31.728585+00:00',
    ...
  },
  'kinematics_2': {
    'batch_id': '00000000-bbbb-1111-2222-333333333333',
    'sid': [0, 1, 2, 3],
    'created_at': '2023-06-21T13:51:47.29987+00:00',
    ...
  },
  'dynamics': {
    'batch_id': '00000000-dddd-1111-2222-333333333333',
    'sid': [1, 3, 2],
    'created_at': '2023-06-21T15:03:07.308498+00:00',
    ...
  }
}
```

The `order_by` argument enables to choose the order of the output by one of the field. To display the output in ascending order by one or more fields, list them in `order_by` argument. If the field is the only one, it may be passed directly as a str, for example, to order the output of the previous example in asccending order by name of the batches:

```python
>>> citros.batch_info('9:00', search_by = 'updated_before', order_by = 'name').print()
```
```js
{
  'dynamics': {
    'batch_id': '00000000-dddd-1111-2222-333333333333',
    'sid': [1, 3, 2],
    'created_at': '2023-06-21T15:03:07.308498+00:00',
    ...
  },
  'kinematics': {
    'batch_id': '00000000-aaaa-1111-2222-333333333333',
    'sid': [1, 2, 3, 4, 5],
    'created_at': '2023-06-14T11:44:31.728585+00:00',
    ...
  },
  'kinematics_2': {
    'batch_id': '00000000-bbbb-1111-2222-333333333333',
    'sid': [0, 1, 2, 3],
    'created_at': '2023-06-21T13:51:47.29987+00:00',
    ...
  }
}
```

To indicate the desired order, whether descending or ascending, you can pass an argument as a dictionary. For instance, to arrange the output based on the creation time in descending order, placing the most recent first, use the following:

```python
>>> citros.batch_info('11:00', search_by = 'updated_before', order_by = {'created_at': 'desc'}).print()
```
```js
{
  'dynamics': {
    'batch_id': '00000000-dddd-1111-2222-333333333333',
    'sid': [1, 3, 2],
    'created_at': '2023-06-21T15:03:07.308498+00:00',
    ...
  },
   'kinematics_2': {
    'batch_id': '00000000-bbbb-1111-2222-333333333333',
    'sid': [0, 1, 2, 3],
    'created_at': '2023-06-21T13:51:47.29987+00:00',
    ...
  }
  'kinematics': {
    'batch_id': '00000000-aaaa-1111-2222-333333333333',
    'sid': [1, 2, 3, 4, 5],
    'created_at': '2023-06-14T11:44:31.728585+00:00',
    ...
  }
}
```

By default, the displayed batches include all batches, regardless of their creator. You can limit the display to only show batches that belong to you by setting `user`` to 'me':

```python
>>> citros.batch_info('kinematics', user = 'me').print()
```
```js
{
  'kinematics': {
    'batch_id': '00000000-aaaa-1111-2222-333333333333',
    'sid': [1, 2, 3, 4, 5],
    'created_at': '2023-06-14T11:44:31.728585+00:00',
    ...
  }
}
```

### Setting batch

The batch is set either when [**CitrosDB**](getting_started.md#connection-to-the-database) object is created (by passing an argument `batch` or automatically, getting id from the environment variable `bid`) or by method [**batch()**](../documentation/data_access/citros_db.md#citros_data_analysis.data_access.citros_db.CitrosDB.batch). 

If the exact batch id is known, it may be passed in the following way:

```python
>>> citros = da.CitrosDB()
>>> citros = citros.batch('00000000-1111-2222-3333-444444444444')
```

By default, method [**batch()**](../documentation/data_access/citros_db.md#citros_data_analysis.data_access.citros_db.CitrosDB.batch) returns [**CitrosDB**](getting_started.md#connection-to-the-database) object with set `batch` parameter, which then can be used in a chain, for example, to [query data](query_data.md#query-data). Alternatively, the batch may be set to the existing [**CitrosDB**](getting_started.md#connection-to-the-database) object if the parameter `inplace` = True:

```python
>>> citros = da.CitrosDB()
>>> print(f"current batch name: {citros.get_batch()}")
>>> print(f"current batch id: {citros.get_batch_id()}")
```
```text
current batch name:
current batch id:
```
```python
>>> citros.batch('00000000-1111-2222-3333-444444444444', inplace = True)
>>> print(f"current batch name: {citros.get_batch()}")
>>> print(f"current batch id: {citros.get_batch_id()}")
```
```text
current batch name: spectroscopy
current batch id: 00000000-1111-2222-3333-444444444444
```

The name and the id of the current batch may be obtained by **get_batch()** and **get_batch_id()** [methods](#current-batch-name-and-id).

Similar to the [**batch_info**](#batch-information), you can also set the batch using its name:

```python
>>> citros = citros.batch('kinematics')
```

or by its order of the creation:

```python
>>> citros = citros.batch(-1)
```

In the above example, the most recently created batch is assigned. If the provided batch name has multiple matches, the clarification may be needed. This can be easily achieved by checking the list of batches by [**batch_info**](#batch-information) method.

### Current batch name and id

Name of the current batch and its id may be retrieved by [**get_batch()**](../documentation/data_access/citros_db.md#citros_data_analysis.data_access.citros_db.CitrosDB.get_batch) and [**get_batch_id()**](../documentation/data_access/citros_db.md#citros_data_analysis.data_access.citros_db.CitrosDB.get_batch_id) methods correspondingly:

```python
>>> citros.batch('spectroscopy', inplace = True)
>>> print(f"current batch name: {citros.get_batch()}")
>>> print(f"current batch id: {citros.get_batch_id()}")
```
```text
current batch name: spectroscopy
current batch id: 00000000-1111-2222-3333-444444444444
```

### Batch size

To check the batch sizes in the current schema method [**get_batch_size()**](../documentation/data_access/citros_db.md#citros_data_analysis.data_access.citros_db.CitrosDB.get_batch_size) is used:

```python
>>> citros.get_batch_size()
```
The result is a table that contains batch names, batch ids, batch sizes and total sizes with indexes. The output might look something like this:

```text
+--------------+--------------------------------------+------------+------------+
| batch        | batch id                             | size       | total size |
+--------------+--------------------------------------+------------+------------+
| spectroscopy | 00000000-1111-2222-3333-444444444444 | 32 kB      | 64 kB      |
| photometry   | 00000000-aaaa-2222-3333-444444444444 | 8192 bytes | 16 kB      |
+--------------+--------------------------------------+------------+------------+
```

### Current batch size

Similar to [**get_batch_size()**](#batch-size) method, [**get_current_batch_size()**](../documentation/data_access/citros_db.md#citros_data_analysis.data_access.citros_db.CitrosDB.get_batch_size) method is used, with the difference that it shows the size for the current batch (if it is set):

```python
>>> citros.batch('photo').get_current_batch_size()
```
The result is a table that contains batch names, batch sizes and total sizes with indexes. The output might look something like this:

```text
+--------------+--------------------------------------+------------+------------+
| batch        | batch id                             | size       | total size |
+--------------+--------------------------------------+------------+------------+
| photometry   | 00000000-aaaa-2222-3333-444444444444 | 8192 bytes | 16 kB      |
+--------------+--------------------------------------+------------+------------+
```

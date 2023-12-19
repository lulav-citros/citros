---
toc_max_heading_level: 4
sidebar_label: 'Getting Started: Query Data'
hide_title: true
sidebar_position: 1
description: 'Quick start'
---
# Getting Started: Query Data

For performing error analysis module [error_analysis](../documentation/error_analysis/citros_data.md) is used. To download module:

```python
from citros_data_analysis import error_analysis as analysis
```

But first of all, let's have a quick look at [data_access](../documentation/data_access/citros_db.md) module, which is dedicate to query data.

## Query Data

To get access to a Citros database, create [**CitrosDB**](../documentation/data_access/citros_db.md#citros_data_analysis.data_access.citros_db.CitrosDB) object:

```python
from citros_data_analysis import data_access as da

>>> citros = da.CitrosDB()
```
This way [**CitrosDB**](../documentation/data_access/citros_db.md#citros_data_analysis.data_access.citros_db.CitrosDB) is created with defaults parameters. To specify connection parameters, pass corresponding arguments:

```python
>>> citros = da.CitrosDB(host = 'hostName',
                         user = 'user',
                         password = 'myPassword',
                         database = 'myDatabase',
                         schema = 'mySchema',
                         batch = batchName,
                         port = '5432')
```

Data is always queried for exact topic. For example, to query all data for topic 'A':

```python
>>> df = citros.topic('A').data()
>>> print(df)
```
<details>
    <summary>Show the result:</summary>

||sid	|rid	|time	|topic	|type	|data.x.x_1	|data.x.x_2	|data.x.x_3	|data.time	|data.time	|data.y
|--|--|--|--|--|--|--|--|--|--|--|--|
0	|3	|0	|105036927	|A	|a	|-0.080	|-0.002	|17.70	|0.3	|0.3	|[2, 28, 45]
1	|1	|0	|312751159	|A	|a	|0.000	|0.080	|154.47	|10.0	|10.0	|[15, 41, 43]
...|...|...|...|...|...|...|...|...|...|...|...
</details>

The result is a [**DataFrame**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) of the [**pandas** package](https://pandas.pydata.org/).

Batch consists of two parts: json-data column, and all other columns.
To query exact json-objects, pass list with their labels to [**data()**](../documentation/data_access/citros_db.md#citros_data_analysis.data_access.citros_db.CitrosDB.data).
For example, if the json-data column looks like:

```js
data
{'x': {'x_1' : 1, 'x_2' : 12, 'x_3' : 70}, 'y': [5.0, 3.4, 10], 'height' : 12}
{'x': {'x_1' : 5, 'x_2' : 10, 'x_3' : 73}, 'y': [5.5, 6.7, 50], 'height' : 11}
...
```
to query 'x_1', 'x_2', 'height' and values from the first position of 'y' json-array, the following code may be used:
```python
>>> df = citros.topic('A').data(['data.x.x_1', 'data.x.x_2', 'data.height', 'data.y[0]'])
```

Also, different constraints may be applied to query, see [examples of data_access module](../data_access/).
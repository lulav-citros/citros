---
toc_max_heading_level: 4
sidebar_label: 'Getting Started'
hide_title: true
sidebar_position: 1
description: 'Quick start'
---
# Getting Started

The [**validation**](../documentation/validation/validation.md) module provides a set of tests check the simulation results. These tests include:

 - [**std_bound_test()**](../documentation/validation/validation.md#citros_data_analysis.validation.validation.Validation.std_bound_test) - verifies whether the n-$\sigma$ standard deviation boundary falls within the specified limits;

 - [**mean_test()**](../documentation/validation/validation.md#citros_data_analysis.validation.validation.Validation.mean_test) - checks if the mean value is within the given limits;

 - [**std_test()**](../documentation/validation/validation.md#citros_data_analysis.validation.validation.Validation.std_test) - verifies whether the n-$\sigma$ standard deviation is less then the given limit;

 - [**sid_test()**](../documentation/validation/validation.md#citros_data_analysis.validation.validation.Validation.sid_test) - examines if the simulation values do not exceed the limits;

 - [**norm_test**](../documentation/validation/validation.md#citros_data_analysis.validation.validation.Validation.norm_test) - evaluates norm of each simulation and compares it with the specified limit;

Number and type of tests may be set by [**set_tests()**](../documentation/validation/validation.md#citros_data_analysis.validation.validation.Validation.set_tests) method that allows to specify the desired tests by providing their names and corresponding parameters and produces a consolidated report.

## Query and Prepare Data

To connect to the database [**CitrosDB**](../documentation/data_access/citros_db.md#citros_data_analysis.data_access.citros_db.CitrosDB) object is created:
```python
from citros_data_analysis import data_access as da

>>> citros = da.CitrosDB()
```
To learn more about connection parameters, see [examples of data_access module](../data_access/getting_started.md).

Let's assume, that data for topic 'A' looks like:

||sid	|rid	|time	|topic	|type	|data
|--|--|--|--|--|--|--
0	|1	|0	|312751159	|A	|a	|{'x': {'x_1': 0.0, 'x_2': 0.08, 'x_3': 154.47}, 'time': 10.0}
1	|1	|1	|407264008	|A	|a	|{'x': {'x_1': 0.008, 'x_2': 0.08, 'x_3': 130.97}, 'time': 17.9}
2	|1	|2	|951279608	|A	|a	|{'x': {'x_1': 0.016, 'x_2': 0.078, 'x_3': 117.66}, 'time': 20.3}
...|...|...|...|...|...|...|

A json-data column contains information about time and vector x, that has elements x_1, x_2 and x_3. Let's query these columns:

```python
>>> df = citros.topic('A').data(['data.x', 'data.time'])
```
The output is a [**pandas.DataFrame**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html):

||sid	|rid	|time	|topic	|type	|data.x|	data.time
|--|--|--|--|--|--|--|--|
0	|1	|0	|312751159	|A	|a	|{'x_1': 0.0, 'x_2': 0.08, 'x_3': 154.47}	|10.0
1	|1	|1	|407264008	|A	|a	|{'x_1': 0.008, 'x_2': 0.08, 'x_3': 130.97}	|17.9
2	|1	|2	|951279608	|A	|a	|{'x_1': 0.016, 'x_2': 0.078, 'x_3': 117.66}	|20.3
...|...|...|...|...|...|...|...

Analysis of data from multiple simulations may be performed if the correspondence between data values from different simulation is set. It may be done through an independent variable that is shared between simulations. Indexes are assigned based on this variable, connecting data values across the simulations.

There are two methods to handle index assignment:

 - to divides the independent variable into `num` ranges, assign an index to each interval, and calculate data value averages for each simulation within each range (see [**bin_data()**](../documentation/error_analysis/citros_data.md#citros_data_analysis.error_analysis.citros_data.CitrosData.bin_data))
 - to scale for each simulation the independent variable to the interval [0,1], defines `num` uniformly distributed points from 0 to 1, and interpolates data points over this new interval (see [**scale_data()**](../documentation/error_analysis/citros_stat.md#citros_data_analysis.error_analysis.citros_data.CitrosData.scale_data)).

This preparation may be done by creating [**Validation**](../documentation/validation/validation.md#citros_data_analysis.validation.validation.Validation) object, that is able to apply mentioned above approaches to assign indexes and to calculate statistics over different simulations. Let's choose 'data.time' as an independent variable and use it to assign indexes and connect 'data.x' values of different simulations. The method of index setting is specified by `method`: 'scale' or 'bin', the number of points (bins) is passed by `num`:

```python
from citros_data_analysis import validation as va

>>> V = va.Validation(df, data_label = ['data.x'], param_label = 'data.time', 
                  method = 'scale', num = 20, units = 'm')
```
`units` are specified to make plots more informative.

If only some of the elements of the vector 'data.x' are needed, for example 'data.x.x_1' and 'data.x.x_2', they may be queried and passed to [**Validation**](../documentation/validation/validation.md#citros_data_analysis.validation.validation.Validation) object as follows:

```python
>>> df = citros.topic('A').data(['data.x.x_1', 'data.x.x_2', 'data.time'])
>>> V = va.Validation(df, data_label = ['data.x.x_1', 'data.x.x_2'], param_label = 'data.time', 
                      method = 'scale', num = 20, units = 'm')
```

After initialization, [**Validation**](../documentation/validation/validation.md#citros_data_analysis.validation.validation.Validation) object stores statistics as a [**CitrosStat**](../documentation/error_analysis/citros_stat.md#citros_data_analysis.error_analysis.citros_stat.CitrosStat) in `stat` attribute. For example, to get mean values:

```python
>>> print(V.stat.mean)
```
```js
              data.x.x_1   data.x.x_2   data.x.x_3
data.time_id
0             -0.045667    0.044667     93.706667
1             0.007875     0.069515     95.639414
2             0.056261     0.043401     33.128443
...           ...          ...          ...
```
In the same way it is possible to access scaled 'data.time' range (`V.stat.x`), standard deviation (`V.stat.sigma`) and covariant matrix (`V.stat.covar_matrix`).
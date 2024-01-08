---
# Display h3 headings
sidebar_label: 'Class Validation'
toc_max_heading_level: 3
hide_title: true
description: 'Documentation'
---

# Class Validation







    
## Class `Validation` {#validation.validation.Validation}





```python
class Validation(
    df=None,
    data_label=None,
    param_label=None,
    method='scale',
    num=100,
    units='',
    omit_nan_rows=True,
    inf_vals=1e+308
)
```


<details>
  <summary>Description</summary>

Validation class.

#### Parameters

Name|Type|Description
--|--|--
|**```df```**|**pandas.DataFrame**|Data table to perform validation tests on.
|**```data_label```**|**str** or **list** of **str**|Specifies the label(s) of the data column(s) in data table.
|**```param_label```**|**str**|Specifies the label of the column used to calculate the indices.
|**```method```**|`{'scale', 'bin'}`, default `'scale'`|Method of data preparation: scaling to [0,1] interval or binning.
|**```num```**|**int**, default **100**|Number of points in a new scale that will be used for interpolation if the **method** is 'scale'<br />    or number of bins if the **method** is 'bin'.
|**```units```**|**str**, optional|Specifies units of the data.
|**```omit_nan_rows```**|**bool**|If True, rows with one or more NaN values will be omitted from the analysis.<br />    If not specified, considered to be True.
|**```inf_vals```**|**None** or **float**, default **1e308**|If specified, all values from **data_label** column that exceed the provided value in absolute terms<br />    will be treated as NaN values. If this functionality is not required, set inf_vals = None.
#### Attributes

Name|Type|Description
--|--|--
|**```df```**|**pandas.DataFrame** or **None**|Data table to perform validation tests on.
|**```db```**|**[CitrosData](../analysis/citros_data.md#analysis.citros_data.CitrosData "analysis.citros_data.CitrosData")** or **None**|CitrosData object after binning or scaling.
|**```stat```**|**[CitrosStat](../analysis/citros_stat.md#analysis.citros_stat.CitrosStat "analysis.citros_stat.CitrosStat")** or **None**|CitrosStat object that stores mean, standard deviation and covariance matrix as attributes.

</details>
<details>
  <summary>Examples</summary>

Import Validation and CitrosDB:

```python
>>> from citros import CitrosDB, Validation
```


From the batch 'albedo' of the simulation 'planetary_nebula' from the json-data column of the topic 'A' 
download simulated data labeled as 'data.x.x_1' and column with time 'data.time'.

```python
>>> citros = CitrosDB(simulation = 'planetary_nebula', batch = 'albedo')
>>> df = citros.topic('A').set_order({'sid':'asc','rid':'asc'}).data(['data.x.x_1','data.time'])
>>> print(df)
    sid   rid   time        topic   type   data.x.x_1   data.time
0   1     0     312751159   A       a      0.000        10.0
1   1     1     407264008   A       a      0.008        17.9
2   1     2     951279608   A       a      0.016        20.3
```


Set 'data.time' as independent variable and 'data.x.x_1' as dependent one.
**method** defines the method of data preparation and index assignment: method = 'bin' - bins values of column **param_label** in **num** intervals,
set index to each of the interval, group data according to the binning and calculate mean data values for each group.

```python
>>> V = Validation(df, data_label = ['data.x.x_1'], param_label = 'data.time',
...                method = 'bin', num = 50, units = 'm')
```


For topic 'A' download 3-dimensional json-data 'data.x' that contains 'data.x.x_1', 'data.x.x_2' and 'data.x.x_3' columns,
and column with time 'data.time'.
```python
>>> df = citros.topic('A').set_order({'sid':'asc','rid':'asc'}).data(['data.x','data.time'])
>>> print(df['data.x'])
0          {'x_1': 0.0, 'x_2': 0.08, 'x_3': 0.047}
1       {'x_1': 0.008, 'x_2': 0.08, 'x_3': -0.003}
2      {'x_1': 0.016, 'x_2': 0.078, 'x_3': -0.034}
...
```


Set 'data.time' as independent variable and 'data.x' as dependent vector.
**method** defines the method of data preparation and index assignment: method = 'scale' - scales parameter **param_label** for each of the 'sid' to [0, 1] interval
and interpolate data on the new scale.

```python
>>> V = Validation(df, data_label = 'data.x', param_label = 'data.time',
...                method = 'scale', num = 50, units = 'm')
```

</details>









    
## Method `std_bound_test` {#validation.validation.Validation.std_bound_test}




```python
def std_bound_test(
    limits=1.0,
    n_std=3,
    nan_passed=True,
    std_color='b',
    connect_nan_std=False,
    std_area=False,
    std_lines=True
)
```


<details>
  <summary>Description</summary>

Test whether **n_std**-standard deviation boundary is within the given limits.

The output is:
- dictionary with summary of the test results, with the following structure:
```python
{
'test_param' : list,          # initial tests parameters
column_name:                  # label of the column, str
    {'passed' : bool},        # if the tests was passed or not
    {'pass_rate' : float},    # fraction of the points that pass the test
    {'failed' : 
        {x_index: x_value}},  # indexes and values of the x coordinate of 
                              #   the points that fail the test {int: float} 
    {'nan_std' :
        {x_index: x_value}}   # indexes and values of the x coordinate of the points
}                             #   that have NaN (Not a Number) values for standard deviation
```
- table that provides test results for each standard deviation boundary point, 
using a boolean value to indicate whether it passed or failed the test;

- figure with plotted simulations, mean values, standard deviation boundaries and limit boundaries;

#### Parameters

Name|Type|Description
--|--|--
|**```limits```**|**float** or **list**, default **1.0**|Limit to test standard deviation boundary. Limits may be set as:<br />      &#8226; one value and it will be treated as an +- interval: value -> [-value, value];<br />      &#8226; list of lower and upper limits: [lower_limit, upper_limit];<br />      &#8226; If the data has multiple columns, limits may be set for each of the column.<br />    That way list length must be equal to number of columns. For example, for the 3-dimensional vector with corresponding standard deviation boundaries [std_bound_1, std_bound_2, std_bound_3]:<br />    [[**limit_lower**, **limit_upper**], **value_1**, **value_2**] will be processed as: <br />    **limit_lower** < std_bound_1 < **limit_upper**,<br />    -**value_1** < std_bound_2 < **value_1**,<br />    -**value_2** < std_bound_2 < **value_2**.
|**```n_std```**|**int**, default **3**|The parameter specifies the number of standard deviations to be within limits.
|**```nan_passed```**|**bool**, default **True**|If True, the NaN values of standard deviation will pass the test.
#### Returns

Name|Type|Description
--|--|--
|**```log```**|**[CitrosDict](../access/citros_dict.md#access.citros_dict.CitrosDict "access.citros_dict.CitrosDict")**|Dictionary with validation test results.
|**```table```**|**pandas.DataFrame**|Table with test results for each of the standard deviation boundary point, indicating whether it passes or fails the test.
|**```fig```**|**matplotlib.figure.Figure**|Figure with plotted simulations, mean values, standard deviation boundaries and limit boundaries.
#### Other Parameters

Name|Type|Description
--|--|--
|**```std_color```**|**str**, default `'b'`|Color for displaying standard deviations, blue by default.
|**```connect_nan_std```**|**bool**, default **False**|If True, all non-NaN values in standard deviation boundary line are connected, resulting in a continuous line. <br />    Otherwise, breaks are introduced in the standard deviation line whenever NaN values are encountered.
|**```std_area```**|**bool**, default **False**|Fill area within **n_std**-standard deviation lines with color.
|**```std_lines```**|**bool**, default **True**|If False, remove standard deviation boundary lines.
#### See Also

**pandas.DataFrame**, **pandas.Series**


</details>
<details>
  <summary>Examples</summary>

Import Validation and CitrosDB:

```python
>>> from citros import CitrosDB, Validation
```


From the batch 'density' of the simulation 'diffuse_nebula' from the topic 'A' download 2 columns of the simulated data 
labeled 'data.x.x_1' and 'data.x.x_2' and column with time 'data.time'.
Set 'data.time' as independent variable and 'data.x.x_1' and 'data.x.x_2' as dependent 2-dimensional vector.
**method** defines the method of data preparation and index assignment: method = 'bin' - bins values of column **param_label** in **num** intervals, 
set index to each of the interval, group data according to the binning and calculate mean data values for each group.

```python
>>> citros = CitrosDB(simulation = 'diffuse_nebula', batch = 'density')
>>> df = citros.topic('A').set_order({'sid':'asc','rid':'asc'})\
...                       .data(['data.x.x_1','data.x.x_2','data.time'])
>>> V = Validation(df, data_label = ['data.x.x_1', 'data.x.x_2'], param_label = 'data.time', 
...                method = 'bin', num = 50, units = 'm')
```


Test whether 3-sigma standard deviation boundary is within interval [-0.3, 0.3] (treat nan values of the
standard deviation, if they exist, as passing the test):

```python
>>> log, table, fig = V.std_bound_test(limits = 0.3, n_std = 3, nan_passed = True)
>>> log.print()
std_bound_test: passed
{
 'test_param': {
   'limits': 0.3,
   'n_std': 3,
   'nan_passed': True
 },
 'data.x.x_1': {
   'passed': True,
   'pass_rate': 1.0,
   'failed': {
   },
   'nan_std': {
     49: 807.942
   }
 },
 'data.x.x_2': {
   'passed': True,
   'pass_rate': 1.0,
   'failed': {
   },
   'nan_std': {
     49: 807.942
   }
 }
}
```


The same, but set limit interval to be [-1, 0.3]:

```python
>>> log, table, fig = V.std_bound_test(limits = [-1, 0.3], n_std = 3, nan_passed = True)
std_bound_test: passed
```


Set different limits for 1-sigma standard deviation boundaries of 2-dimensional vector: for the first 
element of the vector boundaries should be within interval [-1, 2] and for the second one - [-0.5, 0.5]:

```python
>>> log, table, fig = V.std_bound_test(limits = [[-1, 2], 0.5], n_std = 1)
std_bound_test: passed
```


The same as in the previous example, but limits should be [-1, 1] for the first element of the vector 
and [-0.5, 0.5] for the second. In this case limits should be set as [[-1, 1], [-0.5, 0.5]] and not as [1, 0.5],
because in the latter case limits will be treated as a common boundary for both elements.

```python
>>> log, table, fig = V.std_bound_test(limits = [[-1, 1], [-0.5, 0.5]], n_std = 1)
std_bound_test: passed
```


Download 3-dimensional json-data 'data.x' that contains 'data.x.x_1', 'data.x.x_2' and 'data.x.x_3' columns, and column with time 'data.time'.
Set 'data.time' as independent variable and 'data.x' as dependent vector.
**method** defines the method of data preparation and index assignment: method = 'scale' - scales parameter **param_label** for each of the 'sid' to [0, 1] interval 
and interpolate data on the new scale.

```python
>>> df = citros.topic('A').set_order({'sid':'asc','rid':'asc'}).data(['data.x','data.time'])
>>> V3 = Validation(df, data_label = 'data.x', param_label = 'data.time', 
...                 method = 'scale', num = 50, units = 'm')
```


Set different limits on 3-dimensional vector: [-0.5, 0.5] for the first element, [-1.5, 1.5] for the second,
[-20, 10] for the third:

```python
>>> log, table, fig = V3.std_bound_test(limits = [0.5, 1.5, [-20, 10]], n_std = 3)
std_bound_test: passed
```

</details>


    
## Method `mean_test` {#validation.validation.Validation.mean_test}




```python
def mean_test(
    limits=1.0,
    nan_passed=True
)
```


<details>
  <summary>Description</summary>

Test whether mean is within the given limits.

The output is:
- dictionary with summary of the test results, with the following structure:
```python
{
'test_param' : list,          # initial tests parameters
column_name:                  # label of the column, str
    {'passed' : bool},        # if the tests was passed or not.
    {'pass_rate' : float},    # fraction of the points that pass the test
    {'failed' : 
        {x_index: x_value}},  # indexes and values of the x coordinate of the 
}                             #   points that fail the test {int: float}   
```

- table that provides test results for each of the mean point, 
using a boolean value to indicate whether it passed or failed the test;

- figure with plotted simulations, mean values and limit boundaries.

#### Parameters

Name|Type|Description
--|--|--
|**```limits```**|**float** or **list**, default **1.0**|Limit to test mean. Limits may be set as:<br />      &#8226; one value and it will be treated as an +- interval: value -> [-value, value];<br />      &#8226; list of lower and upper limits: [lower_limit, upper_limit];<br />      &#8226; If the data has multiple columns, limits may be set for each of the column.<br />    That way list length must be equal to number of columns. For example, for the 3-dimensional vector with corresponding mean vector [mean_1, mean_2, mean_3]:<br />    [[**limit_lower**, **limit_upper**], **value_1**, **value_2**] will be processed as: <br />    **limit_lower** < mean_1 < **limit_upper**,<br />    -**value_1** < mean_2 < **value_1**,<br />    -**value_2** < mean_2 < **value_2**.
|**```nan_passed```**|**bool**, default **True**|If True, the NaN values of the mean will pass the test.
#### Returns

Name|Type|Description
--|--|--
|**```log```**|**[CitrosDict](../access/citros_dict.md#access.citros_dict.CitrosDict "access.citros_dict.CitrosDict")**|Dictionary with validation test results.
|**```table```**|**pandas.DataFrame**|Table with test results for each of the mean point, indicating whether it passes or fails the test.
|**```fig```**|**matplotlib.figure.Figure**|Figure with plotted simulations, mean values and limit boundaries.

</details>
<details>
  <summary>Examples</summary>

Import Validation and CitrosDB:

```python
>>> from citros import CitrosDB, Validation
```


From the batch 'density' of the simulation 'diffuse_nebula' from the topic 'A' download 2 columns of the simulated data 
labeled 'data.x.x_1' and 'data.x.x_2' and column with time 'data.time'.
Set 'data.time' as independent variable and 'data.x.x_1' and 'data.x.x_2' as dependent 2-dimensional vector.
**method** defines the method of data preparation and index assignment: method = 'bin' - bins values of column **param_label** in **num** intervals, 
set index to each of the interval, group data according to the binning and calculate mean data values for each group.

```python
>>> citros = CitrosDB(simulation = 'diffuse_nebula', batch = 'density')
>>> df = citros.topic('A').set_order({'sid':'asc','rid':'asc'})\
...                       .data(['data.x.x_1','data.x.x_2','data.time'])
>>> V = Validation(df, data_label = ['data.x.x_1', 'data.x.x_2'], param_label = 'data.time', 
...                method = 'bin', num = 50, units = 'm')
```


Test whether mean values are is within the  interval [-10, 10]:

```python
>>> log, table, fig = V.mean_test(limits = 10)
>>> log.print()
mean_test: passed
{
 'test_param': {
   'limits': 10
 },
 'data.x.x_1': {
   'passed': True,
   'pass_rate': 1.0,
   'failed': {
   }
 },
 'data.x.x_2': {
   'passed': True,
   'pass_rate': 1.0,
   'failed': {
   }
 }
}
```


The same, but set limit interval to be [-0.5, 0.8]:

```python
>>> log, table, fig = V.mean_test(limits = [-0.5, 0.8])
mean_test: passed
```


Set different limits on mean values for each of the 1-dimensional element of the 2-dimensional vector: 
[-0.05, 0.08] for the first element and [-0.5, 0.5] for the second:

```python
>>> log, table, fig = V.mean_test(limits = [[-0.05, 0.08], 0.5])
mean_test: passed
```


The same as in the previous example, but limits should be [-1, 1] for the first element of the vector 
and [-0.5, 0.5] for the second. In this case limits should be set as [[-1, 1], [-0.5, 0.5]] and not as [1, 0.5],
because in the latter case limits will be treated as a common boundary for both elements.

```python
>>> log, table, fig = V.mean_test(limits = [[-1, 1], [-0.5, 0.5]])
mean_test: passed
```


Download 3-dimensional json-data 'data.x' that contains 'data.x.x_1', 'data.x.x_2' and 'data.x.x_3' columns, and column with time 'data.time'.
Set 'data.time' as independent variable and 'data.x' as dependent vector.
**method** defines the method of data preparation and index assignment: method = 'scale' - scales parameter **param_label** for each of the 'sid' to [0, 1] interval 
and interpolate data on the new scale.

```python
>>> df = citros.topic('A').set_order({'sid':'asc','rid':'asc'}).data(['data.x','data.time'])
>>> V3 = Validation(df, data_label = 'data.x', param_label = 'data.time', 
...                 method = 'scale', num = 50, units = 'm')
```


Set different limits on 3-dimensional vector: [-0.5, 0.5] for the first element, [-1.5, 1.5] for the second,
[-20, 10] for the third:

```python
>>> log, table, fig = V3.mean_test(limits = [0.5, 1.5, [-20, 10]])
mean_test: passed
```

</details>


    
## Method `std_test` {#validation.validation.Validation.std_test}




```python
def std_test(
    limits=1.0,
    n_std=3,
    nan_passed=True,
    std_color='b',
    connect_nan_std=False,
    std_area=False,
    std_lines=True
)
```


<details>
  <summary>Description</summary>

Test whether **n_std**-standard deviation does not exceed the given limits.

The output is:
- dictionary with summary of the test results, with the following structure:
```python
{
'test_param' : list,          # initial tests parameters
column_name:                  # label of the column, str
    {'passed' : bool},        # if the tests was passed or not
    {'pass_rate' : float},    # fraction of the points that pass the test
    {'failed' : 
        {x_index: x_value}},  # indexes and values of the x coordinate of 
                              #   the points that fail the test {int: float} 
    {'nan_std' :
        {x_index: x_value}}   # indexes and values of the x coordinate of the points
}                             #   that have NaN (Not a Number) values for standard deviation
```

- table that provides test results for each standard deviation point, 
using a boolean value to indicate whether it passed or failed the test.

- figure with standard deviations and limit boundaries.

#### Parameters

Name|Type|Description
--|--|--
|**```limits```**|**float** or **list**, default **1.0**|Limit to test standard deviation. Limits may be set as:<br />      &#8226; one value;<br />      &#8226; If the data has multiple columns, limits may be set for each of the column.<br />    That way list length must be equal to number of columns. <br />    For example, in case of 3-dimensional vector with corresponding standard deviation vector = [std_1, std_2, std_3], limits = [**value_1**, **value_2**, **value_3**] will be processed as:<br />    std_1 < **value_1**,<br />    std_2 < **value_2**,<br />    std_2 < **value_3**.
|**```n_std```**|**int**, default **3**|The parameter specifies the number of standard deviations to be less then limits.
|**```nan_passed```**|**bool**, default **True**|If True, the NaN values of standard deviation will pass the test.
#### Returns

Name|Type|Description
--|--|--
|**```log```**|**[CitrosDict](../access/citros_dict.md#access.citros_dict.CitrosDict "access.citros_dict.CitrosDict")**|Dictionary with validation test results.
|**```table```**|**pandas.DataFrame**|Table with test results for each of the standard deviation point, indicating whether it passes or fails the test.
|**```fig```**|**matplotlib.figure.Figure**|Figure with standard deviations and limit boundaries.
#### Other Parameters

Name|Type|Description
--|--|--
|**```std_color```**|**str**, default `'b'`|Color for displaying standard deviation, blue by default.
|**```connect_nan_std```**|**bool**, default **False**|If True, all non-NaN values in standard deviation line are connected, resulting in a continuous line. <br />    Otherwise, breaks are introduced in the standard deviation line whenever NaN values are encountered.
|**```std_area```**|**bool**, default **False**|Fill area within **n_std**-standard deviation line with color.
|**```std_lines```**|**bool**, default **True**|If False, remove standard deviation line.
#### See Also

**pandas.DataFrame**, **pandas.Series**


</details>
<details>
  <summary>Examples</summary>

Import Validation and CitrosDB:

```python
>>> from citros import CitrosDB, Validation
```


From the batch 'density' of the simulation 'diffuse_nebula' from the topic 'A' download 2 columns of the simulated data 
labeled 'data.x.x_1' and 'data.x.x_2' and column with time 'data.time'.
Set 'data.time' as independent variable and 'data.x.x_1' and 'data.x.x_2' as dependent 2-dimensional vector.
**method** defines the method of data preparation and index assignment: method = 'bin' - bins values of column **param_label** in **num** intervals, 
set index to each of the interval, group data according to the binning and calculate mean data values for each group.

```python
>>> citros = CitrosDB(simulation = 'diffuse_nebula', batch = 'density')
>>> df = citros.topic('A').set_order({'sid':'asc','rid':'asc'})\
...                       .data(['data.x.x_1','data.x.x_2','data.time'])
>>> V = Validation(df, data_label = ['data.x.x_1', 'data.x.x_2'], param_label = 'data.time', 
...                method = 'bin', num = 50, units = 'm')
```


Test whether 3-sigma standard deviation is within interval [-0.3, 0.3] (treat nan values of the
standard deviation, if they exist, as passing the test):

```python
>>> log, table, fig = V.std_test(limits = 1.5, n_std = 3, nan_passed = True)
>>> log.print()
std_bound_test: passed
{
 'test_param': {
   'limits': 0.3,
   'n_std': 3,
   'nan_passed': True
 },
 'data.x.x_1': {
   'passed': True,
   'pass_rate': 1.0,
   'failed': {
   },
   'nan_std': {
     49: 807.942
   }
 },
 'data.x.x_2': {
   'passed': True,
   'pass_rate': 1.0,
   'failed': {
   },
   'nan_std': {
     49: 807.942
   }
 }
}
```


Download 3-dimensional json-data 'data.x' that contains 'data.x.x_1', 'data.x.x_2' and 'data.x.x_3' columns, and column with time 'data.time'.
Set 'data.time' as independent variable and 'data.x' as dependent vector.
**method** defines the method of data preparation and index assignment: method = 'scale' - scales parameter **param_label** for each of the 'sid' to [0, 1] interval 
and interpolate data on the new scale.

```python
>>> df = citros.topic('A').set_order({'sid':'asc','rid':'asc'}).data(['data.x','data.time'])
>>> V3 = Validation(df, data_label = 'data.x', param_label = 'data.time', 
...                 method = 'scale', num = 50, units = 'm')
```


Set different limits on 3-dimensional vector: 1.5 for the first element, 1.5 for the second,
30 for the third:

```python
>>> log, table, fig = V3.std_test(limits = [1.5, 1.5, 30], n_std = 3)
std_test: passed
```

</details>


    
## Method `sid_test` {#validation.validation.Validation.sid_test}




```python
def sid_test(
    limits=1.0,
    nan_passed=True
)
```


<details>
  <summary>Description</summary>

Test whether all simulations are within the given limits.

The output is:
- dictionary with summary of the test results, with the following structure:
```python
{
'test_param' : list,                # initial tests parameters
column_name:                        # label of the column, str
    {'passed' : bool},              # if the tests was passed or not.
    {'pass_rate' : 
        {'sid_fraction' : float},   # fraction of simulations that pass the test
        {sid : fraction}},          # fraction of the points that pass the test for each simulation {int: float}
    {'failed' : 
        {sid :                      # id of the simulation that contains points that failed the test
            {x_index: x_value}}},   # indexes and values of the x coordinate of the points 
}                                   #   that fail the test {int: {int: float}}
```

- table that provides test results for for each point of the simulations, 
using a boolean value to indicate whether it passed or failed the test;

- figure with plotted simulations, mean values and limit boundaries.

#### Parameters

Name|Type|Description
--|--|--
|**```limits```**|**float** or **list**, default **1.0**|Limit to test simulation results. Limits may be set as:<br />      &#8226; one value and it will be treated as an +- interval: value -> [-value, value];<br />      &#8226; list of lower and upper limits: [lower_limit, upper_limit];<br />      &#8226; If the data has multiple columns, limits may be set for each of the column.<br />    That way list length must be equal to number of columns. For example, for the 3-dimensional vector that contains v1, v2, v3 columns and numbers N simulations:<br />    [[**limit_lower**, **limit_upper**], **value_1**, **value_2**] will be processed as: <br />    **limit_lower** < v1 < **limit_upper**, <br />    -**value_1** < v2 < **value_1**, <br />    -**value_2** < v3 < **value_2** for each of the N simulations.
|**```nan_passed```**|**bool**, default **True**|If True, the NaN values will pass the test.
#### Returns

Name|Type|Description
--|--|--
|**```log```**|**[CitrosDict](../access/citros_dict.md#access.citros_dict.CitrosDict "access.citros_dict.CitrosDict")**|Dictionary with validation test results.
|**```table```**|**pandas.DataFrame**|Table with test results for each point of the simulations, indicating whether it passes or fails the test.
|**```fig```**|**matplotlib.figure.Figure**|Figure with plotted simulations, mean values and limit boundaries.

</details>
<details>
  <summary>Examples</summary>

Import Validation and CitrosDB:

```python
>>> from citros import CitrosDB, Validation
```


From the batch 'density' of the simulation 'diffuse_nebula' from the topic 'A' download 2 columns of the simulated data 
labeled 'data.x.x_1' and 'data.x.x_2' and column with time 'data.time'.
Set 'data.time' as independent variable and 'data.x.x_1' and 'data.x.x_2' as dependent 2-dimensional vector.
**method** defines the method of data preparation and index assignment: method = 'bin' - bins values of column **param_label** in **num** intervals, 
set index to each of the interval, group data according to the binning and calculate mean data values for each group.

```python
>>> citros = CitrosDB(simulation = 'diffuse_nebula', batch = 'density')
>>> df = citros.topic('A').set_order({'sid':'asc','rid':'asc'})\
                          .data(['data.x.x_1','data.x.x_2','data.time'])
>>> V = Validation(df, data_label = ['data.x.x_1', 'data.x.x_2'], param_label = 'data.time', 
...                method = 'bin', num = 50, units = 'm')
```


Test whether all simulations are is within the interval [-10, 10]:

```python
>>> log, table, fig = V.sid_test(limits = 10)
>>> log.print()
sid_test: passed
{
 'test_param': {
   'limits': 10
 },
 'data.x.x_1': {
   'passed': True,
   'pass_rate': 1.0,
   'failed': {
   }
 },
 'data.x.x_2': {
   'passed': True,
   'pass_rate': 1.0,
   'failed': {
   }
 }
}
```


The same, but set limit interval to be [-0.5, 0.8]:

```python
>>> log, table, fig = V.sid_test(limits = [-0.5, 0.8])
sid_test: passed
```


Set different limits on mean values for each of the 1-dimensional element of the 2-dimensional vector: 
[-0.05, 0.08] for the first element and [-0.5, 0.5] for the second:

```python
>>> log, table, fig = V.sid_test(limits = [[-0.05, 0.08], 0.5])
sid_test: passed
```


The same as in the previous example, but limits should be [-1, 1] for the first element of the vector 
and [-0.5, 0.5] for the second. In this case limits should be set as [[-1, 1], [-0.5, 0.5]] and not as [1, 0.5],
because in the latter case limits will be treated as a common boundary for both elements.

```python
>>> log, table, fig = V.sid_test(limits = [[-1, 1], [-0.5, 0.5]])
sid_test: passed
```


For topic 'A' download 3-dimensional json-data 'data.x' that contains 'data.x.x_1', 'data.x.x_2' and 'data.x.x_3' columns, and column with time 'data.time'.
Set 'data.time' as independent variable and 'data.x' as dependent vector.
**method** defines the method of data preparation and index assignment: method = 'scale' - scales parameter **param_label** for each of the 'sid' to [0, 1] interval 
and interpolate data on the new scale.

```python
>>> df = citros.topic('A').set_order({'sid':'asc','rid':'asc'}).data(['data.x','data.time'])
>>> V3 = Validation(df, data_label = 'data.x', param_label = 'data.time', 
...                 method = 'scale', num = 50, units = 'm')
```


Set different limits on 3-dimensional vector: [-0.5, 0.5] for the first element, [-1.5, 1.5] for the second one, an
[-20, 10] for the third vector element:

```python
>>> log, table, fig = V3.sid_test(limits = [0.5, 1.5, [-20, 10]])
sid_test: passed
```

</details>


    
## Method `norm_test` {#validation.validation.Validation.norm_test}




```python
def norm_test(
    norm_type='L2',
    limits=1.0
)
```


<details>
  <summary>Description</summary>

Test whether norm of the each simulation is less than the given limit.

The output is:
- dictionary with summary of the test results, with the following structure:
```python
{
'test_param' : list,                # initial tests parameters
column_name :                       # label of the column, str
    {'passed' : bool},              # if the tests was passed or not.
    {'pass_rate' : float}           # fraction of the simulations that pass the test
    {'norm_value' :
        {sid: value}},              # norm for each of the simulation {int: float}
    {'failed' : list}               # sid that fail the test
}
```

- table that provides test results for each simulation,
using a boolean value to indicate whether it passed or failed the test;

- figure with plotted norm value and limits.

#### Parameters

Name|Type|Description
--|--|--
|**```norm_type```**|`{'L2', 'Linf'}`, default `'L2'`|Norm type. Norm is calculated for each of the simulation. If data is a multidimensional vector, it is calculated<br />    for each simulation of the each vector element.<br />    Type of the norm:<br />      &#8226; 'L2' - Euclidean norm, square root of the sum of the squares.<br />      &#8226; 'Linf' - absolute maximum.
|**```limits```**|**float** or **list**, default **1.0**|Limits on the simulation norm. Limits may be set as:<br />      &#8226; one value;<br />      &#8226; if the data has multiple columns, limits may be set for each of the column separately as a list.<br />    That way list length must be equal to number of the columns.
#### Returns

Name|Type|Description
--|--|--
|**```log```**|**[CitrosDict](../access/citros_dict.md#access.citros_dict.CitrosDict "access.citros_dict.CitrosDict")**|Dictionary with validation test results.
|**```table```**|**pandas.DataFrame**|Table with test results for each simulation, indicating whether it passes or fails the test.
|**```fig```**|**matplotlib.figure.Figure**|Figure with plotted norm value and limits.

</details>
<details>
  <summary>Examples</summary>

Import Validation and CitrosDB:

```python
>>> from citros import CitrosDB, Validation
```


From the batch 'density' of the simulation 'diffuse_nebula' from the topic 'A' download 1 columns of the simulated data 
labeled 'data.x.x_1' and column with time 'data.time'.
Set 'data.time' as independent variable and 'data.x.x_1' as a dependent one.
**method** defines the method of data preparation and index assignment: method = 'bin' - bins values of column **param_label** in **num** intervals,
set index to each of the interval, group data according to the binning and calculate mean data values for each group.

```python
>>> citros = CitrosDB(simulation = 'diffuse_nebula', batch = 'density')
>>> df = citros.topic('A').set_order({'sid':'asc','rid':'asc'}).data(['data.x.x_1','data.time'])
>>> V = Validation(df, data_label = 'data.x.x_1', param_label = 'data.time',
...                method = 'bin', num = 50, units = 'm')
```


Test whether L2 norm for each of the simulation does not exceed 1:

```python
>>> log, table, fig = V.norm_test(norm_type = 'L2', limits = 1)
>>> log.print()
>>> print(table)
norm_test L2: passed
{
 'test_param': {
   'limits': 1
 },
 'data.x.x_1': {
   'passed': True,
   'pass_rate': 1.0,
   'norm_value': {
     1: 0.39,
     2: 0.39,
     3: 0.38
   },
   'failed': []
 },
}
>>> print(table)
     data.x.x_1
sid
1          True
2          True
3          True
```


Download 3-dimensional json-data 'data.x' that contains 'data.x.x_1', 'data.x.x_2' and 'data.x.x_3' columns, and column with time 'data.time'.
Set 'data.time' as independent variable and 'data.x' as dependent vector.
**method** defines the method of data preparation and index assignment: method = 'scale' - scales parameter **param_label** for each of the 'sid' to [0, 1] interval
and interpolate data on the new scale.

```python
>>> df = citros.topic('A').set_order({'sid':'asc','rid':'asc'}).data(['data.x','data.time'])
>>> V3 = Validation(df, data_label = 'data.x', param_label = 'data.time',
...                method = 'scale', num = 50, units = 'm')
```


Set different limits on Linf norm for each of the element of the 3-dimensional vector: 1.0 for the first element,
0.1 for the second one, and 0.5 for the third vector element:

```python
>>> log, table, fig = V3.norm_test(norm_type = 'Linf', limits = [1.0, 0.1, 0.5])
norm_test Linf: passed
```

</details>


    
## Method `set_tests` {#validation.validation.Validation.set_tests}




```python
def set_tests(
    test_method={'std_bound': {'limits': 1.0, 'n_std': 3, 'nan_passed': True}, 'mean': {'limits': 1.0, 'nan_passed': True}, 'sid': {'limits': 1.0, 'nan_passed': True}, 'norm_L2': {'limits': 1.0}, 'norm_Linf': {'limits': 1.0}}
)
```


<details>
  <summary>Description</summary>

Perform tests on the data.

Possible test methods are:
<details>
    <summary>'std_bound'</summary>

Test whether standard deviation is within the given limits.
Test parameters are stored as the dict with the following keys:
- 'limits' : float or list, default 1.0
    Limit to test standard deviation boundary. Limits may be set as:
   - one value and it will be treated as an +- interval: value -> [-value, value];
   - list of lower and upper limits: [lower_limit, upper_limit];
   - If the data has multiple columns, limits may be set for each of the column.
    That way list length must be equal to number of columns. For example, for the 3-dimensional vector with corresponding standard deviation boundaries [std_bound_1, std_bound_2, std_bound_3]:
    [[**limit_lower**, **limit_upper**], **value_1**, **value_2**] will be processed as:
    **limit_lower** < std_bound_1 < **limit_upper**,
    -**value_1** < std_bound_2 < **value_1**,
    -**value_2** < std_bound_2 < **value_2**.
- 'n_std' : int, default 3
    The parameter specifies the number of standard deviations to be within limits.
- 'nan_passed' : bool, default True
    If True, the NaN values of standard deviation will pass the test.

</details>

<details>
    <summary>'mean'</summary>

Test whether mean is within the given limits.
Test parameters are stored as the dict:
- 'limits' : float or list, default 1.0
    Limit to test mean. Limits may be set as:
   - one value and it will be treated as an +- interval: value -> [-value, value];
   - list of lower and upper limits: [lower_limit, upper_limit];
   - If the data has multiple columns, limits may be set for each of the column.
    That way list length must be equal to number of columns. For example, for the 3-dimensional vector
    with corresponding mean vector [mean_1, mean_2 and mean_3]:
    [[**limit_lower**, **limit_upper**], **value_1**, **value_2**] will be processed as:
    **limit_lower** < mean_1 < **limit_upper**,
    -**value_1** < mean_2 < **value_1**,
    -**value_2** < mean_2 < **value_2**.
- 'nan_passed' : bool, default True
    If True, the NaN values of the mean will pass the test.

</details>

<details>
    <summary>'std'</summary>

Test whether standard deviation is less then the given limits.
Test parameters are stored as the dict:
- 'limits' : float or list, default 1.0
    Limit to test standard deviation. Limits may be set as:
   - one value;
   - If the data has multiple columns, limits may be set for each of the column.
    That way list length must be equal to number of columns. For example, for the 3-dimensional vector
    with corresponding standard deviation vectors [std_1, std_2, std_3]:
    limits = [**value_1**, **value_2**, **value_3**] will be processed as:
    std_1 < **value_1**,
    std_2 < **value_2**,
    std_2 < **value_3**.
- 'n_std' : int, default 3
    The parameter specifies the number of standard deviations to be less then limits.
- 'nan_passed' : bool, default True
    If True, the NaN values of the mean will pass the test.

</details>

<details>
    <summary>'sid'</summary>

Test whether all simulations are within the given limits.
Test parameters are stored as the dict:
- 'limits' : float or list, default 1.0
    Limit to test simulation results. Limits may be set as:
   - one value and it will be treated as an +- interval: value -> [-value, value];
   - list of lower and upper limits: [lower_limit, upper_limit];
   - If the data has multiple columns, limits may be set for each of the column.
    That way list length must be equal to number of columns. For example, for the 3-dimensional vector that
    contains v1, v2, v3 columns and numbers N simulations:
    [[**limit_lower**, **limit_upper**], **value_1**, **value_2**] will be processed as:
    **limit_lower** < v1 < **limit_upper**,
    -**value_1** < v2 < **value_1**,
    -**value_2** < v3 < **value_2** for each of the N simulations.
- 'nan_passed' : bool, default True
    If True, the NaN values will pass the test.

</details>

<details>
    <summary>'norm_L2'</summary>

Test whether L2 norm of the each simulation is less than the given limit.
Test parameters are stored as the dict:
- 'limits' : float or list, default 1.0
    Limits on the simulation norm. Limits may be set as:
   - one value;
   - if the data has multiple columns, limits may be set for each of the column separately as a list.
    That way list length must be equal to number of the columns.

</details>

<details>
    <summary>'norm_Linf'</summary>

Test whether Linf norm of the each simulation is less than the given limit.
Test parameters are stored as the dict:
- 'limits' : float or list, default 1.0
    Limits on the simulation norm. Limits may be set as:
   - one value;
   - if the data has multiple columns, limits may be set for each of the column separately as a list.
    That way list length must be equal to number of the columns.

</details>

#### Parameters

Name|Type|Description
--|--|--
|**```tests_method```**|**dict**|Keys define test methods and corresponding test parameters are stored as values.
#### Returns

Name|Type|Description
--|--|--
|**```log```**|**[CitrosDict](../access/citros_dict.md#access.citros_dict.CitrosDict "access.citros_dict.CitrosDict")**|Dictionary with the test results.
|**```tables```**|**dict**|Dictionary with test methods as keys and pandas.DataFrame table with results of the test as values.
|**```figures```**|**dict**|Dictionary with test methods as keys and matplotlib.figure.Figure with test results as values.
#### See Also

**[Validation.std_bound_test()](#validation.validation.Validation.std_bound_test "validation.validation.Validation.std_bound_test")**, **[Validation.mean_test()](#validation.validation.Validation.mean_test "validation.validation.Validation.mean_test")**, **[Validation.std_test()](#validation.validation.Validation.std_test "validation.validation.Validation.std_test")**, **[Validation.sid_test()](#validation.validation.Validation.sid_test "validation.validation.Validation.sid_test")**, **[Validation.norm_test()](#validation.validation.Validation.norm_test "validation.validation.Validation.norm_test")**


</details>
<details>
  <summary>Examples</summary>

Import Validation and CitrosDB:

```python
>>> from citros import CitrosDB, Validation
```


From the batch 'density' of the simulation 'diffuse_nebula' from the topic 'A' download 3-dimensional 
json-data 'data.x' that contains 'data.x.x_1', 'data.x.x_2' and 'data.x.x_3' columns,
and column with time 'data.time'.

```python
>>> citros = CitrosDB(simulation = 'diffuse_nebula', batch = 'density')
>>> df = citros.topic('A').set_order({'sid':'asc','rid':'asc'}).data(['data.x','data.time'])
>>> print(df['data.x'])
0          {'x_1': 0.0, 'x_2': 0.08, 'x_3': 0.047}
1       {'x_1': 0.008, 'x_2': 0.08, 'x_3': -0.003}
2      {'x_1': 0.016, 'x_2': 0.078, 'x_3': -0.034}
...
```


Set 'data.time' as independent variable and 'data.x' as dependent vector.
**method** defines the method of data preparation and index assignment: method = 'scale' - scales parameter **param_label** for each of the 'sid' to [0, 1] interval
and interpolate data on the new scale.

```python
>>> V = Validation(df, data_label = 'data.x', param_label = 'data.time',
...                method = 'scale', num = 50, units = 'm')
```


Test whether 3 standard deviation boundary is within [-0.3, 0.3] interval (treat nan values of the
standard deviation, if they are presented, as passed the test) and L2 norm of the each simulation is less than 12.5:

```python
>>> logs, tables, figs = V.set_tests(test_method = {
...                                    'std_bound' : {'limits' : 0.3, 'n_std': 3, 'nan_passed': True},
...                                    'norm_L2' : {'limits' : 12.5}})
std_bound_test: passed
norm_test L2: passed
```


Print detailed standard deviation boundary test results:

```python
>>> logs['std_bound'].print()
{
 'test_param': {
   'limits': 0.3,
   'n_std': 3,
   'nan_passed': True
 },
 'data.x.x_1': {
   'passed': True,
   'pass_rate': 1.0,
   'failed': {
   },
   'nan_std': {
     49: 807.942
   }
 },
 'data.x.x_2': {
   'passed': True,
   'pass_rate': 1.0,
   'failed': {
   },
   'nan_std': {
     49: 807.942
   }
 },
 'data.x.x_2': {
   'passed': True,
   'pass_rate': 1.0,
   'failed': {
   },
   'nan_std': {
     49: 807.942
   }
  }
}
```


Print results of norm test in details:

```python
>>> logs['norm_L2'].print()
{
 'test_param': {
   'limits': 12.5
 },
 'data.x.x_1': {
   'passed': True,
   'pass_rate': 1.0,
   'norm_value': {
     1: 0.39,
     2: 0.38,
     3: 0.38
   },
   'failed': []
 },
 'data.x.x_2': {
   'passed': True,
   'pass_rate': 1.0,
   'norm_value': {
     1: 0.38,
     2: 0.40,
     3: 0.40
   },
   'failed': []
 },
 'data.x.x_3': {
   'passed': True,
   'pass_rate': 1.0,
   'norm_value': {
     1: 0.12,
     2: 0.11,
     3: 0.12
   },
   'failed': []
 }
}
```

</details>
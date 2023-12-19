---
# Display h3 headings
sidebar_label: 'Class CitrosData'
toc_max_heading_level: 3
hide_title: true
description: 'Documentation'
---

# Class CitrosData







    
## Class `CitrosData` {#citros_data_analysis.error_analysis.citros_data.CitrosData}





```python
class CitrosData(
    db=None,
    type_name='',
    units='',
    data_label='data',
    parameters=None,
    parameter_label='',
    sid_label='sid',
    omit_nan_rows=None,
    inf_vals=1e+308
)
```


<details>
  <summary>Description</summary>

Create CitrosData object, that allows to bin and interpolate data.

CitrosData object has two main attributes: 'data' - the vector of depending variables, 
and all other additional columns - 'addData'. Both 'data' and 'addData' attributes contains pandas.DataFrame.

#### Parameters

Name|Type|Description
--|--|--
|**```db```**|**DataFrame** or **tuple** of **two DataFrames** or **None**, optional|If **db** is a DataFrame, column **data_label** is supposed to be a data sample and set to a 'data' attribute of a CitrosData object.<br />    The additional information about data may be extracted from columns labeled as:<br />        'type_name' - specify type of the data, set to the 'type' attribute,<br />        'units' - data units, set to the 'units' attribute.<br />        'parameter_label' - column with dict, specifying the parameters, if it is presented, the first row is set as parameters.<br />    All other columns are assigned to 'addData' attribute.
|**```type_name```**|**str**, optional|Specifies type of the data.
|**```units```**|**str**, optional|Specifies units of the data.
|**```data_label```**|**str** or **list** of **str**, default `'data'`|Specifies label of the data in DataFrame
|**```parameters```**|**dict**|Parameters. Mostly used in regression analysis.
|**```parameter_label```**|**str** or **list** of **str**|Specify label of a column in a pandas DataFrame, where the parameters are written as a dict.<br />    Used only if **db** is a pandas DataFrame and **parameters** is not specified.
|**```sid_label```**|**str**, default `'sid'`|label of the sim run id column (usually 'sim_run_id' or 'sid').
|**```omit_nan_rows```**|**bool**, default **None**|If True, any rows containing one or more NaN values will be excluded from the analysis, see **Notes**.
|**```inf_vals```**|**None** or **float**, default **1e308**|If specified, all values from **data_label** column that exceed the provided value in absolute terms <br />    will be treated as NaN values. If this functionality is not required, set inf_vals = None.
#### Notes

If **omit_nan_rows** set True in case of multidimensional vectors, the mean and covariance matrices will be calculated 
only for rows that do not contain NaN values in all columns of the vector.
Otherwise, if **omit_nan_rows** is set to False, columns are treated individually.
The mean values are computed over non-NaN values within each column, and the elements of the covariance 
matrices are calculated pairwise, for rows without NaN values.
For example, for 3-dimensional vector:

```code
+----+-----+-----+
| x  | y   | z   |
+====+=====+=====+
| 1  | 3   | NaN |
+----+-----+-----+
| 2  | NaN | 5   |
+----+-----+-----+
| 3  | 5   | 6   |
+----+-----+-----+
| 4  | 7   | 7   |
+----+-----+-----+
```

if **omit_nan_rows** set True, the first and the second rows will be omitted from all calculations, while 
in case **omit_nan_rows** set False, NaN values will be omitted only when the column is used in calculations. 
For example, for mean calculations difference is the follows:

```code
    omit_nan_rows = True   omit_nan_rows = False
+-----+---+-----+      +-----+---+---+
|  x  | y | z   |      |  x  | y | z |
+=====+===+=====+      +=====+===+===+
| 3.5 | 6 | 6.5 |      | 2.5 | 5 | 6 |
+-----+---+-----+      +-----+---+---+
```
</details>









    
## Method `add_addData` {#citros_data_analysis.error_analysis.citros_data.CitrosData.add_addData}




```python
def add_addData(
    column,
    column_label
)
```


<details>
  <summary>Description</summary>

Add column to 'addData' attribute.

#### Parameters

Name|Type|Description
--|--|--
|**```column```**|`array-like object`|Column to add.
|**```column_label```**|**str**|Label of the new column in 'addData'.

</details>


    
## Method `drop_addData` {#citros_data_analysis.error_analysis.citros_data.CitrosData.drop_addData}




```python
def drop_addData(
    column_label
)
```


<details>
  <summary>Description</summary>

Delete column from 'addData' attribute.

#### Parameters

Name|Type|Description
--|--|--
|**```column_label```**|**str**|Label of the column to delete .

</details>


    
## Method `set_parameter` {#citros_data_analysis.error_analysis.citros_data.CitrosData.set_parameter}




```python
def set_parameter(
    key=None,
    value=None,
    item=None
)
```


<details>
  <summary>Description</summary>

Set parameter value to a CitrosData object.

#### Parameters

Name|Type|Description
--|--|--
|**```key```**|**str**|Label of the parameter.
|**```value```**|**int** or **float**|Parameter value.
|**```item```**|**dict**|Dictionary with parameters.

</details>


    
## Method `drop_parameter` {#citros_data_analysis.error_analysis.citros_data.CitrosData.drop_parameter}




```python
def drop_parameter(
    key=None
)
```


<details>
  <summary>Description</summary>

Delete parameter labeled **key** and associated value.

#### Parameters

Name|Type|Description
--|--|--
|**```key```**|**str**|Label of the parameter to remove.

</details>


    
## Method `bin_data` {#citros_data_analysis.error_analysis.citros_data.CitrosData.bin_data}




```python
def bin_data(
    n_bins=10,
    param_label='rid',
    min_lim=None,
    max_lim=None,
    show_fig=False
)
```


<details>
  <summary>Description</summary>

Bin values of column **param_label** in **n_bins** intervals, group data according to the binning and 
calculate mean data values of each group.

In order to establish a correspondence between the values of the data from different simulations, 
an independent variable **param_label** is selected and used to assign indexes. **param_label** values are divided into 
**n_bins** ranges, assigning index to each interval, and then for each simulation the averages of the data values 
is calculated in each bin.
'addData' and 'data' attributes of the new CitrosData object have two levels of indexes, 
with id values from binning as the first level and 'sid' as the second one.

#### Parameters

Name|Type|Description
--|--|--
|**```n_bins```**|**int**, default **10**|Number of bins.
|**```param_label```**|**str**, default `'rid'`|Label of column on the basis of which the indixes will be calculated.
|**```min_lim```**|**float**|The minimum value of the range for binning, **min_lim** < **max_lim**.<br />    If None then the minimum value of the entire range is selected.
|**```max_lim```**|**float**|The maximum value of the range for binning, **min_lim** < **max_lim**.<br />    If None then the maximum value of the entire range is selected.
|**```show_fig```**|**bool**, default **False**|If the histogram that represents the distribution of the values in **param_label** should be shown.
#### Returns

Name|Type|Description
--|--|--
|**```out```**|**[CitrosData](#citros_data_analysis.error_analysis.citros_data.CitrosData "citros_data_analysis.error_analysis.citros_data.CitrosData")**|New CitrosData object with two levels of indexes in 'addData' and 'data' attributes.

</details>
<details>
  <summary>Examples</summary>

Query some data from the topic 'A'

```python
>>> df = citros.topic('A').data(['data.x.x_1', 'data.time'])
>>> print(df)
```


Construct CitrosData object with one data-column 'data.x.x_1':

```python
>>> dataset = analysis.CitrosData(df, data_label=['data.x.x_1'], units = 'm')
```


Divide 'data.time' values in 50 bins and assign indexes to these intervals. For each simulation group 
'data.x.x_1' values according to the binning and calculate mean of the each group:

```python
>>> db = dataset.bin_data(n_bins = 50, param_label = 'data.time')
```


The result is a CitrosData object with two levels of indexes:

```python
>>> print(db.data)
                    data.x.x_1
data.time_id  sid            
0             1     0.00000
              2     -0.04460
              3     -0.07900
1             1     0.01600
...
```


```python
>>> print(db.addData)
                    data.time
data.time_id  sid           
0             1     8.458
              2     8.458
              3     8.458
1             1     24.774
...
```

</details>


    
## Method `scale_data` {#citros_data_analysis.error_analysis.citros_data.CitrosData.scale_data}




```python
def scale_data(
    n_points=10,
    param_label='rid',
    show_fig=False,
    intr_kind='linear'
)
```


<details>
  <summary>Description</summary>

Scale parameter **param_label** for each of the 'sid' and interpolate data on the new scale.

In order to establish a correspondence between the values of the data from different simulations, 
an independent variable **param_label** is selected and used to assign indexes. 
First the **param_label** interval is shifted and scaled in the way that the minimum value equals 0 and the maximum is 1.
Then the data is interpolated to a new scale, that consists of **n_points** evenly spaced points and spans from 0 to 1.
For each 'sid' this procedure is performed separately.
'addData' and 'data' attributes of the new CitrosData object have two levels of indexes, 
with id values from scaling as the first level and 'sid' as the second one.

#### Parameters

Name|Type|Description
--|--|--
|**```n_points```**|**int**, default **10**|Number of points in a new scale, which will be used for interpolation.
|**```param_label```**|**str**, default `'rid'`|Label of the parameter to scale
|**```show_fig```**|**bool**, default **False**|If the figures with the results of interpolation should be shown.<br />    If the 'sid' exceed 5, only first 5 will be shown.<br />    If data consists of several vectors, for each of them the separate figure will be plotted.
|**```intr_kind```**|**str**, default `'linear'`|Type of the interpolation, see scipy.interpolate.interp1d.
#### Returns

Name|Type|Description
--|--|--
|**```out```**|**[CitrosData](#citros_data_analysis.error_analysis.citros_data.CitrosData "citros_data_analysis.error_analysis.citros_data.CitrosData")**|CitrosData object with multi-level indexing: the first level stores ids of the points of the new scale, the second one - 'sid'.<br />    Values of the new scale are stored in 'addData' attribute.

</details>
<details>
  <summary>Examples</summary>

Query some data from the topic 'A'

```python
>>> df = citros.topic('A').data(['data.x.x_1', 'data.time'])
>>> print(df)
```


Construct CitrosData object with one data-column 'data.x.x_1':

```python
>>> dataset = analysis.CitrosData(df, data_label=['data.x.x_1'], units = 'm')
```


Scale 'data.time' to [0, 1] interval, define a new range of 50 points uniformly distributed from 0 to 1, 
and interpolate data points over this new interval:

```python
>>> db = dataset.scale_data(n_points = 50, param_label = 'data.time')
```


The result is a CitrosData object with two levels of indexes:

```python
>>> print(db.data)
                    data.x.x_1
data.time_id  sid            
0             1      0.000000
              2     -0.057000
              3     -0.080000
1             1      0.025494
...
```


```python
>>> print(db.addData)
                    data.time
data.time_id  sid           
0             1     0.000000
              2     0.000000
              3     0.000000
1             1     0.020408
...
```

</details>


    
## Method `get_statistics` {#citros_data_analysis.error_analysis.citros_data.CitrosData.get_statistics}




```python
def get_statistics(
    return_format='pandas'
)
```


<details>
  <summary>Description</summary>

Return table with statistics for CitrosData object.

#### Parameters

Name|Type|Description
--|--|--
|**```return_format```**|`{'pandas', 'citrosStat'}`, default `'pandas'`|Returning format.
#### Returns

Name|Type|Description
--|--|--
|**```Statistics```**|**pandas.DataFrame** or **[CitrosStat](citros_stat.md#citros_data_analysis.error_analysis.citros_stat.CitrosStat "citros_data_analysis.error_analysis.citros_stat.CitrosStat")**|Collected statistics.<br />    If **return_format** is 'pandas', then returns pandas.DataFrame with the following columns:<br />      &#8226; (1) the independent variable column, its label matches **x_label** attribute; <br />      &#8226; (2) column with mean values;<br />      &#8226; (3) column with the covariance matrixes; <br />      &#8226; (4) column with the square roots of the diagonal elements of the covariance matrix: ( sqrt(s1), sqrt(s2), sqrt(s3) ), <br />    where s1,s2,s3 - diagonal of the covariance matrix. <br />    <br />    If **return_format** is 'citrosStat', then returns CitrosStat object with 'x', 'mean', 'covar_matrix' and 'sigma' attributes,<br />    that corresponds to (1)-(4) items, but in the form of pandas.DataFrames.
#### See Also

**[CitrosData.bin_data()](#citros_data_analysis.error_analysis.citros_data.CitrosData.bin_data "citros_data_analysis.error_analysis.citros_data.CitrosData.bin_data")**, **[CitrosData.scale_data()](#citros_data_analysis.error_analysis.citros_data.CitrosData.scale_data "citros_data_analysis.error_analysis.citros_data.CitrosData.scale_data")**, **[CitrosData.show_statistics()](#citros_data_analysis.error_analysis.citros_data.CitrosData.show_statistics "citros_data_analysis.error_analysis.citros_data.CitrosData.show_statistics")**


</details>
<details>
  <summary>Examples</summary>

Import 'data_access' and 'error_analysis' modules and create CitrosDB object to query data:

```python
>>> from citros_data_analysis import data_access as da
>>> from citros_data_analysis import error_analysis as analysis
>>> citros = da.CitrosDB()
```


Let's consider a data of the topic 'A', json-data part of which has the following structure:

```python
data
{'x': {'x_1': -0.08, 'x_2': -0.002, 'x_3': 17.7}, 'time': 0.3}
{'x': {'x_1': 0.0, 'x_2': 0.08, 'x_3': 154.47}, 'time': 10.0}
...
```

Let's query data and pass it to CitrosData object to perform analysis.
It is possible to query all columns separately:

```python
>>> df = citros.topic('A').data(['data.x.x_1', 'data.x.x_2', 'data.x.x_3', 'data.time'])
>>> print(df)
   sid   rid   time       topic   type   data.x.x_1   data.x.x_2   data.x.x_3   data.time
0  1     0     312751159  A       a      0.000        0.080        154.47       10.0
1  1     1     407264008  A       a      0.008        0.080        130.97       17.9
2  1     2     951279608  A       a      0.016        0.078        117.66       20.3
...
```


and define data labels for the CitrosData object as follows:

```python
>>> dataset = analysis.CitrosData(df,
...                               data_label = ['data.x.x_1', 'data.x.x_2', 'data.x.x_3'],
...                               units = 'm')
```


or query 'data.x' as a one column:

```python
>>> df = citros.topic('A').data(['data.x', 'data.time'])
>>> print(df)
   sid   rid   time       topic   type   data.x                                       data.time
0  1     0     312751159  A       a      {'x_1': 0.0, 'x_2': 0.08, 'x_3': 154.47}     10.0
1  1     1     407264008  A       a      {'x_1': 0.008, 'x_2': 0.08, 'x_3': 130.97}   17.9
2  1     2     951279608  A       a      {'x_1': 0.016, 'x_2': 0.078, 'x_3': 117.66}  20.3
...
```


and correspondingly set data_label:

```python
>>> dataset = analysis.CitrosData(df,
...                               data_label = 'data.x',
...                               units = 'm')
```


To analyze data of multiple simulations it is necessary to establish a correspondence between the values of the data 
from these different simulations. One approach is to select an independent variable, define a scale that is common 
to all simulations and assign indexes on this scale. Then, the values of variables from different simulations
will be connected by this independent variable.

There are two ways to perform index assignment: divide the independent variable into N ranges, 
assign an index to each interval, and calculate the averages of the data values for each simulation in each range, 
or scale the independent variable to the interval [0,1], define a new range of N points uniformly distributed from 0 to 1, 
and interpolate data points over this new interval. The first approach corresponds to the bin_data() method, while the second 
is implemented by the scale_data() method:

```python
>>> db = dataset.bin_data(n_bins = 50, param_label = 'data.time')
>>> #or
>>> db = dataset.scale_data(n_points = 50, param_label = 'data.time')
```


Let's assume that the last variant was chosen. And now get the statistics:

```python
>>> stat = db.get_statistics(return_format = 'citrosStat')
```


It returns CitrosStat object, that stores independent variable values, mean data values, covariant matrix and 
standard deviation (square root of the covariant matrix diagonal elements) for each index.

The mean data value, independent variable values and standard deviation are the pandas.DataFrames:

```python
>>> print(stat.mean)
               data.x.x_1   data.x.x_2  data.x.x_3
data.time_id                                    
0              -0.045667    0.044667    93.706667
1              -0.026038    0.059598    73.345027
...
```


```python
>>> print(stat.x)
               data.time
data.time_id           
0              0.000000
1              0.020408
...
```


```python
>>> print(stat.sigma)
                data.x.x_1  data.x.x_2  data.x.x_3
data.time_id                                    
0               0.041187    0.042158    69.647524
1               0.050354    0.026935    84.049381
2               0.049388    0.010733    40.279784
```


and the covariant matrix is a pandas.Series. Each its row contains N x N dimensional numpy.ndarray, where N
is a data dimension:

```python
>>> print(stat.covar_matrix.loc[0])
[[1.69633333e-03 1.54366667e-03 2.60583167e+00]
[1.54366667e-03 1.77733333e-03 2.93335333e+00]
[2.60583167e+00 2.93335333e+00 4.85077763e+03]]
```

</details>


    
## Method `show_statistics` {#citros_data_analysis.error_analysis.citros_data.CitrosData.show_statistics}




```python
def show_statistics(
    fig=None,
    show_fig=True,
    return_fig=False,
    n_std=3,
    fig_title='Statistics',
    std_color='r',
    connect_nan_std=True,
    std_area=False,
    std_lines=True
)
```


<details>
  <summary>Description</summary>

Collect statistics for CitrosData object and plot it.

#### Parameters

Name|Type|Description
--|--|--
|**```fig```**|**matplotlib.figure.Figure**|figure to plot on. If None, the new one will be created.
|**```show_fig```**|**bool**|If the figure should be shown, True by default.
|**```return_fig```**|**bool**|If the figure parameters fig, ax should be returned; <br />    fig is matplotlib.figure.Figure and ax is matplotlib.axes.Axes
|**```n_std```**|**int**, default **3**|Error interval to display in standard deviations.
|**```fig_title```**|**str**, default `'Statistics'`|Title of the figure.
|**```std_color```**|**str**, default `'r'`|Color for displaying standard deviations, red by default.
|**```connect_nan_std```**|**bool**, default **True**|If True, all non-NaN values in standard deviation boundary line are connected, resulting in a continuous line. <br />    Otherwise, breaks are introduced in the standard deviation line whenever NaN values are encountered.
|**```std_area```**|**bool**, default **False**|Fill area within **n_std**-standard deviation lines with color.
|**```std_lines```**|**bool**, default **True**|If False, remove standard deviation boundary lines.
#### Returns

Name|Type|Description
--|--|--
|**```fig```**|**matplotlib.figure.Figure**|if **return_fig** set to True
|**```ax```**|**numpy.ndarray** of **matplotlib.axes.Axes**|if **return_fig** set to True
#### See Also

**[CitrosData.get_statistics()](#citros_data_analysis.error_analysis.citros_data.CitrosData.get_statistics "citros_data_analysis.error_analysis.citros_data.CitrosData.get_statistics")**, **[CitrosData.bin_data()](#citros_data_analysis.error_analysis.citros_data.CitrosData.bin_data "citros_data_analysis.error_analysis.citros_data.CitrosData.bin_data")**, **[CitrosData.scale_data()](#citros_data_analysis.error_analysis.citros_data.CitrosData.scale_data "citros_data_analysis.error_analysis.citros_data.CitrosData.scale_data")**


</details>
<details>
  <summary>Examples</summary>

Import 'data_access' and 'error_analysis' modules and create CitrosDB object to query data:

```python
>>> from citros_data_analysis import data_access as da
>>> from citros_data_analysis import error_analysis as analysis
>>> citros = da.CitrosDB()
```


Download json-data column 'data.x', that contains data.x.x_1, data.x.x_2 and data.x.x_3 and column 'data.time':

```python
>>> df = citros.topic('A').data(['data.x', 'data.time'])
```


Construct CitrosData object with 3 data-columns from 'data.x':

```python
>>> dataset = analysis.CitrosData(df, data_label=['data.x'], units = 'm')
```


Use method scale_data() or bin_data() to get correspondence between different simulation:

```python
>>> db_sc = dataset.scale_data(n_points = 150, 
                               param_label = 'data.time', 
                               show_fig = False)
```


Show statistics plot:

```python
>>> db_sc.show_statistics()
```

</details>


    
## Method `show_correlation` {#citros_data_analysis.error_analysis.citros_data.CitrosData.show_correlation}




```python
def show_correlation(
    db2=None,
    x_col=0,
    y_col=0,
    slice_id=None,
    slice_val=None,
    n_std=3,
    bounding_error=False,
    fig=None,
    return_fig=False,
    display_id=True,
    return_ellipse_param=False,
    **kwargs
)
```


<details>
  <summary>Description</summary>

Show data correlation for the given **slice_id**. 

Prepare data from one or more CitrosData objects and plot confidence ellipses for the specified id = **slice_id**.
If the data stored in CitrosData object **db** is multidimensional, then **x_colNumber** and **y_colNumber** must be provided.
If the data from another CitrosData objects is used, the latter must be provided in **db2**. Then the data from **db** 
is supposed to be plotted along x-axis and the data from **db2** is supposed to be plotted along y-axis.

#### Parameters

Name|Type|Description
--|--|--
|**```db2```**|**[CitrosData](#citros_data_analysis.error_analysis.citros_data.CitrosData "citros_data_analysis.error_analysis.citros_data.CitrosData")**|Additional CitrosData object.
|**```x_col```**|`int >=0` or **str**, optional|      &#8226; If **int** - index of column to plot along x axis, >=0.<br />      &#8226; If **str** - label of the column to plot along y axis<br />      &#8226; If data is multidimensional, must be specified, otherwise data is supposed to be 1-dimensional.
|**```y_col```**|`int >=0`  or **str**, optional|      &#8226; If **int** - index of column to plot along y axis, >=0.<br />      &#8226; If **str** - label of the column to plot along y axis<br />      &#8226; If data is multidimensional, must be specified, otherwise data is supposed to be 1-dimensional.
|**```slice_id```**|**int**|id of the slice.
|**```slice_val```**|**float**|Value, for which the nearest slice_id is search.<br />    Used only if slice_id is None.
|**```n_std```**|**list** or **int**, default **3**|Radius or list of radii of the confidence ellipses in sigmas, 3 by default.
|**```bounding_error```**|**bool**, default **False**|If the bounding error should be depicted.
|**```fig```**|**matplotlib.figure.Figure**, optional|figure to plot on. If None, then the new one is created.
return_fig : bool, default False.
    If the fig, ax should be returned.
|**```display_id```**|**bool**, default **True**|Whether to print the pair of **slice_id** **slice_val** or not.
|**```return_ellipse_param```**|**bool**, default **False**|If True, returns ellipse parameters.
#### Other Parameters

Name|Type|Description
--|--|--
|**```kwargs```**|**dict**, optional|see matplotlib.patches.Ellipse.
#### Returns

Name|Type|Description
--|--|--
|**```fig```**|**matplotlib.figure.Figure**|if **return_fig** set to True
|**```ax```**|**matplotlib.axes.Axes**|if **return_fig** set to True
|**```ellipse_param```**|**dict** or **list** of **dict**|Ellipse parameters if **return_ellipse_param** set True.<br />    Parameters of the ellipse:<br />      &#8226; x : float - x coordinate of the center.<br />      &#8226; y : float - y coordinate of the center.<br />      &#8226; width : float - total ellipse width (diameter along the longer axis).<br />      &#8226; height : float - total ellipse height (diameter along the shorter axis).<br />      &#8226; alpha : float - angle of rotation, in degrees anti-clockwise from the minor axis.<br /><br />    If bounding_error set True:<br />      &#8226; bounding_error : float - radius of the error circle.

</details>
<details>
  <summary>Examples</summary>

Import 'data_access' and 'error_analysis' modules and create CitrosDB object to query data:

```python
>>> from citros_data_analysis import data_access as da
>>> from citros_data_analysis import error_analysis as analysis
>>> citros = da.CitrosDB()
```


For topic 'B' query json-data column 'data.x.x_1', 'data.x.x_2' and 'data.time':

```python
>>> df = citros.topic('B').data(['data.x.x_1', 'data.x.x_2', 'data.time'])
```


Construct CitrosData object with 2 data-columns 'data.x.x_1', 'data.x.x_2':

```python
>>> dataset = analysis.CitrosData(df, data_label=['data.x.x_1', 'data.x.x_2'], units = 'm')
```


Use method scale_data() or bin_data() to get correspondence between different simulation
and assign indexes to 'data.time' axis:

```python
>>> db_sc = dataset.scale_data(n_points = 20, 
...                            param_label = 'data.time', 
...                            show_fig = False)
```


Plot correlation plot for the index = 5:

```python
>>> db_sc.show_correlation(x_col = 'data.x.x_2',
...                        y_col = 'data.x.x_1',
...                        slice_id = 5,
...                        n_std = [1,2,3],
...                        bounding_error= False)
slice_id = 5,
slice_val = 0.2632
```

</details>


    
## Method `to_pandas` {#citros_data_analysis.error_analysis.citros_data.CitrosData.to_pandas}




```python
def to_pandas()
```


<details>
  <summary>Description</summary>

Concatenate **data** and **addData** attributes and return the result table as a pandas.DataFrame.

#### Returns

Name|Type|Description
--|--|--
|**```df```**|**pandas.DataFrame**|Concatenated table.

</details>
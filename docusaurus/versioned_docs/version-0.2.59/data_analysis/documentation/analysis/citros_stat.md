---
# Display h3 headings
sidebar_label: 'Class CitrosStat'
toc_max_heading_level: 3
hide_title: true
description: 'Documentation'
---

# Class CitrosStat







    
## Class `CitrosStat` {#analysis.citros_stat.CitrosStat}





```python
class CitrosStat(
    F,
    labels,
    x_label
)
```


<details>
  <summary>Description</summary>

Object to store statistics.

#### Parameters

Name|Type|Description
--|--|--
|**```F```**|**pandas.DataFrame**|Table with statistics.
|**```labels```**|`array-like`|Labels of the data columns.
|**```x_label```**|**str**|Label of the independent variable.
#### Attributes

Name|Type|Description
--|--|--
|**```x```**|**pandas.DataFrame**|Table with independent variable.
|**```mean```**|**pandas.DataFrame**|Table with mean values. If statistics was collected for a vector, columns correspond to vector elements.
|**```covar_matrix```**|**pandas.DataFrame**|Table with the covariance matrixes. If statistics was collected for a vector, columns correspond to vector elements.
|**```sigma```**|**pandas.DataFrame**|Table with the square roots of the diagonal elements of the covariance matrix. <br />    If statistics was collected for a vector, columns correspond to vector elements.

</details>









    
## Method `to_pandas` {#analysis.citros_stat.CitrosStat.to_pandas}




```python
def to_pandas()
```


<details>
  <summary>Description</summary>

Convert CitrosStat object back to pandas DataFrame.

#### Returns

Name|Type|Description
--|--|--
|**```df```**|**pandas.DataFrame**|Converted to pandas DataFrame.

</details>


    
## Method `plot` {#analysis.citros_stat.CitrosStat.plot}




```python
def plot(
    fig=None,
    show_fig=True,
    return_fig=False,
    n_std=3,
    fig_title='Statistics',
    std_color='r'
)
```


<details>
  <summary>Description</summary>

Plot mean values and standard deviations.

#### Parameters

Name|Type|Description
--|--|--
|**```fig```**|**matplotlib.figure.Figure**|figure to plot on. If None, the new one will be created.
|**```show_fig```**|**bool**|If the figure should be shown, True by default.
|**```return_fig```**|**bool**|If the figure parameters fig, ax should be returned; <br />    fig is matplotlib.figure.Figure and ax is matplotlib.axes.Axes
|**```n_std```**|**int**, default **3**|Error interval to display, specified in standard deviations.
|**```fig_title```**|**str**, default `'Statistics'`|Title of the figure.
|**```std_color```**|**str**, default `'r'`|Color for displaying standard deviations, red by default.
#### Returns

Name|Type|Description
--|--|--
|**```fig```**|**matplotlib.figure.Figure**|if **return_fig** set to True
|**```ax```**|**list** of **matplotlib.axes.Axes**|if **return_fig** set to True

</details>
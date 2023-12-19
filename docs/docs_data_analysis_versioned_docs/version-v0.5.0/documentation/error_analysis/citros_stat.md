---
# Display h3 headings
sidebar_label: 'class CitrosStat'
toc_max_heading_level: 3
hide_title: true
---








    
## Class `CitrosStat` {#citros_data_analysis.error_analysis.citros_stat.CitrosStat}





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

---
#### Parameters

**```F```** :&ensp;**pandas.DataFrame**
:   Table with statistics.


**```labels```** :&ensp;`array-like`
:   Labels of the data columns.


**```x_label```** :&ensp;**str**
:   Label of the independent variable.

---
#### Attributes

**```x```** :&ensp;**pandas.DataFrame**
:   Table with independent variable.


**```mean```** :&ensp;**pandas.DataFrame**
:   Table with mean values. If statistics was collected for a vector, columns correspond to vector elements.


**```covar_matrix```** :&ensp;**pandas.DataFrame**
:   Table with the covariance matrixes. If statistics was collected for a vector, columns correspond to vector elements.


**```sigma```** :&ensp;**pandas.DataFrame**
:   Table with the square roots of the diagonal elements of the covariance matrix. 
    If statistics was collected for a vector, columns correspond to vector elements.





</details>






    
### Method `plot` {#citros_data_analysis.error_analysis.citros_stat.CitrosStat.plot}




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

---
#### Parameters

**```fig```** :&ensp;**matplotlib.figure.Figure**
:   figure to plot on. If None, the new one will be created.


**```show_fig```** :&ensp;**bool**
:   If the fugure should be shown, True by default.


**```return_fig```** :&ensp;**bool**
:   If the figure parameters fig, ax should be returned; 
    fig is matplotlib.figure.Figure and ax is matplotlib.axes.Axes


**```n_std```** :&ensp;**int**, default **3**
:   Error interval to display, specified in standard deviations.


**```fig_title```** :&ensp;**str**, default `'Statistics'`
:   Title of the figure.


**```std_color```** :&ensp;**str**, default `'r'`
:   Color for dispalying standard deviations, red by default.

---
#### Returns

**```fig```** :&ensp;**matplotlib.figure.Figure**
:   if **return_fig** set to True


**```ax```** :&ensp;**list** of **matplotlib.axes.Axes**
:   if **return_fig** set to True


</details>


    
### Method `to_pandas` {#citros_data_analysis.error_analysis.citros_stat.CitrosStat.to_pandas}




```python
def to_pandas()
```


<details>
  <summary>Description</summary>

Convert CitrosStat object back to pandas DataFrame.

---
#### Returns

&ensp;**pandas.DataFrame**
:   Converted to pandas DataFrame.


</details>
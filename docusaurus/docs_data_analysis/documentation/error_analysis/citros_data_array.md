---
# Display h3 headings
sidebar_label: 'Class CitrosDataArray'
toc_max_heading_level: 3
hide_title: true
description: 'Documentation'
---

# Class CitrosDataArray







    
## Class `CitrosDataArray` {#citros_data_analysis.error_analysis.citros_data_array.CitrosDataArray}





```python
class CitrosDataArray(
    dbs=None
)
```


<details>
  <summary>Description</summary>

Store CitrosData objects in a "dbs" attribute for regression analysis.

#### Parameters

Name|Type|Description
--|--|--
|**```dbs```**|**list**|list of CitrosData objects

</details>









    
### Method `add_db` {#citros_data_analysis.error_analysis.citros_data_array.CitrosDataArray.add_db}




```python
def add_db(
    db
)
```


<details>
  <summary>Description</summary>

Add one CitrosData object to CitrosDataArray.

#### Parameters

Name|Type|Description
--|--|--
|**```db```**|**[CitrosData](citros_data.md#citros_data_analysis.error_analysis.citros_data.CitrosData "citros_data_analysis.error_analysis.citros_data.CitrosData")**|CitrosData object to add to storage.

</details>


    
### Method `add_dbs` {#citros_data_analysis.error_analysis.citros_data_array.CitrosDataArray.add_dbs}




```python
def add_dbs(
    dbs
)
```


<details>
  <summary>Description</summary>

Add list of CitrosData objects to CitrosDataArray.

#### Parameters

Name|Type|Description
--|--|--
|**```dbs```**|**list**|list of CitrosData objects to add to storage.

</details>


    
### Method `drop_db` {#citros_data_analysis.error_analysis.citros_data_array.CitrosDataArray.drop_db}




```python
def drop_db(
    value
)
```


<details>
  <summary>Description</summary>

Remove CitrosData object from CitrosDataArray.

If **value** is an int, then removes by index, 
if **value** is a CitrosData object, then removes it if it exists in CitrosDataArray.

#### Parameters

Name|Type|Description
--|--|--
|**```value```**|**int** or **[CitrosData](citros_data.md#citros_data_analysis.error_analysis.citros_data.CitrosData "citros_data_analysis.error_analysis.citros_data.CitrosData")**|Object or index of object to remove.

</details>


    
### Method `get_prediction` {#citros_data_analysis.error_analysis.citros_data_array.CitrosDataArray.get_prediction}




```python
def get_prediction(
    parameters,
    method='poly',
    n_poly=2,
    activation='relu',
    max_iter=500,
    solver='lbfgs',
    hidden_layer_sizes=(10,),
    alpha=1e-16,
    fig=None,
    show_fig=False,
    return_fig=False,
    **kwargs
)
```


<details>
  <summary>Description</summary>

Show the predictions based on the results of the regression solution, neural net or gaussian mixture model.

#### Parameters

Name|Type|Description
--|--|--
|**```parameters```**|**dict**|Names of the independent parameters and their values to calculate the prediction.
|**```method```**|**str** or **list** of **str**, default `'poly'`|      &#8226; 'poly' - the polynomial regression.<br />      &#8226; 'neural_net' - the solution is finding based on [sklearn.neural_network.MLPRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html).<br />      &#8226; 'gmm' - the gaussian mixture model is built and used for the prediction.
|**```n_poly```**|**int**, default **2**|Only used if **method** = 'poly'.<br />    The highest degree of the polynomial (1 for linear, 2 for quadratic, etc).
|**```activation```**|`{'relu', 'identity', 'logistic'` or `'tanh'}`, default `'relu'`|Only used if **method** = 'neural_net'.<br />    Activation function for the hidden layer, see sklearn.neural_network.MLPRegressor
|**```max_iter```**|**int**, default **500**|Only used if **method** = 'neural_net'.<br />    Maximum number of iterations.
|**```solver```**|`{'lbfgs', 'sgd', 'adam'}`, default `'lbfgs'`|Only used if **method** = 'neural_net'.<br />    The solver for weight optimization.
|**```hidden_layer_sizes```**|`array-like` of `shape(n_layers - 2,)`, default=**(10,)**|Only used if **method** = 'neural_net'.<br />    The ith element represents the number of neurons in the ith hidden layer.
|**```alpha```**|**float**, default `1e-16`|Only used if **method** = 'gmm'.<br />    Value of the covariance element of parameters.
|**```fig```**|**matplotlib.figure.Figure**, optional|figure to plot on. If None, then the new one is created.
|**```show_fig```**|**bool**, default **True**|If the figure will be shown.
|**```return_fig```**|**bool**, default **False**|If True, the figure and ax (or list of ax) will be returned.
#### Other Parameters

Name|Type|Description
--|--|--
|**```kwargs```**|**dict**, optional|Other keyword arguments for **method** = 'neural_net', see [sklearn.neural_network.MLPRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html).
#### Returns

Name|Type|Description
--|--|--
|**```result```**|**pandas.DataFrame**|Predicted table
|**```fig```**|**matplotlib.figure.Figure**|if **return_fig** set to True
|**```ax```**|**matplotlib.axes.Axes** or **list** of **matplotlib.axes.Axes**|if **return_fig** set to True

</details>
<details>
  <summary>Examples</summary>

Create CitrosDataArray object:

```python
>>> db_array = analysis.CitrosDataArray()
```


Let's assume that for the topic 'A' there are simulations for the four different values of the some parameter 't', 
that is written in json-data column 'data.t'. To get list of the 'data.t' parameters get_unique_values() 
method may be used:

```python
>>> list_t = citros.topic('A').get_unique_values('data.t')
>>> print(list_t)
[-1.5, 0, 2.5, 4]
```


Let's find prediction for the values of the 'data.x.x_1' json-column for the case when 'data.t' equals 1.
Query data for each of these parameter values, set it as parameter, assign indexes over 'data.time' axis to set
correspondence between different simulations and pass the result to CitrosDataArray that we created:

```python
>>> for t in list_t:
...     #query data
...     df = citros.topic('A')\
...                .set_filter({'data.t': [t]})\
...                .data(['data.x.x_1', 'data.time', 'data.t'])
...
...     #create CitrosData object and set 'data.t' as a parameter.
...     dataset = analysis.CitrosData(df,  
...                                  data_label=['data.x.x_1'],
...                                  units = 'm', 
...                                  parameter_label = ['data.t'])
...
...     #scale over 'data.time'
...     db_sc = dataset.scale_data(n_points = 100, 
...                                param_label = 'data.time', 
...                                show_fig = False)
...
...     #store in CitrosDataArray by add_db() method
...     db_array.add_db(db_sc)
```


Get the prediction with 'poly' method:

```python
>>> result = db_array.get_prediction(parameters = {'data.t': 1},
...                                  method = 'poly', 
...                                  n_poly = 2,
...                                  show_fig = True)
>>> print(result)
    data.time   data.x.x_1
0       0.000000        1.155301
1       0.010101        1.145971
2       0.020202        1.232255
...
```

</details>
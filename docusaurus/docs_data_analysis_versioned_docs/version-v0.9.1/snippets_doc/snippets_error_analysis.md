---
toc_max_heading_level: 4
hide_title: true
sidebar_label: 'Error Analysis'
---
# Error Analysis

## Get Statistics For Simulations

### 1-dimensional Vector
To analyze data of multiple simulations it is necessary to establish a correspondence between the values of the data from these different simulations. One approach is to select an independent variable, define a scale that is common to all simulations and assign indexes on this scale. Then, the values of variables from different simulations will be connected by this independent variable.

There are two ways to perform index assignment: divide the independent variable into N ranges, assign an index to each interval, and calculate the averages of the data values for each simulation in each range, or scale the independent variable to the interval [0,1], define a new range of N points uniformly distributed from 0 to 1, and interpolate data points over this new interval. The first approach corresponds to the bin_data() method, while the second is implemented by the scale_data() method.

Let's consider a table for topic 'my_topic' from the batch 'my_batch', where each row under the 'data' column holds a dictionary and within this dictionary, under the key 'data' is a list of values, as shown:

|data                 |
|---------------------|
|{data: [1, 2, 3...]} |
|{data: [4, 5, 6...]} |
|...                  |

Let's consider that we would like to calculate statistics among simulations for the values at the first position of the list. An independent variable can be set using values, for instance, from the second position. Also, in some cases, an array of the independent variables be constructed using the 'rid' column, which represents a step in each simulation.
Let's assume, that in each simulation value is recorded every 0.2 seconds, so we can construct and independent variable Time = rid*0.2.

```python
# --- adjust to your data --- #

# Set batch and topic names.
batch_name = 'my_batch'
topic_name = 'my_topic'

# Data is queried from the first index:
data_label = 'data.data[0]'

# Set method of index assignment as 'scale' or 'bin':
method = 'bin'

# Set time step to construct independent variable column as: Time = rid*time_step.
time_step  = 0.2
# --------------------------- #

# Import 'data_access' and 'error_analysis' modules and create CitrosDB object:
from citros_data_analysis import data_access as da
from citros_data_analysis import error_analysis as analysis
citros = da.CitrosDB()

# Query data:
df = citros.batch(batch_name).topic(topic_name).data(data_label)

# Construct independent variable column as: Time = rid*time_step.
df['Time'] = df['rid']*time_step

# Construct CitrosData object, setting 'data.data[0]' as a data-column:
dataset = analysis.CitrosData(df, data_label = data_label, units = 'm')

# set an independent variable as 'Time' (column, that we constructed previously) by label by `param_label`:
if method == 'bin':
    db = dataset.bin_data(n_bins = 50, param_label = 'Time')
# or
elif method == 'scale':
    db = dataset.scale_data(n_points = 50, param_label = 'Time')
else:
    print('please define method of index assignment: "scale" or "bin"')

# Get statistics.
# When data is binned or interpolated, for each of the index the mean values, covariant matrix 
# and standard deviations (the square root the covariant matrix diagonal elements) may be calculated.
# The output table is a pandas DataFrame:

stat = db.get_statistics(return_format = 'citrosStat')

# `stat` contains 3 attributes:
# the mean values (type - pandas.DataFrame):
print('mean values:\n', stat.mean.head(5))

# the standard deviation (type - pandas.DataFrame):
print('standard deviation:\n', stat.std.head(5))

# the covariance matrix (type - pandas.Series):
print('covariance matrix:\n', stat.covar_matrix.head(5))

# Method head(n) of pandas.DataFrame is used to show the first n rows of the table


# Plot statistics.
db.show_statistics()
# by default, it plots +-3 standard deviation boundary.
# To plot for another number of standard deviations, for example for +- 5std boundary: n_std = 5
# you may style area between standard deviation boundaries: by std_area = True fill area with color.
# by std_lines = False - remove lines of the boundary :
db.show_statistics(n_std = 5, std_area = True, std_lines = False)
```
### N-dimensional Vector

The same example as for the [1-dimensional vector](#get-statistics-for-simulations-1-dimensional-vector), but for the multidimensional vector.

Suppose for topic 'my_topic' from the batch 'my_batch' every row in the 'data' column contains a dictionary and within this dictionary, the 'data' key corresponds to a list that has a length of 3, as illustrated below:

|data              |
|------------------|
|{data: [1, 2, 3]} |
|{data: [4, 5, 6]} |
|...               |

```python
# --- adjust to your data --- #

# Set batch and topic names.
batch_name = 'my_batch'
topic_name = 'my_topic'

# Data is queried from the first, second, and third indices.
# you can explicitly list columns you would like to query:
data_labels = ['data.data[0]', 'data.data[1]', 'data.data[2]']
# or if the entire array is needed, it can be queried, in this example, simply as 'data.data'.
# This way, when the CitrosData object is created, the array will be automatically divided into separate columns
# data_labels = 'data.data'

# Set method of index assignment as 'scale' or 'bin':
method = 'bin'

# Set time step to construct independent variable column as: Time = rid*time_step.
time_step  = 0.2
# --------------------------- #

# Import 'data_access' and 'error_analysis' modules and create CitrosDB object:
from citros_data_analysis import data_access as da
from citros_data_analysis import error_analysis as analysis
citros = da.CitrosDB()

# Query data:
df = citros.batch(batch_name).topic(topic_name).data(data_labels)

# Construct independent variable column as: Time = rid*time_step.
df['Time'] = df['rid']*time_step

# Construct CitrosData object:
dataset = analysis.CitrosData(df, data_label = data_labels, units = 'm')

# set an independent variable as 'Time' (column, that we constructed previously) by label by `param_label`:
if method == 'bin':
    db = dataset.bin_data(n_bins = 50, param_label = 'Time')
# or
elif method == 'scale':
    db = dataset.scale_data(n_points = 50, param_label = 'Time')
else:
    print('please define method of index assignment: "scale" or "bin"')


# Get statistics.
# When data is binned or interpolated, for each of the index mean values, covariant matrix 
# and standard deviations (the square root the covariant matrix diagonal elements) may be calculated.
# The output table is a pandas DataFrame:
stat = db.get_statistics(return_format = 'citrosStat')

# `stat` contains 3 attributes:
# the mean values (type - pandas.DataFrame):
print('mean values:\n', stat.mean.head(5))

# the standard deviation (type - pandas.DataFrame):
print('standard deviation:\n', stat.std.head(5))

# the covariance matrix (type - pandas.Series):
print('covariance matrix:\n', stat.covar_matrix.head(5))

# Method head(n) of pandas.DataFrame is used to show the first n rows of the table


# Plot statistics.
db.show_statistics()
# by default, it plots +-3 standard deviation boundary.
# To plot for another number of standard deviations, for example for +- 5std boundary: n_std = 5
# you may style area between standard deviation boundaries: by std_area = True fill area with color.
# by std_lines = False - remove lines of the boundary:
db.show_statistics(n_std = 5, std_area = True, std_lines = False)
```
## Correlation Between Variables

For topic 'my_topic' from batch 'my_batch' consider a table where the 'data' column holds dictionaries with keys 'x', 'y', and 'time', as illustrated:

|data                     |
|-------------------------|
|{x: 1, y: 2, time: 0.1}  |
|{x: 4, y: 5, time: 0.2}  |
|...                      |

First, the values from different simulations should be corresponded with each other. For this purpose a common scale may be established through the independent variable. Two methods may be applied. The first one is to divide the independent variable into N ranges, index each, and average the data values within those ranges; it is implemented by `bin_data()` method. The second one is to scale the independent variable between [0,1], set N uniformly distributed points in this range, and interpolate data over this interval; this approach is implemented by method `scale_data()`.

Let's choose 'data.time' as an independent variable, set indices and collect the statistics among different simulations and plot the correlation 'data.x' vs. 'data.y'.

```python
# --- adjust to your data --- #

# Set batch and topic names.
batch_name = 'my_batch'
topic_name = 'my_topic'

# Data labels to plot correlation for
x = 'data.x'
y = 'data.y'

# Independent variable label
independent_var_label = 'data.time'

# Set method of index assignment as 'scale' or 'bin':
method = 'bin'

# Index to plot corelation for:
slice_id = 1
# or if the index number is unknown, `slice_val` parameter may be used to define 
# the approximate value of the independent variable. The nearest to this value index will be set.
# if the method of index assignment is set as 'scale', do not forget that the interval slice_val is [0, 1].
slice_val = 0.1

# To add bounding error to the plot, set bounding_error = True:
bounding_error = False
# --------------------------- #

# Import 'data_access' and 'error_analysis' modules and create CitrosDB object to query data:
from citros_data_analysis import data_access as da
from citros_data_analysis import error_analysis as analysis
citros = da.CitrosDB()

# Query data
df = citros.batch(batch_name).topic(topic_name).data([x, y, independent_var_label])

# Construct CitrosData object, setting 'data.x' and 'data.y' as a data-columns:
dataset = analysis.CitrosData(df, data_label = [x, y], units = 'm')

# Use method scale_data() or bin_data() to get correspondence between different simulation and assign indexes to independent_var_label axis:

if method == 'bin':
    db = dataset.bin_data(n_bins = 50, param_label = independent_var_label)
# or
elif method == 'scale':
    db = dataset.scale_data(n_points = 50, param_label = independent_var_label)
else:
    print('please define method of index assignment: "scale" or "bin"')

# Plot correlation plot for the exact index:
ellipse_param = db.show_correlation(x_col = x, y_col = y,
                                    slice_id = slice_id,
                                    n_std = 3,
                                    bounding_error = bounding_error,
                                    return_ellipse_param = True)

# Print ellipse parameters:
print("ellipse parameters:")
print(f"center: {ellipse_param['x']}, {ellipse_param['y']}")
print(f"width: {ellipse_param['width']}, height: {ellipse_param['height']}")
print(f"angle: {ellipse_param['alpha']}\n")
if bounding_error:
    print(f"radius of the error circle: {ellipse_param['bounding_error']}\n")

# As an alternative, instead of setting the exact value of index (`slice_id`), the approximate
# value of the independent variable may be provided by `slice_val`. Then the nearest to this value index will be adopted.
#the number of error ellipses and their radii are controlled by parameter `n_std`
db.show_correlation(x_col = x, y_col = y,
                    slice_val = slice_val,
                    n_std = [1, 2, 3],
                    bounding_error = bounding_error)
```
## Predictions

Let's assume that in batch 'my_batch' for the topic 'my_topic' there are four simulations, each of them corresponds to the different value of some parameter 'M'. Also let's consider that each cell in the 'data' column contains a dictionary:

|data               |
|-------------------|
|{x: 1, time: 0.1}  |
|{x: 4, time: 0.2}  |
|...                |

To conduct a comparison of the values of different simulations, the correspondence between these values should be established. That may be done by assigning indices through independent variable. One of the approach is to to divide the independent variable into N ranges, index each, and average the data values within those ranges; it is implemented by `bin_data()` method. The second one is to scale the independent variable between [0,1], set N uniformly distributed points in this range, and interpolate data over this interval; this approach is implemented by method `scale_data()`.

Let's set 'data.time' as an independent variable and find the prediction for the 'data.x' variable for value of M = M0. 

```python
# --- adjust to your data --- #

# Set batch and topic names.
batch_name = 'my_batch'
topic_name = 'my_topic'

# Data labels to plot correlation for 
data_label = 'data.x'

# Independent variable label
independent_var_label = 'data.time'

# Set method of index assignment as 'scale' or 'bin':
method = 'bin'

# Define which simulation (sid) corresponds to which value of parameter M:
# Let's assume that sid = 0 corresponds to M = -1.5; sid = 1, M = 0, sid = 2, M = 2.5; sid = 3, M = 4:
M = {0: -1.5, 1: 0, 2: 2.5, 3: 4}

# And we would like to find value for the M = 1:
M0 = 1

# Prediction method: 'neural_net' - neural net regression, 'poly' - polynomial regression ('poly') or 'gmm' - gaussian mixture model
predict_method = 'poly'
# --------------------------- #

# Import 'data_access' and 'error_analysis' modules and create CitrosDB object to query data:
from citros_data_analysis import data_access as da
from citros_data_analysis import error_analysis as analysis
citros = da.CitrosDB()

# Create CitrosDataArray object:
db_array = analysis.CitrosDataArray()

# Query data for each of the M parameter, assign indexes over 'data.time' axis to set
# correspondence between different simulations and pass the result to CitrosDataArray that we created:
for s, m in M.items():
    #query data
    df = citros.batch(batch_name).topic(topic_name).sid(s).data([data_label, independent_var_label])

    #create CitrosData object and set 'data.t' as a parameter.
    dataset = analysis.CitrosData(df,  
                                 data_label = data_label,
                                 parameters = {'M': m})
    if method == 'bin':
        db = dataset.bin_data(n_bins = 50, param_label = independent_var_label, show_fig = False)
    # or
    elif method == 'scale':
        db = dataset.scale_data(n_points = 50, param_label = independent_var_label, show_fig = False)
    else:
        print('please define method of index assignment: "scale" or "bin"')

    #store in CitrosDataArray by add_db() method
    db_array.add_db(db)

# Get the prediction with the defined prediction method:

if predict_method == 'poly':
    result = db_array.get_prediction(parameters = {'M': M0},
                                    method = 'poly', 
                                    n_poly = 2,
                                    show_fig = True)
elif predict_method == 'neural_net':
    result = db_array.get_prediction(parameters = {'M': M0}, 
                                     method = 'neural_net',
                                     activation='tanh', max_iter = 200, solver='lbfgs',
                                     hidden_layer_sizes = (8,), random_state = 9,
                                     show_fig = True)
elif predict_method == 'gmm':
    result = db_array.get_prediction(parameters = {'M': M0}, 
                                     method = 'gmm',
                                     show_fig = True)
else:
    print('define prediction method as "neural_net", "poly" or "gmm"')
    result = None

if result is not None:
    print(result.head(5))
```
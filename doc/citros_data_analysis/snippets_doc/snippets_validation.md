---
toc_max_heading_level: 4
hide_title: true
sidebar_label: 'Validation'
---
# Validation

## Overview

Let's consider a table for topic 'my_topic' from the batch 'my_batch', created by simulation 'my_simulation', where each row under the 'data' column contains dictionaries with keys 'x', 'y', and 'z', as illustrated:



|data                |
|--------------------|
|{x: 1, y: 2, z: 3}  |
|{x: 4, y: 5, z: 6}  |
|...                 |


Let's assume that there are number of simulations (sids) and we would like to perform several test on this data to evaluate the quality of the simulation results.

The pipeline is the following: query data, define the independent variable (that is used to establish the correspondence between different simulations), set test parameters.


## Checking the Standard Deviation Boundary

Whether the standard deviation boundary is within the limits.

```python
# --- adjust to your data --- #

# Set simulation, batch and topic names:
simulation_name = 'my_simulation'
batch_name = 'my_batch'
topic_name = 'my_topic'

# Data labels
data_labels = ['data.x', 'data.y', 'data.z']

# Set time step to construct independent variable column as: Time = rid*time_step.
time_step  = 0.2

# 'method' defines how the index assignment will be done:
#    - 'scale': by scaling independent variable to unit interval and interpolating data on this interval,
#    - 'bin': by dividing independent variable on bins and calculating mean data values among points fallen in each bin
method = 'bin'

# limits: a one value to set the same +-limits to each element of the vector, for examples limits = 0.25
#        list of values to set +-limits for each vector element, for examples limits = [0.25, 0.5, 100]
#        list of lists to set lower and upper intervals separately, for examples limits = [0.25, [-0.3, 0.8], [-150, 100]]
limits = [0.25, [-0.3, 0.8], [-150, 100]]

# number of standard deviations in standard deviation boundary
n_std = 3

# whether nan values are treated as passed test or not
nan_passed = True

# to style the output plot:
# std_area - set True to fill with color standard deviation boundary
std_area = False
# std_lines - set False to remove standard deviation boundary lines
std_lines = True
# std_color - set standard deviation boundary color, default 'b'
std_color = 'b'
# --------------------------- #

from citros import CitrosDB, Validation

citros = CitrosDB()

# query data.
df = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).data(data_labels)
# construct independent variable column as: Time = rid*time_step
df['Time'] = df['rid']*time_step

# construct Validation object. It determines how the data will be preprocessed: 
#'data_label' determine data columns, 
#'param_label' is for independent variable that will be used for defining indexes and setting correspondence between different sids 
#'method' defines how the index assignment will be done:
#    - 'scale': by scaling independent variable to unit interval and interpolating data on this interval,
#    - 'bin': by dividing independent variable on bins and calculating mean data values among points fallen in each bin
#'num' determines number of points if method set as 'scale' or bins if 'method' set as 'bin':
V = Validation(df, data_label = data_labels, param_label = 'Time', 
                  method = method, num = 50, units = 'm')

# Set test
log, table, fig = V.std_bound_test(limits = limits, n_std = n_std, nan_passed = nan_passed, 
            std_area = std_area, std_lines = std_lines, std_color = std_color)

# print the report of the test:
log.print()

#DataFrame table that for each point indicates whether it passes the test or not:
print(table.head(5)) #method head(n) shows first n rows of the DataFrame table
```
## Checking the Mean Value
Test whether the mean values are within the defined boundaries.
Even when some points of the individual simulations may exceed the limits, but the test will be passed for those, whose mean values are within limits.

```python
# --- adjust to your data --- #

# Set simulation, batch and topic names:
simulation_name = 'my_simulation'
batch_name = 'my_batch'
topic_name = 'my_topic'

# Data labels
data_labels = ['data.x', 'data.y', 'data.z']

# Set time step to construct independent variable column as: Time = rid*time_step.
time_step  = 0.2

# 'method' defines how the index assignment will be done:
#    - 'scale': by scaling independent variable to unit interval and interpolating data on this interval,
#    - 'bin': by dividing independent variable on bins and calculating mean data values among points fallen in each bin
method = 'bin'

# limits: a one value to set the same +-limits to each element of the vector, for examples limits = 0.25
#        list of values to set +-limits for each vector element, for examples limits = [0.25, 0.5, 100]
#        list of lists to set lower and upper intervals separately, for examples limits = [0.25, [-0.3, 0.8], [-150, 100]]
limits = [0.05, 0.05, [-1, 3]]

# whether nan values are treated as passed test or not
nan_passed = True
# --------------------------- #

from citros import CitrosDB, Validation

citros = CitrosDB()

# query data.
df = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).data(data_labels)
# construct independent variable column as: Time = rid*time_step
df['Time'] = df['rid']*time_step

# construct Validation object. It determines how the data will be preprocessed: 
#'data_label' determine data columns, 
#'param_label' is for independent variable that will be used for defining indexes and setting correspondence between different sids 
#'method' defines how the index assignment will be done:
#    - 'scale': by scaling independent variable to unit interval and interpolating data on this interval,
#    - 'bin': by dividing independent variable on bins and calculating mean data values among points fallen in each bin
#'num' determines number of points if method set as 'scale' or bins if 'method' set as 'bin':
V = Validation(df, data_label = data_labels, param_label = 'Time', 
                  method = method, num = 50, units = 'm')

# Set test
log, table, fig = V.mean_test(limits = limits)

# print the report of the test:
log.print()

#DataFrame table that for each point indicates whether it passes the test or not:
print(table.head(5)) #method head(n) shows first n rows of the DataFrame table
```
## Checking the Standard Deviation Values
Whether the standard deviation values do not exceed the limits.

```python
# --- adjust to your data --- #

# Set simulation, batch and topic names:
simulation_name = 'my_simulation'
batch_name = 'my_batch'
topic_name = 'my_topic'

# Data labels
data_labels = ['data.x', 'data.y', 'data.z']

# Set time step to construct independent variable column as: Time = rid*time_step.
time_step  = 0.2

# 'method' defines how the index assignment will be done:
#    - 'scale': by scaling independent variable to unit interval and interpolating data on this interval,
#    - 'bin': by dividing independent variable on bins and calculating mean data values among points fallen in each bin
method = 'bin'

# limits: a one value to set the same limit to each element of the vector, for examples limits = 0.25
#        list of values to set the limits for each vector element, for examples limits = [0.25, 0.5, 100]
limits = [0.25, 0.5, 100]

# number of standard deviations in standard deviation boundary
n_std = 3

# whether nan values are treated as passed test or not
nan_passed = True

# to style the output plot:
# std_area - set True to fill with color standard deviation boundary
std_area = False
# std_lines - set False to remove standard deviation lines
std_lines = True
# std_color - set standard deviation color, default 'b'
std_color = 'b'
# --------------------------- #

from citros import CitrosDB, Validation

citros = CitrosDB()

# query data.
df = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).data(data_labels)
# construct independent variable column as: Time = rid*time_step
df['Time'] = df['rid']*time_step

# construct Validation object. It determines how the data will be preprocessed: 
#'data_label' determine data columns, 
#'param_label' is for independent variable that will be used for defining indexes and setting correspondence between different sids 
#'method' defines how the index assignment will be done:
#    - 'scale': by scaling independent variable to unit interval and interpolating data on this interval,
#    - 'bin': by dividing independent variable on bins and calculating mean data values among points fallen in each bin
#'num' determines number of points if method set as 'scale' or bins if 'method' set as 'bin':
V = Validation(df, data_label = data_labels, param_label = 'Time', 
                  method = method, num = 50, units = 'm')

# Set test
log, table, fig = V.std_test(limits = limits, n_std = n_std, nan_passed = nan_passed, 
            std_area = std_area, std_lines = std_lines, std_color = std_color)

# print the report of the test:
log.print()

#DataFrame table that for each point indicates whether it passes the test or not:
print(table.head(5)) #method head(n) shows first n rows of the DataFrame table
```
## Checking the Individual Simulations


```python
# --- adjust to your data --- #

# Set simulation, batch and topic names:
simulation_name = 'my_simulation'
batch_name = 'my_batch'
topic_name = 'my_topic'

# Data labels
data_labels = ['data.x', 'data.y', 'data.z']

# Set time step to construct independent variable column as: Time = rid*time_step.
time_step  = 0.2

# 'method' defines how the index assignment will be done:
#    - 'scale': by scaling independent variable to unit interval and interpolating data on this interval,
#    - 'bin': by dividing independent variable on bins and calculating mean data values among points fallen in each bin
method = 'bin'

# limits: a one value to set the same +-limits to each element of the vector, for examples limits = 0.25
#        list of values to set +-limits for each vector element, for examples limits = [0.25, 0.5, 100]
#        list of lists to set lower and upper intervals separately, for examples limits = [0.25, [-0.3, 0.8], [-150, 100]]
limits = [0.05, 0.15, [-1, 3]]

# whether nan values are treated as passed test or not
nan_passed = True
# --------------------------- #

from citros import CitrosDB, Validation

citros = CitrosDB()

# query data.
df = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).data(data_labels)
# construct independent variable column as: Time = rid*time_step
df['Time'] = df['rid']*time_step

# construct Validation object. It determines how the data will be preprocessed: 
#'data_label' determine data columns, 
#'param_label' is for independent variable that will be used for defining indexes and setting correspondence between different sids 
#'method' defines how the index assignment will be done:
#    - 'scale': by scaling independent variable to unit interval and interpolating data on this interval,
#    - 'bin': by dividing independent variable on bins and calculating mean data values among points fallen in each bin
#'num' determines number of points if method set as 'scale' or bins if 'method' set as 'bin':
V = Validation(df, data_label = data_labels, param_label = 'Time', 
                  method = method, num = 50, units = 'm')

# Set test
log, table, fig = V.sid_test(limits = limits)

# print the report of the test:
log.print()

#DataFrame table that for each point indicates whether it passes the test or not:
print(table.head(5)) #method head(n) shows first n rows of the DataFrame table
```
## Norm Limit Test
Test whether the norm of each simulation do not exceed the given limit

```python
# --- adjust to your data --- #

# Set simulation, batch and topic names:
simulation_name = 'my_simulation'
batch_name = 'my_batch'
topic_name = 'my_topic'

# Data labels
data_labels = ['data.x', 'data.y', 'data.z']

# Set time step to construct independent variable column as: Time = rid*time_step.
time_step  = 0.2

# 'method' defines how the index assignment will be done:
#    - 'scale': by scaling independent variable to unit interval and interpolating data on this interval,
#    - 'bin': by dividing independent variable on bins and calculating mean data values among points fallen in each bin
method = 'bin'

# type of the norm:
#     - 'Linf' - test whether absolute maximum of each simulation is less then the limits
#     - 'L2' - test whether for each simulation the Euclidean norm (square root of the sum of the squares) 
#     does not exceed the given limit
norm_type = 'Linf'

# limits: a one value to set the same +-limits to each element of the vector, for examples limits = 0.25
#        list of values to set +-limits for each vector element, for examples limits = [0.25, 0.5, 100]
limits = [0.2, 0.2, 15]
# --------------------------- #

from citros import CitrosDB, Validation

citros = CitrosDB()

# query data.
df = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).data(data_labels)
# construct independent variable column as: Time = rid*time_step
df['Time'] = df['rid']*time_step

# construct Validation object. It determines how the data will be preprocessed: 
#'data_label' determine data columns, 
#'param_label' is for independent variable that will be used for defining indexes and setting correspondence between different sids 
#'method' defines how the index assignment will be done:
#    - 'scale': by scaling independent variable to unit interval and interpolating data on this interval,
#    - 'bin': by dividing independent variable on bins and calculating mean data values among points fallen in each bin
#'num' determines number of points if method set as 'scale' or bins if 'method' set as 'bin':
V = Validation(df, data_label = data_labels, param_label = 'Time', 
                  method = method, num = 50, units = 'm')

# Set test
log, table, fig = V.norm_test(norm_type = norm_type, limits = limits)

# print the report of the test:
log.print()

#DataFrame table that for each point indicates whether it passes the test or not:
print(table.head(5)) #method head(n) shows first n rows of the DataFrame table
```
## Set Multiple Tests
Set several tests at once.

```python
# --- adjust to your data --- #

# Set simulation, batch and topic names:
simulation_name = 'my_simulation'
batch_name = 'my_batch'
topic_name = 'my_topic'

# Data labels
data_labels = ['data.x', 'data.y', 'data.z']

# Set time step to construct independent variable column as: Time = rid*time_step.
time_step  = 0.2

# 'method' defines how the index assignment will be done:
#    - 'scale': by scaling independent variable to unit interval and interpolating data on this interval,
#    - 'bin': by dividing independent variable on bins and calculating mean data values among points fallen in each bin
method = 'bin'

# Define parameters of the tests as dictionaries with key being the test name ('std_bound', 'mean', 'sid', 'norm_L2', 'norm_Linf'):
define_tests = {'std_bound' : {'limits' : [0.2, 0.2, [-2, 4]], 'n_std': 3},
                'norm_Linf' : {'limits' : [0.1, 0.1, 2]}}
# --------------------------- #

from citros import CitrosDB, Validation

citros = CitrosDB()

# query data.
df = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).data(data_labels)
# construct independent variable column as: Time = rid*time_step
df['Time'] = df['rid']*time_step

# construct Validation object. It determines how the data will be preprocessed: 
#'data_label' determine data columns, 
#'param_label' is for independent variable that will be used for defining indexes and setting correspondence between different sids 
#'method' defines how the index assignment will be done:
#    - 'scale': by scaling independent variable to unit interval and interpolating data on this interval,
#    - 'bin': by dividing independent variable on bins and calculating mean data values among points fallen in each bin
#'num' determines number of points if method set as 'scale' or bins if 'method' set as 'bin':
V = Validation(df, data_label = data_labels, param_label = 'Time', 
                  method = method, num = 50, units = 'm')

# Set tests
logs, tables, figs = V.set_tests(test_method = define_tests)

#logs, tables, figs are the dictionaries with the corresponding to each test log, table and fig, 
#where key of the dictionary is the name of the test:
logs['std_bound'].print()
print(tables['norm_Linf'])
```
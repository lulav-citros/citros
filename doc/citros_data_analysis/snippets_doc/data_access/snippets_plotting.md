---
toc_max_heading_level: 4
hide_title: true
sidebar_label: 'Plotting'
---
# Plotting

## Plot with pandas

This type of plot does not require saving the data prior to plotting and can be directly called after querying.

If the data of a topic 'my_topic' in batch 'my_batch', created by simulation 'my_simulation' looks like the following:



|data                |
|--------------------|
|{x: 1, y: 2, z: 3}  |
|{x: 4, y: 5, z: 6}  |
|...                 |


To plot a graph with 'data.y' on the vertical axis versus 'rid' on the horizontal axis, and to separate the data based on 'sid', follow these steps:

```python
from citros import CitrosDB

# --- adjust to your data --- #
simulation_name = 'my_simulation'
batch_name = 'my_batch'
topic_name = 'my_topic'

y = 'data.y'
# --------------------------- #

citros = CitrosDB()
citros.simulation(simulation_name).batch(batch_name).topic(topic_name)\
      .data(y).set_index(['rid','sid']).unstack()[y].plot()
```
## Time Plot

This type of plot does not require saving the data prior to plotting and can be directly called after querying.

If the data for topic 'my_topic' in batch 'my_batch', created by simulation 'my_simulation' looks like the following:

|data                |
|--------------------|
|{x: 1, y: 2, z: 3}  |
|{x: 4, y: 5, z: 6}  |
|...                 |

To plot 'data.x' against Time for each simulation (sid), where `Time` = `time_step` * rid:

```python
from citros import CitrosDB
import matplotlib.pyplot as plt
fig, ax = plt.subplots()

# --- adjust to your data --- #
simulation_name = 'my_simulation'
batch_name = 'my_batch'
topic_name = 'my_topic'

y = 'data.x'
# --------------------------- #

citros = CitrosDB()
citros.simulation(simulation_name).batch(batch_name).topic(topic_name).\
       time_plot(ax, var_name = y, time_step = 0.5, y_label = 'x', title_text = 'x vs. Time')
```
## (y Vs. X)

This type of plot does not require saving the data prior to plotting and can be directly called after querying.

If the data for topic 'my_topic' in batch 'my_batch', created by simulation 'my_simulation' looks like the following:


|data                |
|--------------------|
|{x: 1, y: 2, z: 3}  |
|{x: 4, y: 5, z: 6}  |
|...                 |


To plot a graph with 'data.y' on the vertical axis versus 'data.x' on the horizontal axis, separating data according to simulations (sid), do the following:

```python
from citros import CitrosDB
import matplotlib.pyplot as plt
fig, ax = plt.subplots()

# --- adjust to your data --- #
simulation_name = 'my_simulation'
batch_name = 'my_batch'
topic_name = 'my_topic'

x = 'data.x'
y = 'data.y'
# --------------------------- #

citros = CitrosDB()
citros.simulation(simulation_name).batch(batch_name).topic(topic_name).\
       xy_plot(ax, var_x_name = x, var_y_name = y, x_label = 'x', y_label = 'y', title_text = 'y vs. x')
```
## Plot (y Vs. X)

If the data under the topic 'my_topic' within the batch 'my_batch', created by simulation 'my_simulation' is structured as follows:

|data                |
|--------------------|
|{x: 1, y: 2, z: 3}  |
|{x: 4, y: 5, z: 6}  |
|...                 |

To query this data and plot a graph of 'y vs. x', separating by simulation ids (sid):

```python
from citros import CitrosDB

# --- adjust to your data --- #
simulation_name = 'my_simulation'
batch_name = 'my_batch'
topic_name = 'my_topic'

x = 'data.x'
y = 'data.y'
# --------------------------- #

citros = CitrosDB()
df = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).data([x, y])

fig, ax = citros.plot_graph(df, x, y, '-', title = 'y vs.x')
```
## 3d Plot

If the data under the topic 'my_topic' within the batch 'my_batch', created by simulation 'my_simulation' is structured as follows:

|data                |
|--------------------|
|{x: 1, y: 2, z: 3}  |
|{x: 4, y: 5, z: 6}  |
|...                 |

to query data and make a 3d plot 'z vs. x and y', separating by simulation ids (sid):

```python
from citros import CitrosDB

# --- adjust to your data --- #
simulation_name = 'my_simulation'
batch_name = 'my_batch'
topic_name = 'my_topic'

x = 'data.x'
y = 'data.y'
z = 'data.z'
# --------------------------- #

#specify whether the axis range should be the same for all axes, True by default
scale = False

citros = CitrosDB()
df = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).data([x, y, z])

fig, ax = citros.plot_3dgraph(df, x, y, z, '--', title = 'z vs. x and y', scale = scale)
```
## Shared X-axis

If the data under the topic 'my_topic' within the batch 'my_batch', created by simulation 'my_simulation' is structured as follows:

|data                |
|--------------------|
|{x: 1, y: 2, z: 3}  |
|{x: 4, y: 5, z: 6}  |
|...                 |

to query and make two plots 'y vs. x' and 'z va. x', separating by simulation ids (sid):

```python
from citros import CitrosDB

# --- adjust to your data --- #
batch_name = 'my_batch'
topic_name = 'my_topic'
simulation_name = 'my_simulation'

x = 'data.x'
y = 'data.y'
z = 'data.z'
# --------------------------- #

citros = CitrosDB()
df = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).data([x, y, z])

fig, ax = citros.multiple_y_plot(df, x, [y, z], '--')
```
## Grid of Plots

If the data under the topic 'my_topic' within the batch 'my_batch', created by simulation 'my_simulation' is structured as follows:

|data                |
|--------------------|
|{x: 1, y: 2, z: 3}  |
|{x: 4, y: 5, z: 6}  |
|...                 |

To display a 3 x 3 matrix of graphs, where: (1) for the diagonal plots, show histograms depicting value distributions;
(2) for the off-diagonal plots, illustrate the pairwise relationships between x, y, and z, execute the following:

```python
from citros import CitrosDB

# --- adjust to your data --- #
simulation_name = 'my_simulation'
batch_name = 'my_batch'
topic_name = 'my_topic'

x = 'data.x'
y = 'data.y'
z = 'data.z'
# --------------------------- #

#specify whether the axis range should be the same for both axes, True by default
scale = False

citros = CitrosDB()
df = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).data([x, y, z])

fig, ax = citros.multiplot(df, [x, y, z], '-', scale = scale)
```
## Error Ellipse

If the data of the topic 'my_topic' in batch 'my_batch', created by simulation 'my_simulation' is structured as follows:

|data                |
|--------------------|
|{x: 1, y: 2, z: 3}  |
|{x: 4, y: 5, z: 6}  |
|...                 |

To plot error ellipse for the values of 'data.x' and 'data.y' columns that corresponds to the last point (rid) in each simulation (sid):

```python
from citros import CitrosDB

# --- adjust to your data --- #

#specify batch, simulation and topic name
simulation_name = 'my_simulation'
batch_name = 'my_batch'
topic_name = 'my_topic'

#specify columns to plot
x = 'data.x'
y = 'data.y'
# --------------------------- #

#create citrosDB object
citros = CitrosDB()

#get all possible sid:
sid_list = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).get_unique_values('sid')
print(f"sid numbers: {sid_list}")

#for each sid get the last rid:
rid_dict = {}
for s in sid_list:
    rid_dict[s] = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).sid(s).get_max_value('rid')
print(f"rid last numbers: {rid_dict}")

# get the values of 'data.x' and 'data.y', that corresponds to the last rid:
# we are creating an empty DataFrame 'df', query for the values of the exact sid and rid and add the result to the 'df'.
import pandas as pd
df = pd.DataFrame()
for s, r in rid_dict.items():
    df = pd.concat([df, citros.simulation(simulation_name).batch(batch_name).topic(topic_name).sid(s).rid(r).data([x, y])])

# print(df)
fig, ax = citros.plot_sigma_ellipse(df, x_label = x, y_label = y, 
                                    n_std = [1,2,3], plot_origin=False, bounding_error=False,
                                    set_x_label='x', set_y_label = 'y', title = 'Error ellipse')
```
---
toc_max_heading_level: 4
hide_title: true
sidebar_label: 'Batch Content'
---
# Batch Content

## General Information
Show information about batch 'my_batch', created by simulation 'my_simulation':

```python
from citros import CitrosDB

# --- adjust to your data --- #
simulation_name = 'my_simulation'
batch_name = 'my_batch'
# --------------------------- #

citros = CitrosDB()
citros.simulation(simulation_name).batch(batch_name).info().print()
```
## Topic Overview
Show information and structure of the data of the topic 'my_topic' from the batch 'my_batch', created by simulation 'my_simulation':

```python
from citros import CitrosDB

# --- adjust to your data --- #
simulation_name = 'my_simulation'
batch_name = 'my_batch'
topic_name = 'my_topic'
# --------------------------- #

citros = CitrosDB()
citros.simulation(simulation_name).batch(batch_name).topic(topic_name).info().print()
```
## Data Structure
Show table with data structure for topic 'my_topic' of  the batch 'my_batch', created by simulation 'my_simulation':

```python
from citros import CitrosDB

# --- adjust to your data --- #
simulation_name = 'my_simulation'
batch_name = 'my_batch'
topic_name = 'my_topic'
# --------------------------- #

citros = CitrosDB()
citros.simulation(simulation_name).batch(batch_name).topic(topic_name).get_data_structure()
```

## Sizes of the Batches
Display sizes of the all uploaded to the PostgreSQL batches:

```python
from citros import CitrosDB

citros = CitrosDB()
citros.get_batch_sizes()
```

## Sizes of the Batches of the Certain Simulation
Display sizes of the batches, created by simulation simulation 'my_simulation':

```python
from citros import CitrosDB

# --- adjust to your data --- #
simulation_name = 'my_simulation'
# --------------------------- #

citros = CitrosDB()
citros.simulation(simulation_name).get_batch_sizes()
```

## Size of the Certain Batch
Display size of the batch 'my_batch', created by simulation simulation 'my_simulation':

```python
from citros import CitrosDB

# --- adjust to your data --- #
simulation_name = 'my_simulation'
batch_name = 'my_batch'
# --------------------------- #

citros = CitrosDB()
citros.simulation(simulation_name).batch(batch_name).get_batch_sizes()
```

## Maximum Value
Get maximum value of the column 'my_column' for the topic 'my_topic' from the batch 'my_batch', created by simulation 'my_simulation':

```python
from citros import CitrosDB

# --- adjust to your data --- #
simulation_name = 'my_simulation'
batch_name = 'my_batch'
topic_name = 'my_topic'
column_name = 'my_column'
# --------------------------- #

citros = CitrosDB()
max_value = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).get_max_value(column_name)
print(max_value)
```
## Minimum Value
Get minimum value of the column 'my_column' for the topic 'my_topic' from the batch 'my_batch', created by simulation 'my_simulation':

```python
from citros import CitrosDB

# --- adjust to your data --- #
simulation_name = 'my_simulation'
batch_name = 'my_batch'
topic_name = 'my_topic'
column_name = 'my_column'
# --------------------------- #

citros = CitrosDB()
min_value = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).get_min_value(column_name)
print(min_value)
```
## Indices of the Minimum and Maximum Values
Get minimum and maximum values of the column 'my_column' and corresponding to them values of sid and rid for the topic 'my_topic' from the batch 'my_batch', created by simulation 'my_simulation':

```python
from citros import CitrosDB

# --- adjust to your data --- #
simulation_name = 'my_simulation'
batch_name = 'my_batch'
topic_name = 'my_topic'
column_name = 'my_column'
# --------------------------- #

citros = CitrosDB()
max_value, sid_max, rid_max = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).get_max_value(column_name, return_index = True)
min_value, sid_min, rid_min = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).get_min_value(column_name, return_index = True)
print(f"maximum value of the column {column_name} = {max_value}, corresponding sid = {sid_max}, rid = {rid_max}")
print(f"minimum value of the column {column_name} = {min_value}, corresponding sid = {sid_min}, rid = {rid_min}")
```
## List of Unique Values
Get list of simulation ids (sid) for the topic 'my_topic' from the batch 'my_batch', created by simulation 'my_simulation':

```python
from citros import CitrosDB

# --- adjust to your data --- #
simulation_name = 'my_simulation'
batch_name = 'my_batch'
topic_name = 'my_topic'
# --------------------------- #

citros = CitrosDB()
sid_list = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).get_unique_values('sid')
print(sid_list)
```
## Number of Messages
Get number of messages in the batch 'my_batch', created by simulation 'my_simulation', for the topic 'my_topic':

```python
from citros import CitrosDB

# --- adjust to your data --- #
simulation_name = 'my_simulation'
batch_name = 'my_batch'
topic_name = 'my_topic'
# --------------------------- #

citros = CitrosDB()
n = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).get_counts()
print(n)
```
## Number of Messages in Each Simulation
Get number of messages in the batch 'my_batch', created by simulation 'my_simulation', for the topic 'my_topic' for each simulation id (sid):

```python
from citros import CitrosDB

# --- adjust to your data --- #
simulation_name = 'my_simulation'
batch_name = 'my_batch'
topic_name = 'my_topic'
# --------------------------- #

citros = CitrosDB()
n_by_sid = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).get_counts(group_by='sid')
print(n_by_sid)
```
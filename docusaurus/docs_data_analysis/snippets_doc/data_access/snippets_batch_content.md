---
toc_max_heading_level: 4
hide_title: true
sidebar_label: 'Batch Content'
---
# Batch Content

## General Information
Show information about batch 'my_batch':

```python
from citros_data_analysis import data_access as da

# --- adjust to your data --- #
batch_name = 'my_batch'
# --------------------------- #

citros = da.CitrosDB()
citros.batch(batch_name).info().print()
```
## Topic Overview
Show information and structure of the data of the topic 'my_topic' from the batch 'my_batch':

```python
from citros_data_analysis import data_access as da

# --- adjust to your data --- #
batch_name = 'my_batch'
topic_name = 'my_topic'
# --------------------------- #

citros = da.CitrosDB()
citros.batch(batch_name).topic(topic_name).info().print()
```
## Data Structure
Show table with data structure for topic 'my_topic' of  the batch 'my_batch' :

```python
from citros_data_analysis import data_access as da

# --- adjust to your data --- #
batch_name = 'my_batch'
topic_name = 'my_topic'
# --------------------------- #

citros = da.CitrosDB()
citros.batch(batch_name).topic(topic_name).get_data_structure()
```
## Maximum Value
Get maximum value of the column 'my_column' for the topic 'my_topic' from the batch 'my_batch':

```python
from citros_data_analysis import data_access as da

# --- adjust to your data --- #
batch_name = 'my_batch'
topic_name = 'my_topic'
column_name = 'my_column'
# --------------------------- #

citros = da.CitrosDB()
max_value = citros.batch(batch_name).topic(topic_name).get_max_value(column_name)
print(max_value)
```
## Minimum Value
Get minimum value of the column 'my_column' for the topic 'my_topic' from the batch 'my_batch':

```python
from citros_data_analysis import data_access as da

# --- adjust to your data --- #
batch_name = 'my_batch'
topic_name = 'my_topic'
column_name = 'my_column'
# --------------------------- #

citros = da.CitrosDB()
min_value = citros.batch(batch_name).topic(topic_name).get_min_value(column_name)
print(min_value)
```
## Indices of the Minimum and Maximum Values
Get minimum and maximum values of the column 'my_column' and corresponding to them values of sid and rid for the topic 'my_topic' from the batch 'my_batch':

```python
from citros_data_analysis import data_access as da

# --- adjust to your data --- #
batch_name = 'my_batch'
topic_name = 'my_topic'
column_name = 'my_column'
# --------------------------- #

citros = da.CitrosDB()
max_value, sid_max, rid_max = citros.batch(batch_name).topic(topic_name).get_max_value(column_name, return_index = True)
min_value, sid_min, rid_min = citros.batch(batch_name).topic(topic_name).get_min_value(column_name, return_index = True)
print(f"maximum value of the column {column_name} = {max_value}, corresponding sid = {sid_max}, rid = {rid_max}")
print(f"minimum value of the column {column_name} = {min_value}, corresponding sid = {sid_min}, rid = {rid_min}")
```
## List of Unique Values
Get list of simulation ids (sid) for the topic 'my_topic' from the batch 'my_batch':

```python
from citros_data_analysis import data_access as da

# --- adjust to your data --- #
batch_name = 'my_batch'
topic_name = 'my_topic'
# --------------------------- #

citros = da.CitrosDB()
sid_list = citros.batch(batch_name).topic(topic_name).get_unique_values('sid')
print(sid_list)
```
## Number of Messages
Get number of messages in the batch 'my_batch' for the topic 'my_topic':

```python
from citros_data_analysis import data_access as da

# --- adjust to your data --- #
batch_name = 'my_batch'
topic_name = 'my_topic'
# --------------------------- #

citros = da.CitrosDB()
n = citros.batch(batch_name).topic(topic_name).get_counts()
print(n)
```
## Number of Messages in Each Simulation
Get number of messages in the batch 'my_batch' for the topic 'my_topic' for each simulation id (sid):

```python
from citros_data_analysis import data_access as da

# --- adjust to your data --- #
batch_name = 'my_batch'
topic_name = 'my_topic'
# --------------------------- #

citros = da.CitrosDB()
n_by_sid = citros.batch(batch_name).topic(topic_name).get_counts(group_by='sid')
print(n_by_sid)
```
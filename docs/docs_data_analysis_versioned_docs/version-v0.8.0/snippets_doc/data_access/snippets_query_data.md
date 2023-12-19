---
toc_max_heading_level: 4
hide_title: true
sidebar_label: 'Query Data'
---
# Query Data

## Query All Data

Query data from the batch 'my_batch' for topic 'my_topic':

```python
from citros_data_analysis import data_access as da

# --- adjust to your data --- #
batch_name = 'my_batch'
topic_name = 'my_topic'
# --------------------------- #

citros = da.CitrosDB()
df = citros.batch(batch_name).topic(topic_name).data()

#print first 5 rows of the obtained pandas.DataFrame
print(df.head(5))
```
## Query Exact Simulation

Query data from the batch 'my_batch' for topic 'my_topic' for the exact simulation id (sid) = 1:

```python
from citros_data_analysis import data_access as da

# --- adjust to your data --- #
batch_name = 'my_batch'
topic_name = 'my_topic'
# --------------------------- #

citros = da.CitrosDB()
df = citros.batch(batch_name).topic(topic_name).sid(1).data()

#print first 5 rows of the obtained pandas.DataFrame
print(df.head(5))
```
## Query Several Simulations

Query data from the batch 'my_batch' for topic 'my_topic' for simulation id (sid) = 1 and 2:

```python
from citros_data_analysis import data_access as da

# --- adjust to your data --- #
batch_name = 'my_batch'
topic_name = 'my_topic'
# --------------------------- #

citros = da.CitrosDB()
df = citros.batch(batch_name).topic(topic_name).sid([1, 2]).data()

#print first 5 rows of the obtained pandas.DataFrame
print(df.head(5))
```
## Query First `n` Messages

Query first `n` messages of the each simulation from batch 'my_batch' for topic 'my_topic'. Parameter `rid` is a serial number (starts from 0) in each simulation and by method `rid()` we can set the last rid to query:

```python
from citros_data_analysis import data_access as da

# --- adjust to your data --- #
batch_name = 'my_batch'
topic_name = 'my_topic'
n = 5
# --------------------------- #

citros = da.CitrosDB()
df = citros.batch(batch_name).topic(topic_name).rid(end = n-1).data()
print(df)
```
## Query Every n-th Message

Query every n-th message of each simulation from batch 'my_batch' for topic 'my_topic':

```python
from citros_data_analysis import data_access as da

# --- adjust to your data --- #
batch_name = 'my_batch'
topic_name = 'my_topic'
n = 5
# --------------------------- #

citros = da.CitrosDB()
df = citros.batch(batch_name).topic(topic_name).skip(n).data()

#print first 5 rows of the obtained pandas.DataFrame
print(df.head(5))
```
## Average Before Querying

### Average

Group and average every set of `n` consecutive messages of each simulation run and query averaged data from batch 'my_batch' for topic 'my_topic'. The queried column(s) must be numeric and explicitly specified.

```python
from citros_data_analysis import data_access as da

# --- adjust to your data --- #
batch_name = 'my_batch'
topic_name = 'my_topic'
data_column = 'my_column'
n = 5
# --------------------------- #

citros = da.CitrosDB()
df = citros.batch(batch_name).topic(topic_name).avg(n).data(data_column)

#print first 5 rows of the obtained pandas.DataFrame
print(df.head(5))
```
### Moving Average

Compute moving average with the window size equals `n` and then query each `s`-th message of the result. The queried column(s) must be numeric and explicitly specified.

```python
from citros_data_analysis import data_access as da

# --- adjust to your data --- #
batch_name = 'my_batch'
topic_name = 'my_topic'
data_column = 'my_column'
n = 5
s = 2
# --------------------------- #

citros = da.CitrosDB()
df = citros.batch(batch_name).topic(topic_name).move_avg(n, s).data(data_column)

#print first 5 rows of the obtained pandas.DataFrame
print(df.head(5))
```
## Query Array Data

#### Retrieve One Column
Let's consider a table for topic 'my_topic' from the batch 'my_batch', where each row under the 'data' column holds a dictionary (json-object) and within this dictionary, the key 'data' maps to a array of values, as shown:


|data                 |
|---------------------|
|{data: [1, 2, 3...]} |
|{data: [4, 5, 6...]} |
|...                  |


To extract the values from the first indexes from these arrays, follow these steps:

```python
from citros_data_analysis import data_access as da

# --- adjust to your data --- #
batch_name = 'my_batch'
topic_name = 'my_topic'
column_name = 'data.data[0]'
# --------------------------- #

citros = da.CitrosDB()

# index starts from 0, so refer to the first index as "[0]"
df = citros.batch(batch_name).topic(topic_name).data(column_name)

#print first 5 rows of the obtained pandas.DataFrame
print(df.head(5))
```
#### Retrieve Several Columns
Let's consider a table for topic 'my_topic' from the batch 'my_batch', where each row under the 'data' column holds a dictionary and within this dictionary, the key 'val' maps to a list of values, as shown:


|data                 |
|---------------------|
|{val: [1, 2, 3...]}  |
|{val: [4, 5, 6...]}  |
|...                  |


To extract the values, for example, from the first and second indexes from these arrays, follow these steps:

```python
from citros_data_analysis import data_access as da

# --- adjust to your data --- #
batch_name = 'my_batch'
topic_name = 'my_topic'
column_names = ['data.val[0]', 'data.val[1]']
# --------------------------- #

citros = da.CitrosDB()

# index starts from 0, so refer to the first index as "[0]" and to the second as "[1]"
df = citros.batch(batch_name).topic(topic_name).data(column_names)

#print first 5 rows of the obtained pandas.DataFrame
print(df.head(5))
```
#### Divide Array By Columns
Suppose for topic 'my_topic' from the batch 'my_batch' every row in the 'data' column contains a dictionary and within this dictionary, the 'data' key corresponds to a list that has a length of 3, as illustrated below:

|data              |
|------------------|
|{data: [1, 2, 3]} |
|{data: [4, 5, 6]} |
|...               |

To extract these values into separate columns and label them as 'x', 'y', and 'z', proceed as follows:

```python
from citros_data_analysis import data_access as da

# --- adjust to your data --- #
batch_name = 'my_batch'
topic_name = 'my_topic'
# --------------------------- #

new_column_names = ['x', 'y', 'z']
query = ['data.data['+str(i)+']' for i in range(len(new_column_names))]

citros = da.CitrosDB()
df = citros.batch(batch_name).topic(topic_name).data(query)
df.rename({query[i]: new_column_names[i] for i in range(len(query))}, axis = 1, inplace = True)

#print first 5 rows of the obtained pandas.DataFrame
print(df.head(5))
```
## Query Json-object Data

For topic 'my_topic' from batch 'my_batch' consider a table where the 'data' column holds dictionaries with keys 'x', 'y', and 'z', as illustrated:

|data                |
|--------------------|
|{x: 1, y: 2, z: 3}  |
|{x: 4, y: 5, z: 6}  |
|...                 |

To retrieve only the data corresponding to the keys 'x' and 'y':

```python
from citros_data_analysis import data_access as da

# --- adjust to your data --- #
batch_name = 'my_batch'
topic_name = 'my_topic'
column_names = ['data.x', 'data.y']
# --------------------------- #

citros = da.CitrosDB()

df = citros.batch(batch_name).topic(topic_name).data(column_names)

#print first 5 rows of the obtained pandas.DataFrame
print(df.head(5))
```
## Query Mixed Format Data

If data has a very complex format, combining json-arrays and json-objects nested inside each other, for example like:

|data                           |
|-------------------------------
|{coord: {v: [0, {w: [1]} ] } } |
|{coord: {v: [0, {w: [2]} ] } } |
|...                            |

to retrieve values from array under the key 'w', batch is 'my_batch' and topic is 'my_topic':

```python
from citros_data_analysis import data_access as da

# --- adjust to your data --- #
batch_name = 'my_batch'
topic_name = 'my_topic'
column_name = 'data.coord.v[1].w[0]'
# --------------------------- #

citros = da.CitrosDB()

df = citros.batch(batch_name).topic(topic_name).data(column_name)

#print first 5 rows of the obtained pandas.DataFrame
print(df.head(5))
```
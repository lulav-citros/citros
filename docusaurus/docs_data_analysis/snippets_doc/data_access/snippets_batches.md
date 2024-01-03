---
toc_max_heading_level: 4
hide_title: true
sidebar_label: 'Batches'
---
# Batches

## All Batches
Get overview about the batches:

```python
from citros_data_analysis import data_access as da

citros = da.CitrosDB()
citros.search_batch().print()
```
## Last Created Batch

Show information about my last created batch:

```python
from citros_data_analysis import data_access as da

citros = da.CitrosDB()
citros.search_batch(-1, user = 'me').print()
```
## Exact Batch

Show information about exact batch 'my_batch':

```python
from citros_data_analysis import data_access as da

# --- adjust to your data --- #
batch_name = 'my_batch'
# --------------------------- #

citros = da.CitrosDB()
citros.search_batch(batch_name).print()
```
## Exact Batch in the Exact Repository

Show information about the exact batch 'my_batch' in the repository 'my_repository':

```python
from citros_data_analysis import data_access as da

# --- adjust to your data --- #
repo_name = 'my_repository'
batch_name = 'my_batch'
# --------------------------- #

citros = da.CitrosDB()
citros.repo(repo_name).search_batch(batch_name).print()
```
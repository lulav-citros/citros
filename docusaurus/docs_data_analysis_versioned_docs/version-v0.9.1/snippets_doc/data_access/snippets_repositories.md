---
toc_max_heading_level: 4
hide_title: true
sidebar_label: 'Repositories'
---
# Repositories

## All Repositories
Get overview about the repositories:

```python
from citros_data_analysis import data_access as da

citros = da.CitrosDB()
citros.search_repo().print()
```
## Exact Repository

Get overview about exact repository 'my_repository':

```python
from citros_data_analysis import data_access as da

# --- adjust to your data --- #
repo_name = 'my_repository'
# --------------------------- #

citros = da.CitrosDB()
citros.search_repo(repo_name).print()
```
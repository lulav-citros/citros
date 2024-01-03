---
toc_max_heading_level: 4
hide_title: true
sidebar_label: 'Users'
---
# Users

## Table of Users

Show table with user's information

```python
from citros_data_analysis import data_access as da

citros = da.CitrosDB()
citros.get_users()
```
## Users and Repositories They Created

Print user's information as dictionary, including information about repositories they created:

```python
from citros_data_analysis import data_access as da

citros = da.CitrosDB()
citros.search_user(order_by = 'name').print()
```
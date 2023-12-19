---
toc_max_heading_level: 4
hide_title: true
sidebar_position: 2
sidebar_label: 'Repository Overview'
description: 'Information about repositories'
---
# Repository Overview

Projects are organized and stored within *repositories*. Each repository may comprise multiple [*batches* (tables)](batch_overview.md#batch-overview), that contain specific datasets, divided by [*topics*](query_data.md#query-data). Method [**repo_info()**](#repository-information) provides an overview of the existing repositories, offering insights into their properties and contents. When you wish to work with a specific repository, you can utilize the [**repo()**](#setting-repository) method to set the target repository. This can be particularly useful to narrow down searches or operations to batches within that chosen repository. Methods [**get_repo()** and **get_repo_id()**](#current-repository-name-and-id) return the name and the id of the current repository, respectively.

## Repository Information

To display the main information about the repositories, such as repositories names, ids, times of creation and update, description and git source, method [**repo_info()**](../documentation/data_access/citros_db.md#citros_data_analysis.data_access.citros_db.CitrosDB.repo_info) is applied. The result is a [**CitrosDict**](../documentation/data_access/citros_dict.md#citros_data_analysis.data_access.citros_dict.CitrosDict) object. It inherits behavior of an ordinary python dictionary, but has some additional methods, like [**print()**](../documentation/data_access/citros_dict.md#citros_data_analysis.data_access.citros_dict.CitrosDict.print) method. To display the information about all repositories:

```python
>>> citros.repo_info().print()
```
```js
{
 'projects': {
   'repo_id': 'rrrrrrrr-1111-2222-aaaa-555555555555',
   'description': 'statistics',
   'created_at': '2023-05-18T12:55:41.144263+00:00',
   'updated_at': '2023-08-18T11:25:31.356987+00:00',
   'git': '...'
 },
 'citros_project': {
   'repo_id': 'rrrrrrrr-1111-2222-3333-444444444444',
   'description': 'citros runs',
   'created_at': '2023-05-20T09:57:44.632361+00:00',
   'updated_at': '2023-08-20T07:45:11.136632+00:00',
   'git': '...'
 }
}
```

<details>
  <summary>more about CitrosDict</summary>

`print()` method allows to print the output with proper indents, enhancing readability. However, it is always an option to display the result using the standard Python print method, displaying it as a regular dictionary:

```python
>>> print(citros.repo_info())
```
```text
{'projects': {'repo_id': 'rrrrrrrr-1111-2222-aaaa-555555555555', 'description': 'statistics', ...}, 'citros_project': {'repo_id': 'rrrrrrrr-1111-2222-3333-444444444444', ...}}
 ```

[**CitrosDict**](../documentation/data_access/citros_dict.md#citros_data_analysis.data_access.citros_dict.CitrosDict) object can be converted to json string by the method [**to_json()**](../documentation/data_access/citros_dict.md#citros_data_analysis.data_access.citros_dict.CitrosDict.to_json) and printed:
```python
>>> print(citros.repo_info().to_json())
```
```js
{
  "projects": {
    "repo_id": "rrrrrrrr-1111-2222-aaaa-555555555555",
    "description": "statistics",
    "created_at": "2023-05-18T12:55:41.144263+00:00",
    "updated_at": "2023-08-18T11:25:31.356987+00:00",
    "git": "..."
  },
  "citros_project": {
    "repo_id": "rrrrrrrr-1111-2222-3333-444444444444",
    "description": "citros runs",
    "created_at": "2023-05-20T09:57:44.632361+00:00",
    "updated_at": "2023-08-20T07:45:11.136632+00:00",
    "git": "..."
  }
}
```
or printed by the method [**print()**](../documentation/data_access/citros_dict.md#citros_data_analysis.data_access.citros_dict.CitrosDict.print) as it was shown above.

</details>

There are several ways to search for the exact repository. Passing a string that matches the repository name, the search will yield all repositories whose names correspond to the provided string:

```python
>>> citros.repo_info('citros').print()
```
```js
{
 'citros_project': {
   'repo_id': 'rrrrrrrr-1111-2222-3333-444444444444',
   'description': 'citros runs',
   'created_at': '2023-05-20T09:57:44.632361+00:00',
   'updated_at': '2023-08-20T07:45:11.136632+00:00',
   'git': '...'
 }
}
```

By providing the repository id:

```python
>>> citros.repo_info('rrrrrrrr-1111-2222-aaaa-555555555555').print()
```
```js
{
 'projects': {
   'repo_id': 'rrrrrrrr-1111-2222-aaaa-555555555555',
   'description': 'statistics',
   'created_at': '2023-05-18T12:55:41.144263+00:00',
   'updated_at': '2023-08-18T11:25:31.356987+00:00',
   'git': '...'
 }
}
```

Or it is possible to select the last created repository by passing int value -1:

```python
>>> citros.repo_info(-1).print()
```
```js
{
 'citros_project': {
   'repo_id': 'rrrrrrrr-1111-2222-3333-444444444444',
   'description': 'citros runs',
   'created_at': '2023-05-20T09:57:44.632361+00:00',
   'updated_at': '2023-08-20T07:45:11.136632+00:00',
   'git': '...'
 }
}
```

To retrieve the second-to-last created repository, provide -2 as an argument. Similarly, to select the repository that was created first, use 0; for the second created repository, use 1, and so on.

To perform search by another field, specify it by `search_by` argument and provide `search` argument of the appropriate format. Provide str to search by 'description' and 'git' fields, for example to display all repositories with word 'statistics' in 'description':

```python
>>> citros.repo_info('statistics', search_by = 'description').print()
```
```js
{
 'projects': {
   'repo_id': 'rrrrrrrr-1111-2222-aaaa-555555555555',
   'description': 'statistics',
   'created_at': '2023-05-18T12:55:41.144263+00:00',
   'updated_at': '2023-08-18T11:25:31.356987+00:00',
   'git': '...'
 }
}
```

To search by date fields, choose one of the key word for `search_by` field - 'created_after', 'created_before', 'updated_after' or 'updated_before' - and specify date in `search` argument in the one of the following format:
- 'dd-mm-yyyy hh:mm:ss +hh:mm' - the full date, time and time zone: 
- 'dd-mm-yyyy hh:mm:ss' - date and time without time zone (by default timezone +00:00)
- 'dd-mm-yyyy' / 'dd-mm' / 'dd' - only date. This way, time in the search is set to be 00:00:00
- 'hh:mm:ss' / 'hh:mm' - only time, in this case the date is set as today.

For example, to display all the repositories that were created after 19 May:

```python
>>> citros.repo_info('19-05', search_by = 'created_after').print()
```
```js
{
 'citros_project': {
   'repo_id': 'rrrrrrrr-1111-2222-3333-444444444444',
   'description': 'citros runs',
   'created_at': '2023-05-20T09:57:44.632361+00:00',
   'updated_at': '2023-08-20T07:45:11.136632+00:00',
   'git': '...'
 }
}
```

And to show the repositories that were updated before 11:00 of the current day, do the following:

```python
>>> citros.repo_info('11:00', search_by = 'updated_before').print()     
```
```js
{
 'projects': {
   'repo_id': 'rrrrrrrr-1111-2222-aaaa-555555555555',
   'description': 'statistics',
   'created_at': '2023-05-18T12:55:41.144263+00:00',
   'updated_at': '2023-08-18T11:25:31.356987+00:00',
   'git': '...'
 },
 'citros_project': {
   'repo_id': 'rrrrrrrr-1111-2222-3333-444444444444',
   'description': 'citros runs',
   'created_at': '2023-05-20T09:57:44.632361+00:00',
   'updated_at': '2023-08-20T07:45:11.136632+00:00',
   'git': '...'
 }
}
```

The `order_by` parameter allows to define the sorting order of the output based on a chosen field. To display the output in ascending order by one or multiple fields, you can simply list those fields within the `order_by` parameter. If there's only one field, it can be directly passed as a string argument. For instance, in the previous example, you could use the following to arrange the output in ascending order by the repository names:

```python
>>> citros.repo_info('11:00', search_by = 'updated_before', order_by = 'name').print()
```
```js 
{
 'citros_project': {
   'repo_id': 'rrrrrrrr-1111-2222-3333-444444444444',
   'description': 'citros runs',
   'created_at': '2023-05-20T09:57:44.632361+00:00',
   'updated_at': '2023-08-20T07:45:11.136632+00:00',
   'git': '...'
 },
 'projects': {
   'repo_id': 'rrrrrrrr-1111-2222-aaaa-555555555555',
   'description': 'statistics',
   'created_at': '2023-05-18T12:55:41.144263+00:00',
   'updated_at': '2023-08-18T11:25:31.356987+00:00',
   'git': '...'
 } 
}
```

To specify whether the descending or ascending order should be applied, pass argument as a dict. For example, to order by time of creation in descending order, so the last created will be the first in the output, do the following:

```python
>>> citros.repo_info('11:00', search_by = 'updated_before', order_by = {'created_at': 'desc'}).print()
```
```js
{
 'citros_project': {
   'repo_id': 'rrrrrrrr-1111-2222-3333-444444444444',
   'description': 'citros runs',
   'created_at': '2023-05-20T09:57:44.632361+00:00',
   'updated_at': '2023-08-20T07:45:11.136632+00:00',
   'git': '...'
 },
 'projects': {
   'repo_id': 'rrrrrrrr-1111-2222-aaaa-555555555555',
   'description': 'statistics',
   'created_at': '2023-05-18T12:55:41.144263+00:00',
   'updated_at': '2023-08-18T11:25:31.356987+00:00',
   'git': '...'
 } 
}
```

By default, all repositories are displayed, regardless of the creator. To exclusively view the repositories that belong to you, set `user` = 'me'. To display 

```python
>>> citros.repo_info('project', user = 'me').print()
```
```js
{
'citros_project': {
   'repo_id': 'rrrrrrrr-1111-2222-3333-444444444444',
   'description': 'citros runs',
   'created_at': '2023-05-20T09:57:44.632361+00:00',
   'updated_at': '2023-08-20T07:45:11.136632+00:00',
   'git': '...'
 }
}
```

## Setting Repository

Although defining the repository is not necessary, since in different repositories there may be batches with the same name, applying method [**repo()**](../documentation/data_access/citros_db.md#citros_data_analysis.data_access.citros_db.CitrosDB.repo) ensures that only information that corresponds to the exact repository will be displayed. It also may be set when [**CitrosDB**](getting_started.md#connection-to-the-database) object is created (by passing an argument `repo`). 

If the exact repository id is known, it may be passed in the following way:

```python
>>> citros = da.CitrosDB()
>>> citros = citros.repo('rrrrrrrr-1111-2222-3333-444444444444')
```

By default, method [**repo()**](../documentation/data_access/citros_db.md#citros_data_analysis.data_access.citros_db.CitrosDB.repo) returns [**CitrosDB**](getting_started.md#connection-to-the-database) object with set `repo` parameter, which then can be used in a chain, for example, to [get information about batches](batch_overview.md#batch-information), that belong to that repository. Alternatively, the repository may be set to the existing [**CitrosDB**](getting_started.md#connection-to-the-database) object if the parameter `inplace` = True. Let's see how the `inplace` = True affects:

```python
>>> citros = da.CitrosDB()
>>> citros.repo('rrrrrrrr-1111-2222-3333-444444444444')
>>> print("inplace = False by default:")
>>> print(f"current repository name: {citros.get_repo()}")
>>> print(f"current repository id: {citros.get_repo_id()}")
>>> citros.repo('rrrrrrrr-1111-2222-3333-444444444444', inplace = True)
>>> print("\ninplace = True:")
>>> print(f"current repository name: {citros.get_repo()}")
>>> print(f"current repository id: {citros.get_repo_id()}")
```
```text
inplace = False by default:
current repository name: None
current repository id: None

inplace = True:
current repository name: citros_project
current repository id: rrrrrrrr-1111-2222-3333-444444444444
```
About methods [**get_repo()**](../documentation/data_access/citros_db.md#citros_data_analysis.data_access.citros_db.CitrosDB.get_repo) and [**get_repo_id()**](../documentation/data_access/citros_db.md#citros_data_analysis.data_access.citros_db.CitrosDB.get_repo_id) see in the next [subsection](#current-repository-name-and-id). 

Similar to the [**repo_info**](#repository-information), repository may be set by its name:

```python
>>> citros = citros.repo('citros_project')
```

or its order of the creation:

 ```python
>>> citros = citros.repo(-1)
```

In the above example, the most recently created repository is assigned. If the provided repository name has multiple matches, the clarification may be needed. This can be easily achieved by checking the list of repositories by [**repo_info()**](#repository-information) method.

## Current Repository Name and ID

As it was demonstrated above, the current repository name and id may be checked by methods [**get_repo()**](../documentation/data_access/citros_db.md#citros_data_analysis.data_access.citros_db.CitrosDB.get_repo) and [**get_repo_id()**](../documentation/data_access/citros_db.md#citros_data_analysis.data_access.citros_db.CitrosDB.get_repo_id), respectively:

```python
>>> citros = da.CitrosDB()
>>> citros.repo('citros_project', inplace = True)
>>> print(f"current repository name: {citros.get_repo()}")
>>> print(f"current repository id: {citros.get_repo_id()}")
```
```text
current repository name: citros_project
current repository id: rrrrrrrr-1111-2222-3333-444444444444
```

If the repository is not set, both id and name will be None.
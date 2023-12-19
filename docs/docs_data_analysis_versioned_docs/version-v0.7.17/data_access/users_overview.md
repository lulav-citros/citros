---
toc_max_heading_level: 4
hide_title: true
sidebar_position: 4
sidebar_label: 'Users Overview'
description: 'Information about users'
---
# Users Overview

To display the main information about users of the organization, methods [**get_users()**](../documentation/data_access/citros_db.md#citros_data_analysis.data_access.citros_db.CitrosDB.get_users) and [**user_info()**](../documentation/data_access/citros_db.md#citros_data_analysis.data_access.citros_db.CitrosDB.user_info) are used. 

## Table with Users' Information

Method [**get_users()**](../documentation/data_access/citros_db.md#citros_data_analysis.data_access.citros_db.CitrosDB.get_users) display the table with users names and last names and their emails:

```python
>>> citros.get_users()
```
```text
+--------+------------+-----------------------------+
| name   | last name  | email                       |
+--------+------------+-----------------------------+
| alex   | blanc      | alex@mail.com               |
| david  | gilbert    | david@mail.com              |
| mary   | stevenson  | mary@mail.com               |
+--------+------------+-----------------------------+
```

## Dictionary with Users' Information

The [**user_info()**](../documentation/data_access/citros_db.md#citros_data_analysis.data_access.citros_db.CitrosDB.user_info) method allows you to retrieve the main information about users in a [**CitrosDict**](../documentation/data_access/citros_dict.md#citros_data_analysis.data_access.citros_dict.CitrosDict) format, that inherits behavior of an ordinary python dictionary, but has some additional methods, like method [**print()**](../documentation/data_access/citros_dict.md#citros_data_analysis.data_access.citros_dict.CitrosDict.print). The obtained information includes users' first names, last names, emails, as well as lists of repositories they've created and repositories in which they've created batches, with emails serving as the dictionary keys.

To view all users, sorted by their names, execute the following command:

```python
>>> citros.user_info('order_by' = 'name').print()
```
```js
{
 'alex@mail.com': {
   'name': 'alex',
   'last_name': 'blanc',
   'create_repo': [],
   'create_batch_in_repo': ['automaton_lab']
 },
 'david@mail.com': {
   'name': 'david',
   'last_name': 'gilbert',
   'create_repo': ['robot_master', 'automaton_lab'],
   'create_batch_in_repo': ['robot_master']
 },
 'mary@mail.com': {
   'name': 'mary',
   'last_name': 'stevenson',
   'create_repo': ['mech_craft'],
   'create_batch_in_repo': ['mech_craft', 'robot_master']
 }
}
```
The order of the output may be set according to 'name', 'last_name' or 'email'.

In the example above, the organization has three members: David, Mary, and Alex. It is evident that David created two repositories, namely 'robot_master' and 'automaton_lab,' and generated batches in the former one. Mary established one repository, 'mech_craft,' and generated batches both in 'mech_craft' and 'robot_master' repositories. And Alex only created batches in the 'automaton_lab' repository.

To display information about a specific user, such as Alex, you can choose to search by email (the default search), by name or by last name. In the latter two cases, set the `search_by` parameter to 'name' and 'last_name,' respectively.

```python
>>> citros.user_info('alex@mail.com').print()
>>> citros.user_info('alex', search_by = 'name').print()
>>> citros.user_info('blanc', search_by = 'last_name').print()
```
The output in all this cases will be:

```js
{
 'alex@mail.com': {
   'name': 'alex',
   'last_name': 'blanc',
   'create_repo': [],
   'create_batch_in_repo': ['automaton_lab']
 }
}
```

When a specific repository is set using the [**repo()**](repository_overview.md#setting-repository) method, the method displays information only considered the set repository: about user who created this repository and the users who have created batches within it:

```python
>>> citros.repo('robot_master').user_info().print()
```
```js
{
'david@mail.com': {
   'name': 'david',
   'last_name': 'gilbert',
   'create_repo': ['robot_master'],
   'create_batch_in_repo': ['robot_master']
 },
 'mary@mail.com': {
   'name': 'mary',
   'last_name': 'stevenson',
   'create_repo': [],
   'create_batch_in_repo': ['robot_master']
 }
}
```

If a particular batch is set using the [**batch()**](batch_overview.md#setting-batch) method, it provides details about the user who created this specific batch. Let's assume that in 'robot_master' repository there is a batch 'stress_test'. To show the user, who created this batch, execute the following:

```python
>>> citros.batch('stress_test').user_info().print()
```
```js
{
'mary@mail.com': {
   'name': 'mary',
   'last_name': 'stevenson',
   'create_repo': [],
   'create_batch_in_repo': ['robot_master']
 }
}
```

---
toc_max_heading_level: 4
hide_title: true
sidebar_position: 6
sidebar_label: 'Set multiple tests'
---

## Set multiple tests

It is possible to set several tests by the method [**set_tests**](../documentation/validation/validation.md#citros_data_analysis.validation.validation.Validation.set_tests):

```python
>>> V.set_tests(test_method = {<test_type> : <parameters>})
```
The types of tests and corresponding parameters are provided as a dictionary by a `test_method` parameter, where each test is represented by a key-value pair. The key defines the name of the test, and the corresponding value is a dictionary containing the test parameters. The allowed test_type keywords:

  - 'std_bound' - perform [**std_bound_test()**](standard_deviation_boundary_test.md);
  - 'mean_test' - set [**mean_test()**](mean_value_test.md);
  - 'sid_test' - for [**sid_test()**](testing_each_simulation.md);
  - 'norm_L2' and 'norm_Linf' - set [**norm_test()**](norm_test.md).

For example, to set a standard deviation boundary test and a test on norm $L^2$:

```python
>>> logs, tables, figs = V.set_tests(test_method = 
                                 {'std_bound' : {'limits' : [0.25, 0.3, [-150, 300]], 'n_std': 3},
                                  'norm_L2' : {'limits' : [0.3, 0.35, 450]}})
```
### Returning parameters

The method returns three dictionaris, that containes the output results of each test: 

- `log` : [**CitrosDict**](../documentation/data_access/citros_dict.md#citros_data_analysis.data_access.citros_dict.CitrosDict) - dictionary with test result summary for each test method;

- `table` :  dictionary with [**pandas.DataFrame**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) tables for each test method that specifies for each point whether it passes the test (True) or fails (False).

- `fig` : dictionary with figures [**matplotlib.figure.Figure**](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.Figure) for each test method.

```mermaid
flowchart TD
    Results("set_tests()
    output") --- logs("logs : {
    'std_bound' : log_std,
    'mean' : log_mean,
    'sid' : log_sid,
    'norm_L2' : log_norm,
    'norm_Linf' : log_norm
    }")
    Results ---  tables("tables : {
    'std_bound' : DataFrame,
    'mean' : DataFrame,
    'sid' : DataFrame,
    'norm_L2' : DataFrame,
    'norm_Linf' : DataFrame
    }") -.- DataFrame("DataFrame - pandas.DataFrame")
    
    Results --- figures("figures : {
    'std_bound' : fig_std,
    'mean' : fig_mean,
    'sid' : fig_sid,
    'norm_L2' : fig_norm,
    'norm_Linf' : fig_norm
    }") -.- fig("fig_... - matplotlib.figure.Figure")
```
For example, to get detailed information about the results of the norm test:

```python
>>> logs['norm_L2'].print()
```
```js
{
 'test_param': {
   'limits': [0.3, 0.35, 450]
 },
 'data.x.x_1': {
   'passed': True,
   'pass_rate': 1.0,
...
 }
}
```
To get table that specifies for each simulation whether the norm is less then the given limit:

```python
>>> print(tables['norm_L2'])
```
```js
     data.x.x_1  data.x.x_2  data.x.x_3
sid                                    
1          True        True       False
2          True        True        True
3          True        True       False
```

To get the corresponding figure:

```python
>>> figs['norm_L2']
```
![fig4](img/fig24.png "Fig4")

See [**std_bound_test()**](standard_deviation_boundary_test.md), [**mean_test()**](mean_value_test.md), [**sid_test()**](testing_each_simulation.md) and [**norm_test()**](norm_test.md) for the output detailes.

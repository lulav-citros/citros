---
# Display h3 headings
sidebar_label: 'class CitrosDict'
toc_max_heading_level: 3
hide_title: true
---








    
## Class `CitrosDict` {#citros_data_analysis.data_access.citros_dict.CitrosDict}





```python
class CitrosDict(
    *args,
    **kwargs
)
```


<details>
  <summary>Description</summary>

Citros dictionary

CitrosDict is a dictionary-like object, that allows to print the content as a json-object.



</details>






    
### Method `print` {#citros_data_analysis.data_access.citros_dict.CitrosDict.print}




```python
def print()
```


<details>
  <summary>Description</summary>

Print content of the CitrosDict object in a 'json'-style.

---
#### Examples

Make a CitrosDict object and print it in json-style:

```python
>>> d = da.CitrosDict({'package': 'data_analysis', 'module': 'data_access', 'object': 'CitrosDict', 'style': 'json'})
>>> d.print()
{
 'package': 'data_analysis',
 'module': 'data_access',
 'object': 'CitrosDict',
 'style': 'json'
}
```

</details>


    
### Method `to_json` {#citros_data_analysis.data_access.citros_dict.CitrosDict.to_json}




```python
def to_json()
```


<details>
  <summary>Description</summary>

Convert to json string.

---
#### Returns

&ensp;**str**
:   json_str

---
#### Examples

Make a CitrosDict object, convert it to json string and print it:

```python
>>> d = da.CitrosDict({'package': 'data_analysis', 'module': 'data_access', 'object': 'CitrosDict', 'style': 'json'})
>>> print(d.to_json())
{
  "package": "data_analysis",
  "module": "data_access",
  "object": "CitrosDict",
  "style": "json"
}
```

</details>
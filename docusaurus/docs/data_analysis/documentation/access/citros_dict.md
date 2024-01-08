---
# Display h3 headings
sidebar_label: 'Class CitrosDict'
toc_max_heading_level: 3
hide_title: true
description: 'Documentation'
---

# Class CitrosDict







    
## Class `CitrosDict` {#access.citros_dict.CitrosDict}





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









    
## Method `to_json` {#access.citros_dict.CitrosDict.to_json}




```python
def to_json()
```


<details>
  <summary>Description</summary>

Convert to json string.

#### Returns

Name|Type|Description
--|--|--
|**```out```**|**str**|json_str

</details>
<details>
  <summary>Examples</summary>

Make a CitrosDict object, convert it to json string and print it:

```python
>>> from citros import CitrosDict
>>> d = CitrosDict({'package': 'data_analysis', 'object': 'CitrosDict', 'method': 'to_json', 'style': 'json'})
>>> print(d.to_json())
{
  "package": "citros",
  "object": "CitrosDict",
  'method': 'to_json',
  "style": "json"
}
```

</details>


    
## Method `print` {#access.citros_dict.CitrosDict.print}




```python
def print()
```


<details>
  <summary>Description</summary>

Print content of the CitrosDict object in a 'json'-style.


</details>
<details>
  <summary>Examples</summary>

Make a CitrosDict object and print it in json-style:

```python
>>> from citros import CitrosDict
>>> d = CitrosDict({'package': 'citros', 'object': 'CitrosDict', 'method': 'print', 'style': 'json'})
>>> d.print()
{
 'package': 'citros',
 'object': 'CitrosDict',
 'method': 'print',
 'style': 'json'
}
```

</details>
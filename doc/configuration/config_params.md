# Adding Functions to Parameter Setup

In order to define a function in your parameter setup file, simply replace any constant parameter value with a `function object`.

Function objects provide a powerful and dynamic way to compute and set values in the parameter_setup.json file for ROS 2 nodes. This feature allows for much greater flexibility and dynamism when setting parameters.

## How to Add Function Objects

Function objects are essentially references to functions (either from numpy or user-defined) that will be executed to compute a value for a particular key.

### Numpy Functions

To use a numpy function, simply provide its fully qualified name as the value in the dictionary. For example:

    {
        "my_param": {
            "function": "numpy.add",
            "args": [1, 2]
        }
    }

<details>
<summary>Examples</summary>

#### Simple Arithmetic 

compute the product of two numbers:

    {
        "product_param": {
            "function": "numpy.multiply",
            "args": [4, 7]
        }
    }

#### Using Random Distribution

Generating a random number from a normal distribution with a mean of 0 and standard deviation of 1:

    {
        "random_param": {
            "function": "numpy.random.normal",
            "args": [0, 1]
        }
    }


Drawing a random value between 1 and 10:

    {
        "low": 1.0,
        "high": 10.0,
        "uniform_random_param": {
            "function": "numpy.random.uniform",
            "args": ["low", "high"]
        }
    }

</details>

### User-Defined Functions

For user-defined functions, you need to:

- Define your function in a separate `.py` file and place it under `.citros/parameter_setups/functions`.
- Use the file name (with the `.py` extension) followed by the function name, separated by a colon, as the value of the `function` key.

For instance, if you have a function named `my_function` in a file named `my_functions.py`, you would reference it as:

    {
        "my_param": {
            "function": "my_functions.py:my_function",
            "args": [...]
        }
    }

<details>
<summary>Examples</summary>

#### Read from a CSV File

Suppose you want to load a matrix from a csv file into a parameter of type list of lists of floats. Copy the following function to a python file (let's call it `file_utils.py`) and place it in the `functions` directory:
```python
def load_matrix_from_csv(filename):
    import csv
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        matrix = [list(map(float, row)) for row in reader]
    return matrix
```
Reference it in your parameter_setup.json as:

    {
        "matrix_param": {
            "function": "file_utils.py:load_matrix_from_csv",
            "args": ["my_data.csv"]
        }
    }



#### Function with CITROS Context

Sometimes you may want to access some information that is part of the Citros context. For example, you may want to write a user-defined function that uses the run index of the simulation being run. In such a case, you could write a function with a parameter named `citros_context` (which must appear last in the parameter list):

    def func_with_context(num, citros_context):
        return num + float(citros_context['run_id'])

`citros_context` is a dictionary with key/value pairs describing the current Citros context. Currently the only key is `run_id`, but more may be added in the future. Then, you would call it from your `parameter_setup.json` file:

    "init_speed": {
        "function": "my_func.py:func_with_context",
        "args": [50.0]
    }

Notice that the argument for `citros_context` is added automatically for you - the `args` list only contains the argument for the first parameter (`num`).

</details>

### Full parameter_setup.json Example

Using the following parameter setup file, the `init_angle` parameter in the `analytic_dynamics` node of the `cannon_analytic` package (taken from the `cannon` project), will get a random value each time the simulation is run. Specifically, 60% of the evaluated values will be between 30 and 60 degrees (a standard deviation of 15 around 45). In addition, the parameter `init_speed` will be evaluated to 50.0 on the first run, and will be incremented by one for every subsequent run (see previous example for details):

    {
        "packages": {
            "cannon_analytic": {
                "analytic_dynamics": {
                    "ros__parameters": {
                        "init_speed": {
                            "function": "my_func.py:func_with_context",
                            "args": [50.0]
                        },
                        "init_angle": {
                            "function": "numpy.random.normal",
                            "args": [45, 15]
                        },
                        "dt": 0.01
                    }
                }
            },
            "cannon_numeric": {
                "numeric_dynamics": {
                    "ros__parameters": {
                        "init_speed": 50.0,
                        "init_angle": 30.0,
                        "dt": 0.01
                    }
                }
            },
            "scheduler": {
                "scheduler": {
                    "ros__parameters": {
                        "dt": 0.1
                    }
                }
            }
        }
    }

So, for example, if you run the following command in the `cannon` project:

    citros run -n "my_batch_name" -m "some message" -c 10

and choose `simulation_cannon_analytic`, the simulation will be run 10 times, and each time `init_angle` and `init_speed` will be evaluated to different values. You can see for yourself the evaluated values if you open the `cannon_analytic.yaml` under `.citors/runs/simulation_cannon_analytic/my_batch_name/0/config`, after the run has finished.

## Pitfalls and Gotchas

### User-Defined Functions

- **Import Handling** - Always perform imports inside the function. This ensures the function has all the necessary dependencies when called.
- **Return Types** - The function should return native Python types or numpy scalars. Avoid returning non-scalar numpy values.
- **Function Path** - Only the file name where the function is defined is needed (including the `.py` suffix). Avoid including directory paths.
- **Citros context** - if you're using the `citros_context` parameter in your user-defined function, make sure to add it *last* in the function's parameter list.

### Numpy functions

- Always use the fully qualified name for numpy functions, such as numpy.random.exponential.

- Make sure you use numpy functions such that a scalar is returned. For example, when using [numpy.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html), make sure to have an empty argument list:

    ```bash
    "pos_x": {
            "function": "numpy.random.rand",
            "args": []
        }
    ```
    ...since the arguments are the dimensions of the output array. No arguments will return a native scalar, which is what we want. 

    If you need to return an array, you can write your own user-defined function that wraps the numpy function and converts the numpy array to a native python array.

### General Pitfalls

- **Multi-Level Key References** - When referencing a dictionary key from a function, if the key is not unique across the dictionary, use a multi-level key string to differentiate it, separating dictionary levels with `'.'`. For example: 

        {
            "outer": {
                "inner_a": 5,
                "inner_b": {
                    "function": "numpy.add",
                    "args": ["inner_a", 3]
                }
            },
            "sum": {
                "inner_b" : 42,
                "function": "numpy.add",
                "args": ["outer.inner_b", 2]
            }
        }

- **Circular Dependencies** - Be wary of creating circular dependencies with key references. This will result in a runtime error.

- **Expected Return Types** - Ensure that the functions you use, be they numpy or user-defined, return the value type your ROS simulation expects. Mismatches (e.g., returning an integer when a float is expected) can cause errors in your simulation.

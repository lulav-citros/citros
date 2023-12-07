import pytest
import numpy
from pathlib import Path
from citros.citros_params import citros_params

class MockCitros:
    def __init__(self):
        self.log = self
        self.PARAMS_FUNCTIONS_DIR = Path("input/param_functions")

    # in case we use self.debug in citros_params
    def debug(self, msg):
        print(msg)


@pytest.fixture
def citros_params_obj():
    citros = MockCitros()
    return citros_params(citros)


def test_evaluate_numpy_function(citros_params_obj):
    data = {
        "math_op": {
            "function": "numpy.add",
            "args": [5, 3]
        }
    }
    result = citros_params_obj.evaluate_dictionary(data)
    assert result == {"math_op": 8}

def test_evaluate_user_function1(citros_params_obj):
    # Ensure you have a function in your specified directory for this test
    data = {
        "custom_math": {
            "function": "custom_math.py:addition",
            "args": [5, 3]
        }
    }
    result = citros_params_obj.evaluate_dictionary(data)
    assert result == {"custom_math": 8}

def test_evaluate_user_function2(citros_params_obj):
    # Ensure you have a function in your specified directory for this test
    data = {
        "custom_math": {
            "function": "custom_math.py:addition_with_np",
            "args": [5, 3]
        }
    }
    result = citros_params_obj.evaluate_dictionary(data)
    assert result == {"custom_math": 8}

def test_recursive_evaluation(citros_params_obj):
    data = {
        "a": 10,
        "b": {
            "function": "numpy.add",
            "args": ["a", 5]
        },
        "c": {
            "function": "numpy.multiply",
            "args": ["b", 2]
        }
    }
    result = citros_params_obj.evaluate_dictionary(data)
    assert result == {"a": 10, "b": 15, "c": 30}

def test_circular_dependency_detection(citros_params_obj):
    data = {
        "a": {
            "function": "numpy.add",
            "args": ["b", 1]
        },
        "b": {
            "function": "numpy.add",
            "args": ["a", 1]
        }
    }
    with pytest.raises(ValueError, match="Circular dependency detected"):
        citros_params_obj.evaluate_dictionary(data)

def test_nested_key_reference_multi_level(citros_params_obj):
    data = {
        "outer": {
            "inner_a": 5,
            "inner_b": {
                "function": "numpy.add",
                "args": ["inner_a", 3]
            }
        },
        "sum": {
            "function": "numpy.add",
            "args": ["outer.inner_b", 2]
        }
    }
    result = citros_params_obj.evaluate_dictionary(data)
    assert result == {"outer": {"inner_a": 5, "inner_b": 8}, "sum": 10}

def test_nested_key_reference_single_level(citros_params_obj):
    data = {
        "outer": {
            "inner_a": 5,
            "inner_b": {
                "function": "numpy.add",
                "args": ["inner_a", 3]
            }
        },
        "sum": {
            "function": "numpy.add",
            "args": ["inner_b", 2]
        }
    }
    result = citros_params_obj.evaluate_dictionary(data)
    assert result == {"outer": {"inner_a": 5, "inner_b": 8}, "sum": 10}

def test_list_processing(citros_params_obj):
    data = {
        "list": [1, 2, 3],
        "sum": {
            "function": "numpy.sum",
            "args": ["list"]
        }
    }
    result = citros_params_obj.evaluate_dictionary(data)
    assert result == {
        "list": [1, 2, 3],
        "sum": 6
    }

def test_recursive_evaluation_multiple_files(citros_params_obj):
    data = {
        "d": {
            "function": "more_custom_math.py:multiply_with_np",
            "args": ["c", "b"]
        },
        "a": 10,
        "b": {
            "function": "custom_math.py:addition",
            "args": ["a", 5]
        },
        "c": {
            "function": "custom_math.py:addition_with_np",
            "args": ["b", 2]
        }
    }
    result = citros_params_obj.evaluate_dictionary(data)
    assert result == {"a": 10, "b": 15, "c":17, "d": 255}

def test_numpy_normal(citros_params_obj):
    data = {
        "mu": 0.0,
        "sigma": 1.0,
        "random_normal": {
            "function": "numpy.random.normal",
            "args": ["mu", "sigma"]
        }
    }
    result = citros_params_obj.evaluate_dictionary(data)
    assert isinstance(result['random_normal'], float)

def test_numpy_uniform(citros_params_obj):
    data = {
        "low": 1.0,
        "high": 10.0,
        "random_uniform": {
            "function": "numpy.random.uniform",
            "args": ["low", "high"]
        }
    }
    result = citros_params_obj.evaluate_dictionary(data)
    assert 1.0 <= result['random_uniform'] < 10.0

def test_numpy_exponential(citros_params_obj):
    data = {
        "scale": 2.0,
        "random_exponential": {
            "function": "numpy.random.exponential",
            "args": ["scale"]
        }
    }
    result = citros_params_obj.evaluate_dictionary(data)
    assert result['random_exponential'] >= 0
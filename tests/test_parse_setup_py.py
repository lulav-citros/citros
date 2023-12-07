import pytest
import random
import os
import tempfile
from faker import Faker
from citros import Citros

NUM_TEST_RUNS = 10

faker = Faker()

def generate_random_version():
    return f"{random.randint(1, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"

def valid_setup_py_content():
    package_name = f"my_package_{faker.pystr(min_chars=5, max_chars=20)}"
    maintainer = faker.name()
    maintainer_email = faker.ascii_free_email()
    version=generate_random_version()
    description=faker.sentence()
    content = f"""
import os
from glob import glob
from setuptools import setup

package_name = '{package_name}'

setup(
    name=package_name,
    version='{str(version)}',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    author='ROS 2 Developer',
    author_email='foo@bar.com',
    maintainer='{maintainer}',
    maintainer_email='{maintainer_email}',
    keywords=['foo', 'bar'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: TODO',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='{description}',
    license='TODO',
    entry_points={{
        'console_scripts': [
            'my_script = {package_name}.my_script:main'
        ],
    }},
)
"""
    return content, maintainer, maintainer_email, version, description


def generate_setup_py():
    for _ in range(NUM_TEST_RUNS):
        yield valid_setup_py_content()


@pytest.mark.parametrize("valid_setup_py_content, maintainer, maintainer_email, version, description", generate_setup_py())
def test_parse_setup_py(valid_setup_py_content, maintainer, maintainer_email, version, description):
    
    with tempfile.TemporaryDirectory() as tmpdir:
        setup_path = os.path.join(tmpdir, "setup.py")
        with open(setup_path, "w") as f:
            f.write(valid_setup_py_content)
        with Citros() as citros:
            result = citros.parser_ros2.parse_setup_py(tmpdir)

        assert result["setup_py"] == setup_path
        assert result["version"] == str(version)
        assert result["maintainer"] == maintainer
        assert result["maintainer_email"] == maintainer_email
        assert result["description"] == description


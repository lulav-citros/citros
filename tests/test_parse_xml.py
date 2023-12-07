# to run: python3 -m pytest test_parse_xml.py

import pytest
import random
import os
import tempfile
from faker import Faker
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom
from citros import Citros

NUM_TEST_RUNS = 10


def generate_package_xml(package_name, version, maintainer, maintainer_email, description, license, build_type):
    """
    Generates a package.xml string.
    """
    package = Element('package')

    name_elem = SubElement(package, 'name')
    name_elem.text = package_name

    version_elem = SubElement(package, 'version')
    version_elem.text = version

    maintainer_elem = SubElement(package, 'maintainer', {'email': maintainer_email})
    maintainer_elem.text = maintainer

    description_elem = SubElement(package, 'description')
    description_elem.text = description

    license_elem = SubElement(package, 'license')
    license_elem.text = license

    export_elem = SubElement(package, 'export')
    build_type_elem = SubElement(export_elem, 'build_type')
    build_type_elem.text = build_type

    raw_string = tostring(package, 'utf-8')
    reparsed = minidom.parseString(raw_string)
    return reparsed.toprettyxml(indent="  ")


def generate_random_version():
    return f"{random.randint(1, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"


def generate_test_data():
    fake = Faker()
    for _ in range(NUM_TEST_RUNS):
        yield (
            fake.word(),
            generate_random_version(),
            fake.name(),
            fake.email(),
            fake.sentence(),
            "Apache-2.0",
            random.choice(["ament_cmake", "ament_python"]),
        )


@pytest.mark.parametrize("package_name, version, maintainer, maintainer_email, description, license, build_type", generate_test_data())
def test_parse_xml(package_name, version, maintainer, maintainer_email, description, license, build_type):
    package_xml_content = generate_package_xml(package_name, version, maintainer, maintainer_email, description, license, build_type)
    
    with tempfile.TemporaryDirectory() as tmpdir:
        xml_path = os.path.join(tmpdir, "package.xml")
        with open(xml_path, "w") as f:
            f.write(package_xml_content)
            f.close()
            package_path = os.path.dirname(f.name)
            
            with Citros() as citros: 
                # Test the parse_xml function
                result = citros.parser_ros2.parse_xml(package_path)

                # Verify the results
                assert result == {
                    "package_xml": f.name,
                    "package_name": package_name,
                    "version": version,
                    "maintainer": maintainer,
                    "maintainer_email": maintainer_email,
                    "description": description,
                    "license": license,
                    "nodes": [],
                    "build_type": build_type,
                }


def test_empty_file():
    with tempfile.TemporaryDirectory() as tmpdir:
        xml_path = os.path.join(tmpdir, "package.xml")
        with open(xml_path, "w") as f:
            f.close()  # Empty file

            with Citros() as citros: 
                result = citros.parser_ros2.parse_xml(os.path.dirname(f.name))

        assert result == {}


def test_missing_fields():
    package_xml_content = """
    <?xml version="1.0"?>
    <?xml-model href="http://download.ros.org/schema/package_format2.xsd" schematypens="http://www.w3.org/2001/XMLSchema"?>
    <package format="2">
        <name>rclcpp_tutorials</name>
    </package>
    """.strip()

    with tempfile.TemporaryDirectory() as tmpdir:
        xml_path = os.path.join(tmpdir, "package.xml")
        with open(xml_path, "w") as f:
            f.write(package_xml_content)
            f.close()

            with Citros() as citros: 
                result = citros.parser_ros2.parse_xml(os.path.dirname(f.name))

            assert result == {
            "package_xml": f.name,
            "package_name": "rclcpp_tutorials",
            "version" : "",
            "maintainer" : "",
            "maintainer_email" : "",
            "description" : "",
            "license" : "",
            "nodes": [],
            "build_type": None
            }


def test_invalid_xml():
    package_xml_content = """
    This is not a valid XML file.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        xml_path = os.path.join(tmpdir, "package.xml")
        with open(xml_path, "w") as f:
            f.write(package_xml_content)
            f.close()

            with Citros() as citros: 
                result = citros.parser_ros2.parse_xml(os.path.dirname(f.name))

            assert result == {}
        

def test_gleb_xml():
    with Citros() as citros: 
        result = citros.parser_ros2.parse_xml('input/gleb')

        assert result == {
            "package_xml": 'input/gleb/package.xml',
            "package_name": "turtlebot3_fake_node",
            "version" : "2.2.3",
            "maintainer" : "Will Son",
            "maintainer_email" : "willson@robotis.com",
            "description" : "\n    Package for TurtleBot3 fake node. With this package, simple tests can be done without a robot.\n" + \
                            "    You can do simple tests using this package on rviz without real robots.\n  ",
            "license" : "Apache 2.0",
            "nodes": [],
            "build_type": 'ament_cmake'
            }
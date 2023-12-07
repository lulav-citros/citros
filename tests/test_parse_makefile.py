# to run: python3 -m pytest test_parse_makefile.py

import os
import tempfile
from faker import Faker
import pytest
from citros import Citros

NUM_TEST_RUNS = 10

faker = Faker()


def generate_cmake_content(executables):
    content = "\n".join([f"add_executable({exe} src/{exe}.cpp)" for exe in executables])
    install_targets = " ".join(executables)
    content += f"\n\ninstall(TARGETS {install_targets} DESTINATION lib/${{PROJECT_NAME}})\n"
    return content


def cmake_data():
    for _ in range(NUM_TEST_RUNS):
        executables = [faker.pystr_format() for _ in range(faker.random_int(min=1, max=5))]
        yield executables, generate_cmake_content(executables)


@pytest.mark.parametrize("executables,cmake_content", cmake_data())
def test_parse_makefile(executables, cmake_content):
    with tempfile.TemporaryDirectory() as tmpdir:
        cmake_path = os.path.join(tmpdir, "CMakeLists.txt")
        with open(cmake_path, "w") as f:
            f.write(cmake_content)

        with Citros(debug=True) as citros:
            result = citros.parser_ros2.parse_makefile(tmpdir)

        assert result["cmake"] == cmake_path
        nodes = result["nodes"]
        assert len(nodes) == len(executables)
        for node in nodes:
            assert "name" in node
            assert node["name"] in executables
            assert "entry_point" in node
            assert node["entry_point"] == ""
            assert "path" in node
            assert node["path"] == ""
            assert "parameters" in node
            assert node["parameters"] == []


def test_parse_makefile_no_install():
    with tempfile.TemporaryDirectory() as tmpdir:
        cmake_path = os.path.join(tmpdir, "CMakeLists.txt")
        with open(cmake_path, "w") as f:
            f.write("add_executable(foo src/foo.cpp)")

        with Citros(debug=True) as citros:
            with pytest.raises(ValueError) as e:
                citros.parser_ros2.parse_makefile(tmpdir)
            assert str(e.value) == f"{cmake_path} is not formatted correctly: `add_executable` with no 'install' command."


def test_parse_makefile_no_targets():
    with tempfile.TemporaryDirectory() as tmpdir:
        cmake_path = os.path.join(tmpdir, "CMakeLists.txt")
        with open(cmake_path, "w") as f:
            f.write("install(TARGETS DESTINATION lib/${PROJECT_NAME})")

        with Citros(debug=True) as citros:
            result = citros.parser_ros2.parse_makefile(tmpdir)

        # no targets (nodes) is OK - e.g. a cmake file that just
        # installs some common cmake functionality for other cmake files.
        assert result["cmake"] == cmake_path
        assert result["nodes"] == []
            

def test_parse_makefile_multiline_install():
    executables = [faker.pystr_format() for _ in range(faker.random_int(min=1, max=5))]

    with tempfile.TemporaryDirectory() as tmpdir:
        cmake_path = os.path.join(tmpdir, "CMakeLists.txt")
        with open(cmake_path, "w") as f:
            f.write("install(TARGETS \n")
            for exe in executables:
                f.write(f"{exe} \n")
            f.write("DESTINATION lib/${PROJECT_NAME})")

        with Citros(debug=True) as citros:
              result = citros.parser_ros2.parse_makefile(tmpdir)

        assert result["cmake"] == cmake_path
        nodes = result["nodes"]
        assert len(nodes) == len(executables)
        for node in nodes:
            assert "name" in node
            assert node["name"] in executables
            assert "entry_point" in node
            assert node["entry_point"] == ""
            assert "path" in node
            assert node["path"] == ""
            assert "parameters" in node
            assert node["parameters"] == []


def test_gleb_makefile():
    with Citros(debug=True) as citros:
        result = citros.parser_ros2.parse_makefile('input/gleb')

        assert result["cmake"] == 'input/gleb/CMakeLists.txt'
        nodes = result["nodes"]
        assert len(nodes) == 1
        
        node = nodes[0]
        assert "name" in node
        assert node["name"] == "turtlebot3_fake_node"
        assert "entry_point" in node
        assert node["entry_point"] == ""
        assert "path" in node
        assert node["path"] == ""
        assert "parameters" in node
        assert node["parameters"] == []


def test_micro_ros_agent_makefile():
    with Citros(debug=True) as citros:
        result = citros.parser_ros2.parse_makefile('input/micro_ros_agent')

        assert result["cmake"] == 'input/micro_ros_agent/CMakeLists.txt'
        nodes = result["nodes"]
        assert len(nodes) == 1

        node = nodes[0]
        assert "name" in node
        assert node["name"] == "micro_ros_agent"
        assert "entry_point" in node
        assert node["entry_point"] == ""
        assert "path" in node
        assert node["path"] == ""
        assert "parameters" in node
        assert node["parameters"] == []


def test_px4_makefile():
    with Citros(debug=True) as citros:
        result = citros.parser_ros2.parse_makefile('input/px4_msgs')

        assert result["cmake"] == 'input/px4_msgs/CMakeLists.txt'
        nodes = result["nodes"]
        assert len(nodes) == 0


def test_multiple_assignments_makefile():
    with Citros(debug=True) as citros:
        result = citros.parser_ros2.parse_makefile('input/moveit2_planning')

        assert result["cmake"] == 'input/moveit2_planning/CMakeLists.txt'
        
        nodes = result["nodes"]
        assert len(nodes) == 14


def test_multiple_installs_makefile():
    with Citros(debug=True) as citros:
        result = citros.parser_ros2.parse_makefile('input/moveit2_setup')

        assert result["cmake"] == 'input/moveit2_setup/CMakeLists.txt'
        
        nodes = result["nodes"]
        assert len(nodes) == 1

        assert nodes[0]["name"] == "moveit_setup_simulation"


import glob
import yaml
import os
import ast
import re
import json
import git
from pathlib import Path

import xml.etree.ElementTree as ET

from .parser_base import parser_base


class parser_ros2(parser_base):
    """
    Class to parse ROS2 package files (XML, CMakeLists.txt, setup.py etc).
    """  

    def __init__(self, citros) -> None:                                
        self.log = citros.log
        self.project = None
        self.print = citros.print
        self.ignore_list = []
        self.get_ignore_list = citros.get_ignore_list

    ################################ Any lang #################################

    def parse_xml(self, package_path):
        """
        Parse an XML file in the given package path.

        :param package_path: Path of the package.
        """  
        path_to_package_xml = Path(package_path, "package.xml")
        if not path_to_package_xml.exists():
            self.log.error(f"File not found: {str(path_to_package_xml)}")
            return {}

        path_to_package_xml = str(path_to_package_xml)

        try:
            tree = ET.parse(path_to_package_xml)
            root = tree.getroot()
        except ET.ParseError as ex:
            self.log.exception(f"parsing error while trying to parse: {path_to_package_xml}")
            return {}
        
        package_name = root.find("name")
        version = root.find("version")
        maintainer = root.find("maintainer")
        maintainer_email = maintainer.attrib["email"] if maintainer is not None else ""
        description = root.find("description")
        license = root.find("license")
        export = root.find("export")
        build_type = export.find("build_type") if export is not None else None
        
        return {
            "package_xml": path_to_package_xml,
            "package_name": package_name.text if package_name is not None else "",
            "version": version.text if version is not None else "",
            "maintainer": maintainer.text if maintainer is not None else "",
            "maintainer_email": maintainer_email,
            "description": description.text if description is not None else "",
            "license": license.text if license is not None else "",
            "nodes": [],
            "build_type": build_type.text if build_type is not None else None
        }
    
    ################################# C / CPP #################################

    def parse_makefile(self, package_path):
        path_to_cmake = Path(package_path, "CMakeLists.txt")
        
        nodes = self.find_install_targets(path_to_cmake)

        return {
            "cmake": str(path_to_cmake),
            "nodes": nodes 
        } 
    

    def find_install_targets(self, cmake_file_path : Path):
        """
        Parses the given CMakelists.txt file and returns a list of nodes, 
        whose names are the install targets defined in the file.

        Unhandled edge cases:
        1.  Multiple assignments: If a variable is set multiple times in the
            CMakeLists.txt file, the value that this function will use is the 
            value that was set last before the `install` command.
        2.  Conditional assignments: If a variable is set inside an if statement,
            the function will still process it regardless of the condition.
        3.  Function definitions: If `install` is called inside a function definition,
            and a target variable used is a function parameter, an exception will be 
            raised (since the variable will not be recognized). 
        4.  Nested variable references (e.g., ${${ANOTHER_VAR}}).
        """
        # import locally to avoid conflicts with the `ast` (for python) module.
        from cmakeast import ast
        from cmakeast.ast_visitor import recurse

        with open(cmake_file_path, 'r') as f:
            contents = f.read()

        # Parse the CMake file to an AST
        root = ast.parse(contents)

        var_assignments = {'PROJECT_NAME': str(cmake_file_path.parent.name)}

        # List to store all install targets
        install_target_nodes = []

        def add_node(node_name):
            install_target_nodes.append({
                "name": node_name,
                "entry_point": "",                    
                "path": "",
                "parameters": []
            })
            self.print(f"     node: {node_name}", only_verbose=True)

        def unquote(string):
            if string.startswith('"') and string.endswith('"'):
                return string[1:-1]
            return string
        
        def get_var_assignments(set_node):
            if len(set_node.arguments) >= 2:
                # The first argument is the variable name
                var_name = set_node.arguments[0].contents

                # Concatenate all subsequent arguments assuming they may be part of the list
                values_list = set_node.arguments[1:]
                
                # CMake lists can be separated by whitespace or semicolons.
                value = ";".join(arg.contents for arg in values_list)
                
                # Remove surrounding quotes from the entire value if present
                value = unquote(value)

                # We split on whitespace and flatten the result in case any individual
                # element was already a semicolon-separated list.
                # Split on whitespace first
                value_split = value.split()

                # Process each element by splitting on semicolons
                sublists = (elem.split(';') for elem in value_split)
                
                # Flatten the list of lists, remove individual quotes, and filter out empty strings
                value_elements = [unquote(item) for sublist in sublists for item in sublist if item]
                var_assignments[var_name] = value_elements

        validity_checks = {
            'exec_found': False,
            'install_found': False,
            'at_least_one_node': False
        }

        # Known properties - see https://cmake.org/cmake/help/latest/command/install.html#targets
        properties = {"EXPORT", "RUNTIME_DEPENDENCIES", "RUNTIME_DEPENDENCY_SET", "ARCHIVE", "LIBRARY", 
                    "RUNTIME", "OBJECTS", "FRAMEWORK", "BUNDLE", "PRIVATE_HEADER", "PUBLIC_HEADER",
                    "RESOURCE", "FILE_SET", "CXX_MODULES_BMI", "DESTINATION", "PERMISSIONS", 
                    "CONFIGURATIONS", "COMPONENT", "NAMELINK_COMPONENT", "OPTIONAL", 
                    "EXCLUDE_FROM_ALL", "NAMELINK_ONLY", "NAMELINK_SKIP", "INCLUDES DESTINATION"}

        cmake_file_path = str(cmake_file_path)

        # Define a handler for FunctionCall nodes
        def handle_function_call(name, node, depth):
            # Handle `set` commands to track variable assignments
            if node.name == "set":
                get_var_assignments(node)
            # Handle install commands to track install targets
            elif node.name == "add_executable":
                # If there is an executable, there should be an install
                validity_checks['exec_found'] = True
            elif node.name == "install":
                validity_checks['install_found'] = True
                arguments = node.arguments
                if arguments and arguments[0].contents == "TARGETS":
                    # Loop through the arguments until a property is found
                    for arg in arguments[1:]:
                        if arg.contents in properties:
                            break
                        validity_checks['at_least_one_node'] = True
                        if arg.contents.startswith("${") and arg.contents.endswith("}"):
                            var_name = arg.contents[2:-1]
                            if var_name in var_assignments:
                                var_value = var_assignments[var_name]
                                if isinstance(var_value, list):
                                    for target in var_value:
                                        add_node(target)
                                elif isinstance(var_value, str):
                                    add_node(var_value)
                            else:
                                raise ValueError(f"Unknown cmake variable name: {var_name} in {cmake_file_path}")
                        else:
                            add_node(arg.contents)

        # Use the recurse function to traverse the AST with the handler
        recurse(root, function_call=handle_function_call)

        if not validity_checks['install_found'] and not validity_checks['exec_found']:
            self.log.debug(f"{cmake_file_path} is a pure interface package without install and nodes.")
        else:
            if not validity_checks['install_found']:
                self.log.error(f"{cmake_file_path} is not formatted correctly: `add_executable` with no 'install' command.")
                raise ValueError(f"{cmake_file_path} is not formatted correctly: `add_executable` with no 'install' command.")
            if not validity_checks['at_least_one_node']:
                self.log.debug(f"{cmake_file_path} does not install any nodes.")

        return install_target_nodes

    
    ################################# Python ##################################
 
    def _extract_contents(self, node, global_scope):
        """
        Recursive helper function for parsing a variety of objects such as lists, function calls etc.
        Does not handle every case, such as nested functions etc. Returns None on failure.
        """
        if isinstance(node, ast.Str):
            return node.s
        elif isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.Name):
            return global_scope.get(node.id)
        elif isinstance(node, ast.List):
            return [self._extract_contents(item, global_scope) for item in node.elts]
        elif isinstance(node, ast.Tuple):
            return tuple(self._extract_contents(item, global_scope) for item in node.elts)
        elif isinstance(node, ast.Dict):
            return {self._extract_contents(key, global_scope): self._extract_contents(value, global_scope)
                    for key, value in zip(node.keys, node.values)}
        elif isinstance(node, ast.BinOp):
            return self._extract_contents(node.left, global_scope) + self._extract_contents(node.right, global_scope)
        elif isinstance(node, ast.Call):
            pos_args = tuple(self._extract_contents(arg, global_scope) for arg in node.args)
            kw_args = tuple(f"{kw.arg}={self._extract_contents(kw.value, global_scope)}" for kw in node.keywords)
            if isinstance(node.func, ast.Name):
                return f"{node.func.id}{pos_args+kw_args}"
            elif isinstance(node.func, ast.Attribute):
                return f"{node.func.attr}{pos_args+kw_args}"
        elif isinstance(node, ast.Constant):
            return node.s
        else:
            return None
    

    def _extract_setup_parameters(self, tree, global_scope):
        """
        Returns a dictionary containing the parameters in the `setup` function, 
        by extracting them from the given syntax tree.
        """
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'setup':
                parameters = {}
                for keyword in node.keywords:
                    parameter_name = keyword.arg
                    parameter_value = self._extract_contents(keyword.value, global_scope)
                    parameters[parameter_name] = parameter_value
                return parameters
    
        return None
    

    def _populate_global_scope(self, tree):
        """
        Returns a dictionary containing variables defined globally in the given syntax tree.
        """
        global_scope = {}
        for node in tree.body:
            if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
                target_name = node.targets[0].id
                target_value = self._extract_contents(node.value, global_scope)
                global_scope[target_name] = target_value
        return global_scope


    def _parse_entry_point(self, ep):
        """
        Example of expected entrypoint format:
        analytic_dynamics = cannon_analytic.analytic_dynamics:main
        """
        try:
            node_name = ep.split('=')[0].strip()
            entry_point = ep.split('=')[1].strip()
            file_name = f"{entry_point.split(':')[0].split('.')[1]}.py"
        except Exception as e:
            self.log.error(f"Failed to parse entry point {ep}")
            return None,None,None

        return node_name, entry_point, file_name 


    def parse_setup_py(self, package_path):
        """
        Parse a setup.py file in the given package path.

        :param package_path: Path of the package.
        """
        package_path = Path(package_path)
        path_to_setup = str(Path(package_path, "setup.py"))  

        try:
            with open(path_to_setup, 'r') as f:
                source = f.read()
        except FileNotFoundError as e:
            self.log.error(f"Failed to find {path_to_setup}")
            return {}

        tree = ast.parse(source)
        global_scope = self._populate_global_scope(tree)
        parameters = self._extract_setup_parameters(tree, global_scope)

        if not parameters:
            self.log.error("Failed to parse setup.py")
            return {}

        nodes = []

        if not parameters['entry_points'] or \
           not parameters['entry_points']['console_scripts']:
            self.log.warning(f"No entry points have been defined in `setup.py` of package {package_path}")
        else:
            for console_script in parameters['entry_points']['console_scripts']:
                node_name, entry_point, file_name = self._parse_entry_point(console_script)

                self.print(f"    node: {node_name}", only_verbose=True)

                nodes.append({                
                    "name": node_name,
                    "entry_point": entry_point,                
                    "path": str(Path(package_path, package_path.name, file_name)),
                    "parameters": []
                })

        return {
            "setup_py": path_to_setup,
            "package_name": package_path.name,
            "version": parameters.get("version", ""),
            "maintainer": parameters.get("maintainer", ""),
            "maintainer_email": parameters.get("maintainer_email", ""),
            "description": parameters.get("description", ""),
            "license": parameters.get("license", ""),
            "nodes": nodes
        }
    
    ################################# Project #################################

    def get_project_packages(self, project_path, package_paths):
        """
        Collects packages metadata (nodes, parameters etc.)
        """              
        self.log.debug(f" + get_project_packages {package_paths}")
        
        packages = []
        for package_path in package_paths:            
            self.log.debug(f"package_path: {package_path}")
            self.print(f"parsing package: {package_path}", only_verbose=True)
            
            parsed_data = None     
            try:
                parsed_data = self.parse_xml(package_path)
            except ET.ParseError as e:
                self.print(f"The path `{package_path}` doesn't contain xml, probably not a package. Skipping.")
                continue
            
            if parsed_data["build_type"] == "ament_python":                
                temp = self.parse_setup_py(package_path)
                parsed_data["nodes"] = temp["nodes"]                
                parsed_data["setup_py"] = temp["setup_py"]
                
            elif parsed_data["build_type"] == "ament_cmake":          
                temp = self.parse_makefile(package_path)
                parsed_data["nodes"] = temp["nodes"]
                parsed_data["cmake"] = temp["cmake"]                
                
            else:
                msg = f"Build type {parsed_data['build_type']} not allowed for ROS 2. Skipping `{package_path}`."
                self.log.error(msg)
                self.print(msg, color='yellow')
                continue

            all_parameters = {}
            package_parameters = {}

            path_to_config = os.path.join(package_path, "config", "params.yaml")
            if os.path.exists(path_to_config):
                with open(path_to_config, 'r') as config_file:
                    try:
                        config = yaml.safe_load(config_file)
                    except yaml.YAMLError as ye:
                        self.log.exception(f"Error parsing params.yaml in package {package_path}: {ye}")
                        raise ye       
                    
                for node_name, val in config.items():
                    par_dict = val.get("ros__parameters", {})                 
                    all_parameters[node_name] = []
                    for key, val in par_dict.items():
                        all_parameters[node_name].append({                            
                            "name":key,
                            "parameterType": type(val).__name__, # TODO[]: Fix type
                            "value": val,
                            "description": "Parameter loaded from config.yaml",                            
                        })
                # first, populate parameters that belong to actual nodes.
                nodes_with_params = []
                for node in parsed_data["nodes"]:
                    node["parameters"] = all_parameters.get(node["name"], [])
                    nodes_with_params.append(node["name"])
                
                # then, populate package parameters, i.e. those that don't belong to any actual nodes. 
                for name, param_list in all_parameters.items():
                    if not any(name == node_name for node_name in nodes_with_params):
                        package_parameters[name] = param_list

            else:
                self.log.info(f"no params.yaml file for package {package_path}")

            package_launch_paths = glob.glob(os.path.join(package_path, "**", "*.launch.py"), recursive=True)

            # filter ignored files
            package_launch_paths = [plp for plp in package_launch_paths if plp not in self.ignore_list]

            packages.append({               
                "name": parsed_data["package_name"],
                "cover": "",
                "path": package_path,
                "setup_py": parsed_data.get("setup_py", ""),
                "package_xml": parsed_data.get("package_xml", ""),
                "maintainer": parsed_data.get("maintainer", ""),
                "maintainer_email" : parsed_data.get("maintainer_email", ""),
                "description": parsed_data.get("description", ""),
                "license": parsed_data.get("license", ""),

                "readme": f"{package_path}{os.path.sep}README.md",
                "git": "", 
                
                "launches": self.get_project_launch_files(package_launch_paths),
                "nodes": parsed_data.get("nodes", []),
                "parameters": package_parameters
            })
            
        return packages


    def get_project_launch_files(self, launch_paths):
        """
        returns a list of dictionaries describing the *.launch.py files in the given list.
        """
        launch_files = []
        for launch_path in launch_paths:
            launch_files.append({                
                "name": Path(launch_path).name,
                "path": launch_path,

                # "tags": [],
                "description": "",                
            })

        launch_files.sort(key=lambda x: x['name'])
        return launch_files


    def get_git_remote_url(self, project_path, no_remote_ok=False):
        """
        Get the URL of the 'origin' remote.
        
        Assumption: there exists a remote named 'origin'.
        """
        try:
            repo = git.Repo(project_path)
            default_remote_name = 'origin'
            if default_remote_name in repo.remotes:
                default_remote = repo.remotes[default_remote_name]
                default_remote_url = default_remote.config_reader.get('url')

                # sanity check
                if default_remote_url.endswith(".git"):
                    return default_remote_url
                else:
                    self.log.error("Could not obtain git remote url for path " + project_path)
                    return ""
            else:
                msg = f"{project_path} has no git remote named `origin`."
                if no_remote_ok:
                    #self.log.info(msg)
                    pass
                else:
                    self.log.error(msg)
                return ""

        except Exception as e:
            self.log.exception(e)
            return ""
        
        
    def get_git_local_hash(self, project_path):
        try:
            # Get the hash of the latest commit on the current branch
            latest_commit_hash = git.Repo(project_path).head.commit.hexsha

        except Exception as e:
            self.log.exception(e)
            return None

        # sanity check
        if len(latest_commit_hash) == 40:
            return latest_commit_hash
        else:
            self.log.error("Could not obtain git hash for local path " + project_path)
            return None
    

    def get_project_description(self, project_path):
        #TODO[low] implement get_project_description(self, project_path):
        return ""


    def get_file_content(self, path):
        try:
            with open(path, 'r') as f:
                content = f.read()
            return content
        except Exception as e:
            self.log.error(f"could not open file {path}")
            return ""        
    

    def _setup_project(self, project_name, project_path):
        from citros_meta import __version__
        self.project = {
            "citros_cli_version": __version__,                     
            "cover": "",
            "name": project_name,
            "image": project_name,
            "tags": [],
            "is_active": True,
            "description": "",                 
            "git": self.get_git_remote_url(project_path), 
            #"path": project_path,    
                            
            "packages": None,                
            "launches": None,

            "readme": None,
            "license":None
        }


    def _is_descendant(self, file_path, directory_path):
        file = Path(file_path).resolve()
        directory = Path(directory_path).resolve()
        return str(directory) in str(file)


    def get_project_package_paths(self, project_path : str):
        self.log.debug(f"ignore list = {self.ignore_list}")

        pkg_xmls = glob.glob(os.path.join(project_path, "**", "src", "**", "package.xml"), recursive=True)
        pkg_xmls.sort()

        # get the directories containing the package.xml files
        package_paths = [os.path.dirname(file) for file in pkg_xmls]

        # save paths relative to project path
        package_paths = [os.path.relpath(pp, project_path) for pp in package_paths]

        # filter files from ignore list
        package_paths = [pp for pp in package_paths if pp not in self.ignore_list]
        
        return package_paths
    

    def get_project_launch_paths(self, project_path, package_paths):
        # project-level launch files are either descendants of src but not inside a package, 
        # or directly under project_path/launch 
        launch_paths = glob.glob(os.path.join(project_path, "**", "src", "**", "*.launch.py"), recursive=True)
        project_launch_paths = [lp for lp in launch_paths if not any(self._is_descendant(lp, pkg) for pkg in package_paths)]
        project_launch_paths = project_launch_paths + glob.glob(os.path.join(project_path, "launch", "*.launch.py"))

        # filter ignored files
        project_launch_paths = [plp for plp in project_launch_paths if plp not in self.ignore_list]
        
        return project_launch_paths


    def parse(self, project_path : str, project_name : str):
        """
        parses the project with the given name under the given path.

        Assumptions:

            1. a package is a directory that holds a `package.xml` file, 
               and is a decendant of a `src` directory,
               which is a descendant of the project directory.

            2. a launch file is a file whose name ends with `.launch.py`,
               and is a decendant of a `src` directory,
               which is a descendant of the project directory.

        param: project_path - the project directory's full path
        param: project_name - a possible alternate name for the project, 
                              in case a name different than the project directory's name is required.        

        Returns:
        a dictionary holding all metadata for the project.
        """    
        packages = []
        launches = []

        self.ignore_list = self.get_ignore_list()

        if not self.project:
            self._setup_project(project_name, project_path)

        package_paths = self.get_project_package_paths(project_path)
        project_launch_paths = self.get_project_launch_paths(project_path, package_paths)
        
        packages = self.get_project_packages(project_path, package_paths)
        launches = self.get_project_launch_files(project_launch_paths)
                        
        self.project["description"] = self.get_project_description(project_path)
        self.project["packages"] = packages
        self.project["launches"] = launches
        self.project["readme"] = self.get_file_content(os.path.join(project_path, "README.md"))
        self.project["license"] = self.get_file_content(os.path.join(project_path,"LICENSE"))
        
        return self.project
        

    def generate_default_proj_json(self, proj_name, package_names=[]):
        proj_json =  {
                        "name": f"{proj_name}",
                        "packages": []
                    }
        
        for pkg in package_names:
            pkg_content = {
                              "name": f"{pkg}",
                              "nodes": [],
                              "launches": [],
                              "parameters": []
                          }
            proj_json["packages"].append(pkg_content)

        return proj_json
    

    def get_msg_files(self, project_path, from_install=True):
        if from_install:
            msg_paths = glob.glob(os.path.join("**", "install", "**", "share", "**", "msg", "*.msg"), recursive=True)
            return msg_paths
        else:
            msg_paths = glob.glob(os.path.join(project_path, "**", "*.msg"), recursive=True)
            return msg_paths
    

    def generate_default_params_setup(self, project_json, params_setup_json, override_existing=False):
        if Path(params_setup_json).exists() and not override_existing:
            self.print(f"File {params_setup_json} already exists, avoiding override by default file.", only_verbose=True)
            return

        with open(project_json, 'r') as f:
            data = json.load(f)

        packages = data['packages']

        json_data = {'packages': {}}
        
        for package in packages:
            package_dict = {package['name']: {}}
            for node in package['nodes']:
                node_dict = {node['name']: {'ros__parameters': {}}}
                for parameter in node['parameters']:
                    node_dict[node['name']]['ros__parameters'][parameter['name']] = parameter['value']
                package_dict[package['name']][node['name']] = node_dict[node['name']]
            
            # node parameters
            json_data['packages'][package['name']] = package_dict[package['name']]

            # package parameters
            for node_name, param_list in package['parameters'].items():
                node_dict = {node_name: {'ros__parameters': {}}}
                for parameter in param_list:
                    node_dict[node_name]['ros__parameters'][parameter['name']] = parameter['value']
                json_data['packages'][package['name']] = node_dict


        with open(params_setup_json, 'w') as f:
            json.dump(json_data, f, indent=4)

    ####################### verify user defined functions #######################

    def find_function_in_file(self, file_path, function_name):
        """Scan a Python file to check if a global function exists with the given function_name."""
        try:
            self.log.debug(f"opening {file_path} to look for {function_name}.")
            with open(file_path, 'r') as file:
                tree = ast.parse(file.read())
                for node in ast.walk(tree):
                    if isinstance(node, ast.FunctionDef) and node.name == function_name:
                        return True
        except Exception as e:
            msg = f"exception was raise while trying to find function `{function_name}` in file {file_path}."
            self.log.error(f"{msg}\n{e}")
            self.print(f"{msg}", color='red')
            return False
        
        self.print(f"Could not find the user-defined function `{function_name}` in {file_path}.", color='red')
        return False


    def scan_for_functions(self, data, functions_dir):
        """Recursively scan nested JSON data for the 'function' key."""
        if isinstance(data, dict):
            if 'function' in data:
                value = data['function']
                
                # Check if the value contains ':' (i.e. it's a user-defined function)
                if ':' in value:
                    file_name, func_name = value.split(':')
                    if not self.find_function_in_file(Path(functions_dir, file_name), func_name):
                        # Found the key-value pair, but function doesn't exist
                        return False

            for key in data:
                if not self.scan_for_functions(data[key], functions_dir):
                    return False

        # unnecessary, but just in case...
        elif isinstance(data, list):
            for item in data:
                if not self.scan_for_functions(item, functions_dir):
                    return False

        return True


    def check_user_defined_functions(self, param_setup_dir : Path):
        for param_setup_file in param_setup_dir.iterdir():
            if param_setup_file.is_file() and str(param_setup_file).endswith(".json"):
                self.log.debug(f"checking user-defined functions for {param_setup_file}.")
                with open(param_setup_file, 'r') as file:
                    data = json.load(file)
                    if not self.scan_for_functions(data, Path(param_setup_dir, 'functions')):
                        return False
        return True
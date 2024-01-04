# .CITROS File Structure

.CITROS folder and file structure is automatically generated for you (when you run `citros init`):

```
└── .citros
    ├──data
    ├── logs
    ├── notebooks
    ├── parameter_setups
    │   ├── default_param_setup.json
    │   └── functions
    │       └── my_func.py
    ├── reports
    ├── simulations
    │   ├── simulation_1.json
    │   ├── simulation_2.json
    │   └── simulation_3.json
    ├── .gitignore
    ├── project.json
    └── settings.json

```
## Directory `data`
<details>
<summary>Description</summary>
The runs directory stores data and metadata about each run of your simulations. Its structure is as follows:


```
data
   └── Simulation Name
       └── Batch Name
           └── version
               ├── Run ID
               │   ├── bags
               │   ├── citros.log
               │   ├── config
               │   ├── environment.json
               │   ├── ros.log
               │   └── stats.csv
               ├── citros.log
               └── info.json
```
- Simulation Name: These directories are named after each of the simulations defined in the simulation files. For every simulation file that is run, a corresponding directory is created here. Each Simulation Name directory may include multiple Batch Name directories.

- Batch Name: This directory holds a batch of simulation runs. A batch consists of multiple runs of the same simulation with different parameters.

- Version ID: 

- Run ID: Each unique simulation run has its own directory, identified by a Run ID. Under this directory, there are several files and sub-directories:

- `bag`: This sub-directory holds the recorded data from the simulation run. It includes:

- bag_0.mcap: This is a ROS bag file that contains all the messages that were sent during the simulation. The default bag format is `mcap` (hence the mcap postfix), but you may also use the `sqlite3` format. See [simulations](#directory-simulations).

- metadata.yaml: A file holding metadata information associated with the bag file.

- `config`: This sub-directory contains YAML files (pkg1.yaml, pkg2.yaml, etc.) for each package in your ROS project, detailing the actual parameters used in the simulation. If you used any functions in your parameter setup, the values appearing here will be those that were evaluated according to the function you defined.
         
- `citros.log`: A standard log file, documenting CITROS actions and events that took place during the execution of CITROS commands. Running a CITROS command with the `-d` flag, will change the log level (which is set to `INFO` by default), to `DEBUG`.

- `ros.log`: A standard log file that was active during the simulation run, documenting ROS actions and events throughout the simulation. 

    **Note:** the destination of ROS logs is controlled by the `output` parameter to `Node` instances defined in the launch file being used. There are 3 possible values this parameter can take:

    - `log`: This option directs the output to log files.
    - `screen`: This option directs the output to the console or screen, which is useful for debugging purposes.
    - `both`: This option combines the functionalities of both `log` and `screen`, directing the output simultaneously to the log file and the screen.

    For example, the ROS logger output for the following node, defined in `cannon_analytic.launch.py`, will be written to both the console and the log file:
    ```python
    cannon_analytic_node=Node(
    package = 'cannon_analytic',
    name = 'analytic_dynamics',
    executable = 'analytic_dynamics',
    parameters = [config_analytic],
    output='both',
    emulate_tty=True
    )
    ```

- `environment.json`: A file capturing a snapshot of your environment variables and Python packages at the time of the simulation run.

- `info.json`: A JSON file containing general metadata about the run, such as batch ID, batch name, datetime of the run, user's Git commit and branch information, and CITROS' Git commit and branch information, as well as a hash of the bag file.

- `metrics.csv`: A CSV file recording system performance metrics during the simulation run, including CPU usage, total memory, available memory, used memory, and memory usage percentage.

These files collectively provide a comprehensive record of each simulation run, the conditions under which it was run, and the results it produced. This makes it easy to reproduce and understand the results of each simulation.

</details>

## Directory `logs`
<details>
  <summary>Description</summary>
</details>

## Directory `notebooks`
<details>
  <summary>Description</summary>
  This folder contains Jupiter notebook files you may use for data analysis of your simulation results.
</details>

## Directory `parameter_setups`
<details>

<summary>Description</summary>

The `parameter_setups` directory stores your JSON-formatted parameter setup files. When you initialize your CITROS repository, a `default_param_setup.json` file is automatically generated. This file consolidates all the default parameters for every node across all the packages in your ROS project, providing a consolidated and easily accessible record of these parameters.

The file `default_param_setup.json` will not be overwritten during CITROS `init`, `run` or `status` commands. Nevertheless, it is recommended to duplicate this file under a different name within the `parameter_setups` directory before making any modifications. This practice ensures your custom setups are preserved and allows you to experiment with various parameter configurations.
    
The structured format of the parameter setup files streamlines both the understanding and alteration of parameters for each node in your ROS project. This becomes especially valuable when you're keen to explore the influence of different parameter values on your ROS project's behavior. Take, for instance, a static parameter value like 42. Instead of hard-coding it, you could use a *function object* to derive a value from a normal distribution centered at 42. The introduction of function objects broadens your horizons, enabling you to use any numpy function or even craft user-defined functions for meticulous computational adjustments. A prime example is when parameter values are intricate, making them cumbersome to hard-code; in such scenarios, you can devise a function to fetch them from a file. In essence, this newfound flexibility paves the way for limitless computational and manipulative possibilities for your parameters.
    
To learn how to add functions to parameter setups, please refer to the [Adding functions to parameter setup](../guides/config_params.md) section.
</details>

## Directory `reports`
<details>
  <summary>Description</summary>
  This folder holds reports describing the results of your simulation runs.
</details>

## Directory `simulations`
<details>
<summary>Description</summary>

The `simulations` directory stores your JSON-formatted simulation files.

A simulation json file is an auto-generated file corresponding to each launch file in your ROS project. For instance, a launch file named `foo.launch.py` will have a corresponding `simulation_foo.json` file. This file outlines the details necessary to run the corresponding simulation, specifying parameters, resources, and launch files.

Here's a breakdown of its typical structure and content:

- `description`: This is a descriptive field for the simulation setup. You can modify it to better describe your specific simulation.

- `parameter_setup`: This field points to the parameter setup JSON file that will be used for this simulation. By default, it points to `default_param_setup.json`, but you can point it to any custom parameter setup file you created in the `parameter_setups` directory.

- `launch_file`: Specifies the ROS launch file that will be used to start the simulation. For instance, `foo.launch.py`.

- `timeout`: This is the maximum time (in seconds) the simulation is allowed to run. The default is 60 seconds. If the simulation does not conclude within this timeframe, it will be terminated.

- `GPU`: Specifies the number of GPU resources required for the simulation. The default is 0, indicating that no GPU resources are needed.

- `CPU`: Specifies the number of CPU resources required for the simulation. The default is 2.

- `MEM`: Specifies the amount of memory required for the simulation in megabytes, e.g., 265.

- `storage_type`: This setting determines the storage format for the ROS bag files generated during the simulation's runs. The possible valid value are `SQLITE3` and `MCAP` (default).

You can modify these fields to suit your simulation needs, just remember to save your customized version under a different name to prevent overwriting during citros `init`, `run`, or `status` commands.

</details>

## File `.gitignore`
<details>
<summary>Description</summary>
This file may be used by the user to specify names of packages and launch files in the project that should be ignored by CITROS. These packages and launch files will not be parsed and validated. Note that a launch file from another package may still use nodes from ignored packages.

To ignore a package, write the package directory path relative to the project directory. A package directory is a directory with a `package.xml` file.

Example:

    `src/cannon_analytic`

To ignore a launch file, write the file path relative to the project directory.
A launch file is a file of the form `*.launch.py`

Example:

    `src/scheduler/launch/cannon_analytic.launch.py`
</details>


## File `project.json`
<details>
<summary>Description</summary>
The project.json file is a key component of your CITROS repository. It contains metadata about your ROS project, and is automatically generated by the citros `init`, `run` and `status` commands. Here's a description of its top-level fields:

- `citros_cli_version`: The CITROS CLI version installed.

- `cover`: A placeholder for a potential image that represents the project.

- `description`: A string for providing a detailed description of the project.

- `git`: The git repository URL associated with the project.

- `image`: A name that corresponds to the docker image of the project.

- `is_active`: A boolean flag indicating whether the project is active or not.

- `launches`: An array for storing metadata about launch files associated with the project. 
  
    **Note**: these are the global launch files, which are not associated with any specific package. Generally, they are less commonly used. For package launch files, see inside the list of [*packages*](#packages-array).

- `license`: A string indicating the license of the project.

- `name`: The name of the project. *Note*: this is the only field that you may edit and it will not be overwritten during subsequent CITROS commands.

- [`packages`](#packages-array): An array of objects that describe the ROS packages that exist within the project.

- `path`: The directory path to the project.

- `readme`: The contents of the project's README file.

- `tags`: An array of strings for tagging and categorizing the project.

#### `packages` Array

In the `packages` array, each object describes a specific package within the project. These objects contain similar information to the top-level fields, with additional fields:

- `maintainer`: The maintainer of the package.

- `maintainer_email`: The email address of the maintainer.

- [`nodes`](#nodes-array): An array of objects describing each node in the package, including their parameters and entry points.

- `package_xml`: The path to the package's XML file.

- `setup_py`: The path to the package's `setup.py` file. For python ROS projects only.

- `cmake`: The path to the package's `CMakeLists.txt` file. For C++ ROS projects only.

- `parameters`: An array of objects that describe the package-level parameters, i.e. parameters which are not associated with any node. As with node-level parameters, this includes their name, type, and value.

#### `nodes` Array

The `nodes` array contains objects that describe the ROS nodes within a package. Each object includes the following fields:

- `entry_point`: The entry point for the node, typically the function that should be executed when the node is run.

- `name`: The name of the node.

- `parameters`: An array of objects that describe the parameters associated with the node, including their name, type, and value.

- `path`: The path to the node's Python file.

</details>

## File `settings.json`
<details>
<summary>Description</summary>

The settings.json file holds configuration settings for your CITROS repository. Here is a breakdown of each field in 
this file:

- `name`: The name of the current settings profile. This can be useful if you want to maintain different sets of settings for different contexts (e.g., 'default_settings', 'debug_settings', etc.).

- `force_message`: This is a boolean setting (in string format). If set to "True", it enforces that a descriptive message is provided for each batch of simulation runs. This can be helpful for keeping track of the purpose or characteristics of each run batch.

- `force_batch_name`: Similar to force_message, this is a boolean setting (in string format). If set to "True", it enforces that a unique name is provided for each batch of simulation runs. This can be useful for organizing and identifying different batches of runs.

</details>

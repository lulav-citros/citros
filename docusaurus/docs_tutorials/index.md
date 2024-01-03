---
sidebar_position: 5
sidebar_label: 'Introduction to CITROS'
hide_title: true
---
<!-- 
```mdx-code-block
import DocCardList from '@theme/DocCardList';

<DocCardList />
``` -->

# Introduction to CITROS

This tutorial will guide you through the CITROS CLI interface, using a simple ROS 2 example project to demonstrate the usage, while providing useful recommendations and best practices. While this is not a comprehensive guide to all CITROS CLI commands, it should get you up and running using your own projects with CITROS in no time. For further details and an exhaustive guide to the CITROS CLI, refer to the [CLI Documentation](https://citros.io/doc/docs_cli).

![orangesqueeze](img/orange_squeeze.jpg "CITROS CLI")

## The Cannon Example Project Overview

This project is a ROS 2 implementation of the [cannonball simulation](https://nasa.github.io/trick/tutorial/ATutASimpleSim) provided by NASA Johnson Space Center as part of the tutorial for the 
[Trick Simulation Environment](https://nasa.github.io/trick/).

It determines the trajectory and time of impact of a cannon ball that is fired with an initial speed and initial angle, assuming a constant acceleration of gravity (g), and no aerodynamic forces.

![Cannonball](img/CannonInit.png "Cannonball")

Two versions of the simulation are provided: an analytic solution and a numeric integration solution.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Workspace Overview](#implementation-overview)
4. [Running the Solutions](#running-the-solutions)
5. [Visualization with Foxglove](#visualization-with-foxglove)
6. [Working with CITROS](#working-with-citros)
7. [CITROS Initialization](#citros-initialization)
8. [Simulations](#simulations)
9. [Data analysis](#data-analysis)

## Prerequisites

1. Install [Visual Studio code](https://code.visualstudio.com/download)
2. Install and Run [Docker](https://docs.docker.com/get-docker/)
3. Install [Foxglove](https://foxglove.dev/download) (optional)

## Installation

Open cmd on your desktop

1. Clone the project:

```bash
$ git clone git@github.com:citros-garden/cannon.git
```

2. Change to Cannon project directory:

```bash
$ cd ~/cannon
```

3. Open Cannon project in VScode:

```bash
$ code .
```
5. Re-open in Dev Container

    1. press on the bottom left corner icon.
     
     ![Alt text](img/container_corner.png)

    2. Choose **Reopen in Container**
     
     ![Alt text](img/container_open_container.png)

6. Open VScode terminal and make sure you are in the right location
 
 ```    
 ros@docker-desktop:/workspaces/cannon$ 
 ```

:::note
From this point, all the actions should be typed in VScode terminal.
:::

7. Build your project

 ```bash
 $ colcon build
 $ source install/local_setup.bash
 ```

## Workspace Overview
The project is made out of three ROS nodes - `cannon_analytic`, `cannon_numeric` and `scheduler`. The scheduler node is responsible for driving the simulation by publishing a `scheduler` topic at a given rate (say, 100Hz). The cannon nodes subscribe to this topic, and upon receiving it perform a single calculation step. The rate (`dt`) is a ROS parameter for the scheduler node, which means you may change its value in the `config/params.yaml` file, without the need to recompile. The two cannon nodes also have `params.yaml` files of their own, in which you can set the initial speed and angle, and also the time/integration delta (`dt`).

Additionally, the `scheduler` node subscribes to a `debug` topic, which, together with the provided Foxglove layout, facilitates a play/pause/step/resume functionality.

The output of the simulation, i.e. the topic containing the calculated results, is called `cannon/state` (in both analytic and numeric versions). It is a list of `float` of size 4, the layout being:
        
    [position_x, position_y, velocity_x, velocity_y]

The simulation will halt when `position_y` reaches zero (i.e. impact).

## Running the Solutions

The cannon project contains two launch files, one for each solution

1. To Run the analytic solution

 ```bash
 $ ros2 launch scheduler cannon_analytic.launch.py
 ```

2. To run the numeric integration solution

 ```bash
 $ ros2 launch scheduler cannon_numeric.launch.py
 ```

:::note
Running either of the two simulations will result in the logger output being written to the console.
:::


## Visualization with Foxglove
To view a graphical representation of the simulation:
1. Open [Foxglove](https://foxglove.dev/) 
2. Press on Foxglove icon at the top right
3. Click View
4. Click "Import layout from file"

 ![Alt text](img/foxglove_open.png)

5. Choose `CITROS_Cannon.json` from the cannon project directory

6. Open a new Connection

 ![Alt text](img/foxglove_connection.png)

7. Choose Rosbridge and press the 'Open' button
 
 ![Alt text](img/foxglove_rosbridge.png)

8. You now have a working connection to your simulation.

9. If your simulation has stopped running in the terminal, run one of the [solutions](#running-the-solutions) again.

Output example:
![Foxglove screenshot](img/foxglove_screenshot.png)

## Working with CITROS

Working with the CITROS CLI is pretty straight forward, since there are only two things you need to do - initialize your CITROS repository, and run your project. Additionally, you may configure your CITROS repository to fit your simulation needs, but if all you want to do is to run your project via CITROS with the default configuration, than only two commands are necessary.

## CITROS Initialization

### Installation
First, let's make sure we can run CITROS:

1. Make sure the project (in this case Cannon) is opened inside a VS Code dev-container.
2. Build and source your project by running:
    ```bash
    $ colcon build
    $ source install/local_setup.bash
    ```
3. in the dev-container's terminal, run
    ```bash
    $ pip install citros
    ```

    You can verify that the installation succeeded by running 
    ```bash
    $ citros -h
    1.2.3
    ```

    to get the CITROS CLI version installed.


### Initialization

Alrighty then! You're now ready to run the first command - `init`, which will initialize your local CITROS repository:
```bash
$ citros init
```

This command creates a folder named `.citros` under your project directory.<br />
The `.citros` directory contains several files and folders that capture the state of your project and allow you to configure your simulations according to your needs. We will discuss some of them briefly later on. For a full and detailed description of the contents of the `.citros`  directory, refer to the [CLI Documentation](https://citros.io/doc/docs_cli).

## Simulations

### Running a Simulation

After your `.citros` repository has been initialized, you're ready to run a CITROS simulation, albeit with all the default configurations, by using the `run` command:

```bash
$ citros
```

Choose the `Run` action:

```sh
? Select Action: 
Init: initialize .citros in current directory 
❯ Run: new simulation                  
Data: for data management                                            
Report: generation and management                                               
```

Name the batch run (or press enter for *"citros"* as a default batch name):

```sh
Please name this batch run: my_first_batch
```

Enter a message for the batch (or press enter for *"This is a default batch message from citros"* as a default batch name):

```sh
Enter a message for this batch run: My first CITROS simulation!
```

Choose number of runs (or press enter to run once):

```sh
How many times you want the simulation to run?: 1
```

Lastly choose *"simulation_cannon_analytic"*:
```sh
? Please choose the simulation you wish to run: 
❯ simulation_cannon_analytic
  simulation_cannon_numeric
```


:::note

This command will run the simulation on your machine, and save all the results under `.citros/data/[simulation_name]` folder. The content of the [folder](/docs/cli/citros_structure#directory-runs) will contain 
- recorded bags
- logs from the simulation and citros itself
- metadata about the run
- metrics and information about the system it was running 
- and more.

:::

### Short Simulations Structure Overview

To fully understand what's going on, we need to familiarize ourselves with three concepts that are core to the way CITROS works:
- ## **[simulation](/docs/cli/citros_structure#directory-simulations)** 
    The simulation object is defining what you want to run and how. It is a set of the launch file (the what) and the parameter setup (the how) as well as the resources needed for it to run and after how much time it should be killed. 

    Defaults simulation files defined by a ROS 2 launch file. You may have as many launch files as you want in your project, as long as there is at least one. Each simulation will correspond to a launch file in your project. When you run a CITROS simulation, if you don't specify the name of the simulation (using the `-s` flag), a command-line menu will be presented, in which you can use the up and down arrows to choose the simulation you want. The simulation names will be of the form `simulation_<name of launch_file>`. In the case of the Cannon project, we have two launch files - `cannon_analytic.launch.py` and `cannon_numeric.launch.py`, and as you can see in the output above, we are prompted to choose between them. 

    Each simulation also corresponds to a json file of the same name, which resides under the [`.citros/simulations`](/docs/cli/citros_structure#directory-simulations) directory. You may use this file to configure the way your simulation runs. 

    When you run a CITROS simulation, a directory for that simulation is created under the [`.citros/runs`](/docs/cli/citros_structure#directory-runs) directory. This directory will contain subdirectories corresponding to **batch**es, a new one created every time you run a simulation.

- ## **batch** 

    Defined as a group of one or more simulation runs. Since you can specify one or more simulations runs ('*completions*') when running a CITROS simulation, a **batch** is simply a convenient way to group them together. For instance, in the case of the above example, if we choose `simulation_cannon_analytic` from the menu, the following folder structure will be created: `.citros/data/simulation_cannon_analytic/my_first_batch/20231231120623/0`. The last folder - `0`, is the folder corresponding to the only run for this batch - when you don't specify the number of completions (i.e. runs) using the `-c` flag, it will default to 1, and the name of each run is a zero based index, incremented by one for each additional run.

- ## **run**

    Defined as a single execution of a simulation as defined by the chosen launch file. Launching CITROS simulations with multiple runs ('*completions*') is particularly advantageous when working online, in which case a large number of simulation runs can be simultaneously executed on the CITROS cloud.

    The folder corresponding to a simulation run will contain all the information relevant for that run. Look through such a folder after running a simulation and see for yourself. For further details refer to the [CLI Documentation](https://citros.io/doc/docs_cli)


By default, when using the `run` command, you must provide a batch name (using the `-n` flag) and a message (using the `-m` flag). The name you provide will be used as the name of the directory in which all runs for this batch will be saved. If a batch by that name already exists - no worries, CITROS will simply add a new version under the simulation name you provided, thereby keeping the batch version unique for each simulation. 

Now that you understand what's going on, choose one of the simulations presented in the menu, press enter and see it run...

### Configuring a Simulation

We just ran a simulation with all the default configurations, which is admittedly not that exciting. Let's see how we can turn things up a notch by setting up dynamic parameter evaluation for our simulation, thereby allowing each run within the same batch to have different parameter values.

The [`.citros/parameter_setups`](/docs/cli/citros_structure#directory-parameter_setups) directory stores your JSON-formatted parameter setup files. When you initialize your citros repository, a `default_param_setup.json` file is automatically generated. This file consolidates all the default parameters for every node across all the packages in your ROS project, providing a consolidated and easily accessible record of these parameters.

The structured format of the parameter setup files streamlines both the understanding and alteration of parameters for each node in your ROS project. This becomes especially valuable when you're keen to explore the influence of different parameter values on your ROS project's behavior.

In the Cannon project, we have a total of three nodes. Let's look at the parameters for the `analytic_dynamics` node in the `cannon_analytic` package, as defined in the `default_param_setup.json` file.
We can see we have 3 parameters to play around with - `init_speed`, `init_angle` and `dt`. 

```json
//[project]/.citros/parameter_setups/default_param_setup.json
{
    "packages": {
        "cannon_analytic": {
            "analytic_dynamics": {
                "ros__parameters": {
                    "init_speed": 50.0,
                    "init_angle": 30.0,
                    "dt": 0.01
                }
            }
        },
        ...
    }
}
```

Let's say we want to find out the optimal initial angle for the cannon, which will provide the maximum range. Assuming we're completely blanking out on high-school physics, let's randomize the value for this parameter, execute several simulation runs, and see where we get the maximum range. To achieve this, we can simply replace the hard-coded default value with a [**function object**](/docs/cli/config_params). Function objects are json objects comprised of two fields - `function` and `args`. They come in two flavors - numpy and user-defined. For our purposes we can use numpy's random module to generate a normal distribution around a given value:

    "init_angle": {
                    "function": "numpy.random.normal",
                    "args": [45, 15]
                },

This will cause a normal distribution with a standard deviation of 15 around 45 to be evaluated for every simulation run.

Another way to use the run command is writing the full command: 

```bash
citros run -n "test_params" -m "testing random initial angle" -c 10
```

and choose `simulation_cannon_analytic` from the menu, the simulation will run 10 times (sequentially if working offline), and each time the cannon will have a different initial angle. By looking at the [results](#data-analysis-online-only), we can hopefully come to the conclusion that 45 degrees is the optimal angle. 

### Review All Simulations Data

To view all simulations use the data command:

```bash
$ citros
```

Choose the `Data` action:

```sh
? Select Action: 
Init: initialize .citros in current directory 
Run: new simulation                  
❯ Data: for data management                                            
Report: generation and management                                            
```

Choose `List` to view all simulations

```sh
❯ List: list all runs
simulation_cannon_analytic
simulation_cannon_numeric   
```

Table of all the simulations will be shown as output. <br />
The table contains the following fields: Run name, Versions, message, status, completions, path

![Alt text](img/cannon_data.png)


## Data Analysis

### Execute Notebook
After you've run a batch run on CITROS, your data is stored on CITROS's servers.
you can access the data using citros data analysis either from the Python [notebook](https://citros.io/cannon/blob/main/notebooks/data_analysis.ipynb) or from a local kernel Python environment.

:::note

citros data analysis package is installed while running `pip install citros`, so at this point you should have this package and you don't have to download it again.

:::

1. Open .citros directory

2. Go to notebooks.

3. Open data_analysis.ipynb

4. Press `Run All` button

5. Scroll down the notebook to see the results.

#### Results

here is a sample from the provided [notebook](https://citros.io/cannon/blob/main/notebooks/data_analysis.ipynb):
```python
#import matplotlib
import matplotlib.pyplot as plt

#create a figure to plot on
fig, ax = plt.subplots()

citros.batch(-1).topic('/cannon/state').sid([0,1,2,3,4]).\
       time_plot(ax, var_name = 'data.data[1]', time_step = 0.01, y_label = 'y', title_text = 'y vs. t')
```

![Alt text](img/nb_sample.png)


### Generate Report

After running the notebook and verifying that everything works properly you can generate a report from your Python Notebook signed by CITROS.

run citros command

```bash
$ citros
```

Choose the `Report` action:

```sh
? Select Action:                  
Init: initialize .citros in current directory 
Run: new simulation                  
Data: for data management                                            
❯ Report: generation and management                              
```

Choose `Generate` to generate a report

```sh
List: reports list
❯ Generate: new report
Validate: report integrity 
```

Choose the simulation source for the report

```sh
simulation_cannon_analytic 
❯ simulation_cannon_numeric
```

Select a batch from you batch list

```sh
Select Batch: numeric simulations
```

Select a version
```sh
Select Batch: numeric simulations
```

Name your report *(or press enter for "citros" as a default report name)*:
```sh
Please name this report: My first report
```

Enter a message for the report (or press enter for "This is a default message message from citros" as a default report message):
```sh
Enter a message for this report: Best report ever
```

choose the notebook for the report

```sh
❯ citros_template/notebooks/data_analysis.ipynb
citros_template/notebooks/test1.ipynb
```

To view your generated report go to .citros/reports/[report_name]

:::note

The content of the [Reports folder](/docs/cli/citros_structure#directory-reports) will contain 
- output of the python notebook
- Report info
- Generated pdf report

:::
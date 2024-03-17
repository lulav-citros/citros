---
sidebar_label: 'citros run'
---

# `citros run`

## Description

The `citros run`command will run the simulation on your machine.<br/> 
All the results will be saved under `.citros/data/[simulation_name]/[batch_name]/[date]` folder.<br /> 
The content of the [folder](../advanced_guides/citros_structure#directory-data) will contain: 
- recorded bags
- logs from the simulation and citros itself
- metadata about the run
- metrics and information about the system it was running 
- and more.

```bash
$ citros run [-h] [-dir DIR] [-s [SIMULATION]] [-n [NAME]] [-m [MESSAGE]]
             [--version [VERSION]] [-l] [-c [COMPLETIONS]] [-i [INDEX]] [-d] [-v]
```

:::note
For foxy and/or humble based ROS projects you may need to pre-install mcap support before running citros.
```
sudo apt-get update
sudo apt-get install -y ros-humble-rosbridge-suite ros-humble-rosbag2-storage-mcap
```
:::

## Options

Option|Description
|--|--|
|-h, --help       |       Show help message|
|-dir DIR       |       The working dir of the project|
|-s, --simulation [SIMULATION]       |       Simulation name|
|-n, --name [NAME]       |       Sets a name for the batch run|
|-m, --message [MESSAGE]       |       Sets a message for the run|
|--version [VERSION]       |       The batch run version.<br/>.citros/data/{sim_name}/{batch_name}/{ **batch_version**}/{sid}|
|-l, --lan_traffic       |       Receive LAN ROS traffic in your simulation.|
|-c, --completions [COMPLETIONS]       |       Number of times to run the simulation|
|-i, --index [INDEX]       |       The pard of the batch. if -1 will run all the batch|
|-d, --debug       |       Set logging level to debug|
|-v, --verbose       |       Use verbose console prints|


## Examples
```bash
$ citros run -n batch --message "batch message" -c 2
? Please choose the simulation you wish to run 
❯ simulation_name
simulation_name_2
```

:::note
When entering the explicit command, it is mandatory adding both **batch name** and a **batch message**
:::

## Interactive Mode

```bash
$ citros
```

```sh
? Select Action: 
┌────────────────────────────────────────────────────────────────────────────────────┐
│  Init: initialize .citros in current directory                                     │
│❯ Run: new simulation                                                               │
│  Data: for data management                                                         │
│  Report: generation and management                                                 │
│  ---------------                                                                   │
│  EXIT                                                                              │
└────────────────────────────────────────────────────────────────────────────────────┘
```

#### Name of the batch run:
```sh
? Select Action: Run: new simulation
Please name this batch run (citros): 
```
:::note
Default batch name is: *citros*
:::

#### Message for the batch:
```sh
? Select Action: Run: new simulation
Please name this batch run (citros): 
Enter a message for this batch run (This is a default batch message from citros):
```
:::note
Default batch run message is: *This is a default batch message from citros*
:::

#### Number of runs:

```sh
? Select Action: Run: new simulation
Please name this batch run (citros): 
Enter a message for this batch run (This is a default batch message from citros):
How many times you want the simulation to run? (1):
```
:::note
Default number of runs id: *1*
:::


#### Simulation to run:
```sh
? Select Action: Run: new simulation
Please name this batch run (citros): 
Enter a message for this batch run (This is a default batch message from citros):
How many times you want the simulation to run? (1):
? Please choose the simulation you wish to run:
```


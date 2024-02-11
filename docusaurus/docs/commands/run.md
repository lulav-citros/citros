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
$ citros run [-h] [-dir DIR] [-n [BATCH_NAME]] [-m [BATCH_MESSAGE]] [-l] 
             [-s [SIMULATION_NAME]] [--version [VERSION]]
             [-c [COMPLETIONS]] [-i [INDEX]] [-d] [-v]
```

## Options

Option|Description
|--|--|
|-h, --help       |       Show help message|
|-dir DIR       |       The working dir of the project|
|-n, --batch_name [BATCH_NAME]       |       Sets a name for the run|
|-m, --batch_message [BATCH_MESSAGE]       |       Sets a message for the run|
|-l, --lan_traffic       |       Receive LAN ROS traffic in your simulation.|
|-s, --simulation_name [SIMULATION_NAME]       |       Simulation name|
|--version [VERSION]       |       The batch run version.<br/>.citros/data/{sim_name}/{batch_name}/{ **batch_version**}/{sid}|
|-c, --completions [COMPLETIONS]       |       Number of times to run the simulation|
|-i, --index [INDEX]       |       The pard of the batch. if -1 will run all the batch|
|-d, --debug       |       Set logging level to debug|
|-v, --verbose       |       Use verbose console prints|


## Examples
```bash
$ citros run --batch_name batch --batch_message "batch message" -c 2
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


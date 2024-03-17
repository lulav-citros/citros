---
sidebar_label: 'citros data tree delete'
---

# `citros data tree delete`

## Description

The `delete` command is used to delete a simulation data.

```bash
$ citros data tree delete [-h] [-s SIMULATION] [-b BATCH] [--version VERSION] [-d] [-v]
```

## Options
Option|Description
|--|--|
|-h, --help       |       Show help message|
|-s, --simulation [SIMULATION]       |       Simulation name|
|-b, --batch [BATCH]       |       Sets a name for the batch run|
|--version [VERSION]       |       The batch run version.<br/>.citros/data/{sim_name}/{batch_name}/{ **batch_version**}/{sid}|
|-d, --debug       |       Set logging level to debug|
|-v, --verbose       |       Use verbose console prints|

## Examples

```sh
$ citros data tree unload -s simulation_1 -b "batch" --version 20240207190125
deleting data from simulation_1 / batch / 20240207190125
```

:::note
When entering the explicit command, it is mandatory adding **simulation name**, **batch name** and **version**
:::

## Interactive Mode

```bash
$ citros
```

```sh
? Select Action: 
┌────────────────────────────────────────────────────────────────────────────────────┐
│  Init: initialize .citros in current directory                                     │
│  Run: new simulation                                                               │
│❯ Data: for data management                                                         │
│  Report: generation and management                                                 │
│  ---------------                                                                   │
│  EXIT                                                                              │
└────────────────────────────────────────────────────────────────────────────────────┘
```

```sh
? Select Action: Data: for data management 
? Select Action: 
┌────────────────────────────────────────────────────────────────────────────────────┐
│❯ Tree view                                                                         │
│  List data                                                                         │
│  DB: section                                                                       │
│  ---------------                                                                   │
│  EXIT                                                                              │
└────────────────────────────────────────────────────────────────────────────────────┘
```

```sh
? Select Action: Data: for data management 
? Select Action: Tree view
? Select Simulation: simulation_1
? Select Batch: batch
? Select Version: 20240207190125
? Select Action: 
┌──────────────────────────────────────────────────────────────────────────────────┐
│  Info                                                                            │
│  Load                                                                            │
│  Unload                                                                          │
│❯ Delete                                                                          │
│  ---------------                                                                 │
│  EXIT                                                                            │
└──────────────────────────────────────────────────────────────────────────────────┘
```
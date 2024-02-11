# `citros data tree info`

## Description

The `info` command prints the info.json of the simulation.
The `info.json` can be found at .citros/data/[simulation_name]/[batch_name]/version directory

```bash
$ citros data tree info [-h] [-s SIMULATION] [-b BATCH] [-t VERSION] [-d] [-v]
```

## Options
Option|Description
|--|--|
|-h, --help       |       Show this help message and exit|
|-s, --simulation_name [SIMULATION_NAME]       |       Simulation name|
|-n, --batch_name [BATCH_NAME]       |       Sets a name for the run|
|--version [VERSION]       |       The batch run version.<br/>.citros/data/{sim_name}/{batch_name}/{ **batch_version**}/{sid}|
|-d, --debug       |       Set logging level to debug|
|-v, --verbose       |       Use verbose console prints|



## Examples

```sh
$ citros data tree info --simulation simulation_1 --batch "batch" --version 20240207190125
────────────────────── simulation_1 / batch / 20240207190125 ───────────────────────
{
  "branch": "main",
  "commit": "0f0b75858fdfd4667323c93122799c88edbd6f81",
  "completions": "2",
  "cpu": 2,
  "created_at": "2024-02-07 19:01:25",
  "gpu": 0,
  "memory": 265,
  "message": "batch message",
  "metadata": "",
  "name": "batch",
  "simulation": "simulation_cannon_analytic",
  "status": "RUNNING",
  "storage_type": "MCAP",
  "timeout": 60,
  "updated_at": "2024-02-07 19:01:25"
}
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
│❯ Info                                                                            │
│  Load                                                                            │
│  Unload                                                                          │
│  Delete                                                                          │
│  ---------------                                                                 │
│  EXIT                                                                            │
└──────────────────────────────────────────────────────────────────────────────────┘
```
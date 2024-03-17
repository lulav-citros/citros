---
sidebar_label: 'citros report generate'
---

# `citros report generate`

### Description

The `generate` command generates a signed pdf report from a batch of simulations and a set of notebooks

```bash
$ citros report generate [-h] [-dir DIR] -n [NAME] -m [MESSAGE] -s [SIMULATION] -b [BATCH] 
                         [-ver [VERSION]] [-nb NOTEBOOKS [NOTEBOOKS ...]] [-style STYLE_PATH] 
                         [-output OUTPUT] [--sign] [-key KEY_PATH] [-d] [-v]
```

## Options

Option|Description
|--|--|
|-h, --help       |       Show help message|
|-dir DIR       |       The working dir of the project|
|-s, --simulation [SIMULATION]       |       Simulation name|
|-b, --batch [BATCH]       |       Sets a name for the batch run|
|-n, --name [NAME]       |       Sets a name for the report|
|-m, --message [MESSAGE]       |       Sets a message for the run|
|--version [VERSION]       |       The batch run version.<br/>.citros/data/{sim_name}/{batch_name}/{ **batch_version**}/{sid}|
|-nb, --notebooks NOTEBOOKS [NOTEBOOKS ...]       |       Paths to Jupyter notebooks|
|-style, --style-path STYLE_PATH       |       Path to CSS style file|
|-output, --output OUTPUT       |       Path to output folder|
|--sign        |       Sign PDFs|
|-key, --key-path KEY_PATH        |       Path to private key file for signing|
|-d, --debug       |       Set logging level to debug|
|-v, --verbose       |       Use verbose console prints|


## Example:

```bash
$ citros report generate -n report -m "test report" -s simulation_1 -b batch 
? Select notebook: Use [space] to select notebooks, [enter] to confirm selection. 
┌────────────────────────────────────────────────────────────────────────────────────┐
│❯ citros_template/notebooks/notebook1.ipynb                                         │
│  citros_template/notebooks/notebook2.ipynb                                         │
└────────────────────────────────────────────────────────────────────────────────────┘
Executing notebook...
progress: 0
===================================== test session starts =====================================
platform linux -- Python 3.10.12, pytest-8.0.0, pluggy-1.4.0
rootdir: /workspaces/test
plugins: ament-flake8-0.12.7, launch-testing-ros-0.19.5, ament-lint-0.12.7, ament-copyright-0.12.7, ament-pep257-0.12.7, ament-xmllint-0.12.7, launch-testing-1.0.4, anyio-4.2.0, xdist-3.5.0, metadata-3.1.1, nbmake-1.5.0, html-4.1.1, colcon-core-0.12.1
4 workers [1 item]          
.                                                                                                [100%]
===================================== 1 passed, 1 warning in 3.78s =====================================
progress: 100
Report generation completed at ".citros/reports/report/20240213131820"
```

:::note
1. When entering the explicit command, it is mandatory adding **report name** **report message**, **simulation name** and a **batch name** 
2. If you have more than one version in the batch, it is recommended to add **batch version** as well to avoid confusion.
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
│  Data: for data management                                                         │
│❯ Report: generation and management                                                 │
│  ---------------                                                                   │
│  EXIT                                                                              │
└────────────────────────────────────────────────────────────────────────────────────┘
```

```sh
? Select Action: Report: generation and management
? Select Action: 
┌────────────────────────────────────────────────────────────────────────────────────┐
│  List: reports list                                                                │
│❯ Generate: new report                                                              │
│  ---------------                                                                   │
│  EXIT                                                                              │
└────────────────────────────────────────────────────────────────────────────────────┘
```
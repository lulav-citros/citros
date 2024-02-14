---
sidebar_label: 'citros report list'
---

# `citros report list`

## Description

Shows a table of all the reports in `.citros/reports` folder 

Table Field|Description
|--|--|
|Date       |       Thh date the report was generated|
|Name       |       The given name for the report|
|Version       |       The version of the report|
|Message       |       The given message for the report|
|Progress       |       the percentage of the report completion|
|Status       |       Status of the report created. can be One of [`OK`, `FAILED`] values|
|Path       |       The location of the report|


```bash
$ citros report list [-h] [-dir DIR] [-d] [-v]
```


## Options
Option|Description
|--|--|
|-h, --help       |       Show help message|
|-dir DIR       |       The working dir of the project|
|-d, --debug       |       Set logging level to debug|
|-v, --verbose       |       Use verbose console prints|


### Example:
```bash
$ citros report list
                            Reports from: .citros/reports                             
┌─────────────┬────────┬─────────────┬─────────────┬──────────┬────────┬─────────────┐
│ Date        │ Name   │ Versions    │ Message     │ Progress │ Status │ Path        │
├─────────────┼────────┼─────────────┼─────────────┼──────────┼────────┼─────────────┤
│ 2024-02-13  │ citros │ 2024021312… │ report      │      100 │ OK     │ .citros/rep │
│ 12:56:46    │        │             │ message     │          │        │ orts/citros │
│             │        │             │             │          │        │ /2024021312 │
│             │        │             │             │          │        │ 5646        │
│ 2024-02-13  │        │ 2024021312… │ report      │      100 │ FAILED │ .citros/rep │
│ 12:55:46    │        │             │ message     │          │        │ orts/citros │
│             │        │             │             │          │        │ /2024021312 │
│             │        │             │             │          │        │ 5546        │
│ 2024-02-13  │        │ 2024021312… │ report      │      100 │ OK     │ .citros/rep │
│ 12:54:03    │        │             │ message     │          │        │ orts/citros │
│             │        │             │             │          │        │ /2024021312 │
│             │        │             │             │          │        │ 5403        │
│ 2024-02-13  │        │ 2024021312… │ report      │      100 │ OK     │ .citros/rep │
│ 12:53:27    │        │             │ message     │          │        │ orts/citros │
│             │        │             │             │          │        │ /2024021312 │
│             │        │             │             │          │        │ 5327        │
│ 2024-02-13  │        │ 2024021312… │ report      │      100 │ FAILED │ .citros/rep │
│ 12:38:31    │        │             │ message     │          │        │ orts/citros │
│             │        │             │             │          │        │ /2024021312 │
│             │        │             │             │          │        │ 3831        │
│ 2024-02-13  │ report │ 2024021313… │ test report │      100 │ OK     │ .citros/rep │
│ 13:18:20    │        │             │             │          │        │ orts/report │
│             │        │             │             │          │        │ /2024021313 │
│             │        │             │             │          │        │ 1820        │
│ 2024-02-13  │        │ 2024021313… │ test report │        0 │ START  │ .citros/rep │
│ 13:18:06    │        │             │             │          │        │ orts/report │
│             │        │             │             │          │        │ /2024021313 │
│             │        │             │             │          │        │ 1806        │
│ 2024-02-13  │        │ 2024021313… │ test report │        0 │ START  │ .citros/rep │
│ 13:17:20    │        │             │             │          │        │ orts/report │
│             │        │             │             │          │        │ /2024021313 │
│             │        │             │             │          │        │ 1720        │
└─────────────┴────────┴─────────────┴─────────────┴──────────┴────────┴─────────────┘
```

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
│❯ List: reports list                                                                │
│  Generate: new report                                                              │
│  ---------------                                                                   │
│  EXIT                                                                              │
└────────────────────────────────────────────────────────────────────────────────────┘
```
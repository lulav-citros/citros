---
sidebar_label: 'citros data db stop'
---

# `citros data db stop`

## Description

The `stop` command stops the database instance. 

```bash
$ citros data db stop [-h] [-d] [-v]
```

## Options
Option|Description
|--|--|
|-h, --help       |       Show help message|
|-d, --debug       |       Set logging level to debug|
|-v, --verbose       |       Use verbose console prints|

## Example

```bash
$ citros data db stop
CITROS DB is stopped.
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
│  Tree view                                                                         │
│  List data                                                                         │
│❯ DB: section                                                                       │
│  ---------------                                                                   │
│  EXIT                                                                              │
└────────────────────────────────────────────────────────────────────────────────────┘
```

```sh
? Select Action: Data: for data management 
? Select Action: DB: section
? Select Action: 
┌────────────────────────────────────────────────────────────────────────────────────┐
│  Create: create citros db docker instance and initializes it.                      │
│  Remove: remove the db instance from docker.                                       │
│  Init: initialize the db instance                                                  │
│  Clean: clears all data from DB.                                                   │
│  Status: Show whether the service is up or not                                     │
│  Start: starts the citros db docker instance if exists.                            │
│❯ Stop: stops the citros db docker instance if running.                             │
│  Logs: show logs of DB instance                                                    │
│  ---------------                                                                   │
│  EXIT                                                                              │
└────────────────────────────────────────────────────────────────────────────────────┘
```
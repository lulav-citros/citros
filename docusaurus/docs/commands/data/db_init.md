---
sidebar_label: 'citros data db init'
---

# `citros data db init`
## Description

The `init` command initializes the database.

```bash
$ citros data db init [-h] [-d] [-v]
```

## Options
Option|Description
|--|--|
|-h, --help       |       Show this help message and exit|
|-d, --debug       |       Set logging level to debug|
|-v, --verbose       |       Use verbose console prints|

## Example

```bash
$ citros data db init
Initializing DB...
DB is running at: localhost:5454
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
│❯ Init: initialize the db instance                                                  │
│  Clean: clears all data from DB.                                                   │
│  Status: Show weather the serivce is up or not                                     │
│  Start: starts the citros db docker instance if exists.                            │
│  Stop: stops the citros db docker instance if running.                             │
│  Logs: show logs of DB instance                                                    │
│  ---------------                                                                   │
│  EXIT                                                                              │
└────────────────────────────────────────────────────────────────────────────────────┘
```
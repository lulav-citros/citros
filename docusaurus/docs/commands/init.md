---
sidebar_label: 'citros init'
---

# `citros init`

## Description

The `init` command is used to initialize a CITROS repository  in an idempotent way. 

The initialization process involves creating a `.citros` directory within your ROS project directory and generating several files and folders therein. These files are set up to allow you to run a simulation of your project with default configurations and settings. You can tailor your CITROS repository to your specific needs by manually modifying these files (see the Project Configuration section for more details).

```bash
$ citros init [-h] [-dir DIR] [-d] [-v]
```

***Idempotence** 
**means that no matter how many times you execute it the `init` command, you achieve the same result.*

## Options

Option|Description
|--|--|
|-h, --help       |       Show help message|
|-dir DIR       |       The working dir of the project|
|-d, --debug       |       Set logging level to debug|
|-v, --verbose       |       Use verbose console prints|

## Example
```bash
$ citros init
initializing CITROS at ["path to ros2 project"]. 
```

## Interactive Mode

```bash
$ citros
```

```sh
? Select Action: 
┌────────────────────────────────────────────────────────────────────────────────────┐
│❯ Init: initialize .citros in current directory                                     │
│  Run: new simulation                                                               │
│  Data: for data management                                                         │
│  Report: generation and management                                                 │
│  ---------------                                                                   │
│  EXIT                                                                              │
└────────────────────────────────────────────────────────────────────────────────────┘
```

```sh
? Select Action: Init: initialize .citros in current directory
initializing CITROS at ["path to ros2 project"]. 
```

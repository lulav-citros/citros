---
sidebar_label: 'citros data db logs'
---

# `citros data db logs`

## Description

the `logs` command prints the logs of the database instance.

```bash
$ citros data db logs [-h] [-d] [-v]
```

## Options
Option|Description
|--|--|
|-h, --help       |       Show this help message and exit|
|-d, --debug       |       Set logging level to debug|
|-v, --verbose       |       Use verbose console prints|

## Example

```bash
$ citros data db logs
──────────────────  Logs from CITROS database container: citros_db ──────────────────
The files belonging to this database system will be owned by user "postgres".
This user must also own the server process.

The database cluster will be initialized with locale "en_US.utf8".
The default database encoding has accordingly been set to "UTF8".
The default text search configuration will be set to "english".

Data page checksums are disabled.

fixing permissions on existing directory /var/lib/postgresql/data ... ok
creating subdirectories ... ok
selecting dynamic shared memory implementation ... posix
selecting default max_connections ... 100
selecting default shared_buffers ... 128MB
selecting default time zone ... Etc/UTC
creating configuration files ... ok
running bootstrap script ... ok
performing post-bootstrap initialization ... ok
syncing data to disk ... ok


initdb: warning: enabling "trust" authentication for local connections
Success. You can now start the database server using:

initdb: hint: You can change this by editing pg_hba.conf or using the option -A, or 
--auth-local and --auth-host, the next time you run initdb.
pg_ctl -D /var/lib/postgresql/data -l logfile start

waiting for server to start....2024-02-11 08:36:02.334 UTC [48] LOG:  starting 
PostgreSQL 16.1 (Debian 16.1-1.pgdg120+1) on x86_64-pc-linux-gnu, compiled by gcc 
(Debian 12.2.0-14) 12.2.0, 64-bit
2024-02-11 08:36:02.335 UTC [48] LOG:  listening on Unix socket 
"/var/run/postgresql/.s.PGSQL.5432"
2024-02-11 08:36:02.338 UTC [51] LOG:  database system was shut down at 2024-02-11 
08:36:02 UTC
2024-02-11 08:36:02.341 UTC [48] LOG:  database system is ready to accept connections
done
server started
CREATE DATABASE

...
─────────────────────────────────────────────────────────────────────────────────────

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
│  Status: Show weather the serivce is up or not                                     │
│  Start: starts the citros db docker instance if exists.                            │
│  Stop: stops the citros db docker instance if running.                             │
│❯ Logs: show logs of DB instance                                                    │
│  ---------------                                                                   │
│  EXIT                                                                              │
└────────────────────────────────────────────────────────────────────────────────────┘
```
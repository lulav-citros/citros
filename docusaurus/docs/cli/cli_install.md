# Installation

The following document will guide you through CITROS CLI installation.

## Prerequisites

- [Docker](https://www.docker.com/)
- [Python3](https://www.python.org/downloads/)
- [git](https://git-scm.com/)

## Installation

To install CITROS using pip, open terminal and write the following command:

    $ pip install citros 

to make sure the installation was successful, run

    $ citros -V
    1.2.59

to get the installed version. 

In some environments you **might** also need to make sure the installation directory is in your `PATH` environment variable, either by 

    $ source ~/.profile

or 

    $ set PATH=/usr/local/bin:$PATH

## Environment Variables
   
   `citros_cli` uses several environment variables, some of which you may change according to your needs, although for the most part, the defaults are likely to be what you want. Generally speaking, most of these are only used by developers of the package, and should not be used.

| ENV | Description |
| --- | --- |
| `CITROS_DOMAIN` | The main domain, defaults to `citros.io` |
| `CITROS_DIR` | Used by the citros cluster, do not use. |
| `CITROS_SIM_RUN_DIR` | The directory under `.citros/runs` in which all simulation data will be saved (see [runs](../advanced_guides/citros_structure.md#directory-runs)). This can be handy, if your code needs to know this location in order to access some of the files, e.g. parameter setups. |
| `CITROS_NETWORK_CHECK_URL` | If you do not have access to the internet, i.e. you're working inside a company intranet and the CITROS servers are installed onsite, change this variable to the url of an intranet site you should always have access to, sort of like the company `google.com`.|

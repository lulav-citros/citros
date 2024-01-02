# CLI Installation

The following document will guide you through CITROS CLI installation.


## Prerequisites

- [vscode](https://code.visualstudio.com/download)
- [Docker](https://www.docker.com/)
- [Python3](https://www.python.org/downloads/)
- [git](https://git-scm.com/)

## Installation

<Tabs groupId="install-options">

<TabItem value="op1" label="Without Code">

    $ pip install citros 

</TabItem>

<TabItem value="op2" label="With Code">

1. Clone the repo:
    
```shell 
    $ git clone git@citros.io:lulav/citros_cli.git
```
2.  Within the cloned `citros_cli` folder, Install the package to a global bin folder:

```shell 
    $ python3 -m pip install .
    $ source ~/.profile
```

</TabItem>

<TabItem value="op3" label="With Code and Soft Links">

If you are developing the citros_cli package itself, than the best practice is to create a `utils` directory under a ROS project.

1. Clone the repo:

```shell 
    $ git clone git@citros.io:lulav/citros_cli.git
```

2. Within the cloned `citros_cli` folder, Install the package to a global bin folder:

```shell 
    $ python3 -m pip install .
    $ source ~/.profile
```

3. Install the package with soft links to dev environment. I.e. from your ROS project dir:

```shell 
    $ mkdir utils && cd utils
    $ git clone git@citros.io:lulav/citros_cli.git
    $ cd ..
    $ python3 -m pip install -e utils/citros_cli
  ```

</TabItem>
</Tabs>

## Environment Variables
   
   `citros_cli` uses several environment variables, some of which you may change according to your needs, although for the most part, the defaults are likely to be what you want. Generally speaking, most of these are only used by developers of the package, and should not be used.

| ENV | Description | used in |
| --- | --- | --- |
| `CITROS_DOMAIN` | The main domain, defaults to `citros.io` | all packages |
| `CITROS_DIR` | Used by the citros cluster, do not use. | citros |
| `CITROS_SIM_RUN_DIR` | The directory under `.citros/runs` in which all simulation data will be saved (see [runs](../citros_structure.md#directory-runs)). This can be handy, if your code needs to know this location in order to access some of the files, e.g. parameter setups. | citros |

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
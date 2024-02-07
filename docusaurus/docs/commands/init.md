```sh
$ citros init [-dir <folder_name>] 
              [-d | --debug] 
              [-v | --verbose]               
```

### Description

The `init` command is used to initialize a CITROS repository idempotently. 

The initialization process involves creating a `.citros` directory within your ROS project directory and generating several files and folders therein. These files are set up to allow you to run a simulation of your project with default configurations and settings. You can tailor your CITROS repository to your specific needs by manually modifying these files (see the Project Configuration section for more details).

***Idempotence***
*means that no matter how many times you execute the `init` command, you achieve the same result.*

### Example:
```bash
$ citros init
initializing CITROS at ["path to ros2 project"]. 
```


"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[32611],{3905:(e,t,a)=>{a.d(t,{Zo:()=>u,kt:()=>h});var n=a(67294);function i(e,t,a){return t in e?Object.defineProperty(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}function r(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,n)}return a}function o(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?r(Object(a),!0).forEach((function(t){i(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):r(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}function l(e,t){if(null==e)return{};var a,n,i=function(e,t){if(null==e)return{};var a,n,i={},r=Object.keys(e);for(n=0;n<r.length;n++)a=r[n],t.indexOf(a)>=0||(i[a]=e[a]);return i}(e,t);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);for(n=0;n<r.length;n++)a=r[n],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(i[a]=e[a])}return i}var s=n.createContext({}),p=function(e){var t=n.useContext(s),a=t;return e&&(a="function"==typeof e?e(t):o(o({},t),e)),a},u=function(e){var t=p(e.components);return n.createElement(s.Provider,{value:t},e.children)},c="mdxType",d={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},m=n.forwardRef((function(e,t){var a=e.components,i=e.mdxType,r=e.originalType,s=e.parentName,u=l(e,["components","mdxType","originalType","parentName"]),c=p(a),m=i,h=c["".concat(s,".").concat(m)]||c[m]||d[m]||r;return a?n.createElement(h,o(o({ref:t},u),{},{components:a})):n.createElement(h,o({ref:t},u))}));function h(e,t){var a=arguments,i=t&&t.mdxType;if("string"==typeof e||i){var r=a.length,o=new Array(r);o[0]=m;var l={};for(var s in t)hasOwnProperty.call(t,s)&&(l[s]=t[s]);l.originalType=e,l[c]="string"==typeof e?e:i,o[1]=l;for(var p=2;p<r;p++)o[p]=a[p];return n.createElement.apply(null,o)}return n.createElement.apply(null,a)}m.displayName="MDXCreateElement"},80001:(e,t,a)=>{a.r(t),a.d(t,{assets:()=>s,contentTitle:()=>o,default:()=>d,frontMatter:()=>r,metadata:()=>l,toc:()=>p});var n=a(87462),i=(a(67294),a(3905));const r={},o=".CITROS File Structure",l={unversionedId:"advanced_guides/citros_structure",id:"version-0.2.63/advanced_guides/citros_structure",title:".CITROS File Structure",description:".CITROS folder and file structure is automatically generated for you (when you run citros init):",source:"@site/versioned_docs/version-0.2.63/advanced_guides/citros_structure.md",sourceDirName:"advanced_guides",slug:"/advanced_guides/citros_structure",permalink:"/docs/0.2.63/advanced_guides/citros_structure",draft:!1,tags:[],version:"0.2.63",frontMatter:{},sidebar:"gettingStartedSidebar",previous:{title:"WHAT IS CITROS",permalink:"/docs/0.2.63/advanced_guides/citros_overview"},next:{title:"install_advanced",permalink:"/docs/0.2.63/advanced_guides/install_advanced"}},s={},p=[{value:"Directory <code>data</code>",id:"directory-data",level:2},{value:"Directory <code>logs</code>",id:"directory-logs",level:2},{value:"Directory <code>notebooks</code>",id:"directory-notebooks",level:2},{value:"Directory <code>parameter_setups</code>",id:"directory-parameter_setups",level:2},{value:"Directory <code>reports</code>",id:"directory-reports",level:2},{value:"Directory <code>simulations</code>",id:"directory-simulations",level:2},{value:"File <code>.gitignore</code>",id:"file-gitignore",level:2},{value:"File <code>project.json</code>",id:"file-projectjson",level:2},{value:"<code>packages</code> Array",id:"packages-array",level:4},{value:"<code>nodes</code> Array",id:"nodes-array",level:4},{value:"File <code>settings.json</code>",id:"file-settingsjson",level:2}],u={toc:p},c="wrapper";function d(e){let{components:t,...a}=e;return(0,i.kt)(c,(0,n.Z)({},u,a,{components:t,mdxType:"MDXLayout"}),(0,i.kt)("h1",{id:"citros-file-structure"},".CITROS File Structure"),(0,i.kt)("p",null,".CITROS folder and file structure is automatically generated for you (when you run ",(0,i.kt)("inlineCode",{parentName:"p"},"citros init"),"):"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre"},"\u2514\u2500\u2500 .citros\n    \u251c\u2500\u2500data\n    \u251c\u2500\u2500 logs\n    \u251c\u2500\u2500 notebooks\n    \u251c\u2500\u2500 parameter_setups\n    \u2502   \u251c\u2500\u2500 default_param_setup.json\n    \u2502   \u2514\u2500\u2500 functions\n    \u2502       \u2514\u2500\u2500 my_func.py\n    \u251c\u2500\u2500 reports\n    \u251c\u2500\u2500 simulations\n    \u2502   \u251c\u2500\u2500 simulation_1.json\n    \u2502   \u251c\u2500\u2500 simulation_2.json\n    \u2502   \u2514\u2500\u2500 simulation_3.json\n    \u251c\u2500\u2500 .gitignore\n    \u251c\u2500\u2500 project.json\n    \u2514\u2500\u2500 settings.json\n\n")),(0,i.kt)("h2",{id:"directory-data"},"Directory ",(0,i.kt)("inlineCode",{parentName:"h2"},"data")),(0,i.kt)("details",null,(0,i.kt)("summary",null,"Description"),"The runs directory stores data and metadata about each run of your simulations. Its structure is as follows:",(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre"},"data\n   \u2514\u2500\u2500 Simulation Name\n       \u2514\u2500\u2500 Batch Name\n           \u2514\u2500\u2500 version\n               \u251c\u2500\u2500 Run ID\n               \u2502   \u251c\u2500\u2500 bags\n               \u2502   \u251c\u2500\u2500 citros.log\n               \u2502   \u251c\u2500\u2500 config\n               \u2502   \u251c\u2500\u2500 environment.json\n               \u2502   \u251c\u2500\u2500 ros.log\n               \u2502   \u2514\u2500\u2500 stats.csv\n               \u251c\u2500\u2500 citros.log\n               \u2514\u2500\u2500 info.json\n")),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"Simulation Name: These directories are named after each of the simulations defined in the simulation files. For every simulation file that is run, a corresponding directory is created here. Each Simulation Name directory may include multiple Batch Name directories.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"Batch Name: This directory holds a batch of simulation runs. A batch consists of multiple runs of the same simulation with different parameters.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"Version ID: ")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"Run ID: Each unique simulation run has its own directory, identified by a Run ID. Under this directory, there are several files and sub-directories:")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"bag"),": This sub-directory holds the recorded data from the simulation run. It includes:")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"bag_0.mcap: This is a ROS bag file that contains all the messages that were sent during the simulation. The default bag format is ",(0,i.kt)("inlineCode",{parentName:"p"},"mcap")," (hence the mcap postfix), but you may also use the ",(0,i.kt)("inlineCode",{parentName:"p"},"sqlite3")," format. See ",(0,i.kt)("a",{parentName:"p",href:"#directory-simulations"},"simulations"),".")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"metadata.yaml: A file holding metadata information associated with the bag file.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"config"),": This sub-directory contains YAML files (pkg1.yaml, pkg2.yaml, etc.) for each package in your ROS project, detailing the actual parameters used in the simulation. If you used any functions in your parameter setup, the values appearing here will be those that were evaluated according to the function you defined.\n")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"citros.log"),": A standard log file, documenting CITROS actions and events that took place during the execution of CITROS commands. Running a CITROS command with the ",(0,i.kt)("inlineCode",{parentName:"p"},"-d")," flag, will change the log level (which is set to ",(0,i.kt)("inlineCode",{parentName:"p"},"INFO")," by default), to ",(0,i.kt)("inlineCode",{parentName:"p"},"DEBUG"),".")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"ros.log"),": A standard log file that was active during the simulation run, documenting ROS actions and events throughout the simulation. "),(0,i.kt)("p",{parentName:"li"},"  ",(0,i.kt)("strong",{parentName:"p"},"Note:")," the destination of ROS logs is controlled by the ",(0,i.kt)("inlineCode",{parentName:"p"},"output")," parameter to ",(0,i.kt)("inlineCode",{parentName:"p"},"Node")," instances defined in the launch file being used. There are 3 possible values this parameter can take:"),(0,i.kt)("ul",{parentName:"li"},(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"log"),": This option directs the output to log files.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"screen"),": This option directs the output to the console or screen, which is useful for debugging purposes.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"both"),": This option combines the functionalities of both ",(0,i.kt)("inlineCode",{parentName:"p"},"log")," and ",(0,i.kt)("inlineCode",{parentName:"p"},"screen"),", directing the output simultaneously to the log file and the screen."),(0,i.kt)("p",{parentName:"li"},"For example, the ROS logger output for the following node, defined in ",(0,i.kt)("inlineCode",{parentName:"p"},"cannon_analytic.launch.py"),", will be written to both the console and the log file:"),(0,i.kt)("pre",{parentName:"li"},(0,i.kt)("code",{parentName:"pre",className:"language-python"},"cannon_analytic_node=Node(\npackage = 'cannon_analytic',\nname = 'analytic_dynamics',\nexecutable = 'analytic_dynamics',\nparameters = [config_analytic],\noutput='both',\nemulate_tty=True\n)\n"))))),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"environment.json"),": A file capturing a snapshot of your environment variables and Python packages at the time of the simulation run.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"info.json"),": A JSON file containing general metadata about the run, such as batch ID, batch name, datetime of the run, user's Git commit and branch information, and CITROS' Git commit and branch information, as well as a hash of the bag file.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"metrics.csv"),": A CSV file recording system performance metrics during the simulation run, including CPU usage, total memory, available memory, used memory, and memory usage percentage."))),(0,i.kt)("p",null,"These files collectively provide a comprehensive record of each simulation run, the conditions under which it was run, and the results it produced. This makes it easy to reproduce and understand the results of each simulation.")),(0,i.kt)("h2",{id:"directory-logs"},"Directory ",(0,i.kt)("inlineCode",{parentName:"h2"},"logs")),(0,i.kt)("details",null,(0,i.kt)("summary",null,"Description")),(0,i.kt)("h2",{id:"directory-notebooks"},"Directory ",(0,i.kt)("inlineCode",{parentName:"h2"},"notebooks")),(0,i.kt)("details",null,(0,i.kt)("summary",null,"Description"),"This folder contains Jupiter notebook files you may use for data analysis of your simulation results."),(0,i.kt)("h2",{id:"directory-parameter_setups"},"Directory ",(0,i.kt)("inlineCode",{parentName:"h2"},"parameter_setups")),(0,i.kt)("details",null,(0,i.kt)("summary",null,"Description"),(0,i.kt)("p",null,"The ",(0,i.kt)("inlineCode",{parentName:"p"},"parameter_setups")," directory stores your JSON-formatted parameter setup files. When you initialize your CITROS repository, a ",(0,i.kt)("inlineCode",{parentName:"p"},"default_param_setup.json")," file is automatically generated. This file consolidates all the default parameters for every node across all the packages in your ROS project, providing a consolidated and easily accessible record of these parameters."),(0,i.kt)("p",null,"The file ",(0,i.kt)("inlineCode",{parentName:"p"},"default_param_setup.json")," will not be overwritten during CITROS ",(0,i.kt)("inlineCode",{parentName:"p"},"init"),", ",(0,i.kt)("inlineCode",{parentName:"p"},"run")," or ",(0,i.kt)("inlineCode",{parentName:"p"},"status")," commands. Nevertheless, it is recommended to duplicate this file under a different name within the ",(0,i.kt)("inlineCode",{parentName:"p"},"parameter_setups")," directory before making any modifications. This practice ensures your custom setups are preserved and allows you to experiment with various parameter configurations."),(0,i.kt)("p",null,"The structured format of the parameter setup files streamlines both the understanding and alteration of parameters for each node in your ROS project. This becomes especially valuable when you're keen to explore the influence of different parameter values on your ROS project's behavior. Take, for instance, a static parameter value like 42. Instead of hard-coding it, you could use a ",(0,i.kt)("em",{parentName:"p"},"function object")," to derive a value from a normal distribution centered at 42. The introduction of function objects broadens your horizons, enabling you to use any numpy function or even craft user-defined functions for meticulous computational adjustments. A prime example is when parameter values are intricate, making them cumbersome to hard-code; in such scenarios, you can devise a function to fetch them from a file. In essence, this newfound flexibility paves the way for limitless computational and manipulative possibilities for your parameters."),(0,i.kt)("p",null,"To learn how to add functions to parameter setups, please refer to the ",(0,i.kt)("a",{parentName:"p",href:"/docs/0.2.63/guides/config_params"},"Adding functions to parameter setup")," section.")),(0,i.kt)("h2",{id:"directory-reports"},"Directory ",(0,i.kt)("inlineCode",{parentName:"h2"},"reports")),(0,i.kt)("details",null,(0,i.kt)("summary",null,"Description"),"This folder holds reports describing the results of your simulation runs."),(0,i.kt)("h2",{id:"directory-simulations"},"Directory ",(0,i.kt)("inlineCode",{parentName:"h2"},"simulations")),(0,i.kt)("details",null,(0,i.kt)("summary",null,"Description"),(0,i.kt)("p",null,"The ",(0,i.kt)("inlineCode",{parentName:"p"},"simulations")," directory stores your JSON-formatted simulation files."),(0,i.kt)("p",null,"A simulation json file is an auto-generated file corresponding to each launch file in your ROS project. For instance, a launch file named ",(0,i.kt)("inlineCode",{parentName:"p"},"foo.launch.py")," will have a corresponding ",(0,i.kt)("inlineCode",{parentName:"p"},"simulation_foo.json")," file. This file outlines the details necessary to run the corresponding simulation, specifying parameters, resources, and launch files."),(0,i.kt)("p",null,"Here's a breakdown of its typical structure and content:"),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"description"),": This is a descriptive field for the simulation setup. You can modify it to better describe your specific simulation.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"parameter_setup"),": This field points to the parameter setup JSON file that will be used for this simulation. By default, it points to ",(0,i.kt)("inlineCode",{parentName:"p"},"default_param_setup.json"),", but you can point it to any custom parameter setup file you created in the ",(0,i.kt)("inlineCode",{parentName:"p"},"parameter_setups")," directory.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"launch_file"),": Specifies the ROS launch file that will be used to start the simulation. For instance, ",(0,i.kt)("inlineCode",{parentName:"p"},"foo.launch.py"),".")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"timeout"),": This is the maximum time (in seconds) the simulation is allowed to run. The default is 60 seconds. If the simulation does not conclude within this timeframe, it will be terminated.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"GPU"),": Specifies the number of GPU resources required for the simulation. The default is 0, indicating that no GPU resources are needed.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"CPU"),": Specifies the number of CPU resources required for the simulation. The default is 2.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"MEM"),": Specifies the amount of memory required for the simulation in megabytes, e.g., 265.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"storage_type"),": This setting determines the storage format for the ROS bag files generated during the simulation's runs. The possible valid value are ",(0,i.kt)("inlineCode",{parentName:"p"},"SQLITE3")," and ",(0,i.kt)("inlineCode",{parentName:"p"},"MCAP")," (default)."))),(0,i.kt)("p",null,"You can modify these fields to suit your simulation needs, just remember to save your customized version under a different name to prevent overwriting during citros ",(0,i.kt)("inlineCode",{parentName:"p"},"init"),", ",(0,i.kt)("inlineCode",{parentName:"p"},"run"),", or ",(0,i.kt)("inlineCode",{parentName:"p"},"status")," commands.")),(0,i.kt)("h2",{id:"file-gitignore"},"File ",(0,i.kt)("inlineCode",{parentName:"h2"},".gitignore")),(0,i.kt)("details",null,(0,i.kt)("summary",null,"Description"),"This file may be used by the user to specify names of packages and launch files in the project that should be ignored by CITROS. These packages and launch files will not be parsed and validated. Note that a launch file from another package may still use nodes from ignored packages.",(0,i.kt)("p",null,"To ignore a package, write the package directory path relative to the project directory. A package directory is a directory with a ",(0,i.kt)("inlineCode",{parentName:"p"},"package.xml")," file."),(0,i.kt)("p",null,"Example:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre"},"`src/cannon_analytic`\n")),(0,i.kt)("p",null,"To ignore a launch file, write the file path relative to the project directory.\nA launch file is a file of the form ",(0,i.kt)("inlineCode",{parentName:"p"},"*.launch.py")),(0,i.kt)("p",null,"Example:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre"},"`src/scheduler/launch/cannon_analytic.launch.py`\n"))),(0,i.kt)("h2",{id:"file-projectjson"},"File ",(0,i.kt)("inlineCode",{parentName:"h2"},"project.json")),(0,i.kt)("details",null,(0,i.kt)("summary",null,"Description"),"The project.json file is a key component of your CITROS repository. It contains metadata about your ROS project, and is automatically generated by the citros `init`, `run` and `status` commands. Here's a description of its top-level fields:",(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"citros_cli_version"),": The CITROS CLI version installed.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"cover"),": A placeholder for a potential image that represents the project.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"description"),": A string for providing a detailed description of the project.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"git"),": The git repository URL associated with the project.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"image"),": A name that corresponds to the docker image of the project.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"is_active"),": A boolean flag indicating whether the project is active or not.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"launches"),": An array for storing metadata about launch files associated with the project. "),(0,i.kt)("p",{parentName:"li"},"  ",(0,i.kt)("strong",{parentName:"p"},"Note"),": these are the global launch files, which are not associated with any specific package. Generally, they are less commonly used. For package launch files, see inside the list of ",(0,i.kt)("a",{parentName:"p",href:"#packages-array"},(0,i.kt)("em",{parentName:"a"},"packages")),".")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"license"),": A string indicating the license of the project.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"name"),": The name of the project. ",(0,i.kt)("em",{parentName:"p"},"Note"),": this is the only field that you may edit and it will not be overwritten during subsequent CITROS commands.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("a",{parentName:"p",href:"#packages-array"},(0,i.kt)("inlineCode",{parentName:"a"},"packages")),": An array of objects that describe the ROS packages that exist within the project.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"path"),": The directory path to the project.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"readme"),": The contents of the project's README file.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"tags"),": An array of strings for tagging and categorizing the project."))),(0,i.kt)("h4",{id:"packages-array"},(0,i.kt)("inlineCode",{parentName:"h4"},"packages")," Array"),(0,i.kt)("p",null,"In the ",(0,i.kt)("inlineCode",{parentName:"p"},"packages")," array, each object describes a specific package within the project. These objects contain similar information to the top-level fields, with additional fields:"),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"maintainer"),": The maintainer of the package.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"maintainer_email"),": The email address of the maintainer.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("a",{parentName:"p",href:"#nodes-array"},(0,i.kt)("inlineCode",{parentName:"a"},"nodes")),": An array of objects describing each node in the package, including their parameters and entry points.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"package_xml"),": The path to the package's XML file.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"setup_py"),": The path to the package's ",(0,i.kt)("inlineCode",{parentName:"p"},"setup.py")," file. For python ROS projects only.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"cmake"),": The path to the package's ",(0,i.kt)("inlineCode",{parentName:"p"},"CMakeLists.txt")," file. For C++ ROS projects only.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"parameters"),": An array of objects that describe the package-level parameters, i.e. parameters which are not associated with any node. As with node-level parameters, this includes their name, type, and value."))),(0,i.kt)("h4",{id:"nodes-array"},(0,i.kt)("inlineCode",{parentName:"h4"},"nodes")," Array"),(0,i.kt)("p",null,"The ",(0,i.kt)("inlineCode",{parentName:"p"},"nodes")," array contains objects that describe the ROS nodes within a package. Each object includes the following fields:"),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"entry_point"),": The entry point for the node, typically the function that should be executed when the node is run.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"name"),": The name of the node.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"parameters"),": An array of objects that describe the parameters associated with the node, including their name, type, and value.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"path"),": The path to the node's Python file.")))),(0,i.kt)("h2",{id:"file-settingsjson"},"File ",(0,i.kt)("inlineCode",{parentName:"h2"},"settings.json")),(0,i.kt)("details",null,(0,i.kt)("summary",null,"Description"),(0,i.kt)("p",null,"The settings.json file holds configuration settings for your CITROS repository. Here is a breakdown of each field in\nthis file:"),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"name"),": The name of the current settings profile. This can be useful if you want to maintain different sets of settings for different contexts (e.g., 'default_settings', 'debug_settings', etc.).")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"force_message"),': This is a boolean setting (in string format). If set to "True", it enforces that a descriptive message is provided for each batch of simulation runs. This can be helpful for keeping track of the purpose or characteristics of each run batch.')),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},(0,i.kt)("inlineCode",{parentName:"p"},"force_batch_name"),': Similar to force_message, this is a boolean setting (in string format). If set to "True", it enforces that a unique name is provided for each batch of simulation runs. This can be useful for organizing and identifying different batches of runs.')))))}d.isMDXComponent=!0}}]);
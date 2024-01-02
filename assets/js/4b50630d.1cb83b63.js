"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[8248],{3905:(e,t,n)=>{n.d(t,{Zo:()=>u,kt:()=>h});var a=n(7294);function i(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function o(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);t&&(a=a.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,a)}return n}function r(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?o(Object(n),!0).forEach((function(t){i(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):o(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function l(e,t){if(null==e)return{};var n,a,i=function(e,t){if(null==e)return{};var n,a,i={},o=Object.keys(e);for(a=0;a<o.length;a++)n=o[a],t.indexOf(n)>=0||(i[n]=e[n]);return i}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(a=0;a<o.length;a++)n=o[a],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(i[n]=e[n])}return i}var s=a.createContext({}),p=function(e){var t=a.useContext(s),n=t;return e&&(n="function"==typeof e?e(t):r(r({},t),e)),n},u=function(e){var t=p(e.components);return a.createElement(s.Provider,{value:t},e.children)},c="mdxType",m={inlineCode:"code",wrapper:function(e){var t=e.children;return a.createElement(a.Fragment,{},t)}},d=a.forwardRef((function(e,t){var n=e.components,i=e.mdxType,o=e.originalType,s=e.parentName,u=l(e,["components","mdxType","originalType","parentName"]),c=p(n),d=i,h=c["".concat(s,".").concat(d)]||c[d]||m[d]||o;return n?a.createElement(h,r(r({ref:t},u),{},{components:n})):a.createElement(h,r({ref:t},u))}));function h(e,t){var n=arguments,i=t&&t.mdxType;if("string"==typeof e||i){var o=n.length,r=new Array(o);r[0]=d;var l={};for(var s in t)hasOwnProperty.call(t,s)&&(l[s]=t[s]);l.originalType=e,l[c]="string"==typeof e?e:i,r[1]=l;for(var p=2;p<o;p++)r[p]=n[p];return a.createElement.apply(null,r)}return a.createElement.apply(null,n)}d.displayName="MDXCreateElement"},9165:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>s,contentTitle:()=>r,default:()=>m,frontMatter:()=>o,metadata:()=>l,toc:()=>p});var a=n(7462),i=(n(7294),n(3905));const o={sidebar_position:5,sidebar_label:"Introduction to CITROS",hide_title:!0},r=void 0,l={unversionedId:"index",id:"index",title:"index",description:"\x3c!--",source:"@site/docs_tutorials/index.md",sourceDirName:".",slug:"/",permalink:"/docs_tutorials/",draft:!1,tags:[],version:"current",sidebarPosition:5,frontMatter:{sidebar_position:5,sidebar_label:"Introduction to CITROS",hide_title:!0},sidebar:"tutorialSidebar",previous:{title:"CITROS in Dockerfile",permalink:"/docs_tutorials/dockerfile_overview/"},next:{title:"Soft Landing",permalink:"/docs_tutorials/soft_landing/"}},s={},p=[{value:"The Cannon Example Project Overview",id:"the-cannon-example-project-overview",level:2},{value:"Table of Contents",id:"table-of-contents",level:2},{value:"Prerequisites",id:"prerequisites",level:2},{value:"Installation",id:"installation",level:2},{value:"Workspace Overview",id:"workspace-overview",level:2},{value:"Running the Solutions",id:"running-the-solutions",level:2},{value:"Visualization with Foxglove",id:"visualization-with-foxglove",level:2},{value:"Working with CITROS",id:"working-with-citros",level:2},{value:"CITROS Initialization",id:"citros-initialization",level:2},{value:"Installation",id:"installation-1",level:3},{value:"Initialization",id:"initialization",level:3},{value:"Simulations",id:"simulations",level:2},{value:"Running a Simulation",id:"running-a-simulation",level:3},{value:"Short Simulations Structure Overview",id:"short-simulations-structure-overview",level:3},{value:"Configuring a Simulation",id:"configuring-a-simulation",level:3},{value:"Review All Simulations Data",id:"review-all-simulations-data",level:3},{value:"Data Analysis",id:"data-analysis",level:2},{value:"Execute Notebook",id:"execute-notebook",level:3},{value:"Results",id:"results",level:4},{value:"Generate Report",id:"generate-report",level:3}],u={toc:p},c="wrapper";function m(e){let{components:t,...o}=e;return(0,i.kt)(c,(0,a.Z)({},u,o,{components:t,mdxType:"MDXLayout"}),(0,i.kt)("h1",{id:"introduction-to-citros"},"Introduction to CITROS"),(0,i.kt)("p",null,"This tutorial will guide you through the CITROS CLI interface, using a simple ROS 2 example project to demonstrate the usage, while providing useful recommendations and best practices. While this is not a comprehensive guide to all CITROS CLI commands, it should get you up and running using your own projects with CITROS in no time. For further details and an exhaustive guide to the CITROS CLI, refer to the ",(0,i.kt)("a",{parentName:"p",href:"https://citros.io/doc/docs_cli"},"CLI Documentation"),"."),(0,i.kt)("p",null,(0,i.kt)("img",{alt:"orangesqueeze",src:n(5253).Z,title:"CITROS CLI",width:"612",height:"384"})),(0,i.kt)("h2",{id:"the-cannon-example-project-overview"},"The Cannon Example Project Overview"),(0,i.kt)("p",null,"This project is a ROS 2 implementation of the ",(0,i.kt)("a",{parentName:"p",href:"https://nasa.github.io/trick/tutorial/ATutASimpleSim"},"cannonball simulation")," provided by NASA Johnson Space Center as part of the tutorial for the\n",(0,i.kt)("a",{parentName:"p",href:"https://nasa.github.io/trick/"},"Trick Simulation Environment"),"."),(0,i.kt)("p",null,"It determines the trajectory and time of impact of a cannon ball that is fired with an initial speed and initial angle, assuming a constant acceleration of gravity (g), and no aerodynamic forces."),(0,i.kt)("p",null,(0,i.kt)("img",{alt:"Cannonball",src:n(5228).Z,title:"Cannonball",width:"640",height:"320"})),(0,i.kt)("p",null,"Two versions of the simulation are provided: an analytic solution and a numeric integration solution."),(0,i.kt)("h2",{id:"table-of-contents"},"Table of Contents"),(0,i.kt)("ol",null,(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("a",{parentName:"li",href:"#prerequisites"},"Prerequisites")),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("a",{parentName:"li",href:"#installation"},"Installation")),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("a",{parentName:"li",href:"#implementation-overview"},"Workspace Overview")),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("a",{parentName:"li",href:"#running-the-solutions"},"Running the Solutions")),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("a",{parentName:"li",href:"#visualization-with-foxglove"},"Visualization with Foxglove")),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("a",{parentName:"li",href:"#working-with-citros"},"Working with CITROS")),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("a",{parentName:"li",href:"#citros-initialization"},"CITROS Initialization")),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("a",{parentName:"li",href:"#simulations"},"Simulations")),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("a",{parentName:"li",href:"#data-analysis"},"Data analysis"))),(0,i.kt)("h2",{id:"prerequisites"},"Prerequisites"),(0,i.kt)("ol",null,(0,i.kt)("li",{parentName:"ol"},"Install ",(0,i.kt)("a",{parentName:"li",href:"https://code.visualstudio.com/download"},"Visual Studio code")),(0,i.kt)("li",{parentName:"ol"},"Install and Run ",(0,i.kt)("a",{parentName:"li",href:"https://docs.docker.com/get-docker/"},"Docker")),(0,i.kt)("li",{parentName:"ol"},"Install ",(0,i.kt)("a",{parentName:"li",href:"https://foxglove.dev/download"},"Foxglove")," (optional)")),(0,i.kt)("h2",{id:"installation"},"Installation"),(0,i.kt)("p",null,"Open cmd on your desktop"),(0,i.kt)("ol",null,(0,i.kt)("li",{parentName:"ol"},"Clone the project:")),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-bash"},"$ git clone git@github.com:citros-garden/cannon.git\n")),(0,i.kt)("ol",{start:2},(0,i.kt)("li",{parentName:"ol"},"Change to Cannon project directory:")),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-bash"},"$ cd ~/cannon\n")),(0,i.kt)("ol",{start:3},(0,i.kt)("li",{parentName:"ol"},"Open Cannon project in VScode:")),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-bash"},"$ code .\n")),(0,i.kt)("ol",{start:5},(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"Re-open in Dev Container"),(0,i.kt)("ol",{parentName:"li"},(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"press on the bottom left corner icon."),(0,i.kt)("p",{parentName:"li"},(0,i.kt)("img",{alt:"Alt text",src:n(8204).Z,width:"1601",height:"881"}))),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"Choose ",(0,i.kt)("strong",{parentName:"p"},"Reopen in Container")),(0,i.kt)("p",{parentName:"li"},(0,i.kt)("img",{alt:"Alt text",src:n(5753).Z,width:"1601",height:"881"}))))),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"Open VScode terminal and make sure you are in the right location"),(0,i.kt)("pre",{parentName:"li"},(0,i.kt)("code",{parentName:"pre"},"ros@docker-desktop:/workspaces/cannon$ \n")))),(0,i.kt)("admonition",{type:"note"},(0,i.kt)("p",{parentName:"admonition"},"From this point, all the actions should be typed in VScode terminal.")),(0,i.kt)("ol",{start:7},(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"Build your project"),(0,i.kt)("pre",{parentName:"li"},(0,i.kt)("code",{parentName:"pre",className:"language-bash"},"$ colcon build\n$ source install/local_setup.bash\n")))),(0,i.kt)("h2",{id:"workspace-overview"},"Workspace Overview"),(0,i.kt)("p",null,"The project is made out of three ROS nodes - ",(0,i.kt)("inlineCode",{parentName:"p"},"cannon_analytic"),", ",(0,i.kt)("inlineCode",{parentName:"p"},"cannon_numeric")," and ",(0,i.kt)("inlineCode",{parentName:"p"},"scheduler"),". The scheduler node is responsible for driving the simulation by publishing a ",(0,i.kt)("inlineCode",{parentName:"p"},"scheduler")," topic at a given rate (say, 100Hz). The cannon nodes subscribe to this topic, and upon receiving it perform a single calculation step. The rate (",(0,i.kt)("inlineCode",{parentName:"p"},"dt"),") is a ROS parameter for the scheduler node, which means you may change its value in the ",(0,i.kt)("inlineCode",{parentName:"p"},"config/params.yaml")," file, without the need to recompile. The two cannon nodes also have ",(0,i.kt)("inlineCode",{parentName:"p"},"params.yaml")," files of their own, in which you can set the initial speed and angle, and also the time/integration delta (",(0,i.kt)("inlineCode",{parentName:"p"},"dt"),")."),(0,i.kt)("p",null,"Additionally, the ",(0,i.kt)("inlineCode",{parentName:"p"},"scheduler")," node subscribes to a ",(0,i.kt)("inlineCode",{parentName:"p"},"debug")," topic, which, together with the provided Foxglove layout, facilitates a play/pause/step/resume functionality."),(0,i.kt)("p",null,"The output of the simulation, i.e. the topic containing the calculated results, is called ",(0,i.kt)("inlineCode",{parentName:"p"},"cannon/state")," (in both analytic and numeric versions). It is a list of ",(0,i.kt)("inlineCode",{parentName:"p"},"float")," of size 4, the layout being:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre"},"[position_x, position_y, velocity_x, velocity_y]\n")),(0,i.kt)("p",null,"The simulation will halt when ",(0,i.kt)("inlineCode",{parentName:"p"},"position_y")," reaches zero (i.e. impact)."),(0,i.kt)("h2",{id:"running-the-solutions"},"Running the Solutions"),(0,i.kt)("p",null,"The cannon project contains two launch files, one for each solution"),(0,i.kt)("ol",null,(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"To Run the analytic solution"),(0,i.kt)("pre",{parentName:"li"},(0,i.kt)("code",{parentName:"pre",className:"language-bash"},"$ ros2 launch scheduler cannon_analytic.launch.py\n"))),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"To run the numeric integration solution"),(0,i.kt)("pre",{parentName:"li"},(0,i.kt)("code",{parentName:"pre",className:"language-bash"},"$ ros2 launch scheduler cannon_numeric.launch.py\n")))),(0,i.kt)("admonition",{type:"note"},(0,i.kt)("p",{parentName:"admonition"},"Running either of the two simulations will result in the logger output being written to the console.")),(0,i.kt)("h2",{id:"visualization-with-foxglove"},"Visualization with Foxglove"),(0,i.kt)("p",null,"To view a graphical representation of the simulation:"),(0,i.kt)("ol",null,(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"Open ",(0,i.kt)("a",{parentName:"p",href:"https://foxglove.dev/"},"Foxglove")," ")),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"Press on Foxglove icon at the top right")),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"Click View")),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},'Click "Import layout from file"'),(0,i.kt)("p",{parentName:"li"},(0,i.kt)("img",{alt:"Alt text",src:n(4767).Z,width:"1601",height:"881"}))),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"Choose ",(0,i.kt)("inlineCode",{parentName:"p"},"CITROS_Cannon.json")," from the cannon project directory")),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"Open a new Connection"),(0,i.kt)("p",{parentName:"li"},(0,i.kt)("img",{alt:"Alt text",src:n(1493).Z,width:"1601",height:"881"}))),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"Choose Rosbridge and press the 'Open' button"),(0,i.kt)("p",{parentName:"li"},(0,i.kt)("img",{alt:"Alt text",src:n(4922).Z,width:"1601",height:"881"}))),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"You now have a working connection to your simulation.")),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"If your simulation has stopped running in the terminal, run one of the ",(0,i.kt)("a",{parentName:"p",href:"#running-the-solutions"},"solutions")," again."))),(0,i.kt)("p",null,"Output example:\n",(0,i.kt)("img",{alt:"Foxglove screenshot",src:n(7219).Z,width:"1212",height:"926"})),(0,i.kt)("h2",{id:"working-with-citros"},"Working with CITROS"),(0,i.kt)("p",null,"Working with the CITROS CLI is pretty straight forward, since there are only two things you need to do - initialize your CITROS repository, and run your project. Additionally, you may configure your CITROS repository to fit your simulation needs, but if all you want to do is to run your project via CITROS with the default configuration, than only two commands are necessary."),(0,i.kt)("h2",{id:"citros-initialization"},"CITROS Initialization"),(0,i.kt)("h3",{id:"installation-1"},"Installation"),(0,i.kt)("p",null,"First, let's make sure we can run CITROS:"),(0,i.kt)("ol",null,(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"Make sure the project (in this case Cannon) is opened inside a VS Code dev-container.")),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"Build and source your project by running:"),(0,i.kt)("pre",{parentName:"li"},(0,i.kt)("code",{parentName:"pre",className:"language-bash"},"$ colcon build\n$ source install/local_setup.bash\n"))),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"in the dev-container's terminal, run"),(0,i.kt)("pre",{parentName:"li"},(0,i.kt)("code",{parentName:"pre",className:"language-bash"},"$ pip install citros\n")),(0,i.kt)("p",{parentName:"li"},"You can verify that the installation succeeded by running "),(0,i.kt)("pre",{parentName:"li"},(0,i.kt)("code",{parentName:"pre",className:"language-bash"},"$ citros -h\n1.2.3\n")),(0,i.kt)("p",{parentName:"li"},"to get the CITROS CLI version installed."))),(0,i.kt)("h3",{id:"initialization"},"Initialization"),(0,i.kt)("p",null,"Alrighty then! You're now ready to run the first command - ",(0,i.kt)("inlineCode",{parentName:"p"},"init"),", which will initialize your local CITROS repository:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-bash"},"$ citros init\n")),(0,i.kt)("p",null,"This command creates a folder named ",(0,i.kt)("inlineCode",{parentName:"p"},".citros")," under your project directory.",(0,i.kt)("br",null),"\nThe ",(0,i.kt)("inlineCode",{parentName:"p"},".citros")," directory contains several files and folders that capture the state of your project and allow you to configure your simulations according to your needs. We will discuss some of them briefly later on. For a full and detailed description of the contents of the ",(0,i.kt)("inlineCode",{parentName:"p"},".citros"),"  directory, refer to the ",(0,i.kt)("a",{parentName:"p",href:"https://citros.io/doc/docs_cli"},"CLI Documentation"),"."),(0,i.kt)("h2",{id:"simulations"},"Simulations"),(0,i.kt)("h3",{id:"running-a-simulation"},"Running a Simulation"),(0,i.kt)("p",null,"After your ",(0,i.kt)("inlineCode",{parentName:"p"},".citros")," repository has been initialized, you're ready to run a CITROS simulation, albeit with all the default configurations, by using the ",(0,i.kt)("inlineCode",{parentName:"p"},"run")," command:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-bash"},"$ citros\n")),(0,i.kt)("p",null,"Choose the ",(0,i.kt)("inlineCode",{parentName:"p"},"Run")," action:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sh"},"? Select Action: \nInit: initialize .citros in current directory \n\u276f Run: new simulation                  \nData: for data management                                            \nReport: generation and management                                               \n")),(0,i.kt)("p",null,"Name the batch run (or press enter for ",(0,i.kt)("em",{parentName:"p"},'"citros"')," as a default batch name):"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sh"},"Please name this batch run: my_first_batch\n")),(0,i.kt)("p",null,"Enter a message for the batch (or press enter for ",(0,i.kt)("em",{parentName:"p"},'"This is a default batch message from citros"')," as a default batch name):"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sh"},"Enter a message for this batch run: My first CITROS simulation!\n")),(0,i.kt)("p",null,"Choose number of runs (or press enter to run once):"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sh"},"How many times you want the simulation to run?: 1\n")),(0,i.kt)("p",null,"Lastly choose ",(0,i.kt)("em",{parentName:"p"},'"simulation_cannon_analytic"'),":"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sh"},"? Please choose the simulation you wish to run: \n\u276f simulation_cannon_analytic\n  simulation_cannon_numeric\n")),(0,i.kt)("admonition",{type:"note"},(0,i.kt)("p",{parentName:"admonition"},"This command will run the simulation on your machine, and save all the results under ",(0,i.kt)("inlineCode",{parentName:"p"},".citros/data/[simulation_name]")," folder. The content of the ",(0,i.kt)("a",{parentName:"p",href:"/docs/cli/citros_structure#directory-runs"},"folder")," will contain "),(0,i.kt)("ul",{parentName:"admonition"},(0,i.kt)("li",{parentName:"ul"},"recorded bags"),(0,i.kt)("li",{parentName:"ul"},"logs from the simulation and citros itself"),(0,i.kt)("li",{parentName:"ul"},"metadata about the run"),(0,i.kt)("li",{parentName:"ul"},"metrics and information about the system it was running "),(0,i.kt)("li",{parentName:"ul"},"and more."))),(0,i.kt)("h3",{id:"short-simulations-structure-overview"},"Short Simulations Structure Overview"),(0,i.kt)("p",null,"To fully understand what's going on, we need to familiarize ourselves with three concepts that are core to the way CITROS works:"),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("h2",{parentName:"li",id:"simulation"},(0,i.kt)("strong",{parentName:"h2"},(0,i.kt)("a",{parentName:"strong",href:"/docs/cli/citros_structure#directory-simulations"},"simulation"))),(0,i.kt)("p",{parentName:"li"},"  The simulation object is defining what you want to run and how. It is a set of the launch file (the what) and the parameter setup (the how) as well as the resources needed for it to run and after how much time it should be killed. "),(0,i.kt)("p",{parentName:"li"},"  Defaults simulation files defined by a ROS 2 launch file. You may have as many launch files as you want in your project, as long as there is at least one. Each simulation will correspond to a launch file in your project. When you run a CITROS simulation, if you don't specify the name of the simulation (using the ",(0,i.kt)("inlineCode",{parentName:"p"},"-s")," flag), a command-line menu will be presented, in which you can use the up and down arrows to choose the simulation you want. The simulation names will be of the form ",(0,i.kt)("inlineCode",{parentName:"p"},"simulation_<name of launch_file>"),". In the case of the Cannon project, we have two launch files - ",(0,i.kt)("inlineCode",{parentName:"p"},"cannon_analytic.launch.py")," and ",(0,i.kt)("inlineCode",{parentName:"p"},"cannon_numeric.launch.py"),", and as you can see in the output above, we are prompted to choose between them. "),(0,i.kt)("p",{parentName:"li"},"  Each simulation also corresponds to a json file of the same name, which resides under the ",(0,i.kt)("a",{parentName:"p",href:"/docs/cli/citros_structure#directory-simulations"},(0,i.kt)("inlineCode",{parentName:"a"},".citros/simulations"))," directory. You may use this file to configure the way your simulation runs. "),(0,i.kt)("p",{parentName:"li"},"  When you run a CITROS simulation, a directory for that simulation is created under the ",(0,i.kt)("a",{parentName:"p",href:"/docs/cli/citros_structure#directory-runs"},(0,i.kt)("inlineCode",{parentName:"a"},".citros/runs"))," directory. This directory will contain subdirectories corresponding to ",(0,i.kt)("strong",{parentName:"p"},"batch"),"es, a new one created every time you run a simulation.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("h2",{parentName:"li",id:"batch"},(0,i.kt)("strong",{parentName:"h2"},"batch")),(0,i.kt)("p",{parentName:"li"},"  Defined as a group of one or more simulation runs. Since you can specify one or more simulations runs ('",(0,i.kt)("em",{parentName:"p"},"completions"),"') when running a CITROS simulation, a ",(0,i.kt)("strong",{parentName:"p"},"batch")," is simply a convenient way to group them together. For instance, in the case of the above example, if we choose ",(0,i.kt)("inlineCode",{parentName:"p"},"simulation_cannon_analytic")," from the menu, the following folder structure will be created: ",(0,i.kt)("inlineCode",{parentName:"p"},".citros/data/simulation_cannon_analytic/my_first_batch/20231231120623/0"),". The last folder - ",(0,i.kt)("inlineCode",{parentName:"p"},"0"),", is the folder corresponding to the only run for this batch - when you don't specify the number of completions (i.e. runs) using the ",(0,i.kt)("inlineCode",{parentName:"p"},"-c")," flag, it will default to 1, and the name of each run is a zero based index, incremented by one for each additional run.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("h2",{parentName:"li",id:"run"},(0,i.kt)("strong",{parentName:"h2"},"run")),(0,i.kt)("p",{parentName:"li"},"  Defined as a single execution of a simulation as defined by the chosen launch file. Launching CITROS simulations with multiple runs ('",(0,i.kt)("em",{parentName:"p"},"completions"),"') is particularly advantageous when working online, in which case a large number of simulation runs can be simultaneously executed on the CITROS cloud."),(0,i.kt)("p",{parentName:"li"},"  The folder corresponding to a simulation run will contain all the information relevant for that run. Look through such a folder after running a simulation and see for yourself. For further details refer to the ",(0,i.kt)("a",{parentName:"p",href:"https://citros.io/doc/docs_cli"},"CLI Documentation")))),(0,i.kt)("p",null,"By default, when using the ",(0,i.kt)("inlineCode",{parentName:"p"},"run")," command, you must provide a batch name (using the ",(0,i.kt)("inlineCode",{parentName:"p"},"-n")," flag) and a message (using the ",(0,i.kt)("inlineCode",{parentName:"p"},"-m")," flag). The name you provide will be used as the name of the directory in which all runs for this batch will be saved. If a batch by that name already exists - no worries, CITROS will simply add a new version under the simulation name you provided, thereby keeping the batch version unique for each simulation. "),(0,i.kt)("p",null,"Now that you understand what's going on, choose one of the simulations presented in the menu, press enter and see it run..."),(0,i.kt)("h3",{id:"configuring-a-simulation"},"Configuring a Simulation"),(0,i.kt)("p",null,"We just ran a simulation with all the default configurations, which is admittedly not that exciting. Let's see how we can turn things up a notch by setting up dynamic parameter evaluation for our simulation, thereby allowing each run within the same batch to have different parameter values."),(0,i.kt)("p",null,"The ",(0,i.kt)("a",{parentName:"p",href:"/docs/cli/citros_structure#directory-parameter_setups"},(0,i.kt)("inlineCode",{parentName:"a"},".citros/parameter_setups"))," directory stores your JSON-formatted parameter setup files. When you initialize your citros repository, a ",(0,i.kt)("inlineCode",{parentName:"p"},"default_param_setup.json")," file is automatically generated. This file consolidates all the default parameters for every node across all the packages in your ROS project, providing a consolidated and easily accessible record of these parameters."),(0,i.kt)("p",null,"The structured format of the parameter setup files streamlines both the understanding and alteration of parameters for each node in your ROS project. This becomes especially valuable when you're keen to explore the influence of different parameter values on your ROS project's behavior."),(0,i.kt)("p",null,"In the Cannon project, we have a total of three nodes. Let's look at the parameters for the ",(0,i.kt)("inlineCode",{parentName:"p"},"analytic_dynamics")," node in the ",(0,i.kt)("inlineCode",{parentName:"p"},"cannon_analytic")," package, as defined in the ",(0,i.kt)("inlineCode",{parentName:"p"},"default_param_setup.json")," file.\nWe can see we have 3 parameters to play around with - ",(0,i.kt)("inlineCode",{parentName:"p"},"init_speed"),", ",(0,i.kt)("inlineCode",{parentName:"p"},"init_angle")," and ",(0,i.kt)("inlineCode",{parentName:"p"},"dt"),". "),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-json"},'//[project]/.citros/parameter_setups/default_param_setup.json\n{\n    "packages": {\n        "cannon_analytic": {\n            "analytic_dynamics": {\n                "ros__parameters": {\n                    "init_speed": 50.0,\n                    "init_angle": 30.0,\n                    "dt": 0.01\n                }\n            }\n        },\n        ...\n    }\n}\n')),(0,i.kt)("p",null,"Let's say we want to find out the optimal initial angle for the cannon, which will provide the maximum range. Assuming we're completely blanking out on high-school physics, let's randomize the value for this parameter, execute several simulation runs, and see where we get the maximum range. To achieve this, we can simply replace the hard-coded default value with a ",(0,i.kt)("a",{parentName:"p",href:"/docs/cli/config_params"},(0,i.kt)("strong",{parentName:"a"},"function object")),". Function objects are json objects comprised of two fields - ",(0,i.kt)("inlineCode",{parentName:"p"},"function")," and ",(0,i.kt)("inlineCode",{parentName:"p"},"args"),". They come in two flavors - numpy and user-defined. For our purposes we can use numpy's random module to generate a normal distribution around a given value:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre"},'"init_angle": {\n                "function": "numpy.random.normal",\n                "args": [45, 15]\n            },\n')),(0,i.kt)("p",null,"This will cause a normal distribution with a standard deviation of 15 around 45 to be evaluated for every simulation run."),(0,i.kt)("p",null,"Another way to use the run command is writing the full command: "),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-bash"},'citros run -n "test_params" -m "testing random initial angle" -c 10\n')),(0,i.kt)("p",null,"and choose ",(0,i.kt)("inlineCode",{parentName:"p"},"simulation_cannon_analytic")," from the menu, the simulation will run 10 times (sequentially if working offline), and each time the cannon will have a different initial angle. By looking at the ",(0,i.kt)("a",{parentName:"p",href:"#data-analysis-online-only"},"results"),", we can hopefully come to the conclusion that 45 degrees is the optimal angle. "),(0,i.kt)("h3",{id:"review-all-simulations-data"},"Review All Simulations Data"),(0,i.kt)("p",null,"To view all simulations use the data command:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-bash"},"$ citros\n")),(0,i.kt)("p",null,"Choose the ",(0,i.kt)("inlineCode",{parentName:"p"},"Data")," action:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sh"},"? Select Action: \nInit: initialize .citros in current directory \nRun: new simulation                  \n\u276f Data: for data management                                            \nReport: generation and management                                            \n")),(0,i.kt)("p",null,"Choose ",(0,i.kt)("inlineCode",{parentName:"p"},"List")," to view all simulations"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sh"},"\u276f List: list all runs\nsimulation_cannon_analytic\nsimulation_cannon_numeric   \n")),(0,i.kt)("p",null,"Table of all the simulations will be shown as output. ",(0,i.kt)("br",null),"\nThe table contains the following fields: Run name, Versions, message, status, completions, path"),(0,i.kt)("p",null,(0,i.kt)("img",{alt:"Alt text",src:n(8788).Z,width:"1010",height:"527"})),(0,i.kt)("h2",{id:"data-analysis"},"Data Analysis"),(0,i.kt)("h3",{id:"execute-notebook"},"Execute Notebook"),(0,i.kt)("p",null,"After you've run a batch run on CITROS, your data is stored on CITROS's servers.\nyou can access the data using Python ",(0,i.kt)("a",{parentName:"p",href:"https://pypi.org/project/citros-data-analysis/"},"citros data analysis package")," either from the Python ",(0,i.kt)("a",{parentName:"p",href:"https://citros.io/cannon/blob/main/notebooks/data_analysis.ipynb"},"notebook")," or from a local kernel Python environment."),(0,i.kt)("admonition",{type:"note"},(0,i.kt)("p",{parentName:"admonition"},"citros data analysis package is installed while running ",(0,i.kt)("inlineCode",{parentName:"p"},"pip install citros"),", so at this point you should have this package and you don't have to download it again.")),(0,i.kt)("ol",null,(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"Open .citros directory")),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"Go to notebooks.")),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"Open data_analysis.ipynb")),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"Press ",(0,i.kt)("inlineCode",{parentName:"p"},"Run All")," button")),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"Scroll down the notebook to see the results."))),(0,i.kt)("h4",{id:"results"},"Results"),(0,i.kt)("p",null,"here is a sample from the provided ",(0,i.kt)("a",{parentName:"p",href:"https://citros.io/cannon/blob/main/notebooks/data_analysis.ipynb"},"notebook"),":"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},"#import matplotlib\nimport matplotlib.pyplot as plt\n\n#create a figure to plot on\nfig, ax = plt.subplots()\n\ncitros.batch(-1).topic('/cannon/state').sid([0,1,2,3,4]).\\\n       time_plot(ax, var_name = 'data.data[1]', time_step = 0.01, y_label = 'y', title_text = 'y vs. t')\n")),(0,i.kt)("p",null,(0,i.kt)("img",{alt:"Alt text",src:n(3113).Z,width:"1142",height:"910"})),(0,i.kt)("h3",{id:"generate-report"},"Generate Report"),(0,i.kt)("p",null,"After running the notebook and verifying that everything works properly you can generate a report from your Python Notebook signed by CITROS."),(0,i.kt)("p",null,"run citros command"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-bash"},"$ citros\n")),(0,i.kt)("p",null,"Choose the ",(0,i.kt)("inlineCode",{parentName:"p"},"Report")," action:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sh"},"? Select Action:                  \nInit: initialize .citros in current directory \nRun: new simulation                  \nData: for data management                                            \n\u276f Report: generation and management                              \n")),(0,i.kt)("p",null,"Choose ",(0,i.kt)("inlineCode",{parentName:"p"},"Generate")," to generate a report"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sh"},"List: reports list\n\u276f Generate: new report\nValidate: report integrity \n")),(0,i.kt)("p",null,"Choose the simulation source for the report"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sh"},"simulation_cannon_analytic \n\u276f simulation_cannon_numeric\n")),(0,i.kt)("p",null,"Select a batch from you batch list"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sh"},"Select Batch: numeric simulations\n")),(0,i.kt)("p",null,"Select a version"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sh"},"Select Batch: numeric simulations\n")),(0,i.kt)("p",null,"Name your report ",(0,i.kt)("em",{parentName:"p"},'(or press enter for "citros" as a default report name)'),":"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sh"},"Please name this report: My first report\n")),(0,i.kt)("p",null,'Enter a message for the report (or press enter for "This is a default message message from citros" as a default report message):'),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sh"},"Enter a message for this report: Best report ever\n")),(0,i.kt)("p",null,"choose the notebook for the report"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sh"},"\u276f citros_template/notebooks/data_analysis.ipynb\ncitros_template/notebooks/test1.ipynb\n")),(0,i.kt)("p",null,"To view your generated report go to .citros/reports/","[report_name]"),(0,i.kt)("admonition",{type:"note"},(0,i.kt)("p",{parentName:"admonition"},"The content of the ",(0,i.kt)("a",{parentName:"p",href:"/docs/cli/citros_structure#directory-reports"},"Reports folder")," will contain "),(0,i.kt)("ul",{parentName:"admonition"},(0,i.kt)("li",{parentName:"ul"},"output of the python notebook"),(0,i.kt)("li",{parentName:"ul"},"Report info"),(0,i.kt)("li",{parentName:"ul"},"Generated pdf report"))))}m.isMDXComponent=!0},5228:(e,t,n)=>{n.d(t,{Z:()=>a});const a=n.p+"assets/images/CannonInit-8344c7c43fee3bdf61ea3be3a4ce9e94.png"},8788:(e,t,n)=>{n.d(t,{Z:()=>a});const a=n.p+"assets/images/cannon_data-c01debf78ab342e534d3a71339c2bead.png"},8204:(e,t,n)=>{n.d(t,{Z:()=>a});const a=n.p+"assets/images/container_corner-f8c50033906f369e40bdaf20be574baf.png"},5753:(e,t,n)=>{n.d(t,{Z:()=>a});const a=n.p+"assets/images/container_open_container-41c041099556b7ec2a713ba2444c9d24.png"},1493:(e,t,n)=>{n.d(t,{Z:()=>a});const a=n.p+"assets/images/foxglove_connection-bf88605ed4e767d61fad33aec9bb154d.png"},4767:(e,t,n)=>{n.d(t,{Z:()=>a});const a=n.p+"assets/images/foxglove_open-f39d9ead654d2eb518c5ce9e0de950aa.png"},4922:(e,t,n)=>{n.d(t,{Z:()=>a});const a=n.p+"assets/images/foxglove_rosbridge-c5e64c6d5b79820786e834d9dcd46959.png"},7219:(e,t,n)=>{n.d(t,{Z:()=>a});const a=n.p+"assets/images/foxglove_screenshot-8b82912ff4ecaed893d7e540e0b4f99d.png"},3113:(e,t,n)=>{n.d(t,{Z:()=>a});const a=n.p+"assets/images/nb_sample-4fb211887f00d4632afa9d8662e467b8.png"},5253:(e,t,n)=>{n.d(t,{Z:()=>a});const a=n.p+"assets/images/orange_squeeze-22d42f55efca96cadffc64eb9efad82f.jpg"}}]);
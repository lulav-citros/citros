"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[3610],{3905:(t,e,a)=>{a.d(e,{Zo:()=>m,kt:()=>k});var n=a(67294);function r(t,e,a){return e in t?Object.defineProperty(t,e,{value:a,enumerable:!0,configurable:!0,writable:!0}):t[e]=a,t}function i(t,e){var a=Object.keys(t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(t);e&&(n=n.filter((function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable}))),a.push.apply(a,n)}return a}function o(t){for(var e=1;e<arguments.length;e++){var a=null!=arguments[e]?arguments[e]:{};e%2?i(Object(a),!0).forEach((function(e){r(t,e,a[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(a)):i(Object(a)).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(a,e))}))}return t}function l(t,e){if(null==t)return{};var a,n,r=function(t,e){if(null==t)return{};var a,n,r={},i=Object.keys(t);for(n=0;n<i.length;n++)a=i[n],e.indexOf(a)>=0||(r[a]=t[a]);return r}(t,e);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(t);for(n=0;n<i.length;n++)a=i[n],e.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(t,a)&&(r[a]=t[a])}return r}var s=n.createContext({}),p=function(t){var e=n.useContext(s),a=e;return t&&(a="function"==typeof t?t(e):o(o({},e),t)),a},m=function(t){var e=p(t.components);return n.createElement(s.Provider,{value:e},t.children)},u="mdxType",d={inlineCode:"code",wrapper:function(t){var e=t.children;return n.createElement(n.Fragment,{},e)}},c=n.forwardRef((function(t,e){var a=t.components,r=t.mdxType,i=t.originalType,s=t.parentName,m=l(t,["components","mdxType","originalType","parentName"]),u=p(a),c=r,k=u["".concat(s,".").concat(c)]||u[c]||d[c]||i;return a?n.createElement(k,o(o({ref:e},m),{},{components:a})):n.createElement(k,o({ref:e},m))}));function k(t,e){var a=arguments,r=e&&e.mdxType;if("string"==typeof t||r){var i=a.length,o=new Array(i);o[0]=c;var l={};for(var s in e)hasOwnProperty.call(e,s)&&(l[s]=e[s]);l.originalType=t,l[u]="string"==typeof t?t:r,o[1]=l;for(var p=2;p<i;p++)o[p]=a[p];return n.createElement.apply(null,o)}return n.createElement.apply(null,a)}c.displayName="MDXCreateElement"},40568:(t,e,a)=>{a.r(e),a.d(e,{assets:()=>s,contentTitle:()=>o,default:()=>d,frontMatter:()=>i,metadata:()=>l,toc:()=>p});var n=a(87462),r=(a(67294),a(3905));const i={sidebar_position:40,sidebar_label:"Robotic Arm"},o="Robotic Arm",l={unversionedId:"robotic_arm/robotic_arm",id:"robotic_arm/robotic_arm",title:"Robotic Arm",description:"Overview",source:"@site/docs_tutorials/robotic_arm/robotic_arm.md",sourceDirName:"robotic_arm",slug:"/robotic_arm/",permalink:"/docs_tutorials/robotic_arm/",draft:!1,tags:[],version:"current",sidebarPosition:40,frontMatter:{sidebar_position:40,sidebar_label:"Robotic Arm"},sidebar:"tutorialSidebar",previous:{title:"Aerosandbox",permalink:"/docs_tutorials/aerosandbox/"},next:{title:"TurtleBot",permalink:"/docs_tutorials/turtlebot/"}},s={},p=[{value:"Overview",id:"overview",level:2},{value:"Prerequisites",id:"prerequisites",level:2},{value:"Table of Contents",id:"table-of-contents",level:2},{value:"Installation",id:"installation",level:2},{value:"Workspace Overview",id:"workspace-overview",level:2},{value:"CITROS Initialization",id:"citros-initialization",level:2},{value:"Scenario",id:"scenario",level:2},{value:"Running the Scenario Using CITROS",id:"running-the-scenario-using-citros",level:2},{value:"Results",id:"results",level:2}],m={toc:p},u="wrapper";function d(t){let{components:e,...i}=t;return(0,r.kt)(u,(0,n.Z)({},m,i,{components:e,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"robotic-arm"},"Robotic Arm"),(0,r.kt)("h2",{id:"overview"},"Overview"),(0,r.kt)("p",null,"This project is designed to wrap the ",(0,r.kt)("a",{parentName:"p",href:"https://github.com/dvalenciar/robotic_arm_environment"},"Robotic Arm Simulation project")," and integrate it with CITROS platform. The node provides ROS 2 parameters that allow users to adjust target arm joints position. In addition, the Inverse Kinematic ROS 2 node was added."),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"png",src:a(85866).Z,title:"Arm",width:"571",height:"425"})),(0,r.kt)("h2",{id:"prerequisites"},"Prerequisites"),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},"Please make sure you have all the ",(0,r.kt)("a",{parentName:"li",href:"../../docs/guides/getting_started#prerequisites-for-working-with-citros"},"necessary softwares")," to work with CITROS installed on your computer."),(0,r.kt)("li",{parentName:"ol"},"Install ",(0,r.kt)("a",{parentName:"li",href:"https://code.visualstudio.com/download"},"Visual Studio code"),"."),(0,r.kt)("li",{parentName:"ol"},"We strongly recommend that you work with ",(0,r.kt)("a",{parentName:"li",href:"../../docs/guides/dockerfile_overview"},"dockers"),". However, if you wish to work without dockers, please refer to the .devcontainer ",(0,r.kt)("a",{parentName:"li",href:"https://github.com/citros-garden/aerosandbox_cessna/tree/main/.devcontainer"},"directory")," in project's repo, the dependencies you need are in the ",(0,r.kt)("inlineCode",{parentName:"li"},"Dockerfile")," file."),(0,r.kt)("li",{parentName:"ol"},"(Optional) Install ",(0,r.kt)("a",{parentName:"li",href:"https://docs.Foxglove.dev/docs/introduction"},"Foxglove"),".")),(0,r.kt)("h2",{id:"table-of-contents"},"Table of Contents"),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"#installation"},"Installation")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"#workspace-overview"},"Workspace Overview")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"#citros-initialization"},"CITROS Initialization")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"#scenario"},"Scenario")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"#running-the-scenario-using-citros"},"Running the Scenario Using CITROS")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"#results"},"Results"))),(0,r.kt)("h2",{id:"installation"},"Installation"),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},"Clone the repository:")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-bash"},"git clone git@github.com:citros-garden/robotic_arm.git\n")),(0,r.kt)("ol",{start:2},(0,r.kt)("li",{parentName:"ol"},"Open the repository in the ",(0,r.kt)("a",{parentName:"li",href:"../../docs/guides/citros_garden#run-project-in-vscode"},"VScode Dev Container"),".")),(0,r.kt)("h2",{id:"workspace-overview"},"Workspace Overview"),(0,r.kt)("p",null,"The Robotic Arm simulation has the following ROS 2 parameters:"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},"Forward Kinematic simulation parameters:"),(0,r.kt)("table",{parentName:"li"},(0,r.kt)("thead",{parentName:"table"},(0,r.kt)("tr",{parentName:"thead"},(0,r.kt)("th",{parentName:"tr",align:null},"Parameter"),(0,r.kt)("th",{parentName:"tr",align:null},"Description"),(0,r.kt)("th",{parentName:"tr",align:null},"Package"))),(0,r.kt)("tbody",{parentName:"table"},(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"j0"),(0,r.kt)("td",{parentName:"tr",align:null},"First joint target position"),(0,r.kt)("td",{parentName:"tr",align:null},"my_doosan_pkg")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"j1"),(0,r.kt)("td",{parentName:"tr",align:null},"Second joint target position"),(0,r.kt)("td",{parentName:"tr",align:null},"my_doosan_pkg")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"j2"),(0,r.kt)("td",{parentName:"tr",align:null},"Third joint target position"),(0,r.kt)("td",{parentName:"tr",align:null},"my_doosan_pkg")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"j3"),(0,r.kt)("td",{parentName:"tr",align:null},"Fourth joint target position"),(0,r.kt)("td",{parentName:"tr",align:null},"my_doosan_pkg")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"j4"),(0,r.kt)("td",{parentName:"tr",align:null},"Fifth joint target position"),(0,r.kt)("td",{parentName:"tr",align:null},"my_doosan_pkg")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"j5"),(0,r.kt)("td",{parentName:"tr",align:null},"Sixth joint target position"),(0,r.kt)("td",{parentName:"tr",align:null},"my_doosan_pkg"))))),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},"Inverse Kinematic simulation parameters:"),(0,r.kt)("table",{parentName:"li"},(0,r.kt)("thead",{parentName:"table"},(0,r.kt)("tr",{parentName:"thead"},(0,r.kt)("th",{parentName:"tr",align:null},"Parameter"),(0,r.kt)("th",{parentName:"tr",align:null},"Description"),(0,r.kt)("th",{parentName:"tr",align:null},"Package"))),(0,r.kt)("tbody",{parentName:"table"},(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"pos0"),(0,r.kt)("td",{parentName:"tr",align:null},"Arm target position by first axis"),(0,r.kt)("td",{parentName:"tr",align:null},"inverse_kinematic_pkg")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"pos1"),(0,r.kt)("td",{parentName:"tr",align:null},"Arm target position by second axis"),(0,r.kt)("td",{parentName:"tr",align:null},"inverse_kinematic_pkg")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"pos2"),(0,r.kt)("td",{parentName:"tr",align:null},"Arm target position by third axis"),(0,r.kt)("td",{parentName:"tr",align:null},"inverse_kinematic_pkg")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"ori0"),(0,r.kt)("td",{parentName:"tr",align:null},"Arm target orientation by first axis"),(0,r.kt)("td",{parentName:"tr",align:null},"inverse_kinematic_pkg")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"ori1"),(0,r.kt)("td",{parentName:"tr",align:null},"Arm target orientation by second axis"),(0,r.kt)("td",{parentName:"tr",align:null},"inverse_kinematic_pkg")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"ori3"),(0,r.kt)("td",{parentName:"tr",align:null},"Arm target orientation by third axis"),(0,r.kt)("td",{parentName:"tr",align:null},"inverse_kinematic_pkg")))))),(0,r.kt)("p",null,"This project contains two launch files: "),(0,r.kt)("table",null,(0,r.kt)("thead",{parentName:"table"},(0,r.kt)("tr",{parentName:"thead"},(0,r.kt)("th",{parentName:"tr",align:null},"Launch File"),(0,r.kt)("th",{parentName:"tr",align:null},"Description"),(0,r.kt)("th",{parentName:"tr",align:null},"Package"))),(0,r.kt)("tbody",{parentName:"table"},(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"my_doosan_gazebo_controller.launch.py"),(0,r.kt)("td",{parentName:"tr",align:null},"Gazebo Robotic Arm launch file for Forward Kinematic"),(0,r.kt)("td",{parentName:"tr",align:null},"my_doosan_pkg")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"simulation_inverse_kinematic_pkg.launch.py"),(0,r.kt)("td",{parentName:"tr",align:null},"Gazebo Robotic Arm launch file for Inverse Kinematic"),(0,r.kt)("td",{parentName:"tr",align:null},"inverse_kinematic_pkg")))),(0,r.kt)("h2",{id:"citros-initialization"},"CITROS Initialization"),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"https://citros.io/doc/docs_tutorials/getting_started/#installation"},"Install CITROS"),"."),(0,r.kt)("li",{parentName:"ol"},"Follow ",(0,r.kt)("a",{parentName:"li",href:"https://citros.io/doc/docs_tutorials/getting_started/#initialization"},"these steps")," to Initialize CITROS.")),(0,r.kt)("p",null,"Now you can see .citros directory in the explorer."),(0,r.kt)("h2",{id:"scenario"},"Scenario"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},"Inverse kinematics ",(0,r.kt)("br",null),"\nThe Inverse Kinematic calculations are used to show more useful way to interact with robotic arm.  ",(0,r.kt)("br",null),"\nUser provides target position and target rotation of arm by three axes as input parameters to configure the simulation. The robotic arm will change its position trying to meet the target conditions. ")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},"Forward kinematics ",(0,r.kt)("br",null),"\nForward Kinematic calculation is the simplest way to control the robotic arm behavior. ",(0,r.kt)("br",null),"\nUser provides joints target positions as input parameters to configure the simulation. The robotic arm will change its position trying to meet the target conditions, and the simulation publishes the current positions of joints as a result.",(0,r.kt)("br",null)),(0,r.kt)("p",{parentName:"li"},"  In this tutorial, let's check how the robotic arm's behavior changes depending on target position. ",(0,r.kt)("br",null),"\nFor that, we will launch a batch simulation with a random distribution ranging between 0.0 and 0.5, for the last joint position parameter  (",(0,r.kt)("inlineCode",{parentName:"p"},"j5"),").\nThe parameter will be set by a NumPy random function and its  setup is listed in ",(0,r.kt)("inlineCode",{parentName:"p"},".citros/parameter_setups/default_param_setup.json"),": ",(0,r.kt)("br",null)))),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-json"},'{\n    "packages": {\n        "my_doosan_pkg": {\n            "trajectory_points_act_server": {\n                "ros__parameters": {\n                    "j0": -0.8,\n                    "j1": 0.2,\n                    "j2": 0.75,\n                    "j3": -0.102,\n                    "j4": 1.57,\n                    "j5": {\n                        "function": "numpy.random.uniform",\n                        "args": [0.0, 0.5]\n                    }\n                }\n            }\n        }\n    }\n}\n')),(0,r.kt)("p",null,"Learn more about parameter setup and defining custom functions in ",(0,r.kt)("a",{parentName:"p",href:"../../docs/advanced_guides/citros_structure#directory-simulations"},"Directory parameter_setups")," and ",(0,r.kt)("a",{parentName:"p",href:"../../docs/guides/config_params"},"Adding Functions to Parameter Setup")," pages."),(0,r.kt)("p",null,"In addition to parameter setup, you can configure the simulation performance setup (timeout, CPU, GPU and Memory) as well.\nThese parameters can be found in ",(0,r.kt)("inlineCode",{parentName:"p"},".citros/simulations/simulation_my_doosan_gazebo_controller.json")," for Forward Kinematic or ",(0,r.kt)("inlineCode",{parentName:"p"},".citros/simulations/simulation_inverse_kinematic_pkg.json")," for Inverse Kinematic. ",(0,r.kt)("br",null),"\nLook in ",(0,r.kt)("a",{parentName:"p",href:"../../docs/advanced_guides/citros_structure#directory-simulations"},"Directory simulations page")," for more information."),(0,r.kt)("h2",{id:"running-the-scenario-using-citros"},"Running the Scenario Using CITROS"),(0,r.kt)("p",null,"Follow these steps to ",(0,r.kt)("a",{parentName:"p",href:"../../docs/guides/getting_started#run-simulation"},"Run Simulation"),":"),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},"Name your  batch run simulation: ",(0,r.kt)("inlineCode",{parentName:"li"},"robotic_arm")),(0,r.kt)("li",{parentName:"ol"},"Add a message to your batch run simulation: ",(0,r.kt)("inlineCode",{parentName:"li"},"local test run")),(0,r.kt)("li",{parentName:"ol"},"Run your simulation ",(0,r.kt)("strong",{parentName:"li"}," 5 times "),".")),(0,r.kt)("p",null,"All the results will be saved under ",(0,r.kt)("inlineCode",{parentName:"p"},".citros/data/simulation_robotic_arm_cessna")," folder."),(0,r.kt)("p",null,"To plot the local run results you can use ",(0,r.kt)("a",{parentName:"p",href:"../../docs/guides/foxglove_visual"},"Foxglove")," with the layout file existing in ",(0,r.kt)("inlineCode",{parentName:"p"},"foxglove_layout")," folder."),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"gif",src:a(75728).Z,title:"Foxglove example",width:"1555",height:"1001"})),(0,r.kt)("h2",{id:"results"},"Results"),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"../../docs/guides/getting_started#create-db"},"Create Database")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"../../docs/guides/getting_started#load-data-to-db"},"Upload data to the database")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"../../docs/guides/getting_started#verify-data-loaded"},"Verify the data was loaded")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"../../docs/guides/getting_started#execute-notebook"},"Execute the Notebook")," ",(0,r.kt)("inlineCode",{parentName:"li"},"robotic_arm_notebook_example.ipynb"),". ",(0,r.kt)("br",null),"\nYou will find the notebook under ",(0,r.kt)("inlineCode",{parentName:"li"},"citros_template/notebooks")," folder.")),(0,r.kt)("p",null,"You can see the different behavior of the last joint on these plots:"),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"png",src:a(7973).Z,title:"CITROS example",width:"1318",height:"877"})))}d.isMDXComponent=!0},85866:(t,e,a)=>{a.d(e,{Z:()=>n});const n=a.p+"assets/images/arm0-1882d383bdfa7e93b5fbe21a49d955f7.png"},7973:(t,e,a)=>{a.d(e,{Z:()=>n});const n=a.p+"assets/images/citros3-440017ff74560c8ca054e1e7aa11acb4.png"},75728:(t,e,a)=>{a.d(e,{Z:()=>n});const n=a.p+"assets/images/foxglove1-5af0da8dae23731e99f43cd727c722f6.gif"}}]);
"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[6996],{3905:(e,t,a)=>{a.d(t,{Zo:()=>p,kt:()=>k});var n=a(67294);function r(e,t,a){return t in e?Object.defineProperty(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}function i(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,n)}return a}function o(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?i(Object(a),!0).forEach((function(t){r(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):i(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}function l(e,t){if(null==e)return{};var a,n,r=function(e,t){if(null==e)return{};var a,n,r={},i=Object.keys(e);for(n=0;n<i.length;n++)a=i[n],t.indexOf(a)>=0||(r[a]=e[a]);return r}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(n=0;n<i.length;n++)a=i[n],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(r[a]=e[a])}return r}var s=n.createContext({}),d=function(e){var t=n.useContext(s),a=t;return e&&(a="function"==typeof e?e(t):o(o({},t),e)),a},p=function(e){var t=d(e.components);return n.createElement(s.Provider,{value:t},e.children)},u="mdxType",c={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},m=n.forwardRef((function(e,t){var a=e.components,r=e.mdxType,i=e.originalType,s=e.parentName,p=l(e,["components","mdxType","originalType","parentName"]),u=d(a),m=r,k=u["".concat(s,".").concat(m)]||u[m]||c[m]||i;return a?n.createElement(k,o(o({ref:t},p),{},{components:a})):n.createElement(k,o({ref:t},p))}));function k(e,t){var a=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var i=a.length,o=new Array(i);o[0]=m;var l={};for(var s in t)hasOwnProperty.call(t,s)&&(l[s]=t[s]);l.originalType=e,l[u]="string"==typeof e?e:r,o[1]=l;for(var d=2;d<i;d++)o[d]=a[d];return n.createElement.apply(null,o)}return n.createElement.apply(null,a)}m.displayName="MDXCreateElement"},78342:(e,t,a)=>{a.r(t),a.d(t,{assets:()=>s,contentTitle:()=>o,default:()=>c,frontMatter:()=>i,metadata:()=>l,toc:()=>d});var n=a(87462),r=(a(67294),a(3905));const i={sidebar_position:40,sidebar_label:"Aerosandbox"},o="Aerosandbox",l={unversionedId:"aerosandbox/aerosandbox",id:"aerosandbox/aerosandbox",title:"Aerosandbox",description:"Overview",source:"@site/docs_tutorials/aerosandbox/aerosandbox.md",sourceDirName:"aerosandbox",slug:"/aerosandbox/",permalink:"/docs_tutorials/aerosandbox/",draft:!1,tags:[],version:"current",sidebarPosition:40,frontMatter:{sidebar_position:40,sidebar_label:"Aerosandbox"},sidebar:"tutorialSidebar",previous:{title:"Galactic Orbits",permalink:"/docs_tutorials/gal_orbits/"},next:{title:"Robotic Arm",permalink:"/docs_tutorials/robotic_arm/"}},s={},d=[{value:"Overview",id:"overview",level:2},{value:"Prerequisites",id:"prerequisites",level:2},{value:"Table of Contents",id:"table-of-contents",level:2},{value:"Installation",id:"installation",level:2},{value:"Workspace Overview",id:"workspace-overview",level:2},{value:"CITROS Initialization",id:"citros-initialization",level:2},{value:"Scenario",id:"scenario",level:2},{value:"Running the Scenario Using CITROS",id:"running-the-scenario-using-citros",level:2},{value:"Results",id:"results",level:2}],p={toc:d},u="wrapper";function c(e){let{components:t,...i}=e;return(0,r.kt)(u,(0,n.Z)({},p,i,{components:t,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"aerosandbox"},"Aerosandbox"),(0,r.kt)("h2",{id:"overview"},"Overview"),(0,r.kt)("p",null,"The project is a simulation tool developed using ROS 2 (Robot Operating System) nodes and leverages the Aerosandbox Python library for aerodynamic calculations. Its primary objective is to simulate gliding flight scenarios for a Cessna 152 aircraft in the event of engine failure."),(0,r.kt)("p",null,"You can find more information about this useful aerodynamics library on ",(0,r.kt)("a",{parentName:"p",href:"https://github.com/peterdsharpe/AeroSandbox"},"Aerosandbox official website"),". All project installation, code overview and usage details are also available on the project's ",(0,r.kt)("a",{parentName:"p",href:"https://github.com/citros-garden/aerosandbox_cessna"},"GitHub page"),"."),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"jpg",src:a(28100).Z,title:"https://en.wikipedia.org/wiki/File:Cessna_152_PR-EJQ_(8476096843).jpg",width:"800",height:"533"})),(0,r.kt)("h2",{id:"prerequisites"},"Prerequisites"),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},"Please make sure you have all the ",(0,r.kt)("a",{parentName:"li",href:"../../docs/guides/getting_started#prerequisites-for-working-with-citros"},"necessary softwares")," to work with CITROS installed on your computer."),(0,r.kt)("li",{parentName:"ol"},"Install ",(0,r.kt)("a",{parentName:"li",href:"https://code.visualstudio.com/download"},"Visual Studio code"),"."),(0,r.kt)("li",{parentName:"ol"},"We strongly recommend that you work with ",(0,r.kt)("a",{parentName:"li",href:"../../docs/guides/dockerfile_overview"},"dockers"),". However, if you wish to work without dockers, please refer to the .devcontainer ",(0,r.kt)("a",{parentName:"li",href:"https://github.com/citros-garden/aerosandbox_cessna/tree/main/.devcontainer"},"directory")," in project's repo, the dependencies you need are in the ",(0,r.kt)("inlineCode",{parentName:"li"},"Dockerfile")," file."),(0,r.kt)("li",{parentName:"ol"},"(Optional) Install ",(0,r.kt)("a",{parentName:"li",href:"https://docs.Foxglove.dev/docs/introduction"},"Foxglove"),".")),(0,r.kt)("h2",{id:"table-of-contents"},"Table of Contents"),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"#installation"},"Installation")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"#workspace-overview"},"Workspace Overview")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"#citros-initialization"},"CITROS Initialization")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"#scenario"},"Scenario")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"#running-the-scenario-using-citros"},"Running the Scenario Using CITROS")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"#results"},"Results"))),(0,r.kt)("h2",{id:"installation"},"Installation"),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},"Clone the repository:")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-bash"},"git clone git@github.com:citros-garden/aerosandbox_cessna.git\n")),(0,r.kt)("ol",{start:2},(0,r.kt)("li",{parentName:"ol"},"Open the repository in the ",(0,r.kt)("a",{parentName:"li",href:"../../docs/guides/getting_started#open-project-in-vscode-dev-container"},"VScode Dev Container"),".")),(0,r.kt)("h2",{id:"workspace-overview"},"Workspace Overview"),(0,r.kt)("p",null,"The Aerosandbox simulation has the following ROS 2 parameters:"),(0,r.kt)("table",null,(0,r.kt)("thead",{parentName:"table"},(0,r.kt)("tr",{parentName:"thead"},(0,r.kt)("th",{parentName:"tr",align:null},"Parameter"),(0,r.kt)("th",{parentName:"tr",align:null},"Description"),(0,r.kt)("th",{parentName:"tr",align:null},"Package"))),(0,r.kt)("tbody",{parentName:"table"},(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"h_0"),(0,r.kt)("td",{parentName:"tr",align:null},"Initial altitude (m)"),(0,r.kt)("td",{parentName:"tr",align:null},"aerosandbox_cessna")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"v_0"),(0,r.kt)("td",{parentName:"tr",align:null},"Initial velocity (knots)"),(0,r.kt)("td",{parentName:"tr",align:null},"aerosandbox_cessna")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"publish_freq"),(0,r.kt)("td",{parentName:"tr",align:null},"Frequency of publishing"),(0,r.kt)("td",{parentName:"tr",align:null},"aerosandbox_cessna")))),(0,r.kt)("p",null,"This project contains only one launch file ",(0,r.kt)("inlineCode",{parentName:"p"},"aerosandbox_cessna.launch.py"),". This file will be used for CITROS launch. "),(0,r.kt)("table",null,(0,r.kt)("thead",{parentName:"table"},(0,r.kt)("tr",{parentName:"thead"},(0,r.kt)("th",{parentName:"tr",align:null},"Launch File"),(0,r.kt)("th",{parentName:"tr",align:null},"Description"),(0,r.kt)("th",{parentName:"tr",align:null},"Package"))),(0,r.kt)("tbody",{parentName:"table"},(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"aerosandbox_cessna.launch.py"),(0,r.kt)("td",{parentName:"tr",align:null},"Aerosandbox simulation launch file"),(0,r.kt)("td",{parentName:"tr",align:null},"aerosandbox_cessna")))),(0,r.kt)("h2",{id:"citros-initialization"},"CITROS Initialization"),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"../../docs/guides/getting_started#installation"},"Install CITROS"),"."),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"../../docs/guides/getting_started#initialization"},"Initialize CITROS"),".")),(0,r.kt)("h2",{id:"scenario"},"Scenario"),(0,r.kt)("p",null,"For this tutorial, let's check how far the Cessna can glide with engine failure depending on initial altitude. To find it out, we need to set up parameters and launch CITROS simulation. ",(0,r.kt)("br",null),"\nThe user provides flight parameters as input parameters to configure the simulation. These parameters are essential for defining the initial conditions of the simulated flight.",(0,r.kt)("br",null),"\nThe simulation takes into account various flight dynamics and aerodynamic factors to model the gliding behavior of the Cessna 152. The maximum gliding distance depends on plane's aerodynamic parameters, initial altitude and initial velocity.",(0,r.kt)("br",null),"\nWe will be using ",(0,r.kt)("a",{parentName:"p",href:"https://en.wikipedia.org/wiki/IPOPT#:~:text=IPOPT%2C%20short%20for%20%22Interior%20Point,the%20EPL%20(formerly%20CPL)."},"iPOPT")," - optimal under the hood problem solver (iPOPT is also installed as part of the AeroSandbox package).",(0,r.kt)("br",null),"\nThe parameter setup is listed in ",(0,r.kt)("inlineCode",{parentName:"p"},".citros/parameter_setups/default_param_setup.json"),". ",(0,r.kt)("br",null),"\nTo find out how far the Cessna can glide with engine failure, we will examine the initial altitude, starting from 1000m and up to 10000m."),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-json"},'{\n    "packages": {\n        "aerosandbox_cessna": {\n            "aerosandbox_cessna": {\n                "ros__parameters": {\n                    "h_0": {\n                        "function": "my_func.py:func_with_context",\n                        "args": [1000.0]\n                    },\n                    "v_0": 107.0,\n                    "publish_freq": 10.0\n                }\n            }\n        }\n    }\n}\n')),(0,r.kt)("p",null,"The ",(0,r.kt)("inlineCode",{parentName:"p"},"my_func.py")," file should contain:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"def func_with_context(num, citros_context):\n    return num + float(citros_context['run_id'])*1000\n")),(0,r.kt)("p",null,"This function will set the ",(0,r.kt)("inlineCode",{parentName:"p"},"h_0")," parameter in range from 1000 to 1000+1000*n, where n = number of runs."),(0,r.kt)("p",null,"Learn more about parameter setup and defining custom functions in ",(0,r.kt)("a",{parentName:"p",href:"../../docs/advanced_guides/citros_structure#directory-simulations"},"Directory parameter_setups")," and ",(0,r.kt)("a",{parentName:"p",href:"../../docs/guides/config_params"},"Adding Functions to Parameter Setup")," pages."),(0,r.kt)("p",null,"In addition to parameter setup, you can configure the simulation performance setup (timeout, CPU, GPU and Memory) as well.\nThis parameters can be found in ",(0,r.kt)("inlineCode",{parentName:"p"},".citros/simulations/simulation_aerosandbox_cessna.json"),". ",(0,r.kt)("br",null),"\nThe default setup is 180 seconds timeout, 4 CPU, 4 GPU and 4096 MB of Memory."),(0,r.kt)("p",null,"Look in ",(0,r.kt)("a",{parentName:"p",href:"../../docs/advanced_guides/citros_structure#directory-simulations"},"Directory simulations page")," for more information."),(0,r.kt)("h2",{id:"running-the-scenario-using-citros"},"Running the Scenario Using CITROS"),(0,r.kt)("p",null,"Follow these steps to ",(0,r.kt)("a",{parentName:"p",href:"../../docs/guides/getting_started#run-simulation"},"Run Simulation"),":"),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},"Name your  batch run simulation: ",(0,r.kt)("inlineCode",{parentName:"li"},"aerosandbox_cessna")),(0,r.kt)("li",{parentName:"ol"},"Add a message to your batch run simulation: ",(0,r.kt)("inlineCode",{parentName:"li"},"local test run")),(0,r.kt)("li",{parentName:"ol"},"Run your simulation ",(0,r.kt)("strong",{parentName:"li"}," 5 times "),".")),(0,r.kt)("p",null,"All the results will be saved under ",(0,r.kt)("inlineCode",{parentName:"p"},".citros/data/simulation_aerosandbox_cessna")," folder."),(0,r.kt)("p",null,"To plot the local run results you can use ",(0,r.kt)("a",{parentName:"p",href:"../../docs/guides/foxglove_visual"},"Foxglove")," with the layout file existing in ",(0,r.kt)("inlineCode",{parentName:"p"},"foxglove_layout")," folder."),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"gif",src:a(61193).Z,title:"Foxglove example",width:"1553",height:"1001"})),(0,r.kt)("h2",{id:"results"},"Results"),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"../../docs/guides/getting_started#create-db"},"Create Database")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"../../docs/guides/getting_started#load-data-to-db"},"Upload data to the database")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"../../docs/guides/getting_started#verify-data-loaded"},"Verify the data was loaded")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"../../docs/guides/getting_started#execute-notebook"},"Execute the Notebook")," ",(0,r.kt)("inlineCode",{parentName:"li"},"aerosandbox_notebook_example.ipynb"),". ",(0,r.kt)("br",null),"\nYou will find the notebook under ",(0,r.kt)("inlineCode",{parentName:"li"},"citros_template/notebooks")," folder.")),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"png",src:a(7816).Z,title:"CITROS example",width:"597",height:"453"})))}c.isMDXComponent=!0},28100:(e,t,a)=>{a.d(t,{Z:()=>n});const n=a.p+"assets/images/cessna152-81db7e1381c262c422f54372e3657d4c.jpg"},7816:(e,t,a)=>{a.d(t,{Z:()=>n});const n=a.p+"assets/images/citros3-ccdafcb9d38633f78d4fe9529ed08a7e.png"},61193:(e,t,a)=>{a.d(t,{Z:()=>n});const n=a.p+"assets/images/gif0-564f74b19b470f267d1c7b1ce8dd2278.gif"}}]);
"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[40243],{3905:(t,e,a)=>{a.d(e,{Zo:()=>m,kt:()=>c});var n=a(67294);function r(t,e,a){return e in t?Object.defineProperty(t,e,{value:a,enumerable:!0,configurable:!0,writable:!0}):t[e]=a,t}function i(t,e){var a=Object.keys(t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(t);e&&(n=n.filter((function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable}))),a.push.apply(a,n)}return a}function l(t){for(var e=1;e<arguments.length;e++){var a=null!=arguments[e]?arguments[e]:{};e%2?i(Object(a),!0).forEach((function(e){r(t,e,a[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(a)):i(Object(a)).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(a,e))}))}return t}function o(t,e){if(null==t)return{};var a,n,r=function(t,e){if(null==t)return{};var a,n,r={},i=Object.keys(t);for(n=0;n<i.length;n++)a=i[n],e.indexOf(a)>=0||(r[a]=t[a]);return r}(t,e);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(t);for(n=0;n<i.length;n++)a=i[n],e.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(t,a)&&(r[a]=t[a])}return r}var s=n.createContext({}),p=function(t){var e=n.useContext(s),a=e;return t&&(a="function"==typeof t?t(e):l(l({},e),t)),a},m=function(t){var e=p(t.components);return n.createElement(s.Provider,{value:e},t.children)},u="mdxType",d={inlineCode:"code",wrapper:function(t){var e=t.children;return n.createElement(n.Fragment,{},e)}},k=n.forwardRef((function(t,e){var a=t.components,r=t.mdxType,i=t.originalType,s=t.parentName,m=o(t,["components","mdxType","originalType","parentName"]),u=p(a),k=r,c=u["".concat(s,".").concat(k)]||u[k]||d[k]||i;return a?n.createElement(c,l(l({ref:e},m),{},{components:a})):n.createElement(c,l({ref:e},m))}));function c(t,e){var a=arguments,r=e&&e.mdxType;if("string"==typeof t||r){var i=a.length,l=new Array(i);l[0]=k;var o={};for(var s in e)hasOwnProperty.call(e,s)&&(o[s]=e[s]);o.originalType=t,o[u]="string"==typeof t?t:r,l[1]=o;for(var p=2;p<i;p++)l[p]=a[p];return n.createElement.apply(null,l)}return n.createElement.apply(null,a)}k.displayName="MDXCreateElement"},56153:(t,e,a)=>{a.r(e),a.d(e,{assets:()=>s,contentTitle:()=>l,default:()=>d,frontMatter:()=>i,metadata:()=>o,toc:()=>p});var n=a(87462),r=(a(67294),a(3905));const i={sidebar_position:80,sidebar_label:"Poliastro"},l="Poliastro",o={unversionedId:"poliastro/poliastro",id:"poliastro/poliastro",title:"Poliastro",description:"Overview",source:"@site/docs_tutorials/poliastro/poliastro.md",sourceDirName:"poliastro",slug:"/poliastro/",permalink:"/docs_tutorials/poliastro/",draft:!1,tags:[],version:"current",sidebarPosition:80,frontMatter:{sidebar_position:80,sidebar_label:"Poliastro"},sidebar:"tutorialSidebar",previous:{title:"Pendulum",permalink:"/docs_tutorials/pendulum/"},next:{title:"Robotic Arm",permalink:"/docs_tutorials/robotic_arm/"}},s={},p=[{value:"Overview",id:"overview",level:2},{value:"Prerequisites",id:"prerequisites",level:2},{value:"Table of Contents",id:"table-of-contents",level:2},{value:"Installation",id:"installation",level:2},{value:"Workspace Overview",id:"workspace-overview",level:2},{value:"CITROS Initialization",id:"citros-initialization",level:2},{value:"Scenario",id:"scenario",level:2},{value:"Running the Scenario Using CITROS",id:"running-the-scenario-using-citros",level:2},{value:"Simple Orbit Simulation",id:"simple-orbit-simulation",level:4},{value:"Atmo Drag Simulation",id:"atmo-drag-simulation",level:4},{value:"Results",id:"results",level:2}],m={toc:p},u="wrapper";function d(t){let{components:e,...i}=t;return(0,r.kt)(u,(0,n.Z)({},m,i,{components:e,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"poliastro"},"Poliastro"),(0,r.kt)("h2",{id:"overview"},"Overview"),(0,r.kt)("p",null,"This project contains three simple examples using Poliastro lib for Python3: "),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},"Simple orbit example"),(0,r.kt)("li",{parentName:"ol"},"Orbital maneuver example "),(0,r.kt)("li",{parentName:"ol"},"Atmospheric drag simulation.  ")),(0,r.kt)("p",null,"You can find all the information about the used functions and the mathematical explanation on the ",(0,r.kt)("a",{parentName:"p",href:"https://docs.poliastro.space/en/stable/"},"Poliastro Website"),". ",(0,r.kt)("br",null),"\nAll project installation, code overview and usage details are also available on the project's ",(0,r.kt)("a",{parentName:"p",href:"https://github.com/citros-garden/poliastro"},"GitHub page"),"."),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"jpg",src:a(52182).Z,width:"1920",height:"1440"})),(0,r.kt)("h2",{id:"prerequisites"},"Prerequisites"),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},"Please make sure you have all the ",(0,r.kt)("a",{parentName:"li",href:"../../docs/guides/getting_started#prerequisites-for-working-with-citros"},"necessary softwares")," to work with CITROS installed on your computer."),(0,r.kt)("li",{parentName:"ol"},"Install ",(0,r.kt)("a",{parentName:"li",href:"https://code.visualstudio.com/download"},"Visual Studio code"),"."),(0,r.kt)("li",{parentName:"ol"},"We strongly recommend that you work with ",(0,r.kt)("a",{parentName:"li",href:"../../docs/guides/dockerfile_overview"},"dockers"),". However, if you wish to work without dockers, please refer to the .devcontainer ",(0,r.kt)("a",{parentName:"li",href:"https://github.com/citros-garden/aerosandbox_cessna/tree/main/.devcontainer"},"directory")," in project's repo, the dependencies you need are in the ",(0,r.kt)("inlineCode",{parentName:"li"},"Dockerfile")," file."),(0,r.kt)("li",{parentName:"ol"},"(Optional) Install ",(0,r.kt)("a",{parentName:"li",href:"https://docs.Foxglove.dev/docs/introduction"},"Foxglove"),".")),(0,r.kt)("h2",{id:"table-of-contents"},"Table of Contents"),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"#installation"},"Installation")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"#workspace-overview"},"Workspace Overview")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"#citros-initialization"},"CITROS Initialization")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"#scenario"},"Scenario")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"#running-the-scenario-using-citros"},"Running the Scenario Using CITROS")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"#results"},"Results"))),(0,r.kt)("h2",{id:"installation"},"Installation"),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("p",{parentName:"li"},"Clone the repository:"),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-bash"},"git clone git@github.com:citros-garden/poliastro.git\n"))),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("p",{parentName:"li"},"Open the repository in the ",(0,r.kt)("a",{parentName:"p",href:"../../docs/guides/citros_garden#run-project-in-vscode"},"VScode Dev Container"),".")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("p",{parentName:"li"},(0,r.kt)("a",{parentName:"p",href:"../../docs/guides/citros_garden#build-the-project"},"Build the project"),"."))),(0,r.kt)("h2",{id:"workspace-overview"},"Workspace Overview"),(0,r.kt)("p",null,"The examples have the following parameters:"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},"Poliastro Atmospheric Drag simulation parameters:"),(0,r.kt)("table",{parentName:"li"},(0,r.kt)("thead",{parentName:"table"},(0,r.kt)("tr",{parentName:"thead"},(0,r.kt)("th",{parentName:"tr",align:null},"Parameter"),(0,r.kt)("th",{parentName:"tr",align:null},"Description"),(0,r.kt)("th",{parentName:"tr",align:null},"Package"))),(0,r.kt)("tbody",{parentName:"table"},(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"earth_r"),(0,r.kt)("td",{parentName:"tr",align:null},"Earth radius"),(0,r.kt)("td",{parentName:"tr",align:null},"poliastro_atmo_drag")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"a"),(0,r.kt)("td",{parentName:"tr",align:null},"Semi-Major axis"),(0,r.kt)("td",{parentName:"tr",align:null},"poliastro_atmo_drag")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"ecc"),(0,r.kt)("td",{parentName:"tr",align:null},"Eccentricity"),(0,r.kt)("td",{parentName:"tr",align:null},"poliastro_atmo_drag")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"inc"),(0,r.kt)("td",{parentName:"tr",align:null},"Inclination"),(0,r.kt)("td",{parentName:"tr",align:null},"poliastro_atmo_drag")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"raan"),(0,r.kt)("td",{parentName:"tr",align:null},"Right Ascension of the Ascending Node"),(0,r.kt)("td",{parentName:"tr",align:null},"poliastro_atmo_drag")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"argp"),(0,r.kt)("td",{parentName:"tr",align:null},"Argument of periapsis"),(0,r.kt)("td",{parentName:"tr",align:null},"poliastro_atmo_drag")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"nu"),(0,r.kt)("td",{parentName:"tr",align:null},"True anomaly"),(0,r.kt)("td",{parentName:"tr",align:null},"poliastro_atmo_drag")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"c_d"),(0,r.kt)("td",{parentName:"tr",align:null},"Drag coefficient"),(0,r.kt)("td",{parentName:"tr",align:null},"poliastro_atmo_drag")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"t_limit"),(0,r.kt)("td",{parentName:"tr",align:null},"Maximum simulation duration"),(0,r.kt)("td",{parentName:"tr",align:null},"poliastro_atmo_drag")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"publish_freq"),(0,r.kt)("td",{parentName:"tr",align:null},"Frequency of publishing"),(0,r.kt)("td",{parentName:"tr",align:null},"poliastro_atmo_drag"))))),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},"Poliastro Simple Orbit simulation parameters:"),(0,r.kt)("table",{parentName:"li"},(0,r.kt)("thead",{parentName:"table"},(0,r.kt)("tr",{parentName:"thead"},(0,r.kt)("th",{parentName:"tr",align:null},"Parameter"),(0,r.kt)("th",{parentName:"tr",align:null},"Description"),(0,r.kt)("th",{parentName:"tr",align:null},"Package"))),(0,r.kt)("tbody",{parentName:"table"},(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"apo_r"),(0,r.kt)("td",{parentName:"tr",align:null},"Apoapsis altitude"),(0,r.kt)("td",{parentName:"tr",align:null},"poliastro_simple_orbit")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"peri_r"),(0,r.kt)("td",{parentName:"tr",align:null},"Periapsis altitude"),(0,r.kt)("td",{parentName:"tr",align:null},"poliastro_simple_orbit")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"start_t"),(0,r.kt)("td",{parentName:"tr",align:null},"Start date and time"),(0,r.kt)("td",{parentName:"tr",align:null},"poliastro_simple_orbit")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"finish_t"),(0,r.kt)("td",{parentName:"tr",align:null},"Final date and time"),(0,r.kt)("td",{parentName:"tr",align:null},"poliastro_simple_orbit")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"publish_freq"),(0,r.kt)("td",{parentName:"tr",align:null},"Frequency of publishing"),(0,r.kt)("td",{parentName:"tr",align:null},"poliastro_simple_orbit"))))),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},"Poliastro Maneuver simulation parameters:"),(0,r.kt)("table",{parentName:"li"},(0,r.kt)("thead",{parentName:"table"},(0,r.kt)("tr",{parentName:"thead"},(0,r.kt)("th",{parentName:"tr",align:null},"Parameter"),(0,r.kt)("th",{parentName:"tr",align:null},"Description"),(0,r.kt)("th",{parentName:"tr",align:null},"Package"))),(0,r.kt)("tbody",{parentName:"table"},(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"r_init"),(0,r.kt)("td",{parentName:"tr",align:null},"Initial orbital altitude"),(0,r.kt)("td",{parentName:"tr",align:null},"poliastro_maneuver")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"r_final"),(0,r.kt)("td",{parentName:"tr",align:null},"Final orbital altitude"),(0,r.kt)("td",{parentName:"tr",align:null},"poliastro_maneuver")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"publish_freq"),(0,r.kt)("td",{parentName:"tr",align:null},"Frequency of publishing"),(0,r.kt)("td",{parentName:"tr",align:null},"poliastro_maneuver")))))),(0,r.kt)("p",null,"There are three launch files in this project, these files will be used for CITROS launch:"),(0,r.kt)("table",null,(0,r.kt)("thead",{parentName:"table"},(0,r.kt)("tr",{parentName:"thead"},(0,r.kt)("th",{parentName:"tr",align:null},"Launch File"),(0,r.kt)("th",{parentName:"tr",align:null},"Description"),(0,r.kt)("th",{parentName:"tr",align:null},"Package"))),(0,r.kt)("tbody",{parentName:"table"},(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"poliastro_atmo_drag.launch.py"),(0,r.kt)("td",{parentName:"tr",align:null},"Poliastro Atmospheric Drag simulation launch file"),(0,r.kt)("td",{parentName:"tr",align:null},"poliastro_atmo_drag")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"poliastro_maneuver.launch.py"),(0,r.kt)("td",{parentName:"tr",align:null},"Poliastro Simple Orbit simulation launch file"),(0,r.kt)("td",{parentName:"tr",align:null},"poliastro_maneuver")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"poliastro_simple_orbit.launch.py"),(0,r.kt)("td",{parentName:"tr",align:null},"Poliastro Maneuver simulation launch file"),(0,r.kt)("td",{parentName:"tr",align:null},"poliastro_simple_orbit")))),(0,r.kt)("h2",{id:"citros-initialization"},"CITROS Initialization"),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"../../docs/guides/getting_started#installation"},"Install CITROS"),"."),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"../../docs/guides/getting_started#initialization"},"Initialize CITROS"),".")),(0,r.kt)("h2",{id:"scenario"},"Scenario"),(0,r.kt)("p",null,"The Poliastro project consists of three packages suitable for orbital mechanics calculations:"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"Poliastro_simple_orbit"),(0,r.kt)("br",null),"\nThis package is used to calculate vessel orbital coordinates around the Earth between time bounds from given apoapsis and periapsis altitudes. ",(0,r.kt)("br",null),"\nThe result is an ephemerids of orbit (actually a part of it between given time bounds) with zero right ascension of the ascending node, argument of the pericenter and true anomaly for simplicity. ",(0,r.kt)("br",null)),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"Poliastro_maneuver"),(0,r.kt)("br",null),"\nThis package calculates three orbits for the Hohmann transition: an initial orbit, an intermediate orbit, and a final orbit. ",(0,r.kt)("br",null),"\nThe simulation takes the radius of the initial orbit and the radius of the final orbit as input. ",(0,r.kt)("br",null),"\nThe result is the ephemerids of these orbits, not the trajectory! ",(0,r.kt)("br",null)),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"Poliastro_atmo_drag"),(0,r.kt)("br",null),"\nThis package shows the effect of aerodynamic drag forces on an artificial satellite in low Earth orbit. ",(0,r.kt)("br",null),"\nThe simulation takes Earth diameter, drag coefficient, Keppler orbit parameters and maximum simulation time as inputs. ",(0,r.kt)("br",null),"\nThe result is a plot of altitude versus time and flight time before hitting the surface.",(0,r.kt)("br",null))),(0,r.kt)("p",null,"Drag forces calculations are more difficult and more rare than the others, hence, in this tutorial we will use the Atmospheric Drag simulation scenario. ",(0,r.kt)("br",null),"\nLet's check how the exact orbit duration reduces depending on Drag coefficient. For that, we will set up Drag Coefficient (",(0,r.kt)("inlineCode",{parentName:"p"},"c_d"),") parameter random distribution in range from 2 to 4. ",(0,r.kt)("br",null),"\nThe parameter will be set by a NumPy random function and its setup is listed in\xa0",(0,r.kt)("inlineCode",{parentName:"p"},".citros/parameter_setups/default_param_setup.json"),":"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-json"},'    "packages": {\n        "poliastro_atmo_drag": {\n            "poliastro_atmo_drag": {\n                "ros__parameters": {\n                    "earth_r": 6378.1366,\n                    "a": 6550.85876692,\n                    "ecc": 0.0,\n                    "inc": 0.0,\n                    "raan": 0.0,\n                    "argp": 0.0,\n                    "nu": 0.0,\n                    "c_d": {\n                        "function": "numpy.random.uniform",\n                        "args": [2, 4]\n                    },\n                    "t_limit": 1.0,\n                    "publish_freq": 10.0\n                }\n            }\n        },\n')),(0,r.kt)("p",null,"Learn more about parameter setup and defining custom functions in ",(0,r.kt)("a",{parentName:"p",href:"../../docs/advanced_guides/citros_structure#directory-parameter_setups"},"Directory parameter_setups")," and ",(0,r.kt)("a",{parentName:"p",href:"../../docs/guides/config_params"},"Adding Functions to Parameter Setup")," pages."),(0,r.kt)("p",null,"In addition to parameter setup, you can configure the simulation performance setup (timeout, CPU, GPU and Memory) as well.\nThis parameters can be found in ",(0,r.kt)("inlineCode",{parentName:"p"},".citros/simulations/simulation_poliastro_atmo_drag.json"),". ",(0,r.kt)("br",null),"\nLook in ",(0,r.kt)("a",{parentName:"p",href:"../../docs/advanced_guides/citros_structure#directory-simulations"},"Directory simulations page")," for more information."),(0,r.kt)("h2",{id:"running-the-scenario-using-citros"},"Running the Scenario Using CITROS"),(0,r.kt)("p",null,"We will run two simulations of the three exist in the project - ",(0,r.kt)("inlineCode",{parentName:"p"},"simulation_poliastro_simple_orbit")," and ",(0,r.kt)("inlineCode",{parentName:"p"},"simulation_poliastro_atmo_drag"),"."),(0,r.kt)("p",null,"Follow these steps to ",(0,r.kt)("a",{parentName:"p",href:"../../docs/guides/getting_started#run-simulation"},"Run Simulation")),(0,r.kt)("h4",{id:"simple-orbit-simulation"},"Simple Orbit Simulation"),(0,r.kt)("p",null,"run the simulation with the following details:"),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},"Name your batch run simulation: ",(0,r.kt)("inlineCode",{parentName:"li"},"poliastro_simple_orbit")),(0,r.kt)("li",{parentName:"ol"},"Add a message to your batch run simulation: ",(0,r.kt)("inlineCode",{parentName:"li"},"simple orbit run")),(0,r.kt)("li",{parentName:"ol"},"Run your simulation ",(0,r.kt)("strong",{parentName:"li"}," 10 times "),"."),(0,r.kt)("li",{parentName:"ol"},"choose the ",(0,r.kt)("inlineCode",{parentName:"li"},"simulation_poliastro_simple_orbit")," simulation\nAll the results will be saved under ",(0,r.kt)("inlineCode",{parentName:"li"},".citros/data/simulation_poliastro_simple_orbit")," folder.",(0,r.kt)("br",null),(0,r.kt)("em",{parentName:"li"},"in this case, batch_name is poliastro_simple_orbit"))),(0,r.kt)("h4",{id:"atmo-drag-simulation"},"Atmo Drag Simulation"),(0,r.kt)("p",null,"After the above will run, go a head and run another simulation with the following details:"),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},"Name your batch run simulation: ",(0,r.kt)("inlineCode",{parentName:"li"},"poliastro_atmo_drag")),(0,r.kt)("li",{parentName:"ol"},"Add a message to your batch run simulation: ",(0,r.kt)("inlineCode",{parentName:"li"},"atmo drag run")),(0,r.kt)("li",{parentName:"ol"},"Run your simulation ",(0,r.kt)("strong",{parentName:"li"}," 10 times "),"."),(0,r.kt)("li",{parentName:"ol"},"choose the ",(0,r.kt)("inlineCode",{parentName:"li"},"simulation_poliastro_atmo_drag")," simulation\nAll the results will be saved under ",(0,r.kt)("inlineCode",{parentName:"li"},".citros/data/simulation_poliastro_atmo_drag/[batch_name]")," folder.",(0,r.kt)("br",null),(0,r.kt)("em",{parentName:"li"},"in this case, batch_name is poliastro_atmo_drag"))),(0,r.kt)("p",null,"To plot the results you can use ",(0,r.kt)("a",{parentName:"p",href:"../../docs/guides/foxglove_visual"},"Foxglove")," with the ",(0,r.kt)("inlineCode",{parentName:"p"},"atmo_drag_layout.json")," layout file existing in ",(0,r.kt)("inlineCode",{parentName:"p"},"foxglove_layout")," folder."),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"gif",src:a(42951).Z,title:"Foxglove example",width:"2854",height:"1862"})),(0,r.kt)("h2",{id:"results"},"Results"),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"../../docs/guides/getting_started#create-db"},"Create Database")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"../../docs/guides/getting_started#load-data-to-db"},"Upload data to the database")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"../../docs/guides/getting_started#verify-data-loaded"},"Verify the data was loaded")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"../../docs/guides/getting_started#execute-notebook"},"Execute the Notebook")," ",(0,r.kt)("inlineCode",{parentName:"li"},"pliastro_notebook_example.ipynb"),". ",(0,r.kt)("br",null),"\nYou will find the notebook under ",(0,r.kt)("inlineCode",{parentName:"li"},"citros_template/notebooks")," folder.")),(0,r.kt)("p",null,"The graph below shows us the exact orbit duration depending of Drag coefficient:"),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"png",src:a(87552).Z,title:"CITROS example",width:"562",height:"547"})))}d.isMDXComponent=!0},87552:(t,e,a)=>{a.d(e,{Z:()=>n});const n=a.p+"assets/images/citros3-d07909f63d6b7c7a3214cab86653fa63.png"},52182:(t,e,a)=>{a.d(e,{Z:()=>n});const n=a.p+"assets/images/img0-3505373173cfa4396e59f70d5a98edb9.jpg"},42951:(t,e,a)=>{a.d(e,{Z:()=>n});const n=a.p+"assets/images/main-6577a8b57a04a0e1399aa77a87c426d7.gif"}}]);
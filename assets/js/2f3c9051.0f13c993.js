"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[2288],{3905:(e,t,a)=>{a.d(t,{Zo:()=>u,kt:()=>h});var n=a(67294);function r(e,t,a){return t in e?Object.defineProperty(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}function i(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,n)}return a}function l(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?i(Object(a),!0).forEach((function(t){r(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):i(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}function o(e,t){if(null==e)return{};var a,n,r=function(e,t){if(null==e)return{};var a,n,r={},i=Object.keys(e);for(n=0;n<i.length;n++)a=i[n],t.indexOf(a)>=0||(r[a]=e[a]);return r}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(n=0;n<i.length;n++)a=i[n],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(r[a]=e[a])}return r}var s=n.createContext({}),p=function(e){var t=n.useContext(s),a=t;return e&&(a="function"==typeof e?e(t):l(l({},t),e)),a},u=function(e){var t=p(e.components);return n.createElement(s.Provider,{value:t},e.children)},d="mdxType",m={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},c=n.forwardRef((function(e,t){var a=e.components,r=e.mdxType,i=e.originalType,s=e.parentName,u=o(e,["components","mdxType","originalType","parentName"]),d=p(a),c=r,h=d["".concat(s,".").concat(c)]||d[c]||m[c]||i;return a?n.createElement(h,l(l({ref:t},u),{},{components:a})):n.createElement(h,l({ref:t},u))}));function h(e,t){var a=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var i=a.length,l=new Array(i);l[0]=c;var o={};for(var s in t)hasOwnProperty.call(t,s)&&(o[s]=t[s]);o.originalType=e,o[d]="string"==typeof e?e:r,l[1]=o;for(var p=2;p<i;p++)l[p]=a[p];return n.createElement.apply(null,l)}return n.createElement.apply(null,a)}c.displayName="MDXCreateElement"},1073:(e,t,a)=>{a.r(t),a.d(t,{assets:()=>s,contentTitle:()=>l,default:()=>m,frontMatter:()=>i,metadata:()=>o,toc:()=>p});var n=a(87462),r=(a(67294),a(3905));const i={sidebar_position:60,sidebar_label:"Lunar Hopper"},l="Lunar Hopper",o={unversionedId:"lunar_hopper/lunar_hopper",id:"lunar_hopper/lunar_hopper",title:"Lunar Hopper",description:"Overview",source:"@site/docs_tutorials/lunar_hopper/lunar_hopper.md",sourceDirName:"lunar_hopper",slug:"/lunar_hopper/",permalink:"/docs_tutorials/lunar_hopper/",draft:!1,tags:[],version:"current",sidebarPosition:60,frontMatter:{sidebar_position:60,sidebar_label:"Lunar Hopper"},sidebar:"tutorialSidebar",previous:{title:"TurtleBot",permalink:"/docs_tutorials/turtlebot/"},next:{title:"Lunar Starship",permalink:"/docs_tutorials/lunar_starship/"}},s={},p=[{value:"Overview",id:"overview",level:2},{value:"Prerequisites",id:"prerequisites",level:2},{value:"Table of Contents",id:"table-of-contents",level:2},{value:"Installation",id:"installation",level:2},{value:"Workspace Overview",id:"workspace-overview",level:2},{value:"CITROS Initialization",id:"citros-initialization",level:2},{value:"Scenario",id:"scenario",level:2},{value:"Running the Scenario Using CITROS",id:"running-the-scenario-using-citros",level:2},{value:"Results",id:"results",level:2}],u={toc:p},d="wrapper";function m(e){let{components:t,...i}=e;return(0,r.kt)(d,(0,n.Z)({},u,i,{components:t,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"lunar-hopper"},"Lunar Hopper"),(0,r.kt)("h2",{id:"overview"},"Overview"),(0,r.kt)("p",null,"The Lunar Hopper project is a lunar exploration planning project aimed at solving the intricate problem of lunar hopper missions. It focuses on optimizing the spacecraft's trajectory across the whole flight. Leveraging state-of-the-art optimal problem-solving algorithms, specifically the ",(0,r.kt)("a",{parentName:"p",href:"https://mpopt.readthedocs.io/en/latest/"},"MPOPT Python library"),", this project seeks to determine the most efficient path for maximizing the distance traveled during the mission. It empowers users to customize essential parameters such as spacecraft mass, fuel quantity, thrust, and specific impulse. "),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"jpg",src:a(13146).Z,title:"Did you find an easter egg?)",width:"1024",height:"1024"})),(0,r.kt)("h2",{id:"prerequisites"},"Prerequisites"),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},"Please make sure you have all the ",(0,r.kt)("a",{parentName:"li",href:"../../docs/guides/getting_started#prerequisites-for-working-with-citros"},"necessary softwares")," to work with CITROS installed on your computer."),(0,r.kt)("li",{parentName:"ol"},"Install ",(0,r.kt)("a",{parentName:"li",href:"https://code.visualstudio.com/download"},"Visual Studio code"),"."),(0,r.kt)("li",{parentName:"ol"},"We strongly recommend that you work with ",(0,r.kt)("a",{parentName:"li",href:"../../docs/guides/dockerfile_overview"},"dockers"),". However, if you wish to work without dockers, please refer to the .devcontainer ",(0,r.kt)("a",{parentName:"li",href:"https://github.com/citros-garden/aerosandbox_cessna/tree/main/.devcontainer"},"directory")," in project's repo, the dependencies you need are in the ",(0,r.kt)("inlineCode",{parentName:"li"},"Dockerfile")," file."),(0,r.kt)("li",{parentName:"ol"},"(Optional) Install ",(0,r.kt)("a",{parentName:"li",href:"https://docs.Foxglove.dev/docs/introduction"},"Foxglove"),".")),(0,r.kt)("h2",{id:"table-of-contents"},"Table of Contents"),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"#installation"},"Installation")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"#workspace-overview"},"Workspace Overview")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"#citros-initialization"},"CITROS Initialization")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"#scenario"},"Scenario")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"#running-the-scenario-using-citros"},"Running the Scenario Using CITROS")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"#results"},"Results"))),(0,r.kt)("h2",{id:"installation"},"Installation"),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},"Clone the repository:")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-bash"},"git clone git@github.com:citros-garden/lunar_hopper.git\n")),(0,r.kt)("ol",{start:2},(0,r.kt)("li",{parentName:"ol"},"Open the repository in the ",(0,r.kt)("a",{parentName:"li",href:"../../docs/guides/getting_started#open-project-in-vscode-dev-container"},"VScode Dev Container"),".")),(0,r.kt)("h2",{id:"workspace-overview"},"Workspace Overview"),(0,r.kt)("p",null,"The Lunar Hopper simulation has the following ROS 2 parameters:"),(0,r.kt)("table",null,(0,r.kt)("thead",{parentName:"table"},(0,r.kt)("tr",{parentName:"thead"},(0,r.kt)("th",{parentName:"tr",align:null},"Parameter"),(0,r.kt)("th",{parentName:"tr",align:null},"Description"),(0,r.kt)("th",{parentName:"tr",align:null},"Package"))),(0,r.kt)("tbody",{parentName:"table"},(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"m_fuel_0"),(0,r.kt)("td",{parentName:"tr",align:null},"Initial fuel mass date"),(0,r.kt)("td",{parentName:"tr",align:null},"lunar_hopper")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"m_fuel_f"),(0,r.kt)("td",{parentName:"tr",align:null},"Final fuel mass"),(0,r.kt)("td",{parentName:"tr",align:null},"lunar_hopper")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"dry_mass"),(0,r.kt)("td",{parentName:"tr",align:null},"dry mass"),(0,r.kt)("td",{parentName:"tr",align:null},"lunar_hopper")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"F_thrustmax"),(0,r.kt)("td",{parentName:"tr",align:null},"The maximum amount of thrust"),(0,r.kt)("td",{parentName:"tr",align:null},"lunar_hopper")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"Isp"),(0,r.kt)("td",{parentName:"tr",align:null},"Specific impulse"),(0,r.kt)("td",{parentName:"tr",align:null},"lunar_hopper")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"publish_freq"),(0,r.kt)("td",{parentName:"tr",align:null},"Frequency of publishing"),(0,r.kt)("td",{parentName:"tr",align:null},"lunar_hopper")))),(0,r.kt)("admonition",{type:"note"},(0,r.kt)("ul",{parentName:"admonition"},(0,r.kt)("li",{parentName:"ul"},"Variables with '_0' are initial conditions."),(0,r.kt)("li",{parentName:"ul"},"Variables with '_f' are final conditions."))),(0,r.kt)("p",null,"This project contains only one launch file which will be used for CITROS launch. "),(0,r.kt)("table",null,(0,r.kt)("thead",{parentName:"table"},(0,r.kt)("tr",{parentName:"thead"},(0,r.kt)("th",{parentName:"tr",align:null},"Launch File"),(0,r.kt)("th",{parentName:"tr",align:null},"Description"),(0,r.kt)("th",{parentName:"tr",align:null},"Package"))),(0,r.kt)("tbody",{parentName:"table"},(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"lunar_hopper.launch.py"),(0,r.kt)("td",{parentName:"tr",align:null},"Lunar Hopper simulation launch file"),(0,r.kt)("td",{parentName:"tr",align:null},"lunar_hopper")))),(0,r.kt)("h2",{id:"citros-initialization"},"CITROS Initialization"),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"../../docs/guides/getting_started#installation"},"Install CITROS"),"."),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"../../docs/guides/getting_started#initialization"},"Initialize CITROS"),".")),(0,r.kt)("h2",{id:"scenario"},"Scenario"),(0,r.kt)("p",null,"The optimal trajectory computes by solving non-linear OCP (optimal control problems) in the standard Bolza form, by using pseudo-spectral collocation methods and adjusted, using an additional real dynamic function. ",(0,r.kt)("br",null),"\nThe OCP solver used in this example is ",(0,r.kt)("a",{parentName:"p",href:"https://mpopt.readthedocs.io/en/latest/"},"MPOPT")," (based on ",(0,r.kt)("a",{parentName:"p",href:"https://en.wikipedia.org/wiki/IPOPT#:~:text=IPOPT%2C%20short%20for%20%22Interior%20Point,the%20EPL%20(formerly%20CPL)."},"IPOPT"),") library modified by Lulav Space team. ",(0,r.kt)("br",null),'\nThe main goal of the project is to find the optimal way to "hop" on the Moon as far as possible with given vessel parameters.',(0,r.kt)("br",null)),(0,r.kt)("p",null,"For this tutorial, let's check how far the Hopper can hop on the Moon depending on Specific Impulse.\nFor that, we will launch a simulation batch with a distribution of Specific impulse parameter, starting from 200 and up to 300.\nThe parameter setup is listed in ",(0,r.kt)("inlineCode",{parentName:"p"},".citros/parameter_setups/default_param_setup.json"),". ",(0,r.kt)("br",null)),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-json"},'{\n    "packages": {\n        "lunar_hopper": {\n            "lunar_hopper": {\n                "ros__parameters": {\n                    "m_fuel_0": 27.5,\n                    "m_fuel_f": 0.0,\n                    "dry_mass": 30.0,\n                    "Fthrustmax": 208.0,\n                    "Isp": {\n                        "function": "my_func.py:func_with_context",\n                        "args": [200]\n                    },\n                    "publish_freq": 10.0\n                }\n            }\n        }\n    }\n}\n')),(0,r.kt)("p",null,"The ",(0,r.kt)("inlineCode",{parentName:"p"},"my_func.py")," file should contain:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"def func_with_context(num, context):\n    return num + float(context['sid'])*10\n")),(0,r.kt)("p",null,"This function will set the ",(0,r.kt)("inlineCode",{parentName:"p"},"Isp")," parameter in range from 200 to 200+10*n, where n = number of runs."),(0,r.kt)("p",null,"Learn more about parameter setup and defining custom functions in ",(0,r.kt)("a",{parentName:"p",href:"../../docs/advanced_guides/citros_structure#directory-simulations"},"Directory parameter_setups")," and ",(0,r.kt)("a",{parentName:"p",href:"../../docs/guides/config_params"},"Adding Functions to Parameter Setup")," pages."),(0,r.kt)("p",null,"In addition to parameter setup, you can configure the simulation performance setup (timeout, CPU, GPU and Memory) as well.\nThese parameters can be found in ",(0,r.kt)("inlineCode",{parentName:"p"},".citros/simulations/simulation_lunar_hopper.json"),". ",(0,r.kt)("br",null),"\nLook in ",(0,r.kt)("a",{parentName:"p",href:"../../docs/advanced_guides/citros_structure#directory-simulations"},"Directory simulations page")," for more information."),(0,r.kt)("h2",{id:"running-the-scenario-using-citros"},"Running the Scenario Using CITROS"),(0,r.kt)("p",null,"Follow these steps to ",(0,r.kt)("a",{parentName:"p",href:"../../docs/guides/getting_started#run-simulation"},"Run Simulation"),":"),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},"Name your  batch run simulation: ",(0,r.kt)("inlineCode",{parentName:"li"},"Lunar_hopper")),(0,r.kt)("li",{parentName:"ol"},"Add a message to your batch run simulation: ",(0,r.kt)("inlineCode",{parentName:"li"},"local test run")),(0,r.kt)("li",{parentName:"ol"},"Run your simulation ",(0,r.kt)("strong",{parentName:"li"}," 10 times "),".")),(0,r.kt)("p",null,"All the results will be saved under ",(0,r.kt)("inlineCode",{parentName:"p"},".citros/data/simulation_lunar_hopper/[simulation_name]")," folder.",(0,r.kt)("br",null),"\n",(0,r.kt)("em",{parentName:"p"},"in this case, simulation_name is Lunar_hopper")),(0,r.kt)("p",null,"To plot the local run results you can use ",(0,r.kt)("a",{parentName:"p",href:"../../docs/guides/foxglove_visual"},"Foxglove")," with the layout file existing in ",(0,r.kt)("inlineCode",{parentName:"p"},"foxglove_layout")," folder."),(0,r.kt)("p",null,"Use ",(0,r.kt)("inlineCode",{parentName:"p"},"layout_states.json")," for states plots:"),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"png",src:a(90222).Z,title:"Foxglove Example 1",width:"2487",height:"1511"})),(0,r.kt)("p",null,"Use ",(0,r.kt)("inlineCode",{parentName:"p"},"layout_controls.json")," for controls plots:"),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"png",src:a(14139).Z,title:"Foxglove Example 2",width:"2487",height:"1511"})),(0,r.kt)("h2",{id:"results"},"Results"),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"../../docs/guides/getting_started#create-db"},"Create Database")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"../../docs/guides/getting_started#load-data-to-db"},"Upload data to the database")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"../../docs/guides/getting_started#verify-data-loaded"},"Verify the data was loaded")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"../../docs/guides/getting_started#execute-notebook"},"Execute the Notebook")," ",(0,r.kt)("inlineCode",{parentName:"li"},"lunar_hopper_notebook_example.ipynb"),". ",(0,r.kt)("br",null),"\nYou will find the notebook under ",(0,r.kt)("inlineCode",{parentName:"li"},"citros_template/notebooks")," folder.")),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"png",src:a(85496).Z,title:"CITROS example",width:"607",height:"463"})))}m.isMDXComponent=!0},85496:(e,t,a)=>{a.d(t,{Z:()=>n});const n=a.p+"assets/images/citros3-e22000abe186deb81041b08973ea51a8.png"},90222:(e,t,a)=>{a.d(t,{Z:()=>n});const n=a.p+"assets/images/foxglove0-754c9f3b3f1059f8a5727e8cf5ca66d4.png"},14139:(e,t,a)=>{a.d(t,{Z:()=>n});const n=a.p+"assets/images/foxglove1-7daba796dcb1ed11807eb7b8e6fef295.png"},13146:(e,t,a)=>{a.d(t,{Z:()=>n});const n=a.p+"assets/images/hopper0-91d9e5bbe219e78dfc469d041432b3a9.jpg"}}]);
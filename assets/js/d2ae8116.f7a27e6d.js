"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[8290],{3905:(t,a,e)=>{e.d(a,{Zo:()=>p,kt:()=>k});var n=e(7294);function r(t,a,e){return a in t?Object.defineProperty(t,a,{value:e,enumerable:!0,configurable:!0,writable:!0}):t[a]=e,t}function i(t,a){var e=Object.keys(t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(t);a&&(n=n.filter((function(a){return Object.getOwnPropertyDescriptor(t,a).enumerable}))),e.push.apply(e,n)}return e}function s(t){for(var a=1;a<arguments.length;a++){var e=null!=arguments[a]?arguments[a]:{};a%2?i(Object(e),!0).forEach((function(a){r(t,a,e[a])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(e)):i(Object(e)).forEach((function(a){Object.defineProperty(t,a,Object.getOwnPropertyDescriptor(e,a))}))}return t}function l(t,a){if(null==t)return{};var e,n,r=function(t,a){if(null==t)return{};var e,n,r={},i=Object.keys(t);for(n=0;n<i.length;n++)e=i[n],a.indexOf(e)>=0||(r[e]=t[e]);return r}(t,a);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(t);for(n=0;n<i.length;n++)e=i[n],a.indexOf(e)>=0||Object.prototype.propertyIsEnumerable.call(t,e)&&(r[e]=t[e])}return r}var o=n.createContext({}),m=function(t){var a=n.useContext(o),e=a;return t&&(e="function"==typeof t?t(a):s(s({},a),t)),e},p=function(t){var a=m(t.components);return n.createElement(o.Provider,{value:a},t.children)},c="mdxType",d={inlineCode:"code",wrapper:function(t){var a=t.children;return n.createElement(n.Fragment,{},a)}},h=n.forwardRef((function(t,a){var e=t.components,r=t.mdxType,i=t.originalType,o=t.parentName,p=l(t,["components","mdxType","originalType","parentName"]),c=m(e),h=r,k=c["".concat(o,".").concat(h)]||c[h]||d[h]||i;return e?n.createElement(k,s(s({ref:a},p),{},{components:e})):n.createElement(k,s({ref:a},p))}));function k(t,a){var e=arguments,r=a&&a.mdxType;if("string"==typeof t||r){var i=e.length,s=new Array(i);s[0]=h;var l={};for(var o in a)hasOwnProperty.call(a,o)&&(l[o]=a[o]);l.originalType=t,l[c]="string"==typeof t?t:r,s[1]=l;for(var m=2;m<i;m++)s[m]=e[m];return n.createElement.apply(null,s)}return n.createElement.apply(null,e)}h.displayName="MDXCreateElement"},4940:(t,a,e)=>{e.r(a),e.d(a,{assets:()=>o,contentTitle:()=>s,default:()=>d,frontMatter:()=>i,metadata:()=>l,toc:()=>m});var n=e(7462),r=(e(7294),e(3905));const i={sidebar_position:10,sidebar_label:"Soft Landing"},s="Soft Landing Tutorial",l={unversionedId:"soft_landing/soft_landing",id:"soft_landing/soft_landing",title:"Soft Landing Tutorial",description:"Overview",source:"@site/docs_tutorials/soft_landing/soft_landing.md",sourceDirName:"soft_landing",slug:"/soft_landing/",permalink:"/docs_tutorials/soft_landing/",draft:!1,tags:[],version:"current",sidebarPosition:10,frontMatter:{sidebar_position:10,sidebar_label:"Soft Landing"},sidebar:"tutorialSidebar",previous:{title:"Introduction to CITROS",permalink:"/docs_tutorials/"},next:{title:"Drone",permalink:"/docs_tutorials/drone/"}},o={},m=[{value:"Overview",id:"overview",level:2},{value:"Prerequisites",id:"prerequisites",level:2},{value:"Table of Contents",id:"table-of-contents",level:2},{value:"Installation",id:"installation",level:2},{value:"Workspace Overview",id:"workspace-overview",level:2},{value:"CITROS Initialization",id:"citros-initialization",level:2},{value:"Scenario",id:"scenario",level:2},{value:"Running the Scenario Using CITROS",id:"running-the-scenario-using-citros",level:2},{value:"Running on The Cloud",id:"running-on-the-cloud",level:3},{value:"Results",id:"results",level:2}],p={toc:m},c="wrapper";function d(t){let{components:a,...i}=t;return(0,r.kt)(c,(0,n.Z)({},p,i,{components:a,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"soft-landing-tutorial"},"Soft Landing Tutorial"),(0,r.kt)("h2",{id:"overview"},"Overview"),(0,r.kt)("p",null,"This is a ROS 2 simulation of soft landing of an object.",(0,r.kt)("br",{parentName:"p"}),"\n","In the ROS 2 system we have two nodes: the first represents the ",(0,r.kt)("inlineCode",{parentName:"p"},"dynamics")," and the second one is the ",(0,r.kt)("inlineCode",{parentName:"p"},"controller"),"."),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},(0,r.kt)("strong",{parentName:"p"},"System dynamics")," - The system's equation of motion is the kinematic equation of a free body fall.",(0,r.kt)("br",{parentName:"p"}),"\n","for more information see ",(0,r.kt)("a",{parentName:"p",href:"https://github.com/CITROS-garden/soft_landing"},"Soft Landing"),"  ")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},(0,r.kt)("strong",{parentName:"p"},"The controller")," - The controller is based on this paper:\n",(0,r.kt)("em",{parentName:"p"},'S. Gutman, "Rendezvous and Soft Landing in Closed Form via LQ Optimization," 2019 27th Mediterranean Conference on Control and Automation (MED), Akko, Israel, 2019, pp. 536-540, doi: 10.1109/MED.2019.8798572.')))),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"jpg",src:e(7084).Z,title:"soft landing",width:"1992",height:"501"})),(0,r.kt)("p",null,"With CITROS, you can easily run multiple simulations and compare the results to find the optimal solution. It's a powerful tool that saves time and effort, allowing you to focus on improving your designs and achieving your goals.  "),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"jpg",src:e(6797).Z,width:"2048",height:"2048"})),(0,r.kt)("h2",{id:"prerequisites"},"Prerequisites"),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},"Please make sure you have all the ",(0,r.kt)("a",{parentName:"li",href:"/docs_tutorials/getting_started/#softwares-to-work-with-citros"},"necessary softwares")," to work with CITROS installed on your computer."),(0,r.kt)("li",{parentName:"ol"},"Install ",(0,r.kt)("a",{parentName:"li",href:"https://code.visualstudio.com/download"},"Visual Studio code"),"."),(0,r.kt)("li",{parentName:"ol"},"We strongly recommend that you work with ",(0,r.kt)("a",{parentName:"li",href:"/docs_tutorials/dockerfile_overview/"},"dockers"),". However, if you wish to work without dockers, please refer to the ",(0,r.kt)("a",{parentName:"li",href:"https://github.com/citros-garden/soft_landing/tree/main/.devcontainer"},".devcontainer")," directory in project's repo, the dependencies you need are in the ",(0,r.kt)("inlineCode",{parentName:"li"},"Dockerfile")," and ",(0,r.kt)("inlineCode",{parentName:"li"},"install.sh")," files.")),(0,r.kt)("h2",{id:"table-of-contents"},"Table of Contents"),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"#installation"},"Installation")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"#workspace-overview"},"Workspace Overview")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"#citros-initialization"},"CITROS Initialization")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"#scenario"},"Scenario")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"#running-the-scenario-using-citros"},"Running the Scenario Using CITROS")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"#results"},"Results"))),(0,r.kt)("h2",{id:"installation"},"Installation"),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("p",{parentName:"li"},"Clone the repository:"),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-sh"},"git clone git@github.com:citros-garden/soft_landing.git\n"))),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("p",{parentName:"li"},"Open the repository in the ",(0,r.kt)("a",{parentName:"p",href:"/docs_tutorials/getting_started/#open-project-in-vscode-dev-container"},"VScode Dev Container"),"."))),(0,r.kt)("h2",{id:"workspace-overview"},"Workspace Overview"),(0,r.kt)("p",null,"After all the prerequisites done, we can start configuring our project.",(0,r.kt)("br",{parentName:"p"}),"\n","This is a list of all the ROS 2 parameters that can be control by the user wish:"),(0,r.kt)("table",null,(0,r.kt)("thead",{parentName:"table"},(0,r.kt)("tr",{parentName:"thead"},(0,r.kt)("th",{parentName:"tr",align:null},"Parameter"),(0,r.kt)("th",{parentName:"tr",align:null},"Description"),(0,r.kt)("th",{parentName:"tr",align:null},"Package"))),(0,r.kt)("tbody",{parentName:"table"},(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"r_x0 , r_y0, r_z0"),(0,r.kt)("td",{parentName:"tr",align:null},"initial position"),(0,r.kt)("td",{parentName:"tr",align:null},"dynamics")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"v_x0 ,v_y0,v_z0"),(0,r.kt)("td",{parentName:"tr",align:null},"initial velocity"),(0,r.kt)("td",{parentName:"tr",align:null},"dynamics")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"g_x , g_y , g_z"),(0,r.kt)("td",{parentName:"tr",align:null},"gravity vector"),(0,r.kt)("td",{parentName:"tr",align:null},"dynamics")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"dt"),(0,r.kt)("td",{parentName:"tr",align:null},"time interval"),(0,r.kt)("td",{parentName:"tr",align:null},"dynamics")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"setpoint_r_x , setpoint_r_y , setpoint_r_z ,"),(0,r.kt)("td",{parentName:"tr",align:null},"ending position"),(0,r.kt)("td",{parentName:"tr",align:null},"controller")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"setpoint_v_x , setpoint_v_y , setpoint_v_z ,"),(0,r.kt)("td",{parentName:"tr",align:null},"ending velocity"),(0,r.kt)("td",{parentName:"tr",align:null},"controller")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"g"),(0,r.kt)("td",{parentName:"tr",align:null},"gravity parameter"),(0,r.kt)("td",{parentName:"tr",align:null},"controller")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"um"),(0,r.kt)("td",{parentName:"tr",align:null},"acceleration limit"),(0,r.kt)("td",{parentName:"tr",align:null},"controller")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"e"),(0,r.kt)("td",{parentName:"tr",align:null},"stoping condition value"),(0,r.kt)("td",{parentName:"tr",align:null},"controller")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"dt"),(0,r.kt)("td",{parentName:"tr",align:null},"time interval"),(0,r.kt)("td",{parentName:"tr",align:null},"controller")))),(0,r.kt)("p",null,(0,r.kt)("a",{parentName:"p",href:"/docs/config_params"},"citros_cli")," provides more information about how to change the parameters by the user."),(0,r.kt)("p",null,"The launch files:",(0,r.kt)("br",{parentName:"p"}),"\n","",(0,r.kt)("inlineCode",{parentName:"p"},"dynamics_controller.launch.py")," launch the dynamics with the controller and ",(0,r.kt)("inlineCode",{parentName:"p"},"dynamics.launch.py")," launch only the dynamics.",(0,r.kt)("br",{parentName:"p"}),"\n","You can view the launch files ",(0,r.kt)("a",{parentName:"p",href:"https://github.com/citros-garden/soft_landing/tree/main/src/dynamics/launch"},"here"),"."),(0,r.kt)("h2",{id:"citros-initialization"},"CITROS Initialization"),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"/docs_tutorials/getting_started/#installation"},"Install CITROS"),"."),(0,r.kt)("li",{parentName:"ol"},"Follow ",(0,r.kt)("a",{parentName:"li",href:"/docs_tutorials/getting_started/#initialization"},"these steps")," to Initialize CITROS.")),(0,r.kt)("p",null,"Now you can see ",(0,r.kt)("inlineCode",{parentName:"p"},".CITROS")," directory in the explorer. "),(0,r.kt)("h2",{id:"scenario"},"Scenario"),(0,r.kt)("p",null,"Let's say we wish to land safely at some point on the moon's surface. To do that, we need a controller that can manage our velocity and guide us to the landing point while minimizing our speed.",(0,r.kt)("br",{parentName:"p"}),"\n","There are many controller ideas but we need to determine their effectiveness and limitations.",(0,r.kt)("br",{parentName:"p"}),"\n","Here we will try to find the limitations of the controller that based on the paper above by using CITROS."),(0,r.kt)("p",null,"The control guidance is a time-to-go dependent affine function. Time-to-go is obtained by solving a quartic polynomial equation for the initial conditions.",(0,r.kt)("br",{parentName:"p"}),"\n","So by giving the initial velocity value, we could check the validation of that controller.\nInstead of giving some random values to the initial velocity of the simulation until we can find the limits, CITROS allows us to run multiple simulations parallel at a short time and also provide random values of the initial velocity.",(0,r.kt)("br",{parentName:"p"}),"\n","In this scenario,let's say that each initial velocity parameter (v_x0, v_y0, v_z0) will be distributed normally: N(",(0,r.kt)("span",{parentName:"p",className:"math math-inline"},(0,r.kt)("span",{parentName:"span",className:"katex"},(0,r.kt)("span",{parentName:"span",className:"katex-mathml"},(0,r.kt)("math",{parentName:"span",xmlns:"http://www.w3.org/1998/Math/MathML"},(0,r.kt)("semantics",{parentName:"math"},(0,r.kt)("mrow",{parentName:"semantics"},(0,r.kt)("mi",{parentName:"mrow"},"\u03bc")),(0,r.kt)("annotation",{parentName:"semantics",encoding:"application/x-tex"},"\\mu")))),(0,r.kt)("span",{parentName:"span",className:"katex-html","aria-hidden":"true"},(0,r.kt)("span",{parentName:"span",className:"base"},(0,r.kt)("span",{parentName:"span",className:"strut",style:{height:"0.625em",verticalAlign:"-0.1944em"}}),(0,r.kt)("span",{parentName:"span",className:"mord mathnormal"},"\u03bc"))))),", ",(0,r.kt)("span",{parentName:"p",className:"math math-inline"},(0,r.kt)("span",{parentName:"span",className:"katex"},(0,r.kt)("span",{parentName:"span",className:"katex-mathml"},(0,r.kt)("math",{parentName:"span",xmlns:"http://www.w3.org/1998/Math/MathML"},(0,r.kt)("semantics",{parentName:"math"},(0,r.kt)("mrow",{parentName:"semantics"},(0,r.kt)("mi",{parentName:"mrow"},"\u03c3")),(0,r.kt)("annotation",{parentName:"semantics",encoding:"application/x-tex"},"\\sigma")))),(0,r.kt)("span",{parentName:"span",className:"katex-html","aria-hidden":"true"},(0,r.kt)("span",{parentName:"span",className:"base"},(0,r.kt)("span",{parentName:"span",className:"strut",style:{height:"0.4306em"}}),(0,r.kt)("span",{parentName:"span",className:"mord mathnormal",style:{marginRight:"0.03588em"}},"\u03c3"))))),").  "),(0,r.kt)("p",null,"By configuring the velocity parameters using ",(0,r.kt)("span",{parentName:"p",className:"math math-inline"},(0,r.kt)("span",{parentName:"span",className:"katex"},(0,r.kt)("span",{parentName:"span",className:"katex-mathml"},(0,r.kt)("math",{parentName:"span",xmlns:"http://www.w3.org/1998/Math/MathML"},(0,r.kt)("semantics",{parentName:"math"},(0,r.kt)("mrow",{parentName:"semantics"},(0,r.kt)("mi",{parentName:"mrow"},"\u03bc")),(0,r.kt)("annotation",{parentName:"semantics",encoding:"application/x-tex"},"\\mu")))),(0,r.kt)("span",{parentName:"span",className:"katex-html","aria-hidden":"true"},(0,r.kt)("span",{parentName:"span",className:"base"},(0,r.kt)("span",{parentName:"span",className:"strut",style:{height:"0.625em",verticalAlign:"-0.1944em"}}),(0,r.kt)("span",{parentName:"span",className:"mord mathnormal"},"\u03bc")))))," and ",(0,r.kt)("span",{parentName:"p",className:"math math-inline"},(0,r.kt)("span",{parentName:"span",className:"katex"},(0,r.kt)("span",{parentName:"span",className:"katex-mathml"},(0,r.kt)("math",{parentName:"span",xmlns:"http://www.w3.org/1998/Math/MathML"},(0,r.kt)("semantics",{parentName:"math"},(0,r.kt)("mrow",{parentName:"semantics"},(0,r.kt)("mi",{parentName:"mrow"},"\u03c3")),(0,r.kt)("annotation",{parentName:"semantics",encoding:"application/x-tex"},"\\sigma")))),(0,r.kt)("span",{parentName:"span",className:"katex-html","aria-hidden":"true"},(0,r.kt)("span",{parentName:"span",className:"base"},(0,r.kt)("span",{parentName:"span",className:"strut",style:{height:"0.4306em"}}),(0,r.kt)("span",{parentName:"span",className:"mord mathnormal",style:{marginRight:"0.03588em"}},"\u03c3"))))),", we can identify the conditions under which the controller is most likely to fail."),(0,r.kt)("h2",{id:"running-the-scenario-using-citros"},"Running the Scenario Using CITROS"),(0,r.kt)("p",null,"To configure the scenario described ",(0,r.kt)("a",{parentName:"p",href:"#scenario"},"above"),", I created a ",(0,r.kt)("inlineCode",{parentName:"p"},"default_param_setup.json")," file located in ",(0,r.kt)("inlineCode",{parentName:"p"},".citros/parameter_setups")," and a ",(0,r.kt)("inlineCode",{parentName:"p"},"function object")," located in ",(0,r.kt)("inlineCode",{parentName:"p"},".citros/parameter_setups/functions")," to randomize the initial velocity with ",(0,r.kt)("span",{parentName:"p",className:"math math-inline"},(0,r.kt)("span",{parentName:"span",className:"katex"},(0,r.kt)("span",{parentName:"span",className:"katex-mathml"},(0,r.kt)("math",{parentName:"span",xmlns:"http://www.w3.org/1998/Math/MathML"},(0,r.kt)("semantics",{parentName:"math"},(0,r.kt)("mrow",{parentName:"semantics"},(0,r.kt)("mi",{parentName:"mrow"},"\u03bc")),(0,r.kt)("annotation",{parentName:"semantics",encoding:"application/x-tex"},"\\mu")))),(0,r.kt)("span",{parentName:"span",className:"katex-html","aria-hidden":"true"},(0,r.kt)("span",{parentName:"span",className:"base"},(0,r.kt)("span",{parentName:"span",className:"strut",style:{height:"0.625em",verticalAlign:"-0.1944em"}}),(0,r.kt)("span",{parentName:"span",className:"mord mathnormal"},"\u03bc")))))," and ",(0,r.kt)("span",{parentName:"p",className:"math math-inline"},(0,r.kt)("span",{parentName:"span",className:"katex"},(0,r.kt)("span",{parentName:"span",className:"katex-mathml"},(0,r.kt)("math",{parentName:"span",xmlns:"http://www.w3.org/1998/Math/MathML"},(0,r.kt)("semantics",{parentName:"math"},(0,r.kt)("mrow",{parentName:"semantics"},(0,r.kt)("mi",{parentName:"mrow"},"\u03c3")),(0,r.kt)("annotation",{parentName:"semantics",encoding:"application/x-tex"},"\\sigma")))),(0,r.kt)("span",{parentName:"span",className:"katex-html","aria-hidden":"true"},(0,r.kt)("span",{parentName:"span",className:"base"},(0,r.kt)("span",{parentName:"span",className:"strut",style:{height:"0.4306em"}}),(0,r.kt)("span",{parentName:"span",className:"mord mathnormal",style:{marginRight:"0.03588em"}},"\u03c3")))))," for each parameter.",(0,r.kt)("br",{parentName:"p"}),"\n","For the initial validation of the controller, I chose random values of ",(0,r.kt)("span",{parentName:"p",className:"math math-inline"},(0,r.kt)("span",{parentName:"span",className:"katex"},(0,r.kt)("span",{parentName:"span",className:"katex-mathml"},(0,r.kt)("math",{parentName:"span",xmlns:"http://www.w3.org/1998/Math/MathML"},(0,r.kt)("semantics",{parentName:"math"},(0,r.kt)("mrow",{parentName:"semantics"},(0,r.kt)("mi",{parentName:"mrow"},"\u03bc")),(0,r.kt)("annotation",{parentName:"semantics",encoding:"application/x-tex"},"\\mu")))),(0,r.kt)("span",{parentName:"span",className:"katex-html","aria-hidden":"true"},(0,r.kt)("span",{parentName:"span",className:"base"},(0,r.kt)("span",{parentName:"span",className:"strut",style:{height:"0.625em",verticalAlign:"-0.1944em"}}),(0,r.kt)("span",{parentName:"span",className:"mord mathnormal"},"\u03bc")))))," and ",(0,r.kt)("span",{parentName:"p",className:"math math-inline"},(0,r.kt)("span",{parentName:"span",className:"katex"},(0,r.kt)("span",{parentName:"span",className:"katex-mathml"},(0,r.kt)("math",{parentName:"span",xmlns:"http://www.w3.org/1998/Math/MathML"},(0,r.kt)("semantics",{parentName:"math"},(0,r.kt)("mrow",{parentName:"semantics"},(0,r.kt)("mi",{parentName:"mrow"},"\u03c3")),(0,r.kt)("annotation",{parentName:"semantics",encoding:"application/x-tex"},"\\sigma")))),(0,r.kt)("span",{parentName:"span",className:"katex-html","aria-hidden":"true"},(0,r.kt)("span",{parentName:"span",className:"base"},(0,r.kt)("span",{parentName:"span",className:"strut",style:{height:"0.4306em"}}),(0,r.kt)("span",{parentName:"span",className:"mord mathnormal",style:{marginRight:"0.03588em"}},"\u03c3"))))),"."),(0,r.kt)("p",null,"First ensure that the project has been ",(0,r.kt)("a",{parentName:"p",href:"/docs_tutorials/getting_started/#build-the-project"},"built and sourced")),(0,r.kt)("p",null,"you're now ready to run a CITROS simulation, by using the run command:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sh"},"citros run -n 'test' -m 'testytest'\n? Please choose the simulation you wish to run:  \nsimulation_dynamics\n\u276f simulation_dynamics_controller\n")),(0,r.kt)("p",null,"The ",(0,r.kt)("inlineCode",{parentName:"p"},"simulation_dynamics_controller")," launches the ",(0,r.kt)("inlineCode",{parentName:"p"},"dynamics_controller.launch.py")," file and ",(0,r.kt)("inlineCode",{parentName:"p"},"simulation_dynamics")," launches the ",(0,r.kt)("inlineCode",{parentName:"p"},"dynamics.launch.py")," file.",(0,r.kt)("br",{parentName:"p"}),"\n","To execute, select the launch file and press the ",(0,r.kt)("inlineCode",{parentName:"p"},"Enter")," button.",(0,r.kt)("br",{parentName:"p"}),"\n","Wait for the output in the terminal.  "),(0,r.kt)("h3",{id:"running-on-the-cloud"},"Running on The Cloud"),(0,r.kt)("p",null,(0,r.kt)("a",{parentName:"p",href:"/docs_tutorials/getting_started/#upload-to-citros-server"},"Upload project to CITROS Server")),(0,r.kt)("p",null,"Finally, we can run it in the cloud, simply add ",(0,r.kt)("inlineCode",{parentName:"p"},"-r")," to the terminal command: "),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-bash"},"ros@docker-desktop:/workspaces/soft_landing$ citros run -n 'test' -m 'testytest' -r\n? Please choose the simulation you wish to run:   \nsimulation_dynamics\n\u276f simulation_dynamics_controller\n")),(0,r.kt)("p",null,"The simulation will now commence on the CITROS server, and the results will be uploaded automatically to the CITROS database."),(0,r.kt)("p",null,"For more run options check ",(0,r.kt)("a",{parentName:"p",href:"/docs/cli_commands#command-run"},"cli commands documentation"),". "),(0,r.kt)("p",null,"You can also ",(0,r.kt)("strong",{parentName:"p"},"(run simulations/docs/simulations/sim_step_by_step)")," directly from ",(0,r.kt)("a",{parentName:"p",href:"https://citros.io/soft_landing/batch"},"Runs tab")," in your soft landing repository."),(0,r.kt)("h2",{id:"results"},"Results"),(0,r.kt)("p",null,"The results were:"),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"Alt text",src:e(4430).Z,width:"594",height:"582"})),(0,r.kt)("p",null,"And by getting the miss distance and miss velocity we could show a figure of all the runs.  "),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"Alt text",src:e(5899).Z,width:"501",height:"449"}),"  "),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"Alt text",src:e(9503).Z,width:"451",height:"545"})),(0,r.kt)("p",null,"The full report with the data access and error analysis was generated using the data analysis package, can be found ",(0,r.kt)("a",{parentName:"p",href:"https://CITROS.io/soft_landing/blob/main/notebooks/Soft_landing_analysis.ipynb"},"here"),"."),(0,r.kt)("p",null,"After obtaining the results from CITROS and analyzing the data through visual graphs, we can confirm that the controller has met our demands. Most of the runs indicate that the miss distance and miss velocity are within our desired range.  "),(0,r.kt)("p",null,(0,r.kt)("em",{parentName:"p"},"In summary, for 100 simulations with different starting velocities"),(0,r.kt)("br",null),"\n",(0,r.kt)("em",{parentName:"p"},"we have 8 runs that miss the target (not within the radius 0.01","[m]"," from the target)."),(0,r.kt)("br",null),"\n",(0,r.kt)("em",{parentName:"p"},"And we have 6 fail runs that land with a miss distance greater than 0.01","[m]"," and miss velocity greater than 1","[m/s]")),(0,r.kt)("p",null,"However, it's important to note that this is just the initial validation of the controller. We will need to conduct additional simulations to further validate our findings. Additionally, we can experiment with different values of ",(0,r.kt)("span",{parentName:"p",className:"math math-inline"},(0,r.kt)("span",{parentName:"span",className:"katex"},(0,r.kt)("span",{parentName:"span",className:"katex-mathml"},(0,r.kt)("math",{parentName:"span",xmlns:"http://www.w3.org/1998/Math/MathML"},(0,r.kt)("semantics",{parentName:"math"},(0,r.kt)("mrow",{parentName:"semantics"},(0,r.kt)("mi",{parentName:"mrow"},"\u03bc")),(0,r.kt)("annotation",{parentName:"semantics",encoding:"application/x-tex"},"\\mu")))),(0,r.kt)("span",{parentName:"span",className:"katex-html","aria-hidden":"true"},(0,r.kt)("span",{parentName:"span",className:"base"},(0,r.kt)("span",{parentName:"span",className:"strut",style:{height:"0.625em",verticalAlign:"-0.1944em"}}),(0,r.kt)("span",{parentName:"span",className:"mord mathnormal"},"\u03bc")))))," and ",(0,r.kt)("span",{parentName:"p",className:"math math-inline"},(0,r.kt)("span",{parentName:"span",className:"katex"},(0,r.kt)("span",{parentName:"span",className:"katex-mathml"},(0,r.kt)("math",{parentName:"span",xmlns:"http://www.w3.org/1998/Math/MathML"},(0,r.kt)("semantics",{parentName:"math"},(0,r.kt)("mrow",{parentName:"semantics"},(0,r.kt)("mi",{parentName:"mrow"},"\u03c3")),(0,r.kt)("annotation",{parentName:"semantics",encoding:"application/x-tex"},"\\sigma")))),(0,r.kt)("span",{parentName:"span",className:"katex-html","aria-hidden":"true"},(0,r.kt)("span",{parentName:"span",className:"base"},(0,r.kt)("span",{parentName:"span",className:"strut",style:{height:"0.4306em"}}),(0,r.kt)("span",{parentName:"span",className:"mord mathnormal",style:{marginRight:"0.03588em"}},"\u03c3")))))," for each parameter."))}d.isMDXComponent=!0},4430:(t,a,e)=>{e.d(a,{Z:()=>n});const n=e.p+"assets/images/image-7-ca15520976985fe8f9653ddcdedca688.png"},5899:(t,a,e)=>{e.d(a,{Z:()=>n});const n=e.p+"assets/images/image-8-3ca52fd45c058cba4932c346dbb04654.png"},9503:(t,a,e)=>{e.d(a,{Z:()=>n});const n=e.p+"assets/images/image-bf7695b9dd43c29695191ee137f7def1.png"},6797:(t,a,e)=>{e.d(a,{Z:()=>n});const n=e.p+"assets/images/soft-landing-of-a-spacecraft-on-the-moon-a16ae26c7a09525c908c63633314c21c.png"},7084:(t,a,e)=>{e.d(a,{Z:()=>n});const n=e.p+"assets/images/soft_landing_control-5fd01b83fe6111c479417179e5b57352.jpg"}}]);
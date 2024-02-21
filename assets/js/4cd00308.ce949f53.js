"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[20435],{3905:(e,t,n)=>{n.d(t,{Zo:()=>u,kt:()=>h});var a=n(67294);function r(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function i(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);t&&(a=a.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,a)}return n}function o(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?i(Object(n),!0).forEach((function(t){r(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):i(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function l(e,t){if(null==e)return{};var n,a,r=function(e,t){if(null==e)return{};var n,a,r={},i=Object.keys(e);for(a=0;a<i.length;a++)n=i[a],t.indexOf(n)>=0||(r[n]=e[n]);return r}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(a=0;a<i.length;a++)n=i[a],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(r[n]=e[n])}return r}var s=a.createContext({}),m=function(e){var t=a.useContext(s),n=t;return e&&(n="function"==typeof e?e(t):o(o({},t),e)),n},u=function(e){var t=m(e.components);return a.createElement(s.Provider,{value:t},e.children)},c="mdxType",p={inlineCode:"code",wrapper:function(e){var t=e.children;return a.createElement(a.Fragment,{},t)}},d=a.forwardRef((function(e,t){var n=e.components,r=e.mdxType,i=e.originalType,s=e.parentName,u=l(e,["components","mdxType","originalType","parentName"]),c=m(n),d=r,h=c["".concat(s,".").concat(d)]||c[d]||p[d]||i;return n?a.createElement(h,o(o({ref:t},u),{},{components:n})):a.createElement(h,o({ref:t},u))}));function h(e,t){var n=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var i=n.length,o=new Array(i);o[0]=d;var l={};for(var s in t)hasOwnProperty.call(t,s)&&(l[s]=t[s]);l.originalType=e,l[c]="string"==typeof e?e:r,o[1]=l;for(var m=2;m<i;m++)o[m]=n[m];return a.createElement.apply(null,o)}return a.createElement.apply(null,n)}d.displayName="MDXCreateElement"},92766:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>s,contentTitle:()=>o,default:()=>p,frontMatter:()=>i,metadata:()=>l,toc:()=>m});var a=n(87462),r=(n(67294),n(3905));const i={sidebar_label:"citros run"},o="citros run",l={unversionedId:"commands/run",id:"version-0.2.59/commands/run",title:"citros run",description:"Description",source:"@site/versioned_docs/version-0.2.59/commands/run.md",sourceDirName:"commands",slug:"/commands/run",permalink:"/docs/0.2.59/commands/run",draft:!1,tags:[],version:"0.2.59",frontMatter:{sidebar_label:"citros run"},sidebar:"gettingStartedSidebar",previous:{title:"citros init",permalink:"/docs/0.2.59/commands/init"},next:{title:"citros data tree info",permalink:"/docs/0.2.59/commands/data/tree_info"}},s={},m=[{value:"Description",id:"description",level:2},{value:"Options",id:"options",level:2},{value:"Examples",id:"examples",level:2},{value:"Interactive Mode",id:"interactive-mode",level:2},{value:"Name of the batch run:",id:"name-of-the-batch-run",level:4},{value:"Message for the batch:",id:"message-for-the-batch",level:4},{value:"Number of runs:",id:"number-of-runs",level:4},{value:"Simulation to run:",id:"simulation-to-run",level:4}],u={toc:m},c="wrapper";function p(e){let{components:t,...n}=e;return(0,r.kt)(c,(0,a.Z)({},u,n,{components:t,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"citros-run"},(0,r.kt)("inlineCode",{parentName:"h1"},"citros run")),(0,r.kt)("h2",{id:"description"},"Description"),(0,r.kt)("p",null,"The ",(0,r.kt)("inlineCode",{parentName:"p"},"citros run"),"command will run the simulation on your machine.",(0,r.kt)("br",null),"\nAll the results will be saved under ",(0,r.kt)("inlineCode",{parentName:"p"},".citros/data/[simulation_name]/[batch_name]/[date]")," folder.",(0,r.kt)("br",null),"\nThe content of the ",(0,r.kt)("a",{parentName:"p",href:"../advanced_guides/citros_structure#directory-data"},"folder")," will contain: "),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"recorded bags"),(0,r.kt)("li",{parentName:"ul"},"logs from the simulation and citros itself"),(0,r.kt)("li",{parentName:"ul"},"metadata about the run"),(0,r.kt)("li",{parentName:"ul"},"metrics and information about the system it was running "),(0,r.kt)("li",{parentName:"ul"},"and more.")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-bash"},"$ citros run [-h] [-dir DIR] [-s [SIMULATION]] [-n [NAME]] [-m [MESSAGE]]\n             [--version [VERSION]] [-l] [-c [COMPLETIONS]] [-i [INDEX]] [-d] [-v]\n")),(0,r.kt)("h2",{id:"options"},"Options"),(0,r.kt)("table",null,(0,r.kt)("thead",{parentName:"table"},(0,r.kt)("tr",{parentName:"thead"},(0,r.kt)("th",{parentName:"tr",align:null},"Option"),(0,r.kt)("th",{parentName:"tr",align:null},"Description"))),(0,r.kt)("tbody",{parentName:"table"},(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"-h, --help"),(0,r.kt)("td",{parentName:"tr",align:null},"Show help message")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"-dir DIR"),(0,r.kt)("td",{parentName:"tr",align:null},"The working dir of the project")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"-s, --simulation ","[SIMULATION]"),(0,r.kt)("td",{parentName:"tr",align:null},"Simulation name")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"-n, --name ","[NAME]"),(0,r.kt)("td",{parentName:"tr",align:null},"Sets a name for the batch run")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"-m, --message ","[MESSAGE]"),(0,r.kt)("td",{parentName:"tr",align:null},"Sets a message for the run")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"--version ","[VERSION]"),(0,r.kt)("td",{parentName:"tr",align:null},"The batch run version.",(0,r.kt)("br",null),".citros/data/{sim_name}/{batch_name}/{ ",(0,r.kt)("strong",{parentName:"td"},"batch_version"),"}/{sid}")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"-l, --lan_traffic"),(0,r.kt)("td",{parentName:"tr",align:null},"Receive LAN ROS traffic in your simulation.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"-c, --completions ","[COMPLETIONS]"),(0,r.kt)("td",{parentName:"tr",align:null},"Number of times to run the simulation")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"-i, --index ","[INDEX]"),(0,r.kt)("td",{parentName:"tr",align:null},"The pard of the batch. if -1 will run all the batch")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"-d, --debug"),(0,r.kt)("td",{parentName:"tr",align:null},"Set logging level to debug")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"-v, --verbose"),(0,r.kt)("td",{parentName:"tr",align:null},"Use verbose console prints")))),(0,r.kt)("h2",{id:"examples"},"Examples"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-bash"},'$ citros run -n batch --message "batch message" -c 2\n? Please choose the simulation you wish to run \n\u276f simulation_name\nsimulation_name_2\n')),(0,r.kt)("admonition",{type:"note"},(0,r.kt)("p",{parentName:"admonition"},"When entering the explicit command, it is mandatory adding both ",(0,r.kt)("strong",{parentName:"p"},"batch name")," and a ",(0,r.kt)("strong",{parentName:"p"},"batch message"))),(0,r.kt)("h2",{id:"interactive-mode"},"Interactive Mode"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-bash"},"$ citros\n")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sh"},"? Select Action: \n\u250c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510\n\u2502  Init: initialize .citros in current directory                                     \u2502\n\u2502\u276f Run: new simulation                                                               \u2502\n\u2502  Data: for data management                                                         \u2502\n\u2502  Report: generation and management                                                 \u2502\n\u2502  ---------------                                                                   \u2502\n\u2502  EXIT                                                                              \u2502\n\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518\n")),(0,r.kt)("h4",{id:"name-of-the-batch-run"},"Name of the batch run:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sh"},"? Select Action: Run: new simulation\nPlease name this batch run (citros): \n")),(0,r.kt)("admonition",{type:"note"},(0,r.kt)("p",{parentName:"admonition"},"Default batch name is: ",(0,r.kt)("em",{parentName:"p"},"citros"))),(0,r.kt)("h4",{id:"message-for-the-batch"},"Message for the batch:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sh"},"? Select Action: Run: new simulation\nPlease name this batch run (citros): \nEnter a message for this batch run (This is a default batch message from citros):\n")),(0,r.kt)("admonition",{type:"note"},(0,r.kt)("p",{parentName:"admonition"},"Default batch run message is: ",(0,r.kt)("em",{parentName:"p"},"This is a default batch message from citros"))),(0,r.kt)("h4",{id:"number-of-runs"},"Number of runs:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sh"},"? Select Action: Run: new simulation\nPlease name this batch run (citros): \nEnter a message for this batch run (This is a default batch message from citros):\nHow many times you want the simulation to run? (1):\n")),(0,r.kt)("admonition",{type:"note"},(0,r.kt)("p",{parentName:"admonition"},"Default number of runs id: ",(0,r.kt)("em",{parentName:"p"},"1"))),(0,r.kt)("h4",{id:"simulation-to-run"},"Simulation to run:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sh"},"? Select Action: Run: new simulation\nPlease name this batch run (citros): \nEnter a message for this batch run (This is a default batch message from citros):\nHow many times you want the simulation to run? (1):\n? Please choose the simulation you wish to run:\n")))}p.isMDXComponent=!0}}]);
"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[6050],{3905:(e,t,a)=>{a.d(t,{Zo:()=>c,kt:()=>k});var n=a(67294);function i(e,t,a){return t in e?Object.defineProperty(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}function o(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,n)}return a}function r(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?o(Object(a),!0).forEach((function(t){i(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):o(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}function l(e,t){if(null==e)return{};var a,n,i=function(e,t){if(null==e)return{};var a,n,i={},o=Object.keys(e);for(n=0;n<o.length;n++)a=o[n],t.indexOf(a)>=0||(i[a]=e[a]);return i}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(n=0;n<o.length;n++)a=o[n],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(i[a]=e[a])}return i}var s=n.createContext({}),p=function(e){var t=n.useContext(s),a=t;return e&&(a="function"==typeof e?e(t):r(r({},t),e)),a},c=function(e){var t=p(e.components);return n.createElement(s.Provider,{value:t},e.children)},m="mdxType",d={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},u=n.forwardRef((function(e,t){var a=e.components,i=e.mdxType,o=e.originalType,s=e.parentName,c=l(e,["components","mdxType","originalType","parentName"]),m=p(a),u=i,k=m["".concat(s,".").concat(u)]||m[u]||d[u]||o;return a?n.createElement(k,r(r({ref:t},c),{},{components:a})):n.createElement(k,r({ref:t},c))}));function k(e,t){var a=arguments,i=t&&t.mdxType;if("string"==typeof e||i){var o=a.length,r=new Array(o);r[0]=u;var l={};for(var s in t)hasOwnProperty.call(t,s)&&(l[s]=t[s]);l.originalType=e,l[m]="string"==typeof e?e:i,r[1]=l;for(var p=2;p<o;p++)r[p]=a[p];return n.createElement.apply(null,r)}return n.createElement.apply(null,a)}u.displayName="MDXCreateElement"},90797:(e,t,a)=>{a.r(t),a.d(t,{assets:()=>s,contentTitle:()=>r,default:()=>d,frontMatter:()=>o,metadata:()=>l,toc:()=>p});var n=a(87462),i=(a(67294),a(3905));const o={sidebar_label:"Detailed Guide for CITROS"},r="Detailed Guide for CITROS",l={unversionedId:"guides/getting_started",id:"version-0.2.18/guides/getting_started",title:"Detailed Guide for CITROS",description:"Prerequisites for Working With CITROS",source:"@site/versioned_docs/version-0.2.18/guides/getting_started.md",sourceDirName:"guides",slug:"/guides/getting_started",permalink:"/docs/0.2.18/guides/getting_started",draft:!1,tags:[],version:"0.2.18",frontMatter:{sidebar_label:"Detailed Guide for CITROS"},sidebar:"gettingStartedSidebar",previous:{title:"run",permalink:"/docs/0.2.18/commands/simulation/run"},next:{title:"Adding Functions to Parameter Setup",permalink:"/docs/0.2.18/guides/config_params"}},s={},p=[{value:"Prerequisites for Working With CITROS",id:"prerequisites-for-working-with-citros",level:2},{value:"Installation",id:"installation",level:2},{value:"Initialization",id:"initialization",level:2},{value:"Run Simulation",id:"run-simulation",level:2},{value:"CITROS DB",id:"citros-db",level:2},{value:"Create DB",id:"create-db",level:3},{value:"Load Data to DB",id:"load-data-to-db",level:3},{value:"Verify Data Loaded",id:"verify-data-loaded",level:3},{value:"Batch Status",id:"batch-status",level:4},{value:"Execute Notebook",id:"execute-notebook",level:2}],c={toc:p},m="wrapper";function d(e){let{components:t,...o}=e;return(0,i.kt)(m,(0,n.Z)({},c,o,{components:t,mdxType:"MDXLayout"}),(0,i.kt)("h1",{id:"detailed-guide-for-citros"},"Detailed Guide for CITROS"),(0,i.kt)("h2",{id:"prerequisites-for-working-with-citros"},"Prerequisites for Working With CITROS"),(0,i.kt)("p",null,"Download and install the following to work with CITROS"),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("a",{parentName:"li",href:"https://www.python.org/downloads/"},"Python3")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("a",{parentName:"li",href:"https://git-scm.com/"},"git")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("a",{parentName:"li",href:"https://docs.docker.com/get-docker/"},"Docker")," - To understand why CITROS uses Docker, read ",(0,i.kt)("a",{parentName:"li",href:"../guides/dockerfile_overview"},"CITROS usage in Dockerfile"),".")),(0,i.kt)("h2",{id:"installation"},"Installation"),(0,i.kt)("p",null,"To install CITROS using pip, open terminal and write the following command:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre"},"$ pip install citros --upgrade\n")),(0,i.kt)("p",null,"You can verify that the installation succeeded by running "),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-bash"},"$ citros -V\n")),(0,i.kt)("admonition",{type:"tip"},(0,i.kt)("p",{parentName:"admonition"},"If you ran the ",(0,i.kt)("inlineCode",{parentName:"p"},"pip install citros")," command and you still getting "),(0,i.kt)("pre",{parentName:"admonition"},(0,i.kt)("code",{parentName:"pre",className:"language-bash"}," $ citros: command not found\n")),(0,i.kt)("p",{parentName:"admonition"},"Try running:"),(0,i.kt)("pre",{parentName:"admonition"},(0,i.kt)("code",{parentName:"pre",className:"language-bash"}," $ source ~/.profile \n")),(0,i.kt)("p",{parentName:"admonition"},"This should solve your problem and you should be able to run citros commands, otherwise ",(0,i.kt)("a",{parentName:"p",href:"https://discord.com/"},"contact us"),".")),(0,i.kt)("h2",{id:"initialization"},"Initialization"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-bash"},"$ citros init\n")),(0,i.kt)("p",null,"As you can see, a lot more is happening when you initialize your repository while being logged in. We will not delve into all the details behind the scenes, but as always, feel free to roam through the ",(0,i.kt)("a",{parentName:"p",href:"https://citros.io/doc/docs_cli"},"CLI Documentation")," for further details."),(0,i.kt)("h2",{id:"run-simulation"},"Run Simulation"),(0,i.kt)("p",null,"After your ",(0,i.kt)("inlineCode",{parentName:"p"},".citros")," repository has been initialized, you're ready to run a CITROS simulation."),(0,i.kt)("ol",null,(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"type ",(0,i.kt)("inlineCode",{parentName:"p"},"citros")," command"),(0,i.kt)("pre",{parentName:"li"},(0,i.kt)("code",{parentName:"pre",className:"language-bash"},"$ citros\n"))),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"Choose the ",(0,i.kt)("inlineCode",{parentName:"p"},"Run")," action:"),(0,i.kt)("pre",{parentName:"li"},(0,i.kt)("code",{parentName:"pre",className:"language-sh"},"? Select Action: \n\u250c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510\n\u2502  \ud83c\udf4b Init: initialize .citros in current directory      \u2502\n\u2502\u276f \ud83d\udd25 Run: new simulation                                \u2502\n\u2502  \ud83d\udcca Data: for data management                          \u2502\n\u2502  \ud83d\udcdd Report: generation and management                  \u2502\n\u2502  \ud83d\udd16 Service: CITROS API service functions              \u2502\n\u2502  ---------------                                       \u2502\n\u2502  EXIT                                                  \u2502\n\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518\n"))),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"Name the batch run:"),(0,i.kt)("pre",{parentName:"li"},(0,i.kt)("code",{parentName:"pre",className:"language-sh"},"? Select Action: \ud83d\udd25 Run: new simulation\nPlease name this batch run (citros): \n")),(0,i.kt)("admonition",{parentName:"li",type:"note"},(0,i.kt)("p",{parentName:"admonition"},"Press ",(0,i.kt)("inlineCode",{parentName:"p"},"Enter")," to name the simulation ",(0,i.kt)("em",{parentName:"p"},'"citros"'),".")))),(0,i.kt)("ol",{start:4},(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"Enter a message for the batch:"),(0,i.kt)("pre",{parentName:"li"},(0,i.kt)("code",{parentName:"pre",className:"language-sh"},"? Select Action: \ud83d\udd25 Run: new simulation\nPlease name this batch run (citros): \nEnter a message for this batch run (This is a default batch message from citros):\n")),(0,i.kt)("admonition",{parentName:"li",type:"note"},(0,i.kt)("p",{parentName:"admonition"},"Press ",(0,i.kt)("inlineCode",{parentName:"p"},"Enter")," to add the default batch run message:",(0,i.kt)("br",null),"\n",(0,i.kt)("em",{parentName:"p"},'"This is a default batch message from citros"')))),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"Choose number of runs:"),(0,i.kt)("pre",{parentName:"li"},(0,i.kt)("code",{parentName:"pre",className:"language-sh"},"? Select Action: \ud83d\udd25 Run: new simulation\nPlease name this batch run (citros): \nEnter a message for this batch run (This is a default batch message from citros):\nHow many times you want the simulation to run? (1):\n")),(0,i.kt)("admonition",{parentName:"li",type:"note"},(0,i.kt)("p",{parentName:"admonition"},"Press ",(0,i.kt)("inlineCode",{parentName:"p"},"Enter")," to run the simulation once")))),(0,i.kt)("ol",{start:6},(0,i.kt)("li",{parentName:"ol"},"Lastly choose the simulation you want to run:",(0,i.kt)("pre",{parentName:"li"},(0,i.kt)("code",{parentName:"pre",className:"language-sh"},"? Select Action: \ud83d\udd25 Run: new simulation\nPlease name this batch run (citros): \nEnter a message for this batch run (This is a default batch message from citros):\nHow many times you want the simulation to run? (1):\n? Please choose the simulation you wish to run:\n")))),(0,i.kt)("admonition",{type:"note"},(0,i.kt)("p",{parentName:"admonition"},"The command above will run the simulation on your machine, and save all the results under ",(0,i.kt)("inlineCode",{parentName:"p"},".citros/data/[simulation_name]/[batch_name]/[date]")," folder.",(0,i.kt)("br",null),"\nThe content of the ",(0,i.kt)("a",{parentName:"p",href:"../advanced_guides/citros_structure#directory-data"},"folder")," will contain: "),(0,i.kt)("ul",{parentName:"admonition"},(0,i.kt)("li",{parentName:"ul"},"recorded bags"),(0,i.kt)("li",{parentName:"ul"},"logs from the simulation and citros itself"),(0,i.kt)("li",{parentName:"ul"},"metadata about the run"),(0,i.kt)("li",{parentName:"ul"},"metrics and information about the system it was running "),(0,i.kt)("li",{parentName:"ul"},"and more."))),(0,i.kt)("p",null,"To view all simulations use the data command:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-bash"},"$ citros\n")),(0,i.kt)("p",null,"Choose the ",(0,i.kt)("inlineCode",{parentName:"p"},"Data")," action:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sh"},"? Select Action: \n\u250c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510\n\u2502  \ud83c\udf4b Init: initialize .citros in current directory      \u2502\n\u2502  \ud83d\udd25 Run: new simulation                                \u2502\n\u2502\u276f \ud83d\udcca Data: for data management                          \u2502\n\u2502  \ud83d\udcdd Report: generation and management                  \u2502\n\u2502  \ud83d\udd16 Service: CITROS API service functions              \u2502\n\u2502  ---------------                                       \u2502\n\u2502  EXIT                                                  \u2502\n\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518\n")),(0,i.kt)("p",null,"Choose ",(0,i.kt)("inlineCode",{parentName:"p"},"List")," to view all simulations"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sh"},"? Select Action: \ud83d\udcca Data: for data management \n? Select Action: \n\u250c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510\n\u2502  \ud83c\udf32 Tree: tree view of data                            \u2502\n\u2502\u276f *\ufe0f\u20e3 List: reports list                                 \u2502\n\u2502  \ud83d\udcc2 DB: section                                        \u2502\n\u2502  \ud83d\uddf3 Service: section                                   \u2502\n\u2502  ---------------                                       \u2502\n\u2502  EXIT                                                  \u2502\n\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518\n")),(0,i.kt)("p",null,"Table of all the simulations will be shown as output. ",(0,i.kt)("br",null),"\nThe table contains the following fields: Run name, Versions, message, status, completions, path"),(0,i.kt)("p",null,(0,i.kt)("img",{alt:"Alt text",src:a(23643).Z,width:"842",height:"154"})),(0,i.kt)("h2",{id:"citros-db"},"CITROS DB"),(0,i.kt)("h3",{id:"create-db"},"Create DB"),(0,i.kt)("p",null,"To create an instance of CITROS DB run"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-bash"},"citros data db create\n")),(0,i.kt)("h3",{id:"load-data-to-db"},"Load Data to DB"),(0,i.kt)("ol",null,(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"To load the data"),(0,i.kt)("pre",{parentName:"li"},(0,i.kt)("code",{parentName:"pre",className:"language-bash"},"$ citros\n"))),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"Choose the ",(0,i.kt)("inlineCode",{parentName:"p"},"Data")," action:"),(0,i.kt)("pre",{parentName:"li"},(0,i.kt)("code",{parentName:"pre",className:"language-sh"},"? Select Action: \n\u250c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510\n\u2502  \ud83c\udf4b Init: initialize .citros in current directory      \u2502\n\u2502  \ud83d\udd25 Run: new simulation                                \u2502\n\u2502\u276f \ud83d\udcca Data: for data managment                           \u2502\n\u2502  \ud83d\udcdd Report: generation and management                  \u2502\n\u2502  \ud83d\udd16 Service: CITROS API service functions              \u2502\n\u2502  ---------------                                       \u2502\n\u2502  EXIT                                                  \u2502\n\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518\n"))),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"choose the ",(0,i.kt)("inlineCode",{parentName:"p"},"Tree")," action"),(0,i.kt)("pre",{parentName:"li"},(0,i.kt)("code",{parentName:"pre",className:"language-sh"},"? Select Action: \n\u250c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510\n\u2502\u276f \ud83c\udf32 Tree: tree view of data                            \u2502\n\u2502  *\ufe0f\u20e3 List: reports list                                 \u2502\n\u2502  \ud83d\udcc2 DB: section                                        \u2502\n\u2502  \ud83d\uddf3 Service: section                                   \u2502\n\u2502  ---------------                                       \u2502\n\u2502  EXIT                                                  \u2502\n\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518\n"))),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"Choose the simulation, batch and version you'ld like to upload:"),(0,i.kt)("pre",{parentName:"li"},(0,i.kt)("code",{parentName:"pre",className:"language-sh"},"? Select Action: \ud83d\udcca Data: for data management \n? Select Action: \ud83c\udf32 Tree: tree view of data\n? Select Simulation: [simulation_name]\n? Select Batch: [batch_name]\n? Select Version: [version ID]\n"))),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"Choose the ",(0,i.kt)("inlineCode",{parentName:"p"},"Load")," actions"),(0,i.kt)("pre",{parentName:"li"},(0,i.kt)("code",{parentName:"pre",className:"language-sh"},"? Select Action: \ud83d\udcca Data: for data management \n? Select Action: \ud83c\udf32 Tree: tree view of data\n? Select Simulation: [simulation_name]\n? Select Batch: [batch_name]\n? Select Version: [version ID]\n? Select Action: \n\u250c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510\n\u2502  Info                                                           \u2502\n\u2502\u276f Load                                                           \u2502\n\u2502  Unload                                                         \u2502\n\u2502  Delete                                                         \u2502\n\u2502  ---------------                                                \u2502\n\u2502  EXIT                                                           \u2502\n\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518\n")))),(0,i.kt)("admonition",{type:"note"},(0,i.kt)("p",{parentName:"admonition"},"You can ",(0,i.kt)("a",{parentName:"p",href:"#verify-data-loaded"},"verify")," the data is loaded before uploading it to the database")),(0,i.kt)("h3",{id:"verify-data-loaded"},"Verify Data Loaded"),(0,i.kt)("p",null,"To verify the data is loaded"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-bash"},"citros data list\n")),(0,i.kt)("h4",{id:"batch-status"},"Batch Status"),(0,i.kt)("ol",null,(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("inlineCode",{parentName:"li"},"LOADED")," - the data is loaded to the database"),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("inlineCode",{parentName:"li"},"UNLOADED")," - the data is loaded to the database")),(0,i.kt)("p",null,(0,i.kt)("img",{alt:"Alt text",src:a(39045).Z,width:"842",height:"124"})),(0,i.kt)("h2",{id:"execute-notebook"},"Execute Notebook"),(0,i.kt)("p",null,"CITROS provides a ",(0,i.kt)("a",{parentName:"p",href:"https://pypi.org/project/citros-data-analysis/"},"citros data analysis package")," that gives access and functionality to analyze the data.\nWe recommend to use this package with a ",(0,i.kt)("inlineCode",{parentName:"p"},"python notebook")," which allows you to generate reports down the line."),(0,i.kt)("admonition",{type:"note"},(0,i.kt)("p",{parentName:"admonition"},"citros data analysis package is installed while running ",(0,i.kt)("inlineCode",{parentName:"p"},"pip install citros"),", so at this point you should have this package and you don't have to download it again.")),(0,i.kt)("p",null,"So now, after we uploaded the data, we can execute the notebook"),(0,i.kt)("ol",{start:2},(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"Go to ",(0,i.kt)("inlineCode",{parentName:"p"},"notebooks")," folder in your project.")),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"Open ","[notebook_name]",".ipynb")),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"Press ",(0,i.kt)("inlineCode",{parentName:"p"},"Run All")," button")),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"Scroll down the notebook to see the results."))))}d.isMDXComponent=!0},39045:(e,t,a)=>{a.d(t,{Z:()=>n});const n=a.p+"assets/images/sim_data_db-26007a66d69d2d7cb17c3c2a7f134abb.png"},23643:(e,t,a)=>{a.d(t,{Z:()=>n});const n=a.p+"assets/images/sim_data_list-4d97da1c12b1312d545409bac1325005.png"}}]);
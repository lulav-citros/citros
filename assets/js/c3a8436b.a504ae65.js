"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[27447],{3905:(e,t,a)=>{a.d(t,{Zo:()=>d,kt:()=>b});var n=a(67294);function r(e,t,a){return t in e?Object.defineProperty(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}function s(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,n)}return a}function i(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?s(Object(a),!0).forEach((function(t){r(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):s(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}function o(e,t){if(null==e)return{};var a,n,r=function(e,t){if(null==e)return{};var a,n,r={},s=Object.keys(e);for(n=0;n<s.length;n++)a=s[n],t.indexOf(a)>=0||(r[a]=e[a]);return r}(e,t);if(Object.getOwnPropertySymbols){var s=Object.getOwnPropertySymbols(e);for(n=0;n<s.length;n++)a=s[n],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(r[a]=e[a])}return r}var c=n.createContext({}),l=function(e){var t=n.useContext(c),a=t;return e&&(a="function"==typeof e?e(t):i(i({},t),e)),a},d=function(e){var t=l(e.components);return n.createElement(c.Provider,{value:t},e.children)},u="mdxType",p={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},m=n.forwardRef((function(e,t){var a=e.components,r=e.mdxType,s=e.originalType,c=e.parentName,d=o(e,["components","mdxType","originalType","parentName"]),u=l(a),m=r,b=u["".concat(c,".").concat(m)]||u[m]||p[m]||s;return a?n.createElement(b,i(i({ref:t},d),{},{components:a})):n.createElement(b,i({ref:t},d))}));function b(e,t){var a=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var s=a.length,i=new Array(s);i[0]=m;var o={};for(var c in t)hasOwnProperty.call(t,c)&&(o[c]=t[c]);o.originalType=e,o[u]="string"==typeof e?e:r,i[1]=o;for(var l=2;l<s;l++)i[l]=a[l];return n.createElement.apply(null,i)}return n.createElement.apply(null,a)}m.displayName="MDXCreateElement"},64372:(e,t,a)=>{a.r(t),a.d(t,{assets:()=>c,contentTitle:()=>i,default:()=>p,frontMatter:()=>s,metadata:()=>o,toc:()=>l});var n=a(87462),r=(a(67294),a(3905));const s={toc_max_heading_level:4,sidebar_label:"Getting Started",hide_title:!0,description:"Getting started",sidebar_position:1},i="Getting Started",o={unversionedId:"data_analysis/data_access/getting_started",id:"version-0.2.59/data_analysis/data_access/getting_started",title:"Getting Started",description:"Getting started",source:"@site/versioned_docs/version-0.2.59/data_analysis/data_access/getting_started.md",sourceDirName:"data_analysis/data_access",slug:"/data_analysis/data_access/getting_started",permalink:"/docs/0.2.59/data_analysis/data_access/getting_started",draft:!1,tags:[],version:"0.2.59",sidebarPosition:1,frontMatter:{toc_max_heading_level:4,sidebar_label:"Getting Started",hide_title:!0,description:"Getting started",sidebar_position:1},sidebar:"gettingStartedSidebar",previous:{title:"Overview",permalink:"/docs/0.2.59/data_analysis/data_access/"},next:{title:"Simulations and Batches",permalink:"/docs/0.2.59/data_analysis/data_access/batch_overview"}},c={},l=[{value:"Connection to the Database",id:"connection-to-the-database",level:2}],d={toc:l},u="wrapper";function p(e){let{components:t,...a}=e;return(0,r.kt)(u,(0,n.Z)({},d,a,{components:t,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"getting-started"},"Getting Started"),(0,r.kt)("p",null,"In order to get information about the data of the specific table in the database, to look through the main features and to query the selected parts the class ",(0,r.kt)("strong",{parentName:"p"},"CitrosDB")," from the package ",(0,r.kt)("strong",{parentName:"p"},"citros")," is used:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> from citros import CitrosDB\n")),(0,r.kt)("h2",{id:"connection-to-the-database"},"Connection to the Database"),(0,r.kt)("p",null,"To connect to the database ",(0,r.kt)("a",{parentName:"p",href:"/docs/0.2.59/data_analysis/documentation/access/citros_db#access.citros_db.CitrosDB"},(0,r.kt)("strong",{parentName:"a"},"CitrosDB"))," object is created:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> citros = CitrosDB()\n")),(0,r.kt)("p",null,"You can define simulation and/or batch you will work with:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> citros = CitrosDB(simulation = 'simulation_name', batch = 'batch_name')\n")),(0,r.kt)("p",null,"or set them up later."),(0,r.kt)("details",null,(0,r.kt)("summary",null,"Advanced CitrosDB parameters"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},'simulation : name of the simulation. Default is ENV variable "CITROS_SIMULATION" if it is set or None if the variable is not defined.'),(0,r.kt)("li",{parentName:"ul"},"batch : batch name."),(0,r.kt)("li",{parentName:"ul"},'sid : simulation run id. Default is ENV variable "CITROS_SIMULATION_RUN_ID" if it is set or None if the variable is not defined.'),(0,r.kt)("li",{parentName:"ul"},"host : database host address. Default is citros.database.CitrosDB.db_host."),(0,r.kt)("li",{parentName:"ul"},"port : default is citros.database.CitrosDB.db_port."),(0,r.kt)("li",{parentName:"ul"},"database : database name. Default is citros.database.CitrosDB.db_name."),(0,r.kt)("li",{parentName:"ul"},"user : user name. Default is citros.database.CitrosDB.db_user."),(0,r.kt)("li",{parentName:"ul"},"password : password. Default is citros.database.CitrosDB.db_password."),(0,r.kt)("li",{parentName:"ul"},"debug_connect : if ",(0,r.kt)("inlineCode",{parentName:"li"},"True"),", the number of connections and queries which were done by all CitrosDB objects with ",(0,r.kt)("inlineCode",{parentName:"li"},"debug_connect")," set ",(0,r.kt)("inlineCode",{parentName:"li"},"True")," existing in the current session is recorded. The information is recorded to the _stat.Stat() object. Default is ",(0,r.kt)("inlineCode",{parentName:"li"},"False"),"."),(0,r.kt)("li",{parentName:"ul"},"log : Logger to record log. By default, then the new logger is created.")),(0,r.kt)("p",null,'Say, we would like to connect to a database "myDatabase" with the user name "user" and password "myPassword", to work with batch "batchName" which is located in the schema "mySchema", using port \'5432\'. Also we would like to check how many connections and queries we are making during the session:'),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> citros = CitrosDB(host = 'hostName',\n                      user = 'user',\n                      password = 'myPassword',\n                      database = 'myDatabase',\n                      schema = 'mySchema',\n                      batch = 'batchName',\n                      port = '5432',\n                      debug_connect = True)\n>>> from citros.data.access._stat import Stat\n>>> stat = st.Stat()\n>>> stat.print_stat()\n{\n 'n_pg_connections': 0,\n 'n_pg_queries': 0,\n 'pg_calls': {\n }\n}\n"))))}p.isMDXComponent=!0}}]);
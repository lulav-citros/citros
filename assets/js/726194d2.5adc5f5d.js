"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[1144],{3905:(e,t,a)=>{a.d(t,{Zo:()=>d,kt:()=>h});var n=a(7294);function r(e,t,a){return t in e?Object.defineProperty(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}function i(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,n)}return a}function o(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?i(Object(a),!0).forEach((function(t){r(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):i(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}function s(e,t){if(null==e)return{};var a,n,r=function(e,t){if(null==e)return{};var a,n,r={},i=Object.keys(e);for(n=0;n<i.length;n++)a=i[n],t.indexOf(a)>=0||(r[a]=e[a]);return r}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(n=0;n<i.length;n++)a=i[n],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(r[a]=e[a])}return r}var l=n.createContext({}),c=function(e){var t=n.useContext(l),a=t;return e&&(a="function"==typeof e?e(t):o(o({},t),e)),a},d=function(e){var t=c(e.components);return n.createElement(l.Provider,{value:t},e.children)},p="mdxType",u={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},m=n.forwardRef((function(e,t){var a=e.components,r=e.mdxType,i=e.originalType,l=e.parentName,d=s(e,["components","mdxType","originalType","parentName"]),p=c(a),m=r,h=p["".concat(l,".").concat(m)]||p[m]||u[m]||i;return a?n.createElement(h,o(o({ref:t},d),{},{components:a})):n.createElement(h,o({ref:t},d))}));function h(e,t){var a=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var i=a.length,o=new Array(i);o[0]=m;var s={};for(var l in t)hasOwnProperty.call(t,l)&&(s[l]=t[l]);s.originalType=e,s[p]="string"==typeof e?e:r,o[1]=s;for(var c=2;c<i;c++)o[c]=a[c];return n.createElement.apply(null,o)}return n.createElement.apply(null,a)}m.displayName="MDXCreateElement"},4146:(e,t,a)=>{a.r(t),a.d(t,{assets:()=>l,contentTitle:()=>o,default:()=>u,frontMatter:()=>i,metadata:()=>s,toc:()=>c});var n=a(7462),r=(a(7294),a(3905));const i={toc_max_heading_level:4,sidebar_label:"Getting Started",hide_title:!0,description:"Getting started",sidebar_position:1},o="Getting Started",s={unversionedId:"data_access/getting_started",id:"version-v0.9.1/data_access/getting_started",title:"Getting Started",description:"Getting started",source:"@site/docs_data_analysis_versioned_docs/version-v0.9.1/data_access/getting_started.md",sourceDirName:"data_access",slug:"/data_access/getting_started",permalink:"/docs/docs_data_analysis/data_access/getting_started",draft:!1,tags:[],version:"v0.9.1",sidebarPosition:1,frontMatter:{toc_max_heading_level:4,sidebar_label:"Getting Started",hide_title:!0,description:"Getting started",sidebar_position:1},sidebar:"dataAnalysisSidebar",previous:{title:"Overview",permalink:"/docs/docs_data_analysis/data_access/"},next:{title:"Repository Overview",permalink:"/docs/docs_data_analysis/data_access/repository_overview"}},l={},c=[{value:"Connection to the Database",id:"connection-to-the-database",level:2}],d={toc:c},p="wrapper";function u(e){let{components:t,...a}=e;return(0,r.kt)(p,(0,n.Z)({},d,a,{components:t,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"getting-started"},"Getting Started"),(0,r.kt)("p",null,"In order to get information about the data of the specific table in the database, to look through the main features and to query the selected parts the module ",(0,r.kt)("strong",{parentName:"p"},"data_access")," from the package ",(0,r.kt)("strong",{parentName:"p"},"citros_data_analysis")," is used. Module is imported by:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"from citros_data_analysis import data_access as da\n")),(0,r.kt)("p",null,"To obtain the current package version number, execute the following:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> import citros_data_analysis\n>>> print(citros_data_analysis.__version__)\n")),(0,r.kt)("h2",{id:"connection-to-the-database"},"Connection to the Database"),(0,r.kt)("p",null,"To connect to the database ",(0,r.kt)("a",{parentName:"p",href:"/docs/docs_data_analysis/documentation/data_access/citros_db#citros_data_analysis.data_access.citros_db.CitrosDB"},(0,r.kt)("strong",{parentName:"a"},"CitrosDB"))," object is created:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> citros = da.CitrosDB()\n")),(0,r.kt)("p",null,"When working in the ",(0,r.kt)("a",{parentName:"p",href:"https://citros.io/"},"web")," or with cloud data locally using ",(0,r.kt)("a",{parentName:"p",href:"https://citros.io/doc/docs_cli"},"CITROS CLI"),", you typically don't need to pass any arguments. In the latter case, you need to be ",(0,r.kt)("a",{parentName:"p",href:"https://citros.io/doc/docs_tutorials#logging-in"},"logged in")," first."),(0,r.kt)("details",null,(0,r.kt)("summary",null,"Advanced CitrosDB parameters"),(0,r.kt)("p",null,"If no parameters are passed, the following predefined ENV variables are used:"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"repo: 'CITROS_REPO',"),(0,r.kt)("li",{parentName:"ul"},"simulation: 'CITROS_SIMULATION',"),(0,r.kt)("li",{parentName:"ul"},"batch: 'bid', "),(0,r.kt)("li",{parentName:"ul"},"sid: 'CITROS_SIMULATION_RUN_ID',"),(0,r.kt)("li",{parentName:"ul"},"host: 'PG_HOST'"),(0,r.kt)("li",{parentName:"ul"},"port: 'PG_PORT', or '5432' if 'PG_PORT' is not specified,"),(0,r.kt)("li",{parentName:"ul"},"database: 'PG_DATABASE',"),(0,r.kt)("li",{parentName:"ul"},"schema: 'PG_SCHEMA' or 'data_bucket' if 'PG_SCHEMA' is not specified,"),(0,r.kt)("li",{parentName:"ul"},"user: 'PG_USER',"),(0,r.kt)("li",{parentName:"ul"},"password: 'PG_PASSWORD',")),(0,r.kt)("p",null,"When working from a local environment and user, password, database ENV variables are not defined, they are set using CITROS CLI authentication; if repo ENV variable is not set, it is retrieved from 'name' field of the '.citros/project.json' file."),(0,r.kt)("p",null,"Some additional parameters can be defined:"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"debug: when ",(0,r.kt)("inlineCode",{parentName:"li"},"debug")," is set True, that will lead to code interruption if an error occurs, while with ",(0,r.kt)("inlineCode",{parentName:"li"},"debug")," turned to False program will try to handle errors and only print error messages without code breaking. By default, ",(0,r.kt)("inlineCode",{parentName:"li"},"debug")," = False."),(0,r.kt)("li",{parentName:"ul"},"async_query: if ",(0,r.kt)("inlineCode",{parentName:"li"},"False")," and the batch is not yet downloaded into the database, checks the status of the batch and tries to query it during the ",(0,r.kt)("inlineCode",{parentName:"li"},"async_timeout")," time. Default is ",(0,r.kt)("inlineCode",{parentName:"li"},"False"),"."),(0,r.kt)("li",{parentName:"ul"},"async_timeout: time of waiting for the batch to be downloaded into the database. Used only if ",(0,r.kt)("inlineCode",{parentName:"li"},"async_query")," is set ",(0,r.kt)("inlineCode",{parentName:"li"},"False"),". During this time checks the status of the batch and tries to query it.")),(0,r.kt)("p",null,'Say, we would like to connect to a database "myDatabase" with the user name "user" and password "myPassword", to work with batch "batchName" which is located in the schema "mySchema", using port \'5432\':'),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> citros = da.CitrosDB(host = 'hostName',\n                         user = 'user',\n                         password = 'myPassword',\n                         database = 'myDatabase',\n                         schema = 'mySchema',\n                         batch = 'batchName',\n                         port = '5432',\n                         debug = False)\n"))))}u.isMDXComponent=!0}}]);
"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[58150],{3905:(t,a,e)=>{e.d(a,{Zo:()=>d,kt:()=>g});var n=e(67294);function r(t,a,e){return a in t?Object.defineProperty(t,a,{value:e,enumerable:!0,configurable:!0,writable:!0}):t[a]=e,t}function l(t,a){var e=Object.keys(t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(t);a&&(n=n.filter((function(a){return Object.getOwnPropertyDescriptor(t,a).enumerable}))),e.push.apply(e,n)}return e}function i(t){for(var a=1;a<arguments.length;a++){var e=null!=arguments[a]?arguments[a]:{};a%2?l(Object(e),!0).forEach((function(a){r(t,a,e[a])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(e)):l(Object(e)).forEach((function(a){Object.defineProperty(t,a,Object.getOwnPropertyDescriptor(e,a))}))}return t}function s(t,a){if(null==t)return{};var e,n,r=function(t,a){if(null==t)return{};var e,n,r={},l=Object.keys(t);for(n=0;n<l.length;n++)e=l[n],a.indexOf(e)>=0||(r[e]=t[e]);return r}(t,a);if(Object.getOwnPropertySymbols){var l=Object.getOwnPropertySymbols(t);for(n=0;n<l.length;n++)e=l[n],a.indexOf(e)>=0||Object.prototype.propertyIsEnumerable.call(t,e)&&(r[e]=t[e])}return r}var o=n.createContext({}),p=function(t){var a=n.useContext(o),e=a;return t&&(e="function"==typeof t?t(a):i(i({},a),t)),e},d=function(t){var a=p(t.components);return n.createElement(o.Provider,{value:a},t.children)},u="mdxType",c={inlineCode:"code",wrapper:function(t){var a=t.children;return n.createElement(n.Fragment,{},a)}},m=n.forwardRef((function(t,a){var e=t.components,r=t.mdxType,l=t.originalType,o=t.parentName,d=s(t,["components","mdxType","originalType","parentName"]),u=p(e),m=r,g=u["".concat(o,".").concat(m)]||u[m]||c[m]||l;return e?n.createElement(g,i(i({ref:a},d),{},{components:e})):n.createElement(g,i({ref:a},d))}));function g(t,a){var e=arguments,r=a&&a.mdxType;if("string"==typeof t||r){var l=e.length,i=new Array(l);i[0]=m;var s={};for(var o in a)hasOwnProperty.call(a,o)&&(s[o]=a[o]);s.originalType=t,s[u]="string"==typeof t?t:r,i[1]=s;for(var p=2;p<l;p++)i[p]=e[p];return n.createElement.apply(null,i)}return n.createElement.apply(null,e)}m.displayName="MDXCreateElement"},69863:(t,a,e)=>{e.r(a),e.d(a,{assets:()=>o,contentTitle:()=>i,default:()=>c,frontMatter:()=>l,metadata:()=>s,toc:()=>p});var n=e(87462),r=(e(67294),e(3905));const l={toc_max_heading_level:4,sidebar_label:"Getting Started: Query Data",hide_title:!0,sidebar_position:1,description:"Quick start"},i="Getting Started: Query Data",s={unversionedId:"data_analysis/error_analysis/getting_started_query_data",id:"version-0.2.49/data_analysis/error_analysis/getting_started_query_data",title:"Getting Started: Query Data",description:"Quick start",source:"@site/versioned_docs/version-0.2.49/data_analysis/error_analysis/getting_started_query_data.md",sourceDirName:"data_analysis/error_analysis",slug:"/data_analysis/error_analysis/getting_started_query_data",permalink:"/docs/0.2.49/data_analysis/error_analysis/getting_started_query_data",draft:!1,tags:[],version:"0.2.49",sidebarPosition:1,frontMatter:{toc_max_heading_level:4,sidebar_label:"Getting Started: Query Data",hide_title:!0,sidebar_position:1,description:"Quick start"},sidebar:"gettingStartedSidebar",previous:{title:"Overview",permalink:"/docs/0.2.49/data_analysis/error_analysis/"},next:{title:"Bin, Interpolate and Calculate Statistics",permalink:"/docs/0.2.49/data_analysis/error_analysis/statistics"}},o={},p=[{value:"Query Data",id:"query-data",level:2}],d={toc:p},u="wrapper";function c(t){let{components:a,...e}=t;return(0,r.kt)(u,(0,n.Z)({},d,e,{components:a,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"getting-started-query-data"},"Getting Started: Query Data"),(0,r.kt)("p",null,"First of all, let's have a quick look at the ways to query data using ",(0,r.kt)("a",{parentName:"p",href:"/docs/0.2.49/data_analysis/documentation/access/citros_db"},(0,r.kt)("strong",{parentName:"a"},"class CitrosDB")),"."),(0,r.kt)("h2",{id:"query-data"},"Query Data"),(0,r.kt)("p",null,"To get access to a Citros database, create ",(0,r.kt)("a",{parentName:"p",href:"/docs/0.2.49/data_analysis/documentation/access/citros_db#access.citros_db.CitrosDB"},(0,r.kt)("strong",{parentName:"a"},"CitrosDB"))," object:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> from citros import CitrosDB\n>>> citros = CitrosDB()\n")),(0,r.kt)("p",null,"This way ",(0,r.kt)("a",{parentName:"p",href:"/docs/0.2.49/data_analysis/documentation/access/citros_db#access.citros_db.CitrosDB"},(0,r.kt)("strong",{parentName:"a"},"CitrosDB"))," is created with defaults parameters. To specify connection parameters, pass corresponding arguments:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> citros = CitrosDB()\n")),(0,r.kt)("p",null,"Data is always queried for the exact ",(0,r.kt)("em",{parentName:"p"},"topic"),"; you also need to know the names of the ",(0,r.kt)("em",{parentName:"p"},"batch")," and ",(0,r.kt)("em",{parentName:"p"},"simulation"),".\nFor example, to query all data for topic 'A' from the batch 'batch_name', created by simulation 'simulation_name':"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> df = citros.simulation('simulation_name').batch('batch_name').topic('A').data()\n>>> print(df)\n")),(0,r.kt)("details",null,(0,r.kt)("summary",null,"Show the result:"),(0,r.kt)("table",null,(0,r.kt)("thead",{parentName:"table"},(0,r.kt)("tr",{parentName:"thead"},(0,r.kt)("th",{parentName:"tr",align:null}),(0,r.kt)("th",{parentName:"tr",align:null},"sid"),(0,r.kt)("th",{parentName:"tr",align:null},"rid"),(0,r.kt)("th",{parentName:"tr",align:null},"time"),(0,r.kt)("th",{parentName:"tr",align:null},"topic"),(0,r.kt)("th",{parentName:"tr",align:null},"type"),(0,r.kt)("th",{parentName:"tr",align:null},"data.x.x_1"),(0,r.kt)("th",{parentName:"tr",align:null},"data.x.x_2"),(0,r.kt)("th",{parentName:"tr",align:null},"data.x.x_3"),(0,r.kt)("th",{parentName:"tr",align:null},"data.time"),(0,r.kt)("th",{parentName:"tr",align:null},"data.time"),(0,r.kt)("th",{parentName:"tr",align:null},"data.y"))),(0,r.kt)("tbody",{parentName:"table"},(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"0"),(0,r.kt)("td",{parentName:"tr",align:null},"3"),(0,r.kt)("td",{parentName:"tr",align:null},"0"),(0,r.kt)("td",{parentName:"tr",align:null},"105036927"),(0,r.kt)("td",{parentName:"tr",align:null},"A"),(0,r.kt)("td",{parentName:"tr",align:null},"a"),(0,r.kt)("td",{parentName:"tr",align:null},"-0.080"),(0,r.kt)("td",{parentName:"tr",align:null},"-0.002"),(0,r.kt)("td",{parentName:"tr",align:null},"17.70"),(0,r.kt)("td",{parentName:"tr",align:null},"0.3"),(0,r.kt)("td",{parentName:"tr",align:null},"0.3"),(0,r.kt)("td",{parentName:"tr",align:null},"[2, 28, 45]")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"1"),(0,r.kt)("td",{parentName:"tr",align:null},"1"),(0,r.kt)("td",{parentName:"tr",align:null},"0"),(0,r.kt)("td",{parentName:"tr",align:null},"312751159"),(0,r.kt)("td",{parentName:"tr",align:null},"A"),(0,r.kt)("td",{parentName:"tr",align:null},"a"),(0,r.kt)("td",{parentName:"tr",align:null},"0.000"),(0,r.kt)("td",{parentName:"tr",align:null},"0.080"),(0,r.kt)("td",{parentName:"tr",align:null},"154.47"),(0,r.kt)("td",{parentName:"tr",align:null},"10.0"),(0,r.kt)("td",{parentName:"tr",align:null},"10.0"),(0,r.kt)("td",{parentName:"tr",align:null},"[15, 41, 43]")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"..."),(0,r.kt)("td",{parentName:"tr",align:null},"..."),(0,r.kt)("td",{parentName:"tr",align:null},"..."),(0,r.kt)("td",{parentName:"tr",align:null},"..."),(0,r.kt)("td",{parentName:"tr",align:null},"..."),(0,r.kt)("td",{parentName:"tr",align:null},"..."),(0,r.kt)("td",{parentName:"tr",align:null},"..."),(0,r.kt)("td",{parentName:"tr",align:null},"..."),(0,r.kt)("td",{parentName:"tr",align:null},"..."),(0,r.kt)("td",{parentName:"tr",align:null},"..."),(0,r.kt)("td",{parentName:"tr",align:null},"..."),(0,r.kt)("td",{parentName:"tr",align:null},"..."))))),(0,r.kt)("p",null,"The result is a ",(0,r.kt)("a",{parentName:"p",href:"https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html"},(0,r.kt)("strong",{parentName:"a"},"DataFrame"))," of the ",(0,r.kt)("a",{parentName:"p",href:"https://pandas.pydata.org/"},(0,r.kt)("strong",{parentName:"a"},"pandas")," package"),"."),(0,r.kt)("p",null,"Batch consists of two parts: json-data column, and all other columns.\nTo query exact json-objects, pass list with their labels to ",(0,r.kt)("a",{parentName:"p",href:"/docs/0.2.49/data_analysis/documentation/access/citros_db#access.citros_db.CitrosDB.data"},(0,r.kt)("strong",{parentName:"a"},"data()")),".\nFor example, if the json-data column looks like:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-js"},"data\n{'x': {'x_1' : 1, 'x_2' : 12, 'x_3' : 70}, 'y': [5.0, 3.4, 10], 'height' : 12}\n{'x': {'x_1' : 5, 'x_2' : 10, 'x_3' : 73}, 'y': [5.5, 6.7, 50], 'height' : 11}\n...\n")),(0,r.kt)("p",null,"to query 'x_1', 'x_2', 'height' and values from the first position of 'y' json-array, the following code may be used:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> df = citros.topic('A').data(['data.x.x_1', 'data.x.x_2', 'data.height', 'data.y[0]'])\n")),(0,r.kt)("p",null,"Also, different constraints may be applied to query, see ",(0,r.kt)("a",{parentName:"p",href:"../data_access/"},"examples"),"."))}c.isMDXComponent=!0}}]);
"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[90911],{3905:(e,t,n)=>{n.d(t,{Zo:()=>d,kt:()=>f});var r=n(67294);function o(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function a(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function i(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?a(Object(n),!0).forEach((function(t){o(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):a(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function c(e,t){if(null==e)return{};var n,r,o=function(e,t){if(null==e)return{};var n,r,o={},a=Object.keys(e);for(r=0;r<a.length;r++)n=a[r],t.indexOf(n)>=0||(o[n]=e[n]);return o}(e,t);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);for(r=0;r<a.length;r++)n=a[r],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(o[n]=e[n])}return o}var l=r.createContext({}),m=function(e){var t=r.useContext(l),n=t;return e&&(n="function"==typeof e?e(t):i(i({},t),e)),n},d=function(e){var t=m(e.components);return r.createElement(l.Provider,{value:t},e.children)},s="mdxType",p={inlineCode:"code",wrapper:function(e){var t=e.children;return r.createElement(r.Fragment,{},t)}},u=r.forwardRef((function(e,t){var n=e.components,o=e.mdxType,a=e.originalType,l=e.parentName,d=c(e,["components","mdxType","originalType","parentName"]),s=m(n),u=o,f=s["".concat(l,".").concat(u)]||s[u]||p[u]||a;return n?r.createElement(f,i(i({ref:t},d),{},{components:n})):r.createElement(f,i({ref:t},d))}));function f(e,t){var n=arguments,o=t&&t.mdxType;if("string"==typeof e||o){var a=n.length,i=new Array(a);i[0]=u;var c={};for(var l in t)hasOwnProperty.call(t,l)&&(c[l]=t[l]);c.originalType=e,c[s]="string"==typeof e?e:o,i[1]=c;for(var m=2;m<a;m++)i[m]=n[m];return r.createElement.apply(null,i)}return r.createElement.apply(null,n)}u.displayName="MDXCreateElement"},40200:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>l,contentTitle:()=>i,default:()=>p,frontMatter:()=>a,metadata:()=>c,toc:()=>m});var r=n(87462),o=(n(67294),n(3905));const a={},i="Commands Overview",c={unversionedId:"commands/overview",id:"version-0.2.56/commands/overview",title:"Commands Overview",description:"CITROS commands are...",source:"@site/versioned_docs/version-0.2.56/commands/overview.md",sourceDirName:"commands",slug:"/commands/overview",permalink:"/docs/0.2.56/commands/overview",draft:!1,tags:[],version:"0.2.56",frontMatter:{},sidebar:"gettingStartedSidebar",previous:{title:"Installation",permalink:"/docs/0.2.56/general/install"},next:{title:"citros init",permalink:"/docs/0.2.56/commands/init"}},l={},m=[{value:"Init",id:"init",level:4},{value:"Run",id:"run",level:4},{value:"Data",id:"data",level:4},{value:"Report",id:"report",level:4}],d={toc:m},s="wrapper";function p(e){let{components:t,...n}=e;return(0,o.kt)(s,(0,r.Z)({},d,n,{components:t,mdxType:"MDXLayout"}),(0,o.kt)("h1",{id:"commands-overview"},"Commands Overview"),(0,o.kt)("p",null,"CITROS commands are..."),(0,o.kt)("p",null,"The commands can be written as an explicit CLI command or used as an interactive mode.\nin any case you have trouble remembering what options you have for the command, just run the command and ADD -h for help."),(0,o.kt)("p",null,"The main commands categories, are divided as follows:"),(0,o.kt)("h4",{id:"init"},"Init"),(0,o.kt)("p",null,"Command used to init your .citros directory.\nFor more information about the command go to the ",(0,o.kt)("a",{parentName:"p",href:"../commands/init"},"init command")," page"),(0,o.kt)("h4",{id:"run"},"Run"),(0,o.kt)("p",null,"Command used to run batch simulation of your ROS2 project.\nFor more information about the command go to the ",(0,o.kt)("a",{parentName:"p",href:"../commands/run"},"run command")," page"),(0,o.kt)("h4",{id:"data"},"Data"),(0,o.kt)("p",null,"Commands collection to all data related functionality. "),(0,o.kt)("h4",{id:"report"},"Report"),(0,o.kt)("p",null,"CITROS report is a collection of ",(0,o.kt)("inlineCode",{parentName:"p"},"data from a batch of simulations")," and a ",(0,o.kt)("inlineCode",{parentName:"p"},"set of notebooks")," that renders into a ",(0,o.kt)("inlineCode",{parentName:"p"},"signed pdf")," report that can be shared. "),(0,o.kt)("p",null,"In this section you can list all the generated report under ",(0,o.kt)("inlineCode",{parentName:"p"},".citros/report")," folder, you can ",(0,o.kt)("inlineCode",{parentName:"p"},"generate")," a new report or ",(0,o.kt)("inlineCode",{parentName:"p"},"validate")," an existing one."))}p.isMDXComponent=!0}}]);
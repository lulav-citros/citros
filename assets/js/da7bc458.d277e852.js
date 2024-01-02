"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[8846],{3905:(e,t,r)=>{r.d(t,{Zo:()=>d,kt:()=>m});var n=r(7294);function a(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function o(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function c(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?o(Object(r),!0).forEach((function(t){a(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):o(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function i(e,t){if(null==e)return{};var r,n,a=function(e,t){if(null==e)return{};var r,n,a={},o=Object.keys(e);for(n=0;n<o.length;n++)r=o[n],t.indexOf(r)>=0||(a[r]=e[r]);return a}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(n=0;n<o.length;n++)r=o[n],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(a[r]=e[r])}return a}var l=n.createContext({}),s=function(e){var t=n.useContext(l),r=t;return e&&(r="function"==typeof e?e(t):c(c({},t),e)),r},d=function(e){var t=s(e.components);return n.createElement(l.Provider,{value:t},e.children)},u="mdxType",p={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},f=n.forwardRef((function(e,t){var r=e.components,a=e.mdxType,o=e.originalType,l=e.parentName,d=i(e,["components","mdxType","originalType","parentName"]),u=s(r),f=a,m=u["".concat(l,".").concat(f)]||u[f]||p[f]||o;return r?n.createElement(m,c(c({ref:t},d),{},{components:r})):n.createElement(m,c({ref:t},d))}));function m(e,t){var r=arguments,a=t&&t.mdxType;if("string"==typeof e||a){var o=r.length,c=new Array(o);c[0]=f;var i={};for(var l in t)hasOwnProperty.call(t,l)&&(i[l]=t[l]);i.originalType=e,i[u]="string"==typeof e?e:a,c[1]=i;for(var s=2;s<o;s++)c[s]=r[s];return n.createElement.apply(null,c)}return n.createElement.apply(null,r)}f.displayName="MDXCreateElement"},3645:(e,t,r)=>{r.r(t),r.d(t,{assets:()=>l,contentTitle:()=>c,default:()=>p,frontMatter:()=>o,metadata:()=>i,toc:()=>s});var n=r(7462),a=(r(7294),r(3905));const o={},c=void 0,i={unversionedId:"cli/commands/data",id:"cli/commands/data",title:"data",description:"citros data",source:"@site/docs/cli/commands/data.md",sourceDirName:"cli/commands",slug:"/cli/commands/data",permalink:"/docs/cli/commands/data",draft:!1,tags:[],version:"current",frontMatter:{}},l={},s=[{value:"<code>citros data</code>",id:"citros-data",level:2},{value:"list",id:"list",level:3},{value:"service",id:"service",level:3},{value:"DB",id:"db",level:3}],d={toc:s},u="wrapper";function p(e){let{components:t,...r}=e;return(0,a.kt)(u,(0,n.Z)({},d,r,{components:t,mdxType:"MDXLayout"}),(0,a.kt)("h2",{id:"citros-data"},(0,a.kt)("inlineCode",{parentName:"h2"},"citros data")),(0,a.kt)("p",null,"This section contain all data related functionality"),(0,a.kt)("h3",{id:"list"},"list"),(0,a.kt)("p",null,"Will list all recorded batches under ",(0,a.kt)("inlineCode",{parentName:"p"},".citros/data")," folder"),(0,a.kt)("h3",{id:"service"},"service"),(0,a.kt)("p",null,"This section controls citros data service that that exposes data/report using REST API"),(0,a.kt)("h3",{id:"db"},"DB"),(0,a.kt)("p",null,"We use postgres DB to cash batch data for fast quering. This section cintrols citros DB functionality."))}p.isMDXComponent=!0}}]);
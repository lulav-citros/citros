"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[49850],{3905:(e,t,r)=>{r.d(t,{Zo:()=>d,kt:()=>m});var n=r(67294);function o(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function a(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function i(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?a(Object(r),!0).forEach((function(t){o(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):a(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function c(e,t){if(null==e)return{};var r,n,o=function(e,t){if(null==e)return{};var r,n,o={},a=Object.keys(e);for(n=0;n<a.length;n++)r=a[n],t.indexOf(r)>=0||(o[r]=e[r]);return o}(e,t);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);for(n=0;n<a.length;n++)r=a[n],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(o[r]=e[r])}return o}var l=n.createContext({}),s=function(e){var t=n.useContext(l),r=t;return e&&(r="function"==typeof e?e(t):i(i({},t),e)),r},d=function(e){var t=s(e.components);return n.createElement(l.Provider,{value:t},e.children)},p="mdxType",u={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},f=n.forwardRef((function(e,t){var r=e.components,o=e.mdxType,a=e.originalType,l=e.parentName,d=c(e,["components","mdxType","originalType","parentName"]),p=s(r),f=o,m=p["".concat(l,".").concat(f)]||p[f]||u[f]||a;return r?n.createElement(m,i(i({ref:t},d),{},{components:r})):n.createElement(m,i({ref:t},d))}));function m(e,t){var r=arguments,o=t&&t.mdxType;if("string"==typeof e||o){var a=r.length,i=new Array(a);i[0]=f;var c={};for(var l in t)hasOwnProperty.call(t,l)&&(c[l]=t[l]);c.originalType=e,c[p]="string"==typeof e?e:o,i[1]=c;for(var s=2;s<a;s++)i[s]=r[s];return n.createElement.apply(null,i)}return n.createElement.apply(null,r)}f.displayName="MDXCreateElement"},66416:(e,t,r)=>{r.r(t),r.d(t,{assets:()=>l,contentTitle:()=>i,default:()=>u,frontMatter:()=>a,metadata:()=>c,toc:()=>s});var n=r(87462),o=(r(67294),r(3905));const a={},i=void 0,c={unversionedId:"commands/cli/data",id:"version-0.2.39/commands/cli/data",title:"data",description:"citros data",source:"@site/versioned_docs/version-0.2.39/commands/cli/data.md",sourceDirName:"commands/cli",slug:"/commands/cli/data",permalink:"/docs/0.2.39/commands/cli/data",draft:!1,tags:[],version:"0.2.39",frontMatter:{}},l={},s=[{value:"<code>citros data</code>",id:"citros-data",level:2},{value:"list",id:"list",level:3},{value:"service",id:"service",level:3},{value:"DB",id:"db",level:3}],d={toc:s},p="wrapper";function u(e){let{components:t,...r}=e;return(0,o.kt)(p,(0,n.Z)({},d,r,{components:t,mdxType:"MDXLayout"}),(0,o.kt)("h2",{id:"citros-data"},(0,o.kt)("inlineCode",{parentName:"h2"},"citros data")),(0,o.kt)("p",null,"This section contain all data related functionality"),(0,o.kt)("h3",{id:"list"},"list"),(0,o.kt)("p",null,"Will list all recorded batches under ",(0,o.kt)("inlineCode",{parentName:"p"},".citros/data")," folder"),(0,o.kt)("h3",{id:"service"},"service"),(0,o.kt)("p",null,"This section controls citros data service that that exposes data/report using REST API"),(0,o.kt)("h3",{id:"db"},"DB"),(0,o.kt)("p",null,"We use postgres DB to cash batch data for fast quering. This section cintrols citros DB functionality."))}u.isMDXComponent=!0}}]);
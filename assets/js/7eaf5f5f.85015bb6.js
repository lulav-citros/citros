"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[82389],{3905:(e,t,r)=>{r.d(t,{Zo:()=>u,kt:()=>m});var n=r(67294);function o(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function a(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function i(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?a(Object(r),!0).forEach((function(t){o(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):a(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function c(e,t){if(null==e)return{};var r,n,o=function(e,t){if(null==e)return{};var r,n,o={},a=Object.keys(e);for(n=0;n<a.length;n++)r=a[n],t.indexOf(r)>=0||(o[r]=e[r]);return o}(e,t);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);for(n=0;n<a.length;n++)r=a[n],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(o[r]=e[r])}return o}var s=n.createContext({}),l=function(e){var t=n.useContext(s),r=t;return e&&(r="function"==typeof e?e(t):i(i({},t),e)),r},u=function(e){var t=l(e.components);return n.createElement(s.Provider,{value:t},e.children)},p="mdxType",f={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},d=n.forwardRef((function(e,t){var r=e.components,o=e.mdxType,a=e.originalType,s=e.parentName,u=c(e,["components","mdxType","originalType","parentName"]),p=l(r),d=o,m=p["".concat(s,".").concat(d)]||p[d]||f[d]||a;return r?n.createElement(m,i(i({ref:t},u),{},{components:r})):n.createElement(m,i({ref:t},u))}));function m(e,t){var r=arguments,o=t&&t.mdxType;if("string"==typeof e||o){var a=r.length,i=new Array(a);i[0]=d;var c={};for(var s in t)hasOwnProperty.call(t,s)&&(c[s]=t[s]);c.originalType=e,c[p]="string"==typeof e?e:o,i[1]=c;for(var l=2;l<a;l++)i[l]=r[l];return n.createElement.apply(null,i)}return n.createElement.apply(null,r)}d.displayName="MDXCreateElement"},62623:(e,t,r)=>{r.r(t),r.d(t,{assets:()=>s,contentTitle:()=>i,default:()=>f,frontMatter:()=>a,metadata:()=>c,toc:()=>l});var n=r(87462),o=(r(67294),r(3905));const a={},i="CLI Overview",c={unversionedId:"general/overview",id:"version-0.2.43/general/overview",title:"CLI Overview",description:"Welcome to CITROS CLI. CITROS serves as an innovative platform for executing ROS project simulations, automating integration, and conducting in-depth performance analysis.",source:"@site/versioned_docs/version-0.2.43/general/overview.md",sourceDirName:"general",slug:"/general/overview",permalink:"/docs/0.2.43/general/overview",draft:!1,tags:[],version:"0.2.43",frontMatter:{},sidebar:"gettingStartedSidebar",next:{title:"Quick Start",permalink:"/docs/0.2.43/general/quickstart"}},s={},l=[],u={toc:l},p="wrapper";function f(e){let{components:t,...r}=e;return(0,o.kt)(p,(0,n.Z)({},u,r,{components:t,mdxType:"MDXLayout"}),(0,o.kt)("h1",{id:"cli-overview"},"CLI Overview"),(0,o.kt)("p",null,"Welcome to CITROS CLI. ",(0,o.kt)("a",{parentName:"p",href:"https://citros.io/"},"CITROS")," serves as an innovative platform for executing ROS project simulations, automating integration, and conducting in-depth performance analysis."),(0,o.kt)("p",null,"CITROS offers ROS 2 developers a seamless interface to launch multiple ROS simulations for a specific project with just a single command. Beyond setting static parameter values, it empowers users with the flexibility to utilize function objects. This means you can craft dynamic simulation environments where each execution produces unique parameter values, whether they're sourced from standard numpy functions or tailored via user-defined computations. "),(0,o.kt)("p",null,"After a successfull simulation runs we give the ability to investigate the recorded data using out build in ",(0,o.kt)("inlineCode",{parentName:"p"},"data analysis")," package, and after "),(0,o.kt)("p",null,"Additionally, ",(0,o.kt)("inlineCode",{parentName:"p"},"report")," generation is a standout feature, aiding in effortless documentation of your work. "),(0,o.kt)("p",null,"We are dedicated to enriching your ROS project simulation experience, and this package is our contribution to that cause."))}f.isMDXComponent=!0}}]);
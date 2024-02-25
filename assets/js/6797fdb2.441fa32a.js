"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[69219],{3905:(e,t,r)=>{r.d(t,{Zo:()=>u,kt:()=>f});var n=r(67294);function a(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function o(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function i(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?o(Object(r),!0).forEach((function(t){a(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):o(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function l(e,t){if(null==e)return{};var r,n,a=function(e,t){if(null==e)return{};var r,n,a={},o=Object.keys(e);for(n=0;n<o.length;n++)r=o[n],t.indexOf(r)>=0||(a[r]=e[r]);return a}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(n=0;n<o.length;n++)r=o[n],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(a[r]=e[r])}return a}var s=n.createContext({}),c=function(e){var t=n.useContext(s),r=t;return e&&(r="function"==typeof e?e(t):i(i({},t),e)),r},u=function(e){var t=c(e.components);return n.createElement(s.Provider,{value:t},e.children)},p="mdxType",d={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},m=n.forwardRef((function(e,t){var r=e.components,a=e.mdxType,o=e.originalType,s=e.parentName,u=l(e,["components","mdxType","originalType","parentName"]),p=c(r),m=a,f=p["".concat(s,".").concat(m)]||p[m]||d[m]||o;return r?n.createElement(f,i(i({ref:t},u),{},{components:r})):n.createElement(f,i({ref:t},u))}));function f(e,t){var r=arguments,a=t&&t.mdxType;if("string"==typeof e||a){var o=r.length,i=new Array(o);i[0]=m;var l={};for(var s in t)hasOwnProperty.call(t,s)&&(l[s]=t[s]);l.originalType=e,l[p]="string"==typeof e?e:a,i[1]=l;for(var c=2;c<o;c++)i[c]=r[c];return n.createElement.apply(null,i)}return n.createElement.apply(null,r)}m.displayName="MDXCreateElement"},14011:(e,t,r)=>{r.r(t),r.d(t,{assets:()=>s,contentTitle:()=>i,default:()=>d,frontMatter:()=>o,metadata:()=>l,toc:()=>c});var n=r(87462),a=(r(67294),r(3905));const o={},i="Quick Start",l={unversionedId:"general/quickstart",id:"version-0.2.62/general/quickstart",title:"Quick Start",description:"citros is a suilt of tools for ros2 development and production.",source:"@site/versioned_docs/version-0.2.62/general/quickstart.md",sourceDirName:"general",slug:"/general/quickstart",permalink:"/docs/0.2.62/general/quickstart",draft:!1,tags:[],version:"0.2.62",frontMatter:{},sidebar:"gettingStartedSidebar",previous:{title:"CITROS Overview",permalink:"/docs/0.2.62/general/overview"},next:{title:"Installation",permalink:"/docs/0.2.62/general/install"}},s={},c=[],u={toc:c},p="wrapper";function d(e){let{components:t,...r}=e;return(0,a.kt)(p,(0,n.Z)({},u,r,{components:t,mdxType:"MDXLayout"}),(0,a.kt)("h1",{id:"quick-start"},"Quick Start"),(0,a.kt)("p",null,"citros is a suilt of tools for ros2 development and production.\nWith this tool you can now easily run many monte carlo simulations scenarios by regenarating any of the parameters before running the simulation and then analyze the changes in the results using our built in tools."),(0,a.kt)("p",null,"to install citros"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-bash"},"pip install citros --upgrade\n")),(0,a.kt)("p",null,"go to your ros2 workspace and run citros init, this will create a ",(0,a.kt)("inlineCode",{parentName:"p"},".citros")," folder with all the required files."),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-bash"},"citros init\n")),(0,a.kt)("p",null,"start CITROS db for data indexing. you can load and unload batch runs to the db using the ",(0,a.kt)("inlineCode",{parentName:"p"},"citros data")," command."),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-bash"},"citros data db create\n")),(0,a.kt)("p",null,"to run a simulation run the following command"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-bash"},"citros run \n")),(0,a.kt)("p",null,"this will start a new batch run that will later can be used for analysis."),(0,a.kt)("p",null,"you can now access the data for analysis from any postgres client or use our tool for python data analysis.\nout python data analysis package will help you access the data and analyze it. we recoment using it from python notebook that later can be converted to a signed PDF report by running ",(0,a.kt)("inlineCode",{parentName:"p"},"citros report generate"),". "),(0,a.kt)("p",null,"to analyze the results using citros"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-bash"},"citros report generate \n")))}d.isMDXComponent=!0}}]);
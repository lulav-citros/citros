"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[2093],{3905:(e,t,n)=>{n.d(t,{Zo:()=>u,kt:()=>f});var r=n(67294);function a(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function o(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function i(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?o(Object(n),!0).forEach((function(t){a(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):o(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function l(e,t){if(null==e)return{};var n,r,a=function(e,t){if(null==e)return{};var n,r,a={},o=Object.keys(e);for(r=0;r<o.length;r++)n=o[r],t.indexOf(n)>=0||(a[n]=e[n]);return a}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(r=0;r<o.length;r++)n=o[r],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(a[n]=e[n])}return a}var s=r.createContext({}),c=function(e){var t=r.useContext(s),n=t;return e&&(n="function"==typeof e?e(t):i(i({},t),e)),n},u=function(e){var t=c(e.components);return r.createElement(s.Provider,{value:t},e.children)},p="mdxType",d={inlineCode:"code",wrapper:function(e){var t=e.children;return r.createElement(r.Fragment,{},t)}},m=r.forwardRef((function(e,t){var n=e.components,a=e.mdxType,o=e.originalType,s=e.parentName,u=l(e,["components","mdxType","originalType","parentName"]),p=c(n),m=a,f=p["".concat(s,".").concat(m)]||p[m]||d[m]||o;return n?r.createElement(f,i(i({ref:t},u),{},{components:n})):r.createElement(f,i({ref:t},u))}));function f(e,t){var n=arguments,a=t&&t.mdxType;if("string"==typeof e||a){var o=n.length,i=new Array(o);i[0]=m;var l={};for(var s in t)hasOwnProperty.call(t,s)&&(l[s]=t[s]);l.originalType=e,l[p]="string"==typeof e?e:a,i[1]=l;for(var c=2;c<o;c++)i[c]=n[c];return r.createElement.apply(null,i)}return r.createElement.apply(null,n)}m.displayName="MDXCreateElement"},57499:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>s,contentTitle:()=>i,default:()=>d,frontMatter:()=>o,metadata:()=>l,toc:()=>c});var r=n(87462),a=(n(67294),n(3905));const o={},i="Quick Start",l={unversionedId:"general/quickstart",id:"general/quickstart",title:"Quick Start",description:"citros is a suit of tools for ros2 development and production.",source:"@site/docs/general/quickstart.md",sourceDirName:"general",slug:"/general/quickstart",permalink:"/docs/next/general/quickstart",draft:!1,tags:[],version:"current",frontMatter:{},sidebar:"gettingStartedSidebar",previous:{title:"TODO VOVA - REVIEW",permalink:"/docs/next/general/overview"},next:{title:"Installation",permalink:"/docs/next/general/install"}},s={},c=[],u={toc:c},p="wrapper";function d(e){let{components:t,...n}=e;return(0,a.kt)(p,(0,r.Z)({},u,n,{components:t,mdxType:"MDXLayout"}),(0,a.kt)("h1",{id:"quick-start"},"Quick Start"),(0,a.kt)("p",null,"citros is a suit of tools for ros2 development and production.\nWith this tool you can now easily run many monte carlo simulations scenarios by regenerating any of the parameters before running the simulation and then analyze the changes in the results using our built in tools."),(0,a.kt)("p",null,"to install citros"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-bash"},"pip install citros --upgrade\n")),(0,a.kt)("p",null,"go to your ros2 workspace and run citros init, this will create a ",(0,a.kt)("inlineCode",{parentName:"p"},".citros")," folder with all the required files."),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-bash"},"citros init\n")),(0,a.kt)("p",null,"start CITROS db for data indexing. you can load and unload batch runs to the db using the ",(0,a.kt)("inlineCode",{parentName:"p"},"citros data")," command."),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-bash"},"citros data db create\n")),(0,a.kt)("p",null,"to run a simulation run the following command"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-bash"},"citros run \n")),(0,a.kt)("p",null,"this will start a new batch run that will later can be used for analysis."),(0,a.kt)("p",null,"you can now access the data for analysis from any postgres client or use our tool for python data analysis.\nout python data analysis package will help you access the data and analyze it. we recommend using it from python notebook that later can be converted to a signed PDF report by running ",(0,a.kt)("inlineCode",{parentName:"p"},"citros report generate"),". "),(0,a.kt)("p",null,"to analyze the results using citros"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-bash"},"citros report generate \n")))}d.isMDXComponent=!0}}]);
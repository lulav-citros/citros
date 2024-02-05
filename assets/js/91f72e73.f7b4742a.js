"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[88299],{3905:(e,t,n)=>{n.d(t,{Zo:()=>p,kt:()=>f});var r=n(67294);function i(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function o(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function a(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?o(Object(n),!0).forEach((function(t){i(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):o(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function c(e,t){if(null==e)return{};var n,r,i=function(e,t){if(null==e)return{};var n,r,i={},o=Object.keys(e);for(r=0;r<o.length;r++)n=o[r],t.indexOf(n)>=0||(i[n]=e[n]);return i}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(r=0;r<o.length;r++)n=o[r],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(i[n]=e[n])}return i}var l=r.createContext({}),s=function(e){var t=r.useContext(l),n=t;return e&&(n="function"==typeof e?e(t):a(a({},t),e)),n},p=function(e){var t=s(e.components);return r.createElement(l.Provider,{value:t},e.children)},u="mdxType",d={inlineCode:"code",wrapper:function(e){var t=e.children;return r.createElement(r.Fragment,{},t)}},m=r.forwardRef((function(e,t){var n=e.components,i=e.mdxType,o=e.originalType,l=e.parentName,p=c(e,["components","mdxType","originalType","parentName"]),u=s(n),m=i,f=u["".concat(l,".").concat(m)]||u[m]||d[m]||o;return n?r.createElement(f,a(a({ref:t},p),{},{components:n})):r.createElement(f,a({ref:t},p))}));function f(e,t){var n=arguments,i=t&&t.mdxType;if("string"==typeof e||i){var o=n.length,a=new Array(o);a[0]=m;var c={};for(var l in t)hasOwnProperty.call(t,l)&&(c[l]=t[l]);c.originalType=e,c[u]="string"==typeof e?e:i,a[1]=c;for(var s=2;s<o;s++)a[s]=n[s];return r.createElement.apply(null,a)}return r.createElement.apply(null,n)}m.displayName="MDXCreateElement"},52627:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>l,contentTitle:()=>a,default:()=>d,frontMatter:()=>o,metadata:()=>c,toc:()=>s});var r=n(87462),i=(n(67294),n(3905));const o={},a=void 0,c={unversionedId:"commands/init",id:"version-0.2.18/commands/init",title:"init",description:"citros init",source:"@site/versioned_docs/version-0.2.18/commands/init.md",sourceDirName:"commands",slug:"/commands/init",permalink:"/docs/0.2.18/commands/init",draft:!1,tags:[],version:"0.2.18",frontMatter:{},sidebar:"gettingStartedSidebar",previous:{title:"Installation",permalink:"/docs/0.2.18/general/install"},next:{title:"launch",permalink:"/docs/0.2.18/commands/launch"}},l={},s=[{value:"<code>citros init</code>",id:"citros-init",level:2},{value:"Description",id:"description",level:3},{value:"Example:",id:"example",level:3}],p={toc:s},u="wrapper";function d(e){let{components:t,...n}=e;return(0,i.kt)(u,(0,r.Z)({},p,n,{components:t,mdxType:"MDXLayout"}),(0,i.kt)("h2",{id:"citros-init"},(0,i.kt)("inlineCode",{parentName:"h2"},"citros init")),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sh"},"$ citros init [-dir <folder_name>] \n              [-d | --debug] \n              [-v | --verbose]               \n")),(0,i.kt)("h3",{id:"description"},"Description"),(0,i.kt)("p",null,"The ",(0,i.kt)("inlineCode",{parentName:"p"},"init")," command is used to initialize a CITROS repository idempotently. "),(0,i.kt)("p",null,"The initialization process involves creating a ",(0,i.kt)("inlineCode",{parentName:"p"},".citros")," directory within your ROS project directory and generating several files and folders therein. These files are set up to allow you to run a simulation of your project with default configurations and settings. You can tailor your CITROS repository to your specific needs by manually modifying these files (see the Project Configuration section for more details)."),(0,i.kt)("p",null,(0,i.kt)("strong",{parentName:"p"},"Idempotence")," means that no matter how many times you execute it the init command, you achieve the same result."),(0,i.kt)("h3",{id:"example"},"Example:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-bash"},'$ citros init\ninitializing CITROS at "/path/to/ros2/project". \n')))}d.isMDXComponent=!0}}]);
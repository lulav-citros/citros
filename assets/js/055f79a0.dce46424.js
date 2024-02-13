"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[14159],{3905:(e,t,n)=>{n.d(t,{Zo:()=>p,kt:()=>g});var r=n(67294);function a(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function i(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function o(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?i(Object(n),!0).forEach((function(t){a(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):i(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function l(e,t){if(null==e)return{};var n,r,a=function(e,t){if(null==e)return{};var n,r,a={},i=Object.keys(e);for(r=0;r<i.length;r++)n=i[r],t.indexOf(n)>=0||(a[n]=e[n]);return a}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(r=0;r<i.length;r++)n=i[r],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(a[n]=e[n])}return a}var c=r.createContext({}),s=function(e){var t=r.useContext(c),n=t;return e&&(n="function"==typeof e?e(t):o(o({},t),e)),n},p=function(e){var t=s(e.components);return r.createElement(c.Provider,{value:t},e.children)},m="mdxType",d={inlineCode:"code",wrapper:function(e){var t=e.children;return r.createElement(r.Fragment,{},t)}},u=r.forwardRef((function(e,t){var n=e.components,a=e.mdxType,i=e.originalType,c=e.parentName,p=l(e,["components","mdxType","originalType","parentName"]),m=s(n),u=a,g=m["".concat(c,".").concat(u)]||m[u]||d[u]||i;return n?r.createElement(g,o(o({ref:t},p),{},{components:n})):r.createElement(g,o({ref:t},p))}));function g(e,t){var n=arguments,a=t&&t.mdxType;if("string"==typeof e||a){var i=n.length,o=new Array(i);o[0]=u;var l={};for(var c in t)hasOwnProperty.call(t,c)&&(l[c]=t[c]);l.originalType=e,l[m]="string"==typeof e?e:a,o[1]=l;for(var s=2;s<i;s++)o[s]=n[s];return r.createElement.apply(null,o)}return r.createElement.apply(null,n)}u.displayName="MDXCreateElement"},86700:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>c,contentTitle:()=>o,default:()=>d,frontMatter:()=>i,metadata:()=>l,toc:()=>s});var r=n(87462),a=(n(67294),n(3905));const i={sidebar_label:"citros init"},o="citros init",l={unversionedId:"commands/init",id:"version-0.2.47/commands/init",title:"citros init",description:"Description",source:"@site/versioned_docs/version-0.2.47/commands/init.md",sourceDirName:"commands",slug:"/commands/init",permalink:"/docs/0.2.47/commands/init",draft:!1,tags:[],version:"0.2.47",frontMatter:{sidebar_label:"citros init"},sidebar:"gettingStartedSidebar",previous:{title:"Installation",permalink:"/docs/0.2.47/general/install"},next:{title:"citros run",permalink:"/docs/0.2.47/commands/run"}},c={},s=[{value:"Description",id:"description",level:2},{value:"Options",id:"options",level:2},{value:"Example",id:"example",level:2},{value:"Interactive Mode",id:"interactive-mode",level:2}],p={toc:s},m="wrapper";function d(e){let{components:t,...n}=e;return(0,a.kt)(m,(0,r.Z)({},p,n,{components:t,mdxType:"MDXLayout"}),(0,a.kt)("h1",{id:"citros-init"},(0,a.kt)("inlineCode",{parentName:"h1"},"citros init")),(0,a.kt)("h2",{id:"description"},"Description"),(0,a.kt)("p",null,"The ",(0,a.kt)("inlineCode",{parentName:"p"},"init")," command is used to initialize a CITROS repository  in an idempotent way. "),(0,a.kt)("p",null,"The initialization process involves creating a ",(0,a.kt)("inlineCode",{parentName:"p"},".citros")," directory within your ROS project directory and generating several files and folders therein. These files are set up to allow you to run a simulation of your project with default configurations and settings. You can tailor your CITROS repository to your specific needs by manually modifying these files (see the Project Configuration section for more details)."),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-bash"},"$ citros init [-h] [-dir DIR] [-d] [-v]\n")),(0,a.kt)("p",null,(0,a.kt)("strong",{parentName:"p"},"*Idempotence"),"\n*",(0,a.kt)("em",{parentName:"p"},"means that no matter how many times you execute it the ",(0,a.kt)("inlineCode",{parentName:"em"},"init")," command, you achieve the same result.")),(0,a.kt)("h2",{id:"options"},"Options"),(0,a.kt)("table",null,(0,a.kt)("thead",{parentName:"table"},(0,a.kt)("tr",{parentName:"thead"},(0,a.kt)("th",{parentName:"tr",align:null},"Option"),(0,a.kt)("th",{parentName:"tr",align:null},"Description"))),(0,a.kt)("tbody",{parentName:"table"},(0,a.kt)("tr",{parentName:"tbody"},(0,a.kt)("td",{parentName:"tr",align:null},"-h, --help"),(0,a.kt)("td",{parentName:"tr",align:null},"Show help message")),(0,a.kt)("tr",{parentName:"tbody"},(0,a.kt)("td",{parentName:"tr",align:null},"-dir DIR"),(0,a.kt)("td",{parentName:"tr",align:null},"The working dir of the project")),(0,a.kt)("tr",{parentName:"tbody"},(0,a.kt)("td",{parentName:"tr",align:null},"-d, --debug"),(0,a.kt)("td",{parentName:"tr",align:null},"Set logging level to debug")),(0,a.kt)("tr",{parentName:"tbody"},(0,a.kt)("td",{parentName:"tr",align:null},"-v, --verbose"),(0,a.kt)("td",{parentName:"tr",align:null},"Use verbose console prints")))),(0,a.kt)("h2",{id:"example"},"Example"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-bash"},'$ citros init\ninitializing CITROS at ["path to ros2 project"]. \n')),(0,a.kt)("h2",{id:"interactive-mode"},"Interactive Mode"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-bash"},"$ citros\n")),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-sh"},"? Select Action: \n\u250c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510\n\u2502\u276f Init: initialize .citros in current directory                                     \u2502\n\u2502  Run: new simulation                                                               \u2502\n\u2502  Data: for data management                                                         \u2502\n\u2502  Report: generation and management                                                 \u2502\n\u2502  ---------------                                                                   \u2502\n\u2502  EXIT                                                                              \u2502\n\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518\n")),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-sh"},'? Select Action: Init: initialize .citros in current directory\ninitializing CITROS at ["path to ros2 project"]. \n')))}d.isMDXComponent=!0}}]);
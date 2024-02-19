"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[18236],{3905:(e,t,r)=>{r.d(t,{Zo:()=>u,kt:()=>f});var o=r(67294);function a(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function n(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);t&&(o=o.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,o)}return r}function i(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?n(Object(r),!0).forEach((function(t){a(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):n(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function l(e,t){if(null==e)return{};var r,o,a=function(e,t){if(null==e)return{};var r,o,a={},n=Object.keys(e);for(o=0;o<n.length;o++)r=n[o],t.indexOf(r)>=0||(a[r]=e[r]);return a}(e,t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);for(o=0;o<n.length;o++)r=n[o],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(a[r]=e[r])}return a}var s=o.createContext({}),c=function(e){var t=o.useContext(s),r=t;return e&&(r="function"==typeof e?e(t):i(i({},t),e)),r},u=function(e){var t=c(e.components);return o.createElement(s.Provider,{value:t},e.children)},p="mdxType",d={inlineCode:"code",wrapper:function(e){var t=e.children;return o.createElement(o.Fragment,{},t)}},m=o.forwardRef((function(e,t){var r=e.components,a=e.mdxType,n=e.originalType,s=e.parentName,u=l(e,["components","mdxType","originalType","parentName"]),p=c(r),m=a,f=p["".concat(s,".").concat(m)]||p[m]||d[m]||n;return r?o.createElement(f,i(i({ref:t},u),{},{components:r})):o.createElement(f,i({ref:t},u))}));function f(e,t){var r=arguments,a=t&&t.mdxType;if("string"==typeof e||a){var n=r.length,i=new Array(n);i[0]=m;var l={};for(var s in t)hasOwnProperty.call(t,s)&&(l[s]=t[s]);l.originalType=e,l[p]="string"==typeof e?e:a,i[1]=l;for(var c=2;c<n;c++)i[c]=r[c];return o.createElement.apply(null,i)}return o.createElement.apply(null,r)}m.displayName="MDXCreateElement"},4850:(e,t,r)=>{r.r(t),r.d(t,{assets:()=>s,contentTitle:()=>i,default:()=>d,frontMatter:()=>n,metadata:()=>l,toc:()=>c});var o=r(87462),a=(r(67294),r(3905));const n={},i="WHAT IS CITROS",l={unversionedId:"advanced_guides/citros_overview",id:"version-0.2.57/advanced_guides/citros_overview",title:"WHAT IS CITROS",description:"As described int the overview, CITROS is a platform that offers a wide range of tools to help you develop and test your ROS2 projects.",source:"@site/versioned_docs/version-0.2.57/advanced_guides/citros_overview.md",sourceDirName:"advanced_guides",slug:"/advanced_guides/citros_overview",permalink:"/docs/0.2.57/advanced_guides/citros_overview",draft:!1,tags:[],version:"0.2.57",frontMatter:{},sidebar:"gettingStartedSidebar",previous:{title:"Visualize with Foxglove",permalink:"/docs/0.2.57/guides/foxglove_visual"},next:{title:".CITROS File Structure",permalink:"/docs/0.2.57/advanced_guides/citros_structure"}},s={},c=[{value:"Components",id:"components",level:2},{value:"Flow Diagram",id:"flow-diagram",level:2}],u={toc:c},p="wrapper";function d(e){let{components:t,...n}=e;return(0,a.kt)(p,(0,o.Z)({},u,n,{components:t,mdxType:"MDXLayout"}),(0,a.kt)("h1",{id:"what-is-citros"},"WHAT IS ",(0,a.kt)("inlineCode",{parentName:"h1"},"CITROS")),(0,a.kt)("p",null,"As described int the overview, ",(0,a.kt)("inlineCode",{parentName:"p"},"CITROS")," is a platform that offers a wide range of tools to help you develop and test your ROS2 projects.\nHere we will go over all the citros components and see how they work together to provide a seamless experience for the user."),(0,a.kt)("h2",{id:"components"},"Components"),(0,a.kt)("ul",null,(0,a.kt)("li",{parentName:"ul"},"ROS2 project",(0,a.kt)("ul",{parentName:"li"},(0,a.kt)("li",{parentName:"ul"},"We will use the ",(0,a.kt)("inlineCode",{parentName:"li"},"citros")," cli to run the project"),(0,a.kt)("li",{parentName:"ul"},"When you run ",(0,a.kt)("inlineCode",{parentName:"li"},"citros init")," command, citros will extract all the ROS2 components for future use and create a ",(0,a.kt)("inlineCode",{parentName:"li"},".citros")," directory in your project root directory. the ",(0,a.kt)("a",{parentName:"li",href:"/docs/0.2.57/advanced_guides/citros_structure"},(0,a.kt)("inlineCode",{parentName:"a"},".citros"))," directory will be initiated with defaults so that you can stat right away. "),(0,a.kt)("li",{parentName:"ul"},"when you run your ros2 project with citros, citros will record all the data from all the topics and dave it to the ",(0,a.kt)("inlineCode",{parentName:"li"},".citros/data")," directory for future use. "))),(0,a.kt)("li",{parentName:"ul"},(0,a.kt)("a",{parentName:"li",href:"../advanced_guides/citros_structure"},".citros foder")),(0,a.kt)("li",{parentName:"ul"},"DB",(0,a.kt)("ul",{parentName:"li"},(0,a.kt)("li",{parentName:"ul"},"citros use portgres Db to load all the info into for fast query of the data for anakysis."),(0,a.kt)("li",{parentName:"ul"},"citros provides all the functionality to manage the DB if you dont want the hussle of setting up the DB yourself, just run ",(0,a.kt)("inlineCode",{parentName:"li"},"citros data db create")," and you are good to go."))),(0,a.kt)("li",{parentName:"ul"},(0,a.kt)("a",{parentName:"li",href:"../data_analysis/"},"Data Analysis package")),(0,a.kt)("li",{parentName:"ul"},"Report",(0,a.kt)("ul",{parentName:"li"},(0,a.kt)("li",{parentName:"ul"},"After you have anaklysed your data with python notebook, you can generate a report with the ",(0,a.kt)("inlineCode",{parentName:"li"},"citros report")," command."),(0,a.kt)("li",{parentName:"ul"},"The Python notebook is ray with pytest to generate a test report out of the notebook."),(0,a.kt)("li",{parentName:"ul"},"A pdf file is generated with the test report and the notebook.")))),(0,a.kt)("h2",{id:"flow-diagram"},"Flow Diagram"),(0,a.kt)("p",null,(0,a.kt)("img",{alt:"Alt text",src:r(41830).Z,width:"1692",height:"764"})))}d.isMDXComponent=!0},41830:(e,t,r)=>{r.d(t,{Z:()=>o});const o=r.p+"assets/images/image-4cf29116349fa9ee181be65753535f03.png"}}]);
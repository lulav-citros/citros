"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[86388],{3905:(e,t,n)=>{n.d(t,{Zo:()=>c,kt:()=>m});var o=n(67294);function r(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function a(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);t&&(o=o.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,o)}return n}function i(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?a(Object(n),!0).forEach((function(t){r(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):a(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function l(e,t){if(null==e)return{};var n,o,r=function(e,t){if(null==e)return{};var n,o,r={},a=Object.keys(e);for(o=0;o<a.length;o++)n=a[o],t.indexOf(n)>=0||(r[n]=e[n]);return r}(e,t);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);for(o=0;o<a.length;o++)n=a[o],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(r[n]=e[n])}return r}var p=o.createContext({}),s=function(e){var t=o.useContext(p),n=t;return e&&(n="function"==typeof e?e(t):i(i({},t),e)),n},c=function(e){var t=s(e.components);return o.createElement(p.Provider,{value:t},e.children)},u="mdxType",d={inlineCode:"code",wrapper:function(e){var t=e.children;return o.createElement(o.Fragment,{},t)}},g=o.forwardRef((function(e,t){var n=e.components,r=e.mdxType,a=e.originalType,p=e.parentName,c=l(e,["components","mdxType","originalType","parentName"]),u=s(n),g=r,m=u["".concat(p,".").concat(g)]||u[g]||d[g]||a;return n?o.createElement(m,i(i({ref:t},c),{},{components:n})):o.createElement(m,i({ref:t},c))}));function m(e,t){var n=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var a=n.length,i=new Array(a);i[0]=g;var l={};for(var p in t)hasOwnProperty.call(t,p)&&(l[p]=t[p]);l.originalType=e,l[u]="string"==typeof e?e:r,i[1]=l;for(var s=2;s<a;s++)i[s]=n[s];return o.createElement.apply(null,i)}return o.createElement.apply(null,n)}g.displayName="MDXCreateElement"},61970:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>p,contentTitle:()=>i,default:()=>d,frontMatter:()=>a,metadata:()=>l,toc:()=>s});var o=n(87462),r=(n(67294),n(3905));const a={sidebar_label:"Visualize with Foxglove",hide_title:!0},i="Visualize with Foxglove",l={unversionedId:"guides/foxglove_visual",id:"guides/foxglove_visual",title:"Visualize with Foxglove",description:"Foxglove helps to view a graphical representation of the simulation.",source:"@site/docs/guides/foxglove_visual.md",sourceDirName:"guides",slug:"/guides/foxglove_visual",permalink:"/docs/next/guides/foxglove_visual",draft:!1,tags:[],version:"current",frontMatter:{sidebar_label:"Visualize with Foxglove",hide_title:!0},sidebar:"gettingStartedSidebar",previous:{title:"CITROS in Dockerfile",permalink:"/docs/next/guides/dockerfile_overview"},next:{title:"TODO VOVAAAAAA",permalink:"/docs/next/advanced_guides/citros_overview"}},p={},s=[],c={toc:s},u="wrapper";function d(e){let{components:t,...a}=e;return(0,r.kt)(u,(0,o.Z)({},c,a,{components:t,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"visualize-with-foxglove"},"Visualize with Foxglove"),(0,r.kt)("p",null,"Foxglove helps to view a graphical representation of the simulation."),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("p",{parentName:"li"},"Download and install ",(0,r.kt)("a",{parentName:"p",href:"https://foxglove.dev/download"},"Foxglove"))),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("p",{parentName:"li"},"Open Foxglove")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("p",{parentName:"li"},"Press on Foxglove icon at the top right")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("p",{parentName:"li"},"Click View")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("p",{parentName:"li"},'Click "Import layout from file"'),(0,r.kt)("p",{parentName:"li"},(0,r.kt)("img",{alt:"Alt text",src:n(1081).Z,width:"1601",height:"881"}))),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("p",{parentName:"li"},"Choose the ",(0,r.kt)("inlineCode",{parentName:"p"},"[layout_name].json")," from the project directory.")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("p",{parentName:"li"},"Open a new Connection."),(0,r.kt)("p",{parentName:"li"},(0,r.kt)("img",{alt:"Alt text",src:n(17513).Z,width:"1601",height:"881"}))),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("p",{parentName:"li"},"Choose Rosbridge and press the 'Open' button"),(0,r.kt)("p",{parentName:"li"},(0,r.kt)("img",{alt:"Alt text",src:n(19650).Z,width:"1601",height:"881"}))),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("p",{parentName:"li"},"You now have a working connection to your simulation, you can now run the simulation and check the output in Foxglove."))),(0,r.kt)("p",null,"Output example:\n",(0,r.kt)("img",{alt:"Foxglove screenshot",src:n(6394).Z,width:"1212",height:"926"})))}d.isMDXComponent=!0},17513:(e,t,n)=>{n.d(t,{Z:()=>o});const o=n.p+"assets/images/foxglove_connection-bf88605ed4e767d61fad33aec9bb154d.png"},1081:(e,t,n)=>{n.d(t,{Z:()=>o});const o=n.p+"assets/images/foxglove_open-f39d9ead654d2eb518c5ce9e0de950aa.png"},19650:(e,t,n)=>{n.d(t,{Z:()=>o});const o=n.p+"assets/images/foxglove_rosbridge-c5e64c6d5b79820786e834d9dcd46959.png"},6394:(e,t,n)=>{n.d(t,{Z:()=>o});const o=n.p+"assets/images/foxglove_screenshot-8b82912ff4ecaed893d7e540e0b4f99d.png"}}]);
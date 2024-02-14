"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[97109],{3905:(e,t,r)=>{r.d(t,{Zo:()=>c,kt:()=>g});var n=r(67294);function a(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function o(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function l(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?o(Object(r),!0).forEach((function(t){a(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):o(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function i(e,t){if(null==e)return{};var r,n,a=function(e,t){if(null==e)return{};var r,n,a={},o=Object.keys(e);for(n=0;n<o.length;n++)r=o[n],t.indexOf(r)>=0||(a[r]=e[r]);return a}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(n=0;n<o.length;n++)r=o[n],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(a[r]=e[r])}return a}var p=n.createContext({}),s=function(e){var t=n.useContext(p),r=t;return e&&(r="function"==typeof e?e(t):l(l({},t),e)),r},c=function(e){var t=s(e.components);return n.createElement(p.Provider,{value:t},e.children)},m="mdxType",d={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},u=n.forwardRef((function(e,t){var r=e.components,a=e.mdxType,o=e.originalType,p=e.parentName,c=i(e,["components","mdxType","originalType","parentName"]),m=s(r),u=a,g=m["".concat(p,".").concat(u)]||m[u]||d[u]||o;return r?n.createElement(g,l(l({ref:t},c),{},{components:r})):n.createElement(g,l({ref:t},c))}));function g(e,t){var r=arguments,a=t&&t.mdxType;if("string"==typeof e||a){var o=r.length,l=new Array(o);l[0]=u;var i={};for(var p in t)hasOwnProperty.call(t,p)&&(i[p]=t[p]);i.originalType=e,i[m]="string"==typeof e?e:a,l[1]=i;for(var s=2;s<o;s++)l[s]=r[s];return n.createElement.apply(null,l)}return n.createElement.apply(null,r)}u.displayName="MDXCreateElement"},98872:(e,t,r)=>{r.r(t),r.d(t,{assets:()=>p,contentTitle:()=>l,default:()=>d,frontMatter:()=>o,metadata:()=>i,toc:()=>s});var n=r(87462),a=(r(67294),r(3905));const o={sidebar_label:"citros report list"},l="citros report list",i={unversionedId:"commands/report/report_list",id:"version-0.2.52/commands/report/report_list",title:"citros report list",description:"Description",source:"@site/versioned_docs/version-0.2.52/commands/report/report_list.md",sourceDirName:"commands/report",slug:"/commands/report/report_list",permalink:"/docs/0.2.52/commands/report/report_list",draft:!1,tags:[],version:"0.2.52",frontMatter:{sidebar_label:"citros report list"},sidebar:"gettingStartedSidebar",previous:{title:"citros data db logs",permalink:"/docs/0.2.52/commands/data/db_logs"},next:{title:"citros report generate",permalink:"/docs/0.2.52/commands/report/report_generate"}},p={},s=[{value:"Description",id:"description",level:2},{value:"Options",id:"options",level:2},{value:"Example:",id:"example",level:3},{value:"Interactive Mode",id:"interactive-mode",level:2}],c={toc:s},m="wrapper";function d(e){let{components:t,...r}=e;return(0,a.kt)(m,(0,n.Z)({},c,r,{components:t,mdxType:"MDXLayout"}),(0,a.kt)("h1",{id:"citros-report-list"},(0,a.kt)("inlineCode",{parentName:"h1"},"citros report list")),(0,a.kt)("h2",{id:"description"},"Description"),(0,a.kt)("p",null,"Shows a table of all the reports in ",(0,a.kt)("inlineCode",{parentName:"p"},".citros/reports")," folder "),(0,a.kt)("table",null,(0,a.kt)("thead",{parentName:"table"},(0,a.kt)("tr",{parentName:"thead"},(0,a.kt)("th",{parentName:"tr",align:null},"Table Field"),(0,a.kt)("th",{parentName:"tr",align:null},"Description"))),(0,a.kt)("tbody",{parentName:"table"},(0,a.kt)("tr",{parentName:"tbody"},(0,a.kt)("td",{parentName:"tr",align:null},"Date"),(0,a.kt)("td",{parentName:"tr",align:null},"Thh date the report was generated")),(0,a.kt)("tr",{parentName:"tbody"},(0,a.kt)("td",{parentName:"tr",align:null},"Name"),(0,a.kt)("td",{parentName:"tr",align:null},"The given name for the report")),(0,a.kt)("tr",{parentName:"tbody"},(0,a.kt)("td",{parentName:"tr",align:null},"Version"),(0,a.kt)("td",{parentName:"tr",align:null},"The version of the report")),(0,a.kt)("tr",{parentName:"tbody"},(0,a.kt)("td",{parentName:"tr",align:null},"Message"),(0,a.kt)("td",{parentName:"tr",align:null},"The given message for the report")),(0,a.kt)("tr",{parentName:"tbody"},(0,a.kt)("td",{parentName:"tr",align:null},"Progress"),(0,a.kt)("td",{parentName:"tr",align:null},"the percentage of the report completion")),(0,a.kt)("tr",{parentName:"tbody"},(0,a.kt)("td",{parentName:"tr",align:null},"Status"),(0,a.kt)("td",{parentName:"tr",align:null},"Status of the report created. can be One of ","[",(0,a.kt)("inlineCode",{parentName:"td"},"OK"),", ",(0,a.kt)("inlineCode",{parentName:"td"},"FAILED"),"]"," values")),(0,a.kt)("tr",{parentName:"tbody"},(0,a.kt)("td",{parentName:"tr",align:null},"Path"),(0,a.kt)("td",{parentName:"tr",align:null},"The location of the report")))),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-bash"},"$ citros report list [-h] [-dir DIR] [-d] [-v]\n")),(0,a.kt)("h2",{id:"options"},"Options"),(0,a.kt)("table",null,(0,a.kt)("thead",{parentName:"table"},(0,a.kt)("tr",{parentName:"thead"},(0,a.kt)("th",{parentName:"tr",align:null},"Option"),(0,a.kt)("th",{parentName:"tr",align:null},"Description"))),(0,a.kt)("tbody",{parentName:"table"},(0,a.kt)("tr",{parentName:"tbody"},(0,a.kt)("td",{parentName:"tr",align:null},"-h, --help"),(0,a.kt)("td",{parentName:"tr",align:null},"Show help message")),(0,a.kt)("tr",{parentName:"tbody"},(0,a.kt)("td",{parentName:"tr",align:null},"-dir DIR"),(0,a.kt)("td",{parentName:"tr",align:null},"The working dir of the project")),(0,a.kt)("tr",{parentName:"tbody"},(0,a.kt)("td",{parentName:"tr",align:null},"-d, --debug"),(0,a.kt)("td",{parentName:"tr",align:null},"Set logging level to debug")),(0,a.kt)("tr",{parentName:"tbody"},(0,a.kt)("td",{parentName:"tr",align:null},"-v, --verbose"),(0,a.kt)("td",{parentName:"tr",align:null},"Use verbose console prints")))),(0,a.kt)("h3",{id:"example"},"Example:"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-bash"},"$ citros report list\n                            Reports from: .citros/reports                             \n\u250c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u252c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u252c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u252c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u252c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u252c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u252c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510\n\u2502 Date        \u2502 Name   \u2502 Versions    \u2502 Message     \u2502 Progress \u2502 Status \u2502 Path        \u2502\n\u251c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524\n\u2502 2024-02-13  \u2502 citros \u2502 2024021312\u2026 \u2502 report      \u2502      100 \u2502 OK     \u2502 .citros/rep \u2502\n\u2502 12:56:46    \u2502        \u2502             \u2502 message     \u2502          \u2502        \u2502 orts/citros \u2502\n\u2502             \u2502        \u2502             \u2502             \u2502          \u2502        \u2502 /2024021312 \u2502\n\u2502             \u2502        \u2502             \u2502             \u2502          \u2502        \u2502 5646        \u2502\n\u2502 2024-02-13  \u2502        \u2502 2024021312\u2026 \u2502 report      \u2502      100 \u2502 FAILED \u2502 .citros/rep \u2502\n\u2502 12:55:46    \u2502        \u2502             \u2502 message     \u2502          \u2502        \u2502 orts/citros \u2502\n\u2502             \u2502        \u2502             \u2502             \u2502          \u2502        \u2502 /2024021312 \u2502\n\u2502             \u2502        \u2502             \u2502             \u2502          \u2502        \u2502 5546        \u2502\n\u2502 2024-02-13  \u2502        \u2502 2024021312\u2026 \u2502 report      \u2502      100 \u2502 OK     \u2502 .citros/rep \u2502\n\u2502 12:54:03    \u2502        \u2502             \u2502 message     \u2502          \u2502        \u2502 orts/citros \u2502\n\u2502             \u2502        \u2502             \u2502             \u2502          \u2502        \u2502 /2024021312 \u2502\n\u2502             \u2502        \u2502             \u2502             \u2502          \u2502        \u2502 5403        \u2502\n\u2502 2024-02-13  \u2502        \u2502 2024021312\u2026 \u2502 report      \u2502      100 \u2502 OK     \u2502 .citros/rep \u2502\n\u2502 12:53:27    \u2502        \u2502             \u2502 message     \u2502          \u2502        \u2502 orts/citros \u2502\n\u2502             \u2502        \u2502             \u2502             \u2502          \u2502        \u2502 /2024021312 \u2502\n\u2502             \u2502        \u2502             \u2502             \u2502          \u2502        \u2502 5327        \u2502\n\u2502 2024-02-13  \u2502        \u2502 2024021312\u2026 \u2502 report      \u2502      100 \u2502 FAILED \u2502 .citros/rep \u2502\n\u2502 12:38:31    \u2502        \u2502             \u2502 message     \u2502          \u2502        \u2502 orts/citros \u2502\n\u2502             \u2502        \u2502             \u2502             \u2502          \u2502        \u2502 /2024021312 \u2502\n\u2502             \u2502        \u2502             \u2502             \u2502          \u2502        \u2502 3831        \u2502\n\u2502 2024-02-13  \u2502 report \u2502 2024021313\u2026 \u2502 test report \u2502      100 \u2502 OK     \u2502 .citros/rep \u2502\n\u2502 13:18:20    \u2502        \u2502             \u2502             \u2502          \u2502        \u2502 orts/report \u2502\n\u2502             \u2502        \u2502             \u2502             \u2502          \u2502        \u2502 /2024021313 \u2502\n\u2502             \u2502        \u2502             \u2502             \u2502          \u2502        \u2502 1820        \u2502\n\u2502 2024-02-13  \u2502        \u2502 2024021313\u2026 \u2502 test report \u2502        0 \u2502 START  \u2502 .citros/rep \u2502\n\u2502 13:18:06    \u2502        \u2502             \u2502             \u2502          \u2502        \u2502 orts/report \u2502\n\u2502             \u2502        \u2502             \u2502             \u2502          \u2502        \u2502 /2024021313 \u2502\n\u2502             \u2502        \u2502             \u2502             \u2502          \u2502        \u2502 1806        \u2502\n\u2502 2024-02-13  \u2502        \u2502 2024021313\u2026 \u2502 test report \u2502        0 \u2502 START  \u2502 .citros/rep \u2502\n\u2502 13:17:20    \u2502        \u2502             \u2502             \u2502          \u2502        \u2502 orts/report \u2502\n\u2502             \u2502        \u2502             \u2502             \u2502          \u2502        \u2502 /2024021313 \u2502\n\u2502             \u2502        \u2502             \u2502             \u2502          \u2502        \u2502 1720        \u2502\n\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2534\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2534\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2534\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2534\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2534\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2534\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518\n")),(0,a.kt)("h2",{id:"interactive-mode"},"Interactive Mode"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-bash"},"$ citros\n")),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-sh"},"? Select Action: \n\u250c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510\n\u2502  Init: initialize .citros in current directory                                     \u2502\n\u2502  Run: new simulation                                                               \u2502\n\u2502  Data: for data management                                                         \u2502\n\u2502\u276f Report: generation and management                                                 \u2502\n\u2502  ---------------                                                                   \u2502\n\u2502  EXIT                                                                              \u2502\n\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518\n")),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-sh"},"? Select Action: Report: generation and management\n? Select Action: \n\u250c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510\n\u2502\u276f List: reports list                                                                \u2502\n\u2502  Generate: new report                                                              \u2502\n\u2502  ---------------                                                                   \u2502\n\u2502  EXIT                                                                              \u2502\n\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518\n")))}d.isMDXComponent=!0}}]);
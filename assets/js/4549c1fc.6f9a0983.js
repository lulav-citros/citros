"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[369],{3905:(t,e,a)=>{a.d(e,{Zo:()=>p,kt:()=>g});var n=a(67294);function r(t,e,a){return e in t?Object.defineProperty(t,e,{value:a,enumerable:!0,configurable:!0,writable:!0}):t[e]=a,t}function l(t,e){var a=Object.keys(t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(t);e&&(n=n.filter((function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable}))),a.push.apply(a,n)}return a}function i(t){for(var e=1;e<arguments.length;e++){var a=null!=arguments[e]?arguments[e]:{};e%2?l(Object(a),!0).forEach((function(e){r(t,e,a[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(a)):l(Object(a)).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(a,e))}))}return t}function o(t,e){if(null==t)return{};var a,n,r=function(t,e){if(null==t)return{};var a,n,r={},l=Object.keys(t);for(n=0;n<l.length;n++)a=l[n],e.indexOf(a)>=0||(r[a]=t[a]);return r}(t,e);if(Object.getOwnPropertySymbols){var l=Object.getOwnPropertySymbols(t);for(n=0;n<l.length;n++)a=l[n],e.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(t,a)&&(r[a]=t[a])}return r}var s=n.createContext({}),d=function(t){var e=n.useContext(s),a=e;return t&&(a="function"==typeof t?t(e):i(i({},e),t)),a},p=function(t){var e=d(t.components);return n.createElement(s.Provider,{value:e},t.children)},m="mdxType",u={inlineCode:"code",wrapper:function(t){var e=t.children;return n.createElement(n.Fragment,{},e)}},k=n.forwardRef((function(t,e){var a=t.components,r=t.mdxType,l=t.originalType,s=t.parentName,p=o(t,["components","mdxType","originalType","parentName"]),m=d(a),k=r,g=m["".concat(s,".").concat(k)]||m[k]||u[k]||l;return a?n.createElement(g,i(i({ref:e},p),{},{components:a})):n.createElement(g,i({ref:e},p))}));function g(t,e){var a=arguments,r=e&&e.mdxType;if("string"==typeof t||r){var l=a.length,i=new Array(l);i[0]=k;var o={};for(var s in e)hasOwnProperty.call(e,s)&&(o[s]=e[s]);o.originalType=t,o[m]="string"==typeof t?t:r,i[1]=o;for(var d=2;d<l;d++)i[d]=a[d];return n.createElement.apply(null,i)}return n.createElement.apply(null,a)}k.displayName="MDXCreateElement"},49890:(t,e,a)=>{a.r(e),a.d(e,{assets:()=>s,contentTitle:()=>i,default:()=>u,frontMatter:()=>l,metadata:()=>o,toc:()=>d});var n=a(87462),r=(a(67294),a(3905));const l={sidebar_label:"Class CitrosStat",toc_max_heading_level:3,hide_title:!0,description:"Documentation"},i="Class CitrosStat",o={unversionedId:"data_analysis/documentation/analysis/citros_stat",id:"version-0.2.61/data_analysis/documentation/analysis/citros_stat",title:"Class CitrosStat",description:"Documentation",source:"@site/versioned_docs/version-0.2.61/data_analysis/documentation/analysis/citros_stat.md",sourceDirName:"data_analysis/documentation/analysis",slug:"/data_analysis/documentation/analysis/citros_stat",permalink:"/docs/0.2.61/data_analysis/documentation/analysis/citros_stat",draft:!1,tags:[],version:"0.2.61",frontMatter:{sidebar_label:"Class CitrosStat",toc_max_heading_level:3,hide_title:!0,description:"Documentation"},sidebar:"gettingStartedSidebar",previous:{title:"Class CitrosDataArray",permalink:"/docs/0.2.61/data_analysis/documentation/analysis/citros_data_array"},next:{title:"Overview",permalink:"/docs/0.2.61/data_analysis/validation/"}},s={},d=[{value:"Class <code>CitrosStat</code>",id:"analysis.citros_stat.CitrosStat",level:2},{value:"Parameters",id:"parameters",level:4},{value:"Attributes",id:"attributes",level:4},{value:"Method <code>to_pandas</code>",id:"analysis.citros_stat.CitrosStat.to_pandas",level:2},{value:"Returns",id:"returns",level:4},{value:"Method <code>plot</code>",id:"analysis.citros_stat.CitrosStat.plot",level:2},{value:"Parameters",id:"parameters-1",level:4},{value:"Returns",id:"returns-1",level:4}],p={toc:d},m="wrapper";function u(t){let{components:e,...a}=t;return(0,r.kt)(m,(0,n.Z)({},p,a,{components:e,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"class-citrosstat"},"Class CitrosStat"),(0,r.kt)("h2",{id:"analysis.citros_stat.CitrosStat"},"Class ",(0,r.kt)("inlineCode",{parentName:"h2"},"CitrosStat")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"class CitrosStat(\n    F,\n    labels,\n    x_label\n)\n")),(0,r.kt)("details",null,(0,r.kt)("summary",null,"Description"),(0,r.kt)("p",null,"Object to store statistics."),(0,r.kt)("h4",{id:"parameters"},"Parameters"),(0,r.kt)("table",null,(0,r.kt)("thead",{parentName:"table"},(0,r.kt)("tr",{parentName:"thead"},(0,r.kt)("th",{parentName:"tr",align:null},"Name"),(0,r.kt)("th",{parentName:"tr",align:null},"Type"),(0,r.kt)("th",{parentName:"tr",align:null},"Description"))),(0,r.kt)("tbody",{parentName:"table"},(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},(0,r.kt)("inlineCode",{parentName:"strong"},"F"))),(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},"pandas.DataFrame")),(0,r.kt)("td",{parentName:"tr",align:null},"Table with statistics.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},(0,r.kt)("inlineCode",{parentName:"strong"},"labels"))),(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("inlineCode",{parentName:"td"},"array-like")),(0,r.kt)("td",{parentName:"tr",align:null},"Labels of the data columns.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},(0,r.kt)("inlineCode",{parentName:"strong"},"x_label"))),(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},"str")),(0,r.kt)("td",{parentName:"tr",align:null},"Label of the independent variable.")))),(0,r.kt)("h4",{id:"attributes"},"Attributes"),(0,r.kt)("table",null,(0,r.kt)("thead",{parentName:"table"},(0,r.kt)("tr",{parentName:"thead"},(0,r.kt)("th",{parentName:"tr",align:null},"Name"),(0,r.kt)("th",{parentName:"tr",align:null},"Type"),(0,r.kt)("th",{parentName:"tr",align:null},"Description"))),(0,r.kt)("tbody",{parentName:"table"},(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},(0,r.kt)("inlineCode",{parentName:"strong"},"x"))),(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},"pandas.DataFrame")),(0,r.kt)("td",{parentName:"tr",align:null},"Table with independent variable.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},(0,r.kt)("inlineCode",{parentName:"strong"},"mean"))),(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},"pandas.DataFrame")),(0,r.kt)("td",{parentName:"tr",align:null},"Table with mean values. If statistics was collected for a vector, columns correspond to vector elements.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},(0,r.kt)("inlineCode",{parentName:"strong"},"covar_matrix"))),(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},"pandas.DataFrame")),(0,r.kt)("td",{parentName:"tr",align:null},"Table with the covariance matrixes. If statistics was collected for a vector, columns correspond to vector elements.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},(0,r.kt)("inlineCode",{parentName:"strong"},"sigma"))),(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},"pandas.DataFrame")),(0,r.kt)("td",{parentName:"tr",align:null},"Table with the square roots of the diagonal elements of the covariance matrix. ",(0,r.kt)("br",null),"    If statistics was collected for a vector, columns correspond to vector elements."))))),(0,r.kt)("h2",{id:"analysis.citros_stat.CitrosStat.to_pandas"},"Method ",(0,r.kt)("inlineCode",{parentName:"h2"},"to_pandas")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"def to_pandas()\n")),(0,r.kt)("details",null,(0,r.kt)("summary",null,"Description"),(0,r.kt)("p",null,"Convert CitrosStat object back to pandas DataFrame."),(0,r.kt)("h4",{id:"returns"},"Returns"),(0,r.kt)("table",null,(0,r.kt)("thead",{parentName:"table"},(0,r.kt)("tr",{parentName:"thead"},(0,r.kt)("th",{parentName:"tr",align:null},"Name"),(0,r.kt)("th",{parentName:"tr",align:null},"Type"),(0,r.kt)("th",{parentName:"tr",align:null},"Description"))),(0,r.kt)("tbody",{parentName:"table"},(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},(0,r.kt)("inlineCode",{parentName:"strong"},"df"))),(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},"pandas.DataFrame")),(0,r.kt)("td",{parentName:"tr",align:null},"Converted to pandas DataFrame."))))),(0,r.kt)("h2",{id:"analysis.citros_stat.CitrosStat.plot"},"Method ",(0,r.kt)("inlineCode",{parentName:"h2"},"plot")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"def plot(\n    fig=None,\n    show_fig=True,\n    return_fig=False,\n    n_std=3,\n    fig_title='Statistics',\n    std_color='r'\n)\n")),(0,r.kt)("details",null,(0,r.kt)("summary",null,"Description"),(0,r.kt)("p",null,"Plot mean values and standard deviations."),(0,r.kt)("h4",{id:"parameters-1"},"Parameters"),(0,r.kt)("table",null,(0,r.kt)("thead",{parentName:"table"},(0,r.kt)("tr",{parentName:"thead"},(0,r.kt)("th",{parentName:"tr",align:null},"Name"),(0,r.kt)("th",{parentName:"tr",align:null},"Type"),(0,r.kt)("th",{parentName:"tr",align:null},"Description"))),(0,r.kt)("tbody",{parentName:"table"},(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},(0,r.kt)("inlineCode",{parentName:"strong"},"fig"))),(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},"matplotlib.figure.Figure")),(0,r.kt)("td",{parentName:"tr",align:null},"figure to plot on. If None, the new one will be created.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},(0,r.kt)("inlineCode",{parentName:"strong"},"show_fig"))),(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},"bool")),(0,r.kt)("td",{parentName:"tr",align:null},"If the figure should be shown, True by default.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},(0,r.kt)("inlineCode",{parentName:"strong"},"return_fig"))),(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},"bool")),(0,r.kt)("td",{parentName:"tr",align:null},"If the figure parameters fig, ax should be returned; ",(0,r.kt)("br",null),"    fig is matplotlib.figure.Figure and ax is matplotlib.axes.Axes")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},(0,r.kt)("inlineCode",{parentName:"strong"},"n_std"))),(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},"int"),", default ",(0,r.kt)("strong",{parentName:"td"},"3")),(0,r.kt)("td",{parentName:"tr",align:null},"Error interval to display, specified in standard deviations.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},(0,r.kt)("inlineCode",{parentName:"strong"},"fig_title"))),(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},"str"),", default ",(0,r.kt)("inlineCode",{parentName:"td"},"'Statistics'")),(0,r.kt)("td",{parentName:"tr",align:null},"Title of the figure.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},(0,r.kt)("inlineCode",{parentName:"strong"},"std_color"))),(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},"str"),", default ",(0,r.kt)("inlineCode",{parentName:"td"},"'r'")),(0,r.kt)("td",{parentName:"tr",align:null},"Color for displaying standard deviations, red by default.")))),(0,r.kt)("h4",{id:"returns-1"},"Returns"),(0,r.kt)("table",null,(0,r.kt)("thead",{parentName:"table"},(0,r.kt)("tr",{parentName:"thead"},(0,r.kt)("th",{parentName:"tr",align:null},"Name"),(0,r.kt)("th",{parentName:"tr",align:null},"Type"),(0,r.kt)("th",{parentName:"tr",align:null},"Description"))),(0,r.kt)("tbody",{parentName:"table"},(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},(0,r.kt)("inlineCode",{parentName:"strong"},"fig"))),(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},"matplotlib.figure.Figure")),(0,r.kt)("td",{parentName:"tr",align:null},"if ",(0,r.kt)("strong",{parentName:"td"},"return_fig")," set to True")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},(0,r.kt)("inlineCode",{parentName:"strong"},"ax"))),(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},"list")," of ",(0,r.kt)("strong",{parentName:"td"},"matplotlib.axes.Axes")),(0,r.kt)("td",{parentName:"tr",align:null},"if ",(0,r.kt)("strong",{parentName:"td"},"return_fig")," set to True"))))))}u.isMDXComponent=!0}}]);
"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[5757],{3905:(e,t,n)=>{n.d(t,{Zo:()=>p,kt:()=>k});var r=n(7294);function a(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function l(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function i(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?l(Object(n),!0).forEach((function(t){a(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):l(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function o(e,t){if(null==e)return{};var n,r,a=function(e,t){if(null==e)return{};var n,r,a={},l=Object.keys(e);for(r=0;r<l.length;r++)n=l[r],t.indexOf(n)>=0||(a[n]=e[n]);return a}(e,t);if(Object.getOwnPropertySymbols){var l=Object.getOwnPropertySymbols(e);for(r=0;r<l.length;r++)n=l[r],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(a[n]=e[n])}return a}var s=r.createContext({}),c=function(e){var t=r.useContext(s),n=t;return e&&(n="function"==typeof e?e(t):i(i({},t),e)),n},p=function(e){var t=c(e.components);return r.createElement(s.Provider,{value:t},e.children)},u="mdxType",d={inlineCode:"code",wrapper:function(e){var t=e.children;return r.createElement(r.Fragment,{},t)}},m=r.forwardRef((function(e,t){var n=e.components,a=e.mdxType,l=e.originalType,s=e.parentName,p=o(e,["components","mdxType","originalType","parentName"]),u=c(n),m=a,k=u["".concat(s,".").concat(m)]||u[m]||d[m]||l;return n?r.createElement(k,i(i({ref:t},p),{},{components:n})):r.createElement(k,i({ref:t},p))}));function k(e,t){var n=arguments,a=t&&t.mdxType;if("string"==typeof e||a){var l=n.length,i=new Array(l);i[0]=m;var o={};for(var s in t)hasOwnProperty.call(t,s)&&(o[s]=t[s]);o.originalType=e,o[u]="string"==typeof e?e:a,i[1]=o;for(var c=2;c<l;c++)i[c]=n[c];return r.createElement.apply(null,i)}return r.createElement.apply(null,n)}m.displayName="MDXCreateElement"},9122:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>s,contentTitle:()=>i,default:()=>d,frontMatter:()=>l,metadata:()=>o,toc:()=>c});var r=n(7462),a=(n(7294),n(3905));const l={},i="Installation",o={unversionedId:"cli/cli_install",id:"cli/cli_install",title:"Installation",description:"The following document will guide you through CITROS CLI installation.",source:"@site/docs/cli/cli_install.md",sourceDirName:"cli",slug:"/cli/cli_install",permalink:"/docs/cli/cli_install",draft:!1,tags:[],version:"current",frontMatter:{},sidebar:"gettingStartedSidebar",next:{title:"Installation",permalink:"/docs/cli/cli_quickstart"}},s={},c=[{value:"Prerequisites",id:"prerequisites",level:2},{value:"Installation",id:"installation-1",level:2},{value:"Environment Variables",id:"environment-variables",level:2}],p={toc:c},u="wrapper";function d(e){let{components:t,...n}=e;return(0,a.kt)(u,(0,r.Z)({},p,n,{components:t,mdxType:"MDXLayout"}),(0,a.kt)("h1",{id:"installation"},"Installation"),(0,a.kt)("p",null,"The following document will guide you through CITROS CLI installation."),(0,a.kt)("h2",{id:"prerequisites"},"Prerequisites"),(0,a.kt)("ul",null,(0,a.kt)("li",{parentName:"ul"},(0,a.kt)("a",{parentName:"li",href:"https://www.docker.com/"},"Docker")),(0,a.kt)("li",{parentName:"ul"},(0,a.kt)("a",{parentName:"li",href:"https://www.python.org/downloads/"},"Python3")),(0,a.kt)("li",{parentName:"ul"},(0,a.kt)("a",{parentName:"li",href:"https://git-scm.com/"},"git"))),(0,a.kt)("h2",{id:"installation-1"},"Installation"),(0,a.kt)("p",null,"To install CITROS using pip, open terminal and write the following command:"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre"},"$ pip install citros \n")),(0,a.kt)("p",null,"to make sure the installation was successful, run"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre"},"$ citros -V\n1.2.59\n")),(0,a.kt)("p",null,"to get the installed version. "),(0,a.kt)("p",null,"In some environments you ",(0,a.kt)("strong",{parentName:"p"},"might")," also need to make sure the installation directory is in your ",(0,a.kt)("inlineCode",{parentName:"p"},"PATH")," environment variable, either by "),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre"},"$ source ~/.profile\n")),(0,a.kt)("p",null,"or "),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre"},"$ set PATH=/usr/local/bin:$PATH\n")),(0,a.kt)("h2",{id:"environment-variables"},"Environment Variables"),(0,a.kt)("p",null,"   ",(0,a.kt)("inlineCode",{parentName:"p"},"citros_cli")," uses several environment variables, some of which you may change according to your needs, although for the most part, the defaults are likely to be what you want. Generally speaking, most of these are only used by developers of the package, and should not be used."),(0,a.kt)("table",null,(0,a.kt)("thead",{parentName:"table"},(0,a.kt)("tr",{parentName:"thead"},(0,a.kt)("th",{parentName:"tr",align:null},"ENV"),(0,a.kt)("th",{parentName:"tr",align:null},"Description"))),(0,a.kt)("tbody",{parentName:"table"},(0,a.kt)("tr",{parentName:"tbody"},(0,a.kt)("td",{parentName:"tr",align:null},(0,a.kt)("inlineCode",{parentName:"td"},"CITROS_DOMAIN")),(0,a.kt)("td",{parentName:"tr",align:null},"The main domain, defaults to ",(0,a.kt)("inlineCode",{parentName:"td"},"citros.io"))),(0,a.kt)("tr",{parentName:"tbody"},(0,a.kt)("td",{parentName:"tr",align:null},(0,a.kt)("inlineCode",{parentName:"td"},"CITROS_DIR")),(0,a.kt)("td",{parentName:"tr",align:null},"Used by the citros cluster, do not use.")),(0,a.kt)("tr",{parentName:"tbody"},(0,a.kt)("td",{parentName:"tr",align:null},(0,a.kt)("inlineCode",{parentName:"td"},"CITROS_SIM_RUN_DIR")),(0,a.kt)("td",{parentName:"tr",align:null},"The directory under ",(0,a.kt)("inlineCode",{parentName:"td"},".citros/runs")," in which all simulation data will be saved (see ",(0,a.kt)("a",{parentName:"td",href:"../docs/cli/citros_structure.md#directory-runs"},"runs"),"). This can be handy, if your code needs to know this location in order to access some of the files, e.g. parameter setups.")),(0,a.kt)("tr",{parentName:"tbody"},(0,a.kt)("td",{parentName:"tr",align:null},(0,a.kt)("inlineCode",{parentName:"td"},"CITROS_NETWORK_CHECK_URL")),(0,a.kt)("td",{parentName:"tr",align:null},"If you do not have access to the internet, i.e. you're working inside a company intranet and the CITROS servers are installed onsite, change this variable to the url of an intranet site you should always have access to, sort of like the company ",(0,a.kt)("inlineCode",{parentName:"td"},"google.com"),".")))))}d.isMDXComponent=!0}}]);
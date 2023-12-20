"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[3293],{3905:(e,t,r)=>{r.d(t,{Zo:()=>l,kt:()=>_});var o=r(7294);function a(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function n(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);t&&(o=o.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,o)}return r}function s(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?n(Object(r),!0).forEach((function(t){a(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):n(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function i(e,t){if(null==e)return{};var r,o,a=function(e,t){if(null==e)return{};var r,o,a={},n=Object.keys(e);for(o=0;o<n.length;o++)r=n[o],t.indexOf(r)>=0||(a[r]=e[r]);return a}(e,t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);for(o=0;o<n.length;o++)r=n[o],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(a[r]=e[r])}return a}var p=o.createContext({}),c=function(e){var t=o.useContext(p),r=t;return e&&(r="function"==typeof e?e(t):s(s({},t),e)),r},l=function(e){var t=c(e.components);return o.createElement(p.Provider,{value:t},e.children)},d="mdxType",u={inlineCode:"code",wrapper:function(e){var t=e.children;return o.createElement(o.Fragment,{},t)}},y=o.forwardRef((function(e,t){var r=e.components,a=e.mdxType,n=e.originalType,p=e.parentName,l=i(e,["components","mdxType","originalType","parentName"]),d=c(r),y=a,_=d["".concat(p,".").concat(y)]||d[y]||u[y]||n;return r?o.createElement(_,s(s({ref:t},l),{},{components:r})):o.createElement(_,s({ref:t},l))}));function _(e,t){var r=arguments,a=t&&t.mdxType;if("string"==typeof e||a){var n=r.length,s=new Array(n);s[0]=y;var i={};for(var p in t)hasOwnProperty.call(t,p)&&(i[p]=t[p]);i.originalType=e,i[d]="string"==typeof e?e:a,s[1]=i;for(var c=2;c<n;c++)s[c]=r[c];return o.createElement.apply(null,s)}return o.createElement.apply(null,r)}y.displayName="MDXCreateElement"},4218:(e,t,r)=>{r.r(t),r.d(t,{assets:()=>p,contentTitle:()=>s,default:()=>u,frontMatter:()=>n,metadata:()=>i,toc:()=>c});var o=r(7462),a=(r(7294),r(3905));const n={toc_max_heading_level:4,hide_title:!0,sidebar_label:"Repositories"},s="Repositories",i={unversionedId:"snippets_doc/data_access/snippets_repositories",id:"version-v0.9.1/snippets_doc/data_access/snippets_repositories",title:"Repositories",description:"All Repositories",source:"@site/docs_data_analysis_versioned_docs/version-v0.9.1/snippets_doc/data_access/snippets_repositories.md",sourceDirName:"snippets_doc/data_access",slug:"/snippets_doc/data_access/snippets_repositories",permalink:"/docs_data_analysis/snippets_doc/data_access/snippets_repositories",draft:!1,tags:[],version:"v0.9.1",frontMatter:{toc_max_heading_level:4,hide_title:!0,sidebar_label:"Repositories"},sidebar:"dataAnalysisSidebar",previous:{title:"CITROS Data Analysis",permalink:"/docs_data_analysis/"},next:{title:"Batches",permalink:"/docs_data_analysis/snippets_doc/data_access/snippets_batches"}},p={},c=[{value:"All Repositories",id:"all-repositories",level:2},{value:"Exact Repository",id:"exact-repository",level:2}],l={toc:c},d="wrapper";function u(e){let{components:t,...r}=e;return(0,a.kt)(d,(0,o.Z)({},l,r,{components:t,mdxType:"MDXLayout"}),(0,a.kt)("h1",{id:"repositories"},"Repositories"),(0,a.kt)("h2",{id:"all-repositories"},"All Repositories"),(0,a.kt)("p",null,"Get overview about the repositories:"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-python"},"from citros_data_analysis import data_access as da\n\ncitros = da.CitrosDB()\ncitros.search_repo().print()\n")),(0,a.kt)("h2",{id:"exact-repository"},"Exact Repository"),(0,a.kt)("p",null,"Get overview about exact repository 'my_repository':"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-python"},"from citros_data_analysis import data_access as da\n\n# --- adjust to your data --- #\nrepo_name = 'my_repository'\n# --------------------------- #\n\ncitros = da.CitrosDB()\ncitros.search_repo(repo_name).print()\n")))}u.isMDXComponent=!0}}]);
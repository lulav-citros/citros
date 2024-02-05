"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[96819],{3905:(e,t,r)=>{r.d(t,{Zo:()=>s,kt:()=>y});var n=r(67294);function o(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function i(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function a(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?i(Object(r),!0).forEach((function(t){o(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):i(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function p(e,t){if(null==e)return{};var r,n,o=function(e,t){if(null==e)return{};var r,n,o={},i=Object.keys(e);for(n=0;n<i.length;n++)r=i[n],t.indexOf(r)>=0||(o[r]=e[r]);return o}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(n=0;n<i.length;n++)r=i[n],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(o[r]=e[r])}return o}var c=n.createContext({}),l=function(e){var t=n.useContext(c),r=t;return e&&(r="function"==typeof e?e(t):a(a({},t),e)),r},s=function(e){var t=l(e.components);return n.createElement(c.Provider,{value:t},e.children)},u="mdxType",d={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},m=n.forwardRef((function(e,t){var r=e.components,o=e.mdxType,i=e.originalType,c=e.parentName,s=p(e,["components","mdxType","originalType","parentName"]),u=l(r),m=o,y=u["".concat(c,".").concat(m)]||u[m]||d[m]||i;return r?n.createElement(y,a(a({ref:t},s),{},{components:r})):n.createElement(y,a({ref:t},s))}));function y(e,t){var r=arguments,o=t&&t.mdxType;if("string"==typeof e||o){var i=r.length,a=new Array(i);a[0]=m;var p={};for(var c in t)hasOwnProperty.call(t,c)&&(p[c]=t[c]);p.originalType=e,p[u]="string"==typeof e?e:o,a[1]=p;for(var l=2;l<i;l++)a[l]=r[l];return n.createElement.apply(null,a)}return n.createElement.apply(null,r)}m.displayName="MDXCreateElement"},48036:(e,t,r)=>{r.r(t),r.d(t,{assets:()=>c,contentTitle:()=>a,default:()=>d,frontMatter:()=>i,metadata:()=>p,toc:()=>l});var n=r(87462),o=(r(67294),r(3905));const i={},a="User Templates",p={unversionedId:"not_in_use/user_templates",id:"version-0.2.37/not_in_use/user_templates",title:"User Templates",description:"The CITROS CLI provides a convenient way to automatically copy any predefined files (e.g. notebooks)",source:"@site/versioned_docs/version-0.2.37/not_in_use/user_templates.md",sourceDirName:"not_in_use",slug:"/not_in_use/user_templates",permalink:"/docs/0.2.37/not_in_use/user_templates",draft:!1,tags:[],version:"0.2.37",frontMatter:{}},c={},l=[],s={toc:l},u="wrapper";function d(e){let{components:t,...r}=e;return(0,o.kt)(u,(0,n.Z)({},s,r,{components:t,mdxType:"MDXLayout"}),(0,o.kt)("h1",{id:"user-templates"},"User Templates"),(0,o.kt)("p",null,"The CITROS CLI provides a convenient way to automatically copy any predefined files (e.g. notebooks)\nfrom the user's project to the CITROS repo. Simply create a directory named ",(0,o.kt)("inlineCode",{parentName:"p"},"citros_template")," under your project directory, and inside\nit create any files and subdirectories that parallel the ",(0,o.kt)("inlineCode",{parentName:"p"},".citros")," directory structure."),(0,o.kt)("p",null,"For example, if you've created a notebook file named ",(0,o.kt)("inlineCode",{parentName:"p"},"test1.ipynb")," which you'd like to always be available by default in your ",(0,o.kt)("inlineCode",{parentName:"p"},".citros")," notebooks for this project, simply create a ",(0,o.kt)("inlineCode",{parentName:"p"},"citros_template/notebooks/")," directory under\nthe main directory of your project, and copy the file into it, i.e. "),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre"},"<your project>/citros_template/notebooks/test1.ipynb. \n")),(0,o.kt)("p",null,"From this point, when you run ",(0,o.kt)("inlineCode",{parentName:"p"},"citros init"),"\nfor this project, the file ",(0,o.kt)("inlineCode",{parentName:"p"},"test1.ipynb")," will be automatically copied to the ",(0,o.kt)("inlineCode",{parentName:"p"},"notebooks")," directory\nunder ",(0,o.kt)("inlineCode",{parentName:"p"},".citros"),"."))}d.isMDXComponent=!0}}]);
"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[92388],{3905:(e,t,r)=>{r.d(t,{Zo:()=>s,kt:()=>f});var n=r(67294);function o(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function a(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function i(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?a(Object(r),!0).forEach((function(t){o(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):a(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function c(e,t){if(null==e)return{};var r,n,o=function(e,t){if(null==e)return{};var r,n,o={},a=Object.keys(e);for(n=0;n<a.length;n++)r=a[n],t.indexOf(r)>=0||(o[r]=e[r]);return o}(e,t);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);for(n=0;n<a.length;n++)r=a[n],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(o[r]=e[r])}return o}var l=n.createContext({}),p=function(e){var t=n.useContext(l),r=t;return e&&(r="function"==typeof e?e(t):i(i({},t),e)),r},s=function(e){var t=p(e.components);return n.createElement(l.Provider,{value:t},e.children)},d="mdxType",u={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},m=n.forwardRef((function(e,t){var r=e.components,o=e.mdxType,a=e.originalType,l=e.parentName,s=c(e,["components","mdxType","originalType","parentName"]),d=p(r),m=o,f=d["".concat(l,".").concat(m)]||d[m]||u[m]||a;return r?n.createElement(f,i(i({ref:t},s),{},{components:r})):n.createElement(f,i({ref:t},s))}));function f(e,t){var r=arguments,o=t&&t.mdxType;if("string"==typeof e||o){var a=r.length,i=new Array(a);i[0]=m;var c={};for(var l in t)hasOwnProperty.call(t,l)&&(c[l]=t[l]);c.originalType=e,c[d]="string"==typeof e?e:o,i[1]=c;for(var p=2;p<a;p++)i[p]=r[p];return n.createElement.apply(null,i)}return n.createElement.apply(null,r)}m.displayName="MDXCreateElement"},3434:(e,t,r)=>{r.r(t),r.d(t,{assets:()=>l,contentTitle:()=>i,default:()=>u,frontMatter:()=>a,metadata:()=>c,toc:()=>p});var n=r(87462),o=(r(67294),r(3905));const a={sidebar_label:"CITROS Garden Projects"},i="CITROS Garden Project",c={unversionedId:"guides/citros_garden",id:"version-0.2.58/guides/citros_garden",title:"CITROS Garden Project",description:"CITROS Garden is an open-source organization holds different projects to explore CITROS abilities.",source:"@site/versioned_docs/version-0.2.58/guides/citros_garden.md",sourceDirName:"guides",slug:"/guides/citros_garden",permalink:"/docs/guides/citros_garden",draft:!1,tags:[],version:"0.2.58",frontMatter:{sidebar_label:"CITROS Garden Projects"}},l={},p=[{value:"Clone CITROS Garden Project",id:"clone-citros-garden-project",level:2},{value:"Run Project in VScode",id:"run-project-in-vscode",level:2},{value:"Open Project in VScode Dev Container",id:"open-project-in-vscode-dev-container",level:2},{value:"Build the project",id:"build-the-project",level:2}],s={toc:p},d="wrapper";function u(e){let{components:t,...a}=e;return(0,o.kt)(d,(0,n.Z)({},s,a,{components:t,mdxType:"MDXLayout"}),(0,o.kt)("h1",{id:"citros-garden-project"},"CITROS Garden Project"),(0,o.kt)("p",null,(0,o.kt)("a",{parentName:"p",href:"https://github.com/citros-garden"},"CITROS Garden")," is an open-source organization holds different projects to explore CITROS abilities. ",(0,o.kt)("br",null),"\nAll the projects can be found ",(0,o.kt)("a",{parentName:"p",href:"https://github.com/orgs/citros-garden/repositories"},"here")),(0,o.kt)("h2",{id:"clone-citros-garden-project"},"Clone CITROS Garden Project"),(0,o.kt)("p",null,"To clone the repository:"),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-sh"},"git clone git@github.com:citros-garden/repository_name.git\n")),(0,o.kt)("h2",{id:"run-project-in-vscode"},"Run Project in VScode"),(0,o.kt)("ol",null,(0,o.kt)("li",{parentName:"ol"},(0,o.kt)("p",{parentName:"li"},"Open the cloned repository in VScode:"),(0,o.kt)("pre",{parentName:"li"},(0,o.kt)("code",{parentName:"pre",className:"language-sh"},"cd ~/project-name\ncode .\n")))),(0,o.kt)("h2",{id:"open-project-in-vscode-dev-container"},"Open Project in VScode Dev Container"),(0,o.kt)("p",null,"We strongly recommend that you work with ",(0,o.kt)("a",{parentName:"p",href:"../guides/dockerfile_overview"},"dockers"),". ",(0,o.kt)("br",null),"\nHowever, if you wish to work without dockers, please refer to the .devcontainer in project's repository, the dependencies you need are in the ",(0,o.kt)("inlineCode",{parentName:"p"},"Dockerfile")," file."),(0,o.kt)("ol",null,(0,o.kt)("li",{parentName:"ol"},"Open and run Docker."),(0,o.kt)("li",{parentName:"ol"},"Press on the bottom left corner icon.")),(0,o.kt)("p",null,(0,o.kt)("img",{alt:"img",src:r(47724).Z,width:"1601",height:"881"})),(0,o.kt)("ol",{start:3},(0,o.kt)("li",{parentName:"ol"},"Choose ",(0,o.kt)("strong",{parentName:"li"},"Reopen in Container"))),(0,o.kt)("p",null,(0,o.kt)("img",{alt:"Alt text",src:r(13440).Z,width:"1601",height:"881"})),(0,o.kt)("ol",{start:4},(0,o.kt)("li",{parentName:"ol"},(0,o.kt)("p",{parentName:"li"},"Open VScode terminal and make sure you are in the right location. ",(0,o.kt)("br",null)),(0,o.kt)("pre",{parentName:"li"},(0,o.kt)("code",{parentName:"pre"},"ros@docker-desktop:/workspaces/[Project Name]$\n"))),(0,o.kt)("li",{parentName:"ol"},(0,o.kt)("p",{parentName:"li"},(0,o.kt)("a",{parentName:"p",href:"#build-the-project"},"Build the project")))),(0,o.kt)("h2",{id:"build-the-project"},"Build the project"),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-bash"},"$ colcon build\n$ source install/local_setup.bash\n")))}u.isMDXComponent=!0},47724:(e,t,r)=>{r.d(t,{Z:()=>n});const n=r.p+"assets/images/container_corner-f8c50033906f369e40bdaf20be574baf.png"},13440:(e,t,r)=>{r.d(t,{Z:()=>n});const n=r.p+"assets/images/container_open_container-41c041099556b7ec2a713ba2444c9d24.png"}}]);
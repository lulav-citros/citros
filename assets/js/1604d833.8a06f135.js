"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[8658],{3905:(e,n,t)=>{t.d(n,{Zo:()=>u,kt:()=>f});var r=t(67294);function o(e,n,t){return n in e?Object.defineProperty(e,n,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[n]=t,e}function i(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function a(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?i(Object(t),!0).forEach((function(n){o(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):i(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}function l(e,n){if(null==e)return{};var t,r,o=function(e,n){if(null==e)return{};var t,r,o={},i=Object.keys(e);for(r=0;r<i.length;r++)t=i[r],n.indexOf(t)>=0||(o[t]=e[t]);return o}(e,n);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(r=0;r<i.length;r++)t=i[r],n.indexOf(t)>=0||Object.prototype.propertyIsEnumerable.call(e,t)&&(o[t]=e[t])}return o}var c=r.createContext({}),s=function(e){var n=r.useContext(c),t=n;return e&&(t="function"==typeof e?e(n):a(a({},n),e)),t},u=function(e){var n=s(e.components);return r.createElement(c.Provider,{value:n},e.children)},p="mdxType",m={inlineCode:"code",wrapper:function(e){var n=e.children;return r.createElement(r.Fragment,{},n)}},d=r.forwardRef((function(e,n){var t=e.components,o=e.mdxType,i=e.originalType,c=e.parentName,u=l(e,["components","mdxType","originalType","parentName"]),p=s(t),d=o,f=p["".concat(c,".").concat(d)]||p[d]||m[d]||i;return t?r.createElement(f,a(a({ref:n},u),{},{components:t})):r.createElement(f,a({ref:n},u))}));function f(e,n){var t=arguments,o=n&&n.mdxType;if("string"==typeof e||o){var i=t.length,a=new Array(i);a[0]=d;var l={};for(var c in n)hasOwnProperty.call(n,c)&&(l[c]=n[c]);l.originalType=e,l[p]="string"==typeof e?e:o,a[1]=l;for(var s=2;s<i;s++)a[s]=t[s];return r.createElement.apply(null,a)}return r.createElement.apply(null,t)}d.displayName="MDXCreateElement"},84310:(e,n,t)=>{t.r(n),t.d(n,{assets:()=>c,contentTitle:()=>a,default:()=>m,frontMatter:()=>i,metadata:()=>l,toc:()=>s});var r=t(87462),o=(t(67294),t(3905));const i={},a=void 0,l={unversionedId:"commands/run",id:"version-0.2.36/commands/run",title:"run",description:"citros run",source:"@site/versioned_docs/version-0.2.36/commands/run.md",sourceDirName:"commands",slug:"/commands/run",permalink:"/docs/0.2.36/commands/run",draft:!1,tags:[],version:"0.2.36",frontMatter:{}},c={},s=[{value:"<code>citros run</code>",id:"citros-run",level:2},{value:"Description",id:"description",level:3},{value:"Prerequisites:",id:"prerequisites",level:4},{value:"Examples",id:"examples",level:4}],u={toc:s},p="wrapper";function m(e){let{components:n,...t}=e;return(0,o.kt)(p,(0,r.Z)({},u,t,{components:n,mdxType:"MDXLayout"}),(0,o.kt)("h2",{id:"citros-run"},(0,o.kt)("inlineCode",{parentName:"h2"},"citros run")),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-sh"},"$ citros run [dir <folder_name>] \n             [-d | --debug] \n             [-v | --verbose]\n             [-s, --simulation_name] \n             [-b, --batch_id]\n             [-n, --batch_name] \n             [-m, --batch_message] \n             [-i, --run_id] \n             [-c, --completions]\n             [-r, --remote] \n             [-k, --key] \n             [-l, --lan_traffic] \n             [--branch] \n             [--commit]\n")),(0,o.kt)("h3",{id:"description"},"Description"),(0,o.kt)("p",null,"The ",(0,o.kt)("inlineCode",{parentName:"p"},"run")," command launches a simulation either locally on your machine, or remotely on the CITROS cluster."),(0,o.kt)("h4",{id:"prerequisites"},"Prerequisites:"),(0,o.kt)("p",null,"Ensure that the project has been built and sourced, for example:"),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre"},"$ colcon build\n$ source install/local_setup.bash\n")),(0,o.kt)("p",null,"If you'd like to run your simulation remotely, you would also need to make sure:"),(0,o.kt)("ol",null,(0,o.kt)("li",{parentName:"ol"},"You're logged in (via ",(0,o.kt)("inlineCode",{parentName:"li"},"citros login"),")."),(0,o.kt)("li",{parentName:"ol"},"You've built and pushed a docker image of your project (using ",(0,o.kt)("inlineCode",{parentName:"li"},"citros docker-build-push"),")."),(0,o.kt)("li",{parentName:"ol"},"Your ",(0,o.kt)("inlineCode",{parentName:"li"},".citros")," directory is synched with the remote repository (using ",(0,o.kt)("inlineCode",{parentName:"li"},"citros commit")," and ",(0,o.kt)("inlineCode",{parentName:"li"},"citros push"),"). ")),(0,o.kt)("p",null,"If no simulation name was provided, an interactive session will begin, and you will be prompted to select a simulation from the list of available simulations (via up, down and enter keys). "),(0,o.kt)("h4",{id:"examples"},"Examples"),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-bash"},"$ citros run\n? Please choose the simulation you wish to run \n\u276f simulation_cannon_analytic\n    simulation_cannon_numeric\n")))}m.isMDXComponent=!0}}]);
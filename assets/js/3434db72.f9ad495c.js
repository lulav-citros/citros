"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[3433],{3905:(e,t,n)=>{n.d(t,{Zo:()=>u,kt:()=>h});var a=n(67294);function r(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function o(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);t&&(a=a.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,a)}return n}function i(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?o(Object(n),!0).forEach((function(t){r(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):o(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function l(e,t){if(null==e)return{};var n,a,r=function(e,t){if(null==e)return{};var n,a,r={},o=Object.keys(e);for(a=0;a<o.length;a++)n=o[a],t.indexOf(n)>=0||(r[n]=e[n]);return r}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(a=0;a<o.length;a++)n=o[a],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(r[n]=e[n])}return r}var s=a.createContext({}),c=function(e){var t=a.useContext(s),n=t;return e&&(n="function"==typeof e?e(t):i(i({},t),e)),n},u=function(e){var t=c(e.components);return a.createElement(s.Provider,{value:t},e.children)},p="mdxType",d={inlineCode:"code",wrapper:function(e){var t=e.children;return a.createElement(a.Fragment,{},t)}},m=a.forwardRef((function(e,t){var n=e.components,r=e.mdxType,o=e.originalType,s=e.parentName,u=l(e,["components","mdxType","originalType","parentName"]),p=c(n),m=r,h=p["".concat(s,".").concat(m)]||p[m]||d[m]||o;return n?a.createElement(h,i(i({ref:t},u),{},{components:n})):a.createElement(h,i({ref:t},u))}));function h(e,t){var n=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var o=n.length,i=new Array(o);i[0]=m;var l={};for(var s in t)hasOwnProperty.call(t,s)&&(l[s]=t[s]);l.originalType=e,l[p]="string"==typeof e?e:r,i[1]=l;for(var c=2;c<o;c++)i[c]=n[c];return a.createElement.apply(null,i)}return a.createElement.apply(null,n)}m.displayName="MDXCreateElement"},85162:(e,t,n)=>{n.d(t,{Z:()=>i});var a=n(67294),r=n(86010);const o={tabItem:"tabItem_Ymn6"};function i(e){let{children:t,hidden:n,className:i}=e;return a.createElement("div",{role:"tabpanel",className:(0,r.Z)(o.tabItem,i),hidden:n},t)}},74866:(e,t,n)=>{n.d(t,{Z:()=>v});var a=n(87462),r=n(67294),o=n(86010),i=n(12466),l=n(16550),s=n(91980),c=n(67392),u=n(50012);function p(e){return function(e){return r.Children.map(e,(e=>{if(!e||(0,r.isValidElement)(e)&&function(e){const{props:t}=e;return!!t&&"object"==typeof t&&"value"in t}(e))return e;throw new Error(`Docusaurus error: Bad <Tabs> child <${"string"==typeof e.type?e.type:e.type.name}>: all children of the <Tabs> component should be <TabItem>, and every <TabItem> should have a unique "value" prop.`)}))?.filter(Boolean)??[]}(e).map((e=>{let{props:{value:t,label:n,attributes:a,default:r}}=e;return{value:t,label:n,attributes:a,default:r}}))}function d(e){const{values:t,children:n}=e;return(0,r.useMemo)((()=>{const e=t??p(n);return function(e){const t=(0,c.l)(e,((e,t)=>e.value===t.value));if(t.length>0)throw new Error(`Docusaurus error: Duplicate values "${t.map((e=>e.value)).join(", ")}" found in <Tabs>. Every value needs to be unique.`)}(e),e}),[t,n])}function m(e){let{value:t,tabValues:n}=e;return n.some((e=>e.value===t))}function h(e){let{queryString:t=!1,groupId:n}=e;const a=(0,l.k6)(),o=function(e){let{queryString:t=!1,groupId:n}=e;if("string"==typeof t)return t;if(!1===t)return null;if(!0===t&&!n)throw new Error('Docusaurus error: The <Tabs> component groupId prop is required if queryString=true, because this value is used as the search param name. You can also provide an explicit value such as queryString="my-search-param".');return n??null}({queryString:t,groupId:n});return[(0,s._X)(o),(0,r.useCallback)((e=>{if(!o)return;const t=new URLSearchParams(a.location.search);t.set(o,e),a.replace({...a.location,search:t.toString()})}),[o,a])]}function k(e){const{defaultValue:t,queryString:n=!1,groupId:a}=e,o=d(e),[i,l]=(0,r.useState)((()=>function(e){let{defaultValue:t,tabValues:n}=e;if(0===n.length)throw new Error("Docusaurus error: the <Tabs> component requires at least one <TabItem> children component");if(t){if(!m({value:t,tabValues:n}))throw new Error(`Docusaurus error: The <Tabs> has a defaultValue "${t}" but none of its children has the corresponding value. Available values are: ${n.map((e=>e.value)).join(", ")}. If you intend to show no default tab, use defaultValue={null} instead.`);return t}const a=n.find((e=>e.default))??n[0];if(!a)throw new Error("Unexpected error: 0 tabValues");return a.value}({defaultValue:t,tabValues:o}))),[s,c]=h({queryString:n,groupId:a}),[p,k]=function(e){let{groupId:t}=e;const n=function(e){return e?`docusaurus.tab.${e}`:null}(t),[a,o]=(0,u.Nk)(n);return[a,(0,r.useCallback)((e=>{n&&o.set(e)}),[n,o])]}({groupId:a}),g=(()=>{const e=s??p;return m({value:e,tabValues:o})?e:null})();(0,r.useLayoutEffect)((()=>{g&&l(g)}),[g]);return{selectedValue:i,selectValue:(0,r.useCallback)((e=>{if(!m({value:e,tabValues:o}))throw new Error(`Can't select invalid tab value=${e}`);l(e),c(e),k(e)}),[c,k,o]),tabValues:o}}var g=n(72389);const b={tabList:"tabList__CuJ",tabItem:"tabItem_LNqP"};function f(e){let{className:t,block:n,selectedValue:l,selectValue:s,tabValues:c}=e;const u=[],{blockElementScrollPositionUntilNextRender:p}=(0,i.o5)(),d=e=>{const t=e.currentTarget,n=u.indexOf(t),a=c[n].value;a!==l&&(p(t),s(a))},m=e=>{let t=null;switch(e.key){case"Enter":d(e);break;case"ArrowRight":{const n=u.indexOf(e.currentTarget)+1;t=u[n]??u[0];break}case"ArrowLeft":{const n=u.indexOf(e.currentTarget)-1;t=u[n]??u[u.length-1];break}}t?.focus()};return r.createElement("ul",{role:"tablist","aria-orientation":"horizontal",className:(0,o.Z)("tabs",{"tabs--block":n},t)},c.map((e=>{let{value:t,label:n,attributes:i}=e;return r.createElement("li",(0,a.Z)({role:"tab",tabIndex:l===t?0:-1,"aria-selected":l===t,key:t,ref:e=>u.push(e),onKeyDown:m,onClick:d},i,{className:(0,o.Z)("tabs__item",b.tabItem,i?.className,{"tabs__item--active":l===t})}),n??t)})))}function y(e){let{lazy:t,children:n,selectedValue:a}=e;const o=(Array.isArray(n)?n:[n]).filter(Boolean);if(t){const e=o.find((e=>e.props.value===a));return e?(0,r.cloneElement)(e,{className:"margin-top--md"}):null}return r.createElement("div",{className:"margin-top--md"},o.map(((e,t)=>(0,r.cloneElement)(e,{key:t,hidden:e.props.value!==a}))))}function N(e){const t=k(e);return r.createElement("div",{className:(0,o.Z)("tabs-container",b.tabList)},r.createElement(f,(0,a.Z)({},e,t)),r.createElement(y,(0,a.Z)({},e,t)))}function v(e){const t=(0,g.Z)();return r.createElement(N,(0,a.Z)({key:String(t)},e))}},1441:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>u,contentTitle:()=>s,default:()=>h,frontMatter:()=>l,metadata:()=>c,toc:()=>p});var a=n(87462),r=(n(67294),n(3905)),o=n(74866),i=n(85162);const l={sidebar_position:1,sidebar_label:"Getting Started"},s="Getting Started",c={unversionedId:"guides/getting_started_old",id:"version-0.2.49/guides/getting_started_old",title:"Getting Started",description:"Prerequisites for Working With CITROS",source:"@site/versioned_docs/version-0.2.49/guides/getting_started_old.md",sourceDirName:"guides",slug:"/guides/getting_started_old",permalink:"/docs/0.2.49/guides/getting_started_old",draft:!1,tags:[],version:"0.2.49",sidebarPosition:1,frontMatter:{sidebar_position:1,sidebar_label:"Getting Started"}},u={},p=[{value:"Prerequisites for Working With CITROS",id:"prerequisites-for-working-with-citros",level:2},{value:"Softwares to Work with CITROS",id:"softwares-to-work-with-citros",level:3},{value:"Working With CITROS on Web",id:"working-with-citros-on-web",level:3},{value:"Installation",id:"installation",level:2},{value:"Clone CITROS Garden Project",id:"clone-citros-garden-project",level:2},{value:"Run Project in VScode",id:"run-project-in-vscode",level:2},{value:"Open Project in VScode Dev Container",id:"open-project-in-vscode-dev-container",level:3},{value:"Build the project",id:"build-the-project",level:3},{value:"Initialization",id:"initialization",level:2},{value:"Log in to CITROS",id:"log-in-to-citros",level:3},{value:"Set up SSH",id:"set-up-ssh",level:3},{value:"Init CITROS",id:"init-citros",level:3},{value:"Before Running <code>citros init</code>",id:"before-running-citros-init",level:4},{value:"Running <code>citros init</code>",id:"running-citros-init",level:4},{value:"Upload to CITROS Server",id:"upload-to-citros-server",level:2},{value:"Simulation Running Options",id:"simulation-running-options",level:2},{value:"The basic run command is",id:"the-basic-run-command-is",level:4},{value:"To run more than one simulation add <code>-c number</code>",id:"to-run-more-than-one-simulation-add--c-number",level:4},{value:"To run the simulation on the cloud add <code>-r</code>",id:"to-run-the-simulation-on-the-cloud-add--r",level:4}],d={toc:p},m="wrapper";function h(e){let{components:t,...l}=e;return(0,r.kt)(m,(0,a.Z)({},d,l,{components:t,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"getting-started"},"Getting Started"),(0,r.kt)("h2",{id:"prerequisites-for-working-with-citros"},"Prerequisites for Working With CITROS"),(0,r.kt)("h3",{id:"softwares-to-work-with-citros"},"Softwares to Work with CITROS"),(0,r.kt)("p",null,"Download and install the following to work with CITROS"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("a",{parentName:"li",href:"https://www.python.org/downloads/"},"Python3")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("a",{parentName:"li",href:"https://git-scm.com/"},"git")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("a",{parentName:"li",href:"https://docs.docker.com/get-docker/"},"Docker")," - To understand why CITROS uses Docker, read ",(0,r.kt)("a",{parentName:"li",href:"../guides/dockerfile_overview"},"CITROS usage in Dockerfile"),".")),(0,r.kt)("h3",{id:"working-with-citros-on-web"},"Working With CITROS on Web"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"You need a working internet connection."),(0,r.kt)("li",{parentName:"ul"},"Sign up to ",(0,r.kt)("a",{parentName:"li",href:"https://citros.io"},"CITROS")," and remember your login credentials.")),(0,r.kt)("h2",{id:"installation"},"Installation"),(0,r.kt)("p",null,"To install CITROS using pip, open terminal and write the following command:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},"$ pip install citros \n")),(0,r.kt)("p",null,"You can verify that the installation succeeded by running "),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-bash"},"$ citros -V\n")),(0,r.kt)("admonition",{type:"tip"},(0,r.kt)("p",{parentName:"admonition"},"If you ran the ",(0,r.kt)("inlineCode",{parentName:"p"},"pip install citros")," command and you still getting "),(0,r.kt)("pre",{parentName:"admonition"},(0,r.kt)("code",{parentName:"pre",className:"language-bash"}," $ citros: command not found\n")),(0,r.kt)("p",{parentName:"admonition"},"Try running:"),(0,r.kt)("pre",{parentName:"admonition"},(0,r.kt)("code",{parentName:"pre",className:"language-bash"}," $ source ~/.profile \n")),(0,r.kt)("p",{parentName:"admonition"},"This should solve your problem and you should be able to run citros commands, otherwise ",(0,r.kt)("a",{parentName:"p",href:"https://discord.com/"},"contact us"),".")),(0,r.kt)("h2",{id:"clone-citros-garden-project"},"Clone CITROS Garden Project"),(0,r.kt)("p",null,"All the projects can be found ",(0,r.kt)("a",{parentName:"p",href:"https://github.com/orgs/citros-garden/repositories"},"here")),(0,r.kt)("p",null,"To clone the repository:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sh"},"git clone git@github.com:citros-garden/repository_name.git\n")),(0,r.kt)("h2",{id:"run-project-in-vscode"},"Run Project in VScode"),(0,r.kt)("h3",{id:"open-project-in-vscode-dev-container"},"Open Project in VScode Dev Container"),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("p",{parentName:"li"},"Open the cloned repository in VScode:"),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-sh"},"cd ~/project-name\ncode .\n"))),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("p",{parentName:"li"},"Open and run Docker.")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("p",{parentName:"li"},"Open the project in VScode.")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("p",{parentName:"li"},"Press on the bottom left corner icon."))),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"Alt text",src:n(99940).Z,width:"1601",height:"881"})),(0,r.kt)("ol",{start:5},(0,r.kt)("li",{parentName:"ol"},"Choose ",(0,r.kt)("strong",{parentName:"li"},"Reopen in Container"))),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"Alt text",src:n(71899).Z,width:"1601",height:"881"})),(0,r.kt)("ol",{start:6},(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("p",{parentName:"li"},"Open VScode terminal and make sure you are in the right location. ",(0,r.kt)("br",null)),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre"},"ros@docker-desktop:/workspaces/[Project Name]$\n"))),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("p",{parentName:"li"},(0,r.kt)("a",{parentName:"p",href:"#build-the-project"},"Build the project")))),(0,r.kt)("h3",{id:"build-the-project"},"Build the project"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-bash"},"$ colcon build\n$ source install/local_setup.bash\n")),(0,r.kt)("h2",{id:"initialization"},"Initialization"),(0,r.kt)("h3",{id:"log-in-to-citros"},"Log in to CITROS"),(0,r.kt)("p",null,"First and foremost, we need to log in:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-bash"},"$ citros login\nemail: example@lulav.space\nPassword: \nUser logged in.\n")),(0,r.kt)("h3",{id:"set-up-ssh"},"Set up SSH"),(0,r.kt)("p",null,"This process only needs to be performed once per machine, and can be performed either using the CITROS website or using CITROS CLI"),(0,r.kt)(o.Z,{mdxType:"Tabs"},(0,r.kt)(i.Z,{value:"citros_cli",label:"SSH Setup with CITROS CLI",mdxType:"TabItem"},(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-bash"},"citros setup-ssh\n")),(0,r.kt)("p",null,"for further details, see the ",(0,r.kt)("a",{parentName:"p",href:"https://citros.io/doc/docs_cli"},"CLI Documentation"))),(0,r.kt)(i.Z,{value:"citros_web",label:"SSH Setup with CITROS Website",mdxType:"TabItem"},(0,r.kt)("ol",{start:2},(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("p",{parentName:"li"},(0,r.kt)("a",{parentName:"p",href:"https://citros.io/settings?tab=ssh_keys"},"Navigate to SSH Keys Settings"),".")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("p",{parentName:"li"},'Click "New SSH Key" button')),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("p",{parentName:"li"},"Enter SSH key name.")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("p",{parentName:"li"},"Paste the public key.")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("p",{parentName:"li"},'Click "Add" button to add the SSH Key to the account.')),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("p",{parentName:"li"},"The new key will be added to the list item."))),(0,r.kt)("p",null,"for further details, see the ",(0,r.kt)("a",{parentName:"p",href:"https://citros.io/doc/docs/authentication/ssh/ssh_add_new"},"Adding a New SSH Key Documentation")))),(0,r.kt)("h3",{id:"init-citros"},"Init CITROS"),(0,r.kt)("h4",{id:"before-running-citros-init"},"Before Running ",(0,r.kt)("inlineCode",{parentName:"h4"},"citros init")),(0,r.kt)("p",null,"First and foremost, the ",(0,r.kt)("inlineCode",{parentName:"p"},".citros")," directory can only be ",(0,r.kt)("strong",{parentName:"p"},"initialized once"),".\nIf the ",(0,r.kt)("inlineCode",{parentName:"p"},".citros")," directory exists in your local project and the project ",(0,r.kt)("a",{parentName:"p",href:"https://citros.io/cannon"},(0,r.kt)("strong",{parentName:"a"},"already exists on the remote server")),", you have to delete the ",(0,r.kt)("inlineCode",{parentName:"p"},".citros")," directory from your project before\nrunning ",(0,r.kt)("inlineCode",{parentName:"p"},"citros init")," command."),(0,r.kt)("p",null,"To Check if the project already exists on the remote server:"),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("p",{parentName:"li"},"go to ",(0,r.kt)("a",{parentName:"p",href:"https://citros.io/repo"},"repositories"))),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("p",{parentName:"li"},"Look for your project name either by scrolling through the list or using the search box.")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("p",{parentName:"li"},"If you didn't find your project you may skip the next step.")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("p",{parentName:"li"},"if you found the project, delete the ",(0,r.kt)("inlineCode",{parentName:"p"},".citros")," directory ",(0,r.kt)("strong",{parentName:"p"},"from your local project"),". ")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("p",{parentName:"li"},"you may continue to the ",(0,r.kt)("a",{parentName:"p",href:"#running-citros-init"},"next step"),". "))),(0,r.kt)("h4",{id:"running-citros-init"},"Running ",(0,r.kt)("inlineCode",{parentName:"h4"},"citros init")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-bash"},"$ citros init\nChecking internet connection...\nChecking ssh...\nUpdating Citros...\nWaiting for repo to be ready...\nCitros repo successfully cloned from remote.\nCreating and checking out a new local branch `main` that will track the remote branch.\nDefault branch of remote 'origin' set to: main\nCitros successfully synched with local project.\nYou may review your changes via `citros status` and commit them via `citros commit`.\nInitialized Citros repository.\n")),(0,r.kt)("p",null,"As you can see, a lot more is happening when you initialize your repository while being logged in. We will not delve into all the details behind the scenes, but as always, feel free to roam through the ",(0,r.kt)("a",{parentName:"p",href:"https://citros.io/doc/docs_cli"},"CLI Documentation")," for further details."),(0,r.kt)("admonition",{title:"Warning",type:"caution"},(0,r.kt)("p",{parentName:"admonition"}," If you try to run ",(0,r.kt)("inlineCode",{parentName:"p"},"init")," while a ",(0,r.kt)("inlineCode",{parentName:"p"},".citros")," directory already exists in your project, you will get a response similar to this:"),(0,r.kt)("pre",{parentName:"admonition"},(0,r.kt)("code",{parentName:"pre",className:"language-bash"},"$ citros init\nThe directory /workspaces/cannon has already been initialized.\nworking remotely with [git@citros.io:lulav/cannon.git].\n")),(0,r.kt)("ol",{parentName:"admonition"},(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("p",{parentName:"li"},"If you want to reinitialize your CITROS repository, you'll have to first delete the current ",(0,r.kt)("inlineCode",{parentName:"p"},".citros")," directory.")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("p",{parentName:"li"},"If you initialized the CITROS repository offline, and it ",(0,r.kt)("a",{parentName:"p",href:"https://citros.io/cannon"},(0,r.kt)("strong",{parentName:"a"},"doesn't exist")," on the remote server yet")," (i.e. it has not been initialized online by you or anyone else) - then rather than deleting the ",(0,r.kt)("inlineCode",{parentName:"p"},".citros")," directory, you can run:"),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-bash"},"citros add-remote\n")),(0,r.kt)("p",{parentName:"li"},"which will add the CITROS server as a remote for your CITROS repo on your behalf, and take care of a few other details that are handled when initializing while being logged in."),(0,r.kt)("p",{parentName:"li"},"At this point it is recommended you commit and push your changes to the remote by running:"),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-bash"},"citros commit\ncitros push\n"))))),(0,r.kt)("h2",{id:"upload-to-citros-server"},"Upload to CITROS Server"),(0,r.kt)("p",null,"The working directory of your ROS project must be clean. So if you made any changes, simply commit your changes first."),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sh"}," citros commit\n citros push\n")),(0,r.kt)("p",null,"To run a simulation on the cloud - we need to build a docker image of our ROS project, tag it with the current commit hash for the project, and upload it to CITROS.\nall this is accomplished by running a single command:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-bash"},"citros docker-build-push\n")),(0,r.kt)("h2",{id:"simulation-running-options"},"Simulation Running Options"),(0,r.kt)("h4",{id:"the-basic-run-command-is"},"The basic run command is"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sh"},"citros run -n 'batch_name' -m 'batch_message'\n")),(0,r.kt)("p",null,"This command will run the simulation on your machine, and save all the results under ",(0,r.kt)("inlineCode",{parentName:"p"},".citros/runs/[simulation_name]")," folder. The content of the folder will contain"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"recorded bags"),(0,r.kt)("li",{parentName:"ul"},"logs from the simulation and citros itself"),(0,r.kt)("li",{parentName:"ul"},"metadata about the run"),(0,r.kt)("li",{parentName:"ul"},"metrics and information about the system it was running"),(0,r.kt)("li",{parentName:"ul"},"and more.")),(0,r.kt)("h4",{id:"to-run-more-than-one-simulation-add--c-number"},"To run more than one simulation add ",(0,r.kt)("inlineCode",{parentName:"h4"},"-c number")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sh"},"citros run -n 'batch_name' -m 'batch_message' -c 15\n")),(0,r.kt)("p",null,"This will run 15 simulation and all will be saved as explained above."),(0,r.kt)("h4",{id:"to-run-the-simulation-on-the-cloud-add--r"},"To run the simulation on the cloud add ",(0,r.kt)("inlineCode",{parentName:"h4"},"-r")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sh"},"citros run -n 'batch_name' -m 'batch_message' -r\n")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sh"},"citros run -n 'batch_name' -m 'batch_message' -r 15\n")),(0,r.kt)("p",null,"after you execute a remote (-r) run command, a link directly to the ",(0,r.kt)("em",{parentName:"p"},"runs")," tab on the CITROS website will appear in the output"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-bash"},"created new batch_id: aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeeeee. Running on Citros cluster. See https://citros.io/cannon/batch/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeeeee.\n")),(0,r.kt)("p",null,"For mor run commands parameters and options check ",(0,r.kt)("a",{parentName:"p",href:"/docs/cli/cli_commands"},"CLI Commands"),"."))}h.isMDXComponent=!0},99940:(e,t,n)=>{n.d(t,{Z:()=>a});const a=n.p+"assets/images/container_corner-f8c50033906f369e40bdaf20be574baf.png"},71899:(e,t,n)=>{n.d(t,{Z:()=>a});const a=n.p+"assets/images/container_open_container-41c041099556b7ec2a713ba2444c9d24.png"}}]);
"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[81656],{3905:(e,t,a)=>{a.d(t,{Zo:()=>m,kt:()=>h});var n=a(67294);function s(e,t,a){return t in e?Object.defineProperty(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}function i(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,n)}return a}function r(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?i(Object(a),!0).forEach((function(t){s(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):i(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}function o(e,t){if(null==e)return{};var a,n,s=function(e,t){if(null==e)return{};var a,n,s={},i=Object.keys(e);for(n=0;n<i.length;n++)a=i[n],t.indexOf(a)>=0||(s[a]=e[a]);return s}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(n=0;n<i.length;n++)a=i[n],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(s[a]=e[a])}return s}var c=n.createContext({}),l=function(e){var t=n.useContext(c),a=t;return e&&(a="function"==typeof e?e(t):r(r({},t),e)),a},m=function(e){var t=l(e.components);return n.createElement(c.Provider,{value:t},e.children)},p="mdxType",d={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},u=n.forwardRef((function(e,t){var a=e.components,s=e.mdxType,i=e.originalType,c=e.parentName,m=o(e,["components","mdxType","originalType","parentName"]),p=l(a),u=s,h=p["".concat(c,".").concat(u)]||p[u]||d[u]||i;return a?n.createElement(h,r(r({ref:t},m),{},{components:a})):n.createElement(h,r({ref:t},m))}));function h(e,t){var a=arguments,s=t&&t.mdxType;if("string"==typeof e||s){var i=a.length,r=new Array(i);r[0]=u;var o={};for(var c in t)hasOwnProperty.call(t,c)&&(o[c]=t[c]);o.originalType=e,o[p]="string"==typeof e?e:s,r[1]=o;for(var l=2;l<i;l++)r[l]=a[l];return n.createElement.apply(null,r)}return n.createElement.apply(null,a)}u.displayName="MDXCreateElement"},9519:(e,t,a)=>{a.r(t),a.d(t,{assets:()=>c,contentTitle:()=>r,default:()=>d,frontMatter:()=>i,metadata:()=>o,toc:()=>l});var n=a(87462),s=(a(67294),a(3905));const i={toc_max_heading_level:4,hide_title:!0,sidebar_position:2,sidebar_label:"Simulations and Batches",description:"Simulations and Batches"},r="Simulations and Batches",o={unversionedId:"data_analysis/data_access/batch_overview",id:"version-0.2.40/data_analysis/data_access/batch_overview",title:"Simulations and Batches",description:"Simulations and Batches",source:"@site/versioned_docs/version-0.2.40/data_analysis/data_access/batch_overview.md",sourceDirName:"data_analysis/data_access",slug:"/data_analysis/data_access/batch_overview",permalink:"/docs/data_analysis/data_access/batch_overview",draft:!1,tags:[],version:"0.2.40",sidebarPosition:2,frontMatter:{toc_max_heading_level:4,hide_title:!0,sidebar_position:2,sidebar_label:"Simulations and Batches",description:"Simulations and Batches"},sidebar:"gettingStartedSidebar",previous:{title:"Getting Started",permalink:"/docs/data_analysis/data_access/getting_started"},next:{title:"Batch Content",permalink:"/docs/data_analysis/data_access/batch_content"}},c={},l=[{value:"Setting Simulation",id:"setting-simulation",level:2},{value:"Setting Batch",id:"setting-batch",level:2},{value:"Batch Sizes",id:"batch-sizes",level:2}],m={toc:l},p="wrapper";function d(e){let{components:t,...a}=e;return(0,s.kt)(p,(0,n.Z)({},m,a,{components:t,mdxType:"MDXLayout"}),(0,s.kt)("h1",{id:"simulations-and-batches"},"Simulations and Batches"),(0,s.kt)("p",null,(0,s.kt)("em",{parentName:"p"},"Batches")," (tables with data) are created by various ",(0,s.kt)("em",{parentName:"p"},"simulation")," scenarios and stored in the database under corresponding ",(0,s.kt)("em",{parentName:"p"},"simulation")," names. To access a specific batch, both its name and the name of the simulation are needed."),(0,s.kt)("h2",{id:"setting-simulation"},"Setting Simulation"),(0,s.kt)("p",null,"Simulation name can be set when the ",(0,s.kt)("a",{parentName:"p",href:"/docs/data_analysis/data_access/getting_started#connection-to-the-database"},(0,s.kt)("strong",{parentName:"a"},"CitrosDB"))," object is created:"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> from citros import CitrosDB\n>>> citros = CitrosDB(simulation = 'simulation_name')\n")),(0,s.kt)("p",null,"or by the method ",(0,s.kt)("a",{parentName:"p",href:"/docs/data_analysis/documentation/access/citros_db#access.citros_db.CitrosDB.simulation"},(0,s.kt)("strong",{parentName:"a"},"simulation()")),", like in the following example:"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> citros.simulation('simulation_name').batch('batch_name').data()\n")),(0,s.kt)("p",null,"If the simulation is specified during the creation of the ",(0,s.kt)("a",{parentName:"p",href:"/docs/data_analysis/data_access/getting_started#connection-to-the-database"},(0,s.kt)("strong",{parentName:"a"},"CitrosDB"))," object, the simulation name will be saved and used in all subsequent queries. The ",(0,s.kt)("a",{parentName:"p",href:"/docs/data_analysis/documentation/access/citros_db#access.citros_db.CitrosDB.simulation"},(0,s.kt)("strong",{parentName:"a"},"simulation()"))," method does not save the simulation name. This option can be beneficial if you plan to work with batches from different simulations and want to explicitly specify which one you are using each time. However, it is possible to set the simulation name for an existing ",(0,s.kt)("a",{parentName:"p",href:"/docs/data_analysis/data_access/getting_started#connection-to-the-database"},(0,s.kt)("strong",{parentName:"a"},"CitrosDB"))," object by passing the parameter ",(0,s.kt)("inlineCode",{parentName:"p"},"inplace")," = True. Observe the differences between using the ",(0,s.kt)("a",{parentName:"p",href:"/docs/data_analysis/documentation/access/citros_db#access.citros_db.CitrosDB.simulation"},(0,s.kt)("strong",{parentName:"a"},"simulation()"))," method with and without the ",(0,s.kt)("inlineCode",{parentName:"p"},"inplace")," = True parameter:"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> citros.simulation('simulation_name')\n>>> print(f\"simulation name: {citros.get_simulation_name()}\")\n")),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-text"},"simulation name: None\n")),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> citros.simulation('simulation_name', inplace = True)\n>>> print(f\"simulation name: {citros.get_simulation_name()}\")\n")),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-text"},"simulation name: simulation_name\n")),(0,s.kt)("p",null,"Method ",(0,s.kt)("a",{parentName:"p",href:"/docs/data_analysis/documentation/access/citros_db#access.citros_db.CitrosDB.get_simulation_name"},(0,s.kt)("strong",{parentName:"a"},"get_simulation_name"))," returns the name of the set simulation."),(0,s.kt)("h2",{id:"setting-batch"},"Setting Batch"),(0,s.kt)("p",null,"The batch is set either when ",(0,s.kt)("a",{parentName:"p",href:"/docs/data_analysis/data_access/getting_started#connection-to-the-database"},(0,s.kt)("strong",{parentName:"a"},"CitrosDB"))," object is created by passing a batch name by ",(0,s.kt)("inlineCode",{parentName:"p"},"batch")," argument:"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> citros = CitrosDB(batch = 'batch_name')\n")),(0,s.kt)("p",null,"or later, for example before ",(0,s.kt)("a",{parentName:"p",href:"/docs/data_analysis/data_access/query_data#query-data"},"querying data"),", by method ",(0,s.kt)("a",{parentName:"p",href:"/docs/data_analysis/documentation/access/citros_db#access.citros_db.CitrosDB.batch"},(0,s.kt)("strong",{parentName:"a"},"batch()")),":"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> citros = CitrosDB()\n>>> citros.simulation('simulation_name').batch('batch_name').data()\n")),(0,s.kt)("p",null,"The difference between these two approaches is the same as in ",(0,s.kt)("a",{parentName:"p",href:"#setting-simulation"},"Setting Simulation"),":"),(0,s.kt)("ul",null,(0,s.kt)("li",{parentName:"ul"},"In the first case, the ",(0,s.kt)("a",{parentName:"li",href:"/docs/data_analysis/data_access/getting_started#connection-to-the-database"},(0,s.kt)("strong",{parentName:"a"},"CitrosDB"))," object saves the ",(0,s.kt)("inlineCode",{parentName:"li"},"batch")," name, so you do not need to specify it each time you access the batch."),(0,s.kt)("li",{parentName:"ul"},"In the second option, the batch name is not saved; the method ",(0,s.kt)("a",{parentName:"li",href:"/docs/data_analysis/documentation/access/citros_db#access.citros_db.CitrosDB.batch"},(0,s.kt)("strong",{parentName:"a"},"batch()"))," simply returns a new ",(0,s.kt)("a",{parentName:"li",href:"/docs/data_analysis/data_access/getting_started#connection-to-the-database"},(0,s.kt)("strong",{parentName:"a"},"CitrosDB"))," object with the ",(0,s.kt)("inlineCode",{parentName:"li"},"batch")," parameter set, that can be used further in a chain of methods, for example, to query data, as shown in the example above. The batch name can still be set to the existing ",(0,s.kt)("a",{parentName:"li",href:"/docs/data_analysis/data_access/getting_started#connection-to-the-database"},(0,s.kt)("strong",{parentName:"a"},"CitrosDB"))," object if the parameter ",(0,s.kt)("inlineCode",{parentName:"li"},"inplace")," = True is used. Without the ",(0,s.kt)("inlineCode",{parentName:"li"},"inplace")," parameter, the batch name will not be saved to the current CitrosDB object, enhancing readability by always making clear which batch you are currently using and ensuring that previous settings do not affect your future work:")),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> citros = CitrosDB()\n>>> citros.batch('batch_name').data()\n>>> #some steps...\n>>> print(f\"current batch name: {citros.get_batch_name()}\")\n")),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-text"},"current batch name: None\n")),(0,s.kt)("p",null,"However, if you prefer to work with just one batch and don't want to specify it every time, set ",(0,s.kt)("inlineCode",{parentName:"p"},"inplace")," to True. This will save the batch id and batch name in the settings of the current ",(0,s.kt)("inlineCode",{parentName:"p"},"CitrosDB")," object:"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> citros.batch('batch_name', inplace = True)\n>>> print(f\"current batch name: {citros.get_batch_name()}\")\n")),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-text"},"current batch name: batch_name\n")),(0,s.kt)("p",null,"The method ",(0,s.kt)("a",{parentName:"p",href:"/docs/data_analysis/documentation/access/citros_db#access.citros_db.CitrosDB.get_batch_name"},(0,s.kt)("strong",{parentName:"a"},"get_batch_name()"))," returns the name of the batch."),(0,s.kt)("h2",{id:"batch-sizes"},"Batch Sizes"),(0,s.kt)("p",null,"To list sizes of the all batches uploaded to the database the method ",(0,s.kt)("a",{parentName:"p",href:"/docs/data_analysis/documentation/access/citros_db#access.citros_db.CitrosDB.get_batch_sizes"},(0,s.kt)("strong",{parentName:"a"},"get_batch_sizes()"))," is used:"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> citros = CitrosDB()\n>>> citros.get_batch_sizes()\n")),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-text"},"+---------------------------+--------+------------+\n| batch                     | size   | total size |\n+---------------------------+--------+------------+\n| galaxies                  | 656 kB | 800 kB     |\n| quasars                   | 32 kB  | 64 kB      |\n| stars                     | 808 kB | 960 kB     |\n+---------------------------+--------+------------+\n")),(0,s.kt)("p",null,"To show information about the batches of the certain simulation, specify the simulation name. For example, if two batches - 'galaxies' and 'quasars' - belongs to the simulation named 'simulation_deep_space', their sizes can be shown in the following way:"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> citros = CitrosDB()\n>>> citros.simulation('simulation_deep_space').get_batch_sizes()\n")),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-text"},"+---------------------------+--------+------------+\n| batch                     | size   | total size |\n+---------------------------+--------+------------+\n| galaxies                  | 656 kB | 800 kB     |\n| quasars                   | 32 kB  | 64 kB      |\n+---------------------------+--------+------------+\n")),(0,s.kt)("p",null,"And if we also specify the name of the batch, only information about it will be displayed:"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> citros = CitrosDB()\n>>> citros.simulation('simulation').batch('galaxies').get_batch_sizes()\n")),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-text"},"+---------------------------+--------+------------+\n| batch                     | size   | total size |\n+---------------------------+--------+------------+\n| galaxies                  | 656 kB | 800 kB     |\n+---------------------------+--------+------------+\n")))}d.isMDXComponent=!0}}]);
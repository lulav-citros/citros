"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[31346],{3905:(t,a,e)=>{e.d(a,{Zo:()=>m,kt:()=>k});var n=e(67294);function r(t,a,e){return a in t?Object.defineProperty(t,a,{value:e,enumerable:!0,configurable:!0,writable:!0}):t[a]=e,t}function i(t,a){var e=Object.keys(t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(t);a&&(n=n.filter((function(a){return Object.getOwnPropertyDescriptor(t,a).enumerable}))),e.push.apply(e,n)}return e}function l(t){for(var a=1;a<arguments.length;a++){var e=null!=arguments[a]?arguments[a]:{};a%2?i(Object(e),!0).forEach((function(a){r(t,a,e[a])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(e)):i(Object(e)).forEach((function(a){Object.defineProperty(t,a,Object.getOwnPropertyDescriptor(e,a))}))}return t}function s(t,a){if(null==t)return{};var e,n,r=function(t,a){if(null==t)return{};var e,n,r={},i=Object.keys(t);for(n=0;n<i.length;n++)e=i[n],a.indexOf(e)>=0||(r[e]=t[e]);return r}(t,a);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(t);for(n=0;n<i.length;n++)e=i[n],a.indexOf(e)>=0||Object.prototype.propertyIsEnumerable.call(t,e)&&(r[e]=t[e])}return r}var o=n.createContext({}),d=function(t){var a=n.useContext(o),e=a;return t&&(e="function"==typeof t?t(a):l(l({},a),t)),e},m=function(t){var a=d(t.components);return n.createElement(o.Provider,{value:a},t.children)},p="mdxType",u={inlineCode:"code",wrapper:function(t){var a=t.children;return n.createElement(n.Fragment,{},a)}},c=n.forwardRef((function(t,a){var e=t.components,r=t.mdxType,i=t.originalType,o=t.parentName,m=s(t,["components","mdxType","originalType","parentName"]),p=d(e),c=r,k=p["".concat(o,".").concat(c)]||p[c]||u[c]||i;return e?n.createElement(k,l(l({ref:a},m),{},{components:e})):n.createElement(k,l({ref:a},m))}));function k(t,a){var e=arguments,r=a&&a.mdxType;if("string"==typeof t||r){var i=e.length,l=new Array(i);l[0]=c;var s={};for(var o in a)hasOwnProperty.call(a,o)&&(s[o]=a[o]);s.originalType=t,s[p]="string"==typeof t?t:r,l[1]=s;for(var d=2;d<i;d++)l[d]=e[d];return n.createElement.apply(null,l)}return n.createElement.apply(null,e)}c.displayName="MDXCreateElement"},76406:(t,a,e)=>{e.r(a),e.d(a,{assets:()=>o,contentTitle:()=>l,default:()=>u,frontMatter:()=>i,metadata:()=>s,toc:()=>d});var n=e(87462),r=(e(67294),e(3905));const i={toc_max_heading_level:4,sidebar_label:"Getting Started",hide_title:!0,sidebar_position:1,description:"Quick start"},l="Getting Started",s={unversionedId:"data_analysis/validation/getting_started",id:"version-0.2.41/data_analysis/validation/getting_started",title:"Getting Started",description:"Quick start",source:"@site/versioned_docs/version-0.2.41/data_analysis/validation/getting_started.md",sourceDirName:"data_analysis/validation",slug:"/data_analysis/validation/getting_started",permalink:"/docs/0.2.41/data_analysis/validation/getting_started",draft:!1,tags:[],version:"0.2.41",sidebarPosition:1,frontMatter:{toc_max_heading_level:4,sidebar_label:"Getting Started",hide_title:!0,sidebar_position:1,description:"Quick start"},sidebar:"gettingStartedSidebar",previous:{title:"Overview",permalink:"/docs/0.2.41/data_analysis/validation/"},next:{title:"Standard Deviation Boundary Test",permalink:"/docs/0.2.41/data_analysis/validation/standard_deviation_boundary_test"}},o={},d=[{value:"Query and Prepare Data",id:"query-and-prepare-data",level:2}],m={toc:d},p="wrapper";function u(t){let{components:a,...e}=t;return(0,r.kt)(p,(0,n.Z)({},m,e,{components:a,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"getting-started"},"Getting Started"),(0,r.kt)("p",null,"There is a set of validation tests to check the simulation results. These tests include:"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},(0,r.kt)("a",{parentName:"p",href:"/docs/0.2.41/data_analysis/documentation/validation/#validation.validation.Validation.std_bound_test"},(0,r.kt)("strong",{parentName:"a"},"std_bound_test()"))," - verifies whether the n-",(0,r.kt)("span",{parentName:"p",className:"math math-inline"},(0,r.kt)("span",{parentName:"span",className:"katex"},(0,r.kt)("span",{parentName:"span",className:"katex-mathml"},(0,r.kt)("math",{parentName:"span",xmlns:"http://www.w3.org/1998/Math/MathML"},(0,r.kt)("semantics",{parentName:"math"},(0,r.kt)("mrow",{parentName:"semantics"},(0,r.kt)("mi",{parentName:"mrow"},"\u03c3")),(0,r.kt)("annotation",{parentName:"semantics",encoding:"application/x-tex"},"\\sigma")))),(0,r.kt)("span",{parentName:"span",className:"katex-html","aria-hidden":"true"},(0,r.kt)("span",{parentName:"span",className:"base"},(0,r.kt)("span",{parentName:"span",className:"strut",style:{height:"0.4306em"}}),(0,r.kt)("span",{parentName:"span",className:"mord mathnormal",style:{marginRight:"0.03588em"}},"\u03c3")))))," standard deviation boundary falls within the specified limits;")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},(0,r.kt)("a",{parentName:"p",href:"/docs/0.2.41/data_analysis/documentation/validation/#validation.validation.Validation.mean_test"},(0,r.kt)("strong",{parentName:"a"},"mean_test()"))," - checks if the mean value is within the given limits;")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},(0,r.kt)("a",{parentName:"p",href:"/docs/0.2.41/data_analysis/documentation/validation/#validation.validation.Validation.std_test"},(0,r.kt)("strong",{parentName:"a"},"std_test()"))," - verifies whether the n-",(0,r.kt)("span",{parentName:"p",className:"math math-inline"},(0,r.kt)("span",{parentName:"span",className:"katex"},(0,r.kt)("span",{parentName:"span",className:"katex-mathml"},(0,r.kt)("math",{parentName:"span",xmlns:"http://www.w3.org/1998/Math/MathML"},(0,r.kt)("semantics",{parentName:"math"},(0,r.kt)("mrow",{parentName:"semantics"},(0,r.kt)("mi",{parentName:"mrow"},"\u03c3")),(0,r.kt)("annotation",{parentName:"semantics",encoding:"application/x-tex"},"\\sigma")))),(0,r.kt)("span",{parentName:"span",className:"katex-html","aria-hidden":"true"},(0,r.kt)("span",{parentName:"span",className:"base"},(0,r.kt)("span",{parentName:"span",className:"strut",style:{height:"0.4306em"}}),(0,r.kt)("span",{parentName:"span",className:"mord mathnormal",style:{marginRight:"0.03588em"}},"\u03c3")))))," standard deviation is less then the given limit;")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},(0,r.kt)("a",{parentName:"p",href:"/docs/0.2.41/data_analysis/documentation/validation/#validation.validation.Validation.sid_test"},(0,r.kt)("strong",{parentName:"a"},"sid_test()"))," - examines if the simulation values do not exceed the limits;")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},(0,r.kt)("a",{parentName:"p",href:"/docs/0.2.41/data_analysis/documentation/validation/#validation.validation.Validation.norm_test"},(0,r.kt)("strong",{parentName:"a"},"norm_test"))," - evaluates norm of each simulation and compares it with the specified limit;"))),(0,r.kt)("p",null,"Number and type of tests may be set by ",(0,r.kt)("a",{parentName:"p",href:"/docs/0.2.41/data_analysis/documentation/validation/#validation.validation.Validation.set_tests"},(0,r.kt)("strong",{parentName:"a"},"set_tests()"))," method that allows to specify the desired tests by providing their names and corresponding parameters and produces a consolidated report."),(0,r.kt)("h2",{id:"query-and-prepare-data"},"Query and Prepare Data"),(0,r.kt)("p",null,"To connect to the database ",(0,r.kt)("a",{parentName:"p",href:"/docs/0.2.41/data_analysis/documentation/access/citros_db#access.citros_db.CitrosDB"},(0,r.kt)("strong",{parentName:"a"},"CitrosDB"))," object is created:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> from citros import CitrosDB\n>>> citros = CitrosDB()\n")),(0,r.kt)("p",null,"To learn more about connection parameters, see ",(0,r.kt)("a",{parentName:"p",href:"/docs/0.2.41/data_analysis/data_access/getting_started"},"here"),"."),(0,r.kt)("p",null,"Let's assume, that data for topic 'A' from batch 'planets' of the simulation 'simulation_systems' looks like:"),(0,r.kt)("table",null,(0,r.kt)("thead",{parentName:"table"},(0,r.kt)("tr",{parentName:"thead"},(0,r.kt)("th",{parentName:"tr",align:null}),(0,r.kt)("th",{parentName:"tr",align:null},"sid"),(0,r.kt)("th",{parentName:"tr",align:null},"rid"),(0,r.kt)("th",{parentName:"tr",align:null},"time"),(0,r.kt)("th",{parentName:"tr",align:null},"topic"),(0,r.kt)("th",{parentName:"tr",align:null},"type"),(0,r.kt)("th",{parentName:"tr",align:null},"data"))),(0,r.kt)("tbody",{parentName:"table"},(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"0"),(0,r.kt)("td",{parentName:"tr",align:null},"1"),(0,r.kt)("td",{parentName:"tr",align:null},"0"),(0,r.kt)("td",{parentName:"tr",align:null},"312751159"),(0,r.kt)("td",{parentName:"tr",align:null},"A"),(0,r.kt)("td",{parentName:"tr",align:null},"a"),(0,r.kt)("td",{parentName:"tr",align:null},"{'x': {'x_1': 0.0, 'x_2': 0.08, 'x_3': 154.47}, 'time': 10.0}")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"1"),(0,r.kt)("td",{parentName:"tr",align:null},"1"),(0,r.kt)("td",{parentName:"tr",align:null},"1"),(0,r.kt)("td",{parentName:"tr",align:null},"407264008"),(0,r.kt)("td",{parentName:"tr",align:null},"A"),(0,r.kt)("td",{parentName:"tr",align:null},"a"),(0,r.kt)("td",{parentName:"tr",align:null},"{'x': {'x_1': 0.008, 'x_2': 0.08, 'x_3': 130.97}, 'time': 17.9}")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"2"),(0,r.kt)("td",{parentName:"tr",align:null},"1"),(0,r.kt)("td",{parentName:"tr",align:null},"2"),(0,r.kt)("td",{parentName:"tr",align:null},"951279608"),(0,r.kt)("td",{parentName:"tr",align:null},"A"),(0,r.kt)("td",{parentName:"tr",align:null},"a"),(0,r.kt)("td",{parentName:"tr",align:null},"{'x': {'x_1': 0.016, 'x_2': 0.078, 'x_3': 117.66}, 'time': 20.3}")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"..."),(0,r.kt)("td",{parentName:"tr",align:null},"..."),(0,r.kt)("td",{parentName:"tr",align:null},"..."),(0,r.kt)("td",{parentName:"tr",align:null},"..."),(0,r.kt)("td",{parentName:"tr",align:null},"..."),(0,r.kt)("td",{parentName:"tr",align:null},"..."),(0,r.kt)("td",{parentName:"tr",align:null},"...")))),(0,r.kt)("p",null,"A json-data column contains information about time and vector x, that has elements x_1, x_2 and x_3. Let's query these columns:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> df = citros.simulation('simulation_systems').batch('planets').topic('A').data(['data.x', 'data.time'])\n")),(0,r.kt)("p",null,"The output is a ",(0,r.kt)("a",{parentName:"p",href:"https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html"},(0,r.kt)("strong",{parentName:"a"},"pandas.DataFrame")),":"),(0,r.kt)("table",null,(0,r.kt)("thead",{parentName:"table"},(0,r.kt)("tr",{parentName:"thead"},(0,r.kt)("th",{parentName:"tr",align:null}),(0,r.kt)("th",{parentName:"tr",align:null},"sid"),(0,r.kt)("th",{parentName:"tr",align:null},"rid"),(0,r.kt)("th",{parentName:"tr",align:null},"time"),(0,r.kt)("th",{parentName:"tr",align:null},"topic"),(0,r.kt)("th",{parentName:"tr",align:null},"type"),(0,r.kt)("th",{parentName:"tr",align:null},"data.x"),(0,r.kt)("th",{parentName:"tr",align:null},"data.time"))),(0,r.kt)("tbody",{parentName:"table"},(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"0"),(0,r.kt)("td",{parentName:"tr",align:null},"1"),(0,r.kt)("td",{parentName:"tr",align:null},"0"),(0,r.kt)("td",{parentName:"tr",align:null},"312751159"),(0,r.kt)("td",{parentName:"tr",align:null},"A"),(0,r.kt)("td",{parentName:"tr",align:null},"a"),(0,r.kt)("td",{parentName:"tr",align:null},"{'x_1': 0.0, 'x_2': 0.08, 'x_3': 154.47}"),(0,r.kt)("td",{parentName:"tr",align:null},"10.0")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"1"),(0,r.kt)("td",{parentName:"tr",align:null},"1"),(0,r.kt)("td",{parentName:"tr",align:null},"1"),(0,r.kt)("td",{parentName:"tr",align:null},"407264008"),(0,r.kt)("td",{parentName:"tr",align:null},"A"),(0,r.kt)("td",{parentName:"tr",align:null},"a"),(0,r.kt)("td",{parentName:"tr",align:null},"{'x_1': 0.008, 'x_2': 0.08, 'x_3': 130.97}"),(0,r.kt)("td",{parentName:"tr",align:null},"17.9")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"2"),(0,r.kt)("td",{parentName:"tr",align:null},"1"),(0,r.kt)("td",{parentName:"tr",align:null},"2"),(0,r.kt)("td",{parentName:"tr",align:null},"951279608"),(0,r.kt)("td",{parentName:"tr",align:null},"A"),(0,r.kt)("td",{parentName:"tr",align:null},"a"),(0,r.kt)("td",{parentName:"tr",align:null},"{'x_1': 0.016, 'x_2': 0.078, 'x_3': 117.66}"),(0,r.kt)("td",{parentName:"tr",align:null},"20.3")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"..."),(0,r.kt)("td",{parentName:"tr",align:null},"..."),(0,r.kt)("td",{parentName:"tr",align:null},"..."),(0,r.kt)("td",{parentName:"tr",align:null},"..."),(0,r.kt)("td",{parentName:"tr",align:null},"..."),(0,r.kt)("td",{parentName:"tr",align:null},"..."),(0,r.kt)("td",{parentName:"tr",align:null},"..."),(0,r.kt)("td",{parentName:"tr",align:null},"...")))),(0,r.kt)("p",null,"Analysis of data from multiple simulations may be performed if the correspondence between data values from different simulation is set. It may be done through an independent variable that is shared between simulations. Indexes are assigned based on this variable, connecting data values across the simulations."),(0,r.kt)("p",null,"There are two methods to handle index assignment:"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"to divides the independent variable into ",(0,r.kt)("inlineCode",{parentName:"li"},"num")," ranges, assign an index to each interval, and calculate data value averages for each simulation within each range (see ",(0,r.kt)("a",{parentName:"li",href:"/docs/0.2.41/data_analysis/documentation/analysis/citros_data#analysis.citros_data.CitrosData.bin_data"},(0,r.kt)("strong",{parentName:"a"},"bin_data()")),")"),(0,r.kt)("li",{parentName:"ul"},"to scale for each simulation the independent variable to the interval ","[0,1]",", defines ",(0,r.kt)("inlineCode",{parentName:"li"},"num")," uniformly distributed points from 0 to 1, and interpolates data points over this new interval (see ",(0,r.kt)("a",{parentName:"li",href:"/docs/0.2.41/data_analysis/documentation/analysis/citros_stat#analysis.citros_data.CitrosData.scale_data"},(0,r.kt)("strong",{parentName:"a"},"scale_data()")),").")),(0,r.kt)("p",null,"This preparation may be done by creating ",(0,r.kt)("a",{parentName:"p",href:"/docs/0.2.41/data_analysis/documentation/validation/#validation.validation.Validation"},(0,r.kt)("strong",{parentName:"a"},"Validation"))," object, that is able to apply mentioned above approaches to assign indexes and to calculate statistics over different simulations. Let's choose 'data.time' as an independent variable and use it to assign indexes and connect 'data.x' values of different simulations. The method of index setting is specified by ",(0,r.kt)("inlineCode",{parentName:"p"},"method"),": 'scale' or 'bin', the number of points (bins) is passed by ",(0,r.kt)("inlineCode",{parentName:"p"},"num"),":"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"from citros import Validation\n\n>>> V = Validation(df, data_label = ['data.x'], param_label = 'data.time', \n                   method = 'scale', num = 20, units = 'm')\n")),(0,r.kt)("p",null,(0,r.kt)("inlineCode",{parentName:"p"},"units")," are specified to make plots more informative."),(0,r.kt)("p",null,"If only some of the elements of the vector 'data.x' are needed, for example 'data.x.x_1' and 'data.x.x_2', they may be queried and passed to ",(0,r.kt)("a",{parentName:"p",href:"/docs/0.2.41/data_analysis/documentation/validation/#validation.validation.Validation"},(0,r.kt)("strong",{parentName:"a"},"Validation"))," object as follows:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> df = citros.simulation('simulation_systems').batch('planets').topic('A').data(['data.x.x_1', 'data.x.x_2', 'data.time'])\n>>> V = Validation(df, data_label = ['data.x.x_1', 'data.x.x_2'], param_label = 'data.time', \n                   method = 'scale', num = 20, units = 'm')\n")),(0,r.kt)("p",null,"After initialization, ",(0,r.kt)("a",{parentName:"p",href:"/docs/0.2.41/data_analysis/documentation/validation/#validation.validation.Validation"},(0,r.kt)("strong",{parentName:"a"},"Validation"))," object stores statistics as a ",(0,r.kt)("a",{parentName:"p",href:"/docs/0.2.41/data_analysis/documentation/analysis/citros_stat#analysis.citros_stat.CitrosStat"},(0,r.kt)("strong",{parentName:"a"},"CitrosStat"))," in ",(0,r.kt)("inlineCode",{parentName:"p"},"stat")," attribute. For example, to get mean values:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> print(V.stat.mean)\n")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-js"},"              data.x.x_1   data.x.x_2   data.x.x_3\ndata.time_id\n0             -0.045667    0.044667     93.706667\n1             0.007875     0.069515     95.639414\n2             0.056261     0.043401     33.128443\n...           ...          ...          ...\n")),(0,r.kt)("p",null,"In the same way it is possible to access scaled 'data.time' range (",(0,r.kt)("inlineCode",{parentName:"p"},"V.stat.x"),"), standard deviation (",(0,r.kt)("inlineCode",{parentName:"p"},"V.stat.sigma"),") and covariance matrix (",(0,r.kt)("inlineCode",{parentName:"p"},"V.stat.covar_matrix"),")."))}u.isMDXComponent=!0}}]);
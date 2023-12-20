"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[972],{3905:(t,e,a)=>{a.d(e,{Zo:()=>d,kt:()=>g});var n=a(7294);function r(t,e,a){return e in t?Object.defineProperty(t,e,{value:a,enumerable:!0,configurable:!0,writable:!0}):t[e]=a,t}function l(t,e){var a=Object.keys(t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(t);e&&(n=n.filter((function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable}))),a.push.apply(a,n)}return a}function i(t){for(var e=1;e<arguments.length;e++){var a=null!=arguments[e]?arguments[e]:{};e%2?l(Object(a),!0).forEach((function(e){r(t,e,a[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(a)):l(Object(a)).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(a,e))}))}return t}function s(t,e){if(null==t)return{};var a,n,r=function(t,e){if(null==t)return{};var a,n,r={},l=Object.keys(t);for(n=0;n<l.length;n++)a=l[n],e.indexOf(a)>=0||(r[a]=t[a]);return r}(t,e);if(Object.getOwnPropertySymbols){var l=Object.getOwnPropertySymbols(t);for(n=0;n<l.length;n++)a=l[n],e.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(t,a)&&(r[a]=t[a])}return r}var o=n.createContext({}),p=function(t){var e=n.useContext(o),a=e;return t&&(a="function"==typeof t?t(e):i(i({},e),t)),a},d=function(t){var e=p(t.components);return n.createElement(o.Provider,{value:e},t.children)},m="mdxType",u={inlineCode:"code",wrapper:function(t){var e=t.children;return n.createElement(n.Fragment,{},e)}},c=n.forwardRef((function(t,e){var a=t.components,r=t.mdxType,l=t.originalType,o=t.parentName,d=s(t,["components","mdxType","originalType","parentName"]),m=p(a),c=r,g=m["".concat(o,".").concat(c)]||m[c]||u[c]||l;return a?n.createElement(g,i(i({ref:e},d),{},{components:a})):n.createElement(g,i({ref:e},d))}));function g(t,e){var a=arguments,r=e&&e.mdxType;if("string"==typeof t||r){var l=a.length,i=new Array(l);i[0]=c;var s={};for(var o in e)hasOwnProperty.call(e,o)&&(s[o]=e[o]);s.originalType=t,s[m]="string"==typeof t?t:r,i[1]=s;for(var p=2;p<l;p++)i[p]=a[p];return n.createElement.apply(null,i)}return n.createElement.apply(null,a)}c.displayName="MDXCreateElement"},338:(t,e,a)=>{a.r(e),a.d(e,{assets:()=>o,contentTitle:()=>i,default:()=>u,frontMatter:()=>l,metadata:()=>s,toc:()=>p});var n=a(7462),r=(a(7294),a(3905));const l={toc_max_heading_level:4,hide_title:!0,sidebar_position:5,sidebar_label:"Testing Each Simulation",description:"Check individual simulations"},i="Testing Each Simulation",s={unversionedId:"validation/testing_each_simulation",id:"validation/testing_each_simulation",title:"Testing Each Simulation",description:"Check individual simulations",source:"@site/docs_data_analysis/validation/testing_each_simulation.md",sourceDirName:"validation",slug:"/validation/testing_each_simulation",permalink:"/docs_data_analysis/next/validation/testing_each_simulation",draft:!1,tags:[],version:"current",sidebarPosition:5,frontMatter:{toc_max_heading_level:4,hide_title:!0,sidebar_position:5,sidebar_label:"Testing Each Simulation",description:"Check individual simulations"},sidebar:"dataAnalysisSidebar",previous:{title:"Norm Test",permalink:"/docs_data_analysis/next/validation/norm_test"},next:{title:"Set Multiple Tests",permalink:"/docs_data_analysis/next/validation/set_multiple_tests"}},o={},p=[{value:"Setting Limits",id:"setting-limits",level:2},{value:"Returning Parameters",id:"returning-parameters",level:2}],d={toc:p},m="wrapper";function u(t){let{components:e,...l}=t;return(0,r.kt)(m,(0,n.Z)({},d,l,{components:e,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"testing-each-simulation"},"Testing Each Simulation"),(0,r.kt)("p",null,(0,r.kt)("a",{parentName:"p",href:"/docs_data_analysis/next/documentation/validation/#citros_data_analysis.validation.validation.Validation.sid_test"},(0,r.kt)("strong",{parentName:"a"},"sid_test()"))," test whether all simulation values are within the given limits."),(0,r.kt)("p",null,"Let's query data for a 3 dimensional vector, assign indexes to data to set correspondence between different simulations (see ",(0,r.kt)("a",{parentName:"p",href:"/docs_data_analysis/next/validation/getting_started"},"Getting started")," page) and test whether all simulations retain their values within the limits:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> df = citros.topic('A').data(['data.x.x_1', 'data.x.x_2', 'data.x.x_3', 'data.time'])\n>>> V = va.Validation(df, data_label = ['data.x.x_1', 'data.x.x_2', 'data.x.x_3'], \n                      param_label = 'data.time', method = 'scale', num = 20, units = 'm')\n                      \n>>> log, table, fig = V.sid_test(limits = [0.1, 0.15, [-50, 175]])\n")),(0,r.kt)("h2",{id:"setting-limits"},"Setting Limits"),(0,r.kt)("p",null,"Ways to set limits are the same as for ",(0,r.kt)("a",{parentName:"p",href:"/docs_data_analysis/next/validation/standard_deviation_boundary_test"},(0,r.kt)("strong",{parentName:"a"},"std_bound_test()"))," and ",(0,r.kt)("a",{parentName:"p",href:"/docs_data_analysis/next/validation/mean_value_test"},(0,r.kt)("strong",{parentName:"a"},"mean_test")),":"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"if ",(0,r.kt)("inlineCode",{parentName:"li"},"limits")," are set as a one value, for example ",(0,r.kt)("inlineCode",{parentName:"li"},"limits")," = 1, then it will be applied to all columns and considered as an test interval ","[-1, 1]",";"),(0,r.kt)("li",{parentName:"ul"},"if ",(0,r.kt)("inlineCode",{parentName:"li"},"limits")," are set as a list of two values, for example ",(0,r.kt)("inlineCode",{parentName:"li"},"limits")," = ","[-2, 3]",", then they will be applied to all columns as an test interval ","[-2, 3]",";"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"limits")," may be set separately for each column, as in the example above: ",(0,r.kt)("inlineCode",{parentName:"li"},"limits")," = [0.1, 0.15, ","[-50, 175]","] means that for the first column boundaries are ","[-0.25, 0.25]",", for the second one are ","[-0.3, 0.3]"," and for the last column ","[-50, 175]",". That way length of the ",(0,r.kt)("inlineCode",{parentName:"li"},"limits")," must be equal to the number of columns."),(0,r.kt)("li",{parentName:"ul"},"if number of column equals two, then ",(0,r.kt)("inlineCode",{parentName:"li"},"limits")," = ","[1, 3]"," will be considered as common limits ","[1, 3]"," for both columns. If separate limits ","[-1, 1]"," for the first column and ","[-3, 3]"," for the second one are needed, they must be passed as ",(0,r.kt)("inlineCode",{parentName:"li"},"limits")," = [","[-1, 1]",",  ","[-3, 3]","].")),(0,r.kt)("h2",{id:"returning-parameters"},"Returning Parameters"),(0,r.kt)("p",null,"The method returns three parameters: "),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"log")," : ",(0,r.kt)("a",{parentName:"li",href:"/docs_data_analysis/next/documentation/data_access/citros_dict#citros_data_analysis.data_access.citros_dict.CitrosDict"},(0,r.kt)("strong",{parentName:"a"},"CitrosDict"))," - dictionary with test result summary;")),(0,r.kt)("mermaid",{value:'flowchart TD\nlog_sid((log_sid)) --- init3("\'test_param\'") --\x3e |initial \\ntest parameters| init3_("{\'limits\': list}")\n    \n    log_sid --- col3("column label,\n     str") --\x3e|whether the test\\n passed or failed| B3("{\'passed\': bool}")\n \n    col3 --- C3(\'pass_rate\') --\x3e |fraction\\n of the simulations\\n that pass the test| C3a("{\'sid_fraction\': float}")\n\n    C3 --\x3e |"fraction of the points\\n that pass the test\\n for each simulation,\\n{sid : fraction}"| C3b("{int: float}")\n\n    col3 ---|points that failed| D3(\'failed\') --\x3e |"\\nindexes and values\\nof the x coordinate\\n for each of the sid \\n {sid:\\n {x_index: x_value}}"|D3a("{int: \n    {int : float}}")'}),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},(0,r.kt)("inlineCode",{parentName:"p"},"table")," : ",(0,r.kt)("a",{parentName:"p",href:"https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html"},(0,r.kt)("strong",{parentName:"a"},"pandas.DataFrame"))," - table that specifies for each simulation point whether it passes the test (True) or fails (False).")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},(0,r.kt)("inlineCode",{parentName:"p"},"fig")," : ",(0,r.kt)("a",{parentName:"p",href:"https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.Figure"},(0,r.kt)("strong",{parentName:"a"},"matplotlib.figure.Figure"))))),(0,r.kt)("p",null,"The output of the example above:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> fig.show()\n")),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"fig3",src:a(3758).Z,title:"Fig3",width:"743",height:"602"})),(0,r.kt)("p",null,"All points of 'data.x.x_1' and 'data.x.x_2' columns are within the set limits, while some points of the simulations for 'data.x.x_3' column do not satisfy the given constraints."),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> print(table)\n")),(0,r.kt)("table",null,(0,r.kt)("thead",{parentName:"table"},(0,r.kt)("tr",{parentName:"thead"},(0,r.kt)("th",{parentName:"tr",align:null}),(0,r.kt)("th",{parentName:"tr",align:null}),(0,r.kt)("th",{parentName:"tr",align:null},"data.time"),(0,r.kt)("th",{parentName:"tr",align:null},"data.x.x_1"),(0,r.kt)("th",{parentName:"tr",align:null},"data.x.x_2"),(0,r.kt)("th",{parentName:"tr",align:null},"data.x.x_3"))),(0,r.kt)("tbody",{parentName:"table"},(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"data.time_id"),(0,r.kt)("td",{parentName:"tr",align:null},"sid"),(0,r.kt)("td",{parentName:"tr",align:null}),(0,r.kt)("td",{parentName:"tr",align:null}),(0,r.kt)("td",{parentName:"tr",align:null}),(0,r.kt)("td",{parentName:"tr",align:null})),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"0"),(0,r.kt)("td",{parentName:"tr",align:null},"1"),(0,r.kt)("td",{parentName:"tr",align:null},"0.000000"),(0,r.kt)("td",{parentName:"tr",align:null},"True"),(0,r.kt)("td",{parentName:"tr",align:null},"True"),(0,r.kt)("td",{parentName:"tr",align:null},"True")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"2"),(0,r.kt)("td",{parentName:"tr",align:null}),(0,r.kt)("td",{parentName:"tr",align:null},"0.000000"),(0,r.kt)("td",{parentName:"tr",align:null},"True"),(0,r.kt)("td",{parentName:"tr",align:null},"True"),(0,r.kt)("td",{parentName:"tr",align:null},"True")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"3"),(0,r.kt)("td",{parentName:"tr",align:null}),(0,r.kt)("td",{parentName:"tr",align:null},"0.000000"),(0,r.kt)("td",{parentName:"tr",align:null},"True"),(0,r.kt)("td",{parentName:"tr",align:null},"True"),(0,r.kt)("td",{parentName:"tr",align:null},"True")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"1"),(0,r.kt)("td",{parentName:"tr",align:null},"1"),(0,r.kt)("td",{parentName:"tr",align:null},"0.052632"),(0,r.kt)("td",{parentName:"tr",align:null},"True"),(0,r.kt)("td",{parentName:"tr",align:null},"True"),(0,r.kt)("td",{parentName:"tr",align:null},"True")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"2"),(0,r.kt)("td",{parentName:"tr",align:null}),(0,r.kt)("td",{parentName:"tr",align:null},"0.052632"),(0,r.kt)("td",{parentName:"tr",align:null},"True"),(0,r.kt)("td",{parentName:"tr",align:null},"True"),(0,r.kt)("td",{parentName:"tr",align:null},"True")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"3"),(0,r.kt)("td",{parentName:"tr",align:null}),(0,r.kt)("td",{parentName:"tr",align:null},"0.052632"),(0,r.kt)("td",{parentName:"tr",align:null},"True"),(0,r.kt)("td",{parentName:"tr",align:null},"True"),(0,r.kt)("td",{parentName:"tr",align:null},"True")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"..."),(0,r.kt)("td",{parentName:"tr",align:null},"..."),(0,r.kt)("td",{parentName:"tr",align:null},"..."),(0,r.kt)("td",{parentName:"tr",align:null},"..."),(0,r.kt)("td",{parentName:"tr",align:null},"..."),(0,r.kt)("td",{parentName:"tr",align:null},"...")))),(0,r.kt)("p",null,(0,r.kt)("inlineCode",{parentName:"p"},"log")," can be accessed like a regular python dictionary and can be printed using the ",(0,r.kt)("a",{parentName:"p",href:"/docs_data_analysis/next/documentation/data_access/citros_dict#citros_data_analysis.data_access.citros_dict.CitrosDict.print"},(0,r.kt)("strong",{parentName:"a"},"print()"))," method to display it as a JSON object:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> log.print()\n")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-js"},"{\n 'test_param': {\n   'limits': [0.1, 0.15, [-50, 150]]\n },\n 'data.x.x_1': {\n   'passed': True,\n   'pass_rate': {\n     'sid_fraction': 1.0,\n     1: 1.0,\n     2: 1.0,\n     3: 1.0\n   },\n   'failed': {\n   }\n },\n 'data.x.x_2': {\n   'passed': True,\n   'pass_rate': {\n     'sid_fraction': 1.0,\n     1: 1.0,\n     2: 1.0,\n     3: 1.0\n   },\n   'failed': {\n   }\n },\n 'data.x.x_3': {  \n   'passed': False,\n   'pass_rate': {\n     'sid_fraction': 0.333,\n     1: 0.8,\n     2: 1.0,\n     3: 0.95\n   },\n   'failed': {\n     1: {\n       6: 0.316,\n       8: 0.421,\n       12: 0.632,\n       17: 0.895\n     },\n     3: {\n       5: 0.263\n     }\n   }\n }\n}\n")),(0,r.kt)("p",null,(0,r.kt)("inlineCode",{parentName:"p"},"log")," contains summary of the test result: "),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"initial test parameters:",(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> log['test_param'].print()\n")),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-js"},"{\n 'limits': [0.1, 0.15, [-50, 175]]\n}\n"))),(0,r.kt)("li",{parentName:"ul"},"Information about the test results of each column, let's take a look at the 'data.x.x_1':",(0,r.kt)("ul",{parentName:"li"},(0,r.kt)("li",{parentName:"ul"},"'passed' - whether the test for the column was passed (True) or not (False):",(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> print(log['data.x.x_1']['passed'])\n")),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-js"},"True\n"))),(0,r.kt)("li",{parentName:"ul"},"'pass_rate' contains information about fraction of the simulations that pass the test, 0 < 'pass_rate' < 1:",(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> print(log['data.x.x_1']['pass_rate']['sid_fraction'])\n")),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-js"},"1.0\n")),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> print(log['data.x.x_3']['pass_rate']['sid_fraction'])\n")),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-js"},"0.333\n")),"and for each simulation fraction of the points that pass the test. For example, for simulation with sid = 1:",(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> print(log['data.x.x_1']['pass_rate'][1])\n")),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-js"},"1.0\n")),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> print(log['data.x.x_3']['pass_rate'][1])\n")),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-js"},"0.8\n"))),(0,r.kt)("li",{parentName:"ul"},"'failed' - dictionaries with indexes and corresponding them values of the x axis ('data.time' in this case) for points that failed the test. Since all points of 'data.x.x_1' passed the test, log","['data.x.x_1']['failed']"," is empty:",(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> log['data.x.x_1']['failed'].print()\n")),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-js"},"{\n}\n")),"Otherwise, if there are points that failed the test, they are grouped by sid in the output. For example, in 'data.x.x_3' simulation 1 has 4 point that exceed limits and simulation 3 has 1 point:",(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> log['data.x.x_3']['failed'].print()\n")),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-js"},"{\n 1: {\n   6: 0.315,\n   8: 0.421,\n   12: 0.631,\n   17: 0.894\n },\n 3: {\n   5: 0.263\n }\n}\n")))))))}u.isMDXComponent=!0},3758:(t,e,a)=>{a.d(e,{Z:()=>n});const n=a.p+"assets/images/fig23-71a509372af0aa407f7ec473ffc9e882.png"}}]);
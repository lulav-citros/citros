"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[18015],{3905:(e,t,a)=>{a.d(t,{Zo:()=>m,kt:()=>k});var n=a(67294);function r(e,t,a){return t in e?Object.defineProperty(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}function l(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,n)}return a}function i(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?l(Object(a),!0).forEach((function(t){r(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):l(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}function s(e,t){if(null==e)return{};var a,n,r=function(e,t){if(null==e)return{};var a,n,r={},l=Object.keys(e);for(n=0;n<l.length;n++)a=l[n],t.indexOf(a)>=0||(r[a]=e[a]);return r}(e,t);if(Object.getOwnPropertySymbols){var l=Object.getOwnPropertySymbols(e);for(n=0;n<l.length;n++)a=l[n],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(r[a]=e[a])}return r}var o=n.createContext({}),p=function(e){var t=n.useContext(o),a=t;return e&&(a="function"==typeof e?e(t):i(i({},t),e)),a},m=function(e){var t=p(e.components);return n.createElement(o.Provider,{value:t},e.children)},d="mdxType",u={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},c=n.forwardRef((function(e,t){var a=e.components,r=e.mdxType,l=e.originalType,o=e.parentName,m=s(e,["components","mdxType","originalType","parentName"]),d=p(a),c=r,k=d["".concat(o,".").concat(c)]||d[c]||u[c]||l;return a?n.createElement(k,i(i({ref:t},m),{},{components:a})):n.createElement(k,i({ref:t},m))}));function k(e,t){var a=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var l=a.length,i=new Array(l);i[0]=c;var s={};for(var o in t)hasOwnProperty.call(t,o)&&(s[o]=t[o]);s.originalType=e,s[d]="string"==typeof e?e:r,i[1]=s;for(var p=2;p<l;p++)i[p]=a[p];return n.createElement.apply(null,i)}return n.createElement.apply(null,a)}c.displayName="MDXCreateElement"},52783:(e,t,a)=>{a.r(t),a.d(t,{assets:()=>o,contentTitle:()=>i,default:()=>u,frontMatter:()=>l,metadata:()=>s,toc:()=>p});var n=a(87462),r=(a(67294),a(3905));const l={toc_max_heading_level:4,hide_title:!0,sidebar_position:3,sidebar_label:"Mean Value Test",description:"Check mean value"},i="Mean Value Test",s={unversionedId:"data_analysis/validation/mean_value_test",id:"data_analysis/validation/mean_value_test",title:"Mean Value Test",description:"Check mean value",source:"@site/docs/data_analysis/validation/mean_value_test.md",sourceDirName:"data_analysis/validation",slug:"/data_analysis/validation/mean_value_test",permalink:"/docs/next/data_analysis/validation/mean_value_test",draft:!1,tags:[],version:"current",sidebarPosition:3,frontMatter:{toc_max_heading_level:4,hide_title:!0,sidebar_position:3,sidebar_label:"Mean Value Test",description:"Check mean value"},sidebar:"gettingStartedSidebar",previous:{title:"Standard Deviation Boundary Test",permalink:"/docs/next/data_analysis/validation/standard_deviation_boundary_test"},next:{title:"Standard Deviation Test",permalink:"/docs/next/data_analysis/validation/standard_deviation_test"}},o={},p=[{value:"Setting Limits",id:"setting-limits",level:2},{value:"Returning Parameters",id:"returning-parameters",level:2}],m={toc:p},d="wrapper";function u(e){let{components:t,...l}=e;return(0,r.kt)(d,(0,n.Z)({},m,l,{components:t,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"mean-value-test"},"Mean Value Test"),(0,r.kt)("p",null,(0,r.kt)("a",{parentName:"p",href:"/docs/next/data_analysis/documentation/validation/#validation.validation.Validation.mean_test"},(0,r.kt)("strong",{parentName:"a"},"mean_test()"))," - test whether mean is within the given limits."),(0,r.kt)("p",null,"As ",(0,r.kt)("a",{parentName:"p",href:"/docs/next/data_analysis/validation/standard_deviation_boundary_test"},"previously"),", let's get data of a 3 dimensional vector (from simulation 'simulation_systems', batch 'planets', topic 'A'), assign indexes to data to set correspondence between different simulations (see ",(0,r.kt)("a",{parentName:"p",href:"/docs/next/data_analysis/validation/getting_started"},"Getting started")," page) and test whether the mean value of each vector element does not exceed the limit:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> from citros import CitrosDB, Validation\n\n>>> citros = CitrosDB()\n>>> df = citros.simulation('simulation_systems').batch('planets').topic('A').data(['data.x.x_1', 'data.x.x_2', 'data.x.x_3', 'data.time'])\n>>> V = Validation(df, data_label = ['data.x.x_1', 'data.x.x_2', 'data.x.x_3'], \n                   param_label = 'data.time', method = 'scale', num = 20, units = 'm')\n                      \n>>> log, table, fig = V.mean_test(limits = [0.1, 0.15, [-50, 80]])\n")),(0,r.kt)("h2",{id:"setting-limits"},"Setting Limits"),(0,r.kt)("p",null,"Ways to set limits are the same as for ",(0,r.kt)("a",{parentName:"p",href:"/docs/next/data_analysis/validation/standard_deviation_boundary_test"},(0,r.kt)("strong",{parentName:"a"},"std_bound_test()"))," and ",(0,r.kt)("a",{parentName:"p",href:"/docs/next/data_analysis/validation/testing_each_simulation"},(0,r.kt)("strong",{parentName:"a"},"sid_test()")),":"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"if ",(0,r.kt)("inlineCode",{parentName:"li"},"limits")," are set as a one value, for example ",(0,r.kt)("inlineCode",{parentName:"li"},"limits")," = 1, then it will be applied to all columns and considered as an test interval ","[-1, 1]",";"),(0,r.kt)("li",{parentName:"ul"},"if ",(0,r.kt)("inlineCode",{parentName:"li"},"limits")," are set as a list of two values, for example ",(0,r.kt)("inlineCode",{parentName:"li"},"limits")," = ","[-2, 3]",", then they will be applied to all columns as an test interval ","[-2, 3]",";"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"limits")," may be set separately for each column, as in the example above: ",(0,r.kt)("inlineCode",{parentName:"li"},"limits")," = [0.1, 0.15, ","[-50, 80]","] means that for the first column boundaries are ","[-0.1, 0.1]",", for the second one are ","[-0.15, 0.15]"," and for the last column ","[-50, 80]",". That way length of the ",(0,r.kt)("inlineCode",{parentName:"li"},"limits")," must be equal to the number of columns."),(0,r.kt)("li",{parentName:"ul"},"if number of column equals two, then ",(0,r.kt)("inlineCode",{parentName:"li"},"limits")," = ","[1, 3]"," will be considered as common limits ","[1, 3]"," for both columns. If separate limits ","[-1, 1]"," for the first column and ","[-3, 3]"," for the second one are needed, they must be passed as ",(0,r.kt)("inlineCode",{parentName:"li"},"limits")," = [","[-1, 1]",",  ","[-3, 3]","].")),(0,r.kt)("h2",{id:"returning-parameters"},"Returning Parameters"),(0,r.kt)("p",null,"The method returns three parameters: "),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"log")," : ",(0,r.kt)("a",{parentName:"li",href:"/docs/next/data_analysis/documentation/access/citros_dict#access.citros_dict.CitrosDict"},(0,r.kt)("strong",{parentName:"a"},"CitrosDict"))," - dictionary with test result summary;")),(0,r.kt)("mermaid",{value:'flowchart TD\nlog_mean((log_mean)) --- init2("\'test_param\'") --\x3e |initial \\ntest parameters| init2_("{\'limits\': list}")\n    \n  log_mean --- col2("column label,\n  *str*") --\x3e|whether the test\\n passed or failed| B2("{\'passed\': bool}")\n\n  col2 --\x3e |fraction\\n of the points\\n that pass the test| C2("{\'pass_rate\': float}")\n\n  col2 ---|points that failed| D2(\'failed\') --\x3e |"indexes and values\\nof the x coordinate\\n {x_index: x_value}"|D2a("{int : float}")'}),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},(0,r.kt)("inlineCode",{parentName:"p"},"table")," : ",(0,r.kt)("a",{parentName:"p",href:"https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html"},(0,r.kt)("strong",{parentName:"a"},"pandas.DataFrame"))," - table that specifies for each point whether the mean value passes the test (True) or fails (False).")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},(0,r.kt)("inlineCode",{parentName:"p"},"fig")," : ",(0,r.kt)("a",{parentName:"p",href:"https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.Figure"},(0,r.kt)("strong",{parentName:"a"},"matplotlib.figure.Figure"))))),(0,r.kt)("p",null,"The output of the example above:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> fig.show()\n")),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"fig2",src:a(43751).Z,title:"Fig2",width:"743",height:"602"})),(0,r.kt)("p",null,"As it may be seen, the black line that represents the mean value remain within the limits for the 'data.x.x_1' and 'data.x.x_2' columns, while in case of the 'data.x.x_3' column only some points meets the given constraints."),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> print(table)\n")),(0,r.kt)("table",null,(0,r.kt)("thead",{parentName:"table"},(0,r.kt)("tr",{parentName:"thead"},(0,r.kt)("th",{parentName:"tr",align:null}),(0,r.kt)("th",{parentName:"tr",align:null},"data.time"),(0,r.kt)("th",{parentName:"tr",align:null},"data.x.x_1"),(0,r.kt)("th",{parentName:"tr",align:null},"data.x.x_2"),(0,r.kt)("th",{parentName:"tr",align:null},"data.x.x_3"))),(0,r.kt)("tbody",{parentName:"table"},(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"data.time_id"),(0,r.kt)("td",{parentName:"tr",align:null}),(0,r.kt)("td",{parentName:"tr",align:null}),(0,r.kt)("td",{parentName:"tr",align:null}),(0,r.kt)("td",{parentName:"tr",align:null})),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"0"),(0,r.kt)("td",{parentName:"tr",align:null},"0.000000"),(0,r.kt)("td",{parentName:"tr",align:null},"True"),(0,r.kt)("td",{parentName:"tr",align:null},"True"),(0,r.kt)("td",{parentName:"tr",align:null},"False")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"1"),(0,r.kt)("td",{parentName:"tr",align:null},"0.052632"),(0,r.kt)("td",{parentName:"tr",align:null},"True"),(0,r.kt)("td",{parentName:"tr",align:null},"True"),(0,r.kt)("td",{parentName:"tr",align:null},"False")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"2"),(0,r.kt)("td",{parentName:"tr",align:null},"0.105263"),(0,r.kt)("td",{parentName:"tr",align:null},"True"),(0,r.kt)("td",{parentName:"tr",align:null},"True"),(0,r.kt)("td",{parentName:"tr",align:null},"True")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"..."),(0,r.kt)("td",{parentName:"tr",align:null},"..."),(0,r.kt)("td",{parentName:"tr",align:null},"..."),(0,r.kt)("td",{parentName:"tr",align:null},"..."),(0,r.kt)("td",{parentName:"tr",align:null},"...")))),(0,r.kt)("p",null,(0,r.kt)("inlineCode",{parentName:"p"},"log")," can be accessed like a regular python dictionary and can be printed using the ",(0,r.kt)("a",{parentName:"p",href:"/docs/next/data_analysis/documentation/access/citros_dict#access.citros_dict.CitrosDict.print"},(0,r.kt)("strong",{parentName:"a"},"print()"))," method to display it as a JSON object:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> log.print()\n")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-js"},"{\n 'test_param': {\n   'limits': [0.1, 0.15, [-50, 80]]\n },\n 'data.x.x_1': {\n   'passed': True,\n   'pass_rate': 1.0,\n   'failed': {\n   }\n },\n 'data.x.x_2': {\n   'passed': True,\n   'pass_rate': 1.0,\n   'failed': {\n   }\n },\n 'data.x.x_3': {\n   'passed': False,\n   'pass_rate': 0.3,\n   'failed': {\n     0: 0.0,\n     1: 0.05263157894736842,\n     4: 0.21052631578947367,\n     5: 0.2631578947368421,\n     6: 0.3157894736842105,\n     8: 0.42105263157894735,\n     9: 0.47368421052631576,\n     10: 0.5263157894736842,\n     12: 0.631578947368421,\n     13: 0.6842105263157894,\n     15: 0.7894736842105263,\n     16: 0.8421052631578947,\n     17: 0.894736842105263,\n     18: 0.9473684210526315\n   }\n }\n}\n")),(0,r.kt)("p",null,(0,r.kt)("inlineCode",{parentName:"p"},"log")," contains summary of the test result: "),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},"initial test parameters:"),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> log['test_param'].print()\n")),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-js"},"{\n 'limits': [0.1, 0.15, [-50, 80]]\n}\n"))),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},"Information about the test results of each column, let's take a look at the 'data.x.x_1':"),(0,r.kt)("ul",{parentName:"li"},(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},"'passed' - whether the test for the column was passed (True) or not (False):"),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> print(log['data.x.x_1']['passed'])\n")),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-js"},"True\n"))),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},"'pass_rate' - fraction of the points that pass the test, 0 < 'pass_rate' < 1:"),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> print(log['data.x.x_1']['pass_rate'])\n")),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-js"},"1.0\n"))),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},"'failed' - dictionaries with indexes and corresponding them values of the x axis ('data.time' in this case) for points that failed the test. Since all points of 'data.x.x_1' passed the test, log","['data.x.x_1']['failed']"," is empty:"),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> log['data.x.x_1']['failed'].print()\n")),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-js"},"{\n}\n")),(0,r.kt)("p",{parentName:"li"},"whereas column 'data.x.x_3' has a series of points that exceed the limits:"),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> log['data.x.x_3']['failed'].print()\n")),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-js"},"{\n 0: 0.0,\n 1: 0.052,\n 4: 0.210,\n 5: 0.263,\n 6: 0.315,\n 8: 0.421,\n 9: 0.473,\n 10: 0.526,\n 12: 0.631,\n 13: 0.684,\n 15: 0.789,\n 16: 0.842,\n 17: 0.894,\n 18: 0.947\n}\n")))))))}u.isMDXComponent=!0},43751:(e,t,a)=>{a.d(t,{Z:()=>n});const n=a.p+"assets/images/fig22-8f51fc1f853651fd1bd82685dc67d38d.png"}}]);
"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[32084],{3905:(t,e,a)=>{a.d(e,{Zo:()=>p,kt:()=>h});var n=a(67294);function r(t,e,a){return e in t?Object.defineProperty(t,e,{value:a,enumerable:!0,configurable:!0,writable:!0}):t[e]=a,t}function i(t,e){var a=Object.keys(t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(t);e&&(n=n.filter((function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable}))),a.push.apply(a,n)}return a}function s(t){for(var e=1;e<arguments.length;e++){var a=null!=arguments[e]?arguments[e]:{};e%2?i(Object(a),!0).forEach((function(e){r(t,e,a[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(a)):i(Object(a)).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(a,e))}))}return t}function l(t,e){if(null==t)return{};var a,n,r=function(t,e){if(null==t)return{};var a,n,r={},i=Object.keys(t);for(n=0;n<i.length;n++)a=i[n],e.indexOf(a)>=0||(r[a]=t[a]);return r}(t,e);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(t);for(n=0;n<i.length;n++)a=i[n],e.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(t,a)&&(r[a]=t[a])}return r}var o=n.createContext({}),d=function(t){var e=n.useContext(o),a=e;return t&&(a="function"==typeof t?t(e):s(s({},e),t)),a},p=function(t){var e=d(t.components);return n.createElement(o.Provider,{value:e},t.children)},m="mdxType",u={inlineCode:"code",wrapper:function(t){var e=t.children;return n.createElement(n.Fragment,{},e)}},c=n.forwardRef((function(t,e){var a=t.components,r=t.mdxType,i=t.originalType,o=t.parentName,p=l(t,["components","mdxType","originalType","parentName"]),m=d(a),c=r,h=m["".concat(o,".").concat(c)]||m[c]||u[c]||i;return a?n.createElement(h,s(s({ref:e},p),{},{components:a})):n.createElement(h,s({ref:e},p))}));function h(t,e){var a=arguments,r=e&&e.mdxType;if("string"==typeof t||r){var i=a.length,s=new Array(i);s[0]=c;var l={};for(var o in e)hasOwnProperty.call(e,o)&&(l[o]=e[o]);l.originalType=t,l[m]="string"==typeof t?t:r,s[1]=l;for(var d=2;d<i;d++)s[d]=a[d];return n.createElement.apply(null,s)}return n.createElement.apply(null,a)}c.displayName="MDXCreateElement"},37836:(t,e,a)=>{a.r(e),a.d(e,{assets:()=>o,contentTitle:()=>s,default:()=>u,frontMatter:()=>i,metadata:()=>l,toc:()=>d});var n=a(87462),r=(a(67294),a(3905));const i={toc_max_heading_level:4,hide_title:!0,sidebar_position:2,sidebar_label:"Standard Deviation Boundary Test",description:"Check standard deviation boundary"},s="Standard Deviation Boundary Test",l={unversionedId:"data_analysis/validation/standard_deviation_boundary_test",id:"version-0.2.56/data_analysis/validation/standard_deviation_boundary_test",title:"Standard Deviation Boundary Test",description:"Check standard deviation boundary",source:"@site/versioned_docs/version-0.2.56/data_analysis/validation/standard_deviation_boundary_test.md",sourceDirName:"data_analysis/validation",slug:"/data_analysis/validation/standard_deviation_boundary_test",permalink:"/docs/0.2.56/data_analysis/validation/standard_deviation_boundary_test",draft:!1,tags:[],version:"0.2.56",sidebarPosition:2,frontMatter:{toc_max_heading_level:4,hide_title:!0,sidebar_position:2,sidebar_label:"Standard Deviation Boundary Test",description:"Check standard deviation boundary"},sidebar:"gettingStartedSidebar",previous:{title:"Getting Started",permalink:"/docs/0.2.56/data_analysis/validation/getting_started"},next:{title:"Mean Value Test",permalink:"/docs/0.2.56/data_analysis/validation/mean_value_test"}},o={},d=[{value:"Setting Limits",id:"setting-limits",level:2},{value:"Returning Parameters",id:"returning-parameters",level:2}],p={toc:d},m="wrapper";function u(t){let{components:e,...i}=t;return(0,r.kt)(m,(0,n.Z)({},p,i,{components:e,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"standard-deviation-boundary-test"},"Standard Deviation Boundary Test"),(0,r.kt)("p",null,(0,r.kt)("a",{parentName:"p",href:"/docs/0.2.56/data_analysis/documentation/validation/#validation.validation.Validation.std_bound_test"},(0,r.kt)("strong",{parentName:"a"},"std_bound_test()"))," test whether ",(0,r.kt)("inlineCode",{parentName:"p"},"n_std"),"-standard deviation boundary is within the given limits, where boundary is defined as mean value ",(0,r.kt)("span",{parentName:"p",className:"math math-inline"},(0,r.kt)("span",{parentName:"span",className:"katex"},(0,r.kt)("span",{parentName:"span",className:"katex-mathml"},(0,r.kt)("math",{parentName:"span",xmlns:"http://www.w3.org/1998/Math/MathML"},(0,r.kt)("semantics",{parentName:"math"},(0,r.kt)("mrow",{parentName:"semantics"},(0,r.kt)("mo",{parentName:"mrow"},"\xb1")),(0,r.kt)("annotation",{parentName:"semantics",encoding:"application/x-tex"},"\\pm")))),(0,r.kt)("span",{parentName:"span",className:"katex-html","aria-hidden":"true"},(0,r.kt)("span",{parentName:"span",className:"base"},(0,r.kt)("span",{parentName:"span",className:"strut",style:{height:"0.6667em",verticalAlign:"-0.0833em"}}),(0,r.kt)("span",{parentName:"span",className:"mord"},"\xb1")))))," ",(0,r.kt)("inlineCode",{parentName:"p"},"n_std")," * standard deviation. In case there are NaN (Not a Number) values of standard deviation, to specify whether they should be considered as passing the test, set ",(0,r.kt)("inlineCode",{parentName:"p"},"nan_passed")," = True or False (True by default)."),(0,r.kt)("p",null,"Let's query data of a 3 dimensional vector (simulation 'simulation_systems', batch 'planets', topic 'A'), assign indexes to data to set correspondence between different simulations (see ",(0,r.kt)("a",{parentName:"p",href:"/docs/0.2.56/data_analysis/validation/getting_started"},"Getting started")," page) and test whether the 3 standard deviation boundary is within the set limits:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> from citros import CitrosDB, Validation\n\n>>> citros = CitrosDB()\n>>> df = citros.simulation('simulation_systems').batch('planets').topic('A').data(['data.x.x_1', 'data.x.x_2', 'data.x.x_3', 'data.time'])\n>>> V = Validation(df, data_label = ['data.x.x_1', 'data.x.x_2', 'data.x.x_3'], \n                   param_label = 'data.time', method = 'scale', num = 20, units = 'm')\n                      \n>>> log, table, fig = V.std_bound_test(limits = [0.25, 0.3, [-150, 300]], n_std = 3, \n                                       nan_passed = True)\n")),(0,r.kt)("h2",{id:"setting-limits"},"Setting Limits"),(0,r.kt)("p",null,"Ways to set limits are the same as for ",(0,r.kt)("a",{parentName:"p",href:"/docs/0.2.56/data_analysis/validation/mean_value_test"},(0,r.kt)("strong",{parentName:"a"},"mean_test"))," and ",(0,r.kt)("a",{parentName:"p",href:"/docs/0.2.56/data_analysis/validation/testing_each_simulation"},(0,r.kt)("strong",{parentName:"a"},"sid_test()")),":"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"if ",(0,r.kt)("inlineCode",{parentName:"li"},"limits")," are set as a one value, for example ",(0,r.kt)("inlineCode",{parentName:"li"},"limits")," = 1, then it will be applied to all columns and considered as an test interval ","[-1, 1]",";"),(0,r.kt)("li",{parentName:"ul"},"if ",(0,r.kt)("inlineCode",{parentName:"li"},"limits")," are set as a list of two values, for example ",(0,r.kt)("inlineCode",{parentName:"li"},"limits")," = ","[-2, 3]",", then they will be applied to all columns as an test interval ","[-2, 3]",";"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"limits")," may be set separately for each column, as in the example above: ",(0,r.kt)("inlineCode",{parentName:"li"},"limits")," = [0.25, 0.3, ","[-150, 300]","] means that for the first column boundaries are ","[-0.25, 0.25]",", for the second one are ","[-0.3, 0.3]"," and for the last column ","[-150, 300]",". That way length of the ",(0,r.kt)("inlineCode",{parentName:"li"},"limits")," must be equal to the number of columns."),(0,r.kt)("li",{parentName:"ul"},"if number of column equals two, then ",(0,r.kt)("inlineCode",{parentName:"li"},"limits")," = ","[1, 3]"," will be considered as common limits ","[1, 3]"," for both columns. If separate limits ","[-1, 1]"," for the first column and ","[-3, 3]"," for the second one are needed, they must be passed as ",(0,r.kt)("inlineCode",{parentName:"li"},"limits")," = [","[-1, 1]",",  ","[-3, 3]","].")),(0,r.kt)("h2",{id:"returning-parameters"},"Returning Parameters"),(0,r.kt)("p",null,"The method returns three parameters: "),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"log")," : ",(0,r.kt)("a",{parentName:"li",href:"/docs/0.2.56/data_analysis/documentation/access/citros_dict#access.citros_dict.CitrosDict"},(0,r.kt)("strong",{parentName:"a"},"CitrosDict"))," - dictionary with test result summary;")),(0,r.kt)("mermaid",{value:'flowchart TD\nlog_std((log_std)) --- init1("\'test_param\'") --\x3e |initial \\ntest parameters| init1_("{\'limits\': list,\n\'n_std\': int,\n\'nan_passed\': bool}")\n\nlog_std --- col1("column label,\n    str") --\x3e|whether the test\\n passed or failed| B1("{\'passed\': bool}")\n\ncol1 --\x3e |fraction\\n of the points\\n that pass the test| C1("{\'pass_rate\': float}")\n\ncol1 ---|points that failed| D1(\'failed\') --\x3e |"indexes and values\\nof the x coordinate\\n {x_index: x_value}"|D1a("{int : float}")\n\ncol1 ---|"data points that have\\n NaN (Not a Number) values\\n for standard deviation"| E1(\'nan_std\') --\x3e |"indexes and values\\nof the x coordinate\\n {x_index: x_value}"|E1a("{int : float}")'}),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},(0,r.kt)("inlineCode",{parentName:"p"},"table")," : ",(0,r.kt)("a",{parentName:"p",href:"https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html"},(0,r.kt)("strong",{parentName:"a"},"pandas.DataFrame"))," - table that specifies whether the corresponding standard deviation boundary point passes the test (True) or not (False).")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},(0,r.kt)("inlineCode",{parentName:"p"},"fig")," : ",(0,r.kt)("a",{parentName:"p",href:"https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.Figure"},(0,r.kt)("strong",{parentName:"a"},"matplotlib.figure.Figure"))))),(0,r.kt)("p",null,"Let's inspect the output of the example above:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> fig.show()\n")),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"fig1",src:a(9785).Z,title:"Fig1",width:"743",height:"602"})),(0,r.kt)("p",null,"It is evident that the 3-",(0,r.kt)("span",{parentName:"p",className:"math math-inline"},(0,r.kt)("span",{parentName:"span",className:"katex"},(0,r.kt)("span",{parentName:"span",className:"katex-mathml"},(0,r.kt)("math",{parentName:"span",xmlns:"http://www.w3.org/1998/Math/MathML"},(0,r.kt)("semantics",{parentName:"math"},(0,r.kt)("mrow",{parentName:"semantics"},(0,r.kt)("mi",{parentName:"mrow"},"\u03c3")),(0,r.kt)("annotation",{parentName:"semantics",encoding:"application/x-tex"},"\\sigma")))),(0,r.kt)("span",{parentName:"span",className:"katex-html","aria-hidden":"true"},(0,r.kt)("span",{parentName:"span",className:"base"},(0,r.kt)("span",{parentName:"span",className:"strut",style:{height:"0.4306em"}}),(0,r.kt)("span",{parentName:"span",className:"mord mathnormal",style:{marginRight:"0.03588em"}},"\u03c3")))))," standard deviation boundaries remain within the limits for the 'data.x.x_1' and 'data.x.x_2' values, while in case of the 'data.x.x_3' column, certain points exceed the given limit."),(0,r.kt)("p",null,"To change the standard deviation boundary style, parameters ",(0,r.kt)("inlineCode",{parentName:"p"},"std_area"),", ",(0,r.kt)("inlineCode",{parentName:"p"},"std_lines")," and ",(0,r.kt)("inlineCode",{parentName:"p"},"std_color")," may be used: setting ",(0,r.kt)("inlineCode",{parentName:"p"},"std_area")," = True to fill the area within the boundary, ",(0,r.kt)("inlineCode",{parentName:"p"},"std_lines")," = False to remove the borders and ",(0,r.kt)("inlineCode",{parentName:"p"},"std_color")," change the color of the standard deviation boundary:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> log, table, fig = V.std_bound_test(limits = [0.25, 0.3, [-150, 300]], n_std = 3,\n                            nan_passed = True, std_area = True, std_lines = False, std_color = 'm')\n")),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"fig5",src:a(2812).Z,title:"Fig5",width:"743",height:"602"})),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> print(table)\n")),(0,r.kt)("table",null,(0,r.kt)("thead",{parentName:"table"},(0,r.kt)("tr",{parentName:"thead"},(0,r.kt)("th",{parentName:"tr",align:null}),(0,r.kt)("th",{parentName:"tr",align:null},"data.time"),(0,r.kt)("th",{parentName:"tr",align:null},"data.x.x_1"),(0,r.kt)("th",{parentName:"tr",align:null},"data.x.x_2"),(0,r.kt)("th",{parentName:"tr",align:null},"data.x.x_3"))),(0,r.kt)("tbody",{parentName:"table"},(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"data.time_id"),(0,r.kt)("td",{parentName:"tr",align:null}),(0,r.kt)("td",{parentName:"tr",align:null}),(0,r.kt)("td",{parentName:"tr",align:null}),(0,r.kt)("td",{parentName:"tr",align:null})),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"0"),(0,r.kt)("td",{parentName:"tr",align:null},"0.000000"),(0,r.kt)("td",{parentName:"tr",align:null},"True"),(0,r.kt)("td",{parentName:"tr",align:null},"True"),(0,r.kt)("td",{parentName:"tr",align:null},"False")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"1"),(0,r.kt)("td",{parentName:"tr",align:null},"0.052632"),(0,r.kt)("td",{parentName:"tr",align:null},"True"),(0,r.kt)("td",{parentName:"tr",align:null},"True"),(0,r.kt)("td",{parentName:"tr",align:null},"False")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"2"),(0,r.kt)("td",{parentName:"tr",align:null},"0.105263"),(0,r.kt)("td",{parentName:"tr",align:null},"True"),(0,r.kt)("td",{parentName:"tr",align:null},"True"),(0,r.kt)("td",{parentName:"tr",align:null},"True")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"..."),(0,r.kt)("td",{parentName:"tr",align:null},"..."),(0,r.kt)("td",{parentName:"tr",align:null},"..."),(0,r.kt)("td",{parentName:"tr",align:null},"..."),(0,r.kt)("td",{parentName:"tr",align:null},"...")))),(0,r.kt)("p",null,(0,r.kt)("inlineCode",{parentName:"p"},"log")," can be accessed like a regular python dictionary and can be printed using the ",(0,r.kt)("a",{parentName:"p",href:"/docs/0.2.56/data_analysis/documentation/access/citros_dict#access.citros_dict.CitrosDict.print"},(0,r.kt)("strong",{parentName:"a"},"print()"))," method to display it as a JSON object:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> log.print()\n")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-js"},"{\n 'test_param': {\n   'limits': [0.25, 0.3, [-150, 300]],\n   'n_std': 3,\n   'nan_passed': True\n },\n 'data.x.x_1': {\n   'passed': True,\n   'pass_rate': 1.0,\n   'failed': {\n   },\n   'nan_std': {\n   }\n },\n 'data.x.x_2': {\n   'passed': True,\n   'pass_rate': 1.0,\n   'failed': {\n   },\n   'nan_std': {\n   }\n },\n 'data.x.x_3': {\n   'passed': False,\n   'pass_rate': 0.55,\n   'failed': {\n      0: 0.0,\n      1: 0.052,\n      5: 0.263,\n      6: 0.315,\n      8: 0.421,\n      11: 0.578,\n      12: 0.631,\n      18: 0.947,\n      19: 1.0\n   },\n   'nan_std': {\n   }\n }\n}\n\n")),(0,r.kt)("p",null,(0,r.kt)("inlineCode",{parentName:"p"},"log")," contains summary of the test result: "),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},"initial test parameters:"),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> log['test_param'].print()\n")),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-js"},"{\n 'limits': [0.25, 0.3, [-300, 400]],\n 'n_std': 3,\n 'nan_passed': True\n}\n"))),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},"Information about the test results of each column, let's take a look at the 'data.x.x_1':"),(0,r.kt)("ul",{parentName:"li"},(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},"'passed' - whether the test for the column was passed (True) or not (False):"),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> print(log['data.x.x_1']['passed'])\n")),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-js"},"True\n"))),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},"'pass_rate' - fraction of the points that pass the test, 0 < 'pass_rate' < 1:"),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> print(log['data.x.x_1']['pass_rate'])\n")),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-js"},"1.0\n"))),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},"'failed' - dictionaries with indexes and corresponding them values of the x axis ('data.time' in this case) for points that failed the test. Since all points of 'data.x.x_1' passed the test, log","['data.x.x_1']['failed']"," is empty:"),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> log['data.x.x_1']['failed'].print()\n")),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-js"},"{\n}\n")),(0,r.kt)("p",{parentName:"li"},"whereas column 'data.x.x_3' has a series of points that exceed the limits:"),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> log['data.x.x_3']['failed'].print()\n")),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-js"},"{\n 0: 0.0,\n 1: 0.052,\n 5: 0.263,\n 6: 0.315,\n 8: 0.421,\n 11: 0.578,\n 12: 0.631,\n 18: 0.947,\n 19: 1.0\n}\n"))),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},"'nan_std' - if some of the standard deviations points could not be calculated (for example, number of simulations for this index is less then two, that may occurs if the method of data assignment ",(0,r.kt)("inlineCode",{parentName:"p"},"method")," = 'bin' has been chosen), their indexes and values of the x axis will be stored in the same way, as in the section 'failed'."))))))}u.isMDXComponent=!0},9785:(t,e,a)=>{a.d(e,{Z:()=>n});const n=a.p+"assets/images/fig21-c2d5622bfa7faa4cd8aaf62c154aa48b.png"},2812:(t,e,a)=>{a.d(e,{Z:()=>n});const n=a.p+"assets/images/fig28-f7723c48cd646f3d1ec96aceabcd3dde.png"}}]);
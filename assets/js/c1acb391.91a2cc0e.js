"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[8976],{3905:(t,e,a)=>{a.d(e,{Zo:()=>p,kt:()=>h});var n=a(7294);function r(t,e,a){return e in t?Object.defineProperty(t,e,{value:a,enumerable:!0,configurable:!0,writable:!0}):t[e]=a,t}function i(t,e){var a=Object.keys(t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(t);e&&(n=n.filter((function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable}))),a.push.apply(a,n)}return a}function l(t){for(var e=1;e<arguments.length;e++){var a=null!=arguments[e]?arguments[e]:{};e%2?i(Object(a),!0).forEach((function(e){r(t,e,a[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(a)):i(Object(a)).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(a,e))}))}return t}function s(t,e){if(null==t)return{};var a,n,r=function(t,e){if(null==t)return{};var a,n,r={},i=Object.keys(t);for(n=0;n<i.length;n++)a=i[n],e.indexOf(a)>=0||(r[a]=t[a]);return r}(t,e);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(t);for(n=0;n<i.length;n++)a=i[n],e.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(t,a)&&(r[a]=t[a])}return r}var o=n.createContext({}),d=function(t){var e=n.useContext(o),a=e;return t&&(a="function"==typeof t?t(e):l(l({},e),t)),a},p=function(t){var e=d(t.components);return n.createElement(o.Provider,{value:e},t.children)},m="mdxType",u={inlineCode:"code",wrapper:function(t){var e=t.children;return n.createElement(n.Fragment,{},e)}},c=n.forwardRef((function(t,e){var a=t.components,r=t.mdxType,i=t.originalType,o=t.parentName,p=s(t,["components","mdxType","originalType","parentName"]),m=d(a),c=r,h=m["".concat(o,".").concat(c)]||m[c]||u[c]||i;return a?n.createElement(h,l(l({ref:e},p),{},{components:a})):n.createElement(h,l({ref:e},p))}));function h(t,e){var a=arguments,r=e&&e.mdxType;if("string"==typeof t||r){var i=a.length,l=new Array(i);l[0]=c;var s={};for(var o in e)hasOwnProperty.call(e,o)&&(s[o]=e[o]);s.originalType=t,s[m]="string"==typeof t?t:r,l[1]=s;for(var d=2;d<i;d++)l[d]=a[d];return n.createElement.apply(null,l)}return n.createElement.apply(null,a)}c.displayName="MDXCreateElement"},4151:(t,e,a)=>{a.r(e),a.d(e,{assets:()=>o,contentTitle:()=>l,default:()=>u,frontMatter:()=>i,metadata:()=>s,toc:()=>d});var n=a(7462),r=(a(7294),a(3905));const i={toc_max_heading_level:4,hide_title:!0,sidebar_position:4,sidebar_label:"Standard Deviation Test",description:"Check standard deviation"},l="Standard Deviation Test",s={unversionedId:"validation/standard_deviation_test",id:"version-v0.9.1/validation/standard_deviation_test",title:"Standard Deviation Test",description:"Check standard deviation",source:"@site/docs_data_analysis_versioned_docs/version-v0.9.1/validation/standard_deviation_test.md",sourceDirName:"validation",slug:"/validation/standard_deviation_test",permalink:"/docs/docs_data_analysis/validation/standard_deviation_test",draft:!1,tags:[],version:"v0.9.1",sidebarPosition:4,frontMatter:{toc_max_heading_level:4,hide_title:!0,sidebar_position:4,sidebar_label:"Standard Deviation Test",description:"Check standard deviation"},sidebar:"dataAnalysisSidebar",previous:{title:"Mean Value Test",permalink:"/docs/docs_data_analysis/validation/mean_value_test"},next:{title:"Norm Test",permalink:"/docs/docs_data_analysis/validation/norm_test"}},o={},d=[{value:"Setting Limits",id:"setting-limits",level:2},{value:"Returning Parameters",id:"returning-parameters",level:2}],p={toc:d},m="wrapper";function u(t){let{components:e,...i}=t;return(0,r.kt)(m,(0,n.Z)({},p,i,{components:e,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"standard-deviation-test"},"Standard Deviation Test"),(0,r.kt)("p",null,(0,r.kt)("a",{parentName:"p",href:"/docs/docs_data_analysis/documentation/validation/#citros_data_analysis.validation.validation.Validation.std_test"},(0,r.kt)("strong",{parentName:"a"},"std_test()"))," test whether ",(0,r.kt)("inlineCode",{parentName:"p"},"n_std"),"-standard deviation is less than the given limits. In case there are NaN (Not a Number) values of standard deviation, to specify whether they should be considered as passing the test, set ",(0,r.kt)("inlineCode",{parentName:"p"},"nan_passed")," = True or False (True by default)."),(0,r.kt)("p",null,"Let's query data for a 3 dimensional vector, assign indexes to data to set correspondence between different simulations (see ",(0,r.kt)("a",{parentName:"p",href:"/docs/docs_data_analysis/validation/getting_started"},"Getting started")," page) and test whether whether the 3 standard deviation is within the established limits:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> df = citros.topic('A').data(['data.x.x_1', 'data.x.x_2', 'data.x.x_3', 'data.time'])\n>>> V = va.Validation(df, data_label = ['data.x.x_1', 'data.x.x_2', 'data.x.x_3'], \n                      param_label = 'data.time', method = 'scale', num = 20, units = 'm')\n                      \n>>> log, table, fig = V.std_test(limits = [0.25, 0.3, 300], n_std = 3, nan_passed = True, \n                                 std_area = True)\n")),(0,r.kt)("h2",{id:"setting-limits"},"Setting Limits"),(0,r.kt)("p",null,"Ways to set limits are the same as for ",(0,r.kt)("a",{parentName:"p",href:"/docs/docs_data_analysis/validation/norm_test"},(0,r.kt)("strong",{parentName:"a"},"norm_test")),":"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"if ",(0,r.kt)("inlineCode",{parentName:"li"},"limits")," are set as a one value, for example ",(0,r.kt)("inlineCode",{parentName:"li"},"limits")," = 1, then it will be applied to all columns and considered as maximum value that must not be exceeded;"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"limits")," may be set separately for each column, as in the example above: ",(0,r.kt)("inlineCode",{parentName:"li"},"limits")," = ","[0.25, 0.3, 300]"," means that standard deviation (or 3 standard deviations, as in the example, since ",(0,r.kt)("inlineCode",{parentName:"li"},"n_std")," = 3) for the first column must be < 0.25, for the second < 0.3 and for the last column < 300. That way length of the ",(0,r.kt)("inlineCode",{parentName:"li"},"limits")," must be equal to the number of columns.")),(0,r.kt)("h2",{id:"returning-parameters"},"Returning Parameters"),(0,r.kt)("p",null,"The method returns three parameters: "),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"log")," : ",(0,r.kt)("a",{parentName:"li",href:"/docs/docs_data_analysis/documentation/data_access/citros_dict#citros_data_analysis.data_access.citros_dict.CitrosDict"},(0,r.kt)("strong",{parentName:"a"},"CitrosDict"))," - dictionary with test result summary;")),(0,r.kt)("mermaid",{value:'flowchart TD\nlog_std((log_std)) --- init1("\'test_param\'") --\x3e |initial \\ntest parameters| init1_("{\'limits\': list,\n\'n_std\': int,\n\'nan_passed\': bool}")\n\nlog_std --- col1("column label,\n    str") --\x3e|whether the test\\n passed or failed| B1("{\'passed\': bool}")\n\ncol1 --\x3e |fraction\\n of the points\\n that pass the test| C1("{\'pass_rate\': float}")\n\ncol1 ---|points that failed| D1(\'failed\') --\x3e |"indexes and values\\nof the x coordinate\\n {x_index: x_value}"|D1a("{int : float}")\n\ncol1 ---|"data points that have\\n NaN (Not a Number) values\\n for standard deviation"| E1(\'nan_std\') --\x3e |"indexes and values\\nof the x coordinate\\n {x_index: x_value}"|E1a("{int : float}")'}),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},(0,r.kt)("inlineCode",{parentName:"p"},"table")," : ",(0,r.kt)("a",{parentName:"p",href:"https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html"},(0,r.kt)("strong",{parentName:"a"},"pandas.DataFrame"))," - table that specifies whether the corresponding standard deviation boundary point passes the test (True) or not (False).")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},(0,r.kt)("inlineCode",{parentName:"p"},"fig")," : ",(0,r.kt)("a",{parentName:"p",href:"https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.Figure"},(0,r.kt)("strong",{parentName:"a"},"matplotlib.figure.Figure"))))),(0,r.kt)("p",null,"As for the mentioned above example, the output is:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> fig.show()\n")),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"fig6",src:a(4450).Z,title:"Fig6",width:"732",height:"485"})),(0,r.kt)("p",null,"Red lines show the limits, that must not be exceed by the values of standard deviations. In this example the test is passed.\nLike in ",(0,r.kt)("a",{parentName:"p",href:"/docs/docs_data_analysis/validation/standard_deviation_boundary_test"},(0,r.kt)("strong",{parentName:"a"},"std_bound_test()")),", to change the style of the plot, parameters ",(0,r.kt)("inlineCode",{parentName:"p"},"std_area"),", ",(0,r.kt)("inlineCode",{parentName:"p"},"std_lines")," and ",(0,r.kt)("inlineCode",{parentName:"p"},"std_color")," may be used: setting ",(0,r.kt)("inlineCode",{parentName:"p"},"std_area")," = True to fill the area within y = 0 and the standard deviation (like we did above), ",(0,r.kt)("inlineCode",{parentName:"p"},"std_lines")," = False to remove the borders and ",(0,r.kt)("inlineCode",{parentName:"p"},"std_color")," change the color of the standard deviation boundary."),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> print(table)\n")),(0,r.kt)("table",null,(0,r.kt)("thead",{parentName:"table"},(0,r.kt)("tr",{parentName:"thead"},(0,r.kt)("th",{parentName:"tr",align:null}),(0,r.kt)("th",{parentName:"tr",align:null},"data.time"),(0,r.kt)("th",{parentName:"tr",align:null},"data.x.x_1"),(0,r.kt)("th",{parentName:"tr",align:null},"data.x.x_2"),(0,r.kt)("th",{parentName:"tr",align:null},"data.x.x_3"))),(0,r.kt)("tbody",{parentName:"table"},(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"data.time_id"),(0,r.kt)("td",{parentName:"tr",align:null}),(0,r.kt)("td",{parentName:"tr",align:null}),(0,r.kt)("td",{parentName:"tr",align:null}),(0,r.kt)("td",{parentName:"tr",align:null})),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"0"),(0,r.kt)("td",{parentName:"tr",align:null},"0.000000"),(0,r.kt)("td",{parentName:"tr",align:null},"True"),(0,r.kt)("td",{parentName:"tr",align:null},"True"),(0,r.kt)("td",{parentName:"tr",align:null},"True")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"1"),(0,r.kt)("td",{parentName:"tr",align:null},"0.052632"),(0,r.kt)("td",{parentName:"tr",align:null},"True"),(0,r.kt)("td",{parentName:"tr",align:null},"True"),(0,r.kt)("td",{parentName:"tr",align:null},"True")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"2"),(0,r.kt)("td",{parentName:"tr",align:null},"0.105263"),(0,r.kt)("td",{parentName:"tr",align:null},"True"),(0,r.kt)("td",{parentName:"tr",align:null},"True"),(0,r.kt)("td",{parentName:"tr",align:null},"True")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"..."),(0,r.kt)("td",{parentName:"tr",align:null},"..."),(0,r.kt)("td",{parentName:"tr",align:null},"..."),(0,r.kt)("td",{parentName:"tr",align:null},"..."),(0,r.kt)("td",{parentName:"tr",align:null},"...")))),(0,r.kt)("p",null,(0,r.kt)("inlineCode",{parentName:"p"},"log")," can be accessed like a regular python dictionary and can be printed using the ",(0,r.kt)("a",{parentName:"p",href:"/docs/docs_data_analysis/documentation/data_access/citros_dict#citros_data_analysis.data_access.citros_dict.CitrosDict.print"},(0,r.kt)("strong",{parentName:"a"},"print()"))," method to display it as a JSON object:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> log.print()\n")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-js"},"{\n 'test_param': {\n   'limits': [0.25, 0.3, 300],\n   'n_std': 3,\n   'nan_passed': True\n },\n 'data.x.x_1': {\n   'passed': True,\n   'pass_rate': 1.0,\n   'failed': {\n   },\n   'nan_std': {\n   }\n },\n 'data.x.x_2': {\n   'passed': True,\n   'pass_rate': 1.0,\n   'failed': {\n   },\n   'nan_std': {\n   }\n },\n 'data.x.x_3': {\n   'passed': True,\n   'pass_rate': 1.0,\n   'failed': {\n   },\n   'nan_std': {\n   }\n }\n}\n")),(0,r.kt)("p",null,(0,r.kt)("inlineCode",{parentName:"p"},"log")," contains summary of the test result: "),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},"initial test parameters:"),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> log['test_param'].print()\n")),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-js"},"{\n 'limits': [0.25, 0.3, 300],\n 'n_std': 3,\n 'nan_passed': True\n}\n"))),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},"Information about the test results of each column, let's take a look at the 'data.x.x_1':"),(0,r.kt)("ul",{parentName:"li"},(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},"'passed' - whether the test for the column was passed (True) or not (False):"),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> print(log['data.x.x_1']['passed'])\n")),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-js"},"True\n"))),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},"'pass_rate' - fraction of the points that pass the test, 0 < 'pass_rate' < 1:"),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> print(log['data.x.x_1']['pass_rate'])\n")),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-js"},"1.0\n"))),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},"'failed' - dictionaries with indexes and corresponding them values of the x axis ('data.time' in this case) for points that failed the test. Since all points of 'data.x.x_1' passed the test, log","['data.x.x_1']['failed']"," is empty:"),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> log['data.x.x_1']['failed'].print()\n")),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-js"},"{\n}\n"))),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},"'nan_std' - if some of the standard deviations points could not be calculated (for example, number of simulations for this index is less then two, that may occurs if the method of data assignment ",(0,r.kt)("inlineCode",{parentName:"p"},"method")," = 'bin' has been chosen), their indexes and values of the x axis will be stored in the same way, as in the section 'failed':"),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> log['data.x.x_1']['nan_std'].print()\n")),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-js"},"{\n}\n")))))))}u.isMDXComponent=!0},4450:(t,e,a)=>{a.d(e,{Z:()=>n});const n=a.p+"assets/images/fig29-4cf511c675e77d763941126d34124c3b.png"}}]);
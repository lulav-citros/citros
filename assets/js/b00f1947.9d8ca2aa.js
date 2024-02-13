"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[24934],{3905:(t,e,a)=>{a.d(e,{Zo:()=>m,kt:()=>_});var n=a(67294);function s(t,e,a){return e in t?Object.defineProperty(t,e,{value:a,enumerable:!0,configurable:!0,writable:!0}):t[e]=a,t}function r(t,e){var a=Object.keys(t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(t);e&&(n=n.filter((function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable}))),a.push.apply(a,n)}return a}function i(t){for(var e=1;e<arguments.length;e++){var a=null!=arguments[e]?arguments[e]:{};e%2?r(Object(a),!0).forEach((function(e){s(t,e,a[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(a)):r(Object(a)).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(a,e))}))}return t}function l(t,e){if(null==t)return{};var a,n,s=function(t,e){if(null==t)return{};var a,n,s={},r=Object.keys(t);for(n=0;n<r.length;n++)a=r[n],e.indexOf(a)>=0||(s[a]=t[a]);return s}(t,e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(t);for(n=0;n<r.length;n++)a=r[n],e.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(t,a)&&(s[a]=t[a])}return s}var o=n.createContext({}),p=function(t){var e=n.useContext(o),a=e;return t&&(a="function"==typeof t?t(e):i(i({},e),t)),a},m=function(t){var e=p(t.components);return n.createElement(o.Provider,{value:e},t.children)},d="mdxType",c={inlineCode:"code",wrapper:function(t){var e=t.children;return n.createElement(n.Fragment,{},e)}},u=n.forwardRef((function(t,e){var a=t.components,s=t.mdxType,r=t.originalType,o=t.parentName,m=l(t,["components","mdxType","originalType","parentName"]),d=p(a),u=s,_=d["".concat(o,".").concat(u)]||d[u]||c[u]||r;return a?n.createElement(_,i(i({ref:e},m),{},{components:a})):n.createElement(_,i({ref:e},m))}));function _(t,e){var a=arguments,s=e&&e.mdxType;if("string"==typeof t||s){var r=a.length,i=new Array(r);i[0]=u;var l={};for(var o in e)hasOwnProperty.call(e,o)&&(l[o]=e[o]);l.originalType=t,l[d]="string"==typeof t?t:s,i[1]=l;for(var p=2;p<r;p++)i[p]=a[p];return n.createElement.apply(null,i)}return n.createElement.apply(null,a)}u.displayName="MDXCreateElement"},91410:(t,e,a)=>{a.r(e),a.d(e,{assets:()=>o,contentTitle:()=>i,default:()=>c,frontMatter:()=>r,metadata:()=>l,toc:()=>p});var n=a(87462),s=(a(67294),a(3905));const r={toc_max_heading_level:4,hide_title:!0,sidebar_position:7,sidebar_label:"Set Multiple Tests",description:"Set multiple tests"},i="Set Multiple Tests",l={unversionedId:"data_analysis/validation/set_multiple_tests",id:"version-0.2.48/data_analysis/validation/set_multiple_tests",title:"Set Multiple Tests",description:"Set multiple tests",source:"@site/versioned_docs/version-0.2.48/data_analysis/validation/set_multiple_tests.md",sourceDirName:"data_analysis/validation",slug:"/data_analysis/validation/set_multiple_tests",permalink:"/docs/0.2.48/data_analysis/validation/set_multiple_tests",draft:!1,tags:[],version:"0.2.48",sidebarPosition:7,frontMatter:{toc_max_heading_level:4,hide_title:!0,sidebar_position:7,sidebar_label:"Set Multiple Tests",description:"Set multiple tests"},sidebar:"gettingStartedSidebar",previous:{title:"Testing Each Simulation",permalink:"/docs/0.2.48/data_analysis/validation/testing_each_simulation"},next:{title:"Class Validation",permalink:"/docs/0.2.48/data_analysis/documentation/validation/"}},o={},p=[{value:"Returning Parameters",id:"returning-parameters",level:2}],m={toc:p},d="wrapper";function c(t){let{components:e,...r}=t;return(0,s.kt)(d,(0,n.Z)({},m,r,{components:e,mdxType:"MDXLayout"}),(0,s.kt)("h1",{id:"set-multiple-tests"},"Set Multiple Tests"),(0,s.kt)("p",null,"It is possible to set several tests by the method ",(0,s.kt)("a",{parentName:"p",href:"/docs/0.2.48/data_analysis/documentation/validation/#validation.validation.Validation.set_tests"},(0,s.kt)("strong",{parentName:"a"},"set_tests")),":"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},"Validation().set_tests(test_method = {<test_type> : <parameters>})\n")),(0,s.kt)("p",null,"The types of tests and corresponding parameters are provided as a dictionary by a ",(0,s.kt)("inlineCode",{parentName:"p"},"test_method")," parameter, where each test is represented by a key-value pair. The key defines the name of the test, and the corresponding value is a dictionary containing the test parameters. The allowed test_type keywords:"),(0,s.kt)("ul",null,(0,s.kt)("li",{parentName:"ul"},"'std_bound' - perform ",(0,s.kt)("a",{parentName:"li",href:"/docs/0.2.48/data_analysis/validation/standard_deviation_boundary_test"},(0,s.kt)("strong",{parentName:"a"},"std_bound_test()")),";"),(0,s.kt)("li",{parentName:"ul"},"'mean_test' - set ",(0,s.kt)("a",{parentName:"li",href:"/docs/0.2.48/data_analysis/validation/mean_value_test"},(0,s.kt)("strong",{parentName:"a"},"mean_test()")),";"),(0,s.kt)("li",{parentName:"ul"},"'sid_test' - for ",(0,s.kt)("a",{parentName:"li",href:"/docs/0.2.48/data_analysis/validation/testing_each_simulation"},(0,s.kt)("strong",{parentName:"a"},"sid_test()")),";"),(0,s.kt)("li",{parentName:"ul"},"'norm_L2' and 'norm_Linf' - set ",(0,s.kt)("a",{parentName:"li",href:"/docs/0.2.48/data_analysis/validation/norm_test"},(0,s.kt)("strong",{parentName:"a"},"norm_test()")),".")),(0,s.kt)("p",null,"Once again, let's query data from the batch 'planets', topic 'A', created by simulation 'simulation_systems' and do the necessary data preparations (see ",(0,s.kt)("a",{parentName:"p",href:"/docs/0.2.48/data_analysis/validation/getting_started"},"Getting started"),"):"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> from citros import CitrosDB, Validation\n\n>>> citros = CitrosDB()\n>>> df = citros.simulation('simulation_systems').batch('planets').topic('A').data(['data.x.x_1', 'data.x.x_2', 'data.x.x_3', 'data.time'])\n>>> V = Validation(df, data_label = ['data.x.x_1', 'data.x.x_2', 'data.x.x_3'], \n                   param_label = 'data.time', method = 'scale', num = 20, units = 'm')\n")),(0,s.kt)("p",null,"For example, to set a standard deviation boundary test and a test on norm ",(0,s.kt)("span",{parentName:"p",className:"math math-inline"},(0,s.kt)("span",{parentName:"span",className:"katex"},(0,s.kt)("span",{parentName:"span",className:"katex-mathml"},(0,s.kt)("math",{parentName:"span",xmlns:"http://www.w3.org/1998/Math/MathML"},(0,s.kt)("semantics",{parentName:"math"},(0,s.kt)("mrow",{parentName:"semantics"},(0,s.kt)("msup",{parentName:"mrow"},(0,s.kt)("mi",{parentName:"msup"},"L"),(0,s.kt)("mn",{parentName:"msup"},"2"))),(0,s.kt)("annotation",{parentName:"semantics",encoding:"application/x-tex"},"L^2")))),(0,s.kt)("span",{parentName:"span",className:"katex-html","aria-hidden":"true"},(0,s.kt)("span",{parentName:"span",className:"base"},(0,s.kt)("span",{parentName:"span",className:"strut",style:{height:"0.8141em"}}),(0,s.kt)("span",{parentName:"span",className:"mord"},(0,s.kt)("span",{parentName:"span",className:"mord mathnormal"},"L"),(0,s.kt)("span",{parentName:"span",className:"msupsub"},(0,s.kt)("span",{parentName:"span",className:"vlist-t"},(0,s.kt)("span",{parentName:"span",className:"vlist-r"},(0,s.kt)("span",{parentName:"span",className:"vlist",style:{height:"0.8141em"}},(0,s.kt)("span",{parentName:"span",style:{top:"-3.063em",marginRight:"0.05em"}},(0,s.kt)("span",{parentName:"span",className:"pstrut",style:{height:"2.7em"}}),(0,s.kt)("span",{parentName:"span",className:"sizing reset-size6 size3 mtight"},(0,s.kt)("span",{parentName:"span",className:"mord mtight"},"2")))))))))))),":"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> logs, tables, figs = V.set_tests(test_method = \n                                 {'std_bound' : {'limits' : [0.25, 0.3, [-150, 300]], 'n_std': 3},\n                                  'norm_L2' : {'limits' : [0.3, 0.35, 450]}})\n")),(0,s.kt)("h2",{id:"returning-parameters"},"Returning Parameters"),(0,s.kt)("p",null,"The method returns three dictionaries that contain the output results of each test: "),(0,s.kt)("ul",null,(0,s.kt)("li",{parentName:"ul"},(0,s.kt)("p",{parentName:"li"},(0,s.kt)("inlineCode",{parentName:"p"},"log")," : ",(0,s.kt)("a",{parentName:"p",href:"/docs/0.2.48/data_analysis/documentation/access/citros_dict#access.citros_dict.CitrosDict"},(0,s.kt)("strong",{parentName:"a"},"CitrosDict"))," - dictionary with test result summary for each test method;")),(0,s.kt)("li",{parentName:"ul"},(0,s.kt)("p",{parentName:"li"},(0,s.kt)("inlineCode",{parentName:"p"},"table")," :  dictionary with ",(0,s.kt)("a",{parentName:"p",href:"https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html"},(0,s.kt)("strong",{parentName:"a"},"pandas.DataFrame"))," tables for each test method that specifies for each point whether it passes the test (True) or fails (False).")),(0,s.kt)("li",{parentName:"ul"},(0,s.kt)("p",{parentName:"li"},(0,s.kt)("inlineCode",{parentName:"p"},"fig")," : dictionary with figures ",(0,s.kt)("a",{parentName:"p",href:"https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.Figure"},(0,s.kt)("strong",{parentName:"a"},"matplotlib.figure.Figure"))," for each test method."))),(0,s.kt)("mermaid",{value:"flowchart TD\n    Results(\"set_tests()\n    output\") --- logs(\"logs : {\n    'std_bound' : log_std,\n    'mean' : log_mean,\n    'sid' : log_sid,\n    'norm_L2' : log_norm,\n    'norm_Linf' : log_norm\n    }\")\n    Results ---  tables(\"tables : {\n    'std_bound' : DataFrame,\n    'mean' : DataFrame,\n    'sid' : DataFrame,\n    'norm_L2' : DataFrame,\n    'norm_Linf' : DataFrame\n    }\") -.- DataFrame(\"DataFrame - pandas.DataFrame\")\n    \n    Results --- figures(\"figures : {\n    'std_bound' : fig_std,\n    'mean' : fig_mean,\n    'sid' : fig_sid,\n    'norm_L2' : fig_norm,\n    'norm_Linf' : fig_norm\n    }\") -.- fig(\"fig_... - matplotlib.figure.Figure\")"}),(0,s.kt)("p",null,"For example, to get detailed information about the results of the norm test:"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> logs['norm_L2'].print()\n")),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-js"},"{\n 'test_param': {\n   'limits': [0.3, 0.35, 450]\n },\n 'data.x.x_1': {\n   'passed': True,\n   'pass_rate': 1.0,\n...\n }\n}\n")),(0,s.kt)("p",null,"To get table that specifies for each simulation whether the norm is less then the given limit:"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> print(tables['norm_L2'])\n")),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-js"},"     data.x.x_1  data.x.x_2  data.x.x_3\nsid                                    \n1          True        True       False\n2          True        True        True\n3          True        True       False\n")),(0,s.kt)("p",null,"To get the corresponding figure:"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> figs['norm_L2']\n")),(0,s.kt)("p",null,(0,s.kt)("img",{alt:"fig4",src:a(87544).Z,title:"Fig4",width:"725",height:"602"})),(0,s.kt)("p",null,"See ",(0,s.kt)("a",{parentName:"p",href:"/docs/0.2.48/data_analysis/validation/standard_deviation_boundary_test"},(0,s.kt)("strong",{parentName:"a"},"std_bound_test()")),", ",(0,s.kt)("a",{parentName:"p",href:"/docs/0.2.48/data_analysis/validation/mean_value_test"},(0,s.kt)("strong",{parentName:"a"},"mean_test()")),", ",(0,s.kt)("a",{parentName:"p",href:"/docs/0.2.48/data_analysis/validation/testing_each_simulation"},(0,s.kt)("strong",{parentName:"a"},"sid_test()"))," and ",(0,s.kt)("a",{parentName:"p",href:"/docs/0.2.48/data_analysis/validation/norm_test"},(0,s.kt)("strong",{parentName:"a"},"norm_test()"))," for the output details."))}c.isMDXComponent=!0},87544:(t,e,a)=>{a.d(e,{Z:()=>n});const n=a.p+"assets/images/fig24-a82f3acb90879ba5cd4340e067d47183.png"}}]);
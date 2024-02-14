"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[26283],{3905:(a,e,t)=>{t.d(e,{Zo:()=>o,kt:()=>d});var n=t(67294);function s(a,e,t){return e in a?Object.defineProperty(a,e,{value:t,enumerable:!0,configurable:!0,writable:!0}):a[e]=t,a}function m(a,e){var t=Object.keys(a);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(a);e&&(n=n.filter((function(e){return Object.getOwnPropertyDescriptor(a,e).enumerable}))),t.push.apply(t,n)}return t}function r(a){for(var e=1;e<arguments.length;e++){var t=null!=arguments[e]?arguments[e]:{};e%2?m(Object(t),!0).forEach((function(e){s(a,e,t[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(a,Object.getOwnPropertyDescriptors(t)):m(Object(t)).forEach((function(e){Object.defineProperty(a,e,Object.getOwnPropertyDescriptor(t,e))}))}return a}function p(a,e){if(null==a)return{};var t,n,s=function(a,e){if(null==a)return{};var t,n,s={},m=Object.keys(a);for(n=0;n<m.length;n++)t=m[n],e.indexOf(t)>=0||(s[t]=a[t]);return s}(a,e);if(Object.getOwnPropertySymbols){var m=Object.getOwnPropertySymbols(a);for(n=0;n<m.length;n++)t=m[n],e.indexOf(t)>=0||Object.prototype.propertyIsEnumerable.call(a,t)&&(s[t]=a[t])}return s}var l=n.createContext({}),i=function(a){var e=n.useContext(l),t=e;return a&&(t="function"==typeof a?a(e):r(r({},e),a)),t},o=function(a){var e=i(a.components);return n.createElement(l.Provider,{value:e},a.children)},N="mdxType",c={inlineCode:"code",wrapper:function(a){var e=a.children;return n.createElement(n.Fragment,{},e)}},k=n.forwardRef((function(a,e){var t=a.components,s=a.mdxType,m=a.originalType,l=a.parentName,o=p(a,["components","mdxType","originalType","parentName"]),N=i(t),k=s,d=N["".concat(l,".").concat(k)]||N[k]||c[k]||m;return t?n.createElement(d,r(r({ref:e},o),{},{components:t})):n.createElement(d,r({ref:e},o))}));function d(a,e){var t=arguments,s=e&&e.mdxType;if("string"==typeof a||s){var m=t.length,r=new Array(m);r[0]=k;var p={};for(var l in e)hasOwnProperty.call(e,l)&&(p[l]=e[l]);p.originalType=a,p[N]="string"==typeof a?a:s,r[1]=p;for(var i=2;i<m;i++)r[i]=t[i];return n.createElement.apply(null,r)}return n.createElement.apply(null,t)}k.displayName="MDXCreateElement"},13601:(a,e,t)=>{t.r(e),t.d(e,{assets:()=>l,contentTitle:()=>r,default:()=>c,frontMatter:()=>m,metadata:()=>p,toc:()=>i});var n=t(87462),s=(t(67294),t(3905));const m={toc_max_heading_level:4,hide_title:!0,sidebar_position:6,sidebar_label:"Norm Test",description:"Calculate and check norm"},r="Norm Test",p={unversionedId:"data_analysis/validation/norm_test",id:"version-0.2.52/data_analysis/validation/norm_test",title:"Norm Test",description:"Calculate and check norm",source:"@site/versioned_docs/version-0.2.52/data_analysis/validation/norm_test.md",sourceDirName:"data_analysis/validation",slug:"/data_analysis/validation/norm_test",permalink:"/docs/data_analysis/validation/norm_test",draft:!1,tags:[],version:"0.2.52",sidebarPosition:6,frontMatter:{toc_max_heading_level:4,hide_title:!0,sidebar_position:6,sidebar_label:"Norm Test",description:"Calculate and check norm"},sidebar:"gettingStartedSidebar",previous:{title:"Standard Deviation Test",permalink:"/docs/data_analysis/validation/standard_deviation_test"},next:{title:"Testing Each Simulation",permalink:"/docs/data_analysis/validation/testing_each_simulation"}},l={},i=[{value:"Setting Limits",id:"setting-limits",level:2},{value:"Returning Parameters",id:"returning-parameters",level:2}],o={toc:i},N="wrapper";function c(a){let{components:e,...m}=a;return(0,s.kt)(N,(0,n.Z)({},o,m,{components:e,mdxType:"MDXLayout"}),(0,s.kt)("h1",{id:"norm-test"},"Norm Test"),(0,s.kt)("p",null,(0,s.kt)("a",{parentName:"p",href:"/docs/data_analysis/documentation/validation/#validation.validation.Validation.norm_test"},(0,s.kt)("strong",{parentName:"a"},"norm_test()"))," - test whether norm of the each simulation is less than the given limit."),(0,s.kt)("p",null,"Let's query data for a 3 dimensional vector, assign indexes to data to set correspondence between different simulations (see ",(0,s.kt)("a",{parentName:"p",href:"/docs/data_analysis/validation/getting_started"},"Getting started")," page) and test whether the norm of each simulation is within the given limits:"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> df = citros.topic('A').data(['data.x.x_1', 'data.x.x_2', 'data.x.x_3', 'data.time'])\n>>> V = va.Validation(df, data_label = ['data.x.x_1', 'data.x.x_2', 'data.x.x_3'], \n                      param_label = 'data.time', method = 'scale', num = 20, units = 'm')\n                      \n>>> log_norm, table, fig = V.norm_test(norm_type = 'L2', limits = [0.3, 0.35, 450])\n")),(0,s.kt)("p",null,"The type of the norm may be specified by ",(0,s.kt)("inlineCode",{parentName:"p"},"norm_type")," parameter:"),(0,s.kt)("ul",null,(0,s.kt)("li",{parentName:"ul"},(0,s.kt)("inlineCode",{parentName:"li"},"norm_type")," = 'L2' - Euclidean norm or ",(0,s.kt)("span",{parentName:"li",className:"math math-inline"},(0,s.kt)("span",{parentName:"span",className:"katex"},(0,s.kt)("span",{parentName:"span",className:"katex-mathml"},(0,s.kt)("math",{parentName:"span",xmlns:"http://www.w3.org/1998/Math/MathML"},(0,s.kt)("semantics",{parentName:"math"},(0,s.kt)("mrow",{parentName:"semantics"},(0,s.kt)("msup",{parentName:"mrow"},(0,s.kt)("mi",{parentName:"msup"},"L"),(0,s.kt)("mn",{parentName:"msup"},"2"))),(0,s.kt)("annotation",{parentName:"semantics",encoding:"application/x-tex"},"L^2")))),(0,s.kt)("span",{parentName:"span",className:"katex-html","aria-hidden":"true"},(0,s.kt)("span",{parentName:"span",className:"base"},(0,s.kt)("span",{parentName:"span",className:"strut",style:{height:"0.8141em"}}),(0,s.kt)("span",{parentName:"span",className:"mord"},(0,s.kt)("span",{parentName:"span",className:"mord mathnormal"},"L"),(0,s.kt)("span",{parentName:"span",className:"msupsub"},(0,s.kt)("span",{parentName:"span",className:"vlist-t"},(0,s.kt)("span",{parentName:"span",className:"vlist-r"},(0,s.kt)("span",{parentName:"span",className:"vlist",style:{height:"0.8141em"}},(0,s.kt)("span",{parentName:"span",style:{top:"-3.063em",marginRight:"0.05em"}},(0,s.kt)("span",{parentName:"span",className:"pstrut",style:{height:"2.7em"}}),(0,s.kt)("span",{parentName:"span",className:"sizing reset-size6 size3 mtight"},(0,s.kt)("span",{parentName:"span",className:"mord mtight"},"2"))))))))))))," norm, square root of the sum of the squares:",(0,s.kt)("div",{parentName:"li",className:"math math-display"},(0,s.kt)("span",{parentName:"div",className:"katex-display"},(0,s.kt)("span",{parentName:"span",className:"katex"},(0,s.kt)("span",{parentName:"span",className:"katex-mathml"},(0,s.kt)("math",{parentName:"span",xmlns:"http://www.w3.org/1998/Math/MathML",display:"block"},(0,s.kt)("semantics",{parentName:"math"},(0,s.kt)("mrow",{parentName:"semantics"},(0,s.kt)("msqrt",{parentName:"mrow"},(0,s.kt)("mrow",{parentName:"msqrt"},(0,s.kt)("munderover",{parentName:"mrow"},(0,s.kt)("mo",{parentName:"munderover"},"\u2211"),(0,s.kt)("mrow",{parentName:"munderover"},(0,s.kt)("mi",{parentName:"mrow"},"k"),(0,s.kt)("mo",{parentName:"mrow"},"="),(0,s.kt)("mn",{parentName:"mrow"},"1")),(0,s.kt)("mi",{parentName:"munderover"},"N")),(0,s.kt)("msubsup",{parentName:"mrow"},(0,s.kt)("mi",{parentName:"msubsup"},"x"),(0,s.kt)("mi",{parentName:"msubsup"},"k"),(0,s.kt)("mn",{parentName:"msubsup"},"2"))))),(0,s.kt)("annotation",{parentName:"semantics",encoding:"application/x-tex"},"\\sqrt{\\sum_{k=1}^{N} x_k^2}")))),(0,s.kt)("span",{parentName:"span",className:"katex-html","aria-hidden":"true"},(0,s.kt)("span",{parentName:"span",className:"base"},(0,s.kt)("span",{parentName:"span",className:"strut",style:{height:"3.3582em",verticalAlign:"-1.3021em"}}),(0,s.kt)("span",{parentName:"span",className:"mord sqrt"},(0,s.kt)("span",{parentName:"span",className:"vlist-t vlist-t2"},(0,s.kt)("span",{parentName:"span",className:"vlist-r"},(0,s.kt)("span",{parentName:"span",className:"vlist",style:{height:"2.0561em"}},(0,s.kt)("span",{parentName:"span",className:"svg-align",style:{top:"-5.3182em"}},(0,s.kt)("span",{parentName:"span",className:"pstrut",style:{height:"5.3182em"}}),(0,s.kt)("span",{parentName:"span",className:"mord",style:{paddingLeft:"1.056em"}},(0,s.kt)("span",{parentName:"span",className:"mop op-limits"},(0,s.kt)("span",{parentName:"span",className:"vlist-t vlist-t2"},(0,s.kt)("span",{parentName:"span",className:"vlist-r"},(0,s.kt)("span",{parentName:"span",className:"vlist",style:{height:"1.8283em"}},(0,s.kt)("span",{parentName:"span",style:{top:"-1.8479em",marginLeft:"0em"}},(0,s.kt)("span",{parentName:"span",className:"pstrut",style:{height:"3.05em"}}),(0,s.kt)("span",{parentName:"span",className:"sizing reset-size6 size3 mtight"},(0,s.kt)("span",{parentName:"span",className:"mord mtight"},(0,s.kt)("span",{parentName:"span",className:"mord mathnormal mtight",style:{marginRight:"0.03148em"}},"k"),(0,s.kt)("span",{parentName:"span",className:"mrel mtight"},"="),(0,s.kt)("span",{parentName:"span",className:"mord mtight"},"1")))),(0,s.kt)("span",{parentName:"span",style:{top:"-3.05em"}},(0,s.kt)("span",{parentName:"span",className:"pstrut",style:{height:"3.05em"}}),(0,s.kt)("span",{parentName:"span"},(0,s.kt)("span",{parentName:"span",className:"mop op-symbol large-op"},"\u2211"))),(0,s.kt)("span",{parentName:"span",style:{top:"-4.3em",marginLeft:"0em"}},(0,s.kt)("span",{parentName:"span",className:"pstrut",style:{height:"3.05em"}}),(0,s.kt)("span",{parentName:"span",className:"sizing reset-size6 size3 mtight"},(0,s.kt)("span",{parentName:"span",className:"mord mtight"},(0,s.kt)("span",{parentName:"span",className:"mord mathnormal mtight",style:{marginRight:"0.10903em"}},"N"))))),(0,s.kt)("span",{parentName:"span",className:"vlist-s"},"\u200b")),(0,s.kt)("span",{parentName:"span",className:"vlist-r"},(0,s.kt)("span",{parentName:"span",className:"vlist",style:{height:"1.3021em"}},(0,s.kt)("span",{parentName:"span"}))))),(0,s.kt)("span",{parentName:"span",className:"mspace",style:{marginRight:"0.1667em"}}),(0,s.kt)("span",{parentName:"span",className:"mord"},(0,s.kt)("span",{parentName:"span",className:"mord mathnormal"},"x"),(0,s.kt)("span",{parentName:"span",className:"msupsub"},(0,s.kt)("span",{parentName:"span",className:"vlist-t vlist-t2"},(0,s.kt)("span",{parentName:"span",className:"vlist-r"},(0,s.kt)("span",{parentName:"span",className:"vlist",style:{height:"0.7959em"}},(0,s.kt)("span",{parentName:"span",style:{top:"-2.3987em",marginLeft:"0em",marginRight:"0.05em"}},(0,s.kt)("span",{parentName:"span",className:"pstrut",style:{height:"2.7em"}}),(0,s.kt)("span",{parentName:"span",className:"sizing reset-size6 size3 mtight"},(0,s.kt)("span",{parentName:"span",className:"mord mathnormal mtight",style:{marginRight:"0.03148em"}},"k"))),(0,s.kt)("span",{parentName:"span",style:{top:"-3.0448em",marginRight:"0.05em"}},(0,s.kt)("span",{parentName:"span",className:"pstrut",style:{height:"2.7em"}}),(0,s.kt)("span",{parentName:"span",className:"sizing reset-size6 size3 mtight"},(0,s.kt)("span",{parentName:"span",className:"mord mtight"},"2")))),(0,s.kt)("span",{parentName:"span",className:"vlist-s"},"\u200b")),(0,s.kt)("span",{parentName:"span",className:"vlist-r"},(0,s.kt)("span",{parentName:"span",className:"vlist",style:{height:"0.3013em"}},(0,s.kt)("span",{parentName:"span"})))))))),(0,s.kt)("span",{parentName:"span",style:{top:"-4.0161em"}},(0,s.kt)("span",{parentName:"span",className:"pstrut",style:{height:"5.3182em"}}),(0,s.kt)("span",{parentName:"span",className:"hide-tail",style:{minWidth:"0.742em",height:"3.3982em"}},(0,s.kt)("svg",{parentName:"span",xmlns:"http://www.w3.org/2000/svg",width:"400em",height:"3.3982em",viewBox:"0 0 400000 3398",preserveAspectRatio:"xMinYMin slice"},(0,s.kt)("path",{parentName:"svg",d:"M702 80H40000040\nH742v3264l-4 4-4 4c-.667.7 -2 1.5-4 2.5s-4.167 1.833-6.5 2.5-5.5 1-9.5 1\nh-12l-28-84c-16.667-52-96.667 -294.333-240-727l-212 -643 -85 170\nc-4-3.333-8.333-7.667-13 -13l-13-13l77-155 77-156c66 199.333 139 419.667\n219 661 l218 661zM702 80H400000v40H742z"}))))),(0,s.kt)("span",{parentName:"span",className:"vlist-s"},"\u200b")),(0,s.kt)("span",{parentName:"span",className:"vlist-r"},(0,s.kt)("span",{parentName:"span",className:"vlist",style:{height:"1.3021em"}},(0,s.kt)("span",{parentName:"span"}))))))))))),(0,s.kt)("li",{parentName:"ul"},(0,s.kt)("inlineCode",{parentName:"li"},"norm_type")," = 'Linf' - absolute maximum:",(0,s.kt)("div",{parentName:"li",className:"math math-display"},(0,s.kt)("span",{parentName:"div",className:"katex-display"},(0,s.kt)("span",{parentName:"span",className:"katex"},(0,s.kt)("span",{parentName:"span",className:"katex-mathml"},(0,s.kt)("math",{parentName:"span",xmlns:"http://www.w3.org/1998/Math/MathML",display:"block"},(0,s.kt)("semantics",{parentName:"math"},(0,s.kt)("mrow",{parentName:"semantics"},(0,s.kt)("munder",{parentName:"mrow"},(0,s.kt)("mrow",{parentName:"munder"},(0,s.kt)("mi",{parentName:"mrow"},"max"),(0,s.kt)("mo",{parentName:"mrow"},"\u2061")),(0,s.kt)("mi",{parentName:"munder"},"k")),(0,s.kt)("mrow",{parentName:"mrow"},(0,s.kt)("mi",{parentName:"mrow",mathvariant:"normal"},"\u2223"),(0,s.kt)("msub",{parentName:"mrow"},(0,s.kt)("mi",{parentName:"msub"},"x"),(0,s.kt)("mi",{parentName:"msub"},"k")),(0,s.kt)("mi",{parentName:"mrow",mathvariant:"normal"},"\u2223"))),(0,s.kt)("annotation",{parentName:"semantics",encoding:"application/x-tex"},"\\max_k{|x_k|}")))),(0,s.kt)("span",{parentName:"span",className:"katex-html","aria-hidden":"true"},(0,s.kt)("span",{parentName:"span",className:"base"},(0,s.kt)("span",{parentName:"span",className:"strut",style:{height:"1.5021em",verticalAlign:"-0.7521em"}}),(0,s.kt)("span",{parentName:"span",className:"mop op-limits"},(0,s.kt)("span",{parentName:"span",className:"vlist-t vlist-t2"},(0,s.kt)("span",{parentName:"span",className:"vlist-r"},(0,s.kt)("span",{parentName:"span",className:"vlist",style:{height:"0.4306em"}},(0,s.kt)("span",{parentName:"span",style:{top:"-2.3479em",marginLeft:"0em"}},(0,s.kt)("span",{parentName:"span",className:"pstrut",style:{height:"3em"}}),(0,s.kt)("span",{parentName:"span",className:"sizing reset-size6 size3 mtight"},(0,s.kt)("span",{parentName:"span",className:"mord mathnormal mtight",style:{marginRight:"0.03148em"}},"k"))),(0,s.kt)("span",{parentName:"span",style:{top:"-3em"}},(0,s.kt)("span",{parentName:"span",className:"pstrut",style:{height:"3em"}}),(0,s.kt)("span",{parentName:"span"},(0,s.kt)("span",{parentName:"span",className:"mop"},"max")))),(0,s.kt)("span",{parentName:"span",className:"vlist-s"},"\u200b")),(0,s.kt)("span",{parentName:"span",className:"vlist-r"},(0,s.kt)("span",{parentName:"span",className:"vlist",style:{height:"0.7521em"}},(0,s.kt)("span",{parentName:"span"}))))),(0,s.kt)("span",{parentName:"span",className:"mspace",style:{marginRight:"0.1667em"}}),(0,s.kt)("span",{parentName:"span",className:"mord"},(0,s.kt)("span",{parentName:"span",className:"mord"},"\u2223"),(0,s.kt)("span",{parentName:"span",className:"mord"},(0,s.kt)("span",{parentName:"span",className:"mord mathnormal"},"x"),(0,s.kt)("span",{parentName:"span",className:"msupsub"},(0,s.kt)("span",{parentName:"span",className:"vlist-t vlist-t2"},(0,s.kt)("span",{parentName:"span",className:"vlist-r"},(0,s.kt)("span",{parentName:"span",className:"vlist",style:{height:"0.3361em"}},(0,s.kt)("span",{parentName:"span",style:{top:"-2.55em",marginLeft:"0em",marginRight:"0.05em"}},(0,s.kt)("span",{parentName:"span",className:"pstrut",style:{height:"2.7em"}}),(0,s.kt)("span",{parentName:"span",className:"sizing reset-size6 size3 mtight"},(0,s.kt)("span",{parentName:"span",className:"mord mathnormal mtight",style:{marginRight:"0.03148em"}},"k")))),(0,s.kt)("span",{parentName:"span",className:"vlist-s"},"\u200b")),(0,s.kt)("span",{parentName:"span",className:"vlist-r"},(0,s.kt)("span",{parentName:"span",className:"vlist",style:{height:"0.15em"}},(0,s.kt)("span",{parentName:"span"})))))),(0,s.kt)("span",{parentName:"span",className:"mord"},"\u2223"))))))))),(0,s.kt)("h2",{id:"setting-limits"},"Setting Limits"),(0,s.kt)("p",null,"Limits may be set as:"),(0,s.kt)("ul",null,(0,s.kt)("li",{parentName:"ul"},"if ",(0,s.kt)("inlineCode",{parentName:"li"},"limits")," are set as a one value, for example ",(0,s.kt)("inlineCode",{parentName:"li"},"limits")," = 1, then it will be considered as a limit for all columns;"),(0,s.kt)("li",{parentName:"ul"},(0,s.kt)("inlineCode",{parentName:"li"},"limits")," may be set separately for each column, as in the example above: ",(0,s.kt)("inlineCode",{parentName:"li"},"limits")," = ","[0.3, 0.35, 450]"," means that for the first column limit on the norm is 0.3, for the second one is 0.35 and for the last column 450. That way length of the ",(0,s.kt)("inlineCode",{parentName:"li"},"limits")," must be equal to the number of columns.")),(0,s.kt)("h2",{id:"returning-parameters"},"Returning Parameters"),(0,s.kt)("p",null,"The method returns three parameters: "),(0,s.kt)("ul",null,(0,s.kt)("li",{parentName:"ul"},(0,s.kt)("inlineCode",{parentName:"li"},"log")," : ",(0,s.kt)("a",{parentName:"li",href:"/docs/data_analysis/documentation/access/citros_dict#access.citros_dict.CitrosDict"},(0,s.kt)("strong",{parentName:"a"},"CitrosDict"))," - dictionary with test result summary;")),(0,s.kt)("mermaid",{value:'flowchart TD\n  log_norm((log_norm)) --- init4("\'test_param\'") --\x3e |initial \\ntest parameters| init4_("{\'limits\': list}")\n  \n  log_norm--- col4("column label,\n    str") --\x3e|whether the test\\n passed or failed| B4("{\'passed\': bool}")\n\n  col4 --\x3e |fraction\\n of the simulations\\n that pass the test| C4("`{\'pass_rate\': float}")\n\n  col4 --- E4(\'norm_value\') --\x3e |"norm for each\\n of the simulation\\n{sid: value}"| E4a("{int: float}")\n\n  col4 --\x3e|"sid that\\nfail the test\\n"| D4("`{\'failed\':list}")'}),(0,s.kt)("ul",null,(0,s.kt)("li",{parentName:"ul"},(0,s.kt)("p",{parentName:"li"},(0,s.kt)("inlineCode",{parentName:"p"},"table")," : ",(0,s.kt)("a",{parentName:"p",href:"https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html"},(0,s.kt)("strong",{parentName:"a"},"pandas.DataFrame"))," - table that specifies for each simulation whether the norm is less then the given limit (True) or not (False).")),(0,s.kt)("li",{parentName:"ul"},(0,s.kt)("p",{parentName:"li"},(0,s.kt)("inlineCode",{parentName:"p"},"fig")," : ",(0,s.kt)("a",{parentName:"p",href:"https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.Figure"},(0,s.kt)("strong",{parentName:"a"},"matplotlib.figure.Figure"))))),(0,s.kt)("p",null,"The output of the example above:"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> fig.show()\n")),(0,s.kt)("p",null,(0,s.kt)("img",{alt:"fig4",src:t(20770).Z,title:"Fig4",width:"725",height:"602"})),(0,s.kt)("p",null,"The norm, calculated for each simulation of the 'data.x.x_1' and 'data.x.x_2' columns are within the established limits, while norm for simulation 1 and 3 of the 'data.x.x_3' column exceed the limit."),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> print(table)\n")),(0,s.kt)("table",null,(0,s.kt)("thead",{parentName:"table"},(0,s.kt)("tr",{parentName:"thead"},(0,s.kt)("th",{parentName:"tr",align:null}),(0,s.kt)("th",{parentName:"tr",align:null},"data.x.x_1"),(0,s.kt)("th",{parentName:"tr",align:null},"data.x.x_2"),(0,s.kt)("th",{parentName:"tr",align:null},"data.x.x_3"))),(0,s.kt)("tbody",{parentName:"table"},(0,s.kt)("tr",{parentName:"tbody"},(0,s.kt)("td",{parentName:"tr",align:null},"sid"),(0,s.kt)("td",{parentName:"tr",align:null}),(0,s.kt)("td",{parentName:"tr",align:null}),(0,s.kt)("td",{parentName:"tr",align:null})),(0,s.kt)("tr",{parentName:"tbody"},(0,s.kt)("td",{parentName:"tr",align:null},"1"),(0,s.kt)("td",{parentName:"tr",align:null},"True"),(0,s.kt)("td",{parentName:"tr",align:null},"True"),(0,s.kt)("td",{parentName:"tr",align:null},"False")),(0,s.kt)("tr",{parentName:"tbody"},(0,s.kt)("td",{parentName:"tr",align:null},"2"),(0,s.kt)("td",{parentName:"tr",align:null},"True"),(0,s.kt)("td",{parentName:"tr",align:null},"True"),(0,s.kt)("td",{parentName:"tr",align:null},"True")),(0,s.kt)("tr",{parentName:"tbody"},(0,s.kt)("td",{parentName:"tr",align:null},"3"),(0,s.kt)("td",{parentName:"tr",align:null},"True"),(0,s.kt)("td",{parentName:"tr",align:null},"True"),(0,s.kt)("td",{parentName:"tr",align:null},"False")))),(0,s.kt)("p",null,(0,s.kt)("inlineCode",{parentName:"p"},"log")," can be accessed like a regular python dictionary and can be printed using the ",(0,s.kt)("a",{parentName:"p",href:"/docs/data_analysis/documentation/access/citros_dict#access.citros_dict.CitrosDict.print"},(0,s.kt)("strong",{parentName:"a"},"print()"))," method to display it as a JSON object:"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> log.print()\n")),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-js"},"{\n 'test_param': {\n   'limits': [0.3, 0.35, 450]\n },\n 'data.x.x_1': {\n   'passed': True,\n   'pass_rate': 1.0,\n   'norm_value': {\n     1: 0.253,\n     2: 0.246,\n     3: 0.249\n   },\n   'failed': []\n },\n 'data.x.x_2': {\n   'passed': True,\n   'pass_rate': 1.0,\n   'norm_value': {\n     1: 0.252,\n     2: 0.259,\n     3: 0.256\n   },\n   'failed': []\n },\n 'data.x.x_3': {\n   'passed': False,\n   'pass_rate': 0.333,\n   'norm_value': {\n     1: 571.5,\n     2: 431.8,\n     3: 495.0\n   },\n   'failed': [1, 3]\n }\n}\n")),(0,s.kt)("p",null,(0,s.kt)("inlineCode",{parentName:"p"},"log")," contains summary of the test result: "),(0,s.kt)("ul",null,(0,s.kt)("li",{parentName:"ul"},(0,s.kt)("p",{parentName:"li"},"initial test parameters:"),(0,s.kt)("pre",{parentName:"li"},(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> log['test_param'].print()\n")),(0,s.kt)("pre",{parentName:"li"},(0,s.kt)("code",{parentName:"pre",className:"language-js"},"{\n 'limits': [0.3, 0.35, 450]\n}\n"))),(0,s.kt)("li",{parentName:"ul"},(0,s.kt)("p",{parentName:"li"},"Information about the test results of each column, let's take a look at the 'data.x.x_1':"),(0,s.kt)("ul",{parentName:"li"},(0,s.kt)("li",{parentName:"ul"},(0,s.kt)("p",{parentName:"li"},"'passed' - whether the test for the column was passed (True) or not (False):"),(0,s.kt)("pre",{parentName:"li"},(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> print(log['data.x.x_1']['passed'])\n")),(0,s.kt)("pre",{parentName:"li"},(0,s.kt)("code",{parentName:"pre",className:"language-js"},"True\n"))),(0,s.kt)("li",{parentName:"ul"},(0,s.kt)("p",{parentName:"li"},"'pass_rate' - fraction of the points that pass the test, 0 < 'pass_rate' < 1:"),(0,s.kt)("pre",{parentName:"li"},(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> print(log['data.x.x_1']['pass_rate'])\n")),(0,s.kt)("pre",{parentName:"li"},(0,s.kt)("code",{parentName:"pre",className:"language-js"},"1.0\n"))),(0,s.kt)("li",{parentName:"ul"},(0,s.kt)("p",{parentName:"li"},"'norm_value' - the calculated for each simulation norm:"),(0,s.kt)("pre",{parentName:"li"},(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> log['data.x.x_1']['norm_value'].print()\n")),(0,s.kt)("pre",{parentName:"li"},(0,s.kt)("code",{parentName:"pre",className:"language-js"},"{\n 1: 0.253,\n 2: 0.246,\n 3: 0.249\n}\n"))),(0,s.kt)("li",{parentName:"ul"},(0,s.kt)("p",{parentName:"li"},"'failed' - list with sids that do not pass the test. Since column 'data.x.x_1' passed the test, log","['data.x.x_1']['failed']"," is an empty list:"),(0,s.kt)("pre",{parentName:"li"},(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> print(log['data.x.x_1']['failed'])\n")),(0,s.kt)("pre",{parentName:"li"},(0,s.kt)("code",{parentName:"pre",className:"language-js"},"[]\n")),(0,s.kt)("p",{parentName:"li"},"whereas in case of simulations 1 and 3 norm of the column 'data.x.x_3' exceed the give limit:"),(0,s.kt)("pre",{parentName:"li"},(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> print(log['data.x.x_3']['failed'])\n")),(0,s.kt)("pre",{parentName:"li"},(0,s.kt)("code",{parentName:"pre",className:"language-js"},"[1, 3]\n")))))))}c.isMDXComponent=!0},20770:(a,e,t)=>{t.d(e,{Z:()=>n});const n=t.p+"assets/images/fig24-a82f3acb90879ba5cd4340e067d47183.png"}}]);
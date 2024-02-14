"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[78777],{3905:(e,t,a)=>{a.d(t,{Zo:()=>d,kt:()=>g});var r=a(67294);function n(e,t,a){return t in e?Object.defineProperty(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}function s(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,r)}return a}function i(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?s(Object(a),!0).forEach((function(t){n(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):s(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}function l(e,t){if(null==e)return{};var a,r,n=function(e,t){if(null==e)return{};var a,r,n={},s=Object.keys(e);for(r=0;r<s.length;r++)a=s[r],t.indexOf(a)>=0||(n[a]=e[a]);return n}(e,t);if(Object.getOwnPropertySymbols){var s=Object.getOwnPropertySymbols(e);for(r=0;r<s.length;r++)a=s[r],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(n[a]=e[a])}return n}var o=r.createContext({}),p=function(e){var t=r.useContext(o),a=t;return e&&(a="function"==typeof e?e(t):i(i({},t),e)),a},d=function(e){var t=p(e.components);return r.createElement(o.Provider,{value:t},e.children)},m="mdxType",u={inlineCode:"code",wrapper:function(e){var t=e.children;return r.createElement(r.Fragment,{},t)}},c=r.forwardRef((function(e,t){var a=e.components,n=e.mdxType,s=e.originalType,o=e.parentName,d=l(e,["components","mdxType","originalType","parentName"]),m=p(a),c=n,g=m["".concat(o,".").concat(c)]||m[c]||u[c]||s;return a?r.createElement(g,i(i({ref:t},d),{},{components:a})):r.createElement(g,i({ref:t},d))}));function g(e,t){var a=arguments,n=t&&t.mdxType;if("string"==typeof e||n){var s=a.length,i=new Array(s);i[0]=c;var l={};for(var o in t)hasOwnProperty.call(t,o)&&(l[o]=t[o]);l.originalType=e,l[m]="string"==typeof e?e:n,i[1]=l;for(var p=2;p<s;p++)i[p]=a[p];return r.createElement.apply(null,i)}return r.createElement.apply(null,a)}c.displayName="MDXCreateElement"},9678:(e,t,a)=>{a.r(t),a.d(t,{assets:()=>o,contentTitle:()=>i,default:()=>u,frontMatter:()=>s,metadata:()=>l,toc:()=>p});var r=a(87462),n=(a(67294),a(3905));const s={toc_max_heading_level:4,hide_title:!0,sidebar_position:4,sidebar_label:"Regression",description:"Regression"},i="Regression",l={unversionedId:"data_analysis/error_analysis/regression",id:"version-0.2.53/data_analysis/error_analysis/regression",title:"Regression",description:"Regression",source:"@site/versioned_docs/version-0.2.53/data_analysis/error_analysis/regression.md",sourceDirName:"data_analysis/error_analysis",slug:"/data_analysis/error_analysis/regression",permalink:"/docs/data_analysis/error_analysis/regression",draft:!1,tags:[],version:"0.2.53",sidebarPosition:4,frontMatter:{toc_max_heading_level:4,hide_title:!0,sidebar_position:4,sidebar_label:"Regression",description:"Regression"},sidebar:"gettingStartedSidebar",previous:{title:"Correlation",permalink:"/docs/data_analysis/error_analysis/correlation"},next:{title:"Class CitrosData",permalink:"/docs/data_analysis/documentation/analysis/citros_data"}},o={},p=[{value:"Polynomial Regression",id:"polynomial-regression",level:2},{value:"Neural Net",id:"neural-net",level:2},{value:"Gaussian Mixture Model",id:"gaussian-mixture-model",level:2},{value:"Regression Comparison",id:"regression-comparison",level:2}],d={toc:p},m="wrapper";function u(e){let{components:t,...s}=e;return(0,n.kt)(m,(0,r.Z)({},d,s,{components:t,mdxType:"MDXLayout"}),(0,n.kt)("h1",{id:"regression"},"Regression"),(0,n.kt)("p",null,"Different input parameters may vary the output, and to predict how the parameter affects the result, regressions are used. By now, three methods of regression are supported: polynomial regression ('poly'), simple neural net regression ('neural_net') and gaussian mixture model ('gmm'). To apply regression analysis, we need to construct ",(0,n.kt)("a",{parentName:"p",href:"/docs/data_analysis/documentation/analysis/citros_data_array#analysis.citros_data_array.CitrosDataArray"},(0,n.kt)("strong",{parentName:"a"},"CitrosDataArray"))," object, that stores ",(0,n.kt)("a",{parentName:"p",href:"/docs/data_analysis/error_analysis/statistics#citrosdata-object"},(0,n.kt)("strong",{parentName:"a"},"CitrosData"))," objects with different input parameters."),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-python"},">>> from citros import CitrosDataArray\n>>> db_array = CitrosDataArray()\n")),(0,n.kt)("p",null,"Let's say for the topic 'A' from the batch 'pressure' created by simulation named 'simulation_environment' we have data for four different values of the parameter 't', that is written in json-data column 'data.t'. First, let's get all possible 'data.t' values for topic 'A' (see ",(0,n.kt)("a",{parentName:"p",href:"/docs/data_analysis/data_access/query_data"},"examples"),"):"),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-python"},">>> from citros import CitrosDB\n\n>>> citros = CitrosDB()\n>>> list_t = citros.simulation('simulation_environment').batch('pressure').topic('A').get_unique_values('data.t')\n>>> print(list_t)\n")),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-text"},"[-1.5, 0, 2.5, 4]\n")),(0,n.kt)("p",null,"Now let's query data for each of these parameter values, set it as parameter, scale data over 'data.time' and put to ",(0,n.kt)("a",{parentName:"p",href:"/docs/data_analysis/documentation/analysis/citros_data_array#analysis.citros_data_array.CitrosDataArray"},(0,n.kt)("strong",{parentName:"a"},"CitrosDataArray")),":"),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-python"},">>> from citros import CitrosData\n\nfor t in list_t:\n    #query data\n    df = citros.topic('A').\\\n                set_filter({'data.t': [t]}).\\\n                data(['data.x.x_1', 'data.time', 'data.p', 'data.t'])\n    \n    #create CitrosData object and set 'data.t' as a parameter.\n    dataset = CitrosData(df,  \n                         data_label=['data.x.x_1'],\n                         units = 'm', \n                         parameter_label = ['data.t'])\n\n    #scale over 'data.time'\n    db_sc = dataset.scale_data(n_points = 100, \n                               param_label = 'data.time')\n\n    #store in CitrosDataArray by add_db() method\n    db_array.add_db(db_sc)\n")),(0,n.kt)("p",null,"To set value from 'data.t' column as a parameter, pass the column label to ",(0,n.kt)("inlineCode",{parentName:"p"},"parameter_label")," argument of ",(0,n.kt)("a",{parentName:"p",href:"/docs/data_analysis/error_analysis/statistics#citrosdata-object"},(0,n.kt)("strong",{parentName:"a"},"CitrosData"))," object. "),(0,n.kt)("p",null,"If a column with parameters is not presented, it is possible to put ",(0,n.kt)("inlineCode",{parentName:"p"},"dict")," with parameters by ",(0,n.kt)("inlineCode",{parentName:"p"},"parameters")," argument:"),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-python"},">>> dataset = CitrosData(df,  \n                         data_label=['data.x.x_1'],\n                         units = 'm', \n                         parameters = {'data.t': t})\n")),(0,n.kt)("p",null,"or set parameters manually by ",(0,n.kt)("a",{parentName:"p",href:"/docs/data_analysis/documentation/analysis/citros_data#analysis.citros_data.CitrosData.set_parameter"},(0,n.kt)("inlineCode",{parentName:"a"},"set_parameter("))," method. It accepts either setting parameter one by one by ",(0,n.kt)("inlineCode",{parentName:"p"},"key")," and ",(0,n.kt)("inlineCode",{parentName:"p"},"value"),":"),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-python"},">>> db_sc.set_parameter(key = 'data.t', value = 0)\n")),(0,n.kt)("p",null,"or by passing dictionary by ",(0,n.kt)("inlineCode",{parentName:"p"},"item"),":"),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-python"},">>> db_sc.set_parameter(item={'data.t': 0})\n")),(0,n.kt)("p",null,"The last method allows you to pass multiple parameters, for example:"),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-python"},">>> db_sc.set_parameter(item={'param_1':0, 'param_2':1, 'param_3':2})\n")),(0,n.kt)("p",null,"Let's take a look at the scaled to ","[0,1]"," interval data:"),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-python"},"import matplotlib.pyplot as plt\n\nfor db in db_array.dbs:\n    plt.plot(db.addData['data.time'], db.data['data.x.x_1'], \n             '.', label = 'data.t = ' + str(db.parameters['data.t']))\nplt.xlabel('data.time')\nplt.ylabel('data.x.x_1')\nplt.legend(bbox_to_anchor=(1.0, 1.0))\n")),(0,n.kt)("p",null,"It is a sine function with some noise added, biased by 'data.t' value."),(0,n.kt)("details",null,(0,n.kt)("summary",null,"Show the figure:"),(0,n.kt)("p",null,(0,n.kt)("img",{alt:"fig11",src:a(91115).Z,title:"Fig11",width:"711",height:"432"}))),(0,n.kt)("p",null,"Let's find the solution for the case 'data.t' = 1 by ",(0,n.kt)("a",{parentName:"p",href:"/docs/data_analysis/documentation/analysis/citros_data_array#analysis.citros_data_array.CitrosDataArray.get_prediction"},(0,n.kt)("strong",{parentName:"a"},"get_prediction()"))," method. Parameter label (in our case 'data.t') and value (1), for which the prediction is desired, should be passed as ",(0,n.kt)("inlineCode",{parentName:"p"},"dict")," by ",(0,n.kt)("inlineCode",{parentName:"p"},"parameters")," argument. Method of regression calculation ('poly' for polynomial regression, simple  'neural_net' for neural net regression and 'gmm' for gaussian mixture model) should be stated by ",(0,n.kt)("inlineCode",{parentName:"p"},"method")," argument."),(0,n.kt)("h2",{id:"polynomial-regression"},"Polynomial Regression"),(0,n.kt)("p",null,"The first method is a polynomial regression, with the highest polynomial order defined by ",(0,n.kt)("inlineCode",{parentName:"p"},"n_poly"),":"),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-python"},">>> result = db_array.get_prediction(parameters = {'data.t': 1},\n                                     method = 'poly', \n                                     n_poly = 2)\n")),(0,n.kt)("details",null,(0,n.kt)("summary",null,"Show the figure:"),(0,n.kt)("p",null,(0,n.kt)("img",{alt:"fig12",src:a(110).Z,title:"Fig12",width:"753",height:"599"}))),(0,n.kt)("p",null,"The result is a ",(0,n.kt)("a",{parentName:"p",href:"https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html"},(0,n.kt)("strong",{parentName:"a"},"DataFrame")),"."),(0,n.kt)("details",null,(0,n.kt)("summary",null,"Show the result:"),(0,n.kt)("table",null,(0,n.kt)("thead",{parentName:"table"},(0,n.kt)("tr",{parentName:"thead"},(0,n.kt)("th",{parentName:"tr",align:null}),(0,n.kt)("th",{parentName:"tr",align:null},"data.time"),(0,n.kt)("th",{parentName:"tr",align:null},"data.x.x_1"))),(0,n.kt)("tbody",{parentName:"table"},(0,n.kt)("tr",{parentName:"tbody"},(0,n.kt)("td",{parentName:"tr",align:null},"0"),(0,n.kt)("td",{parentName:"tr",align:null},"0.000000"),(0,n.kt)("td",{parentName:"tr",align:null},"1.155301")),(0,n.kt)("tr",{parentName:"tbody"},(0,n.kt)("td",{parentName:"tr",align:null},"1"),(0,n.kt)("td",{parentName:"tr",align:null},"0.010101"),(0,n.kt)("td",{parentName:"tr",align:null},"1.145971")),(0,n.kt)("tr",{parentName:"tbody"},(0,n.kt)("td",{parentName:"tr",align:null},"2"),(0,n.kt)("td",{parentName:"tr",align:null},"0.020202"),(0,n.kt)("td",{parentName:"tr",align:null},"1.232255")),(0,n.kt)("tr",{parentName:"tbody"},(0,n.kt)("td",{parentName:"tr",align:null},"..."),(0,n.kt)("td",{parentName:"tr",align:null},"..."),(0,n.kt)("td",{parentName:"tr",align:null},"..."))))),(0,n.kt)("h2",{id:"neural-net"},"Neural Net"),(0,n.kt)("p",null,"The second method is 'neural_net', which is based on the ",(0,n.kt)("a",{parentName:"p",href:"https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html"},(0,n.kt)("inlineCode",{parentName:"a"},"sklearn.neural_network.MLPRegressor"))," class. Its the most important arguments are ",(0,n.kt)("inlineCode",{parentName:"p"},"activation"),", that defines activation function for the hidden layers ('relu', 'identity', 'logistic' or 'tanh'), ",(0,n.kt)("inlineCode",{parentName:"p"},"max_iter")," - maximum number of iteration, ",(0,n.kt)("inlineCode",{parentName:"p"},"solver")," - solver for weight optimization ('lbfgs', 'sgd' or 'adam'), ",(0,n.kt)("inlineCode",{parentName:"p"},"hidden_layer_sizes")," - the number of neurons in the ith hidden layer, see ",(0,n.kt)("a",{parentName:"p",href:"https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html"},(0,n.kt)("inlineCode",{parentName:"a"},"sklearn.neural_network.MLPRegressor"))," for the details of the other possible arguments."),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-python"},">>> result = db_array.get_prediction(parameters = {'data.t':1}, \n                                     method = 'neural_net',\n                                     activation='tanh', max_iter = 200, solver='lbfgs',\n                                     hidden_layer_sizes = (8,), random_state = 9)\n")),(0,n.kt)("details",null,(0,n.kt)("summary",null,"Show the figure:"),(0,n.kt)("p",null,(0,n.kt)("img",{alt:"fig13",src:a(22799).Z,title:"Fig13",width:"753",height:"599"}))),(0,n.kt)("h2",{id:"gaussian-mixture-model"},"Gaussian Mixture Model"),(0,n.kt)("p",null,"The last method is a gaussian mixture model:"),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-python"},">>> result = db_array.get_prediction(parameters = {'data.t':1}, \n                                     method = 'gmm')\n")),(0,n.kt)("details",null,(0,n.kt)("summary",null,"Show the result:"),(0,n.kt)("p",null,(0,n.kt)("img",{alt:"fig14",src:a(91795).Z,title:"Fig14",width:"753",height:"599"}))),(0,n.kt)("h2",{id:"regression-comparison"},"Regression Comparison"),(0,n.kt)("p",null,"To compare the results of these methods, list their names as ",(0,n.kt)("inlineCode",{parentName:"p"},"method"),":"),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-python"},">>> result_list = db_array.get_prediction(parameters = {'data.t':1}, \n                                          method = ['neural_net', 'poly', 'gmm'],\n                                          n_poly = 2, \n                                          activation='tanh', solver='lbfgs', hidden_layer_sizes = (8,), random_state = 9)\n")),(0,n.kt)("details",null,(0,n.kt)("summary",null,"The resulting plot:"),(0,n.kt)("p",null,(0,n.kt)("img",{alt:"fig15",src:a(67629).Z,title:"Fig15",width:"753",height:"599"}))),(0,n.kt)("p",null,"That way, the returning result is a list of the ",(0,n.kt)("a",{parentName:"p",href:"https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html"},(0,n.kt)("strong",{parentName:"a"},"DataFrames")),"."))}u.isMDXComponent=!0},91115:(e,t,a)=>{a.d(t,{Z:()=>r});const r=a.p+"assets/images/fig11-86b5bd6958b3702789d435021bd2e001.png"},110:(e,t,a)=>{a.d(t,{Z:()=>r});const r=a.p+"assets/images/fig12-b19d9a30eed22e7e616dd97358ec5440.png"},22799:(e,t,a)=>{a.d(t,{Z:()=>r});const r=a.p+"assets/images/fig13-ea5bd6e2788962ead2d4fd3f9d586222.png"},91795:(e,t,a)=>{a.d(t,{Z:()=>r});const r=a.p+"assets/images/fig14-9b913eab1e720f32664948ba30124d97.png"},67629:(e,t,a)=>{a.d(t,{Z:()=>r});const r=a.p+"assets/images/fig15-c3b7fb32e8cc55015e8e13281fe32267.png"}}]);
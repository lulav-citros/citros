"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[53554],{3905:(e,t,n)=>{n.d(t,{Zo:()=>m,kt:()=>b});var a=n(67294);function i(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function s(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);t&&(a=a.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,a)}return n}function o(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?s(Object(n),!0).forEach((function(t){i(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):s(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function l(e,t){if(null==e)return{};var n,a,i=function(e,t){if(null==e)return{};var n,a,i={},s=Object.keys(e);for(a=0;a<s.length;a++)n=s[a],t.indexOf(n)>=0||(i[n]=e[n]);return i}(e,t);if(Object.getOwnPropertySymbols){var s=Object.getOwnPropertySymbols(e);for(a=0;a<s.length;a++)n=s[a],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(i[n]=e[n])}return i}var d=a.createContext({}),r=function(e){var t=a.useContext(d),n=t;return e&&(n="function"==typeof e?e(t):o(o({},t),e)),n},m=function(e){var t=r(e.components);return a.createElement(d.Provider,{value:t},e.children)},c="mdxType",p={inlineCode:"code",wrapper:function(e){var t=e.children;return a.createElement(a.Fragment,{},t)}},h=a.forwardRef((function(e,t){var n=e.components,i=e.mdxType,s=e.originalType,d=e.parentName,m=l(e,["components","mdxType","originalType","parentName"]),c=r(n),h=i,b=c["".concat(d,".").concat(h)]||c[h]||p[h]||s;return n?a.createElement(b,o(o({ref:t},m),{},{components:n})):a.createElement(b,o({ref:t},m))}));function b(e,t){var n=arguments,i=t&&t.mdxType;if("string"==typeof e||i){var s=n.length,o=new Array(s);o[0]=h;var l={};for(var d in t)hasOwnProperty.call(t,d)&&(l[d]=t[d]);l.originalType=e,l[c]="string"==typeof e?e:i,o[1]=l;for(var r=2;r<s;r++)o[r]=n[r];return a.createElement.apply(null,o)}return a.createElement.apply(null,n)}h.displayName="MDXCreateElement"},58867:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>d,contentTitle:()=>o,default:()=>p,frontMatter:()=>s,metadata:()=>l,toc:()=>r});var a=n(87462),i=(n(67294),n(3905));const s={toc_max_heading_level:4,hide_title:!0,sidebar_label:"Validation"},o="Validation",l={unversionedId:"data_analysis/snippets_doc/snippets_validation",id:"version-0.2.40/data_analysis/snippets_doc/snippets_validation",title:"Validation",description:"Overview",source:"@site/versioned_docs/version-0.2.40/data_analysis/snippets_doc/snippets_validation.md",sourceDirName:"data_analysis/snippets_doc",slug:"/data_analysis/snippets_doc/snippets_validation",permalink:"/docs/0.2.40/data_analysis/snippets_doc/snippets_validation",draft:!1,tags:[],version:"0.2.40",frontMatter:{toc_max_heading_level:4,hide_title:!0,sidebar_label:"Validation"},sidebar:"gettingStartedSidebar",previous:{title:"Error Analysis",permalink:"/docs/0.2.40/data_analysis/snippets_doc/snippets_error_analysis"},next:{title:"Overview",permalink:"/docs/0.2.40/data_analysis/data_access/"}},d={},r=[{value:"Overview",id:"overview",level:2},{value:"Checking the Standard Deviation Boundary",id:"checking-the-standard-deviation-boundary",level:2},{value:"Checking the Mean Value",id:"checking-the-mean-value",level:2},{value:"Checking the Standard Deviation Values",id:"checking-the-standard-deviation-values",level:2},{value:"Checking the Individual Simulations",id:"checking-the-individual-simulations",level:2},{value:"Norm Limit Test",id:"norm-limit-test",level:2},{value:"Set Multiple Tests",id:"set-multiple-tests",level:2}],m={toc:r},c="wrapper";function p(e){let{components:t,...n}=e;return(0,i.kt)(c,(0,a.Z)({},m,n,{components:t,mdxType:"MDXLayout"}),(0,i.kt)("h1",{id:"validation"},"Validation"),(0,i.kt)("h2",{id:"overview"},"Overview"),(0,i.kt)("p",null,"Let's consider a table for topic 'my_topic' from the batch 'my_batch', created by simulation 'my_simulation', where each row under the 'data' column contains dictionaries with keys 'x', 'y', and 'z', as illustrated:"),(0,i.kt)("table",null,(0,i.kt)("thead",{parentName:"table"},(0,i.kt)("tr",{parentName:"thead"},(0,i.kt)("th",{parentName:"tr",align:null},"data"))),(0,i.kt)("tbody",{parentName:"table"},(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"{x: 1, y: 2, z: 3}")),(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"{x: 4, y: 5, z: 6}")),(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"...")))),(0,i.kt)("p",null,"Let's assume that there are number of simulations (sids) and we would like to perform several test on this data to evaluate the quality of the simulation results."),(0,i.kt)("p",null,"The pipeline is the following: query data, define the independent variable (that is used to establish the correspondence between different simulations), set test parameters."),(0,i.kt)("h2",{id:"checking-the-standard-deviation-boundary"},"Checking the Standard Deviation Boundary"),(0,i.kt)("p",null,"Whether the standard deviation boundary is within the limits."),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},"# --- adjust to your data --- #\n\n# Set simulation, batch and topic names:\nsimulation_name = 'my_simulation'\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\n\n# Data labels\ndata_labels = ['data.x', 'data.y', 'data.z']\n\n# Set time step to construct independent variable column as: Time = rid*time_step.\ntime_step  = 0.2\n\n# 'method' defines how the index assignment will be done:\n#    - 'scale': by scaling independent variable to unit interval and interpolating data on this interval,\n#    - 'bin': by dividing independent variable on bins and calculating mean data values among points fallen in each bin\nmethod = 'bin'\n\n# limits: a one value to set the same +-limits to each element of the vector, for examples limits = 0.25\n#        list of values to set +-limits for each vector element, for examples limits = [0.25, 0.5, 100]\n#        list of lists to set lower and upper intervals separately, for examples limits = [0.25, [-0.3, 0.8], [-150, 100]]\nlimits = [0.25, [-0.3, 0.8], [-150, 100]]\n\n# number of standard deviations in standard deviation boundary\nn_std = 3\n\n# whether nan values are treated as passed test or not\nnan_passed = True\n\n# to style the output plot:\n# std_area - set True to fill with color standard deviation boundary\nstd_area = False\n# std_lines - set False to remove standard deviation boundary lines\nstd_lines = True\n# std_color - set standard deviation boundary color, default 'b'\nstd_color = 'b'\n# --------------------------- #\n\nfrom citros import CitrosDB, Validation\n\ncitros = CitrosDB()\n\n# query data.\ndf = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).data(data_labels)\n# construct independent variable column as: Time = rid*time_step\ndf['Time'] = df['rid']*time_step\n\n# construct Validation object. It determines how the data will be preprocessed: \n#'data_label' determine data columns, \n#'param_label' is for independent variable that will be used for defining indexes and setting correspondence between different sids \n#'method' defines how the index assignment will be done:\n#    - 'scale': by scaling independent variable to unit interval and interpolating data on this interval,\n#    - 'bin': by dividing independent variable on bins and calculating mean data values among points fallen in each bin\n#'num' determines number of points if method set as 'scale' or bins if 'method' set as 'bin':\nV = Validation(df, data_label = data_labels, param_label = 'Time', \n                  method = method, num = 50, units = 'm')\n\n# Set test\nlog, table, fig = V.std_bound_test(limits = limits, n_std = n_std, nan_passed = nan_passed, \n            std_area = std_area, std_lines = std_lines, std_color = std_color)\n\n# print the report of the test:\nlog.print()\n\n#DataFrame table that for each point indicates whether it passes the test or not:\nprint(table.head(5)) #method head(n) shows first n rows of the DataFrame table\n")),(0,i.kt)("h2",{id:"checking-the-mean-value"},"Checking the Mean Value"),(0,i.kt)("p",null,"Test whether the mean values are within the defined boundaries.\nEven when some points of the individual simulations may exceed the limits, but the test will be passed for those, whose mean values are within limits."),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},"# --- adjust to your data --- #\n\n# Set simulation, batch and topic names:\nsimulation_name = 'my_simulation'\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\n\n# Data labels\ndata_labels = ['data.x', 'data.y', 'data.z']\n\n# Set time step to construct independent variable column as: Time = rid*time_step.\ntime_step  = 0.2\n\n# 'method' defines how the index assignment will be done:\n#    - 'scale': by scaling independent variable to unit interval and interpolating data on this interval,\n#    - 'bin': by dividing independent variable on bins and calculating mean data values among points fallen in each bin\nmethod = 'bin'\n\n# limits: a one value to set the same +-limits to each element of the vector, for examples limits = 0.25\n#        list of values to set +-limits for each vector element, for examples limits = [0.25, 0.5, 100]\n#        list of lists to set lower and upper intervals separately, for examples limits = [0.25, [-0.3, 0.8], [-150, 100]]\nlimits = [0.05, 0.05, [-1, 3]]\n\n# whether nan values are treated as passed test or not\nnan_passed = True\n# --------------------------- #\n\nfrom citros import CitrosDB, Validation\n\ncitros = CitrosDB()\n\n# query data.\ndf = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).data(data_labels)\n# construct independent variable column as: Time = rid*time_step\ndf['Time'] = df['rid']*time_step\n\n# construct Validation object. It determines how the data will be preprocessed: \n#'data_label' determine data columns, \n#'param_label' is for independent variable that will be used for defining indexes and setting correspondence between different sids \n#'method' defines how the index assignment will be done:\n#    - 'scale': by scaling independent variable to unit interval and interpolating data on this interval,\n#    - 'bin': by dividing independent variable on bins and calculating mean data values among points fallen in each bin\n#'num' determines number of points if method set as 'scale' or bins if 'method' set as 'bin':\nV = Validation(df, data_label = data_labels, param_label = 'Time', \n                  method = method, num = 50, units = 'm')\n\n# Set test\nlog, table, fig = V.mean_test(limits = limits)\n\n# print the report of the test:\nlog.print()\n\n#DataFrame table that for each point indicates whether it passes the test or not:\nprint(table.head(5)) #method head(n) shows first n rows of the DataFrame table\n")),(0,i.kt)("h2",{id:"checking-the-standard-deviation-values"},"Checking the Standard Deviation Values"),(0,i.kt)("p",null,"Whether the standard deviation values do not exceed the limits."),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},"# --- adjust to your data --- #\n\n# Set simulation, batch and topic names:\nsimulation_name = 'my_simulation'\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\n\n# Data labels\ndata_labels = ['data.x', 'data.y', 'data.z']\n\n# Set time step to construct independent variable column as: Time = rid*time_step.\ntime_step  = 0.2\n\n# 'method' defines how the index assignment will be done:\n#    - 'scale': by scaling independent variable to unit interval and interpolating data on this interval,\n#    - 'bin': by dividing independent variable on bins and calculating mean data values among points fallen in each bin\nmethod = 'bin'\n\n# limits: a one value to set the same limit to each element of the vector, for examples limits = 0.25\n#        list of values to set the limits for each vector element, for examples limits = [0.25, 0.5, 100]\nlimits = [0.25, 0.5, 100]\n\n# number of standard deviations in standard deviation boundary\nn_std = 3\n\n# whether nan values are treated as passed test or not\nnan_passed = True\n\n# to style the output plot:\n# std_area - set True to fill with color standard deviation boundary\nstd_area = False\n# std_lines - set False to remove standard deviation lines\nstd_lines = True\n# std_color - set standard deviation color, default 'b'\nstd_color = 'b'\n# --------------------------- #\n\nfrom citros import CitrosDB, Validation\n\ncitros = CitrosDB()\n\n# query data.\ndf = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).data(data_labels)\n# construct independent variable column as: Time = rid*time_step\ndf['Time'] = df['rid']*time_step\n\n# construct Validation object. It determines how the data will be preprocessed: \n#'data_label' determine data columns, \n#'param_label' is for independent variable that will be used for defining indexes and setting correspondence between different sids \n#'method' defines how the index assignment will be done:\n#    - 'scale': by scaling independent variable to unit interval and interpolating data on this interval,\n#    - 'bin': by dividing independent variable on bins and calculating mean data values among points fallen in each bin\n#'num' determines number of points if method set as 'scale' or bins if 'method' set as 'bin':\nV = Validation(df, data_label = data_labels, param_label = 'Time', \n                  method = method, num = 50, units = 'm')\n\n# Set test\nlog, table, fig = V.std_test(limits = limits, n_std = n_std, nan_passed = nan_passed, \n            std_area = std_area, std_lines = std_lines, std_color = std_color)\n\n# print the report of the test:\nlog.print()\n\n#DataFrame table that for each point indicates whether it passes the test or not:\nprint(table.head(5)) #method head(n) shows first n rows of the DataFrame table\n")),(0,i.kt)("h2",{id:"checking-the-individual-simulations"},"Checking the Individual Simulations"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},"# --- adjust to your data --- #\n\n# Set simulation, batch and topic names:\nsimulation_name = 'my_simulation'\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\n\n# Data labels\ndata_labels = ['data.x', 'data.y', 'data.z']\n\n# Set time step to construct independent variable column as: Time = rid*time_step.\ntime_step  = 0.2\n\n# 'method' defines how the index assignment will be done:\n#    - 'scale': by scaling independent variable to unit interval and interpolating data on this interval,\n#    - 'bin': by dividing independent variable on bins and calculating mean data values among points fallen in each bin\nmethod = 'bin'\n\n# limits: a one value to set the same +-limits to each element of the vector, for examples limits = 0.25\n#        list of values to set +-limits for each vector element, for examples limits = [0.25, 0.5, 100]\n#        list of lists to set lower and upper intervals separately, for examples limits = [0.25, [-0.3, 0.8], [-150, 100]]\nlimits = [0.05, 0.15, [-1, 3]]\n\n# whether nan values are treated as passed test or not\nnan_passed = True\n# --------------------------- #\n\nfrom citros import CitrosDB, Validation\n\ncitros = CitrosDB()\n\n# query data.\ndf = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).data(data_labels)\n# construct independent variable column as: Time = rid*time_step\ndf['Time'] = df['rid']*time_step\n\n# construct Validation object. It determines how the data will be preprocessed: \n#'data_label' determine data columns, \n#'param_label' is for independent variable that will be used for defining indexes and setting correspondence between different sids \n#'method' defines how the index assignment will be done:\n#    - 'scale': by scaling independent variable to unit interval and interpolating data on this interval,\n#    - 'bin': by dividing independent variable on bins and calculating mean data values among points fallen in each bin\n#'num' determines number of points if method set as 'scale' or bins if 'method' set as 'bin':\nV = Validation(df, data_label = data_labels, param_label = 'Time', \n                  method = method, num = 50, units = 'm')\n\n# Set test\nlog, table, fig = V.sid_test(limits = limits)\n\n# print the report of the test:\nlog.print()\n\n#DataFrame table that for each point indicates whether it passes the test or not:\nprint(table.head(5)) #method head(n) shows first n rows of the DataFrame table\n")),(0,i.kt)("h2",{id:"norm-limit-test"},"Norm Limit Test"),(0,i.kt)("p",null,"Test whether the norm of each simulation do not exceed the given limit"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},"# --- adjust to your data --- #\n\n# Set simulation, batch and topic names:\nsimulation_name = 'my_simulation'\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\n\n# Data labels\ndata_labels = ['data.x', 'data.y', 'data.z']\n\n# Set time step to construct independent variable column as: Time = rid*time_step.\ntime_step  = 0.2\n\n# 'method' defines how the index assignment will be done:\n#    - 'scale': by scaling independent variable to unit interval and interpolating data on this interval,\n#    - 'bin': by dividing independent variable on bins and calculating mean data values among points fallen in each bin\nmethod = 'bin'\n\n# type of the norm:\n#     - 'Linf' - test whether absolute maximum of each simulation is less then the limits\n#     - 'L2' - test whether for each simulation the Euclidean norm (square root of the sum of the squares) \n#     does not exceed the given limit\nnorm_type = 'Linf'\n\n# limits: a one value to set the same +-limits to each element of the vector, for examples limits = 0.25\n#        list of values to set +-limits for each vector element, for examples limits = [0.25, 0.5, 100]\nlimits = [0.2, 0.2, 15]\n# --------------------------- #\n\nfrom citros import CitrosDB, Validation\n\ncitros = CitrosDB()\n\n# query data.\ndf = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).data(data_labels)\n# construct independent variable column as: Time = rid*time_step\ndf['Time'] = df['rid']*time_step\n\n# construct Validation object. It determines how the data will be preprocessed: \n#'data_label' determine data columns, \n#'param_label' is for independent variable that will be used for defining indexes and setting correspondence between different sids \n#'method' defines how the index assignment will be done:\n#    - 'scale': by scaling independent variable to unit interval and interpolating data on this interval,\n#    - 'bin': by dividing independent variable on bins and calculating mean data values among points fallen in each bin\n#'num' determines number of points if method set as 'scale' or bins if 'method' set as 'bin':\nV = Validation(df, data_label = data_labels, param_label = 'Time', \n                  method = method, num = 50, units = 'm')\n\n# Set test\nlog, table, fig = V.norm_test(norm_type = norm_type, limits = limits)\n\n# print the report of the test:\nlog.print()\n\n#DataFrame table that for each point indicates whether it passes the test or not:\nprint(table.head(5)) #method head(n) shows first n rows of the DataFrame table\n")),(0,i.kt)("h2",{id:"set-multiple-tests"},"Set Multiple Tests"),(0,i.kt)("p",null,"Set several tests at once."),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},"# --- adjust to your data --- #\n\n# Set simulation, batch and topic names:\nsimulation_name = 'my_simulation'\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\n\n# Data labels\ndata_labels = ['data.x', 'data.y', 'data.z']\n\n# Set time step to construct independent variable column as: Time = rid*time_step.\ntime_step  = 0.2\n\n# 'method' defines how the index assignment will be done:\n#    - 'scale': by scaling independent variable to unit interval and interpolating data on this interval,\n#    - 'bin': by dividing independent variable on bins and calculating mean data values among points fallen in each bin\nmethod = 'bin'\n\n# Define parameters of the tests as dictionaries with key being the test name ('std_bound', 'mean', 'sid', 'norm_L2', 'norm_Linf'):\ndefine_tests = {'std_bound' : {'limits' : [0.2, 0.2, [-2, 4]], 'n_std': 3},\n                'norm_Linf' : {'limits' : [0.1, 0.1, 2]}}\n# --------------------------- #\n\nfrom citros import CitrosDB, Validation\n\ncitros = CitrosDB()\n\n# query data.\ndf = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).data(data_labels)\n# construct independent variable column as: Time = rid*time_step\ndf['Time'] = df['rid']*time_step\n\n# construct Validation object. It determines how the data will be preprocessed: \n#'data_label' determine data columns, \n#'param_label' is for independent variable that will be used for defining indexes and setting correspondence between different sids \n#'method' defines how the index assignment will be done:\n#    - 'scale': by scaling independent variable to unit interval and interpolating data on this interval,\n#    - 'bin': by dividing independent variable on bins and calculating mean data values among points fallen in each bin\n#'num' determines number of points if method set as 'scale' or bins if 'method' set as 'bin':\nV = Validation(df, data_label = data_labels, param_label = 'Time', \n                  method = method, num = 50, units = 'm')\n\n# Set tests\nlogs, tables, figs = V.set_tests(test_method = define_tests)\n\n#logs, tables, figs are the dictionaries with the corresponding to each test log, table and fig, \n#where key of the dictionary is the name of the test:\nlogs['std_bound'].print()\nprint(tables['norm_Linf'])\n")))}p.isMDXComponent=!0}}]);
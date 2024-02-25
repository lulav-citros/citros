"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[70866],{3905:(e,t,a)=>{a.d(t,{Zo:()=>m,kt:()=>u});var n=a(67294);function i(e,t,a){return t in e?Object.defineProperty(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}function r(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,n)}return a}function s(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?r(Object(a),!0).forEach((function(t){i(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):r(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}function o(e,t){if(null==e)return{};var a,n,i=function(e,t){if(null==e)return{};var a,n,i={},r=Object.keys(e);for(n=0;n<r.length;n++)a=r[n],t.indexOf(a)>=0||(i[a]=e[a]);return i}(e,t);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);for(n=0;n<r.length;n++)a=r[n],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(i[a]=e[a])}return i}var d=n.createContext({}),l=function(e){var t=n.useContext(d),a=t;return e&&(a="function"==typeof e?e(t):s(s({},t),e)),a},m=function(e){var t=l(e.components);return n.createElement(d.Provider,{value:t},e.children)},c="mdxType",p={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},h=n.forwardRef((function(e,t){var a=e.components,i=e.mdxType,r=e.originalType,d=e.parentName,m=o(e,["components","mdxType","originalType","parentName"]),c=l(a),h=i,u=c["".concat(d,".").concat(h)]||c[h]||p[h]||r;return a?n.createElement(u,s(s({ref:t},m),{},{components:a})):n.createElement(u,s({ref:t},m))}));function u(e,t){var a=arguments,i=t&&t.mdxType;if("string"==typeof e||i){var r=a.length,s=new Array(r);s[0]=h;var o={};for(var d in t)hasOwnProperty.call(t,d)&&(o[d]=t[d]);o.originalType=e,o[c]="string"==typeof e?e:i,s[1]=o;for(var l=2;l<r;l++)s[l]=a[l];return n.createElement.apply(null,s)}return n.createElement.apply(null,a)}h.displayName="MDXCreateElement"},50794:(e,t,a)=>{a.r(t),a.d(t,{assets:()=>d,contentTitle:()=>s,default:()=>p,frontMatter:()=>r,metadata:()=>o,toc:()=>l});var n=a(87462),i=(a(67294),a(3905));const r={toc_max_heading_level:4,hide_title:!0,sidebar_label:"Error Analysis"},s="Error Analysis",o={unversionedId:"data_analysis/snippets_doc/snippets_error_analysis",id:"version-0.2.62/data_analysis/snippets_doc/snippets_error_analysis",title:"Error Analysis",description:"Get Statistics For Simulations",source:"@site/versioned_docs/version-0.2.62/data_analysis/snippets_doc/snippets_error_analysis.md",sourceDirName:"data_analysis/snippets_doc",slug:"/data_analysis/snippets_doc/snippets_error_analysis",permalink:"/docs/0.2.62/data_analysis/snippets_doc/snippets_error_analysis",draft:!1,tags:[],version:"0.2.62",frontMatter:{toc_max_heading_level:4,hide_title:!0,sidebar_label:"Error Analysis"},sidebar:"gettingStartedSidebar",previous:{title:"Plotting",permalink:"/docs/0.2.62/data_analysis/snippets_doc/data_access/snippets_plotting"},next:{title:"Validation",permalink:"/docs/0.2.62/data_analysis/snippets_doc/snippets_validation"}},d={},l=[{value:"Get Statistics For Simulations",id:"get-statistics-for-simulations",level:2},{value:"1-dimensional Vector",id:"1-dimensional-vector",level:3},{value:"N-dimensional Vector",id:"n-dimensional-vector",level:3},{value:"Correlation Between Variables",id:"correlation-between-variables",level:2},{value:"Predictions",id:"predictions",level:2}],m={toc:l},c="wrapper";function p(e){let{components:t,...a}=e;return(0,i.kt)(c,(0,n.Z)({},m,a,{components:t,mdxType:"MDXLayout"}),(0,i.kt)("h1",{id:"error-analysis"},"Error Analysis"),(0,i.kt)("h2",{id:"get-statistics-for-simulations"},"Get Statistics For Simulations"),(0,i.kt)("h3",{id:"1-dimensional-vector"},"1-dimensional Vector"),(0,i.kt)("p",null,"To analyze data of multiple simulations it is necessary to establish a correspondence between the values of the data from these different simulations. One approach is to select an independent variable, define a scale that is common to all simulations and assign indexes on this scale. Then, the values of variables from different simulations will be connected by this independent variable."),(0,i.kt)("p",null,"There are two ways to perform index assignment: divide the independent variable into N ranges, assign an index to each interval, and calculate the averages of the data values for each simulation in each range, or scale the independent variable to the interval ","[0,1]",", define a new range of N points uniformly distributed from 0 to 1, and interpolate data points over this new interval. The first approach corresponds to the bin_data() method, while the second is implemented by the scale_data() method."),(0,i.kt)("p",null,"Let's consider a table for topic 'my_topic' from the batch 'my_batch', created by simulation simulation 'my_simulation', where each row under the 'data' column holds a dictionary and within this dictionary, under the key 'data' is a list of values, as shown:"),(0,i.kt)("table",null,(0,i.kt)("thead",{parentName:"table"},(0,i.kt)("tr",{parentName:"thead"},(0,i.kt)("th",{parentName:"tr",align:null},"data"))),(0,i.kt)("tbody",{parentName:"table"},(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"{data: ","[1, 2, 3...]","}")),(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"{data: ","[4, 5, 6...]","}")),(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"...")))),(0,i.kt)("p",null,"Let's consider that we would like to calculate statistics among simulations for the values at the first position of the list. An independent variable can be set using values, for instance, from the second position. Also, in some cases, an array of the independent variables be constructed using the 'rid' column, which represents a step in each simulation.\nLet's assume, that in each simulation value is recorded every 0.2 seconds, so we can construct and independent variable Time = rid*0.2."),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},"# --- adjust to your data --- #\n\n# Set simulation, batch and topic names:\nsimulation_name = 'my_simulation'\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\n\n# Data column:\ndata_label = 'data.data[0]'\n\n# Set method of index assignment as 'scale' or 'bin':\nmethod = 'bin'\n\n# Set time step to construct independent variable column as: Time = rid*time_step.\ntime_step  = 0.2\n# --------------------------- #\n\n# Create CitrosDB object:\nfrom citros import CitrosDB, CitrosData\ncitros = CitrosDB()\n\n# Query data:\ndf = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).data(data_label)\n\n# Construct independent variable column as: Time = rid*time_step.\ndf['Time'] = df['rid']*time_step\n\n# Construct CitrosData object, setting 'data.data[0]' as a data-column:\ndataset = CitrosData(df, data_label = data_label, units = 'm')\n\n# set an independent variable as 'Time' (column, that we constructed previously) by label by `param_label`:\nif method == 'bin':\n    db = dataset.bin_data(n_bins = 50, param_label = 'Time')\n# or\nelif method == 'scale':\n    db = dataset.scale_data(n_points = 50, param_label = 'Time')\nelse:\n    print('please define method of index assignment: \"scale\" or \"bin\"')\n\n# Get statistics.\n# When data is binned or interpolated, for each of the index the mean values, covariant matrix \n# and standard deviations (the square root the covariant matrix diagonal elements) may be calculated.\n# The output table is a pandas DataFrame:\n\nstat = db.get_statistics(return_format = 'citrosStat')\n\n# `stat` contains 3 attributes:\n# the mean values (type - pandas.DataFrame):\nprint('mean values:\\n', stat.mean.head(5))\n\n# the standard deviation (type - pandas.DataFrame):\nprint('standard deviation:\\n', stat.std.head(5))\n\n# the covariance matrix (type - pandas.Series):\nprint('covariance matrix:\\n', stat.covar_matrix.head(5))\n\n# Method head(n) of pandas.DataFrame is used to show the first n rows of the table\n\n\n# Plot statistics.\ndb.show_statistics()\n# by default, it plots +-3 standard deviation boundary.\n# To plot for another number of standard deviations, for example for +- 5std boundary: n_std = 5\n# you may style area between standard deviation boundaries: by std_area = True fill area with color.\n# by std_lines = False - remove lines of the boundary :\ndb.show_statistics(n_std = 5, std_area = True, std_lines = False)\n")),(0,i.kt)("h3",{id:"n-dimensional-vector"},"N-dimensional Vector"),(0,i.kt)("p",null,"The same example as for the ",(0,i.kt)("a",{parentName:"p",href:"#get-statistics-for-simulations-1-dimensional-vector"},"1-dimensional vector"),", but for the multidimensional vector."),(0,i.kt)("p",null,"Suppose for topic 'my_topic' from the batch 'my_batch', created by simulation 'my_simulation' every row in the 'data' column contains a dictionary and within this dictionary, the 'data' key corresponds to a list that has a length of 3, as illustrated below:"),(0,i.kt)("table",null,(0,i.kt)("thead",{parentName:"table"},(0,i.kt)("tr",{parentName:"thead"},(0,i.kt)("th",{parentName:"tr",align:null},"data"))),(0,i.kt)("tbody",{parentName:"table"},(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"{data: ","[1, 2, 3]","}")),(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"{data: ","[4, 5, 6]","}")),(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"...")))),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},"# --- adjust to your data --- #\n\n# Set simulation, batch and topic names:\nsimulation_name = 'my_simulation'\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\n\n# Data is queried from the first, second, and third indices.\n# you can explicitly list columns you would like to query:\ndata_labels = ['data.data[0]', 'data.data[1]', 'data.data[2]']\n# or if the entire array is needed, it can be queried, in this example, simply as 'data.data'.\n# This way, when the CitrosData object is created, the array will be automatically divided into separate columns\n# data_labels = 'data.data'\n\n# Set method of index assignment as 'scale' or 'bin':\nmethod = 'bin'\n\n# Set time step to construct independent variable column as: Time = rid*time_step.\ntime_step  = 0.2\n# --------------------------- #\n\n# Create CitrosDB object:\nfrom citros import CitrosDB, CitrosData\ncitros = CitrosDB()\n\n# Query data:\ndf = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).data(data_labels)\n\n# Construct independent variable column as: Time = rid*time_step.\ndf['Time'] = df['rid']*time_step\n\n# Construct CitrosData object:\ndataset = CitrosData(df, data_label = data_labels, units = 'm')\n\n# set an independent variable as 'Time' (column, that we constructed previously) by label by `param_label`:\nif method == 'bin':\n    db = dataset.bin_data(n_bins = 50, param_label = 'Time')\n# or\nelif method == 'scale':\n    db = dataset.scale_data(n_points = 50, param_label = 'Time')\nelse:\n    print('please define method of index assignment: \"scale\" or \"bin\"')\n\n\n# Get statistics.\n# When data is binned or interpolated, for each of the index mean values, covariant matrix \n# and standard deviations (the square root the covariant matrix diagonal elements) may be calculated.\n# The output table is a pandas DataFrame:\nstat = db.get_statistics(return_format = 'citrosStat')\n\n# `stat` contains 3 attributes:\n# the mean values (type - pandas.DataFrame):\nprint('mean values:\\n', stat.mean.head(5))\n\n# the standard deviation (type - pandas.DataFrame):\nprint('standard deviation:\\n', stat.std.head(5))\n\n# the covariance matrix (type - pandas.Series):\nprint('covariance matrix:\\n', stat.covar_matrix.head(5))\n\n# Method head(n) of pandas.DataFrame is used to show the first n rows of the table\n\n\n# Plot statistics.\ndb.show_statistics()\n# by default, it plots +-3 standard deviation boundary.\n# To plot for another number of standard deviations, for example for +- 5std boundary: n_std = 5\n# you may style area between standard deviation boundaries: by std_area = True fill area with color.\n# by std_lines = False - remove lines of the boundary:\ndb.show_statistics(n_std = 5, std_area = True, std_lines = False)\n")),(0,i.kt)("h2",{id:"correlation-between-variables"},"Correlation Between Variables"),(0,i.kt)("p",null,"For topic 'my_topic' from batch 'my_batch', created by simulation simulation 'my_simulation' consider a table where the 'data' column holds dictionaries with keys 'x', 'y', and 'time', as illustrated:"),(0,i.kt)("table",null,(0,i.kt)("thead",{parentName:"table"},(0,i.kt)("tr",{parentName:"thead"},(0,i.kt)("th",{parentName:"tr",align:null},"data"))),(0,i.kt)("tbody",{parentName:"table"},(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"{x: 1, y: 2, time: 0.1}")),(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"{x: 4, y: 5, time: 0.2}")),(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"...")))),(0,i.kt)("p",null,"First, the values from different simulations should be corresponded with each other. For this purpose a common scale may be established through the independent variable. Two methods may be applied. The first one is to divide the independent variable into N ranges, index each, and average the data values within those ranges; it is implemented by ",(0,i.kt)("inlineCode",{parentName:"p"},"bin_data()")," method. The second one is to scale the independent variable between ","[0,1]",", set N uniformly distributed points in this range, and interpolate data over this interval; this approach is implemented by method ",(0,i.kt)("inlineCode",{parentName:"p"},"scale_data()"),"."),(0,i.kt)("p",null,"Let's choose 'data.time' as an independent variable, set indices and collect the statistics among different simulations and plot the correlation 'data.x' vs. 'data.y'."),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},"# --- adjust to your data --- #\n\n# Set simulation, batch and topic names:\nsimulation_name = 'my_simulation'\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\n\n# Data labels to plot correlation for\nx = 'data.x'\ny = 'data.y'\n\n# Independent variable label\nindependent_var_label = 'data.time'\n\n# Set method of index assignment as 'scale' or 'bin':\nmethod = 'bin'\n\n# Index to plot corelation for:\nslice_id = 1\n# or if the index number is unknown, `slice_val` parameter may be used to define \n# the approximate value of the independent variable. The nearest to this value index will be set.\n# if the method of index assignment is set as 'scale', do not forget that the interval slice_val is [0, 1].\nslice_val = 0.1\n\n# To add bounding error to the plot, set bounding_error = True:\nbounding_error = False\n# --------------------------- #\n\n# Create CitrosDB object:\nfrom citros import CitrosDB, CitrosData\ncitros = CitrosDB()\n\n# Query data\ndf = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).data([x, y, independent_var_label])\n\n# Construct CitrosData object, setting 'data.x' and 'data.y' as a data-columns:\ndataset = CitrosData(df, data_label = [x, y], units = 'm')\n\n# Use method scale_data() or bin_data() to get correspondence between different simulation and assign indexes to independent_var_label axis:\n\nif method == 'bin':\n    db = dataset.bin_data(n_bins = 50, param_label = independent_var_label)\n# or\nelif method == 'scale':\n    db = dataset.scale_data(n_points = 50, param_label = independent_var_label)\nelse:\n    print('please define method of index assignment: \"scale\" or \"bin\"')\n\n# Plot correlation plot for the exact index:\nellipse_param = db.show_correlation(x_col = x, y_col = y,\n                                    slice_id = slice_id,\n                                    n_std = 3,\n                                    bounding_error = bounding_error,\n                                    return_ellipse_param = True)\n\n# Print ellipse parameters:\nprint(\"ellipse parameters:\")\nprint(f\"center: {ellipse_param['x']}, {ellipse_param['y']}\")\nprint(f\"width: {ellipse_param['width']}, height: {ellipse_param['height']}\")\nprint(f\"angle: {ellipse_param['alpha']}\\n\")\nif bounding_error:\n    print(f\"radius of the error circle: {ellipse_param['bounding_error']}\\n\")\n\n# As an alternative, instead of setting the exact value of index (`slice_id`), the approximate\n# value of the independent variable may be provided by `slice_val`. Then the nearest to this value index will be adopted.\n#the number of error ellipses and their radii are controlled by parameter `n_std`\ndb.show_correlation(x_col = x, y_col = y,\n                    slice_val = slice_val,\n                    n_std = [1, 2, 3],\n                    bounding_error = bounding_error)\n")),(0,i.kt)("h2",{id:"predictions"},"Predictions"),(0,i.kt)("p",null,"Let's assume that in batch 'my_batch' for the topic 'my_topic', created by simulation simulation 'my_simulation' there are four simulations, each of them corresponds to the different value of some parameter 'M'. Also let's consider that each cell in the 'data' column contains a dictionary:"),(0,i.kt)("table",null,(0,i.kt)("thead",{parentName:"table"},(0,i.kt)("tr",{parentName:"thead"},(0,i.kt)("th",{parentName:"tr",align:null},"data"))),(0,i.kt)("tbody",{parentName:"table"},(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"{x: 1, time: 0.1}")),(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"{x: 4, time: 0.2}")),(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"...")))),(0,i.kt)("p",null,"To conduct a comparison of the values of different simulations, the correspondence between these values should be established. That may be done by assigning indices through independent variable. One of the approach is to to divide the independent variable into N ranges, index each, and average the data values within those ranges; it is implemented by ",(0,i.kt)("inlineCode",{parentName:"p"},"bin_data()")," method. The second one is to scale the independent variable between ","[0,1]",", set N uniformly distributed points in this range, and interpolate data over this interval; this approach is implemented by method ",(0,i.kt)("inlineCode",{parentName:"p"},"scale_data()"),"."),(0,i.kt)("p",null,"Let's set 'data.time' as an independent variable and find the prediction for the 'data.x' variable for value of M = M0. "),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},"# --- adjust to your data --- #\n\n# Set simulation, batch and topic names:\nsimulation_name = 'my_simulation'\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\n\n# Data labels to plot correlation for \ndata_label = 'data.x'\n\n# Independent variable label\nindependent_var_label = 'data.time'\n\n# Set method of index assignment as 'scale' or 'bin':\nmethod = 'bin'\n\n# Define which simulation (sid) corresponds to which value of parameter M:\n# Let's assume that sid = 0 corresponds to M = -1.5; sid = 1, M = 0, sid = 2, M = 2.5; sid = 3, M = 4:\nM = {0: -1.5, 1: 0, 2: 2.5, 3: 4}\n\n# And we would like to find value for the M = 1:\nM0 = 1\n\n# Prediction method: 'neural_net' - neural net regression, 'poly' - polynomial regression ('poly') or 'gmm' - gaussian mixture model\npredict_method = 'poly'\n# --------------------------- #\n\n# Create CitrosDB object:\nfrom citros import CitrosDB, CitrosData, CitrosDataArray\ncitros = CitrosDB()\n\n# Create CitrosDataArray object:\ndb_array = CitrosDataArray()\n\n# Query data for each of the M parameter, assign indexes over 'data.time' axis to set\n# correspondence between different simulations and pass the result to CitrosDataArray that we created:\nfor s, m in M.items():\n    #query data\n    df = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).sid(s).data([data_label, independent_var_label])\n\n    #create CitrosData object and set 'data.t' as a parameter.\n    dataset = CitrosData(df,  \n                        data_label = data_label,\n                        parameters = {'M': m})\n    if method == 'bin':\n        db = dataset.bin_data(n_bins = 50, param_label = independent_var_label)\n    # or\n    elif method == 'scale':\n        db = dataset.scale_data(n_points = 50, param_label = independent_var_label)\n    else:\n        print('please define method of index assignment: \"scale\" or \"bin\"')\n\n    #store in CitrosDataArray by add_db() method\n    db_array.add_db(db)\n\n# Get the prediction with the defined prediction method:\n\nif predict_method == 'poly':\n    result = db_array.get_prediction(parameters = {'M': M0},\n                                    method = 'poly', \n                                    n_poly = 2)\nelif predict_method == 'neural_net':\n    result = db_array.get_prediction(parameters = {'M': M0}, \n                                     method = 'neural_net',\n                                     activation='tanh', max_iter = 200, solver='lbfgs',\n                                     hidden_layer_sizes = (8,), random_state = 9)\nelif predict_method == 'gmm':\n    result = db_array.get_prediction(parameters = {'M': M0}, \n                                     method = 'gmm')\nelse:\n    print('define prediction method as \"neural_net\", \"poly\" or \"gmm\"')\n    result = None\n\nif result is not None:\n    print(result.head(5))\n")))}p.isMDXComponent=!0}}]);
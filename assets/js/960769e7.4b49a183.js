"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[8258],{3905:(t,a,e)=>{e.d(a,{Zo:()=>d,kt:()=>y});var n=e(7294);function i(t,a,e){return a in t?Object.defineProperty(t,a,{value:e,enumerable:!0,configurable:!0,writable:!0}):t[a]=e,t}function r(t,a){var e=Object.keys(t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(t);a&&(n=n.filter((function(a){return Object.getOwnPropertyDescriptor(t,a).enumerable}))),e.push.apply(e,n)}return e}function l(t){for(var a=1;a<arguments.length;a++){var e=null!=arguments[a]?arguments[a]:{};a%2?r(Object(e),!0).forEach((function(a){i(t,a,e[a])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(e)):r(Object(e)).forEach((function(a){Object.defineProperty(t,a,Object.getOwnPropertyDescriptor(e,a))}))}return t}function o(t,a){if(null==t)return{};var e,n,i=function(t,a){if(null==t)return{};var e,n,i={},r=Object.keys(t);for(n=0;n<r.length;n++)e=r[n],a.indexOf(e)>=0||(i[e]=t[e]);return i}(t,a);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(t);for(n=0;n<r.length;n++)e=r[n],a.indexOf(e)>=0||Object.prototype.propertyIsEnumerable.call(t,e)&&(i[e]=t[e])}return i}var s=n.createContext({}),p=function(t){var a=n.useContext(s),e=a;return t&&(e="function"==typeof t?t(a):l(l({},a),t)),e},d=function(t){var a=p(t.components);return n.createElement(s.Provider,{value:a},t.children)},m="mdxType",c={inlineCode:"code",wrapper:function(t){var a=t.children;return n.createElement(n.Fragment,{},a)}},u=n.forwardRef((function(t,a){var e=t.components,i=t.mdxType,r=t.originalType,s=t.parentName,d=o(t,["components","mdxType","originalType","parentName"]),m=p(e),u=i,y=m["".concat(s,".").concat(u)]||m[u]||c[u]||r;return e?n.createElement(y,l(l({ref:a},d),{},{components:e})):n.createElement(y,l({ref:a},d))}));function y(t,a){var e=arguments,i=a&&a.mdxType;if("string"==typeof t||i){var r=e.length,l=new Array(r);l[0]=u;var o={};for(var s in a)hasOwnProperty.call(a,s)&&(o[s]=a[s]);o.originalType=t,o[m]="string"==typeof t?t:i,l[1]=o;for(var p=2;p<r;p++)l[p]=e[p];return n.createElement.apply(null,l)}return n.createElement.apply(null,e)}u.displayName="MDXCreateElement"},4086:(t,a,e)=>{e.r(a),e.d(a,{assets:()=>s,contentTitle:()=>l,default:()=>c,frontMatter:()=>r,metadata:()=>o,toc:()=>p});var n=e(7462),i=(e(7294),e(3905));const r={toc_max_heading_level:4,hide_title:!0,sidebar_label:"Plotting"},l="Plotting",o={unversionedId:"data_analysis/snippets_doc/data_access/snippets_plotting",id:"data_analysis/snippets_doc/data_access/snippets_plotting",title:"Plotting",description:"Plot with pandas",source:"@site/docs/data_analysis/snippets_doc/data_access/snippets_plotting.md",sourceDirName:"data_analysis/snippets_doc/data_access",slug:"/data_analysis/snippets_doc/data_access/snippets_plotting",permalink:"/docs/data_analysis/snippets_doc/data_access/snippets_plotting",draft:!1,tags:[],version:"current",frontMatter:{toc_max_heading_level:4,hide_title:!0,sidebar_label:"Plotting"},sidebar:"gettingStartedSidebar",previous:{title:"Query Data",permalink:"/docs/data_analysis/snippets_doc/data_access/snippets_query_data"},next:{title:"Error Analysis",permalink:"/docs/data_analysis/snippets_doc/snippets_error_analysis"}},s={},p=[{value:"Plot with pandas",id:"plot-with-pandas",level:2},{value:"Time Plot",id:"time-plot",level:2},{value:"(y Vs. X)",id:"y-vs-x",level:2},{value:"Plot (y Vs. X)",id:"plot-y-vs-x",level:2},{value:"3d Plot",id:"3d-plot",level:2},{value:"Shared X-axis",id:"shared-x-axis",level:2},{value:"Grid of Plots",id:"grid-of-plots",level:2},{value:"Error Ellipse",id:"error-ellipse",level:2}],d={toc:p},m="wrapper";function c(t){let{components:a,...e}=t;return(0,i.kt)(m,(0,n.Z)({},d,e,{components:a,mdxType:"MDXLayout"}),(0,i.kt)("h1",{id:"plotting"},"Plotting"),(0,i.kt)("h2",{id:"plot-with-pandas"},"Plot with pandas"),(0,i.kt)("p",null,"This type of plot does not require saving the data prior to plotting and can be directly called after querying."),(0,i.kt)("p",null,"If the data of a topic 'my_topic' in batch 'my_batch', created by simulation 'my_simulation' looks like the following:"),(0,i.kt)("table",null,(0,i.kt)("thead",{parentName:"table"},(0,i.kt)("tr",{parentName:"thead"},(0,i.kt)("th",{parentName:"tr",align:null},"data"))),(0,i.kt)("tbody",{parentName:"table"},(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"{x: 1, y: 2, z: 3}")),(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"{x: 4, y: 5, z: 6}")),(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"...")))),(0,i.kt)("p",null,"To plot a graph with 'data.y' on the vertical axis versus 'rid' on the horizontal axis, and to separate the data based on 'sid', follow these steps:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},"from citros import CitrosDB\n\n# --- adjust to your data --- #\nsimulation_name = 'my_simulation'\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\n\ny = 'data.y'\n# --------------------------- #\n\ncitros = CitrosDB()\ncitros.simulation(simulation_name).batch(batch_name).topic(topic_name)\\\n      .data(y).set_index(['rid','sid']).unstack()[y].plot()\n")),(0,i.kt)("h2",{id:"time-plot"},"Time Plot"),(0,i.kt)("p",null,"This type of plot does not require saving the data prior to plotting and can be directly called after querying."),(0,i.kt)("p",null,"If the data for topic 'my_topic' in batch 'my_batch', created by simulation 'my_simulation' looks like the following:"),(0,i.kt)("table",null,(0,i.kt)("thead",{parentName:"table"},(0,i.kt)("tr",{parentName:"thead"},(0,i.kt)("th",{parentName:"tr",align:null},"data"))),(0,i.kt)("tbody",{parentName:"table"},(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"{x: 1, y: 2, z: 3}")),(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"{x: 4, y: 5, z: 6}")),(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"...")))),(0,i.kt)("p",null,"To plot 'data.x' against Time for each simulation (sid), where ",(0,i.kt)("inlineCode",{parentName:"p"},"Time")," = ",(0,i.kt)("inlineCode",{parentName:"p"},"time_step")," * rid:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},"from citros import CitrosDB\nimport matplotlib.pyplot as plt\nfig, ax = plt.subplots()\n\n# --- adjust to your data --- #\nsimulation_name = 'my_simulation'\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\n\ny = 'data.x'\n# --------------------------- #\n\ncitros = CitrosDB()\ncitros.simulation(simulation_name).batch(batch_name).topic(topic_name).\\\n       time_plot(ax, var_name = y, time_step = 0.5, y_label = 'x', title_text = 'x vs. Time')\n")),(0,i.kt)("h2",{id:"y-vs-x"},"(y Vs. X)"),(0,i.kt)("p",null,"This type of plot does not require saving the data prior to plotting and can be directly called after querying."),(0,i.kt)("p",null,"If the data for topic 'my_topic' in batch 'my_batch', created by simulation 'my_simulation' looks like the following:"),(0,i.kt)("table",null,(0,i.kt)("thead",{parentName:"table"},(0,i.kt)("tr",{parentName:"thead"},(0,i.kt)("th",{parentName:"tr",align:null},"data"))),(0,i.kt)("tbody",{parentName:"table"},(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"{x: 1, y: 2, z: 3}")),(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"{x: 4, y: 5, z: 6}")),(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"...")))),(0,i.kt)("p",null,"To plot a graph with 'data.y' on the vertical axis versus 'data.x' on the horizontal axis, separating data according to simulations (sid), do the following:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},"from citros import CitrosDB\nimport matplotlib.pyplot as plt\nfig, ax = plt.subplots()\n\n# --- adjust to your data --- #\nsimulation_name = 'my_simulation'\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\n\nx = 'data.x'\ny = 'data.y'\n# --------------------------- #\n\ncitros = CitrosDB()\ncitros.simulation(simulation_name).batch(batch_name).topic(topic_name).\\\n       xy_plot(ax, var_x_name = x, var_y_name = y, x_label = 'x', y_label = 'y', title_text = 'y vs. x')\n")),(0,i.kt)("h2",{id:"plot-y-vs-x"},"Plot (y Vs. X)"),(0,i.kt)("p",null,"If the data under the topic 'my_topic' within the batch 'my_batch', created by simulation 'my_simulation' is structured as follows:"),(0,i.kt)("table",null,(0,i.kt)("thead",{parentName:"table"},(0,i.kt)("tr",{parentName:"thead"},(0,i.kt)("th",{parentName:"tr",align:null},"data"))),(0,i.kt)("tbody",{parentName:"table"},(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"{x: 1, y: 2, z: 3}")),(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"{x: 4, y: 5, z: 6}")),(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"...")))),(0,i.kt)("p",null,"To query this data and plot a graph of 'y vs. x', separating by simulation ids (sid):"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},"from citros import CitrosDB\n\n# --- adjust to your data --- #\nsimulation_name = 'my_simulation'\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\n\nx = 'data.x'\ny = 'data.y'\n# --------------------------- #\n\ncitros = CitrosDB()\ndf = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).data([x, y])\n\nfig, ax = citros.plot_graph(df, x, y, '-', title = 'y vs.x')\n")),(0,i.kt)("h2",{id:"3d-plot"},"3d Plot"),(0,i.kt)("p",null,"If the data under the topic 'my_topic' within the batch 'my_batch', created by simulation 'my_simulation' is structured as follows:"),(0,i.kt)("table",null,(0,i.kt)("thead",{parentName:"table"},(0,i.kt)("tr",{parentName:"thead"},(0,i.kt)("th",{parentName:"tr",align:null},"data"))),(0,i.kt)("tbody",{parentName:"table"},(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"{x: 1, y: 2, z: 3}")),(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"{x: 4, y: 5, z: 6}")),(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"...")))),(0,i.kt)("p",null,"to query data and make a 3d plot 'z vs. x and y', separating by simulation ids (sid):"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},"from citros import CitrosDB\n\n# --- adjust to your data --- #\nsimulation_name = 'my_simulation'\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\n\nx = 'data.x'\ny = 'data.y'\nz = 'data.z'\n# --------------------------- #\n\n#specify whether the axis range should be the same for all axes, True by default\nscale = False\n\ncitros = CitrosDB()\ndf = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).data([x, y, z])\n\nfig, ax = citros.plot_3dgraph(df, x, y, z, '--', title = 'z vs. x and y', scale = scale)\n")),(0,i.kt)("h2",{id:"shared-x-axis"},"Shared X-axis"),(0,i.kt)("p",null,"If the data under the topic 'my_topic' within the batch 'my_batch', created by simulation 'my_simulation' is structured as follows:"),(0,i.kt)("table",null,(0,i.kt)("thead",{parentName:"table"},(0,i.kt)("tr",{parentName:"thead"},(0,i.kt)("th",{parentName:"tr",align:null},"data"))),(0,i.kt)("tbody",{parentName:"table"},(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"{x: 1, y: 2, z: 3}")),(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"{x: 4, y: 5, z: 6}")),(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"...")))),(0,i.kt)("p",null,"to query and make two plots 'y vs. x' and 'z va. x', separating by simulation ids (sid):"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},"from citros import CitrosDB\n\n# --- adjust to your data --- #\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\nsimulation_name = 'my_simulation'\n\nx = 'data.x'\ny = 'data.y'\nz = 'data.z'\n# --------------------------- #\n\ncitros = CitrosDB()\ndf = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).data([x, y, z])\n\nfig, ax = citros.multiple_y_plot(df, x, [y, z], '--')\n")),(0,i.kt)("h2",{id:"grid-of-plots"},"Grid of Plots"),(0,i.kt)("p",null,"If the data under the topic 'my_topic' within the batch 'my_batch', created by simulation 'my_simulation' is structured as follows:"),(0,i.kt)("table",null,(0,i.kt)("thead",{parentName:"table"},(0,i.kt)("tr",{parentName:"thead"},(0,i.kt)("th",{parentName:"tr",align:null},"data"))),(0,i.kt)("tbody",{parentName:"table"},(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"{x: 1, y: 2, z: 3}")),(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"{x: 4, y: 5, z: 6}")),(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"...")))),(0,i.kt)("p",null,"To display a 3 x 3 matrix of graphs, where: (1) for the diagonal plots, show histograms depicting value distributions;\n(2) for the off-diagonal plots, illustrate the pairwise relationships between x, y, and z, execute the following:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},"from citros import CitrosDB\n\n# --- adjust to your data --- #\nsimulation_name = 'my_simulation'\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\n\nx = 'data.x'\ny = 'data.y'\nz = 'data.z'\n# --------------------------- #\n\n#specify whether the axis range should be the same for both axes, True by default\nscale = False\n\ncitros = CitrosDB()\ndf = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).data([x, y, z])\n\nfig, ax = citros.multiplot(df, [x, y, z], '-', scale = scale)\n")),(0,i.kt)("h2",{id:"error-ellipse"},"Error Ellipse"),(0,i.kt)("p",null,"If the data of the topic 'my_topic' in batch 'my_batch', created by simulation 'my_simulation' is structured as follows:"),(0,i.kt)("table",null,(0,i.kt)("thead",{parentName:"table"},(0,i.kt)("tr",{parentName:"thead"},(0,i.kt)("th",{parentName:"tr",align:null},"data"))),(0,i.kt)("tbody",{parentName:"table"},(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"{x: 1, y: 2, z: 3}")),(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"{x: 4, y: 5, z: 6}")),(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"...")))),(0,i.kt)("p",null,"To plot error ellipse for the values of 'data.x' and 'data.y' columns that corresponds to the last point (rid) in each simulation (sid):"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},"from citros import CitrosDB\n\n# --- adjust to your data --- #\n\n#specify batch, simulation and topic name\nsimulation_name = 'my_simulation'\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\n\n#specify columns to plot\nx = 'data.x'\ny = 'data.y'\n# --------------------------- #\n\n#create citrosDB object\ncitros = CitrosDB()\n\n#get all possible sid:\nsid_list = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).get_unique_values('sid')\nprint(f\"sid numbers: {sid_list}\")\n\n#for each sid get the last rid:\nrid_dict = {}\nfor s in sid_list:\n    rid_dict[s] = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).sid(s).get_max_value('rid')\nprint(f\"rid last numbers: {rid_dict}\")\n\n# get the values of 'data.x' and 'data.y', that corresponds to the last rid:\n# we are creating an empty DataFrame 'df', query for the values of the exact sid and rid and add the result to the 'df'.\nimport pandas as pd\ndf = pd.DataFrame()\nfor s, r in rid_dict.items():\n    df = pd.concat([df, citros.simulation(simulation_name).batch(batch_name).topic(topic_name).sid(s).rid(r).data([x, y])])\n\n# print(df)\nfig, ax = citros.plot_sigma_ellipse(df, x_label = x, y_label = y, \n                                    n_std = [1,2,3], plot_origin=False, bounding_error=False,\n                                    set_x_label='x', set_y_label = 'y', title = 'Error ellipse')\n")))}c.isMDXComponent=!0}}]);
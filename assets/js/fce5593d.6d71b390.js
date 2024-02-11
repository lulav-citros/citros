"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[15777],{3905:(t,a,e)=>{e.d(a,{Zo:()=>c,kt:()=>y});var n=e(67294);function r(t,a,e){return a in t?Object.defineProperty(t,a,{value:e,enumerable:!0,configurable:!0,writable:!0}):t[a]=e,t}function i(t,a){var e=Object.keys(t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(t);a&&(n=n.filter((function(a){return Object.getOwnPropertyDescriptor(t,a).enumerable}))),e.push.apply(e,n)}return e}function o(t){for(var a=1;a<arguments.length;a++){var e=null!=arguments[a]?arguments[a]:{};a%2?i(Object(e),!0).forEach((function(a){r(t,a,e[a])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(e)):i(Object(e)).forEach((function(a){Object.defineProperty(t,a,Object.getOwnPropertyDescriptor(e,a))}))}return t}function s(t,a){if(null==t)return{};var e,n,r=function(t,a){if(null==t)return{};var e,n,r={},i=Object.keys(t);for(n=0;n<i.length;n++)e=i[n],a.indexOf(e)>=0||(r[e]=t[e]);return r}(t,a);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(t);for(n=0;n<i.length;n++)e=i[n],a.indexOf(e)>=0||Object.prototype.propertyIsEnumerable.call(t,e)&&(r[e]=t[e])}return r}var m=n.createContext({}),l=function(t){var a=n.useContext(m),e=a;return t&&(e="function"==typeof t?t(a):o(o({},a),t)),e},c=function(t){var a=l(t.components);return n.createElement(m.Provider,{value:a},t.children)},d="mdxType",u={inlineCode:"code",wrapper:function(t){var a=t.children;return n.createElement(n.Fragment,{},a)}},p=n.forwardRef((function(t,a){var e=t.components,r=t.mdxType,i=t.originalType,m=t.parentName,c=s(t,["components","mdxType","originalType","parentName"]),d=l(e),p=r,y=d["".concat(m,".").concat(p)]||d[p]||u[p]||i;return e?n.createElement(y,o(o({ref:a},c),{},{components:e})):n.createElement(y,o({ref:a},c))}));function y(t,a){var e=arguments,r=a&&a.mdxType;if("string"==typeof t||r){var i=e.length,o=new Array(i);o[0]=p;var s={};for(var m in a)hasOwnProperty.call(a,m)&&(s[m]=a[m]);s.originalType=t,s[d]="string"==typeof t?t:r,o[1]=s;for(var l=2;l<i;l++)o[l]=e[l];return n.createElement.apply(null,o)}return n.createElement.apply(null,e)}p.displayName="MDXCreateElement"},7482:(t,a,e)=>{e.r(a),e.d(a,{assets:()=>m,contentTitle:()=>o,default:()=>u,frontMatter:()=>i,metadata:()=>s,toc:()=>l});var n=e(87462),r=(e(67294),e(3905));const i={toc_max_heading_level:4,hide_title:!0,sidebar_label:"Query Data"},o="Query Data",s={unversionedId:"data_analysis/snippets_doc/data_access/snippets_query_data",id:"version-0.2.42/data_analysis/snippets_doc/data_access/snippets_query_data",title:"Query Data",description:"Query All Data",source:"@site/versioned_docs/version-0.2.42/data_analysis/snippets_doc/data_access/snippets_query_data.md",sourceDirName:"data_analysis/snippets_doc/data_access",slug:"/data_analysis/snippets_doc/data_access/snippets_query_data",permalink:"/docs/data_analysis/snippets_doc/data_access/snippets_query_data",draft:!1,tags:[],version:"0.2.42",frontMatter:{toc_max_heading_level:4,hide_title:!0,sidebar_label:"Query Data"},sidebar:"gettingStartedSidebar",previous:{title:"Batch Content",permalink:"/docs/data_analysis/snippets_doc/data_access/snippets_batch_content"},next:{title:"Plotting",permalink:"/docs/data_analysis/snippets_doc/data_access/snippets_plotting"}},m={},l=[{value:"Query All Data",id:"query-all-data",level:2},{value:"Query Exact Simulation",id:"query-exact-simulation",level:2},{value:"Query Several Simulations",id:"query-several-simulations",level:2},{value:"Query First <code>n</code> Messages",id:"query-first-n-messages",level:2},{value:"Query Every n-th Message",id:"query-every-n-th-message",level:2},{value:"Average Before Querying",id:"average-before-querying",level:2},{value:"Average",id:"average",level:3},{value:"Moving Average",id:"moving-average",level:3},{value:"Query Array Data",id:"query-array-data",level:2},{value:"Retrieve One Column",id:"retrieve-one-column",level:3},{value:"Retrieve Several Columns",id:"retrieve-several-columns",level:3},{value:"Divide Array By Columns",id:"divide-array-by-columns",level:3},{value:"Query Json-object Data",id:"query-json-object-data",level:2},{value:"Query Mixed Format Data",id:"query-mixed-format-data",level:2},{value:"Query Initial Parameters",id:"query-initial-parameters",level:2},{value:"Divide Tables by sid",id:"divide-tables-by-sid",level:2},{value:"Make SQL Query",id:"make-sql-query",level:2}],c={toc:l},d="wrapper";function u(t){let{components:a,...e}=t;return(0,r.kt)(d,(0,n.Z)({},c,e,{components:a,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"query-data"},"Query Data"),(0,r.kt)("h2",{id:"query-all-data"},"Query All Data"),(0,r.kt)("p",null,"Query data for topic 'my_topic' from the batch 'my_batch', created by simulation 'my_simulation':"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"from citros import CitrosDB\n\n# --- adjust to your data --- #\nsimulation_name = 'my_simulation'\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\n# --------------------------- #\n\ncitros = CitrosDB()\ndf = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).data()\n\n#print first 5 rows of the obtained pandas.DataFrame\nprint(df.head(5))\n")),(0,r.kt)("h2",{id:"query-exact-simulation"},"Query Exact Simulation"),(0,r.kt)("p",null,"Query data from the batch 'my_batch', created by simulation 'my_simulation' for topic 'my_topic' for the exact simulation id (sid) = 1:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"from citros import CitrosDB\n\n# --- adjust to your data --- #\nsimulation_name = 'my_simulation'\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\n# --------------------------- #\n\ncitros = CitrosDB()\ndf = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).sid(1).data()\n\n#print first 5 rows of the obtained pandas.DataFrame\nprint(df.head(5))\n")),(0,r.kt)("h2",{id:"query-several-simulations"},"Query Several Simulations"),(0,r.kt)("p",null,"Query data from the batch 'my_batch', created by simulation 'my_simulation' for topic 'my_topic' for simulation id (sid) = 1 and 2:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"from citros import CitrosDB\n\n# --- adjust to your data --- #\nsimulation_name = 'my_simulation'\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\n# --------------------------- #\n\ncitros = CitrosDB()\ndf = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).sid([1, 2]).data()\n\n#print first 5 rows of the obtained pandas.DataFrame\nprint(df.head(5))\n")),(0,r.kt)("h2",{id:"query-first-n-messages"},"Query First ",(0,r.kt)("inlineCode",{parentName:"h2"},"n")," Messages"),(0,r.kt)("p",null,"Query first ",(0,r.kt)("inlineCode",{parentName:"p"},"n")," messages of the each simulation from batch 'my_batch', created by simulation 'my_simulation' for topic 'my_topic'. Parameter ",(0,r.kt)("inlineCode",{parentName:"p"},"rid")," is a serial number (starts from 0) in each simulation and by method ",(0,r.kt)("inlineCode",{parentName:"p"},"rid()")," we can set the last rid to query:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"from citros import CitrosDB\n\n# --- adjust to your data --- #\nsimulation_name = 'my_simulation'\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\nn = 5\n# --------------------------- #\n\ncitros = CitrosDB()\ndf = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).rid(end = n-1).data()\nprint(df)\n")),(0,r.kt)("h2",{id:"query-every-n-th-message"},"Query Every n-th Message"),(0,r.kt)("p",null,"Query every n-th message of each simulation from batch 'my_batch', created by simulation 'my_simulation' for topic 'my_topic':"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"from citros import CitrosDB\n\n# --- adjust to your data --- #\nsimulation_name = 'my_simulation'\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\nn = 5\n# --------------------------- #\n\ncitros = CitrosDB()\ndf = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).skip(n).data()\n\n#print first 5 rows of the obtained pandas.DataFrame\nprint(df.head(5))\n")),(0,r.kt)("h2",{id:"average-before-querying"},"Average Before Querying"),(0,r.kt)("h3",{id:"average"},"Average"),(0,r.kt)("p",null,"Group and average every set of ",(0,r.kt)("inlineCode",{parentName:"p"},"n")," consecutive messages of each simulation run and query averaged data from batch 'my_batch', created by simulation 'my_simulation' for topic 'my_topic'. The queried column(s) must be numeric and explicitly specified."),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"from citros import CitrosDB\n\n# --- adjust to your data --- #\nsimulation_name = 'my_simulation'\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\ndata_column = 'my_column'\nn = 5\n# --------------------------- #\n\ncitros = CitrosDB()\ndf = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).avg(n).data(data_column)\n\n#print first 5 rows of the obtained pandas.DataFrame\nprint(df.head(5))\n")),(0,r.kt)("h3",{id:"moving-average"},"Moving Average"),(0,r.kt)("p",null,"Compute moving average with the window size equals ",(0,r.kt)("inlineCode",{parentName:"p"},"n")," and then query each ",(0,r.kt)("inlineCode",{parentName:"p"},"s"),"-th message of the result for the data from the topic 'my_topic' of the batch 'my_batch', created by simulation 'my_simulation'. The queried column(s) must be numeric and explicitly specified."),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"from citros import CitrosDB\n\n# --- adjust to your data --- #\nsimulation_name = 'my_simulation'\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\ndata_column = 'my_column'\nn = 5\ns = 2\n# --------------------------- #\n\ncitros = CitrosDB()\ndf = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).move_avg(n, s).data(data_column)\n\n#print first 5 rows of the obtained pandas.DataFrame\nprint(df.head(5))\n")),(0,r.kt)("h2",{id:"query-array-data"},"Query Array Data"),(0,r.kt)("h3",{id:"retrieve-one-column"},"Retrieve One Column"),(0,r.kt)("p",null,"Let's consider a table for topic 'my_topic' from the batch 'my_batch', created by simulation 'my_simulation', where each row under the 'data' column holds a dictionary (json-object) and within this dictionary, the key 'data' maps to a array of values, as shown:"),(0,r.kt)("table",null,(0,r.kt)("thead",{parentName:"table"},(0,r.kt)("tr",{parentName:"thead"},(0,r.kt)("th",{parentName:"tr",align:null},"data"))),(0,r.kt)("tbody",{parentName:"table"},(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"{data: ","[1, 2, 3...]","}")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"{data: ","[4, 5, 6...]","}")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"...")))),(0,r.kt)("p",null,"To extract the values from the first indexes from these arrays, follow these steps:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"from citros import CitrosDB\n\n# --- adjust to your data --- #\nsimulation_name = 'my_simulation'\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\ncolumn_name = 'data.data[0]'\n# --------------------------- #\n\ncitros = CitrosDB()\n\n# index starts from 0, so refer to the first index as \"[0]\"\ndf = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).data(column_name)\n\n#print first 5 rows of the obtained pandas.DataFrame\nprint(df.head(5))\n")),(0,r.kt)("h3",{id:"retrieve-several-columns"},"Retrieve Several Columns"),(0,r.kt)("p",null,"Let's consider a table for topic 'my_topic' from the batch 'my_batch', created by simulation 'my_simulation', where each row under the 'data' column holds a dictionary and within this dictionary, the key 'val' maps to a list of values, as shown:"),(0,r.kt)("table",null,(0,r.kt)("thead",{parentName:"table"},(0,r.kt)("tr",{parentName:"thead"},(0,r.kt)("th",{parentName:"tr",align:null},"data"))),(0,r.kt)("tbody",{parentName:"table"},(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"{val: ","[1, 2, 3...]","}")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"{val: ","[4, 5, 6...]","}")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"...")))),(0,r.kt)("p",null,"To extract the values, for example, from the first and second indexes from these arrays, follow these steps:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"from citros import CitrosDB\n\n# --- adjust to your data --- #\nsimulation_name = 'my_simulation'\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\ncolumn_names = ['data.val[0]', 'data.val[1]']\n# --------------------------- #\n\ncitros = CitrosDB()\n\n# index starts from 0, so refer to the first index as \"[0]\" and to the second as \"[1]\"\ndf = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).data(column_names)\n\n#print first 5 rows of the obtained pandas.DataFrame\nprint(df.head(5))\n")),(0,r.kt)("h3",{id:"divide-array-by-columns"},"Divide Array By Columns"),(0,r.kt)("p",null,"Suppose for topic 'my_topic' from the batch 'my_batch', created by simulation 'my_simulation' every row in the 'data' column contains a dictionary and within this dictionary, the 'data' key corresponds to a list that has a length of 3, as illustrated below:"),(0,r.kt)("table",null,(0,r.kt)("thead",{parentName:"table"},(0,r.kt)("tr",{parentName:"thead"},(0,r.kt)("th",{parentName:"tr",align:null},"data"))),(0,r.kt)("tbody",{parentName:"table"},(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"{data: ","[1, 2, 3]","}")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"{data: ","[4, 5, 6]","}")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"...")))),(0,r.kt)("p",null,"To extract these values into separate columns and label them as 'x', 'y', and 'z', proceed as follows:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"from citros import CitrosDB\n\n# --- adjust to your data --- #\nsimulation_name = 'my_simulation'\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\n# --------------------------- #\n\nnew_column_names = ['x', 'y', 'z']\nquery = ['data.data['+str(i)+']' for i in range(len(new_column_names))]\n\ncitros = CitrosDB()\ndf = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).data(query)\ndf.rename({query[i]: new_column_names[i] for i in range(len(query))}, axis = 1, inplace = True)\n\n#print first 5 rows of the obtained pandas.DataFrame\nprint(df.head(5))\n")),(0,r.kt)("h2",{id:"query-json-object-data"},"Query Json-object Data"),(0,r.kt)("p",null,"For topic 'my_topic' from the batch 'my_batch', created by simulation 'my_simulation' consider a table where the 'data' column holds dictionaries with keys 'x', 'y', and 'z', as illustrated:"),(0,r.kt)("table",null,(0,r.kt)("thead",{parentName:"table"},(0,r.kt)("tr",{parentName:"thead"},(0,r.kt)("th",{parentName:"tr",align:null},"data"))),(0,r.kt)("tbody",{parentName:"table"},(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"{x: 1, y: 2, z: 3}")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"{x: 4, y: 5, z: 6}")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"...")))),(0,r.kt)("p",null,"To retrieve only the data corresponding to the keys 'x' and 'y':"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"from citros import CitrosDB\n\n# --- adjust to your data --- #\nsimulation_name = 'my_simulation'\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\ncolumn_names = ['data.x', 'data.y']\n# --------------------------- #\n\ncitros = CitrosDB()\n\ndf = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).data(column_names)\n\n#print first 5 rows of the obtained pandas.DataFrame\nprint(df.head(5))\n")),(0,r.kt)("h2",{id:"query-mixed-format-data"},"Query Mixed Format Data"),(0,r.kt)("p",null,"If data has a very complex format, combining json-arrays and json-objects nested inside each other, for example like:"),(0,r.kt)("p",null,"|data                           |\n|-------------------------------\n|{coord: {v: [0, {w: ","[1]","} ] } } |\n|{coord: {v: [0, {w: ","[2]","} ] } } |\n|...                            |"),(0,r.kt)("p",null,"to retrieve values from array under the key 'w', batch is 'my_batch', created by simulation 'my_simulation', and topic is 'my_topic':"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"from citros import CitrosDB\n\n# --- adjust to your data --- #\nsimulation_name = 'my_simulation'\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\ncolumn_name = 'data.coord.v[1].w[0]'\n# --------------------------- #\n\ncitros = CitrosDB()\n\ndf = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).data(column_name)\n\n#print first 5 rows of the obtained pandas.DataFrame\nprint(df.head(5))\n")),(0,r.kt)("h2",{id:"query-initial-parameters"},"Query Initial Parameters"),(0,r.kt)("p",null,"Initial parameters are stored in the topic '/config'. Its data can be accessed as data of the any other topics:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"from citros import CitrosDB\n\n# --- adjust to your data --- #\nsimulation_name = 'my_simulation'\nbatch_name = 'my_batch'\n# --------------------------- #\n\ncitros = CitrosDB()\n\ndf = citros.simulation(simulation_name).batch(batch_name).topic('/config').data()\nprint(df)\n")),(0,r.kt)("h2",{id:"divide-tables-by-sid"},"Divide Tables by sid"),(0,r.kt)("p",null,"Query the data from the batch 'my_batch', created by simulation 'my_simulation' and split the resulting pandas.DataFrame into several DataFrames based on the 'sid'. The outcome is a dictionary where each DataFrame is stored under a key corresponding to its 'sid'. Print all sids and pandas.DataFrame that corresponds to the sid = 0:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"from citros import CitrosDB\n\n# --- adjust to your data --- #\nsimulation_name = 'my_simulation'\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\n# --------------------------- #\n\ncitros = CitrosDB()\n\ndfs = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).data_dict()\nprint(f'sids = {list(dfs.keys())}')\nprint(dfs[0])\n")),(0,r.kt)("h2",{id:"make-sql-query"},"Make SQL Query"),(0,r.kt)("p",null,"Make your own query to the PostgreSQL database:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},'from citros import CitrosDB\n\n# --- adjust to your data --- #\nmy_sql_query = \'SELECT * from "my_simulation"."my_batch" LIMIT 5\'\n# --------------------------- #\n\ncitros = CitrosDB()\ncurs = citros.get_connection().cursor()\ncurs.execute(my_sql_query)\nD = curs.fetchall()\nprint(D)\n')))}u.isMDXComponent=!0}}]);
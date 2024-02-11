"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[11407],{3905:(t,e,n)=>{n.d(e,{Zo:()=>l,kt:()=>h});var a=n(67294);function i(t,e,n){return e in t?Object.defineProperty(t,e,{value:n,enumerable:!0,configurable:!0,writable:!0}):t[e]=n,t}function o(t,e){var n=Object.keys(t);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(t);e&&(a=a.filter((function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable}))),n.push.apply(n,a)}return n}function m(t){for(var e=1;e<arguments.length;e++){var n=null!=arguments[e]?arguments[e]:{};e%2?o(Object(n),!0).forEach((function(e){i(t,e,n[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(n)):o(Object(n)).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(n,e))}))}return t}function s(t,e){if(null==t)return{};var n,a,i=function(t,e){if(null==t)return{};var n,a,i={},o=Object.keys(t);for(a=0;a<o.length;a++)n=o[a],e.indexOf(n)>=0||(i[n]=t[n]);return i}(t,e);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(t);for(a=0;a<o.length;a++)n=o[a],e.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(t,n)&&(i[n]=t[n])}return i}var r=a.createContext({}),c=function(t){var e=a.useContext(r),n=e;return t&&(n="function"==typeof t?t(e):m(m({},e),t)),n},l=function(t){var e=c(t.components);return a.createElement(r.Provider,{value:e},t.children)},u="mdxType",p={inlineCode:"code",wrapper:function(t){var e=t.children;return a.createElement(a.Fragment,{},e)}},_=a.forwardRef((function(t,e){var n=t.components,i=t.mdxType,o=t.originalType,r=t.parentName,l=s(t,["components","mdxType","originalType","parentName"]),u=c(n),_=i,h=u["".concat(r,".").concat(_)]||u[_]||p[_]||o;return n?a.createElement(h,m(m({ref:e},l),{},{components:n})):a.createElement(h,m({ref:e},l))}));function h(t,e){var n=arguments,i=e&&e.mdxType;if("string"==typeof t||i){var o=n.length,m=new Array(o);m[0]=_;var s={};for(var r in e)hasOwnProperty.call(e,r)&&(s[r]=e[r]);s.originalType=t,s[u]="string"==typeof t?t:i,m[1]=s;for(var c=2;c<o;c++)m[c]=n[c];return a.createElement.apply(null,m)}return a.createElement.apply(null,n)}_.displayName="MDXCreateElement"},6881:(t,e,n)=>{n.r(e),n.d(e,{assets:()=>r,contentTitle:()=>m,default:()=>p,frontMatter:()=>o,metadata:()=>s,toc:()=>c});var a=n(87462),i=(n(67294),n(3905));const o={toc_max_heading_level:4,hide_title:!0,sidebar_label:"Batch Content"},m="Batch Content",s={unversionedId:"data_analysis/snippets_doc/data_access/snippets_batch_content",id:"version-0.2.43/data_analysis/snippets_doc/data_access/snippets_batch_content",title:"Batch Content",description:"General Information",source:"@site/versioned_docs/version-0.2.43/data_analysis/snippets_doc/data_access/snippets_batch_content.md",sourceDirName:"data_analysis/snippets_doc/data_access",slug:"/data_analysis/snippets_doc/data_access/snippets_batch_content",permalink:"/docs/0.2.43/data_analysis/snippets_doc/data_access/snippets_batch_content",draft:!1,tags:[],version:"0.2.43",frontMatter:{toc_max_heading_level:4,hide_title:!0,sidebar_label:"Batch Content"},sidebar:"gettingStartedSidebar",previous:{title:"CITROS Data Analysis",permalink:"/docs/0.2.43/data_analysis/"},next:{title:"Query Data",permalink:"/docs/0.2.43/data_analysis/snippets_doc/data_access/snippets_query_data"}},r={},c=[{value:"General Information",id:"general-information",level:2},{value:"Topic Overview",id:"topic-overview",level:2},{value:"Data Structure",id:"data-structure",level:2},{value:"Sizes of the Batches",id:"sizes-of-the-batches",level:2},{value:"Sizes of the Batches of the Certain Simulation",id:"sizes-of-the-batches-of-the-certain-simulation",level:2},{value:"Size of the Certain Batch",id:"size-of-the-certain-batch",level:2},{value:"Maximum Value",id:"maximum-value",level:2},{value:"Minimum Value",id:"minimum-value",level:2},{value:"Indices of the Minimum and Maximum Values",id:"indices-of-the-minimum-and-maximum-values",level:2},{value:"List of Unique Values",id:"list-of-unique-values",level:2},{value:"Number of Messages",id:"number-of-messages",level:2},{value:"Number of Messages in Each Simulation",id:"number-of-messages-in-each-simulation",level:2}],l={toc:c},u="wrapper";function p(t){let{components:e,...n}=t;return(0,i.kt)(u,(0,a.Z)({},l,n,{components:e,mdxType:"MDXLayout"}),(0,i.kt)("h1",{id:"batch-content"},"Batch Content"),(0,i.kt)("h2",{id:"general-information"},"General Information"),(0,i.kt)("p",null,"Show information about batch 'my_batch', created by simulation 'my_simulation':"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},"from citros import CitrosDB\n\n# --- adjust to your data --- #\nsimulation_name = 'my_simulation'\nbatch_name = 'my_batch'\n# --------------------------- #\n\ncitros = CitrosDB()\ncitros.simulation(simulation_name).batch(batch_name).info().print()\n")),(0,i.kt)("h2",{id:"topic-overview"},"Topic Overview"),(0,i.kt)("p",null,"Show information and structure of the data of the topic 'my_topic' from the batch 'my_batch', created by simulation 'my_simulation':"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},"from citros import CitrosDB\n\n# --- adjust to your data --- #\nsimulation_name = 'my_simulation'\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\n# --------------------------- #\n\ncitros = CitrosDB()\ncitros.simulation(simulation_name).batch(batch_name).topic(topic_name).info().print()\n")),(0,i.kt)("h2",{id:"data-structure"},"Data Structure"),(0,i.kt)("p",null,"Show table with data structure for topic 'my_topic' of  the batch 'my_batch', created by simulation 'my_simulation':"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},"from citros import CitrosDB\n\n# --- adjust to your data --- #\nsimulation_name = 'my_simulation'\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\n# --------------------------- #\n\ncitros = CitrosDB()\ncitros.simulation(simulation_name).batch(batch_name).topic(topic_name).get_data_structure()\n")),(0,i.kt)("h2",{id:"sizes-of-the-batches"},"Sizes of the Batches"),(0,i.kt)("p",null,"Display sizes of the all uploaded to the PostgreSQL batches:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},"from citros import CitrosDB\n\ncitros = CitrosDB()\ncitros.get_batch_sizes()\n")),(0,i.kt)("h2",{id:"sizes-of-the-batches-of-the-certain-simulation"},"Sizes of the Batches of the Certain Simulation"),(0,i.kt)("p",null,"Display sizes of the batches, created by simulation simulation 'my_simulation':"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},"from citros import CitrosDB\n\n# --- adjust to your data --- #\nsimulation_name = 'my_simulation'\n# --------------------------- #\n\ncitros = CitrosDB()\ncitros.simulation(simulation_name).get_batch_sizes()\n")),(0,i.kt)("h2",{id:"size-of-the-certain-batch"},"Size of the Certain Batch"),(0,i.kt)("p",null,"Display size of the batch 'my_batch', created by simulation simulation 'my_simulation':"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},"from citros import CitrosDB\n\n# --- adjust to your data --- #\nsimulation_name = 'my_simulation'\nbatch_name = 'my_batch'\n# --------------------------- #\n\ncitros = CitrosDB()\ncitros.simulation(simulation_name).batch(batch_name).get_batch_sizes()\n")),(0,i.kt)("h2",{id:"maximum-value"},"Maximum Value"),(0,i.kt)("p",null,"Get maximum value of the column 'my_column' for the topic 'my_topic' from the batch 'my_batch', created by simulation 'my_simulation':"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},"from citros import CitrosDB\n\n# --- adjust to your data --- #\nsimulation_name = 'my_simulation'\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\ncolumn_name = 'my_column'\n# --------------------------- #\n\ncitros = CitrosDB()\nmax_value = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).get_max_value(column_name)\nprint(max_value)\n")),(0,i.kt)("h2",{id:"minimum-value"},"Minimum Value"),(0,i.kt)("p",null,"Get minimum value of the column 'my_column' for the topic 'my_topic' from the batch 'my_batch', created by simulation 'my_simulation':"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},"from citros import CitrosDB\n\n# --- adjust to your data --- #\nsimulation_name = 'my_simulation'\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\ncolumn_name = 'my_column'\n# --------------------------- #\n\ncitros = CitrosDB()\nmin_value = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).get_min_value(column_name)\nprint(min_value)\n")),(0,i.kt)("h2",{id:"indices-of-the-minimum-and-maximum-values"},"Indices of the Minimum and Maximum Values"),(0,i.kt)("p",null,"Get minimum and maximum values of the column 'my_column' and corresponding to them values of sid and rid for the topic 'my_topic' from the batch 'my_batch', created by simulation 'my_simulation':"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},"from citros import CitrosDB\n\n# --- adjust to your data --- #\nsimulation_name = 'my_simulation'\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\ncolumn_name = 'my_column'\n# --------------------------- #\n\ncitros = CitrosDB()\nmax_value, sid_max, rid_max = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).get_max_value(column_name, return_index = True)\nmin_value, sid_min, rid_min = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).get_min_value(column_name, return_index = True)\nprint(f\"maximum value of the column {column_name} = {max_value}, corresponding sid = {sid_max}, rid = {rid_max}\")\nprint(f\"minimum value of the column {column_name} = {min_value}, corresponding sid = {sid_min}, rid = {rid_min}\")\n")),(0,i.kt)("h2",{id:"list-of-unique-values"},"List of Unique Values"),(0,i.kt)("p",null,"Get list of simulation ids (sid) for the topic 'my_topic' from the batch 'my_batch', created by simulation 'my_simulation':"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},"from citros import CitrosDB\n\n# --- adjust to your data --- #\nsimulation_name = 'my_simulation'\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\n# --------------------------- #\n\ncitros = CitrosDB()\nsid_list = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).get_unique_values('sid')\nprint(sid_list)\n")),(0,i.kt)("h2",{id:"number-of-messages"},"Number of Messages"),(0,i.kt)("p",null,"Get number of messages in the batch 'my_batch', created by simulation 'my_simulation', for the topic 'my_topic':"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},"from citros import CitrosDB\n\n# --- adjust to your data --- #\nsimulation_name = 'my_simulation'\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\n# --------------------------- #\n\ncitros = CitrosDB()\nn = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).get_counts()\nprint(n)\n")),(0,i.kt)("h2",{id:"number-of-messages-in-each-simulation"},"Number of Messages in Each Simulation"),(0,i.kt)("p",null,"Get number of messages in the batch 'my_batch', created by simulation 'my_simulation', for the topic 'my_topic' for each simulation id (sid):"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},"from citros import CitrosDB\n\n# --- adjust to your data --- #\nsimulation_name = 'my_simulation'\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\n# --------------------------- #\n\ncitros = CitrosDB()\nn_by_sid = citros.simulation(simulation_name).batch(batch_name).topic(topic_name).get_counts(group_by='sid')\nfor item in n_by_sid:\n    print(f'sid = {item[0]}, n = {item[1]}')\n")))}p.isMDXComponent=!0}}]);
"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[7657],{3905:(t,e,a)=>{a.d(e,{Zo:()=>l,kt:()=>d});var n=a(7294);function o(t,e,a){return e in t?Object.defineProperty(t,e,{value:a,enumerable:!0,configurable:!0,writable:!0}):t[e]=a,t}function i(t,e){var a=Object.keys(t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(t);e&&(n=n.filter((function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable}))),a.push.apply(a,n)}return a}function c(t){for(var e=1;e<arguments.length;e++){var a=null!=arguments[e]?arguments[e]:{};e%2?i(Object(a),!0).forEach((function(e){o(t,e,a[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(a)):i(Object(a)).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(a,e))}))}return t}function r(t,e){if(null==t)return{};var a,n,o=function(t,e){if(null==t)return{};var a,n,o={},i=Object.keys(t);for(n=0;n<i.length;n++)a=i[n],e.indexOf(a)>=0||(o[a]=t[a]);return o}(t,e);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(t);for(n=0;n<i.length;n++)a=i[n],e.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(t,a)&&(o[a]=t[a])}return o}var s=n.createContext({}),m=function(t){var e=n.useContext(s),a=e;return t&&(a="function"==typeof t?t(e):c(c({},e),t)),a},l=function(t){var e=m(t.components);return n.createElement(s.Provider,{value:e},t.children)},u="mdxType",p={inlineCode:"code",wrapper:function(t){var e=t.children;return n.createElement(n.Fragment,{},e)}},_=n.forwardRef((function(t,e){var a=t.components,o=t.mdxType,i=t.originalType,s=t.parentName,l=r(t,["components","mdxType","originalType","parentName"]),u=m(a),_=o,d=u["".concat(s,".").concat(_)]||u[_]||p[_]||i;return a?n.createElement(d,c(c({ref:e},l),{},{components:a})):n.createElement(d,c({ref:e},l))}));function d(t,e){var a=arguments,o=e&&e.mdxType;if("string"==typeof t||o){var i=a.length,c=new Array(i);c[0]=_;var r={};for(var s in e)hasOwnProperty.call(e,s)&&(r[s]=e[s]);r.originalType=t,r[u]="string"==typeof t?t:o,c[1]=r;for(var m=2;m<i;m++)c[m]=a[m];return n.createElement.apply(null,c)}return n.createElement.apply(null,a)}_.displayName="MDXCreateElement"},5772:(t,e,a)=>{a.r(e),a.d(e,{assets:()=>s,contentTitle:()=>c,default:()=>p,frontMatter:()=>i,metadata:()=>r,toc:()=>m});var n=a(7462),o=(a(7294),a(3905));const i={toc_max_heading_level:4,hide_title:!0,sidebar_label:"Batch Content"},c="Batch Content",r={unversionedId:"snippets_doc/data_access/snippets_batch_content",id:"version-v0.9.1/snippets_doc/data_access/snippets_batch_content",title:"Batch Content",description:"General Information",source:"@site/docs_data_analysis_versioned_docs/version-v0.9.1/snippets_doc/data_access/snippets_batch_content.md",sourceDirName:"snippets_doc/data_access",slug:"/snippets_doc/data_access/snippets_batch_content",permalink:"/docs/docs_data_analysis/snippets_doc/data_access/snippets_batch_content",draft:!1,tags:[],version:"v0.9.1",frontMatter:{toc_max_heading_level:4,hide_title:!0,sidebar_label:"Batch Content"},sidebar:"dataAnalysisSidebar",previous:{title:"Users",permalink:"/docs/docs_data_analysis/snippets_doc/data_access/snippets_users"},next:{title:"Query Data",permalink:"/docs/docs_data_analysis/snippets_doc/data_access/snippets_query_data"}},s={},m=[{value:"General Information",id:"general-information",level:2},{value:"Topic Overview",id:"topic-overview",level:2},{value:"Data Structure",id:"data-structure",level:2},{value:"Maximum Value",id:"maximum-value",level:2},{value:"Minimum Value",id:"minimum-value",level:2},{value:"Indices of the Minimum and Maximum Values",id:"indices-of-the-minimum-and-maximum-values",level:2},{value:"List of Unique Values",id:"list-of-unique-values",level:2},{value:"Number of Messages",id:"number-of-messages",level:2},{value:"Number of Messages in Each Simulation",id:"number-of-messages-in-each-simulation",level:2}],l={toc:m},u="wrapper";function p(t){let{components:e,...a}=t;return(0,o.kt)(u,(0,n.Z)({},l,a,{components:e,mdxType:"MDXLayout"}),(0,o.kt)("h1",{id:"batch-content"},"Batch Content"),(0,o.kt)("h2",{id:"general-information"},"General Information"),(0,o.kt)("p",null,"Show information about batch 'my_batch':"),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-python"},"from citros_data_analysis import data_access as da\n\n# --- adjust to your data --- #\nbatch_name = 'my_batch'\n# --------------------------- #\n\ncitros = da.CitrosDB()\ncitros.batch(batch_name).info().print()\n")),(0,o.kt)("h2",{id:"topic-overview"},"Topic Overview"),(0,o.kt)("p",null,"Show information and structure of the data of the topic 'my_topic' from the batch 'my_batch':"),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-python"},"from citros_data_analysis import data_access as da\n\n# --- adjust to your data --- #\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\n# --------------------------- #\n\ncitros = da.CitrosDB()\ncitros.batch(batch_name).topic(topic_name).info().print()\n")),(0,o.kt)("h2",{id:"data-structure"},"Data Structure"),(0,o.kt)("p",null,"Show table with data structure for topic 'my_topic' of  the batch 'my_batch' :"),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-python"},"from citros_data_analysis import data_access as da\n\n# --- adjust to your data --- #\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\n# --------------------------- #\n\ncitros = da.CitrosDB()\ncitros.batch(batch_name).topic(topic_name).get_data_structure()\n")),(0,o.kt)("h2",{id:"maximum-value"},"Maximum Value"),(0,o.kt)("p",null,"Get maximum value of the column 'my_column' for the topic 'my_topic' from the batch 'my_batch':"),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-python"},"from citros_data_analysis import data_access as da\n\n# --- adjust to your data --- #\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\ncolumn_name = 'my_column'\n# --------------------------- #\n\ncitros = da.CitrosDB()\nmax_value = citros.batch(batch_name).topic(topic_name).get_max_value(column_name)\nprint(max_value)\n")),(0,o.kt)("h2",{id:"minimum-value"},"Minimum Value"),(0,o.kt)("p",null,"Get minimum value of the column 'my_column' for the topic 'my_topic' from the batch 'my_batch':"),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-python"},"from citros_data_analysis import data_access as da\n\n# --- adjust to your data --- #\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\ncolumn_name = 'my_column'\n# --------------------------- #\n\ncitros = da.CitrosDB()\nmin_value = citros.batch(batch_name).topic(topic_name).get_min_value(column_name)\nprint(min_value)\n")),(0,o.kt)("h2",{id:"indices-of-the-minimum-and-maximum-values"},"Indices of the Minimum and Maximum Values"),(0,o.kt)("p",null,"Get minimum and maximum values of the column 'my_column' and corresponding to them values of sid and rid for the topic 'my_topic' from the batch 'my_batch':"),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-python"},"from citros_data_analysis import data_access as da\n\n# --- adjust to your data --- #\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\ncolumn_name = 'my_column'\n# --------------------------- #\n\ncitros = da.CitrosDB()\nmax_value, sid_max, rid_max = citros.batch(batch_name).topic(topic_name).get_max_value(column_name, return_index = True)\nmin_value, sid_min, rid_min = citros.batch(batch_name).topic(topic_name).get_min_value(column_name, return_index = True)\nprint(f\"maximum value of the column {column_name} = {max_value}, corresponding sid = {sid_max}, rid = {rid_max}\")\nprint(f\"minimum value of the column {column_name} = {min_value}, corresponding sid = {sid_min}, rid = {rid_min}\")\n")),(0,o.kt)("h2",{id:"list-of-unique-values"},"List of Unique Values"),(0,o.kt)("p",null,"Get list of simulation ids (sid) for the topic 'my_topic' from the batch 'my_batch':"),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-python"},"from citros_data_analysis import data_access as da\n\n# --- adjust to your data --- #\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\n# --------------------------- #\n\ncitros = da.CitrosDB()\nsid_list = citros.batch(batch_name).topic(topic_name).get_unique_values('sid')\nprint(sid_list)\n")),(0,o.kt)("h2",{id:"number-of-messages"},"Number of Messages"),(0,o.kt)("p",null,"Get number of messages in the batch 'my_batch' for the topic 'my_topic':"),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-python"},"from citros_data_analysis import data_access as da\n\n# --- adjust to your data --- #\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\n# --------------------------- #\n\ncitros = da.CitrosDB()\nn = citros.batch(batch_name).topic(topic_name).get_counts()\nprint(n)\n")),(0,o.kt)("h2",{id:"number-of-messages-in-each-simulation"},"Number of Messages in Each Simulation"),(0,o.kt)("p",null,"Get number of messages in the batch 'my_batch' for the topic 'my_topic' for each simulation id (sid):"),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-python"},"from citros_data_analysis import data_access as da\n\n# --- adjust to your data --- #\nbatch_name = 'my_batch'\ntopic_name = 'my_topic'\n# --------------------------- #\n\ncitros = da.CitrosDB()\nn_by_sid = citros.batch(batch_name).topic(topic_name).get_counts(group_by='sid')\nprint(n_by_sid)\n")))}p.isMDXComponent=!0}}]);
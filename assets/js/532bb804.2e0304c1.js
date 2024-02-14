"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[27235],{3905:(t,a,e)=>{e.d(a,{Zo:()=>p,kt:()=>k});var n=e(67294);function s(t,a,e){return a in t?Object.defineProperty(t,a,{value:e,enumerable:!0,configurable:!0,writable:!0}):t[a]=e,t}function r(t,a){var e=Object.keys(t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(t);a&&(n=n.filter((function(a){return Object.getOwnPropertyDescriptor(t,a).enumerable}))),e.push.apply(e,n)}return e}function i(t){for(var a=1;a<arguments.length;a++){var e=null!=arguments[a]?arguments[a]:{};a%2?r(Object(e),!0).forEach((function(a){s(t,a,e[a])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(e)):r(Object(e)).forEach((function(a){Object.defineProperty(t,a,Object.getOwnPropertyDescriptor(e,a))}))}return t}function o(t,a){if(null==t)return{};var e,n,s=function(t,a){if(null==t)return{};var e,n,s={},r=Object.keys(t);for(n=0;n<r.length;n++)e=r[n],a.indexOf(e)>=0||(s[e]=t[e]);return s}(t,a);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(t);for(n=0;n<r.length;n++)e=r[n],a.indexOf(e)>=0||Object.prototype.propertyIsEnumerable.call(t,e)&&(s[e]=t[e])}return s}var l=n.createContext({}),c=function(t){var a=n.useContext(l),e=a;return t&&(e="function"==typeof t?t(a):i(i({},a),t)),e},p=function(t){var a=c(t.components);return n.createElement(l.Provider,{value:a},t.children)},m="mdxType",u={inlineCode:"code",wrapper:function(t){var a=t.children;return n.createElement(n.Fragment,{},a)}},d=n.forwardRef((function(t,a){var e=t.components,s=t.mdxType,r=t.originalType,l=t.parentName,p=o(t,["components","mdxType","originalType","parentName"]),m=c(e),d=s,k=m["".concat(l,".").concat(d)]||m[d]||u[d]||r;return e?n.createElement(k,i(i({ref:a},p),{},{components:e})):n.createElement(k,i({ref:a},p))}));function k(t,a){var e=arguments,s=a&&a.mdxType;if("string"==typeof t||s){var r=e.length,i=new Array(r);i[0]=d;var o={};for(var l in a)hasOwnProperty.call(a,l)&&(o[l]=a[l]);o.originalType=t,o[m]="string"==typeof t?t:s,i[1]=o;for(var c=2;c<r;c++)i[c]=e[c];return n.createElement.apply(null,i)}return n.createElement.apply(null,e)}d.displayName="MDXCreateElement"},73904:(t,a,e)=>{e.r(a),e.d(a,{assets:()=>l,contentTitle:()=>i,default:()=>u,frontMatter:()=>r,metadata:()=>o,toc:()=>c});var n=e(87462),s=(e(67294),e(3905));const r={toc_max_heading_level:4,hide_title:!0,sidebar_label:"Batch Content",description:"Information about batch content and topics",sidebar_position:3},i="Batch Content",o={unversionedId:"data_analysis/data_access/batch_content",id:"version-0.2.52/data_analysis/data_access/batch_content",title:"Batch Content",description:"Information about batch content and topics",source:"@site/versioned_docs/version-0.2.52/data_analysis/data_access/batch_content.md",sourceDirName:"data_analysis/data_access",slug:"/data_analysis/data_access/batch_content",permalink:"/docs/0.2.52/data_analysis/data_access/batch_content",draft:!1,tags:[],version:"0.2.52",sidebarPosition:3,frontMatter:{toc_max_heading_level:4,hide_title:!0,sidebar_label:"Batch Content",description:"Information about batch content and topics",sidebar_position:3},sidebar:"gettingStartedSidebar",previous:{title:"Simulations and Batches",permalink:"/docs/0.2.52/data_analysis/data_access/batch_overview"},next:{title:"Query Data",permalink:"/docs/0.2.52/data_analysis/data_access/query_data"}},l={},c=[{value:"Data Overview",id:"data-overview",level:2},{value:"Data Structure",id:"data-structure",level:2}],p={toc:c},m="wrapper";function u(t){let{components:a,...e}=t;return(0,s.kt)(m,(0,n.Z)({},p,e,{components:a,mdxType:"MDXLayout"}),(0,s.kt)("h1",{id:"batch-content"},"Batch Content"),(0,s.kt)("p",null,"In the ",(0,s.kt)("em",{parentName:"p"},"batch")," different simulation runs are identified by their ",(0,s.kt)("em",{parentName:"p"},"sid")," numbers, with each step of the simulation being sequentially numbered by ",(0,s.kt)("em",{parentName:"p"},"rid"),". Batches typically contain multiple topics that encapsulate related datasets."),(0,s.kt)("p",null,"Each batch contains the following columns:"),(0,s.kt)("table",null,(0,s.kt)("thead",{parentName:"table"},(0,s.kt)("tr",{parentName:"thead"},(0,s.kt)("th",{parentName:"tr",align:null}),(0,s.kt)("th",{parentName:"tr",align:null},"sid"),(0,s.kt)("th",{parentName:"tr",align:null},"rid"),(0,s.kt)("th",{parentName:"tr",align:null},"time"),(0,s.kt)("th",{parentName:"tr",align:null},"topic"),(0,s.kt)("th",{parentName:"tr",align:null},"type"),(0,s.kt)("th",{parentName:"tr",align:null},"data"))),(0,s.kt)("tbody",{parentName:"table"},(0,s.kt)("tr",{parentName:"tbody"},(0,s.kt)("td",{parentName:"tr",align:null},"description"),(0,s.kt)("td",{parentName:"tr",align:null},"simulation id"),(0,s.kt)("td",{parentName:"tr",align:null},"run id"),(0,s.kt)("td",{parentName:"tr",align:null},"ros time message"),(0,s.kt)("td",{parentName:"tr",align:null},"topic name"),(0,s.kt)("td",{parentName:"tr",align:null},"type name"),(0,s.kt)("td",{parentName:"tr",align:null},"json-format data")),(0,s.kt)("tr",{parentName:"tbody"},(0,s.kt)("td",{parentName:"tr",align:null},"type"),(0,s.kt)("td",{parentName:"tr",align:null},"BIGINT"),(0,s.kt)("td",{parentName:"tr",align:null},"BIGINT"),(0,s.kt)("td",{parentName:"tr",align:null},"BIGINT"),(0,s.kt)("td",{parentName:"tr",align:null},"VARCHAR"),(0,s.kt)("td",{parentName:"tr",align:null},"VARCHAR"),(0,s.kt)("td",{parentName:"tr",align:null},"JSONB")))),(0,s.kt)("p",null,"Batch may have several ",(0,s.kt)("em",{parentName:"p"},"topic"),"s - to list them along with structure of the json-data column for the current batch the method ",(0,s.kt)("a",{parentName:"p",href:"/docs/0.2.52/data_analysis/data_access/batch_content#data-structure"},(0,s.kt)("strong",{parentName:"a"},"get_data_structure()"))," or ",(0,s.kt)("a",{parentName:"p",href:"/docs/0.2.52/data_analysis/data_access/batch_content#data-overview"},(0,s.kt)("strong",{parentName:"a"},"info()"))," is used. Initial parameters of the simulation are usually written under the topic ",(0,s.kt)("inlineCode",{parentName:"p"},"'/config'"),"."),(0,s.kt)("p",null,"Each simulation in the batch has its own id - ",(0,s.kt)("em",{parentName:"p"},"sid"),", and each message in the simulation is enumerated by run id - ",(0,s.kt)("em",{parentName:"p"},"rid"),"."),(0,s.kt)("p",null,"If there are infinite values in the data, they are stored as ",(0,s.kt)("span",{parentName:"p",className:"math math-inline"},(0,s.kt)("span",{parentName:"span",className:"katex"},(0,s.kt)("span",{parentName:"span",className:"katex-mathml"},(0,s.kt)("math",{parentName:"span",xmlns:"http://www.w3.org/1998/Math/MathML"},(0,s.kt)("semantics",{parentName:"math"},(0,s.kt)("mrow",{parentName:"semantics"},(0,s.kt)("mo",{parentName:"mrow"},"\xb1"),(0,s.kt)("mn",{parentName:"mrow"},"1"),(0,s.kt)("msup",{parentName:"mrow"},(0,s.kt)("mn",{parentName:"msup"},"0"),(0,s.kt)("mn",{parentName:"msup"},"308"))),(0,s.kt)("annotation",{parentName:"semantics",encoding:"application/x-tex"},"\\pm 10^{308}")))),(0,s.kt)("span",{parentName:"span",className:"katex-html","aria-hidden":"true"},(0,s.kt)("span",{parentName:"span",className:"base"},(0,s.kt)("span",{parentName:"span",className:"strut",style:{height:"0.8974em",verticalAlign:"-0.0833em"}}),(0,s.kt)("span",{parentName:"span",className:"mord"},"\xb1"),(0,s.kt)("span",{parentName:"span",className:"mord"},"1"),(0,s.kt)("span",{parentName:"span",className:"mord"},(0,s.kt)("span",{parentName:"span",className:"mord"},"0"),(0,s.kt)("span",{parentName:"span",className:"msupsub"},(0,s.kt)("span",{parentName:"span",className:"vlist-t"},(0,s.kt)("span",{parentName:"span",className:"vlist-r"},(0,s.kt)("span",{parentName:"span",className:"vlist",style:{height:"0.8141em"}},(0,s.kt)("span",{parentName:"span",style:{top:"-3.063em",marginRight:"0.05em"}},(0,s.kt)("span",{parentName:"span",className:"pstrut",style:{height:"2.7em"}}),(0,s.kt)("span",{parentName:"span",className:"sizing reset-size6 size3 mtight"},(0,s.kt)("span",{parentName:"span",className:"mord mtight"},(0,s.kt)("span",{parentName:"span",className:"mord mtight"},"308"))))))))))))),"."),(0,s.kt)("h2",{id:"data-overview"},"Data Overview"),(0,s.kt)("p",null,"To get the overview about the exact batch, say 'dynamics' from the simulation 'simulation_galactic_rotation', the function ",(0,s.kt)("a",{parentName:"p",href:"/docs/0.2.52/data_analysis/documentation/access/citros_db#access.citros_db.CitrosDB.info"},(0,s.kt)("strong",{parentName:"a"},"info()"))," is used:"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> from citros import CitrosDB\n>>> citros = CitrosDB()\n>>> citros.simulation('simulation_galactic_rotation').batch('dynamics').info()\n")),(0,s.kt)("p",null,"It returns dictionary, that contains:"),(0,s.kt)("ul",null,(0,s.kt)("li",{parentName:"ul"},"'size': size of the selected data"),(0,s.kt)("li",{parentName:"ul"},"'sid_count': number of sids"),(0,s.kt)("li",{parentName:"ul"},"'sid_list': list of the sids"),(0,s.kt)("li",{parentName:"ul"},"'topic_count': number of topics"),(0,s.kt)("li",{parentName:"ul"},"'topic_list': list of topics"),(0,s.kt)("li",{parentName:"ul"},"'message_count': number of messages")),(0,s.kt)("p",null,"The result is a ",(0,s.kt)("a",{parentName:"p",href:"/docs/0.2.52/data_analysis/documentation/access/citros_dict#access.citros_dict.CitrosDict"},(0,s.kt)("strong",{parentName:"a"},"CitrosDict"))," object, that inherits behavior of an ordinary python dictionary, but has some additional methods."),(0,s.kt)("details",null,(0,s.kt)("summary",null,"more about CitrosDict:"),(0,s.kt)("p",null,(0,s.kt)("a",{parentName:"p",href:"/docs/0.2.52/data_analysis/documentation/access/citros_dict#access.citros_dict.CitrosDict"},(0,s.kt)("strong",{parentName:"a"},"CitrosDict"))," object can be converted to json string by the method ",(0,s.kt)("a",{parentName:"p",href:"/docs/0.2.52/data_analysis/documentation/access/citros_dict#access.citros_dict.CitrosDict.to_json"},(0,s.kt)("strong",{parentName:"a"},"to_json()")),":"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> citros.simulation('simulation_galactic_rotation').batch('dynamics').info().to_json()\n")),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-js"},'{\n  "size": "534 kB",\n  "sid_count": 3,\n  "sid_list": [\n    1,\n    2,\n    3\n  ],\n  "topic_count": 4,\n  "topic_list": [\n    "A",\n    "B",\n    "C",\n    "D"\n  ],\n  "message_count": 2000\n}\n')),(0,s.kt)("p",null,"or printed by the method ",(0,s.kt)("a",{parentName:"p",href:"/docs/0.2.52/data_analysis/documentation/access/citros_dict#access.citros_dict.CitrosDict.print"},(0,s.kt)("strong",{parentName:"a"},"print()")),":"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> citros.simulation('simulation_galactic_rotation').batch('dynamics').info().print()\n")),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-js"},"{\n 'size': '534 kB',\n 'sid_count': 3,\n 'sid_list': [1, 2, 3],\n 'topic_count': 4,\n 'topic_list': ['A', 'B', 'C', 'D'],\n 'message_count': 2000\n}\n"))),(0,s.kt)("admonition",{type:"note"},(0,s.kt)("p",{parentName:"admonition"},"It is not necessary to call method ",(0,s.kt)("a",{parentName:"p",href:"/docs/0.2.52/data_analysis/data_access/batch_overview#setting-batch"},(0,s.kt)("strong",{parentName:"a"},"batch()"))," and ",(0,s.kt)("a",{parentName:"p",href:"/docs/0.2.52/data_analysis/data_access/batch_overview#setting-simulation"},(0,s.kt)("strong",{parentName:"a"},"simulation()"))," every time to set batch and simulation names. By parameter ",(0,s.kt)("inlineCode",{parentName:"p"},"inplace")," they can be set to current ",(0,s.kt)("a",{parentName:"p",href:"/docs/0.2.52/data_analysis/data_access/getting_started#connection-to-the-database"},(0,s.kt)("strong",{parentName:"a"},"CitrosDB"))," object:"),(0,s.kt)("pre",{parentName:"admonition"},(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> citros.simulation('simulation_galactic_rotation', inplace = True)\n>>> citros.batch('dynamics', inplace = True)\n>>> print(f\"current batch name: {citros.get_batch_name()}\")\n")),(0,s.kt)("pre",{parentName:"admonition"},(0,s.kt)("code",{parentName:"pre",className:"language-text"},"current batch name: dynamics\n"))),(0,s.kt)("p",null,"If specific sid is set, ",(0,s.kt)("a",{parentName:"p",href:"/docs/0.2.52/data_analysis/documentation/access/citros_db#access.citros_db.CitrosDB.info"},(0,s.kt)("strong",{parentName:"a"},"citros.info()"))," also appends dictionary 'sids', with the following structure:"),(0,s.kt)("ul",null,(0,s.kt)("li",{parentName:"ul"},"'sids':",(0,s.kt)("ul",{parentName:"li"},(0,s.kt)("li",{parentName:"ul"},"<sid, int>:",(0,s.kt)("ul",{parentName:"li"},(0,s.kt)("li",{parentName:"ul"},"'topics': ",(0,s.kt)("ul",{parentName:"li"},(0,s.kt)("li",{parentName:"ul"},"<topic_name, str>:",(0,s.kt)("ul",{parentName:"li"},(0,s.kt)("li",{parentName:"ul"},"'message_count': number of messages"),(0,s.kt)("li",{parentName:"ul"},"'start_time': time when simulation started"),(0,s.kt)("li",{parentName:"ul"},"'end_time': time when simulation ended"),(0,s.kt)("li",{parentName:"ul"},"'duration': duration of the simulation process"),(0,s.kt)("li",{parentName:"ul"},"'frequency': frequency of the simulation process ('message_count'/ 'duration', in Hz)")))))))))),(0,s.kt)("p",null,"sid may be passed during ",(0,s.kt)("a",{parentName:"p",href:"/docs/0.2.52/data_analysis/data_access/getting_started#connection-to-the-database"},(0,s.kt)("strong",{parentName:"a"},"CitrosDB")," initialization")," or by ",(0,s.kt)("a",{parentName:"p",href:"/docs/0.2.52/data_analysis/data_access/query_data#sid-constraints"},(0,s.kt)("strong",{parentName:"a"},"citros.sid()"))," method."),(0,s.kt)("p",null,"Let's create ",(0,s.kt)("a",{parentName:"p",href:"/docs/0.2.52/data_analysis/data_access/getting_started#connection-to-the-database"},(0,s.kt)("strong",{parentName:"a"},"CitrosDB"))," object, setting the simulation name as 'simulation_galactic_rotation' and batch name as 'dynamics':"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> citros = CitrosDB(simulation = 'simulation_galactic_rotation', batch = 'dynamics')\n")),(0,s.kt)("p",null,"To get information about data with sid = 1 or 2 and print it:"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> citros.sid([1,2]).info().print()\n")),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-js"},"{\n 'size': '365 kB',\n 'sid_count': 2,\n 'sid_list': [1, 2],\n 'topic_count': 4,\n 'topic_list': ['A', 'B', 'C', 'D'],\n 'message_count': 1369,\n 'sids': {\n   1: {\n     'topics': {\n       'A': {\n         'message_count': 155,\n         'start_time': 312751159,\n         'end_time': 100484965889,\n         'duration': 100172214730,\n         'frequency': 1.547\n       },\n       'B': {\n         'message_count': 178,\n         'start_time': 344594155,\n         'end_time': 100752013600,\n         'duration': 100407419445,\n         'frequency': 1.773\n       },\n       'C': {\n...\n       }\n     }\n   }\n }\n}\n")),(0,s.kt)("p",null,"To set the specific topic, method ",(0,s.kt)("a",{parentName:"p",href:"/docs/0.2.52/data_analysis/documentation/access/citros_db#access.citros_db.CitrosDB.topic"},(0,s.kt)("strong",{parentName:"a"},"topic()"))," is used.\nThis way, dictionary 'topics' is appended:"),(0,s.kt)("ul",null,(0,s.kt)("li",{parentName:"ul"},"'topics':",(0,s.kt)("ul",{parentName:"li"},(0,s.kt)("li",{parentName:"ul"},"<topic_name, str>:",(0,s.kt)("ul",{parentName:"li"},(0,s.kt)("li",{parentName:"ul"},"'type': type"),(0,s.kt)("li",{parentName:"ul"},"'data_structure': structure of the data"),(0,s.kt)("li",{parentName:"ul"},"'message_count': number of messages")))))),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> citros.topic('A').info().print()\n")),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-js"},"{\n 'size': '126 kB',\n 'sid_count': 3,\n 'sid_list': [1, 2, 3],\n 'topic_count': 1,\n 'topic_list': ['A'],\n 'message_count': 474,\n 'topics': {\n   'A': {\n     'type': 'a',\n     'data_structure': {\n       'data': {\n         'x': {\n           'x_1': 'float',\n           'x_2': 'float',\n           'x_3': 'float'\n         },\n         'note': 'list',\n         'time': 'float',\n         'height': 'float'\n       }\n     },\n     'message_count': 474\n   }\n }\n}\n")),(0,s.kt)("p",null,'If the topic has multiple types with the same data structure, they are presented in \'type\' as a list. If the types have different data structures, they are grouped by their data structure types and numbered as "type_group_0", "type_group_1", and so on:'),(0,s.kt)("ul",null,(0,s.kt)("li",{parentName:"ul"},"'topics':",(0,s.kt)("ul",{parentName:"li"},(0,s.kt)("li",{parentName:"ul"},"<topic_name, str>:",(0,s.kt)("ul",{parentName:"li"},(0,s.kt)("li",{parentName:"ul"},'"type_group_0":',(0,s.kt)("ul",{parentName:"li"},(0,s.kt)("li",{parentName:"ul"},"'type': type"),(0,s.kt)("li",{parentName:"ul"},"'data_structure': structure of the data"),(0,s.kt)("li",{parentName:"ul"},"'message_count': number of messages"))),(0,s.kt)("li",{parentName:"ul"},'"type_group_1":\n...')))))),(0,s.kt)("p",null,"The specific piece of information may be achieved by the keywords of the ",(0,s.kt)("a",{parentName:"p",href:"/docs/0.2.52/data_analysis/documentation/access/citros_dict#access.citros_dict.CitrosDict"},(0,s.kt)("strong",{parentName:"a"},"CitrosDict")),", obtained by ",(0,s.kt)("a",{parentName:"p",href:"/docs/0.2.52/data_analysis/documentation/access/citros_db#access.citros_db.CitrosDB.info"},(0,s.kt)("strong",{parentName:"a"},"info()"))," method."),(0,s.kt)("details",null,(0,s.kt)("summary",null,"Examples"),(0,s.kt)("ul",null,(0,s.kt)("li",{parentName:"ul"},"Get total number of messages for sid = 1 or 2:")),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},"#get information about sid equals 1 or 2 and assign the result to the variable 'inf_12':\ninf_12 = citros.sid([1,2]).info()\n\n#access number of messages by key 'message_count' and assign it to 'num':\nnum = inf_12['message_count']\n\n#print:\nprint(f'total number of messages where sid = 1 or 2: {num}')\n")),(0,s.kt)("p",null,"The result is:"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},"total number of messages where sid = 1 or 2: 1369\n")),(0,s.kt)("ul",null,(0,s.kt)("li",{parentName:"ul"},"Get number of messages for topic 'A' for each of these sids:")),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},"#for sid equals 1, for topic 'A' get number of messages by 'message_count':\nnum_1 = inf_12['sids'][1]['topics']['A']['message_count']\n\n#get number of messages for sid = 2, topic 'A':\nnum_2 = inf_12['sids'][2]['topics']['A']['message_count']\n\n#print both numbers:\nprint(f'Number of messages in \"A\" for sid = 1: {num_1}, for sid = 2: {num_2}')\n")),(0,s.kt)("p",null,"The output:"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-text"},'Number of messages in "A" for sid = 1: 155, for sid = 2: 164\n')),(0,s.kt)("ul",null,(0,s.kt)("li",{parentName:"ul"},"Get structure of the topic 'A' and the total number of messages for this topic:")),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},"#get information about topic 'A' and assign the resulting dictionary to the variable 'inf_A'\ninf_A = citros.topic('A').info()\n\n#get number of messages by 'message_count' keyword:\nnum = inf_A['message_count']\n\n#print number of messages:\nprint(f'total number of messages in topic \"A\": {num}')\n\n#print structure of the json-data column:\ninf_A['topics']['A']['data_structure']['data'].print()\n")),(0,s.kt)("p",null,"The result is:"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-js"},"total number of messages in topic \"A\": 474\n{\n 'x': {\n   'x_1': 'float',\n   'x_2': 'float',\n   'x_3': 'float'\n },\n 'note': 'list',\n 'time': 'float',\n 'height': 'float'\n}\n"))),(0,s.kt)("h2",{id:"data-structure"},"Data Structure"),(0,s.kt)("p",null,(0,s.kt)("a",{parentName:"p",href:"/docs/0.2.52/data_analysis/documentation/access/citros_db#access.citros_db.CitrosDB.get_data_structure"},(0,s.kt)("strong",{parentName:"a"},"get_data_structure()"))," method of the ",(0,s.kt)("a",{parentName:"p",href:"/docs/0.2.52/data_analysis/data_access/getting_started#connection-to-the-database"},(0,s.kt)("strong",{parentName:"a"},"CitrosDB"))," object may be used to display json-data structure of the exact batch for the specific topics, set by ",(0,s.kt)("a",{parentName:"p",href:"/docs/0.2.52/data_analysis/documentation/access/citros_db#access.citros_db.CitrosDB.topic"},(0,s.kt)("strong",{parentName:"a"},"topic"))," or listed in ",(0,s.kt)("inlineCode",{parentName:"p"},"topic"),":"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> citros.batch('dynamics').topic(['A', 'C']).get_data_structure()\n")),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-text"},"+-------+------+-----------------+\n| topic | type | data            |\n+-------+------+-----------------+\n|     A |    a | {               |\n|       |      |   x: {          |\n|       |      |     x_1: float, |\n|       |      |     x_2: float, |\n|       |      |     x_3: float  |\n|       |      |   },            |\n|       |      |   note: list,   |\n|       |      |   time: float,  |\n|       |      |   height: float |\n|       |      | }               |\n+-------+------+-----------------+\n|     C |    c | {               |\n|       |      |   x: {          |\n|       |      |     x_1: float, |\n|       |      |     x_2: float, |\n|       |      |     x_3: float  |\n|       |      |   },            |\n|       |      |   note: list,   |\n|       |      |   time: float,  |\n|       |      |   height: float |\n|       |      | }               |\n+-------+------+-----------------+\n")),(0,s.kt)("p",null,"To get the result for all the existing topics, leave ",(0,s.kt)("inlineCode",{parentName:"p"},"topic")," = None. Also let's set batch to this ",(0,s.kt)("a",{parentName:"p",href:"/docs/0.2.52/data_analysis/data_access/getting_started#connection-to-the-database"},(0,s.kt)("strong",{parentName:"a"},"CitrosDB"))," object in advance:"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> citros.batch('dynamics', inplace = True)\n>>> citros.get_data_structure()\n")),(0,s.kt)("details",null,(0,s.kt)("summary",null,"The result:"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-text"},"+-------+------+-----------------+\n| topic | type | data            |\n+-------+------+-----------------+\n|     A |    a | {               |\n|       |      |   x: {          |\n|       |      |     x_1: float, |\n|       |      |     x_2: float, |\n|       |      |     x_3: float  |\n|       |      |   },            |\n|       |      |   note: list,   |\n|       |      |   time: float,  |\n|       |      |   height: float |\n|       |      | }               |\n+-------+------+-----------------+\n|     B |    b | {               |\n|       |      |   x: {          |\n|       |      |     x_1: float, |\n|       |      |     x_2: float, |\n|       |      |     x_3: float  |\n|       |      |   },            |\n|       |      |   note: list,   |\n|       |      |   time: float,  |\n|       |      |   height: float |\n|       |      | }               |\n+-------+------+-----------------+\n|     C |    c | {               |\n|       |      |   x: {          |\n|       |      |     x_1: float, |\n|       |      |     x_2: float, |\n|       |      |     x_3: float  |\n|       |      |   },            |\n|       |      |   note: list,   |\n|       |      |   time: float,  |\n|       |      |   height: float |\n|       |      | }               |\n+-------+------+-----------------+\n"))))}u.isMDXComponent=!0}}]);
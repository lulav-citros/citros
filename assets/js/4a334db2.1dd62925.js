"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[4566],{3905:(t,e,a)=>{a.d(e,{Zo:()=>p,kt:()=>_});var n=a(7294);function s(t,e,a){return e in t?Object.defineProperty(t,e,{value:a,enumerable:!0,configurable:!0,writable:!0}):t[e]=a,t}function o(t,e){var a=Object.keys(t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(t);e&&(n=n.filter((function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable}))),a.push.apply(a,n)}return a}function r(t){for(var e=1;e<arguments.length;e++){var a=null!=arguments[e]?arguments[e]:{};e%2?o(Object(a),!0).forEach((function(e){s(t,e,a[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(a)):o(Object(a)).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(a,e))}))}return t}function i(t,e){if(null==t)return{};var a,n,s=function(t,e){if(null==t)return{};var a,n,s={},o=Object.keys(t);for(n=0;n<o.length;n++)a=o[n],e.indexOf(a)>=0||(s[a]=t[a]);return s}(t,e);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(t);for(n=0;n<o.length;n++)a=o[n],e.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(t,a)&&(s[a]=t[a])}return s}var c=n.createContext({}),l=function(t){var e=n.useContext(c),a=e;return t&&(a="function"==typeof t?t(e):r(r({},e),t)),a},p=function(t){var e=l(t.components);return n.createElement(c.Provider,{value:e},t.children)},u="mdxType",d={inlineCode:"code",wrapper:function(t){var e=t.children;return n.createElement(n.Fragment,{},e)}},m=n.forwardRef((function(t,e){var a=t.components,s=t.mdxType,o=t.originalType,c=t.parentName,p=i(t,["components","mdxType","originalType","parentName"]),u=l(a),m=s,_=u["".concat(c,".").concat(m)]||u[m]||d[m]||o;return a?n.createElement(_,r(r({ref:e},p),{},{components:a})):n.createElement(_,r({ref:e},p))}));function _(t,e){var a=arguments,s=e&&e.mdxType;if("string"==typeof t||s){var o=a.length,r=new Array(o);r[0]=m;var i={};for(var c in e)hasOwnProperty.call(e,c)&&(i[c]=e[c]);i.originalType=t,i[u]="string"==typeof t?t:s,r[1]=i;for(var l=2;l<o;l++)r[l]=a[l];return n.createElement.apply(null,r)}return n.createElement.apply(null,a)}m.displayName="MDXCreateElement"},7541:(t,e,a)=>{a.r(e),a.d(e,{assets:()=>c,contentTitle:()=>r,default:()=>d,frontMatter:()=>o,metadata:()=>i,toc:()=>l});var n=a(7462),s=(a(7294),a(3905));const o={toc_max_heading_level:4,hide_title:!0,sidebar_label:"Batch Content",description:"Information about batch content and topics",sidebar_position:5},r="Batch Content",i={unversionedId:"data_access/batch_content",id:"data_access/batch_content",title:"Batch Content",description:"Information about batch content and topics",source:"@site/docs_data_analysis/data_access/batch_content.md",sourceDirName:"data_access",slug:"/data_access/batch_content",permalink:"/docs_data_analysis/next/data_access/batch_content",draft:!1,tags:[],version:"current",sidebarPosition:5,frontMatter:{toc_max_heading_level:4,hide_title:!0,sidebar_label:"Batch Content",description:"Information about batch content and topics",sidebar_position:5},sidebar:"dataAnalysisSidebar",previous:{title:"Users Overview",permalink:"/docs_data_analysis/next/data_access/users_overview"},next:{title:"Query Data",permalink:"/docs_data_analysis/next/data_access/query_data"}},c={},l=[{value:"Data Overview",id:"data-overview",level:2},{value:"Data Structure",id:"data-structure",level:2}],p={toc:l},u="wrapper";function d(t){let{components:e,...a}=t;return(0,s.kt)(u,(0,n.Z)({},p,a,{components:e,mdxType:"MDXLayout"}),(0,s.kt)("h1",{id:"batch-content"},"Batch Content"),(0,s.kt)("h2",{id:"data-overview"},"Data Overview"),(0,s.kt)("p",null,"To get the overview about the exact batch, say 'dynamics', the function ",(0,s.kt)("a",{parentName:"p",href:"/docs_data_analysis/next/documentation/data_access/citros_db#citros_data_analysis.data_access.citros_db.CitrosDB.info"},(0,s.kt)("strong",{parentName:"a"},"info()"))," is used:"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> citros.batch('dynamics').info()\n")),(0,s.kt)("p",null,"It returns dictionary, that contains:"),(0,s.kt)("ul",null,(0,s.kt)("li",{parentName:"ul"},"'size': size of the selected data"),(0,s.kt)("li",{parentName:"ul"},"'sid_count': number of sids"),(0,s.kt)("li",{parentName:"ul"},"'sid_list': list of the sids"),(0,s.kt)("li",{parentName:"ul"},"'topic_count': number of topics"),(0,s.kt)("li",{parentName:"ul"},"'topic_list': list of topics"),(0,s.kt)("li",{parentName:"ul"},"'message_count': number of messages")),(0,s.kt)("p",null,"The result is a ",(0,s.kt)("a",{parentName:"p",href:"/docs_data_analysis/next/documentation/data_access/citros_dict#citros_data_analysis.data_access.citros_dict.CitrosDict"},(0,s.kt)("strong",{parentName:"a"},"CitrosDict"))," object, that inherits behavior of an ordinary python dictionary, but has some additional methods."),(0,s.kt)("details",null,(0,s.kt)("summary",null,"more about CitrosDict:"),(0,s.kt)("p",null,(0,s.kt)("a",{parentName:"p",href:"/docs_data_analysis/next/documentation/data_access/citros_dict#citros_data_analysis.data_access.citros_dict.CitrosDict"},(0,s.kt)("strong",{parentName:"a"},"CitrosDict"))," object can be converted to json string by the method ",(0,s.kt)("a",{parentName:"p",href:"/docs_data_analysis/next/documentation/data_access/citros_dict#citros_data_analysis.data_access.citros_dict.CitrosDict.to_json"},(0,s.kt)("strong",{parentName:"a"},"to_json()")),":"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> citros.batch('dynamics').info().to_json()\n")),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-js"},'{\n  "size": "534 kB",\n  "sid_count": 3,\n  "sid_list": [\n    1,\n    2,\n    3\n  ],\n  "topic_count": 4,\n  "topic_list": [\n    "A",\n    "B",\n    "C",\n    "D"\n  ],\n  "message_count": 2000\n}\n')),(0,s.kt)("p",null,"or printed by the method ",(0,s.kt)("a",{parentName:"p",href:"/docs_data_analysis/next/documentation/data_access/citros_dict#citros_data_analysis.data_access.citros_dict.CitrosDict.print"},(0,s.kt)("strong",{parentName:"a"},"print()")),":"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> citros.batch('dynamics').info().print()\n")),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-js"},"{\n 'size': '534 kB',\n 'sid_count': 3,\n 'sid_list': [1, 2, 3],\n 'topic_count': 4,\n 'topic_list': ['A', 'B', 'C', 'D'],\n 'message_count': 2000\n}\n"))),(0,s.kt)("admonition",{type:"note"},(0,s.kt)("p",{parentName:"admonition"},"It is not necessary to call method ",(0,s.kt)("a",{parentName:"p",href:"/docs_data_analysis/next/data_access/batch_overview#setting-batch"},(0,s.kt)("strong",{parentName:"a"},"batch()"))," every time to set batch id or name. By parameter ",(0,s.kt)("inlineCode",{parentName:"p"},"inplace")," the batch may be set to current ",(0,s.kt)("a",{parentName:"p",href:"/docs_data_analysis/next/data_access/getting_started#connection-to-the-database"},(0,s.kt)("strong",{parentName:"a"},"CitrosDB"))," object:"),(0,s.kt)("pre",{parentName:"admonition"},(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> citros.batch('dynamics', inplace = True)\n>>> print(f\"current batch name: {citros.get_batch_name()}\")\n")),(0,s.kt)("pre",{parentName:"admonition"},(0,s.kt)("code",{parentName:"pre",className:"language-text"},"current batch name: dynamics\n"))),(0,s.kt)("p",null,"If specific sid is set, ",(0,s.kt)("a",{parentName:"p",href:"/docs_data_analysis/next/documentation/data_access/citros_db#citros_data_analysis.data_access.citros_db.CitrosDB.info"},(0,s.kt)("strong",{parentName:"a"},"citros.info()"))," also appends dictionary 'sids', with the following structure:"),(0,s.kt)("ul",null,(0,s.kt)("li",{parentName:"ul"},"'sids':",(0,s.kt)("ul",{parentName:"li"},(0,s.kt)("li",{parentName:"ul"},"<sid, int>:",(0,s.kt)("ul",{parentName:"li"},(0,s.kt)("li",{parentName:"ul"},"'topics': ",(0,s.kt)("ul",{parentName:"li"},(0,s.kt)("li",{parentName:"ul"},"<topic_name, str>:",(0,s.kt)("ul",{parentName:"li"},(0,s.kt)("li",{parentName:"ul"},"'message_count': number of messages"),(0,s.kt)("li",{parentName:"ul"},"'start_time': time when simulation started"),(0,s.kt)("li",{parentName:"ul"},"'end_time': time when simulation ended"),(0,s.kt)("li",{parentName:"ul"},"'duration': duration of the simulation process"),(0,s.kt)("li",{parentName:"ul"},"'frequency': frequency of the simulation process ('message_count'/ 'duration', in Hz)")))))))))),(0,s.kt)("p",null,"sid may be passed during ",(0,s.kt)("a",{parentName:"p",href:"/docs_data_analysis/next/data_access/getting_started#connection-to-the-database"},(0,s.kt)("strong",{parentName:"a"},"CitrosDB")," initialization")," or by ",(0,s.kt)("a",{parentName:"p",href:"/docs_data_analysis/next/data_access/query_data#sid-constraints"},(0,s.kt)("strong",{parentName:"a"},"citros.sid()"))," method."),(0,s.kt)("p",null,"Let's assume that the batch has been already successfully set:"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> citros.batch('dynamics', inplace = True)\n")),(0,s.kt)("p",null,"To get information about data with sid = 1 or 2 and print it:"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> citros.sid([1,2]).info().print()\n")),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-js"},"{\n 'size': '365 kB',\n 'sid_count': 2,\n 'sid_list': [1, 2],\n 'topic_count': 4,\n 'topic_list': ['A', 'B', 'C', 'D'],\n 'message_count': 1369,\n 'sids': {\n   1: {\n     'topics': {\n       'A': {\n         'message_count': 155,\n         'start_time': 312751159,\n         'end_time': 100484965889,\n         'duration': 100172214730,\n         'frequency': 1.547\n       },\n       'B': {\n         'message_count': 178,\n         'start_time': 344594155,\n         'end_time': 100752013600,\n         'duration': 100407419445,\n         'frequency': 1.773\n       },\n       'C': {\n...\n       }\n     }\n   }\n }\n}\n")),(0,s.kt)("p",null,"To set the specific topic, method ",(0,s.kt)("a",{parentName:"p",href:"/docs_data_analysis/next/documentation/data_access/citros_db#citros_data_analysis.data_access.citros_db.CitrosDB.topic"},(0,s.kt)("strong",{parentName:"a"},"topic()"))," is used.\nThis way, dictionary 'topics' is appended:"),(0,s.kt)("ul",null,(0,s.kt)("li",{parentName:"ul"},"'topics':",(0,s.kt)("ul",{parentName:"li"},(0,s.kt)("li",{parentName:"ul"},"<topic_name, str>:",(0,s.kt)("ul",{parentName:"li"},(0,s.kt)("li",{parentName:"ul"},"'type': type"),(0,s.kt)("li",{parentName:"ul"},"'data_structure': structure of the data"),(0,s.kt)("li",{parentName:"ul"},"'message_count': number of messages")))))),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> citros.topic('A').info().print()\n")),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-js"},"{\n 'size': '126 kB',\n 'sid_count': 3,\n 'sid_list': [1, 2, 3],\n 'topic_count': 1,\n 'topic_list': ['A'],\n 'message_count': 474,\n 'topics': {\n   'A': {\n     'type': 'a',\n     'data_structure': {\n       'data': {\n         'x': {\n           'x_1': 'float',\n           'x_2': 'float',\n           'x_3': 'float'\n         },\n         'note': 'list',\n         'time': 'float',\n         'height': 'float'\n       }\n     },\n     'message_count': 474\n   }\n }\n}\n")),(0,s.kt)("p",null,'If the topic has multiple types with the same data structure, they are presented in \'type\' as a list. If the types have different data structures, they are grouped by their data structure types and numbered as "type_group_0", "type_group_1", and so on:'),(0,s.kt)("ul",null,(0,s.kt)("li",{parentName:"ul"},"'topics':",(0,s.kt)("ul",{parentName:"li"},(0,s.kt)("li",{parentName:"ul"},"<topic_name, str>:",(0,s.kt)("ul",{parentName:"li"},(0,s.kt)("li",{parentName:"ul"},'"type_group_0":',(0,s.kt)("ul",{parentName:"li"},(0,s.kt)("li",{parentName:"ul"},"'type': type"),(0,s.kt)("li",{parentName:"ul"},"'data_structure': structure of the data"),(0,s.kt)("li",{parentName:"ul"},"'message_count': number of messages"))),(0,s.kt)("li",{parentName:"ul"},'"type_group_1":\n...')))))),(0,s.kt)("p",null,"The specific piece of information may be achieved by the keywords of the ",(0,s.kt)("a",{parentName:"p",href:"/docs_data_analysis/next/documentation/data_access/citros_dict#citros_data_analysis.data_access.citros_dict.CitrosDict"},(0,s.kt)("strong",{parentName:"a"},"CitrosDict")),", obtained by ",(0,s.kt)("a",{parentName:"p",href:"/docs_data_analysis/next/documentation/data_access/citros_db#citros_data_analysis.data_access.citros_db.CitrosDB.info"},(0,s.kt)("strong",{parentName:"a"},"info()"))," method."),(0,s.kt)("details",null,(0,s.kt)("summary",null,"Examples"),(0,s.kt)("ul",null,(0,s.kt)("li",{parentName:"ul"},"Get total number of messages for sid = 1 or 2:")),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},"#get information about sid equals 1 or 2 and assign the result to the variable 'inf_12':\ninf_12 = citros.sid([1,2]).info()\n\n#access number of messages by key 'message_count' and assign it to 'num':\nnum = inf_12['message_count']\n\n#print:\nprint(f'total number of messages where sid = 1 or 2: {num}')\n")),(0,s.kt)("p",null,"The result is:"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},"total number of messages where sid = 1 or 2: 1369\n")),(0,s.kt)("ul",null,(0,s.kt)("li",{parentName:"ul"},"Get number of messages for topic 'A' for each of these sids:")),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},"#for sid equals 1, for topic 'A' get number of messages by 'message_count':\nnum_1 = inf_12['sids'][1]['topics']['A']['message_count']\n\n#get number of messages for sid = 2, topic 'A':\nnum_2 = inf_12['sids'][2]['topics']['A']['message_count']\n\n#print both numbers:\nprint(f'Number of messages in \"A\" for sid = 1: {num_1}, for sid = 2: {num_2}')\n")),(0,s.kt)("p",null,"The output:"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-text"},'Number of messages in "A" for sid = 1: 155, for sid = 2: 164\n')),(0,s.kt)("ul",null,(0,s.kt)("li",{parentName:"ul"},"Get structure of the topic 'A' and the total number of messages for this topic:")),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},"#get information about topic 'A' and assign the resulting dictionary to the variable 'inf_A'\ninf_A = citros.topic('A').info()\n\n#get number of messages by 'message_count' keyword:\nnum = inf_A['message_count']\n\n#print number of messages:\nprint(f'total number of messages in topic \"A\": {num}')\n\n#print structure of the json-data column:\ninf_A['topics']['A']['data_structure']['data'].print()\n")),(0,s.kt)("p",null,"The result is:"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-js"},"total number of messages in topic \"A\": 474\n{\n 'x': {\n   'x_1': 'float',\n   'x_2': 'float',\n   'x_3': 'float'\n },\n 'note': 'list',\n 'time': 'float',\n 'height': 'float'\n}\n"))),(0,s.kt)("h2",{id:"data-structure"},"Data Structure"),(0,s.kt)("p",null,(0,s.kt)("a",{parentName:"p",href:"/docs_data_analysis/next/documentation/data_access/citros_db#citros_data_analysis.data_access.citros_db.CitrosDB.get_data_structure"},(0,s.kt)("strong",{parentName:"a"},"get_data_structure(topic = None)"))," method of the ",(0,s.kt)("a",{parentName:"p",href:"/docs_data_analysis/next/data_access/getting_started#connection-to-the-database"},(0,s.kt)("strong",{parentName:"a"},"CitrosDB"))," object may be used to display json-data structure of the exact batch for the specific topics, set by ",(0,s.kt)("a",{parentName:"p",href:"/docs_data_analysis/next/documentation/data_access/citros_db#citros_data_analysis.data_access.citros_db.CitrosDB.topic"},(0,s.kt)("strong",{parentName:"a"},"topic"))," or listed in ",(0,s.kt)("inlineCode",{parentName:"p"},"topic"),":"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> citros.batch('dynamics').topic(['A', 'C']).get_data_structure()\n")),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-text"},"+-------+------+-----------------+\n| topic | type | data            |\n+-------+------+-----------------+\n|     A |    a | {               |\n|       |      |   x: {          |\n|       |      |     x_1: float, |\n|       |      |     x_2: float, |\n|       |      |     x_3: float  |\n|       |      |   },            |\n|       |      |   note: list,   |\n|       |      |   time: float,  |\n|       |      |   height: float |\n|       |      | }               |\n+-------+------+-----------------+\n|     C |    c | {               |\n|       |      |   x: {          |\n|       |      |     x_1: float, |\n|       |      |     x_2: float, |\n|       |      |     x_3: float  |\n|       |      |   },            |\n|       |      |   note: list,   |\n|       |      |   time: float,  |\n|       |      |   height: float |\n|       |      | }               |\n+-------+------+-----------------+\n")),(0,s.kt)("p",null,"To get the result for all the existing topics, leave ",(0,s.kt)("inlineCode",{parentName:"p"},"topic")," = None. Also let's set batch to this ",(0,s.kt)("a",{parentName:"p",href:"/docs_data_analysis/next/data_access/getting_started#connection-to-the-database"},(0,s.kt)("strong",{parentName:"a"},"CitrosDB"))," object in advance:"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> citros.batch('dynamics', inplace = True)\n>>> citros.get_data_structure()\n")),(0,s.kt)("details",null,(0,s.kt)("summary",null,"The result:"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-text"},"+-------+------+-----------------+\n| topic | type | data            |\n+-------+------+-----------------+\n|     A |    a | {               |\n|       |      |   x: {          |\n|       |      |     x_1: float, |\n|       |      |     x_2: float, |\n|       |      |     x_3: float  |\n|       |      |   },            |\n|       |      |   note: list,   |\n|       |      |   time: float,  |\n|       |      |   height: float |\n|       |      | }               |\n+-------+------+-----------------+\n|     B |    b | {               |\n|       |      |   x: {          |\n|       |      |     x_1: float, |\n|       |      |     x_2: float, |\n|       |      |     x_3: float  |\n|       |      |   },            |\n|       |      |   note: list,   |\n|       |      |   time: float,  |\n|       |      |   height: float |\n|       |      | }               |\n+-------+------+-----------------+\n|     C |    c | {               |\n|       |      |   x: {          |\n|       |      |     x_1: float, |\n|       |      |     x_2: float, |\n|       |      |     x_3: float  |\n|       |      |   },            |\n|       |      |   note: list,   |\n|       |      |   time: float,  |\n|       |      |   height: float |\n|       |      | }               |\n+-------+------+-----------------+\n"))))}d.isMDXComponent=!0}}]);
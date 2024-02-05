"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[12157],{3905:(a,t,e)=>{e.d(t,{Zo:()=>d,kt:()=>g});var n=e(67294);function s(a,t,e){return t in a?Object.defineProperty(a,t,{value:e,enumerable:!0,configurable:!0,writable:!0}):a[t]=e,a}function l(a,t){var e=Object.keys(a);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(a);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(a,t).enumerable}))),e.push.apply(e,n)}return e}function i(a){for(var t=1;t<arguments.length;t++){var e=null!=arguments[t]?arguments[t]:{};t%2?l(Object(e),!0).forEach((function(t){s(a,t,e[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(a,Object.getOwnPropertyDescriptors(e)):l(Object(e)).forEach((function(t){Object.defineProperty(a,t,Object.getOwnPropertyDescriptor(e,t))}))}return a}function r(a,t){if(null==a)return{};var e,n,s=function(a,t){if(null==a)return{};var e,n,s={},l=Object.keys(a);for(n=0;n<l.length;n++)e=l[n],t.indexOf(e)>=0||(s[e]=a[e]);return s}(a,t);if(Object.getOwnPropertySymbols){var l=Object.getOwnPropertySymbols(a);for(n=0;n<l.length;n++)e=l[n],t.indexOf(e)>=0||Object.prototype.propertyIsEnumerable.call(a,e)&&(s[e]=a[e])}return s}var o=n.createContext({}),p=function(a){var t=n.useContext(o),e=t;return a&&(e="function"==typeof a?a(t):i(i({},t),a)),e},d=function(a){var t=p(a.components);return n.createElement(o.Provider,{value:t},a.children)},m="mdxType",c={inlineCode:"code",wrapper:function(a){var t=a.children;return n.createElement(n.Fragment,{},t)}},_=n.forwardRef((function(a,t){var e=a.components,s=a.mdxType,l=a.originalType,o=a.parentName,d=r(a,["components","mdxType","originalType","parentName"]),m=p(e),_=s,g=m["".concat(o,".").concat(_)]||m[_]||c[_]||l;return e?n.createElement(g,i(i({ref:t},d),{},{components:e})):n.createElement(g,i({ref:t},d))}));function g(a,t){var e=arguments,s=t&&t.mdxType;if("string"==typeof a||s){var l=e.length,i=new Array(l);i[0]=_;var r={};for(var o in t)hasOwnProperty.call(t,o)&&(r[o]=t[o]);r.originalType=a,r[m]="string"==typeof a?a:s,i[1]=r;for(var p=2;p<l;p++)i[p]=e[p];return n.createElement.apply(null,i)}return n.createElement.apply(null,e)}_.displayName="MDXCreateElement"},67963:(a,t,e)=>{e.r(t),e.d(t,{assets:()=>o,contentTitle:()=>i,default:()=>c,frontMatter:()=>l,metadata:()=>r,toc:()=>p});var n=e(87462),s=(e(67294),e(3905));const l={toc_max_heading_level:4,hide_title:!0,sidebar_position:5,sidebar_label:"Plot Data",description:"Visualizing data with plots"},i="Plot Data",r={unversionedId:"data_analysis/data_access/plot_data",id:"data_analysis/data_access/plot_data",title:"Plot Data",description:"Visualizing data with plots",source:"@site/docs/data_analysis/data_access/plot_data.md",sourceDirName:"data_analysis/data_access",slug:"/data_analysis/data_access/plot_data",permalink:"/docs/next/data_analysis/data_access/plot_data",draft:!1,tags:[],version:"current",sidebarPosition:5,frontMatter:{toc_max_heading_level:4,hide_title:!0,sidebar_position:5,sidebar_label:"Plot Data",description:"Visualizing data with plots"},sidebar:"gettingStartedSidebar",previous:{title:"Query Data",permalink:"/docs/next/data_analysis/data_access/query_data"},next:{title:"Class CitrosDB",permalink:"/docs/next/data_analysis/documentation/access/citros_db"}},o={},p=[{value:"Plot with pandas",id:"plot-with-pandas",level:2},{value:"plot_graph()",id:"plot_graph",level:2},{value:"plot_3dgraph()",id:"plot_3dgraph",level:2},{value:"multiple_y_plot()",id:"multiple_y_plot",level:2},{value:"multiplot()",id:"multiplot",level:2},{value:"plot_sigma_ellipse()",id:"plot_sigma_ellipse",level:2},{value:"time_plot()",id:"time_plot",level:2},{value:"xy_plot()",id:"xy_plot",level:2}],d={toc:p},m="wrapper";function c(a){let{components:t,...l}=a;return(0,s.kt)(m,(0,n.Z)({},d,l,{components:t,mdxType:"MDXLayout"}),(0,s.kt)("h1",{id:"plot-data"},"Plot Data"),(0,s.kt)("p",null,"Let's import and create ",(0,s.kt)("strong",{parentName:"p"},"CitrosDB")," object, setting simulation and batch names:"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> from citros import CitrosDB\n>>> citros = CitrosDB(simulation = 'simulation_name', batch = 'batch_name')\n")),(0,s.kt)("p",null,"Let's make query that select 'data.x.x_1' and 'data.x.x_2' from the json-data column of the topic 'B' with sids equals 1,2 or 3, where 10 <= rid <= 200, 0ns <= time < 200ns. Let's also apply moving average sampling, that averages over 5 messages and select each second row of the result and save the output in variable named ",(0,s.kt)("strong",{parentName:"p"},"df"),":"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> df = citros.topic('B')\\\n               .sid([1,2,3])\\\n               .rid(start = 10, end = 200)\\\n               .time(start = 0, duration = 200)\\\n               .move_avg(5,2)\\\n               .data(['data.x.x_1', 'data.x.x_2'])\n")),(0,s.kt)("h2",{id:"plot-with-pandas"},"Plot with pandas"),(0,s.kt)("p",null,"Since the result of the query is a ",(0,s.kt)("a",{parentName:"p",href:"https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html"},(0,s.kt)("strong",{parentName:"a"},"DataFrame"))," of the ",(0,s.kt)("a",{parentName:"p",href:"https://pandas.pydata.org/"},(0,s.kt)("strong",{parentName:"a"},"pandas")," package"),", ",(0,s.kt)("strong",{parentName:"p"},"pandas")," methods of ",(0,s.kt)("a",{parentName:"p",href:"https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html"},"plotting")," may be applied to it. It is possible to make separate plots for each of the sid presented in data."),(0,s.kt)("p",null,"To plot the graph 'data.x.x_1' vs. 'rid' for each sid:"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> df.set_index(['rid','sid']).unstack()['data.x.x_1'].plot()\n")),(0,s.kt)("details",null,(0,s.kt)("summary",null,"Show figure:"),(0,s.kt)("p",null,(0,s.kt)("img",{alt:"fig1",src:e(57181).Z,title:"Fig1",width:"576",height:"432"}))),(0,s.kt)("p",null,"To make one plot for both 'data.x.x_1' and 'data.x.x_2':"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> df.set_index(['rid','sid']).unstack()[['data.x.x_1','data.x.x_2']].plot()\n")),(0,s.kt)("details",null,(0,s.kt)("summary",null,"Show figure:"),(0,s.kt)("p",null,(0,s.kt)("img",{alt:"fig2",src:e(60308).Z,title:"Fig2",width:"576",height:"432"}))),(0,s.kt)("p",null,"It is also possible to query and plot all at once by a single command:"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> citros.topic('B')\\\n          .sid([1,2,3])\\\n          .rid(start = 10, end = 200)\\\n          .time(start = 0, duration = 200)\\\n          .move_avg(5,2)\\\n          .data(['data.x.x_1', 'data.x.x_2'])\\\n          .set_index(['rid','sid']).unstack()['data.x.x_1'].plot()\n")),(0,s.kt)("details",null,(0,s.kt)("summary",null,"Show figure:"),(0,s.kt)("p",null,(0,s.kt)("img",{alt:"fig1",src:e(57181).Z,title:"Fig1",width:"576",height:"432"}))),(0,s.kt)("h2",{id:"plot_graph"},"plot_graph()"),(0,s.kt)("p",null,(0,s.kt)("a",{parentName:"p",href:"/docs/next/data_analysis/documentation/access/citros_db#access.citros_db.CitrosDB.plot_graph"},(0,s.kt)("strong",{parentName:"a"},"plot_graph(df, x_label, y_label, ","*","args, ax = None, legend = True, title = None, set_x_label = None, set_y_label = None, remove_nan = True, inf_vals = 1e308, ","*","*","kwargs)"))," method of the ",(0,s.kt)("a",{parentName:"p",href:"/docs/next/data_analysis/data_access/getting_started#connection-to-the-database"},(0,s.kt)("strong",{parentName:"a"},"CitrosDB"))," object makes separate graphs '",(0,s.kt)("inlineCode",{parentName:"p"},"y_label")," vs. ",(0,s.kt)("inlineCode",{parentName:"p"},"x_label"),"' for each sid, where ",(0,s.kt)("inlineCode",{parentName:"p"},"x_label")," and ",(0,s.kt)("inlineCode",{parentName:"p"},"y_label")," are the labels of columns of the table ",(0,s.kt)("inlineCode",{parentName:"p"},"df"),". Some other additional arguments may be passed to customize the plot, see documentation for ",(0,s.kt)("a",{parentName:"p",href:"https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html"},"matplotlib.axes.Axes.plot"),"."),(0,s.kt)("p",null,"To plot simple graph 'data.x.x_2' vs 'rid':"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> citros.plot_graph(df, 'rid', 'data.x.x_2', '.', title = 'data.x.x_2 vs. rid')\n")),(0,s.kt)("details",null,(0,s.kt)("summary",null,"Show figure:"),(0,s.kt)("p",null,(0,s.kt)("img",{alt:"fig3",src:e(12301).Z,title:"Fig3",width:"565",height:"547"}))),(0,s.kt)("h2",{id:"plot_3dgraph"},"plot_3dgraph()"),(0,s.kt)("p",null,(0,s.kt)("a",{parentName:"p",href:"/docs/next/data_analysis/documentation/access/citros_db#access.citros_db.CitrosDB.plot_3dgraph"},(0,s.kt)("strong",{parentName:"a"},"plot_3dgraph(df, x_label, y_label, z_label, ","*","args, ax = None, scale = True, legend = True, title = None, set_x_label = None, set_y_label = None, set_z_label = None, remove_nan = True, inf_vals = 1e308, ","*","*","kwargs)"))," method of the ",(0,s.kt)("a",{parentName:"p",href:"/docs/next/data_analysis/data_access/getting_started#connection-to-the-database"},(0,s.kt)("strong",{parentName:"a"},"CitrosDB"))," plots 3D graph '",(0,s.kt)("inlineCode",{parentName:"p"},"z_label")," vs. ",(0,s.kt)("inlineCode",{parentName:"p"},"x_label")," and ",(0,s.kt)("inlineCode",{parentName:"p"},"y_label"),"' for each sid, where ",(0,s.kt)("inlineCode",{parentName:"p"},"x_label"),", ",(0,s.kt)("inlineCode",{parentName:"p"},"y_label")," and ",(0,s.kt)("inlineCode",{parentName:"p"},"z_label")," are the labels of columns of the pandas.DataFrame ",(0,s.kt)("inlineCode",{parentName:"p"},"df"),". Parameter ",(0,s.kt)("inlineCode",{parentName:"p"},"scale")," is used to specify whether the axis range should be the same for all three axes."),(0,s.kt)("p",null,"Let's query for 'data.x.x_1', 'data.x.x_2' and 'data.x.x_3' columns of the topic 'B' and two sids:"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> df = citros.topic('B')\\\n               .sid([1,2])\\\n               .data(['data.x.x_1', 'data.x.x_2', 'data.x.x_3'])\n")),(0,s.kt)("p",null,"If no ",(0,s.kt)("inlineCode",{parentName:"p"},"ax")," is passed, ",(0,s.kt)("strong",{parentName:"p"},"plot_3dgraph()")," creates pair of ",(0,s.kt)("inlineCode",{parentName:"p"},"fig")," and ",(0,s.kt)("inlineCode",{parentName:"p"},"ax")," and returns them:"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> fig, ax = citros.plot_3dgraph(df, 'data.x.x_1', 'data.x.x_2', 'data.x.x_3', '--', \n                 scale = False, title = 'data.x.x_3 vs.\\n data.x.x_1 and data.x.x_2', \n                 legend = True)\n>>> ax.set_box_aspect(aspect=None, zoom=0.9)\n>>> fig.tight_layout()\n")),(0,s.kt)("details",null,(0,s.kt)("summary",null,"Show figure:"),(0,s.kt)("p",null,(0,s.kt)("img",{alt:"fig6",src:e(98827).Z,title:"Fig6",width:"546",height:"590"}))),(0,s.kt)("p",null,"The ",(0,s.kt)("inlineCode",{parentName:"p"},"ax")," parameter allows the option to pass a pre-existing three-dimensional axes for plotting:"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},"import matplotlib.pyplot as plt\nfrom mpl_toolkits import mplot3d\n\n>>> fig = plt.figure(figsize=(6, 6)) \n>>> ax = fig.add_subplot(111, projection = '3d') \n>>> citros.plot_3dgraph(df, 'data.x.x_1', 'data.x.x_2', 'data.x.x_3', '--', ax = ax, \n                        scale = False, legend = True, \n                        title = 'data.x.x_3 vs.\\n data.x.x_1 and data.x.x_2')\n")),(0,s.kt)("h2",{id:"multiple_y_plot"},"multiple_y_plot()"),(0,s.kt)("p",null,(0,s.kt)("a",{parentName:"p",href:"/docs/next/data_analysis/documentation/access/citros_db#access.citros_db.CitrosDB.multiple_y_plot"},(0,s.kt)("strong",{parentName:"a"},"multiple_y_plot(df, x_label, y_labels, ","*","args, fig = None, legend = True, title = None, set_x_label = None, set_y_label = None, remove_nan = True, inf_vals = 1e308, ","*","*","kwargs)"))," plots a series of vertically arranged graphs 'y vs. ",(0,s.kt)("inlineCode",{parentName:"p"},"x_label"),"', with the y-axis labels specified in the ",(0,s.kt)("inlineCode",{parentName:"p"},"y_labels")," parameter."),(0,s.kt)("p",null,"Let's query 'data.x.x_1', 'data.x.x_2' and 'data.x.x_3' and plot them versus 'data.time':"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> df = citros.topic('B')\\\n               .data(['data.x.x_1', 'data.x.x_2', 'data.x.x_3', 'data.time'])\n>>> fig, ax = citros.multiple_y_plot(df, 'data.time', ['data.x.x_1', 'data.x.x_2', 'data.x.x_3'], \n                                     '--', legend = True, title = 'data.x vs. time')\n")),(0,s.kt)("details",null,(0,s.kt)("summary",null,"Show figure:"),(0,s.kt)("p",null,(0,s.kt)("img",{alt:"fig7",src:e(65371).Z,title:"Fig7",width:"670",height:"602"}))),(0,s.kt)("h2",{id:"multiplot"},"multiplot()"),(0,s.kt)("p",null,(0,s.kt)("a",{parentName:"p",href:"/docs/next/data_analysis/documentation/access/citros_db#access.citros_db.CitrosDB.multiplot"},(0,s.kt)("strong",{parentName:"a"},"multiplot(df, labels, ","*","args, scale = True, fig = None, legend = True, title = None, set_x_label = None, set_y_label = None, remove_nan = True, inf_vals = 1e308, label_all_xaxis = False, label_all_yaxis = False, ","*","*","kwargs)"))," method of the ",(0,s.kt)("a",{parentName:"p",href:"/docs/next/data_analysis/data_access/getting_started#connection-to-the-database"},(0,s.kt)("strong",{parentName:"a"},"CitrosDB"))," object plots a matrix of N x N graphs, each displaying either the histogram with values distribution (for graphs on the diagonal) or\nthe relationship between variables listed in ",(0,s.kt)("inlineCode",{parentName:"p"},"labels"),", with N being the length of ",(0,s.kt)("inlineCode",{parentName:"p"},"labels")," list. For non-diagonal graphs, colors are assigned to points according to sids."),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> df = citros.topic('C').skip(10).data(['data.x.x_1', 'data.x.x_2', 'data.x.x_3'])\n>>> fig, ax = citros.multiplot(df, ['data.x.x_1','data.x.x_2', 'data.x.x_3'], '.' , \n                               legend = True, title = 'data.x', scale = True)\n")),(0,s.kt)("details",null,(0,s.kt)("summary",null,"Show figure:"),(0,s.kt)("p",null,(0,s.kt)("img",{alt:"fig8",src:e(8348).Z,title:"Fig8",width:"670",height:"592"}))),(0,s.kt)("h2",{id:"plot_sigma_ellipse"},"plot_sigma_ellipse()"),(0,s.kt)("p",null,(0,s.kt)("a",{parentName:"p",href:"/docs/next/data_analysis/documentation/access/citros_db#access.citros_db.CitrosDB.plot_sigma_ellipse"},(0,s.kt)("strong",{parentName:"a"},"plot_sigma_ellipse(df, x_label, y_label, ax = None, n_std = 3, plot_origin = True, bounding_error = False, inf_vals = 1e308, legend = True, title = None, set_x_label = None, set_y_label = None, scale = False), return_ellipse_param = False"))," method of the ",(0,s.kt)("a",{parentName:"p",href:"/docs/next/data_analysis/data_access/getting_started#connection-to-the-database"},(0,s.kt)("strong",{parentName:"a"},"CitrosDB"))," object plots covariance ellipses for the ",(0,s.kt)("inlineCode",{parentName:"p"},"x_label")," vs. ",(0,s.kt)("inlineCode",{parentName:"p"},"y_label")," columns of the pandas ",(0,s.kt)("a",{parentName:"p",href:"https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html"},(0,s.kt)("strong",{parentName:"a"},"DataFrame"))," ",(0,s.kt)("inlineCode",{parentName:"p"},"df"),". "),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> df = citros.topic('A').data(['data.x.x_1', 'data.x.x_2'])\n>>> fig, ax = citros.plot_sigma_ellipse(df, x_label = 'data.x.x_1', y_label = 'data.x.x_2', \n                                        n_std = 2, plot_origin=True, scale = True)\n")),(0,s.kt)("details",null,(0,s.kt)("summary",null,"Show figure:"),(0,s.kt)("p",null,(0,s.kt)("img",{alt:"fig9",src:e(48298).Z,title:"Fig9",width:"701",height:"590"}))),(0,s.kt)("p",null,"To plot multiple error ellipses, such as 1-",(0,s.kt)("span",{parentName:"p",className:"math math-inline"},(0,s.kt)("span",{parentName:"span",className:"katex"},(0,s.kt)("span",{parentName:"span",className:"katex-mathml"},(0,s.kt)("math",{parentName:"span",xmlns:"http://www.w3.org/1998/Math/MathML"},(0,s.kt)("semantics",{parentName:"math"},(0,s.kt)("mrow",{parentName:"semantics"},(0,s.kt)("mi",{parentName:"mrow"},"\u03c3")),(0,s.kt)("annotation",{parentName:"semantics",encoding:"application/x-tex"},"\\sigma")))),(0,s.kt)("span",{parentName:"span",className:"katex-html","aria-hidden":"true"},(0,s.kt)("span",{parentName:"span",className:"base"},(0,s.kt)("span",{parentName:"span",className:"strut",style:{height:"0.4306em"}}),(0,s.kt)("span",{parentName:"span",className:"mord mathnormal",style:{marginRight:"0.03588em"}},"\u03c3"))))),", 2-",(0,s.kt)("span",{parentName:"p",className:"math math-inline"},(0,s.kt)("span",{parentName:"span",className:"katex"},(0,s.kt)("span",{parentName:"span",className:"katex-mathml"},(0,s.kt)("math",{parentName:"span",xmlns:"http://www.w3.org/1998/Math/MathML"},(0,s.kt)("semantics",{parentName:"math"},(0,s.kt)("mrow",{parentName:"semantics"},(0,s.kt)("mi",{parentName:"mrow"},"\u03c3")),(0,s.kt)("annotation",{parentName:"semantics",encoding:"application/x-tex"},"\\sigma")))),(0,s.kt)("span",{parentName:"span",className:"katex-html","aria-hidden":"true"},(0,s.kt)("span",{parentName:"span",className:"base"},(0,s.kt)("span",{parentName:"span",className:"strut",style:{height:"0.4306em"}}),(0,s.kt)("span",{parentName:"span",className:"mord mathnormal",style:{marginRight:"0.03588em"}},"\u03c3"))))),", and 3-",(0,s.kt)("span",{parentName:"p",className:"math math-inline"},(0,s.kt)("span",{parentName:"span",className:"katex"},(0,s.kt)("span",{parentName:"span",className:"katex-mathml"},(0,s.kt)("math",{parentName:"span",xmlns:"http://www.w3.org/1998/Math/MathML"},(0,s.kt)("semantics",{parentName:"math"},(0,s.kt)("mrow",{parentName:"semantics"},(0,s.kt)("mi",{parentName:"mrow"},"\u03c3")),(0,s.kt)("annotation",{parentName:"semantics",encoding:"application/x-tex"},"\\sigma")))),(0,s.kt)("span",{parentName:"span",className:"katex-html","aria-hidden":"true"},(0,s.kt)("span",{parentName:"span",className:"base"},(0,s.kt)("span",{parentName:"span",className:"strut",style:{height:"0.4306em"}}),(0,s.kt)("span",{parentName:"span",className:"mord mathnormal",style:{marginRight:"0.03588em"}},"\u03c3")))))," ellipses, pass a list to the n_std parameter, like 'n_std=","[1, 2, 3]","'. By setting bounding_error to True, the bounding error will be plotted for all of these ellipses. Additionally, you have the flexibility to customize labels and titles of the plot as desired."),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> fig, ax = citros.plot_sigma_ellipse(df, x_label = 'data.x.x_1', y_label = 'data.x.x_2', \n                                        n_std = [1,2,3], plot_origin=True, bounding_error=True,\n                                        set_x_label='x, [m]', set_y_label = 'y, [m]', \n                                        title = 'Coordinates')\n")),(0,s.kt)("details",null,(0,s.kt)("summary",null,"Show figure:"),(0,s.kt)("p",null,(0,s.kt)("img",{alt:"fig10",src:e(26546).Z,title:"Fig10",width:"701",height:"590"}))),(0,s.kt)("p",null,"If ",(0,s.kt)("inlineCode",{parentName:"p"},"return_ellipse_param")," = True, the dictionary with ellipse parameters is also returned:"),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},">>> fig, ax, ellipse_param = citros.plot_sigma_ellipse(df, x_label = 'data.x.x_1', y_label = 'data.x.x_2', \n                                    n_std = [1,2,3], plot_origin=True, bounding_error=True,\n                                    set_x_label='x, [m]', set_y_label = 'y, [m]', \n                                    title = 'Coordinates', return_ellipse_param = True)\n")),(0,s.kt)("p",null," The output contains:"),(0,s.kt)("ul",null,(0,s.kt)("li",{parentName:"ul"},"'x' - x coordinate of the center;"),(0,s.kt)("li",{parentName:"ul"},"'y' - y coordinate of the center;"),(0,s.kt)("li",{parentName:"ul"},"'width' - ellipse width (along the longer axis);"),(0,s.kt)("li",{parentName:"ul"},"'height' - ellipse height (along the shorter axis);"),(0,s.kt)("li",{parentName:"ul"},"'alpha' - angle of rotation, in degrees.\n")),(0,s.kt)("p",null,"And if ",(0,s.kt)("inlineCode",{parentName:"p"},"bounding_error")," set True:"),(0,s.kt)("ul",null,(0,s.kt)("li",{parentName:"ul"},"bounding_error -radius of the error circle.")),(0,s.kt)("p",null,"If the number of error ellipses is more then 1, the output is the list of dict."),(0,s.kt)("h2",{id:"time_plot"},"time_plot()"),(0,s.kt)("p",null,(0,s.kt)("a",{parentName:"p",href:"/docs/next/data_analysis/documentation/access/citros_db#access.citros_db.CitrosDB.time_plot"},(0,s.kt)("strong",{parentName:"a"},"time_plot(ax, ","*","args, topic_name = None, var_name = None, time_step = 1.0, sids = None, y_label = None, title_text = None, legend = True,  remove_nan = True, inf_vals = 1e308, ","*","*","kwarg)"))," method of the ",(0,s.kt)("a",{parentName:"p",href:"/docs/next/data_analysis/data_access/getting_started#connection-to-the-database"},(0,s.kt)("strong",{parentName:"a"},"CitrosDB"))," object query column ",(0,s.kt)("inlineCode",{parentName:"p"},"var_name")," of the topic ",(0,s.kt)("inlineCode",{parentName:"p"},"topic_name")," and plots ",(0,s.kt)("inlineCode",{parentName:"p"},"var_name")," vs. ",(0,s.kt)("inlineCode",{parentName:"p"},"Time")," for each of the sids, where ",(0,s.kt)("inlineCode",{parentName:"p"},"Time")," = ",(0,s.kt)("inlineCode",{parentName:"p"},"time_step")," * rid. It is possible to specify sids by passing them as a list to ",(0,s.kt)("inlineCode",{parentName:"p"},"sid"),". If ",(0,s.kt)("inlineCode",{parentName:"p"},"sid")," is not specified, data for all sids is used. "),(0,s.kt)("admonition",{type:"note"},(0,s.kt)("p",{parentName:"admonition"},"Such methods as ",(0,s.kt)("a",{parentName:"p",href:"/docs/next/data_analysis/documentation/access/citros_db#access.citros_db.CitrosDB.topic"},(0,s.kt)("strong",{parentName:"a"},"topic()")),", ",(0,s.kt)("a",{parentName:"p",href:"/docs/next/data_analysis/data_access/query_data#rid-constraints"},(0,s.kt)("strong",{parentName:"a"},"rid()")),", ",(0,s.kt)("a",{parentName:"p",href:"/docs/next/data_analysis/data_access/query_data#sid-constraints"},(0,s.kt)("strong",{parentName:"a"},"sid()")),", ",(0,s.kt)("a",{parentName:"p",href:"/docs/next/data_analysis/data_access/query_data#time-constraints"},(0,s.kt)("strong",{parentName:"a"},"time()"))," and ",(0,s.kt)("a",{parentName:"p",href:"/docs/next/data_analysis/data_access/query_data#json-data-constraints"},(0,s.kt)("strong",{parentName:"a"},"set_filter()"))," may be used to put constraints on data before plotting (see ",(0,s.kt)("a",{parentName:"p",href:"/docs/next/data_analysis/data_access/query_data#constraints-combination"},"constraints combination"),").")),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},"import matplotlib.pyplot as plt\n\n>>> fig, ax = plt.subplots()\n>>> citros.topic('A').time_plot(ax, \n                                var_name = 'data.x.x_1', \n                                time_step = 0.5, \n                                sids = [1,3],\n                                y_label='x_1', title_text = 'x_1 vs. Time')\n")),(0,s.kt)("details",null,(0,s.kt)("summary",null,"Show figure:"),(0,s.kt)("p",null,(0,s.kt)("img",{alt:"fig4",src:e(72746).Z,title:"Fig4",width:"591",height:"455"}))),(0,s.kt)("h2",{id:"xy_plot"},"xy_plot()"),(0,s.kt)("p",null,(0,s.kt)("a",{parentName:"p",href:"/docs/next/data_analysis/documentation/access/citros_db#access.citros_db.CitrosDB.xy_plot"},(0,s.kt)("strong",{parentName:"a"},"xy_plot(ax, ","*","args, topic_name = None, var_x_name = None, var_y_name = None, sids = None, x_label = None, y_label = None, title_text = None, legend = True, remove_nan = True, inf_vals = 1e308, ","*","*","kwargs)"))," method of the ",(0,s.kt)("a",{parentName:"p",href:"/docs/next/data_analysis/data_access/getting_started#connection-to-the-database"},(0,s.kt)("strong",{parentName:"a"},"CitrosDB"))," object query columns ",(0,s.kt)("inlineCode",{parentName:"p"},"var_x_name")," and ",(0,s.kt)("inlineCode",{parentName:"p"},"var_y_name")," of the topic ",(0,s.kt)("inlineCode",{parentName:"p"},"topic_name")," and plots ",(0,s.kt)("inlineCode",{parentName:"p"},"var_y_name")," vs. ",(0,s.kt)("inlineCode",{parentName:"p"},"var_x_name")," for each of the sids. It is possible to specify sids by passing them as a list to ",(0,s.kt)("inlineCode",{parentName:"p"},"sid"),". If ",(0,s.kt)("inlineCode",{parentName:"p"},"sid")," is not specified, data for all sids is used."),(0,s.kt)("admonition",{type:"note"},(0,s.kt)("p",{parentName:"admonition"},"Such methods as ",(0,s.kt)("a",{parentName:"p",href:"/docs/next/data_analysis/documentation/access/citros_db#access.citros_db.CitrosDB.topic"},(0,s.kt)("strong",{parentName:"a"},"topic()")),", ",(0,s.kt)("a",{parentName:"p",href:"/docs/next/data_analysis/data_access/query_data#rid-constraints"},(0,s.kt)("strong",{parentName:"a"},"rid()")),", ",(0,s.kt)("a",{parentName:"p",href:"/docs/next/data_analysis/data_access/query_data#sid-constraints"},(0,s.kt)("strong",{parentName:"a"},"sid()")),", ",(0,s.kt)("a",{parentName:"p",href:"/docs/next/data_analysis/data_access/query_data#time-constraints"},(0,s.kt)("strong",{parentName:"a"},"time()"))," and ",(0,s.kt)("a",{parentName:"p",href:"/docs/next/data_analysis/data_access/query_data#json-data-constraints"},(0,s.kt)("strong",{parentName:"a"},"set_filter()"))," may be used to put constraints on data before plotting (see ",(0,s.kt)("a",{parentName:"p",href:"/docs/next/data_analysis/data_access/query_data#constraints-combination"},"constraints combination"),").")),(0,s.kt)("pre",null,(0,s.kt)("code",{parentName:"pre",className:"language-python"},"import matplotlib.pyplot as plt\n\n>>> fig, ax = plt.subplots()\n>>> citros.sid([1,2,3]).topic('A')\\\n                       .xy_plot(ax, \n                                var_x_name = 'data.time', \n                                var_y_name = 'data.height',\n                                x_label='time', y_label = 'height', \n                                title_text='time vs. height')\n")),(0,s.kt)("details",null,(0,s.kt)("summary",null,"Show figure:"),(0,s.kt)("p",null,(0,s.kt)("img",{alt:"fig5",src:e(19486).Z,title:"Fig5",width:"600",height:"455"}))))}c.isMDXComponent=!0},57181:(a,t,e)=>{e.d(t,{Z:()=>n});const n=e.p+"assets/images/fig1-1cbb974a672e961cef1fc76c8d1b84a5.png"},72746:(a,t,e)=>{e.d(t,{Z:()=>n});const n=e.p+"assets/images/fig16-30509eb4faa32f1b27c827182d024c39.png"},19486:(a,t,e)=>{e.d(t,{Z:()=>n});const n=e.p+"assets/images/fig17-d805164cf0fd1969fd30684706553251.png"},98827:(a,t,e)=>{e.d(t,{Z:()=>n});const n=e.p+"assets/images/fig18-fb88b66a47a15140d5107f6488c44556.png"},65371:(a,t,e)=>{e.d(t,{Z:()=>n});const n=e.p+"assets/images/fig19-5f166608230d6f96cb3be0bd0298fbed.png"},60308:(a,t,e)=>{e.d(t,{Z:()=>n});const n=e.p+"assets/images/fig2-56bb64c07f2b524532cf94bbfbc21e5d.png"},8348:(a,t,e)=>{e.d(t,{Z:()=>n});const n=e.p+"assets/images/fig20-fa3c235bedc37ce72d8674620858ca0b.png"},48298:(a,t,e)=>{e.d(t,{Z:()=>n});const n=e.p+"assets/images/fig25-5f8892adcfe85f0b836fe66eb4a95949.png"},26546:(a,t,e)=>{e.d(t,{Z:()=>n});const n=e.p+"assets/images/fig26-3903a3f9543b2dfbb12e818809f42783.png"},12301:(a,t,e)=>{e.d(t,{Z:()=>n});const n=e.p+"assets/images/fig3-7f945e8efc35c1d7287bbb726892c6dd.png"}}]);
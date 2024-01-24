"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[7886],{3905:(e,t,a)=>{a.d(t,{Zo:()=>d,kt:()=>_});var n=a(67294);function r(e,t,a){return t in e?Object.defineProperty(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}function i(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,n)}return a}function o(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?i(Object(a),!0).forEach((function(t){r(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):i(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}function l(e,t){if(null==e)return{};var a,n,r=function(e,t){if(null==e)return{};var a,n,r={},i=Object.keys(e);for(n=0;n<i.length;n++)a=i[n],t.indexOf(a)>=0||(r[a]=e[a]);return r}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(n=0;n<i.length;n++)a=i[n],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(r[a]=e[a])}return r}var s=n.createContext({}),p=function(e){var t=n.useContext(s),a=t;return e&&(a="function"==typeof e?e(t):o(o({},t),e)),a},d=function(e){var t=p(e.components);return n.createElement(s.Provider,{value:t},e.children)},c="mdxType",u={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},m=n.forwardRef((function(e,t){var a=e.components,r=e.mdxType,i=e.originalType,s=e.parentName,d=l(e,["components","mdxType","originalType","parentName"]),c=p(a),m=r,_=c["".concat(s,".").concat(m)]||c[m]||u[m]||i;return a?n.createElement(_,o(o({ref:t},d),{},{components:a})):n.createElement(_,o({ref:t},d))}));function _(e,t){var a=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var i=a.length,o=new Array(i);o[0]=m;var l={};for(var s in t)hasOwnProperty.call(t,s)&&(l[s]=t[s]);l.originalType=e,l[c]="string"==typeof e?e:r,o[1]=l;for(var p=2;p<i;p++)o[p]=a[p];return n.createElement.apply(null,o)}return n.createElement.apply(null,a)}m.displayName="MDXCreateElement"},81476:(e,t,a)=>{a.r(t),a.d(t,{assets:()=>s,contentTitle:()=>o,default:()=>u,frontMatter:()=>i,metadata:()=>l,toc:()=>p});var n=a(87462),r=(a(67294),a(3905));const i={toc_max_heading_level:4,hide_title:!0,sidebar_position:3,sidebar_label:"Correlation",description:"Correlation"},o="Correlation",l={unversionedId:"data_analysis/error_analysis/correlation",id:"version-0.2.18/data_analysis/error_analysis/correlation",title:"Correlation",description:"Correlation",source:"@site/versioned_docs/version-0.2.18/data_analysis/error_analysis/correlation.md",sourceDirName:"data_analysis/error_analysis",slug:"/data_analysis/error_analysis/correlation",permalink:"/docs/data_analysis/error_analysis/correlation",draft:!1,tags:[],version:"0.2.18",sidebarPosition:3,frontMatter:{toc_max_heading_level:4,hide_title:!0,sidebar_position:3,sidebar_label:"Correlation",description:"Correlation"},sidebar:"gettingStartedSidebar",previous:{title:"Bin, Interpolate and Calculate Statistics",permalink:"/docs/data_analysis/error_analysis/statistics"},next:{title:"Regression",permalink:"/docs/data_analysis/error_analysis/regression"}},s={},p=[],d={toc:p},c="wrapper";function u(e){let{components:t,...i}=e;return(0,r.kt)(c,(0,n.Z)({},d,i,{components:t,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"correlation"},"Correlation"),(0,r.kt)("p",null,"Function ",(0,r.kt)("a",{parentName:"p",href:"/docs/data_analysis/documentation/analysis/citros_data#analysis.citros_data.CitrosData.show_correlation"},(0,r.kt)("strong",{parentName:"a"},"show_correlation()"))," plots correlation between two variables for the exact index ",(0,r.kt)("inlineCode",{parentName:"p"},"slice_id"),". Let's apply it to the CitrosData object that we obtained it the ",(0,r.kt)("a",{parentName:"p",href:"/docs/data_analysis/error_analysis/statistics#scale-data"},"previous example")," and named ",(0,r.kt)("em",{parentName:"p"},"db_sc")," for the time_id = 0:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> db_sc.show_correlation(x_col = 'data.x.x_1',\n                           y_col = 'data.x.x_2',\n                           slice_id = 0,\n                           n_std = [1,2,3])\n")),(0,r.kt)("details",null,(0,r.kt)("summary",null,"How we got db_sc:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> from citros import CitrosDB, CitrosData\n\n>>> citros = CitrosDB()\n>>> df = citros.simulation('simulation_environment').batch('temperature').topic('A').data(['data.x.x_1', 'data.x.x_2', 'data.time'])\n\n>>> dataset = CitrosData(df, data_label=['data.x.x_1', 'data.x.x_2'], units = 'm')\n>>> db_sc = dataset.scale_data(n_points = 50,\n                               param_label = 'data.time')\n"))),(0,r.kt)("p",null,"The value of the independent parameter, that corresponds to ",(0,r.kt)("inlineCode",{parentName:"p"},"slice_id")," = 0 is 0.0. This information is printed in the output:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-text"},"slice_id = 0,\nslice_val = 0.0\n")),(0,r.kt)("details",null,(0,r.kt)("summary",null,"Show the correlation plot:"),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"fig7",src:a(77966).Z,title:"Fig7",width:"669",height:"547"}))),(0,r.kt)("p",null,"Pass to ",(0,r.kt)("inlineCode",{parentName:"p"},"x_col")," and ",(0,r.kt)("inlineCode",{parentName:"p"},"y_col")," either label or index of the columns to plot along x and y axis respectively. Instead of ",(0,r.kt)("inlineCode",{parentName:"p"},"slice_id")," index the value ",(0,r.kt)("inlineCode",{parentName:"p"},"slice_val")," may be specified. That way, the nearest ",(0,r.kt)("inlineCode",{parentName:"p"},"slice_id")," index will be found and the corresponding to it exact value of ",(0,r.kt)("inlineCode",{parentName:"p"},"slice_val")," will be printed. ",(0,r.kt)("inlineCode",{parentName:"p"},"n_std")," states the radius or radii of the confidence ellipses in sigmas. If ",(0,r.kt)("inlineCode",{parentName:"p"},"bounding_error")," = True, then the bounding error circle is added to plot."),(0,r.kt)("p",null,"The following code plots first column ('data.x.x_1') vs. second ('data.x.x_2') for the id, nearest to 'data.time' = 0.2 and plots bounding error circle. Additionally, when setting ",(0,r.kt)("inlineCode",{parentName:"p"},"return_fig")," to True, the function will return the figure (matplotlib.figure.Figure) and ax (matplotlib.axes.Axes) objects. These objects can be employed to further enhance the image with customized styling:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> fig, ax = db_sc.show_correlation(x_col = 0,\n                                     y_col = 1,\n                                     slice_val = 0.2,\n                                     n_std = [1,2,3],\n                                     bounding_error = True,\n                                     return_fig = True)\n")),(0,r.kt)("p",null,"The nearest to ",(0,r.kt)("inlineCode",{parentName:"p"},"slice_val")," = 0.2 ",(0,r.kt)("inlineCode",{parentName:"p"},"slice_id")," turned out to be 10 and the exact value, that corresponds to ",(0,r.kt)("inlineCode",{parentName:"p"},"slice_id")," = 10 is 0.204: "),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-text"},"slice_id = 10,\nslice_val = 0.204\n")),(0,r.kt)("details",null,(0,r.kt)("summary",null,"Show the correlation plot with bounding error:"),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"fig8",src:a(24456).Z,title:"Fig8",width:"669",height:"547"}))),(0,r.kt)("p",null,"If ",(0,r.kt)("inlineCode",{parentName:"p"},"return_ellipse_param")," = True, the dictionary with ellipse parameters is also returned:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> fig, ax, ellipse_param = db_sc.show_correlation(x_col = 0, y_col = 1,\n                                                    slice_val = 0.2,\n                                                    n_std = 1,\n                                                    bounding_error = True,\n                                                    return_fig = True,\n                                                    return_ellipse_param = True)\n# Print ellipse parameters:\n>>> print(\"\\nellipse parameters:\")\n>>> print(f\"center: ({ellipse_param['x']}, {ellipse_param['y']})\")\n>>> print(f\"width: {ellipse_param['width']}, height: {ellipse_param['height']}\")\n>>> print(f\"angle of rotation: {ellipse_param['alpha']}\\n\")\n>>> if bounding_error:\n>>>     print(f\"radius of the error circle: {ellipse_param['bounding_error']}\\n\")\n")),(0,r.kt)("p",null," The output contains:"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"'x' - x coordinate of the center;"),(0,r.kt)("li",{parentName:"ul"},"'y' - y coordinate of the center;"),(0,r.kt)("li",{parentName:"ul"},"'width' - ellipse width (along the longer axis);"),(0,r.kt)("li",{parentName:"ul"},"'height' - ellipse height (along the shorter axis);"),(0,r.kt)("li",{parentName:"ul"},"'alpha' - angle of rotation, in degrees.\n")),(0,r.kt)("p",null,"And if ",(0,r.kt)("inlineCode",{parentName:"p"},"bounding_error")," set True:"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"bounding_error - radius of the error circle.")),(0,r.kt)("p",null,"If the number of error ellipses is more then 1, the output is the list of dict."),(0,r.kt)("p",null,"To plot correlation between variables from different ",(0,r.kt)("a",{parentName:"p",href:"/docs/data_analysis/error_analysis/statistics#citrosdata-object"},(0,r.kt)("strong",{parentName:"a"},"CitrosData"))," objects, pass the object by ",(0,r.kt)("inlineCode",{parentName:"p"},"db2")," parameter. This way, ",(0,r.kt)("inlineCode",{parentName:"p"},"x_col")," is supposed to be the column of the first ",(0,r.kt)("a",{parentName:"p",href:"/docs/data_analysis/error_analysis/statistics#citrosdata-object"},(0,r.kt)("strong",{parentName:"a"},"CitrosData"))," objects, while ",(0,r.kt)("inlineCode",{parentName:"p"},"y_col")," - the column of the ",(0,r.kt)("inlineCode",{parentName:"p"},"db2"),". If ",(0,r.kt)("inlineCode",{parentName:"p"},"slice_val")," is passed, then the ",(0,r.kt)("inlineCode",{parentName:"p"},"slice_id")," is searched for each ",(0,r.kt)("a",{parentName:"p",href:"/docs/data_analysis/error_analysis/statistics#citrosdata-object"},(0,r.kt)("strong",{parentName:"a"},"CitrosData"))," objects."),(0,r.kt)("p",null,"Let's query for topic 'B' of the batch 'density' from the simulation 'simulation_environment', scale data using 20 points and plot correlation between 'data.x.x_2' of ",(0,r.kt)("inlineCode",{parentName:"p"},"db_sc")," vs. 'data.x.x_1' of ",(0,r.kt)("inlineCode",{parentName:"p"},"db_sc_B")," near the point 'data.time' = 0.7:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"#download columns 'data.x' and 'data.time' for topic 'B'\ndf_B = citros.simulation('simulation_environment').batch('density').topic('B').data(['data.x', 'data.time'])\n\n#construct CitrosData object with 3 data-columns from 'data.x'\ndataset_B = CitrosData(df, data_label=['data.x'], units = 'm')\n\n#scale data\ndb_sc_B = dataset.scale_data(n_points = 20, \n                             param_label = 'data.time')\n                             \ndb_sc.show_correlation(db2 = db_sc_B,\n                       x_col = 'data.x.x_2',\n                       y_col = 'data.x.x_1',\n                       slice_val = 0.7,\n                       n_std = [1,2,3])\n")),(0,r.kt)("p",null,"The output is:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-text"},"slice_id = 34,\nslice_val = 0.694,\nslice_id_2 = 13,\nslice_val_2 = 0.684\n")),(0,r.kt)("details",null,(0,r.kt)("summary",null,"Show the plot:"),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"fig10",src:a(78449).Z,title:"Fig10",width:"669",height:"547"}))))}u.isMDXComponent=!0},78449:(e,t,a)=>{a.d(t,{Z:()=>n});const n=a.p+"assets/images/fig10-d50185dc0b4747c47bddbb0b74a27a0d.png"},77966:(e,t,a)=>{a.d(t,{Z:()=>n});const n=a.p+"assets/images/fig7-7f315825754f63e51adeab88eecb3b7c.png"},24456:(e,t,a)=>{a.d(t,{Z:()=>n});const n=a.p+"assets/images/fig8-e76d8376b93413a1684557e4ccceb49a.png"}}]);
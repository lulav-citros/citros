"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[2701],{3905:(e,t,a)=>{a.d(t,{Zo:()=>p,kt:()=>m});var n=a(7294);function r(e,t,a){return t in e?Object.defineProperty(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}function i(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,n)}return a}function o(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?i(Object(a),!0).forEach((function(t){r(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):i(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}function l(e,t){if(null==e)return{};var a,n,r=function(e,t){if(null==e)return{};var a,n,r={},i=Object.keys(e);for(n=0;n<i.length;n++)a=i[n],t.indexOf(a)>=0||(r[a]=e[a]);return r}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(n=0;n<i.length;n++)a=i[n],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(r[a]=e[a])}return r}var s=n.createContext({}),c=function(e){var t=n.useContext(s),a=t;return e&&(a="function"==typeof e?e(t):o(o({},t),e)),a},p=function(e){var t=c(e.components);return n.createElement(s.Provider,{value:t},e.children)},d="mdxType",u={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},_=n.forwardRef((function(e,t){var a=e.components,r=e.mdxType,i=e.originalType,s=e.parentName,p=l(e,["components","mdxType","originalType","parentName"]),d=c(a),_=r,m=d["".concat(s,".").concat(_)]||d[_]||u[_]||i;return a?n.createElement(m,o(o({ref:t},p),{},{components:a})):n.createElement(m,o({ref:t},p))}));function m(e,t){var a=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var i=a.length,o=new Array(i);o[0]=_;var l={};for(var s in t)hasOwnProperty.call(t,s)&&(l[s]=t[s]);l.originalType=e,l[d]="string"==typeof e?e:r,o[1]=l;for(var c=2;c<i;c++)o[c]=a[c];return n.createElement.apply(null,o)}return n.createElement.apply(null,a)}_.displayName="MDXCreateElement"},8268:(e,t,a)=>{a.r(t),a.d(t,{assets:()=>s,contentTitle:()=>o,default:()=>u,frontMatter:()=>i,metadata:()=>l,toc:()=>c});var n=a(7462),r=(a(7294),a(3905));const i={toc_max_heading_level:4,hide_title:!0,sidebar_position:3,sidebar_label:"Correlation",description:"Correlation"},o="Correlation",l={unversionedId:"error_analysis/correlation",id:"error_analysis/correlation",title:"Correlation",description:"Correlation",source:"@site/docs_data_analysis/error_analysis/correlation.md",sourceDirName:"error_analysis",slug:"/error_analysis/correlation",permalink:"/docs/docs_data_analysis/next/error_analysis/correlation",draft:!1,tags:[],version:"current",sidebarPosition:3,frontMatter:{toc_max_heading_level:4,hide_title:!0,sidebar_position:3,sidebar_label:"Correlation",description:"Correlation"},sidebar:"dataAnalysisSidebar",previous:{title:"Bin, Interpolate and Calculate Statistics",permalink:"/docs/docs_data_analysis/next/error_analysis/statistics"},next:{title:"Regression",permalink:"/docs/docs_data_analysis/next/error_analysis/regression"}},s={},c=[],p={toc:c},d="wrapper";function u(e){let{components:t,...i}=e;return(0,r.kt)(d,(0,n.Z)({},p,i,{components:t,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"correlation"},"Correlation"),(0,r.kt)("p",null,"Function ",(0,r.kt)("a",{parentName:"p",href:"/docs/docs_data_analysis/next/documentation/error_analysis/citros_data#citros_data_analysis.error_analysis.citros_data.CitrosData.show_correlation"},(0,r.kt)("strong",{parentName:"a"},"show_correlation()"))," plots correlation between two variables for the exact index ",(0,r.kt)("inlineCode",{parentName:"p"},"slice_id"),". Applying it to the ",(0,r.kt)("a",{parentName:"p",href:"/docs/docs_data_analysis/next/error_analysis/statistics#scale-data"},"previous example")," for the time_id = 0:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> db_sc.show_correlation(x_col = 'data.x.x_1',\n                           y_col = 'data.x.x_2',\n                           slice_id = 0,\n                           n_std = [1,2,3])\n")),(0,r.kt)("p",null,"The value of the independent parameter, that corresponds to ",(0,r.kt)("inlineCode",{parentName:"p"},"slice_id")," = 0 is 0.0. This information is printed in the output:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-text"},"slice_id = 0,\nslice_val = 0.0\n")),(0,r.kt)("details",null,(0,r.kt)("summary",null,"Show the correlation plot:"),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"fig7",src:a(4305).Z,title:"Fig7",width:"669",height:"547"}))),(0,r.kt)("p",null,"Pass to ",(0,r.kt)("inlineCode",{parentName:"p"},"x_col")," and ",(0,r.kt)("inlineCode",{parentName:"p"},"y_col")," either label or index of the columns to plot along x and y axis respectively. Instead of ",(0,r.kt)("inlineCode",{parentName:"p"},"slice_id")," index the value ",(0,r.kt)("inlineCode",{parentName:"p"},"slice_val")," may be specified. That way, the nearest ",(0,r.kt)("inlineCode",{parentName:"p"},"slice_id")," index will be found and the corresponding to it exact value of ",(0,r.kt)("inlineCode",{parentName:"p"},"slice_val")," will be printed. ",(0,r.kt)("inlineCode",{parentName:"p"},"n_std")," states the radius or radii of the confidence ellipses in sigmas. If ",(0,r.kt)("inlineCode",{parentName:"p"},"bounding_error")," = True, then the bounding error circle is added to plot."),(0,r.kt)("p",null,"The following code plots first column ('data.x.x_1') vs. second ('data.x.x_2') for the id, nearest to 'data.time' = 0.2 and plots bounding error circle. Additionally, when setting ",(0,r.kt)("inlineCode",{parentName:"p"},"return_fig")," to True, the function will return the figure (matplotlib.figure.Figure) and ax (matplotlib.axes.Axes) objects. These objects can be employed to further enhance the image with customized styling:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> fig, ax = db_sc.show_correlation(x_col = 0,\n                                     y_col = 1,\n                                     slice_val = 0.2,\n                                     n_std = [1,2,3],\n                                     bounding_error = True,\n                                     return_fig = True)\n")),(0,r.kt)("p",null,"The nearest to ",(0,r.kt)("inlineCode",{parentName:"p"},"slice_val")," = 0.2 ",(0,r.kt)("inlineCode",{parentName:"p"},"slice_id")," turned out to be 10 and the exact value, that corresponds to ",(0,r.kt)("inlineCode",{parentName:"p"},"slice_id")," = 10 is 0.204: "),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-text"},"slice_id = 10,\nslice_val = 0.204\n")),(0,r.kt)("details",null,(0,r.kt)("summary",null,"Show the correlation plot with bounding error:"),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"fig8",src:a(9657).Z,title:"Fig8",width:"669",height:"547"}))),(0,r.kt)("p",null,"If ",(0,r.kt)("inlineCode",{parentName:"p"},"return_ellipse_param")," = True, the dictionary with ellipse parameters is also returned:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},">>> fig, ax, ellipse_param = db_sc.show_correlation(x_col = 0, y_col = 1,\n                                                    slice_val = 0.2,\n                                                    n_std = 1,\n                                                    bounding_error = True,\n                                                    return_fig = True,\n                                                    return_ellipse_param = True)\n# Print ellipse parameters:\n>>> print(\"\\nellipse parameters:\")\n>>> print(f\"center: ({ellipse_param['x']}, {ellipse_param['y']})\")\n>>> print(f\"width: {ellipse_param['width']}, height: {ellipse_param['height']}\")\n>>> print(f\"angle of rotation: {ellipse_param['alpha']}\\n\")\n>>> if bounding_error:\n>>>     print(f\"radius of the error circle: {ellipse_param['bounding_error']}\\n\")\n")),(0,r.kt)("p",null," The output contains:"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"'x' - x coordinate of the center;"),(0,r.kt)("li",{parentName:"ul"},"'y' - y coordinate of the center;"),(0,r.kt)("li",{parentName:"ul"},"'width' - ellipse width (along the longer axis);"),(0,r.kt)("li",{parentName:"ul"},"'height' - ellipse height (along the shorter axis);"),(0,r.kt)("li",{parentName:"ul"},"'alpha' - angle of rotation, in degrees.\n")),(0,r.kt)("p",null,"And if ",(0,r.kt)("inlineCode",{parentName:"p"},"bounding_error")," set True:"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"bounding_error - radius of the error circle.")),(0,r.kt)("p",null,"If the number of error ellipses is more then 1, the output is the list of dict."),(0,r.kt)("p",null,"To plot correlation between variables from different ",(0,r.kt)("a",{parentName:"p",href:"/docs/docs_data_analysis/next/error_analysis/statistics#citrosdata-object"},(0,r.kt)("strong",{parentName:"a"},"CitrosData"))," objects, pass the object by ",(0,r.kt)("inlineCode",{parentName:"p"},"db2")," parameter. This way, ",(0,r.kt)("inlineCode",{parentName:"p"},"x_col")," is supposed to be the column of the first ",(0,r.kt)("a",{parentName:"p",href:"/docs/docs_data_analysis/next/error_analysis/statistics#citrosdata-object"},(0,r.kt)("strong",{parentName:"a"},"CitrosData"))," objects, while ",(0,r.kt)("inlineCode",{parentName:"p"},"y_col")," - the column of the ",(0,r.kt)("inlineCode",{parentName:"p"},"db2"),". If ",(0,r.kt)("inlineCode",{parentName:"p"},"slice_val")," is passed, then the ",(0,r.kt)("inlineCode",{parentName:"p"},"slice_id")," is searched for each ",(0,r.kt)("a",{parentName:"p",href:"/docs/docs_data_analysis/next/error_analysis/statistics#citrosdata-object"},(0,r.kt)("strong",{parentName:"a"},"CitrosData"))," objects."),(0,r.kt)("p",null,"Let's query for topic 'B', scale it over 20 points and plot correlation between 'data.x.x_2' of ",(0,r.kt)("inlineCode",{parentName:"p"},"db_sc")," vs. 'data.x.x_1' of ",(0,r.kt)("inlineCode",{parentName:"p"},"db_sc_B")," near the point 'data.time' = 0.7:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"#download columns 'data.x' and 'data.time' for topic 'B'\ndf_B = citros.topic('B').data(['data.x', 'data.time'])\n\n#construct CitrosData object with 3 data-columns from 'data.x'\ndataset_B = analysis.CitrosData(df, data_label=['data.x'], units = 'm')\n\n#scale data\ndb_sc_B = dataset.scale_data(n_points = 20, \n                             param_label = 'data.time', \n                             show_fig = False)\n                             \ndb_sc.show_correlation(db2 = db_sc_B,\n                       x_col = 'data.x.x_2',\n                       y_col = 'data.x.x_1',\n                       slice_val = 0.7,\n                       n_std = [1,2,3])\n")),(0,r.kt)("p",null,"The output is:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-text"},"slice_id = 34,\nslice_val = 0.694,\nslice_id_2 = 13,\nslice_val_2 = 0.684\n")),(0,r.kt)("details",null,(0,r.kt)("summary",null,"Show the plot:"),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"fig10",src:a(485).Z,title:"Fig10",width:"669",height:"547"}))))}u.isMDXComponent=!0},485:(e,t,a)=>{a.d(t,{Z:()=>n});const n=a.p+"assets/images/fig10-d50185dc0b4747c47bddbb0b74a27a0d.png"},4305:(e,t,a)=>{a.d(t,{Z:()=>n});const n=a.p+"assets/images/fig7-7f315825754f63e51adeab88eecb3b7c.png"},9657:(e,t,a)=>{a.d(t,{Z:()=>n});const n=a.p+"assets/images/fig8-e76d8376b93413a1684557e4ccceb49a.png"}}]);
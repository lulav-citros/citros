"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[9222],{3905:(e,n,t)=>{t.d(n,{Zo:()=>p,kt:()=>f});var a=t(7294);function r(e,n,t){return n in e?Object.defineProperty(e,n,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[n]=t,e}function i(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);n&&(a=a.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,a)}return t}function o(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?i(Object(t),!0).forEach((function(n){r(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):i(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}function l(e,n){if(null==e)return{};var t,a,r=function(e,n){if(null==e)return{};var t,a,r={},i=Object.keys(e);for(a=0;a<i.length;a++)t=i[a],n.indexOf(t)>=0||(r[t]=e[t]);return r}(e,n);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(a=0;a<i.length;a++)t=i[a],n.indexOf(t)>=0||Object.prototype.propertyIsEnumerable.call(e,t)&&(r[t]=e[t])}return r}var u=a.createContext({}),s=function(e){var n=a.useContext(u),t=n;return e&&(t="function"==typeof e?e(n):o(o({},n),e)),t},p=function(e){var n=s(e.components);return a.createElement(u.Provider,{value:n},e.children)},c="mdxType",m={inlineCode:"code",wrapper:function(e){var n=e.children;return a.createElement(a.Fragment,{},n)}},d=a.forwardRef((function(e,n){var t=e.components,r=e.mdxType,i=e.originalType,u=e.parentName,p=l(e,["components","mdxType","originalType","parentName"]),c=s(t),d=r,f=c["".concat(u,".").concat(d)]||c[d]||m[d]||i;return t?a.createElement(f,o(o({ref:n},p),{},{components:t})):a.createElement(f,o({ref:n},p))}));function f(e,n){var t=arguments,r=n&&n.mdxType;if("string"==typeof e||r){var i=t.length,o=new Array(i);o[0]=d;var l={};for(var u in n)hasOwnProperty.call(n,u)&&(l[u]=n[u]);l.originalType=e,l[c]="string"==typeof e?e:r,o[1]=l;for(var s=2;s<i;s++)o[s]=t[s];return a.createElement.apply(null,o)}return a.createElement.apply(null,t)}d.displayName="MDXCreateElement"},8578:(e,n,t)=>{t.r(n),t.d(n,{assets:()=>u,contentTitle:()=>o,default:()=>m,frontMatter:()=>i,metadata:()=>l,toc:()=>s});var a=t(7462),r=(t(7294),t(3905));const i={},o="Adding Functions to Parameter Setup",l={unversionedId:"guides/config_params",id:"guides/config_params",title:"Adding Functions to Parameter Setup",description:"In order to define a function in your parameter setup file, simply replace any constant parameter value with a function object.",source:"@site/docs/guides/config_params.md",sourceDirName:"guides",slug:"/guides/config_params",permalink:"/docs/guides/config_params",draft:!1,tags:[],version:"current",frontMatter:{},sidebar:"gettingStartedSidebar",previous:{title:"run",permalink:"/docs/commands/simulation/run"},next:{title:"Getting Started",permalink:"/docs/guides/getting_started"}},u={},s=[{value:"How to Add Function Objects",id:"how-to-add-function-objects",level:2},{value:"Numpy Functions",id:"numpy-functions",level:3},{value:"Simple Arithmetic",id:"simple-arithmetic",level:4},{value:"Using Random Distribution",id:"using-random-distribution",level:4},{value:"User-Defined Functions",id:"user-defined-functions",level:3},{value:"Read from a CSV File",id:"read-from-a-csv-file",level:4},{value:"Function with CITROS Context",id:"function-with-citros-context",level:4},{value:"Full parameter_setup.json Example",id:"full-parameter_setupjson-example",level:3},{value:"Pitfalls and Gotchas",id:"pitfalls-and-gotchas",level:2},{value:"User-Defined Functions",id:"user-defined-functions-1",level:3},{value:"Numpy functions",id:"numpy-functions-1",level:3},{value:"General Pitfalls",id:"general-pitfalls",level:3}],p={toc:s},c="wrapper";function m(e){let{components:n,...t}=e;return(0,r.kt)(c,(0,a.Z)({},p,t,{components:n,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"adding-functions-to-parameter-setup"},"Adding Functions to Parameter Setup"),(0,r.kt)("p",null,"In order to define a function in your parameter setup file, simply replace any constant parameter value with a ",(0,r.kt)("inlineCode",{parentName:"p"},"function object"),"."),(0,r.kt)("p",null,"Function objects provide a powerful and dynamic way to compute and set values in the parameter_setup.json file for ROS 2 nodes. This feature allows for much greater flexibility and dynamism when setting parameters."),(0,r.kt)("h2",{id:"how-to-add-function-objects"},"How to Add Function Objects"),(0,r.kt)("p",null,"Function objects are essentially references to functions (either from numpy or user-defined) that will be executed to compute a value for a particular key."),(0,r.kt)("h3",{id:"numpy-functions"},"Numpy Functions"),(0,r.kt)("p",null,"To use a numpy function, simply provide its fully qualified name as the value in the dictionary. For example:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},'{\n    "my_param": {\n        "function": "numpy.add",\n        "args": [1, 2]\n    }\n}\n')),(0,r.kt)("details",null,(0,r.kt)("summary",null,"Examples"),(0,r.kt)("h4",{id:"simple-arithmetic"},"Simple Arithmetic"),(0,r.kt)("p",null,"compute the product of two numbers:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},'{\n    "product_param": {\n        "function": "numpy.multiply",\n        "args": [4, 7]\n    }\n}\n')),(0,r.kt)("h4",{id:"using-random-distribution"},"Using Random Distribution"),(0,r.kt)("p",null,"Generating a random number from a normal distribution with a mean of 0 and standard deviation of 1:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},'{\n    "random_param": {\n        "function": "numpy.random.normal",\n        "args": [0, 1]\n    }\n}\n')),(0,r.kt)("p",null,"Drawing a random value between 1 and 10:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},'{\n    "low": 1.0,\n    "high": 10.0,\n    "uniform_random_param": {\n        "function": "numpy.random.uniform",\n        "args": ["low", "high"]\n    }\n}\n'))),(0,r.kt)("h3",{id:"user-defined-functions"},"User-Defined Functions"),(0,r.kt)("p",null,"For user-defined functions, you need to:"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"Define your function in a separate ",(0,r.kt)("inlineCode",{parentName:"li"},".py")," file and place it under ",(0,r.kt)("inlineCode",{parentName:"li"},".citros/parameter_setups/functions"),"."),(0,r.kt)("li",{parentName:"ul"},"Use the file name (with the ",(0,r.kt)("inlineCode",{parentName:"li"},".py")," extension) followed by the function name, separated by a colon, as the value of the ",(0,r.kt)("inlineCode",{parentName:"li"},"function")," key.")),(0,r.kt)("p",null,"For instance, if you have a function named ",(0,r.kt)("inlineCode",{parentName:"p"},"my_function")," in a file named ",(0,r.kt)("inlineCode",{parentName:"p"},"my_functions.py"),", you would reference it as:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},'{\n    "my_param": {\n        "function": "my_functions.py:my_function",\n        "args": [...]\n    }\n}\n')),(0,r.kt)("details",null,(0,r.kt)("summary",null,"Examples"),(0,r.kt)("h4",{id:"read-from-a-csv-file"},"Read from a CSV File"),(0,r.kt)("p",null,"Suppose you want to load a matrix from a csv file into a parameter of type list of lists of floats. Copy the following function to a python file (let's call it ",(0,r.kt)("inlineCode",{parentName:"p"},"file_utils.py"),") and place it in the ",(0,r.kt)("inlineCode",{parentName:"p"},"functions")," directory:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"def load_matrix_from_csv(filename):\n    import csv\n    with open(filename, 'r') as f:\n        reader = csv.reader(f)\n        matrix = [list(map(float, row)) for row in reader]\n    return matrix\n")),(0,r.kt)("p",null,"Reference it in your parameter_setup.json as:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},'{\n    "matrix_param": {\n        "function": "file_utils.py:load_matrix_from_csv",\n        "args": ["my_data.csv"]\n    }\n}\n')),(0,r.kt)("h4",{id:"function-with-citros-context"},"Function with CITROS Context"),(0,r.kt)("p",null,"Sometimes you may want to access some information that is part of the CITROS context. For example, you may want to write a user-defined function that uses the run index of the simulation being run. In such a case, you could write a function with a parameter named ",(0,r.kt)("inlineCode",{parentName:"p"},"citros_context")," (which must appear last in the parameter list):"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},"def func_with_context(num, citros_context):\n    return num + float(citros_context['run_id'])\n")),(0,r.kt)("p",null,(0,r.kt)("inlineCode",{parentName:"p"},"citros_context")," is a dictionary with key/value pairs describing the current CITROS context. Currently the only key is ",(0,r.kt)("inlineCode",{parentName:"p"},"run_id"),", but more may be added in the future. Then, you would call it from your ",(0,r.kt)("inlineCode",{parentName:"p"},"parameter_setup.json")," file:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},'"init_speed": {\n    "function": "my_func.py:func_with_context",\n    "args": [50.0]\n}\n')),(0,r.kt)("p",null,"Notice that the argument for ",(0,r.kt)("inlineCode",{parentName:"p"},"citros_context")," is added automatically for you - the ",(0,r.kt)("inlineCode",{parentName:"p"},"args")," list only contains the argument for the first parameter (",(0,r.kt)("inlineCode",{parentName:"p"},"num"),").")),(0,r.kt)("h3",{id:"full-parameter_setupjson-example"},"Full parameter_setup.json Example"),(0,r.kt)("p",null,"Using the following parameter setup file, the ",(0,r.kt)("inlineCode",{parentName:"p"},"init_angle")," parameter in the ",(0,r.kt)("inlineCode",{parentName:"p"},"analytic_dynamics")," node of the ",(0,r.kt)("inlineCode",{parentName:"p"},"cannon_analytic")," package (taken from the ",(0,r.kt)("inlineCode",{parentName:"p"},"cannon")," project), will get a random value each time the simulation is run. Specifically, 60% of the evaluated values will be between 30 and 60 degrees (a standard deviation of 15 around 45). In addition, the parameter ",(0,r.kt)("inlineCode",{parentName:"p"},"init_speed")," will be evaluated to 50.0 on the first run, and will be incremented by one for every subsequent run (see previous example for details):"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},'{\n    "packages": {\n        "cannon_analytic": {\n            "analytic_dynamics": {\n                "ros__parameters": {\n                    "init_speed": {\n                        "function": "my_func.py:func_with_context",\n                        "args": [50.0]\n                    },\n                    "init_angle": {\n                        "function": "numpy.random.normal",\n                        "args": [45, 15]\n                    },\n                    "dt": 0.01\n                }\n            }\n        },\n        "cannon_numeric": {\n            "numeric_dynamics": {\n                "ros__parameters": {\n                    "init_speed": 50.0,\n                    "init_angle": 30.0,\n                    "dt": 0.01\n                }\n            }\n        },\n        "scheduler": {\n            "scheduler": {\n                "ros__parameters": {\n                    "dt": 0.1\n                }\n            }\n        }\n    }\n}\n')),(0,r.kt)("p",null,"So, for example, if you run the following command in the ",(0,r.kt)("inlineCode",{parentName:"p"},"cannon")," project:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},'citros run -n "my_batch_name" -m "some message" -c 10\n')),(0,r.kt)("p",null,"and choose ",(0,r.kt)("inlineCode",{parentName:"p"},"simulation_cannon_analytic"),", the simulation will be run 10 times, and each time ",(0,r.kt)("inlineCode",{parentName:"p"},"init_angle")," and ",(0,r.kt)("inlineCode",{parentName:"p"},"init_speed")," will be evaluated to different values. You can see for yourself the evaluated values if you open the ",(0,r.kt)("inlineCode",{parentName:"p"},"cannon_analytic.yaml")," under ",(0,r.kt)("inlineCode",{parentName:"p"},".citors/runs/simulation_cannon_analytic/my_batch_name/0/config"),", after the run has finished."),(0,r.kt)("h2",{id:"pitfalls-and-gotchas"},"Pitfalls and Gotchas"),(0,r.kt)("h3",{id:"user-defined-functions-1"},"User-Defined Functions"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("strong",{parentName:"li"},"Import Handling")," - Always perform imports inside the function. This ensures the function has all the necessary dependencies when called."),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("strong",{parentName:"li"},"Return Types")," - The function should return native Python types or numpy scalars. Avoid returning non-scalar numpy values."),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("strong",{parentName:"li"},"Function Path")," - Only the file name where the function is defined is needed (including the ",(0,r.kt)("inlineCode",{parentName:"li"},".py")," suffix). Avoid including directory paths."),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("strong",{parentName:"li"},"CITROS context")," - if you're using the ",(0,r.kt)("inlineCode",{parentName:"li"},"citros_context")," parameter in your user-defined function, make sure to add it ",(0,r.kt)("em",{parentName:"li"},"last")," in the function's parameter list.")),(0,r.kt)("h3",{id:"numpy-functions-1"},"Numpy functions"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},"Always use the fully qualified name for numpy functions, such as numpy.random.exponential.")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},"Make sure you use numpy functions such that a scalar is returned. For example, when using ",(0,r.kt)("a",{parentName:"p",href:"https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html"},"numpy.random.rand"),", make sure to have an empty argument list:"),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre",className:"language-bash"},'"pos_x": {\n        "function": "numpy.random.rand",\n        "args": []\n    }\n')),(0,r.kt)("p",{parentName:"li"},"  ...since the arguments are the dimensions of the output array. No arguments will return a native scalar, which is what we want. "),(0,r.kt)("p",{parentName:"li"},"  If you need to return an array, you can write your own user-defined function that wraps the numpy function and converts the numpy array to a native python array."))),(0,r.kt)("h3",{id:"general-pitfalls"},"General Pitfalls"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},(0,r.kt)("strong",{parentName:"p"},"Multi-Level Key References")," - When referencing a dictionary key from a function, if the key is not unique across the dictionary, use a multi-level key string to differentiate it, separating dictionary levels with ",(0,r.kt)("inlineCode",{parentName:"p"},"'.'"),". For example: "),(0,r.kt)("pre",{parentName:"li"},(0,r.kt)("code",{parentName:"pre"},'  {\n      "outer": {\n          "inner_a": 5,\n          "inner_b": {\n              "function": "numpy.add",\n              "args": ["inner_a", 3]\n          }\n      },\n      "sum": {\n          "inner_b" : 42,\n          "function": "numpy.add",\n          "args": ["outer.inner_b", 2]\n      }\n  }\n'))),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},(0,r.kt)("strong",{parentName:"p"},"Circular Dependencies")," - Be wary of creating circular dependencies with key references. This will result in a runtime error.")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},(0,r.kt)("strong",{parentName:"p"},"Expected Return Types")," - Ensure that the functions you use, be they numpy or user-defined, return the value type your ROS simulation expects. Mismatches (e.g., returning an integer when a float is expected) can cause errors in your simulation."))))}m.isMDXComponent=!0}}]);
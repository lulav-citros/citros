"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[12398],{3905:(e,t,n)=>{n.d(t,{Zo:()=>p,kt:()=>k});var a=n(67294);function r(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function o(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);t&&(a=a.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,a)}return n}function i(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?o(Object(n),!0).forEach((function(t){r(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):o(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function s(e,t){if(null==e)return{};var n,a,r=function(e,t){if(null==e)return{};var n,a,r={},o=Object.keys(e);for(a=0;a<o.length;a++)n=o[a],t.indexOf(n)>=0||(r[n]=e[n]);return r}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(a=0;a<o.length;a++)n=o[a],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(r[n]=e[n])}return r}var l=a.createContext({}),c=function(e){var t=a.useContext(l),n=t;return e&&(n="function"==typeof e?e(t):i(i({},t),e)),n},p=function(e){var t=c(e.components);return a.createElement(l.Provider,{value:t},e.children)},u="mdxType",m={inlineCode:"code",wrapper:function(e){var t=e.children;return a.createElement(a.Fragment,{},t)}},d=a.forwardRef((function(e,t){var n=e.components,r=e.mdxType,o=e.originalType,l=e.parentName,p=s(e,["components","mdxType","originalType","parentName"]),u=c(n),d=r,k=u["".concat(l,".").concat(d)]||u[d]||m[d]||o;return n?a.createElement(k,i(i({ref:t},p),{},{components:n})):a.createElement(k,i({ref:t},p))}));function k(e,t){var n=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var o=n.length,i=new Array(o);i[0]=d;var s={};for(var l in t)hasOwnProperty.call(t,l)&&(s[l]=t[l]);s.originalType=e,s[u]="string"==typeof e?e:r,i[1]=s;for(var c=2;c<o;c++)i[c]=n[c];return a.createElement.apply(null,i)}return a.createElement.apply(null,n)}d.displayName="MDXCreateElement"},78227:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>l,contentTitle:()=>i,default:()=>m,frontMatter:()=>o,metadata:()=>s,toc:()=>c});var a=n(87462),r=(n(67294),n(3905));const o={sidebar_position:2,sidebar_label:"CITROS in Dockerfile"},i="CITROS in Dockerfile",s={unversionedId:"guides/dockerfile_overview",id:"version-0.2.51/guides/dockerfile_overview",title:"CITROS in Dockerfile",description:"After configuring the simulation environment and conducting a local simulation using CITROS CLI, the next step is to enhance CITROS' capabilities by deploying the simulation environment to the cloud.",source:"@site/versioned_docs/version-0.2.51/guides/dockerfile_overview.md",sourceDirName:"guides",slug:"/guides/dockerfile_overview",permalink:"/docs/guides/dockerfile_overview",draft:!1,tags:[],version:"0.2.51",sidebarPosition:2,frontMatter:{sidebar_position:2,sidebar_label:"CITROS in Dockerfile"},sidebar:"gettingStartedSidebar",previous:{title:"Adding Functions to Parameter Setup",permalink:"/docs/guides/config_params"},next:{title:"Visualize with Foxglove",permalink:"/docs/guides/foxglove_visual"}},l={},c=[{value:"Table Of Contents",id:"table-of-contents",level:2},{value:"About Dockerfiles",id:"about-dockerfiles",level:2},{value:"Write Your Own Dockerfile",id:"write-your-own-dockerfile",level:2},{value:"Required Packages for CITROS Usage",id:"required-packages-for-citros-usage",level:2},{value:"Examples",id:"examples",level:2}],p={toc:c},u="wrapper";function m(e){let{components:t,...o}=e;return(0,r.kt)(u,(0,a.Z)({},p,o,{components:t,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"citros-in-dockerfile"},"CITROS in Dockerfile"),(0,r.kt)("p",null,"After configuring the simulation environment and conducting a local simulation using ",(0,r.kt)("a",{parentName:"p",href:"https://citros.io/doc/docs_cli"},"CITROS CLI"),", the next step is to enhance CITROS' capabilities by deploying the simulation environment to the cloud."),(0,r.kt)("p",null,"Cloud deployment provides the flexibility to execute multiple parallel simulations, each with predefined parameter distributions. This facilitates Monte-Carlo analysis and leverages the machine learning capabilities of CITROS."),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"jpeg",src:n(35644).Z,width:"389",height:"129"})),(0,r.kt)("h2",{id:"table-of-contents"},"Table Of Contents"),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"#about-dockerfiles"},"About Dockerfiles")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"#write-your-own-dockerfile"},"Write Your Own Dockerfile")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"#required-packages-for-citros-usage"},"Required Packages for CITROS Usage")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"#examples"},"Examples"))),(0,r.kt)("h2",{id:"about-dockerfiles"},"About Dockerfiles"),(0,r.kt)("p",null,(0,r.kt)("a",{parentName:"p",href:"https://docs.docker.com/get-started/02_our_app/"},"Dockerfiles")," are essential components when deploying your CITROS simulation environment on the cloud. A Dockerfile is a text file that contains a set of instructions to build a Docker container image.\nThese images encapsulate all the necessary software, libraries, and dependencies required to run your application consistently across different environments. By utilizing Dockerfiles, you can ensure that your simulation environment remains reproducible, scalable, and easily deployable on cloud platforms. Whether you're performing Monte-Carlo analysis or harnessing machine learning capabilities, Dockerfiles play a crucial role in streamlining the deployment process and maximizing CITROS' potential."),(0,r.kt)("h2",{id:"write-your-own-dockerfile"},"Write Your Own Dockerfile"),(0,r.kt)("p",null,"Creating a customized Dockerfile tailored to your CITROS simulation environment is a fundamental step in harnessing the full power of cloud deployment. A well-crafted Dockerfile allows you to define the exact configuration and dependencies your simulation needs, ensuring a consistent and reliable execution environment. The Dockerfile should build and install all the relevant libraries, packages and source code as the local simulation environment.\nHere are the key steps to write your Dockerfile:"),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("p",{parentName:"li"},(0,r.kt)("strong",{parentName:"p"},"Select a Base Image:")," Begin by choosing a base image that matches your application's requirements. The base image serves as the starting point for your container and may include an operating system and pre-installed software.")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("p",{parentName:"li"},(0,r.kt)("strong",{parentName:"p"},"Install Required Packages:")," Use the ",(0,r.kt)("a",{parentName:"p",href:"https://docs.docker.com/engine/reference/builder/#run"},(0,r.kt)("inlineCode",{parentName:"a"},"RUN"))," instruction to install any necessary packages, libraries, and tools. You can also copy any custom scripts or configurations into the container.")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("p",{parentName:"li"},(0,r.kt)("strong",{parentName:"p"},"Set Environment Variables:")," Use the ",(0,r.kt)("a",{parentName:"p",href:"https://docs.docker.com/engine/reference/builder/#env"},(0,r.kt)("inlineCode",{parentName:"a"},"ENV"))," instruction to define environment variables that your application relies on. This ensures proper configuration within the container.")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("p",{parentName:"li"},(0,r.kt)("strong",{parentName:"p"},"Specify the Entry Point:")," Use the ",(0,r.kt)("a",{parentName:"p",href:"https://docs.docker.com/engine/reference/builder/#cmd"},(0,r.kt)("inlineCode",{parentName:"a"},"CMD"))," or ",(0,r.kt)("a",{parentName:"p",href:"https://docs.docker.com/engine/reference/builder/#entrypoint"},(0,r.kt)("inlineCode",{parentName:"a"},"ENTRYPOINT"))," instruction to define the command that should be executed when the container starts. This is typically the command to run your CITROS simulation.")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("p",{parentName:"li"},(0,r.kt)("strong",{parentName:"p"},"Build the Docker Image:")," Use the ",(0,r.kt)("inlineCode",{parentName:"p"},"docker build")," command to build your Docker image, referencing your Dockerfile. This command will create an image containing your CITROS environment.\nFor example:"))),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-bash"},"docker build -t cannon .\n")),(0,r.kt)("ol",{start:6},(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("strong",{parentName:"li"},"Run Tests"),": Use the ",(0,r.kt)("inlineCode",{parentName:"li"},"docker run")," command with the image tag and the required simulation to locally run your simulation image, verifying the setup works before pushing the image to CITROS.\nFor Example:")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-bash"},"docker run --network=host -it --rm cannon citros run cannon_analytic.launch.py\n")),(0,r.kt)("ol",{start:7},(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("strong",{parentName:"li"},"Push Your Image to CITROS:")," Use ",(0,r.kt)("a",{parentName:"li",href:"https://citros.io/doc/docs_cli/commands/cli_commands#command-docker-build-push"},(0,r.kt)("inlineCode",{parentName:"a"},"citros docker-build-push"))," command to build and push your docker image to CITROS.")),(0,r.kt)("p",null,"Once the upload of the docker image is done, you can check on CITROS ",(0,r.kt)("a",{parentName:"p",href:"https://citros.io/images"},"Image tab")," that the image exists."),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"jpeg",src:n(68359).Z,width:"1600",height:"724"})),(0,r.kt)("admonition",{type:"tip"},(0,r.kt)("p",{parentName:"admonition"},"When writing your Dockerfile, it is advised to build your ROS workspace in the Dockerfile.\nYou can copy the ",(0,r.kt)("inlineCode",{parentName:"p"},"ros_ws/src")," folder and use ",(0,r.kt)("inlineCode",{parentName:"p"},"colcon build")," to build the code:"),(0,r.kt)("pre",{parentName:"admonition"},(0,r.kt)("code",{parentName:"pre",className:"language-dockerfile"},"COPY ros_ws/src ros_ws/src\nRUN cd ros_ws && colcon build\n"))),(0,r.kt)("admonition",{type:"tip"},(0,r.kt)("p",{parentName:"admonition"},"To avoid path errors, use the ",(0,r.kt)("inlineCode",{parentName:"p"},"WORKDIR")," command to specify the container's default working directory to be the same as the local environment.\nFor example the ",(0,r.kt)("a",{parentName:"p",href:"https://github.com/citros-garden/cannon"},"cannon")," project:"),(0,r.kt)("pre",{parentName:"admonition"},(0,r.kt)("code",{parentName:"pre",className:"language-dockerfile"},"WORKDIR /workspaces/cannon\nCOPY src src\nRUN colcon build\n"))),(0,r.kt)("h2",{id:"required-packages-for-citros-usage"},"Required Packages for CITROS Usage"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"citros"),": This will allow CITROS to run the simulation image on the CITROS servers.\nInstall with:")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-dockerfile"},"RUN pip install citros\n")),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"rosbag2-storage-mcap"),"(Optional): For recording bags using ",(0,r.kt)("a",{parentName:"li",href:"https://mcap.dev/guides/getting-started/ros-2"},(0,r.kt)("inlineCode",{parentName:"a"},"mcap"))," format.\nInstall with:")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-dockerfile"},"RUN apt-get update && apt-get install -y ros-${ROS_DISTRO}-rosbag2-storage-mcap\n")),(0,r.kt)("h2",{id:"examples"},"Examples"),(0,r.kt)("p",null,"Each ",(0,r.kt)("a",{parentName:"p",href:"https://github.com/citros-garden"},"CITROS Garden")," project contain Dockerfile for CITROS usage. "),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("a",{parentName:"li",href:"https://github.com/citros-garden/mass_spring_damper/blob/main/Dockerfile"},"Basic ROS 2 project")," (Mass-Spring-Damper):")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-dockerfile"},'FROM ros:humble\n\nENV ROS_DISTRO humble\nENV DEBIAN_FRONTEND=noninteractive\n\n# install citros\nRUN apt update && apt install -y python3-pip\nRUN pip install citros\n\n# copy and build workspace\nWORKDIR /app\nCOPY src src\n\nRUN colcon build\nRUN echo "source /app/install/setup.bash" >> ~/.bashrc\n\nCOPY ros2_entrypoint.sh ros2_entrypoint.sh\nRUN chmod +x ros2_entrypoint.sh\nENTRYPOINT ["/app/ros2_entrypoint.sh"]\n\nCMD ["bash"]\n')),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("a",{parentName:"li",href:"https://github.com/citros-garden/drone/blob/main/Dockerfile"},"Gazebo - ROS 2 Example"))),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-dockerfile"},'FROM althack/ros2:humble-gazebo-nvidia \n\nENV DEBIAN_FRONTEND=noninteractive\n\n# install utils\nRUN apt-get update && apt-get install -y \\\n  bash-completion \\\n  build-essential \\\n  cmake \\\n  gdb \\\n  git \\\n  python3-argcomplete \\\n  python3-pip \\\n  nano \\\n  wget \\\n  curl \\\n  autoconf \\\n  automake \\\n  libtool \\\n  make \\\n  g++ \\\n  unzip \\\n  sudo \\ \n  openssh-server \\\n  gnupg \\\n  gdb-multiarch \\\n  default-jre \\\n  python3 \\\n  python3-setuptools \\\n  python3-vcstool \\\n  python3-colcon-common-extensions \\\n  python3-rosdep \\\n  mesa-utils \\\n  x11-apps \\\n  libcanberra-gtk* \\\n  libglfw3-dev \\\n  libglew-dev \\\n  libgl1-mesa-glx \\\n  libgl1-mesa-dri \\\n  ros-humble-rosbridge-suite \\\n  ros-humble-rosidl* \\\n  ros-humble-rosbag2-storage-mcap \\\n  gazebo \\\n  && rm -rf /var/lib/apt/lists/* \\\n  && echo "source /usr/share/bash-completion/completions/git" >> /home/$USERNAME/.bashrc\n\nRUN pip install citros xmltodict\n\n# define the workdir\nWORKDIR /workspaces/drone\n\n# build ros workspace\nCOPY ros2_ws/src ros2_ws/src\nRUN  . /opt/ros/${ROS_DISTRO}/setup.sh && \\\n     cd ros2_ws && \\\n     colcon build\n\n# finial setup\nCOPY ros2_entrypoint.sh ros2_entrypoint.sh\nRUN chmod +x ros2_entrypoint.sh\n\nRUN echo "source /workspaces/drone/ros2_ws/install/local_setup.bash" >> /home/$USERNAME/.bashrc\n\nENTRYPOINT ["/workspaces/drone/ros2_entrypoint.sh"]\n\nCMD ["bash"]\n')))}m.isMDXComponent=!0},35644:(e,t,n)=>{n.d(t,{Z:()=>a});const a="data:image/jpeg;base64,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"},68359:(e,t,n)=>{n.d(t,{Z:()=>a});const a=n.p+"assets/images/images-1936fd22756e0aea770123530f14a9f9.jpeg"}}]);
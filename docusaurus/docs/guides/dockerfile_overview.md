---
sidebar_position: 2
sidebar_label: 'CITROS in Dockerfile'
---

#  CITROS in Dockerfile

After configuring the simulation environment and conducting a local simulation using [CITROS CLI](https://citros.io/doc/docs_cli), the next step is to enhance CITROS' capabilities by deploying the simulation environment to the cloud.

Cloud deployment provides the flexibility to execute multiple parallel simulations, each with predefined parameter distributions. This facilitates Monte-Carlo analysis and leverages the machine learning capabilities of CITROS.

![jpeg](img/docker-system.jpeg)

## Table Of Contents

1. [About Dockerfiles](#about-dockerfiles)
2. [Write Your Own Dockerfile](#write-your-own-dockerfile)
3. [Required Packages for CITROS Usage](#required-packages-for-citros-usage)
4. [Examples](#examples)

## About Dockerfiles

[Dockerfiles](https://docs.docker.com/get-started/02_our_app/) are essential components when deploying your CITROS simulation environment on the cloud. A Dockerfile is a text file that contains a set of instructions to build a Docker container image. 
These images encapsulate all the necessary software, libraries, and dependencies required to run your application consistently across different environments. By utilizing Dockerfiles, you can ensure that your simulation environment remains reproducible, scalable, and easily deployable on cloud platforms. Whether you're performing Monte-Carlo analysis or harnessing machine learning capabilities, Dockerfiles play a crucial role in streamlining the deployment process and maximizing CITROS' potential.

## Write Your Own Dockerfile

Creating a customized Dockerfile tailored to your CITROS simulation environment is a fundamental step in harnessing the full power of cloud deployment. A well-crafted Dockerfile allows you to define the exact configuration and dependencies your simulation needs, ensuring a consistent and reliable execution environment. The Dockerfile should build and install all the relevant libraries, packages and source code as the local simulation environment.
Here are the key steps to write your Dockerfile:

1. **Select a Base Image:** Begin by choosing a base image that matches your application's requirements. The base image serves as the starting point for your container and may include an operating system and pre-installed software.

2. **Install Required Packages:** Use the [`RUN`](https://docs.docker.com/engine/reference/builder/#run) instruction to install any necessary packages, libraries, and tools. You can also copy any custom scripts or configurations into the container.

3. **Set Environment Variables:** Use the [`ENV`](https://docs.docker.com/engine/reference/builder/#env) instruction to define environment variables that your application relies on. This ensures proper configuration within the container.

4. **Specify the Entry Point:** Use the [`CMD`](https://docs.docker.com/engine/reference/builder/#cmd) or [`ENTRYPOINT`](https://docs.docker.com/engine/reference/builder/#entrypoint) instruction to define the command that should be executed when the container starts. This is typically the command to run your CITROS simulation.

5. **Build the Docker Image:** Use the `docker build` command to build your Docker image, referencing your Dockerfile. This command will create an image containing your CITROS environment.
For example:
```bash
docker build -t cannon .
```

6. **Run Tests**: Use the `docker run` command with the image tag and the required simulation to locally run your simulation image, verifying the setup works before pushing the image to CITROS.
For Example:
```bash
docker run --network=host -it --rm cannon citros run cannon_analytic.launch.py
```

7. **Push Your Image to CITROS:** Use [`citros docker-build-push`](https://citros.io/doc/docs_cli/commands/cli_commands#command-docker-build-push) command to build and push your docker image to CITROS.

Once the upload of the docker image is done, you can check on CITROS [Image tab](https://citros.io/images) that the image exists.

![jpeg](img/images.jpeg)

:::tip

When writing your Dockerfile, it is advised to build your ROS workspace in the Dockerfile.
You can copy the `ros_ws/src` folder and use `colcon build` to build the code:

```dockerfile
COPY ros_ws/src ros_ws/src
RUN cd ros_ws && colcon build
```

:::

:::tip

To avoid path errors, use the `WORKDIR` command to specify the container's default working directory to be the same as the local environment. 
For example the [cannon](https://github.com/citros-garden/cannon) project:
```dockerfile
WORKDIR /workspaces/cannon
COPY src src
RUN colcon build
```

:::

## Required Packages for CITROS Usage

* `citros`: This will allow CITROS to run the simulation image on the CITROS servers. 
Install with:
```dockerfile
RUN pip install citros
```
* `rosbag2-storage-mcap`(Optional): For recording bags using [`mcap`](https://mcap.dev/guides/getting-started/ros-2) format. 
Install with:
```dockerfile
RUN apt-get update && apt-get install -y ros-${ROS_DISTRO}-rosbag2-storage-mcap
```

## Examples
Each [CITROS Garden](https://github.com/citros-garden) project contain Dockerfile for CITROS usage. 


* [Basic ROS 2 project](https://github.com/citros-garden/mass_spring_damper/blob/main/Dockerfile) (Mass-Spring-Damper):
```dockerfile
FROM ros:humble

ENV ROS_DISTRO humble
ENV DEBIAN_FRONTEND=noninteractive

# install citros
RUN apt update && apt install -y python3-pip
RUN pip install citros

# copy and build workspace
WORKDIR /app
COPY src src

RUN colcon build
RUN echo "source /app/install/setup.bash" >> ~/.bashrc

COPY ros2_entrypoint.sh ros2_entrypoint.sh
RUN chmod +x ros2_entrypoint.sh
ENTRYPOINT ["/app/ros2_entrypoint.sh"]

CMD ["bash"]
```

* [Gazebo - ROS 2 Example](https://github.com/citros-garden/drone/blob/main/Dockerfile)

```dockerfile
FROM althack/ros2:humble-gazebo-nvidia 

ENV DEBIAN_FRONTEND=noninteractive

# install utils
RUN apt-get update && apt-get install -y \
  bash-completion \
  build-essential \
  cmake \
  gdb \
  git \
  python3-argcomplete \
  python3-pip \
  nano \
  wget \
  curl \
  autoconf \
  automake \
  libtool \
  make \
  g++ \
  unzip \
  sudo \ 
  openssh-server \
  gnupg \
  gdb-multiarch \
  default-jre \
  python3 \
  python3-setuptools \
  python3-vcstool \
  python3-colcon-common-extensions \
  python3-rosdep \
  mesa-utils \
  x11-apps \
  libcanberra-gtk* \
  libglfw3-dev \
  libglew-dev \
  libgl1-mesa-glx \
  libgl1-mesa-dri \
  ros-humble-rosbridge-suite \
  ros-humble-rosidl* \
  ros-humble-rosbag2-storage-mcap \
  gazebo \
  && rm -rf /var/lib/apt/lists/* \
  && echo "source /usr/share/bash-completion/completions/git" >> /home/$USERNAME/.bashrc

RUN pip install citros xmltodict

# define the workdir
WORKDIR /workspaces/drone

# build ros workspace
COPY ros2_ws/src ros2_ws/src
RUN  . /opt/ros/${ROS_DISTRO}/setup.sh && \
     cd ros2_ws && \
     colcon build

# finial setup
COPY ros2_entrypoint.sh ros2_entrypoint.sh
RUN chmod +x ros2_entrypoint.sh

RUN echo "source /workspaces/drone/ros2_ws/install/local_setup.bash" >> /home/$USERNAME/.bashrc

ENTRYPOINT ["/workspaces/drone/ros2_entrypoint.sh"]

CMD ["bash"]
```
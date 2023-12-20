FROM vovalulav/ros2:humble-dev

# ** [Optional] Uncomment this section to install additional packages. **
#
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
    && apt-get -y install --no-install-recommends postgresql \
    libpq-dev \
    #
    # Clean up
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*
ENV DEBIAN_FRONTEND=dialog

# Set up auto-source of workspace for ros user
ARG WORKSPACE
RUN echo "if [ -f ${WORKSPACE}/install/setup.bash ]; then source ${WORKSPACE}/install/setup.bash; fi" >> /home/ros/.bashrc
# Fixing building error
RUN pip install setuptools==58.2.0 psycopg2 requests python-decouple rosbags tqdm
# download rosbridge for Foxglove monitoring

RUN apt update && apt-get install -y ros-humble-rosbridge-suite 
RUN apt update && apt-get install -y ros-humble-rosbridge-suite ros-humble-rosbag2-storage-mcap

RUN mkdir /run/user/1000
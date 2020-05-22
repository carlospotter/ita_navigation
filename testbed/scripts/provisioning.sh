# wiki.ros.org/kinetic/Installation/Ubuntu
printf "\n\n>> Installing ROS Kinetic\n\n"

sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
apt-get update -y
apt-get install ros-kinetic-desktop-full -y
apt-get install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential -y
apt-get install python-rosdep python-catkin-tools -y

# tum_simulator dependencies
# github.com/angelsantamaria/tum_simulator
apt-get install ros-kinetic-hector-* ros-kinetic-ardrone-autonomy -y

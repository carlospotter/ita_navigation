echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
rosdep update

# creating ROS workspace
# http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment
echo ">> Creating ROS workspace"
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make -DPYTHON_EXECUTABLE=/usr/bin/python3
source devel/setup.bash
echo $ROS_PACKAGE_PATH

function load_ros(){
	/bin/bash -c '. /opt/ros/kinetic/setup.bash; cd /home/vagrant/catkin_ws/; catkin_make'
	/bin/bash -c 'source /home/vagrant/catkin_ws/devel/setup.bash'
	/bin/bash -c 'roscore'
	/bin/bash -c 'roslaunch cvg_sim_gazebo ardrone_testworld.launch'
}

grep -qxF 'source /opt/ros/kinetic/setup.bash' .bashrc || echo "source /opt/ros/kinetic/setup.bash" >> .bashrc
/bin/bash -c 'source .bashrc'
sudo rosdep init
rosdep update

# creating ROS workspace
# http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment
echo ">> Creating ROS workspace"
DIR="catkin_ws"
if [ ! -d "$DIR" ]; then
	echo "> Creating catkin_ws folder"
	mkdir -p catkin_ws/src
fi

cd /home/vagrant
/bin/bash -c '. /opt/ros/kinetic/setup.bash; cd /home/vagrant/catkin_ws/; catkin_make' 
/bin/bash -c 'source /home/vagrant/catkin_ws/devel/setup.bash'
echo $ROS_PACKAGE_PATH

# installing tum_simulator
DIR="/home/vagrant/catkin_ws/src/tum_simulator"
if [ ! -d "$DIR" ]; then
	echo "> Cloning github repositorie of tum_simulator"
	cd ~/catkin_ws/src/
	git clone https://github.com/angelsantamaria/tum_simulator.git

	load_ros
else
	load_ros
fi

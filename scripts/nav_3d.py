#!/usr/bin/env python

from ita_astar import astar_3d
from node_grid import NodeGrid
import sys
import os
import numpy
import rospy
from ardrone_joy.msg import AutoPilotCmd
from std_msgs.msg import Empty

if __name__ == '__main__':
	
	#Initialize ROS stuff:
	rospy.init_node('run_3d_node')
	rospy.loginfo("Start")

	pub_to = rospy.Publisher('/ardrone/takeoff', Empty, queue_size=1)
	pub_move = rospy.Publisher('/autopilot_start_cmd', AutoPilotCmd, queue_size=10)
    
	# Environment representation: 
	absFilePath = os.path.abspath(__file__)
	os.chdir(os.path.dirname(absFilePath))

	map_pgm = ["data/map55.pgm", "data/map65.pgm", "data/map75.pgm", "data/map85.pgm", "data/map95.pgm", 
				"data/map105.pgm", "data/map115.pgm"]
	
	safety_dist = 5
	
	node_grid = NodeGrid(safety_dist,map_pgm)
	the_map = node_grid.generate_grid()

	text = numpy.array2string(the_map)
	with open("txt_map.txt",'w') as f:
		f.write(text)

	# Path planning algorithm:
	start_point = (0,20,20)
	end_point = (0,0,0)

	result, cost = astar_3d(the_map, start_point, end_point)

	drone_route = []
	n_nodes = len(result)
	drone_orient = [0] * (3 * (1+n_nodes))    

	# Coordinate conversion (Node grid --> Gazebo environment)
	for x in range(n_nodes):
		tup = result[x]
		goal_z = tup[0] * 10 + 55       #z position
		goal_x = tup[2] * 5 - 97.5      #x position
		goal_y = tup[1] * (-5) + 97.5   #y position
		drone_route.append(goal_x)
		drone_route.append(goal_y)
		drone_route.append(goal_z)

	stop_x = end_point[2] * 5 - 97.5
	stop_y = end_point[1] * (-5) + 97.5
	stop_z = end_point[0] * 10 + 50  
    
	drone_route.append(stop_x)
	drone_route.append(stop_y)
	drone_route.append(stop_z)

	# ROS commands
	pub_to.publish(Empty())

	pub_move.publish(False,drone_route,drone_orient,n_nodes+1,"no_turn")
    
	rospy.spin()

#!/usr/bin/env python

from ita_astar import astar_3d
from node_grid import new_grid
import sys
import os
import numpy
import rospy
from ardrone_joy.msg import AutoPilotCmd
from std_msgs.msg import Empty
from nav_msgs.msg import Odometry


def newOdom(msg):
    global xod
    global yod
    xod = msg.pose.pose.position.x
    yod = msg.pose.pose.position.y


def coordGtoN(xg,yg):
    # Convert the coordinates from Gazebo to nodegrid
    xst = int(round((xg + 97.5)/5))
    yst = int(round((yg - 97.5)/(-5)))
    return (0, yst, xst)


if __name__ == '__main__':
	
	# Initialize ROS stuff:
	rospy.init_node('run_3d_node')
	rospy.loginfo("Start")

	pub_to = rospy.Publisher('/ardrone/takeoff', Empty, queue_size=1)
	pub_move = rospy.Publisher('/autopilot_start_cmd', AutoPilotCmd, queue_size=10)

	sub = rospy.Subscriber("/ground_truth/state", Odometry, newOdom)
    
	# Environment representation: 
	absFilePath = os.path.abspath(__file__)
	os.chdir(os.path.dirname(absFilePath)) 
	map_pgm = ["data/map55.pgm", "data/map65.pgm", "data/map75.pgm", "data/map85.pgm", "data/map95.pgm", 
				"data/map105.pgm", "data/map115.pgm"]
	
	run_node = raw_input("Generate a new nodegrid (Y/n)? ")
	if run_node == 'y' or run_node == 'Y':
		the_map = new_grid(map_pgm)
	else:

		the_map = numpy.load('saved_map.npy')
	
	# Path planning algorithm:
	start_point = coordGtoN(xod, yod)
	print("Standard landing points (x,y): (-50, 0); (80, -65); (50, 65); (-80,85); (80,20); (-50,-85)")
	x_end, y_end = input("Insert desired landing point: ")
	end_point = coordGtoN(x_end,y_end)
	initial_height = 55
	flight_level_diff = 10

	result, cost = astar_3d(the_map, start_point, end_point)
	print(result)

	drone_route = []
	n_nodes = len(result)
	drone_orient = [0] * (3 * (2+n_nodes))    

	# Coordinate conversion (Node grid --> Gazebo environment)
	for x in range(n_nodes):
		tup = result[x]
		goal_z = tup[0] * flight_level_diff + initial_height	#z position
		goal_x = tup[2] * 5 - 97.5      						#x position
		goal_y = tup[1] * (-5) + 97.5   						#y position
		drone_route.append(goal_x)
		drone_route.append(goal_y)
		drone_route.append(goal_z)

	stop_x = end_point[2] * 5 - 97.5
	stop_y = end_point[1] * (-5) + 97.5
	stop_z = 5  
    
	drone_route.append(stop_x)
	drone_route.append(stop_y)
	drone_route.append(stop_z)

	drone_route.append(stop_x)
	drone_route.append(stop_y)
	drone_route.append(0)

	# Route sent to the drone controller
	pub_to.publish(Empty())

	pub_move.publish(False,drone_route,drone_orient,n_nodes+2,"no_turn")
    
	rospy.spin()

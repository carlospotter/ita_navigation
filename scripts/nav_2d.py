#!/usr/bin/env python

import rospy
from ita_astar import astar_2d
from node_grid import new_grid
from ardrone_joy.msg import AutoPilotCmd
from std_msgs.msg import Empty
from nav_msgs.msg import Odometry
import sys
import os
import numpy


def newOdom(msg):
    global xod
    global yod
    xod = msg.pose.pose.position.x
    yod = msg.pose.pose.position.y


def coordGtoN(xg, yg):
    # Convert the coordinates from Gazebo to nodegrid
    xst = int(round((xg + 97.5)/5))
    yst = int(round((yg - 97.5)/(-5)))
    return (yst, xst)


if __name__ == '__main__':
    
    # Initialize ROS stuff
    rospy.init_node('run_2d_node')
    rospy.loginfo("Start")

    pub_to = rospy.Publisher('/ardrone/takeoff', Empty, queue_size=1)
    pub_move = rospy.Publisher('/autopilot_start_cmd', AutoPilotCmd, queue_size=1)

    sub = rospy.Subscriber("/ground_truth/state", Odometry, newOdom)

    # Environment representation:
    run_node = raw_input("Generate a new nodegrid (Y/n)? ")
    if run_node == 'y' or run_node == 'Y':
        the_map = new_grid()
    else: 
        absFilePath = os.path.abspath(__file__)
        os.chdir(os.path.dirname(absFilePath))
        the_map = numpy.load('saved_map.npy')

    # Path planning algorithm:
    start_point = coordGtoN(xod,yod)
    print("Standard landing points (x,y): (-50, 0); (80, -65); (50, 65); (-80,85); (80,20); (-50,-85)")
    x_end, y_end = input("Insert desired landing point: ")
    end_point = coordGtoN(x_end,y_end)
    initial_height = 55     # meters
    flight_level_diff = 10  # meters

    min_cost = None    
    for n in range(the_map.shape[0]):
        result, cost = astar_2d(the_map[n], start_point, end_point)
        altitude = initial_height + n * flight_level_diff
        cost = cost + 2 * altitude
        if cost < min_cost or min_cost == None:
            min_cost = cost
            min_result = result
            min_alt = altitude 
        
    drone_route = []
    n_nodes = len(min_result)
    drone_orient = [0] * ( 3 * (2+n_nodes))

    # Coordinate conversion (Node grid --> Gazebo environment)
    for x in range(n_nodes):
        tup = min_result[x]
        goal_x = tup[1] * 5 - 97.5      #x position
        goal_y = tup[0] * (-5) + 97.5   #y position
        goal_z = min_alt                #z position
        drone_route.append(goal_x)
        drone_route.append(goal_y)
        drone_route.append(goal_z)
    
    stop_x = end_point[1] * 5 - 97.5
    stop_y = end_point[0] * (-5) + 97.5
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
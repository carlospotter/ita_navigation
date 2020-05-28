#!/usr/bin/env python

import rospy
from ita_astar import astar_2d
from convert_map import convert_map
from ardrone_joy.msg import AutoPilotCmd
from std_msgs.msg import Empty
import sys
import os
import numpy

if __name__ == '__main__':
    rospy.init_node('nav_2d')
    rospy.loginfo("Start")

    pub_to = rospy.Publisher('/ardrone/takeoff', Empty, queue_size=1)
    pub_land = rospy.Publisher('/ardrone/land', Empty, queue_size=1)
    pub_move = rospy.Publisher('/autopilot_start_cmd', AutoPilotCmd, queue_size=1)

    absFilePath = os.path.abspath(__file__)
    os.chdir(os.path.dirname(absFilePath))

    map_pgm = ["data/map55.pgm", "data/map65.pgm", "data/map75.pgm", "data/map85.pgm",
                "data/map95.pgm", "data/map105.pgm", "data/map115.pgm"]


    start_point = (20,20)
    end_point = (39,20)
    initial_height = 55 
    i = 0
    min_cost = None
    results = {}
    for n in map_pgm:
        node_map = convert_map(n)
        result, cost = astar_2d(node_map, start_point, end_point)
        actual_cost = cost + 2 * (initial_height + 10*i)
        if min_cost == None or actual_cost < min_cost:
            min_cost = actual_cost
            min_height = i
            min_result = result
        i += 1
    
    drone_route = []
    print(min_result)
    n_nodes = len(min_result)
    drone_orient = [0] * ( 3 * (1+n_nodes))

    for x in range(n_nodes):
        tup = min_result[x]
        goal_x = tup[1] * 5 - 97.5      #x position
        goal_y = tup[0] * (-5) + 97.5   #y position
        goal_z = min_height * 10 + 55   #z position
        drone_route.append(goal_x)
        drone_route.append(goal_y)
        drone_route.append(goal_z)
    
    stop_x = end_point[1] * 5 - 97.5
    stop_y = end_point[0] * (-5) + 97.5
    stop_z = 55  

    drone_route.append(stop_x)
    drone_route.append(stop_y)
    drone_route.append(stop_z)

    pub_to.publish(Empty())
    
    pub_move.publish(False,drone_route,drone_orient,n_nodes+1,"no_turn")
    
    rospy.spin()
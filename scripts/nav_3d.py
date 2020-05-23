#!/usr/bin/env python

import rospy
from ita_astar import astar_3d
from convert_map import node_grid_3d
from ardrone_joy.msg import AutoPilotCmd
from std_msgs.msg import Empty
import sys
import os
import numpy

if __name__ == '__main__':
    rospy.init_node('run_3d_node')
    rospy.loginfo("Start")

    pub_to = rospy.Publisher('/ardrone/takeoff', Empty, queue_size=1)
    pub_move = rospy.Publisher('/autopilot_start_cmd', AutoPilotCmd, queue_size=10)
    
    absFilePath = os.path.abspath(__file__)
    os.chdir(os.path.dirname(absFilePath))

    map_pgm = ["data/map55.pgm", "data/map65.pgm", "data/map75.pgm", "data/map85.pgm",
                "data/map95.pgm", "data/map105.pgm", "data/map115.pgm"]

    node_map = node_grid_3d(map_pgm)

    start_point = (0,20,20)
    end_point = (0,37,37)

    result, cost = astar_3d(node_map, start_point, end_point)

    drone_route = []
    n_nodes = len(result)
    drone_orient = [0] * (3 * (1+n_nodes))    

    for x in range(n_nodes):
        tup = result[x]
        goal_z = tup[0] * 10 + 55       #z position
        goal_x = tup[1] * 5 - 97.5      #x position
        goal_y = tup[2] * (-5) + 97.5   #y position
        drone_route.append(goal_x)
        drone_route.append(goal_y)
        drone_route.append(goal_z)

    stop_x = end_point[1] * 5 - 97.5
    stop_y = end_point[2] * (-5) + 97.5
    stop_z = end_point[0] * 10 + 50  
    
    drone_route.append(stop_x)
    drone_route.append(stop_y)
    drone_route.append(stop_z)

    pub_to.publish(Empty())

    pub_move.publish(False,drone_route,drone_orient,n_nodes+1,"no_turn")
    
    rospy.spin()

#!usr/bin/env python
import numpy

def astar_2d(space,start,end,eucl=True,xdist=5,ydist=5):

    open_nodes = set([start])
    closed_nodes = set()

    path_log = dict()

    g_cost = {start:0}
    f_cost = {start:euclidean_dist(start,end,xdist,ydist)}

    while open_nodes:

        cost_eval = dict()
        for node in open_nodes:
            cost_eval[node] = f_cost[node]
        current = min(cost_eval, key=cost_eval.get)  

        open_nodes.remove(current)
        closed_nodes.add(current)

        if current == end:
            optimal_path = [current]
            while current != start:
                current = path_log[current]
                optimal_path.append(current)      
            optimal_path.reverse()
            return optimal_path, f_cost[end]
            
        neighbours_current = find_neighbours(current,space)

        for n in neighbours_current:
            if space[n] == 1:
                continue
            if n not in closed_nodes:
                new_g_cost = g_cost[current] + euclidean_dist(current,n,xdist,ydist)
                if n not in open_nodes:
                    open_nodes.add(n)
                                                                    
                else:                        
                    if g_cost[n] <= new_g_cost:
                        continue
                    
                g_cost[n] = new_g_cost
                if eucl == True:
                    f_cost[n] = g_cost[n] + euclidean_dist(n,end,xdist,ydist)
                else:
                    f_cost[n] = g_cost[n] + manhattan_dist(n,end,xdist,ydist)
                path_log[n] = current
            
    return ["Error"], 100000
            
def euclidean_dist(p1,p2,xdist,ydist):
    #Calculate the Euclidean distance from point1 to point2:
    x = xdist*(p2[0] - p1[0])
    y = ydist*(p2[1] - p1[1])
    return numpy.sqrt(x**2 + y**2)
    
def manhattan_dist(p1,p2,xdist,ydist):
    #Calculate the Manhattan distance from point1 to point2:
    return xdist*abs(p2[0] - p1[0]) + ydist*abs(p2[1] - p1[1])

def find_neighbours(node,space):
    neighbours=set()
    x_lim = numpy.shape(space)[1] - 1
    y_lim = numpy.shape(space)[0] - 1
    for x_move in [1,0,-1]:
        for y_move in [1,0,-1]:
            x_n = node[0] + x_move
            y_n = node[1] + y_move
            if x_n < 0 or x_n > x_lim or y_n < 0 or y_n > y_lim:
                continue
            neighbours.add((x_n, y_n))
    return neighbours


def astar_3d(space,start,end,eucl=True,xdist=5,ydist=5,zdist=10):

    open_nodes = set([start])
    closed_nodes = set()

    path_log = {}

    g_cost = {start:0}
    f_cost = {start:euclidean_dist_3d(start,end,xdist,ydist,zdist)}

    while open_nodes:

        cost_eval = dict()
        for node in open_nodes:
            cost_eval[node] = f_cost[node]
        current = min(cost_eval, key=cost_eval.get)        

        open_nodes.remove(current)
        closed_nodes.add(current)

        if current == end:
            optimal_path = [current]
            while current != start:
                current = path_log[current]
                optimal_path.append(current)      
            optimal_path.reverse()
            return optimal_path, f_cost[end]
            
        neighbours_current = find_neighbours_3d(current,space)

        for n in neighbours_current:
            if space[n] == 1:
                continue
            if n not in closed_nodes:
                new_g_cost = g_cost[current] + euclidean_dist_3d(current,n,xdist,ydist,zdist)
                if n not in open_nodes:
                    open_nodes.add(n)
                                                                  
                else:                        
                    if g_cost[n] <= new_g_cost:
                        continue
                  
                g_cost[n] = new_g_cost
                if eucl == True:
                    f_cost[n] = g_cost[n] + euclidean_dist_3d(n,end,xdist,ydist,zdist)
                else:
                    f_cost[n] = g_cost[n] + manhattan_dist_3d(n,end,xdist,ydist,zdist)
                path_log[n] = current
    
    return ["Error"], 100000
            
def euclidean_dist_3d(p1,p2,xdist,ydist,zdist):
    #Calculate the Euclidean distance from point1 to point2:
    x = xdist*(p2[2] - p1[2])
    y = ydist*(p2[1] - p1[1])
    z = zdist*(p2[0] - p1[0])
    return numpy.sqrt(x**2 + y**2 + z**2)
   
def manhattan_dist_3d(p1,p2,xdist,ydist,zdist):
    #Calculate the Manhattan distance from point1 to point2:
    return xdist*abs(p2[2] - p1[2]) + ydist*abs(p2[1] - p1[1]) + zdist*abs(p2[0]-p1[0])

def find_neighbours_3d(node,space):
    neighbours=set()
    x_lim = numpy.shape(space)[2] - 1
    y_lim = numpy.shape(space)[1] - 1 
    z_lim = numpy.shape(space)[0] - 1
    for x_move in [1,0,-1]:
        for y_move in [1,0,-1]:
            for z_move in [1,0,-1]:
                x_n = node[1] + x_move
                y_n = node[2] + y_move
                z_n = node[0] + z_move
                if x_n < 0 or x_n > x_lim or y_n < 0 or y_n > y_lim or z_n < 0 or z_n > z_lim:
                    continue
                neighbours.add((z_n, x_n, y_n))
    return neighbours

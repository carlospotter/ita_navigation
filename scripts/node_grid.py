#!/usr/bin/env python

import matplotlib.image as img
import sys
import os
import numpy

numpy.set_printoptions(threshold=sys.maxsize)

def new_grid(map_list):
    safe_distance = input("Define the distance between drone and obstacles (in meters): ") 
    print("Generating nodegrid...")

    node_grid = NodeGrid(safe_distance,map_list)
    the_map = node_grid.generate_grid()

    absFilePath = os.path.abspath(__file__)
    os.chdir(os.path.dirname(absFilePath))
    numpy.save('saved_map.npy', the_map)

    return the_map

class NodeGrid:
    def __init__(self, safe_distance, map_list):
        self.x_dist = safe_distance
        self.y_dist = safe_distance
        #Considering a 10m flight level separation:
        self.z_dist = safe_distance//10 # + 1
        self.map_list = map_list
    
    def convert_map(self,map_pgm):
        map_matrix = img.imread(map_pgm)
        #(n_lin, n_col) = map_matrix.shape

        #final_matrix = numpy.zeros(shape=(n_lin,n_col))

        #for count_v in range(n_lin):
        #    for count_h in range(n_col):
        #        if map_matrix[count_h, count_v] >= [254]:
        #            final_matrix[count_h, count_v] = 0
        #        else:
        #            final_matrix[count_h, count_v] = 1
                
        return map_matrix #final_matrix

    def node_grid_3d(self):
        z_init_val = 0
        for a in self.map_list:
            if z_init_val == 0:
                node_map = self.convert_map(a)[numpy.newaxis,...]
                z_init_val += 1
            else:
                new_map = self.convert_map(a)[numpy.newaxis,...]
                node_map = numpy.vstack([node_map,new_map])
        return node_map

    def generate_grid(self):
        node_grid = self.node_grid_3d()

        #Applying the distance constraints:
        (z_lim, y_lim, x_lim) = node_grid.shape

        node_map = numpy.zeros(shape=(z_lim, y_lim, x_lim))
        
        for z in range(z_lim):
            for y in range(y_lim):
                for x in range(x_lim):
                    if node_grid[z,y,x] < [254]:
                        x_lower = x - self.x_dist
                        if x_lower < 0:
                            x_lower = 0
                        x_upper = x + self.x_dist
                        if x_upper >= x_lim:
                            x_upper = x_lim - 1
                        y_lower = y - self.y_dist
                        if y_lower < 0:
                            y_lower = 0
                        y_upper = y + self.y_dist
                        if y_upper >= y_lim:
                            y_upper = y_lim - 1
                        z_upper = z + self.z_dist
                        if z_upper >= z_lim:
                            z_upper = z_lim - 1
                        for zf in range(z, z_upper+1):
                            for yf in range(y_lower, y_upper+1):
                                for xf in range(x_lower, x_upper+1):
                                    node_map[zf,yf,xf] = 1
        
        #return node_map

        # Reduction of map scale turning each 1mx1m 
        # square into a 5mx5m square:

        matrix_out = numpy.zeros(shape=(z_lim, y_lim/5, x_lim/5))

        for z in range(z_lim):
            xc = 0
            x_out = 0
            yc = 0
            y_out = 0
            while yc < y_lim:
                while xc < x_lim:
                    mat_5 = node_map[z, yc:yc+5, xc:xc+5]
                    if mat_5.sum()==0:
                        matrix_out[z, y_out, x_out] = 0
                    else:
                        matrix_out[z, y_out, x_out] = 1
                    xc += 5
                    x_out += 1
                yc += 5
                y_out += 1
                xc = 0
                x_out = 0
        
        return matrix_out
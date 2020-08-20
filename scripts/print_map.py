#!/usr/bin/env python

import matplotlib.image as img
import matplotlib.pyplot as plt
import sys
import numpy
from mpl_toolkits.mplot3d import Axes3D
import os


def print_3d_map(map_matrix):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    zl = map_matrix.shape[0]
    xl = map_matrix.shape[1]
    yl = map_matrix.shape[2]

    for z in range(zl):
	    for x in range(xl):
		    for y in range(yl):
			    # if map_matrix[z, x, y] == 1:
				#     ax.scatter(y, 39-x, z, zdir='z', c= 'red')
			    if map_matrix[z, x, y] == 2:
				    ax.scatter(y, 39-x, z, zdir='z', c = 'blue')

    absFilePath = os.path.abspath(__file__)
    os.chdir(os.path.dirname(absFilePath))
    
    plt.savefig("3dmap.png")

    return 0


def print_2d_map(map_matrix):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    xl = map_matrix.shape[0]
    yl = map_matrix.shape[1]

    for x in range(xl):
        for y in range (yl):
            if map_matrix[x,y] == 1:
                ax.scatter(y, 39-x, c = 'red')
            if map_matrix[x,y] == 2:
                ax.scatter(y, 39-x, c = 'blue')
            if map_matrix[x,y] == 0:
                ax.scatter(y, 39-x, c = 'green')
    
    absFilePath = os.path.abspath(__file__)
    os.chdir(os.path.dirname(absFilePath))

    plt.savefig('2dmap.png')

    return 0
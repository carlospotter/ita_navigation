#!/usr/bin/env python

from node_grid import NodeGrid
from print_map import print_3d_map, print_2d_map
import sys
import os
import numpy

if __name__ == '__main__':

	# Environment representation: 
	absFilePath = os.path.abspath(__file__)
	os.chdir(os.path.dirname(absFilePath))

	map_pgm = ["data/map55.pgm", "data/map65.pgm", "data/map75.pgm", "data/map85.pgm", "data/map95.pgm", 
				"data/map105.pgm", "data/map115.pgm"]
	
	safety_dist = 0
	
	node_grid = NodeGrid(safety_dist,map_pgm)
	the_map = node_grid.generate_grid()

	#text = numpy.array2string(the_map)
	#with open("txt_map.txt",'w') as f:
	#	f.write(text)
	
	#print_2d_map(the_map[0])
	print(numpy.shape(the_map)[0])
	print(numpy.shape(the_map)[1])
	print(numpy.shape(the_map)[2])
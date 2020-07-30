#!/usr/bin/env python

from ita_astar import astar_3d
from node_grid import NodeGrid
import sys
import os
import numpy

if __name__ == '__main__':
	absFilePath = os.path.abspath(__file__)
	os.chdir(os.path.dirname(absFilePath))

	map_pgm = ["data/map55.pgm", "data/map65.pgm", "data/map75.pgm", "data/map85.pgm", "data/map95.pgm", 
				"data/map105.pgm", "data/map115.pgm"]

	
	node_grid = NodeGrid(5,map_pgm)
	the_map = node_grid.generate_grid()
#!/usr/bin/env python

import matplotlib.image as img
import sys
import numpy

numpy.set_printoptions(threshold=sys.maxsize)


def node_grid_3d(map_list):
	z_init_val = 0
	for a in map_list:
		if z_init_val == 0:
			node_map = convert_map(a)[numpy.newaxis,...]
			z_init_val += 1
		else:
			new_map = convert_map(a)[numpy.newaxis,...]
			node_map = numpy.vstack([node_map,new_map])
	return node_map

def convert_map(map_pgm):
	map_matrix = img.imread(map_pgm)
	(n_lin,n_col) = map_matrix.shape

	final_matrix = numpy.zeros(shape=(n_lin, n_col))

	count_h = 0
	count_v = 0

	while count_v < 200:
		while count_h < 200:
			if map_matrix[count_h, count_v] == [254]:
				final_matrix[count_h, count_v] = 0
			else:
				final_matrix[count_h, count_v] = 1
			count_h = count_h + 1
		count_v = count_v + 1
		count_h = 0

	c_v = 0
	c_h = 0
	c_out_v = 0
	c_out_h = 0

	matrix_out = numpy.zeros(shape=(n_lin/5, n_col/5))

	while c_v < 200:
		while c_h < 200:
			mat_5 = final_matrix[c_h:c_h+5, c_v:c_v+5]
			if mat_5.sum() == 0:
				matrix_out[c_out_h, c_out_v] = 0
			else:
				matrix_out[c_out_h, c_out_v] = 1
			c_h = c_h + 5
			c_out_h = c_out_h + 1
		c_v = c_v + 5
		c_out_v = c_out_v + 1
		c_h = 0
		c_out_h = 0

	return matrix_out
#!usr/bin/env python

from ita_astar import astar_2d, astar_3d
from convert_map import convert_map
import print_3d_map
from convert_map_2d import convert_map_2d
import print_2d_map
from ttictoc import TicToc
import sys
import os
import numpy

#Change directory:    
absFilePath = os.path.abspath(__file__)

map_pgm = ["data/map55.pgm", "data/map65.pgm", "data/map75.pgm", "data/map85.pgm",
	"data/map95.pgm", "data/map105.pgm", "data/map115.pgm"] 

#Running the 2D A* algorithm:

start = (0,0)
end = [(0,10),(0,30),(10,30),(20,10),(20,20),(20,30),(30,10),(30,30),(30,39),
		(39,10),(39,30),(39,39)]

m_out = dict()
for a in map_pgm:
	m_out[a] = convert_map_2d(a)

print("2D ALGORITHM:")
times2d = []
for x in end :
	costs = []
	alt = 55
	runtime = 0
	
	for a in map_pgm:
		t = TicToc()
		t.tic()
		result, cost = astar_2d(m_out[a], start, x)
		t.toc()	
		c = cost + 2*alt
		costs.append(c)
		alt = alt + 10
		runtime = runtime + t.elapsed

	times2d.append(runtime)	
	print(str(x) + ": 2D min cost: " + str(min(costs)) + " 2D time: " + str(runtime))
print(".")
print(".")
print(".")


#Running the 3D A* algorithm:

b = 0
for a in map_pgm:
	if b == 0:
		d1 = convert_map(a)[numpy.newaxis,...]
		b = b + 1
	else:
		d2 = convert_map(a)[numpy.newaxis,...]
		d1 = numpy.vstack([d1,d2])


start_3d = (0,0,0)
end_3d = [(0,0,10),(0,0,30),(0,10,30),(0,20,10),(0,20,20),(0,20,30),(0,30,10),(0,30,30),
		(0,30,39),(0,39,10),(0,39,30),(0,39,39)]


print("3D ALGORITHM:")
times3d = []
for x in end_3d:
	costs = []
	alt = 55
	runtime = 0
	t = TicToc()
	t.tic()
	result, cost = astar_3d(d1, start_3d, x)
	t.toc()
	runtime = t.elapsed
	c = cost + 2 * alt
	costs.append(c)
	alt = alt + 10

	times3d.append(runtime)
	print(str(x) + " 3D cost: " + str(min(costs)) + " 3D time: " + str(runtime))

print(".")
print(".")
print(".")

av_2d = sum(times2d)/len(times2d)

av_3d = sum(times3d)/len(times3d)

rate = av_3d/av_2d

print("2D average time: " + str(av_2d))
print("3D average time: " + str(av_3d))
print("Rate 3D/2D: " + str(rate))


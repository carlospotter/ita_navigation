#!usr/bin/env python

from ita_astar import astar_2d, astar_3d
from node_grid import new_grid
import timeit
import sys
import os
import numpy

#Change directory:    
absFilePath = os.path.abspath(__file__)
os.chdir(os.path.dirname(absFilePath))

map_pgm = ["data/map55.pgm", "data/map65.pgm", "data/map75.pgm", "data/map85.pgm",
	"data/map95.pgm", "data/map105.pgm", "data/map115.pgm"] 

m_out = new_grid(map_pgm)

text_file = open("runtime_results.txt", "w")

print("Running test...")

#Running the 2D A* algorithm with euclidean distance heuristic:

start = (0,0)
end = [(0,10),(0,30),(10,30),(20,10),(20,20),(20,30),(30,10),(30,30),(30,39),
		(39,10),(39,30),(39,39)]

savetxt = text_file.write("2D ALGORITHM WITH EUCLIDEAN DISTANCE HEURISTIC: \n")

times2d = []
euc2d = {}
for x in end :
	costs = []
	alt = 55
	runtime = 0
	
	for n in range(m_out.shape[0]):
		starttimer = timeit.default_timer()
		result, cost = astar_2d(m_out[n], start, x)
		stoptimer = timeit.default_timer()
		runtime = runtime + (stoptimer - starttimer)
		starttimer = 0
		stoptimer = 0
		c = cost + 2*alt
		costs.append(c)
		alt = alt + 10

	# times2d.append(runtime)	
	euc2d[x] = [min(costs), runtime]
	savetxt = text_file.write(str(x) + ": 2D min cost: " + str(min(costs)) + " 2D time: " + str(runtime) + "\n")
savetxt = text_file.write(". \n . \n")

#Running the 2D A* algorithm with manhattan distance heuristic:

savetxt = text_file.write("2D ALGORITHM WITH MANHATTAN DISTANCE HEURISTIC: \n")

times2d = []
man2d = {}
for x in end :
	costs = []
	alt = 55
	runtime = 0
	
	for n in range(m_out.shape[0]):
		starttimer = timeit.default_timer()
		result, cost = astar_2d(m_out[n], start, x, False)
		stoptimer = timeit.default_timer()
		runtime = runtime + (stoptimer - starttimer)
		starttimer = 0
		stoptimer = 0
		c = cost + 2*alt
		costs.append(c)
		alt = alt + 10
		

	# times2d.append(runtime)	
	man2d[x] = [min(costs), runtime]
	savetxt = text_file.write(str(x) + ": 2D min cost: " + str(min(costs)) + " 2D time: " + str(runtime) + "\n")
savetxt = text_file.write(". \n . \n")


#Running the 3D A* algorithm with euclidean distance heuristic:

start_3d = (0,0,0)
end_3d = [(0,0,10),(0,0,30),(0,10,30),(0,20,10),(0,20,20),(0,20,30),(0,30,10),(0,30,30),
		(0,30,39),(0,39,10),(0,39,30),(0,39,39)]


savetxt = text_file.write("3D ALGORITHM WITH EUCLIDEAN DISTANCE HEURISTIC: \n")
times3d = []
euc3d = {}
for x in end_3d:
	costs = []
	alt = 55
	runtime = 0
	starttimer = timeit.default_timer()
	result, cost = astar_3d(m_out, start_3d, x)
	stoptimer = timeit.default_timer()
	runtime = stoptimer - starttimer
	starttimer = 0
	stoptimer = 0
	c = cost + 2 * alt
	costs.append(c)
	alt = alt + 10

	# times3d.append(runtime)
	euc3d[x] = [c, runtime] 
	savetxt = text_file.write(str(x) + " 3D cost: " + str(min(costs)) + " 3D time: " + str(runtime) + "\n")
savetxt = text_file.write(". \n . \n")


#Running the 3D A* algorithm with manhattan distance heuristic:

start_3d = (0,0,0)
end_3d = [(0,0,10),(0,0,30),(0,10,30),(0,20,10),(0,20,20),(0,20,30),(0,30,10),(0,30,30),
		(0,30,39),(0,39,10),(0,39,30),(0,39,39)]


savetxt = text_file.write("3D ALGORITHM WITH MANHATTAN DISTANCE HEURISTIC: \n")
times3d = []
man3d = {}
for x in end_3d:
	costs = []
	alt = 55
	runtime = 0
	starttimer = timeit.default_timer()
	result, cost = astar_3d(m_out, start_3d, x, False)
	stoptimer = timeit.default_timer()
	runtime = stoptimer - starttimer
	starttimer = 0
	stoptimer = 0
	c = cost + 2 * alt
	costs.append(c)
	alt = alt + 10

	# times3d.append(runtime)
	man3d[x] = [c, runtime] 
	savetxt = text_file.write(str(x) + " 3D cost: " + str(min(costs)) + " 3D time: " + str(runtime) + "\n")
savetxt = text_file.write(". \n . \n")

# Print the tables in the LaTeX format:

# Route length: 

savetxt = text_file.write("Route Length LaTeX Table \n \n")

for count in range(len(end_3d)):
	savetxt = text_file.write("(0,0,0)	& " + str(end_3d[count]) + " & " + str(round(euc2d[end[count]][0],2)) + " & " +
		str(round(man2d[end[count]][0],2)) + " & " + str(round(euc3d[end_3d[count]][0],2)) + " & " + 	
		str(round(man3d[end_3d[count]][0],2)) + " \\\\ \\hline \n" )


savetxt = text_file.write("\n \n Runtime LaTeX Table \n \n")

for count in range(len(end_3d)):
	savetxt = text_file.write("(0,0,0)	& " + str(end_3d[count]) + " & " + str(euc2d[end[count]][1]) + " & " +
		str(man2d[end[count]][1]) + " & " + str(euc3d[end_3d[count]][1]) + " & " + 	str(man3d[end_3d[count]][1]) + " \\\\ \\hline \n"	)




# av_2d = sum(times2d)/len(times2d)

# av_3d = sum(times3d)/len(times3d)

# rate = av_3d/av_2d

# print("2D average time: " + str(av_2d))
# print("3D average time: " + str(av_3d))
# print("Rate 3D/2D: " + str(rate))


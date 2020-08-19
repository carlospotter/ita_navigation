#!usr/bin/env python

from ita_astar import astar_2d, astar_3d
from node_grid import new_grid
import matplotlib.pyplot as plt
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
	euc2d[x] = [min(costs), runtime*1000]
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
	man2d[x] = [min(costs), runtime*1000]
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
	euc3d[x] = [c, runtime*1000] 
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
	man3d[x] = [c, runtime*1000] 
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
	savetxt = text_file.write("(0,0,0)	& " + str(end_3d[count]) + " & " + str(round(euc2d[end[count]][1],2)) + " & " +
		str(round(man2d[end[count]][1],2)) + " & " + str(round(euc3d[end_3d[count]][1],2)) + " & " + 	str(round(man3d[end_3d[count]][1],2)) + " \\\\ \\hline \n"	)


# Plots:

# Plot 2D (euc and man):
time_euc2d = []
dist_euc2d = []
time_man2d = []
dist_man2d = []

for each in euc2d:
	time_euc2d.append(euc2d[each][1])
	dist_euc2d.append(euc2d[each][0])

for each in man2d:
	time_man2d.append(man2d[each][1])
	dist_man2d.append(man2d[each][0])

fig = plt.figure()
fg = fig.add_subplot(111)

fg.scatter(dist_euc2d,time_euc2d, c = 'blue', label='Euclidean distance')
fg.scatter(dist_man2d,time_man2d, c = 'red', marker='v', label='Manhattan distance')
fg.legend(bbox_to_anchor=(0, 1), loc='upper left', ncol=1)
fg.set_xlabel("Travelled distance (m)")
fg.set_ylabel("Execution time (ms)")


plt.savefig('2dresults.png')

# Plot 3D (euc and man)

time_euc3d = []
dist_euc3d = []
time_man3d = []
dist_man3d = []

for each in euc3d:
	time_euc3d.append(euc3d[each][1])
	dist_euc3d.append(euc3d[each][0])

for each in man3d:
	time_man3d.append(man3d[each][1])
	dist_man3d.append(man3d[each][0])

fig = plt.figure()
fg = fig.add_subplot(111)

fg.scatter(dist_euc3d,time_euc3d, c = 'blue',label='Euclidean distance')
fg.scatter(dist_man3d,time_man3d, c = 'red', marker='v',label='Manhattan distance')
fg.legend(bbox_to_anchor=(0, 1), loc='upper left', ncol=1)
fg.set_xlabel("Travelled distance (m)")
fg.set_ylabel("Execution time (ms)")

plt.savefig('3dresults.png')

# Reduction of the map analysis

end = [(0,10),(0,30),(10,30),(20,10),(20,20),(20,30),(30,10),(30,30),(30,39),
		(39,10),(39,30),(39,39)]

m_out2 = new_grid(map_pgm, False)

savetxt = text_file.write(". \n . \n")
savetxt = text_file.write("2D ALGORITHM WITHOUT MAP REDUCTION: \n")

red2d = {}
for x in end :
	costs = []
	alt = 55
	runtime = 0
	x1 = x[0]*5+2
	x2 = x[1]*5+2
	xn = (x1,x2)
	
	for n in range(m_out2.shape[0]):
		starttimer = timeit.default_timer()
		result, cost = astar_2d(m_out2[n], start, xn, True, 1, 1)
		stoptimer = timeit.default_timer()
		runtime = runtime + (stoptimer - starttimer)
		starttimer = 0
		stoptimer = 0
		c = cost + 2*alt
		costs.append(c)
		alt = alt + 10

	# times2d.append(runtime)	
	red2d[x] = [min(costs), runtime*1000]
	savetxt = text_file.write(str(x) + ": 2D min cost: " + str(min(costs)) + " 2D time: " + str(runtime) + "\n")
savetxt = text_file.write(". \n . \n")

time_red = []
dist_red = []

for each in red2d:
	time_red.append(red2d[each][1])
	dist_red.append(red2d[each][0])

fig = plt.figure()
fg = fig.add_subplot(111)

fg.scatter(dist_euc2d,time_euc2d, c = 'blue',label='Reduced map')
fg.scatter(dist_red,time_red, c = 'red', marker='v', label="Original map")
fg.legend(bbox_to_anchor=(0, 1), loc='upper left', ncol=1)
fg.set_xlabel("Travelled distance (m)")
fg.set_ylabel("Execution time (ms)")

plt.savefig('redresults.png')

for count in range(len(end)):
	savetxt = text_file.write("(0,0,0)	& " + str(end[count]) + " & " + str(round(euc2d[end[count]][0],2)) + " & " +
		str(round(red2d[end[count]][0],2)) + " & " + str(round(euc2d[end[count]][1],2)) + " & " + 	
		str(round(red2d[end[count]][1],2)) + " \\\\ \\hline \n" )
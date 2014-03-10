from collections import defaultdict
import math
import numpy as np

#input a fluoresence file location, output a dictionary with dict[neuron_id] = [activity_at_1, ... n]
def parse_time_series(loc_file_F):
	print "\nReading:",loc_file_F
	neuron_time_series = defaultdict(list)
	for timestep, line in enumerate( open(loc_file_F) ):
		for neuron_id, neuron_activity in enumerate( line.strip().split(",") ):
			neuron_time_series[neuron_id].append( float(neuron_activity) )
	return neuron_time_series
	
def discretize_time_series(time_series, threshold = 0.12):
	print "\nDiscretizing",len( time_series ), "timeseries"
	discretized = {}
	for k,v in time_series.items():
		discretized[k] = np.array([1 if f > threshold else 0 for f in list(np.diff(v,axis=0))])
		del time_series[k]
	return discretized
	
#input a network file location, output a dictionary with dict[(neuron_i, neuron_j)] = int connection, and nr of blocked neurons (-1)
def parse_neuron_connections(loc_file_N):
	print "\nReading:",loc_file_N
	neuron_connections = defaultdict(list)
	blocked = 0
	for e, line in enumerate( open(loc_file_N) ):
		row = line.strip().split(",")
		neuron_i = int(row[0]) - 1
		neuron_j = int(row[1]) - 1
		connection = int(row[2])
		if connection == -1:
			blocked += 1
		neuron_connections[(neuron_i,neuron_j)] = connection
	return neuron_connections, blocked
	
#input a position file location, output a dictionary with dict[neuron_id] = (x,y) where x and y are scaled to 500 (from 1000)
def parse_neuron_positions(loc_file_P):
	print "\nReading:", loc_file_P
	neuron_positions = {}
	for neuron_id, line in enumerate( open(loc_file_P) ):
		row = line.strip().split(",")
		x = int(1000*float(row[0])/2)
		y = int(1000*float(row[1])/2)
		neuron_positions[neuron_id] = (x,y)
	return neuron_positions

#returns euclidian distance between two points (x1,y1) (x2,y2)
def calc_dist(p1,p2):
	return math.sqrt( (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 )
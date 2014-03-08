'''Author: 		mlwave.com'''
'''Description:	Python benchmark code for Pearson Correlation with Descretization, in use for Kaggle Connectomics Contest'''
import brainparse as bp
import scipy.stats as stats
import numpy as np
from datetime import datetime
start = datetime.now()
last = datetime.now()

neuron_activities = bp.parse_time_series("d:\\brain\\fluorescence_valid.txt")
neuron_activities = bp.discretize_time_series(neuron_activities, threshold=0.12)
neuron_positions = bp.parse_neuron_positions("d:\\brain\\networkPositions_valid.txt")
predictions_loc = "d:\\brain\\kaggle_preds.csv"

print "\nWriting:", predictions_loc
cache = {}
with open(predictions_loc, "wb") as outfile:
	outfile.write( "NET_neuronI_neuronJ,Strength\n" )
	for e, neuron_i_id in enumerate( xrange(len(neuron_positions)) ):
		for neuron_j_id, neuron_position in neuron_positions.items():
			if (neuron_i_id, neuron_j_id) in cache:
				outfile.write( "valid_"+str(neuron_i_id+1)+"_"+str(neuron_j_id+1)+","+cache[(neuron_i_id, neuron_j_id)] + "\n" )
			elif neuron_i_id == neuron_j_id:
				outfile.write( "valid_"+str(neuron_i_id+1)+"_"+str(neuron_j_id+1)+",0\n" )
			else:
				corr = str(stats.pearsonr(neuron_activities[neuron_i_id], neuron_activities[neuron_j_id])[0])
				cache[(neuron_j_id, neuron_i_id)] = corr
				outfile.write( "valid_"+str(neuron_i_id+1)+"_"+str(neuron_j_id+1)+","+corr + "\n" )
		print e+1,"/",len(neuron_positions),"\t",datetime.now()-start,"\t",datetime.now()-last
		last = datetime.now()
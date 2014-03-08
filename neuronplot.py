import brainparse as bp
import matplotlib.pyplot as plt

neuron_activities = bp.parse_time_series("d:\\brain\\fluorescence_iNet1_Size100_CC02inh.txt")

fig = plt.figure()
fig.suptitle('Top: 2000 Activity series for neuron 0 and 5 superimposed.\n Bottom: 8000 Activity series for neuron 93 and 23 superimposed.')

ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

ax1.plot([f for f in xrange(2000)],neuron_activities[0][:2000])
ax1.plot([f for f in xrange(2000)],neuron_activities[5][:2000])

ax2.plot([f for f in xrange(8000)],neuron_activities[93][:8000])
ax2.plot([f for f in xrange(8000)],neuron_activities[23][:8000])

plt.savefig("neuronplot.png")
plt.show()
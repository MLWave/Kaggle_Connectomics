import brainparse
import pygame
import sys

#parse all data
neuron_activities = brainparse.parse_time_series("d:\\brain\\fluorescence_iNet1_Size100_CC02inh.txt")
neuron_positions = brainparse.parse_neuron_positions("d:\\brain\\networkPositions_iNet1_Size100_CC02inh.txt")
neuron_connections, blocked = brainparse.parse_neuron_connections("d:\\brain\\network_iNet1_Size100_CC02inh.txt")

white = (255,255,255)
grey = (190,190,190)
lightgrey = (0,128,255)

#initialize pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
screen.fill(white)

#draw our network connections between the neurons
for neuron_connection, connection_type in neuron_connections.items():
	if connection_type == -1:
		pygame.draw.lines(screen, lightgrey, False, [neuron_positions[neuron_connection[0]],neuron_positions[neuron_connection[1]]], 1)
	else:
		pygame.draw.lines(screen, grey, False, [neuron_positions[neuron_connection[0]],neuron_positions[neuron_connection[1]]], 1)		
pygame.display.update()

#loop time series
npi = neuron_positions.items()
frame = 0
for frame in xrange(975,len(neuron_activities[0])):
	#draw our neurons in their positions
	for neuron_id, neuron_position in npi:
		s = pygame.Surface((30,30))
		if neuron_activities[neuron_id][frame] > 0:
			if neuron_activities[neuron_id][frame] > 0.9:
				color = (255,255,0)
			else:
				color = (int(neuron_activities[neuron_id][frame] * 254),int(neuron_activities[neuron_id][frame] * 254),255-int(neuron_activities[neuron_id][frame] * 254))
		else:
			color = (0,0,255)
		pygame.draw.circle(screen, color, neuron_position, 20)
	pygame.display.update()
	pygame.time.delay(100)
	#pygame.image.save(screen, "model"+str(frame)+".jpg")
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
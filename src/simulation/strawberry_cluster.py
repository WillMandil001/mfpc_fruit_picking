import time
import math
import numpy as np


class StrawberryCluster(object):
	def __init__(self, p, position):
		# 1. Define random pose for each strawberry within some limit.
		# 2. spawn strawberry into pose
		p.loadURDF("models/strawberry_cluster.urdf", np.array(position), [0,0,0,1], useFixedBase=True)


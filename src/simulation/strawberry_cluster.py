import time
import math
import numpy as np


class StrawberryCluster(object):
	def __init__(self, p, position, orientation):
		# 1. Define random pose for each strawberry within some limit.
		# 2. spawn strawberry into pose
		self.pendulum = p.loadURDF("models/strawberry_cluster.urdf", np.array(position), orientation, useFixedBase=True)

		# p.resetJointState(pendulum, 0, 0.5)
		# p.setJointMotorControl2(pendulum, 0, controlMode=p.TORQUE_CONTROL, force=0.000)
		# p.resetJointState(pendulum, 1, 0.5)
		p.setJointMotorControl2(self.pendulum, 1, controlMode=p.TORQUE_CONTROL, force=0.000)
		p.setJointMotorControl2(self.pendulum, 1, p.VELOCITY_CONTROL, force=0.000)

		p.changeDynamics(self.pendulum, 1, linearDamping=2.5, angularDamping=2.5, contactStiffness=0.0, contactDamping=0.0, 
						lateralFriction=0.0, spinningFriction=0.0, rollingFriction=0.0, jointDamping=0.0)

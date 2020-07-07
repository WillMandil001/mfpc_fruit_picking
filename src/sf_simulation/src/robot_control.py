import pybullet as p
import pybullet_data
import time
import numpy as np
import franka_panda

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.81)
planeId = p.loadURDF("plane.urdf")

timeStep=1./60.
start_pos = [0,0,0]
Joint_start_state = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.02, 0.02]
panda = franka_panda.FrankaPanda(p, start_pos, timeStep, Joint_start_state)

while (1):
	panda.step()
	p.stepSimulation()
	time.sleep(timeStep)



# huskypos = [0, 0, 0.1]
# husky = p.loadURDF("husky/husky.urdf", huskypos[0], huskypos[1], huskypos[2])
# numJoints = p.getNumJoints(husky)
# for joint in range(numJoints):
#   print(p.getJointInfo(husky, joint))
# targetVel = 10  #rad/s
# maxForce = 100  #Newton

# for joint in range(2, 6):
#   p.setJointMotorControl(husky, joint, p.VELOCITY_CONTROL, targetVel, maxForce)
# for step in range(300):
#   p.stepSimulation()

# targetVel = -10
# for joint in range(2, 6):
#   p.setJointMotorControl(husky, joint, p.VELOCITY_CONTROL, targetVel, maxForce)
# for step in range(400):
#   p.stepSimulation()

# p.getContactPoints(husky)

# p.disconnect()
import time
import socket      
import franka_panda
import pybullet_data
import strawberry_cluster
import franka_panda_new_EE
import numpy as np
import pybullet as p
  
s = socket.socket()
port = 12342
s.bind(('', port))
s.listen(5)

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.81)
timeStep=1./240.
p.setTimeStep(timeStep)
planeId = p.loadURDF("plane.urdf")

## Load franka:
start_pos = [0,0,0]
Joint_start_state = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.02, 0.02]
panda = franka_panda.FrankaPanda(p, start_pos, timeStep, Joint_start_state)

## load strawberry cluster:
start_pose = [0.5, 0.5, 1.0]
start_ori = [0, 0, 1, 0]
cluster = strawberry_cluster.StrawberryCluster(p, start_pose, start_ori)

start_pose = [0.53, 0.53, 1.0]
start_ori = [0, 0, 0, 1]
cluster2 = strawberry_cluster.StrawberryCluster(p, start_pose, start_ori)

# c, addr = s.accept()
# print('Got connection from', addr)
for i in range(0,1000):
	# q = p.getJointState(cluster.pendulum, 1)[0]
	# print(q)

	# pos, vel, rf, jmt = p.getJointStates(panda.franka, [0,1,2,3])
	# print(vel)
	print(p.getJointState(panda.franka, 1))
	# joint_state = '[0,1,2,3,4,5,6,7]'
	# c.send(joint_state.encode('utf-8')) 

	p.configureDebugVisualizer(p.COV_ENABLE_SINGLE_STEP_RENDERING) 
	# panda.step()

	p.stepSimulation()
	time.sleep(timeStep)

# s.close()
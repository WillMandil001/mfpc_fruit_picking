import pybullet as p
import pybullet_data
import time
import numpy as np
import franka_panda
import franka_panda_new_EE
import strawberry_cluster

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.81)
timeStep=1./240.
p.setTimeStep(timeStep)
planeId = p.loadURDF("plane.urdf")


## Load franka:
start_pos = [0,0,0]
Joint_start_state = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.02, 0.02]
panda = franka_panda_new_EE.FrankaPanda(p, start_pos, timeStep, Joint_start_state)

## load strawberry cluster:
start_pose = [0.5, 0.5, 1.0]
start_ori = [0, 0, 1, 0]
cluster = strawberry_cluster.StrawberryCluster(p, start_pose, start_ori)

start_pose = [0.53, 0.53, 1.0]
start_ori = [0, 0, 0, 1]
cluster = strawberry_cluster.StrawberryCluster(p, start_pose, start_ori)


# start_pose = [0.5, 0.52, 1.0]
# start_ori = [0, 0, 0, 1]
# cluster2 = strawberry_cluster.StrawberryCluster(p, start_pose, start_ori)

while (1):
	p.configureDebugVisualizer(p.COV_ENABLE_SINGLE_STEP_RENDERING) 
	panda.step()    
	
	q = p.getJointState(cluster.pendulum, 1)[0]
	print(q)

	p.stepSimulation()
	time.sleep(timeStep)

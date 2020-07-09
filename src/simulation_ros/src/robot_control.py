import pybullet as p
import pybullet_data
import time
import numpy as np
import franka_panda
import strawberry_cluster

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.81)
planeId = p.loadURDF("plane.urdf")
timeStep=1./60.

## Load franka:
start_pos = [0,0,0]
Joint_start_state = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.02, 0.02]
panda = franka_panda.FrankaPanda(p, start_pos, timeStep, Joint_start_state)

## load strawberry cluster:
# start_pose = [0.5, 0.5, 0.7]
# cluster = strawberry_cluster.StrawberryCluster(p, start_pose)

start_pose = [0.5, 0.5, 1.0]
start_ori = [0, 0, 0, 1]
cluster = strawberry_cluster.StrawberryCluster(p, start_pose)
# pendulum5 = p.loadURDF("pendulum5.urdf", start_pose, start_ori)

while (1):
	panda.step()
	p.stepSimulation()
	time.sleep(timeStep)

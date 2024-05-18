#python
import numpy as np

def sysCall_init():
    global camera_handle
    sim = require('sim')

    camera_handle = sim.getObjectHandle('Vision_sensor')
    object_handle = sim.getObjectHandle('Sphere')
    obj_position = sim.getObjectPosition(object_handle, -1)
    cam_position = sim.getObjectPosition(camera_handle, -1)
    cam_orientation = sim.getObjectOrientation(camera_handle, -1)
    print("cam_position", cam_position)
def sysCall_thread():
    # Put your main code here, e.g.:
    #
    while not sim.getSimulationStopping():
         p = sim.getObjectPosition(camera_handle, -1)
         euler = sim.getObjectOrientation(camera_handle, -1)
         p[0] += 0.001
         p[1] += 0.001
         euler[0] +=np.pi/19
         sim.setObjectPosition(camera_handle, -1, p)
         sim.setObjectOrientation(camera_handle, -1, euler)
         sim.step() # resume in next simulation step
    
# See the user manual or the available code snippets for additional callback functions and details


"""
#python
import numpy as np

def sysCall_init():
    global camera_handle
    sim = require('sim')

    camera_handle = sim.getObjectHandle('Vision_sensor')
    object_handle = sim.getObjectHandle('Sphere')
    obj_position = sim.getObjectPosition(object_handle, -1)
    cam_position = sim.getObjectPosition(camera_handle, -1)
    cam_orientation = sim.getObjectOrientation(camera_handle, -1)
    print("cam_position", cam_position)
def sysCall_thread():
    # Put your main code here, e.g.:
    #
    poses = np.array([[0,0,0],[0.45, 0.32,0], [1.01, -0.075,0], [0.37, -0.6, 0], [0.37, -0.6, 0]])    
    i = 0
    while not sim.getSimulationStopping():
        p = poses[i,:]
        euler = sim.getObjectOrientation(camera_handle, -1)

        sim.setObjectPosition(camera_handle, -1, list(p))

        sim.step() # resume in next simulation step
        i += 1
        if i == 4:
            break
"""

import sim
import numpy as np
import sys
import matplotlib.pyplot as plt
sim.simxFinish(-1)
clientID = sim.simxStart('127.0.0.1', 19999, True, True, 5000, 5)
if clientID != -1:
    print('Connected Successfully.')
else:
    sys.exit('Failed To connect.')
    
error_code, left_motor_handle = sim.simxGetObjectHandle(clientID, 'Pioneer_p3dx_leftMotor', sim.simx_opmode_oneshot_wait)
error_code, right_motor_handle = sim.simxGetObjectHandle(clientID, 'Pioneer_p3dx_rightMotor', sim.simx_opmode_oneshot_wait)
res, object_handle_indoorPlant0 = sim.simxGetObjectHandle(clientID, 'indoorPlant0', sim.simx_opmode_oneshot_wait)
res, object_handle_indoorPlant1 = sim.simxGetObjectHandle(clientID, 'indoorPlant1', sim.simx_opmode_oneshot_wait)

res1, poses_plant0 = sim.simxGetObjectPosition(clientID, object_handle_indoorPlant0, -1, sim.simx_opmode_oneshot_wait)
        
res2, orientation_indoorPlant0 = sim.simxGetObjectOrientation(clientID, object_handle_indoorPlant0, -1, sim.simx_opmode_oneshot_wait)
# Get the current position of the object
plt.plot(poses_plant0[0], poses_plant0[1], 'b*')
        


while(True):
    error_code, position = sim.simxGetObjectPosition(clientID, left_motor_handle, -1, sim.simx_opmode_oneshot_wait)
    if error_code == sim.simx_return_ok:
        print("Pioneer position: ", position)
    else:
        print("Could not get position")
    # Get the orientation of the Pioneer robot
    error_code, orientation = sim.simxGetObjectOrientation(clientID, left_motor_handle, -1, sim.simx_opmode_oneshot_wait)
    if error_code == sim.simx_return_ok:
        print("Pioneer orientation: ", orientation)
    else:
        print("Could not get orientation")
    plt.plot(position[0], position[1], 'ro')
    plt.pause(0.01)
plt.show()
        
    
    


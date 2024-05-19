#python

def sysCall_init():
    global wheel_right
    global wheel_left
    global robot_handle
    global graph_x
    global graph_y
    global graphHandle_xy
    global graphHandle_d
    global proximity
    global dist
    global graph
    global graph_distance
    sim = require('sim')
    graphHandle_xy = sim.getObject('/Graph1')
    graphHandle_d = sim.getObject('/Graph2')
    proximity = sim.getObject('/Proximity_sensor')
    wheel_right = sim.getObject('/rightMotor')
    wheel_left = sim.getObject('/leftMotor')
    robot_handle = sim.getObject('/PioneerP3DX')
    graph_distance = sim.addGraphStream(graphHandle_d, 'distance',proximity, 0, [0.1, 0.8, 0.2])
                                    
    graph_x = sim.addGraphStream(graphHandle_xy, 'x', 'g',1, [1, 0.8, 0.2])
    graph_y = sim.addGraphStream(graphHandle_xy, 'y', 'g',1)

def sysCall_actuation():
    t = sim.getSimulationTime()
    if (t>1 and dist>0.7) or (t>1 and dist==0):
        
        sim.setJointTargetVelocity(wheel_left,2)
        sim.setJointTargetVelocity(wheel_right,2)
        position = sim.getObjectPosition(robot_handle, sim.handle_world)
        orientation = sim.getObjectOrientation(robot_handle , sim.handle_world)
        sim.setGraphStreamValue(graphHandle_xy,graph_x,position[0])
        sim.setGraphStreamValue(graphHandle_xy,graph_y,position[1])
        
        print("dist = ", dist)
    elif(t>1 and dist<0.7):
        sim.setJointTargetVelocity(wheel_left,7)
        sim.setJointTargetVelocity(wheel_right,-7)
    else:
        sim.setJointTargetVelocity(wheel_left,3)
        sim.setJointTargetVelocity(wheel_right,3)

def sysCall_sensing():
    global dist
    res, dist, point, obj, n = sim.readProximitySensor(proximity)
    print("dist = ", dist)
    sim.setGraphStreamValue(graphHandle_d,graph_distance,dist)


    


    
    
    

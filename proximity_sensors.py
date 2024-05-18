#python

def sysCall_init():
    global joint_right
    global joint_left
    global robot_handle
    global graph_x
    global graph_y
    global graphHandle
    global proximity
    global dist
    global graph
    global graph_distance
    sim = require('sim')
    graphHandle = sim.getObject('/Graph')
    proximity = sim.getObject('/Proximity_sensor')
    graph_distance = sim.addGraphStream(graphHandle, 'distance',' ', 0, [1,0,0], 0)
    joint_right = sim.getObject('/rightMotor')
    joint_left = sim.getObject('/leftMotor')
    robot_handle = sim.getObject('/PioneerP3DX')
    sim.setObjectInt32Param(joint_right,sim.jointintparam_dynctrlmode,sim.jointdynctrl_velocity)
    sim.setObjectInt32Param(joint_left,sim.jointintparam_dynctrlmode,sim.jointdynctrl_velocity)
    
    sim.setJointTargetVelocity(joint_left,2)
    sim.setJointTargetVelocity(joint_right,2)
    graph_x = sim.addGraphStream(graphHandle, 'x', 'm',1)
    graph_y = sim.addGraphStream(graphHandle, 'y', 'm',1)
    curveId = sim.addGraphCurve(graphHandle, 'x/y', 2, [graph_x,graph_y], [0,0],'m by m',0,[1, 0, 0],2)

def sysCall_actuation():
    t = sim.getSimulationTime()
    if (t>1 and dist>0.7) or (t>1 and dist==0):
        
        sim.setJointTargetVelocity(joint_left,2)
        sim.setJointTargetVelocity(joint_right,2)
        position = sim.getObjectPosition(robot_handle, sim.handle_world)
        orientation = sim.getObjectOrientation(robot_handle , sim.handle_world)
        sim.setGraphStreamValue(graphHandle,graph_x,position[0])
        sim.setGraphStreamValue(graphHandle,graph_y,position[1])
        
        print("dist = ", dist)
    elif(t>1 and dist<0.7):
        sim.setJointTargetVelocity(joint_left,7)
        sim.setJointTargetVelocity(joint_right,-7)
    else:
        sim.setJointTargetVelocity(joint_left,3)
        sim.setJointTargetVelocity(joint_right,3)

def sysCall_sensing():
    global dist
    res, dist, point, obj, n = sim.readProximitySensor(proximity)
    print("dist = ", dist)
    sim.setGraphStreamValue(graphHandle,graph_distance,dist)


    


    
    
    

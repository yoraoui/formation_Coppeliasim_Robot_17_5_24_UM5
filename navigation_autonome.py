#python

def sysCall_init():
    """
    Initializes the system.
    """
    sim = require('sim')
    robot=sim.getObject('.')
    obstacles=sim.createCollection(0)
    sim.addItemToCollection(obstacles,sim.handle_all,-1,0)
    sim.addItemToCollection(obstacles,sim.handle_tree,robot,1)
    self.usensors={}
    for i in range(16):
        self.usensors[i] = sim.getObject("./ultrasonicSensor", {"index": i-1})
        sim.setObjectInt32Param(self.usensors[i],sim.proxintparam_entity_to_detect,obstacles)
    
    
    self.motorLeft=sim.getObject("./leftMotor")
    self.motorRight=sim.getObject("./rightMotor")
    self.noDetectionDist=0.5
    self.maxDetectionDist=0.2
    self.detect=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    self.braitenbergL=[-0.2,-0.4,-0.6,-0.8,-1,-1.2,-1.4,-1.6, 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    self.braitenbergR=[-1.6,-1.4,-1.2,-1,-0.8,-0.6,-0.4,-0.2, 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    self.v0=2

#This is a very simple EXAMPLE navigation program, which avoids obstacles using the Braitenberg algorithm



def sysCall_actuation():
    """
    This function performs the actuation step of the system.
    It reads proximity sensor data, calculates the detection level,
    and sets the target velocities for the left and right motors.
    """
    for i in range(16) :
        res,dist, _, _, _=sim.readProximitySensor(self.usensors[i])
        if (res>0) and (dist<self.noDetectionDist):
            if (dist<self.maxDetectionDist):
                dist=self.maxDetectionDist
            
            self.detect[i]=1-((dist-self.maxDetectionDist)/(self.noDetectionDist-self.maxDetectionDist))
        else:
            self.detect[i]=0
    
    
    vLeft=self.v0
    vRight=self.v0
    
    for i in range(16):
        vLeft=vLeft+self.braitenbergL[i]*self.detect[i]
        vRight=vRight+self.braitenbergR[i]*self.detect[i]
    
    sim.setJointTargetVelocity(self.motorLeft,vLeft)
    sim.setJointTargetVelocity(self.motorRight,vRight)


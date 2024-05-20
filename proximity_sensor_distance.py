#python

def sysCall_init():
    global handle_proximity_sensor
    sim = require('sim')
    handle_proximity_sensor = sim.getObject("/Proximity_sensor")


def sysCall_actuation():
    # put your actuation code here
    pass

def sysCall_sensing():


    res, dist, point, obj, n = sim.readProximitySensor(handle_proximity_sensor)
    print("dist = ", dist)
def sysCall_cleanup():
    # do some clean-up here
    pass

# See the user manual or the available code snippets for additional callback functions and details

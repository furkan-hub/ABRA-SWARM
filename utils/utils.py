import math
import numpy as np
from dronekit import *
import time

def connet_swarm(address,drone_count):
    drones = []
    for i in range(drone_count):
        drone = connect(address[i],wait_ready=False)

        drones.append(drone)
        #time.sleep(2)
    print("Connected all drones !")
    return drones

def get_telem(drones):
    
    telems = []

    for i in range(len(drones)):
        
        telem = {
            "drone_num": [i],
            "lat":float(drones[i].location.global_frame.lat),
            "lon":float(drones[i].location.global_frame.lon),
            "alt":float(drones[i].location.global_frame.lon),
            "pitch": float((drones[i].attitude.pitch)*(180 / math.pi)),
            "yaw": float((drones[i].attitude.yaw)*(180 / math.pi)),
            "roll": float((drones[i].attitude.roll)*(180 / math.pi))
        }
        
        telems.append(telem)
    
    return telems

def arm_and_takeoff(drones):
    for i in range(len(drones)):
        
        print(drones[i]," is arming and takeoff")
        drones[i].mode = "GUIDED"
        time.sleep(1)
        
        print(drones[i]," is arming")
        drones[i].armed
        time.sleep(1)
        
        print(drones[i]," is takeoff")
        drones[i].simple_takeoff(10)
        time.sleep(1)

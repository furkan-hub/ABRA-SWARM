from pyproj import Transformer
import numpy as np
import copy

#region rotation matris
def yaw_rotation_matrix(yaw_angle):
    yaw_matrix = np.array([
        [np.cos(yaw_angle), -np.sin(yaw_angle), 0],
        [np.sin(yaw_angle), np.cos(yaw_angle), 0],
        [0, 0, 1]
    ])
    return yaw_matrix

def pitch_rotation_matrix(pitch_angle):
    pitch_matrix = np.array([
        [np.cos(pitch_angle), 0, np.sin(pitch_angle)],
        [0, 1, 0],
        [-np.sin(pitch_angle), 0, np.cos(pitch_angle)]
    ])
    return pitch_matrix

def roll_rotation_matrix(roll_angle):
    roll_matrix = np.array([
        [1, 0, 0],
        [0, np.cos(roll_angle), -np.sin(roll_angle)],
        [0, np.sin(roll_angle), np.cos(roll_angle)]
    ])
    return roll_matrix
#endregion

def len3d(vec3):
    return np.sqrt(vec3[0]**2+vec3[1]**2+vec3[2]**2)
def subList(list1,list2):
    result=[]
    for i in range(len(list1)):
        result.append(list1[i]-list2[i])
    return result

class LocationConverter:
    def __init__(self) -> None:
        self.trans_GPS_to_XYZ = Transformer.from_crs(4979, 4978)
    def relativeLoc(self,loc1,loc2):
        """lat,lon,alt"""
    # lon,lat,alt -> x,y,z
        first=self.trans_GPS_to_XYZ.transform(*loc1)
        rad1=len3d(first)
    # ang1=[-30.2906140,0,-40.7991680]
        second=self.trans_GPS_to_XYZ.transform(*loc2)
        rad2=len3d(second)
        z=rad2-rad1
        locx=copy.copy(loc1)
        locy=copy.copy(loc1)
        locx[1]=loc2[1]
        locy[0]=loc2[0]
        distx=subList(self.trans_GPS_to_XYZ.transform(*locx),first)
        disty=subList(self.trans_GPS_to_XYZ.transform(*locy),first)
        distx=len3d(distx)*np.sign(loc2[1]-loc1[1])
        disty=len3d(disty)*np.sign(loc2[0]-loc1[0])
        return [distx,disty,z]
    


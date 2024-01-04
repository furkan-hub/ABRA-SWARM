from dronekit import *
import json
from utils.utils import *
import time

# JSON dosyasını okuma ve içeriğini alma
with open('param.json', 'r') as file:
    drone_addres_dict = json.load(file)
    
#dict olan veriyi array haline çevirime
drone_addres_array = list(drone_addres_dict.values())

drones = connet_swarm(drone_addres_array,3)#parametre jsonun da kim tüm adresslere bağlanır

print("ok")

time.sleep(1)

arm_and_takeoff(drones)

while True:
    
    telems = get_telem(drones)#bağlanılan tüm dronelarda telemetri paketleri oluşturur

    print(telems)
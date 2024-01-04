#!/bin/bash

# Gazebo'yu aç
gnome-terminal --tab --title="Gazebo" -- bash -c "gazebo --verbose ~/ardupilot_gazebo/worlds/iris_arducopter_runway.world; exec bash"

# İlk drone'u aç
gnome-terminal --tab --title="Drone 1" -- bash -c "sleep 1; sim_vehicle.py -v ArduCopter -f gazebo-drone1 --no-mavproxy -I0; exec bash"

# İkinci drone'u aç
gnome-terminal --tab --title="Drone 2" -- bash -c "sleep 1; sim_vehicle.py -v ArduCopter -f gazebo-drone2 --no-mavproxy -I1; exec bash"

# Üçüncü drone'u aç
gnome-terminal --tab --title="Drone 3" -- bash -c "sleep 1; sim_vehicle.py -v ArduCopter -f gazebo-drone3 --no-mavproxy -I2; exec bash"

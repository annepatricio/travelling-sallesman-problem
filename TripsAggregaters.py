from database import *
from random import *
from GroupTrips import *
from math import trunc

# Generate random trips
tripOrigins = []
number_of_origins = len(origins)
i = 0
while (i < totaltrips):
    origin = random()
    index = 0
    if ((index == 0) and (origin <= graduation[index])):
            tripOrigins.append(origins[index])
    else:
        while (index < number_of_origins):
            if((origin <= graduation[index]) and (origin > graduation[index-1])):
                tripOrigins.append(origins[index])
            index = index + 1
    i = i + 1


# Aggregate trips
i=0
index = 0
number_of_groups = trunc(totaltrips/vehicleCapacity)
gtrips = []

while (index < totaltrips):
    gtrips.append(GroupTrips(i))
    x = 0
    for x in range(vehicleCapacity):
        gtrips[i].group_origins.append(tripOrigins[index+x])
        x = x + 1
    print(gtrips[i].group_origins)
    gtrips[i].group_origins.insert(0, zoneCentroid[0])
    gtrips[i].distance_matrix_calculator()
    gtrips[i].minimum_route_distance_calculator()
    index = index + vehicleCapacity
    i=i + 1



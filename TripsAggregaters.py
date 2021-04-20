from subzone import *
from random import *
from GroupTrips import *
from math import trunc

# Generate random trips
tripOrigins = []
i = 0
while (i < totaltrips):
    origin = random()
    if (origin <= graduation[0]):
        tripOrigins.append(subzones[0])
    else:
        if (origin <= graduation[1]):
            tripOrigins.append(subzones[1])
        else:
            tripOrigins.append(subzones[2])
    i = i + 1

print(tripOrigins)
# Aggregate trips
i=0
index = 0
number_of_groups = trunc(totaltrips/vehicleCapacity)
gtrips = []

while (index < totaltrips):
    gtrips.append(GroupTrips( i, tripOrigins[index], tripOrigins[index+1], tripOrigins[index+2], tripOrigins[index+3]))
    gtrips[i].distance_matrix_calculator(tripOrigins[index], tripOrigins[index+1], tripOrigins[index+2], tripOrigins[index+3])
    gtrips[i].minimum_route_distance_calculator()
    index = index + vehicleCapacity
    i=i + 1



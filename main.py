

import numpy
from TripsAggregaters import *
from GroupTrips import *

#TSP
print("Group trips:")
i = 0
total_route_distances = 0
while (i < number_of_groups):
    print("index: ", gtrips[i].groupNumber, "origins: ", gtrips[i].origin1, ",", gtrips[i].origin2,",", gtrips[i].origin3,",", gtrips[i].origin4,"Minimum route distance:",gtrips[i].minimum_route_distance,"Minimum route:",gtrips[i].minimum_route)
    total_route_distances = total_route_distances + gtrips[i].minimum_route_distance
    i = i+1

med_distance_traveled = total_route_distances/number_of_groups
print(med_distance_traveled)
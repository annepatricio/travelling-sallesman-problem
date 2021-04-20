

import numpy
from TripsAggregaters import *
from GroupTrips import *

#TSP
print("Group trips:")
i = 0
total_route_distances = 0
while (i < number_of_groups):
    print(gtrips[i].groupNumber,", origins: ",gtrips[i].group_origins,", minimum route distance: ", gtrips[i].minimum_route_distance,", minimum route: ", gtrips[i].minimum_route)
    total_route_distances = total_route_distances + gtrips[i].minimum_route_distance
    i = i+1

med_distance_traveled = total_route_distances/number_of_groups
print(med_distance_traveled)
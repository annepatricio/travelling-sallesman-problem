
from TripsAggregaters import *
from python_tsp.exact import solve_tsp_dynamic_programming
import numpy

i = 0
while (i < number_of_groups):
    newDistanceArray = numpy.array(gtrips[i].distance_matrix)
    permutation, distance = solve_tsp_dynamic_programming(newDistanceArray)
    i = i+1
    print(distance)

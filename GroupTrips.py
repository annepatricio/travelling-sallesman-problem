from database import *
from TripsAggregaters import *
from python_tsp.exact import solve_tsp_dynamic_programming
import numpy

class GroupTrips:

    def __init__(self, groupNumber):
        self.groupNumber = groupNumber
        self.group_origins = []
        self.distance_matrix = []

    def distance_matrix_calculator(self):
        lines = 0
        set_of_origins = []
        number_of_origins = len(self.group_origins)
        while (lines < number_of_origins):
            columns = 0
            set_of_origins.clear()
            while(columns < number_of_origins):
                set_of_origins.append(distances[zone_and_subzones.index(self.group_origins[lines])][zone_and_subzones.index(self.group_origins[columns])])
                columns = columns + 1
            self.distance_matrix.insert(lines, set_of_origins.copy())
            lines = lines + 1

    def minimum_route_distance_calculator(self):
        newDistanceArray = numpy.array(self.distance_matrix)
        permutation, distance = solve_tsp_dynamic_programming(newDistanceArray)
        self.minimum_route_distance = distance
        self.minimum_route = permutation

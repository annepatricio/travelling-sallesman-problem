from subzone import *
from TripsAggregaters import *
from python_tsp.exact import solve_tsp_dynamic_programming
import numpy

class GroupTrips:

    def __init__(self, groupNumber, origin1, origin2,origin3,origin4):
        self.groupNumber = groupNumber
        self.origin1 = origin1
        self.origin2 = origin2
        self.origin3 = origin3
        self.origin4 = origin4
        self.distance_matrix = []


    def distance_matrix_calculator(self, origin1, origin2, origin3, origin4):
        self.distance_matrix.insert(0,[distances[subzones.index(origin1)][subzones.index(origin1)], distances[subzones.index(origin1)][subzones.index(origin2)], distances[subzones.index(origin1)][subzones.index(origin3)],distances[subzones.index(origin1)][subzones.index(origin4)]])
        self.distance_matrix.insert(1,[distances[subzones.index(origin2)][subzones.index(origin1)], distances[subzones.index(origin2)][subzones.index(origin2)], distances[subzones.index(origin2)][subzones.index(origin3)],distances[subzones.index(origin2)][subzones.index(origin4)]])
        self.distance_matrix.insert(2,[distances[subzones.index(origin3)][subzones.index(origin1)], distances[subzones.index(origin3)][subzones.index(origin2)], distances[subzones.index(origin3)][subzones.index(origin3)],distances[subzones.index(origin3)][subzones.index(origin4)]])
        self.distance_matrix.insert(3,[distances[subzones.index(origin4)][subzones.index(origin1)], distances[subzones.index(origin4)][subzones.index(origin2)], distances[subzones.index(origin4)][subzones.index(origin3)],distances[subzones.index(origin4)][subzones.index(origin4)]])


    def minimum_route_distance_calculator(self):
        newDistanceArray = numpy.array(self.distance_matrix)
        permutation, distance = solve_tsp_dynamic_programming(newDistanceArray)
        self.minimum_route_distance = distance
        self.minimum_route = permutation

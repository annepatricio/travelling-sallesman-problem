# Database
distanceToCentroid: [ 1, 2, 4]
zoneCentroid = ["can"]
origins = ["can1", "can2", "can3"]
zone_and_subzones = zoneCentroid + origins
print(zone_and_subzones)
populations = [250, 250, 250]
distances = [[0, 2, 5, 4], [2, 0, 5, 3], [5, 5, 0,1 ], [4, 3, 1, 0]]
travel_times = [[0, 20, 50, 40], [20, 0, 50, 30], [50, 50, 0,10], [40, 30, 10, 0]]
vehicleCapacity = 5
totaltrips = 50


# TotalPopulation and proportions
totalPopulation = 0
for i in populations:
    totalPopulation += i
print(totalPopulation)
proportions = []
for i in populations:
    proportions.append(i / totalPopulation)
print("proportions: ",proportions)
graduation = []
value = 0
i = 0
while (i < len(proportions)):
    value = value + proportions[i]
    graduation.append(value)
    i = i + 1
print("graduation: ",graduation)




import pandas as pd
import numpy as np
import openpyxl

# Database
vehicleCapacity = 8
totaltrips = 800


file = pd.read_excel("zones.xlsx")
print(file)
data = pd.DataFrame(file)
data2 = data.to_numpy()
d3 = np.array(data2)
lines = len(d3)
row = 1
zoneCentroid = []
origins = []
populations = []
zoneCentroid.append(d3[0, 0])
distances = []
travel_times = []
for ori in range(lines):
    origins.append(d3[ori, 1])
    populations.append(d3[ori, 2])

zone_and_subzones = zoneCentroid + origins
print(zone_and_subzones)

file2 = pd.read_excel("Input.xlsx")
dat = pd.DataFrame(file2)
dat2 = dat.to_numpy()
dat3 = np.array(dat2)
distance_per_org = []
travel_times_per_org = []
dest = 0
for ori in range(lines+1):
    for i in range(lines+1):
        distance_per_org.append(dat3[dest, 2])
        travel_times_per_org.append(dat3[dest, 3])
        dest = dest + 1
    ori = ori + 1
    distances.append(distance_per_org.copy())
    travel_times.append(travel_times_per_org.copy())
    distance_per_org.clear()
    travel_times_per_org.clear()


print(distances)
print(travel_times)



# TotalPopulation and proportions
totalPopulation = 0
for i in populations:
    totalPopulation += i
print(totalPopulation)
proportions = []
for i in populations:
    proportions.append(i/ totalPopulation)
print("proportions: ", proportions)
graduation = []
value = 0
i = 0
while (i < len(proportions)):
    value = value + proportions[i]
    graduation.append(value)
    i = i + 1
print("graduation: ",graduation)




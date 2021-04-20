# Database
distanceToCentroid:[ 1, 2, 4]
subzones = ["can1", "can2", "can3"]
populations = [250, 250, 250]
distances = [[0, 2, 5], [2, 0, 5], [5, 5, 0]]
vehicleCapacity = 4
totaltrips = 40

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




import xlsxwriter
from main import *
from GroupTrips import *

workbook = xlsxwriter.Workbook('InterzoneDistances.xlsx')
worksheet = workbook.add_worksheet()

print("Group trips:")

row = 0
column = 0

worksheet.write(row, column, med_distance_traveled)

row += 1
column += 0
x = 0
y = 0
number_of_origins_groups = len(gtrips[0].group_origins)

worksheet.write(row, column, "Group Number")
worksheet.write(row, column + 1, "origins:")
worksheet.write(row, column + 1 + number_of_origins_groups, "Route:")
worksheet.write(row, column + number_of_origins_groups*2 + 1, "Minimum route distance")
worksheet.write(row, column + number_of_origins_groups*2 + 2, "Travel time")

row += 1
x = 0
y = 0


for i in range(number_of_groups):
    worksheet.write(row, column, gtrips[i].groupNumber)
    print(number_of_origins)
    while (x < number_of_origins_groups):
        worksheet.write(row, column + 1 + x, gtrips[i].group_origins[x])
        x += 1
    while (y < number_of_origins_groups):
        worksheet.write(row, column + 1 + number_of_origins_groups + y, gtrips[i].minimum_route[y])
        y += 1
    worksheet.write(row, column + number_of_origins_groups*2 + 1, gtrips[i].minimum_route_distance)
    worksheet.write(row, column + number_of_origins_groups * 2 + 2, gtrips[i].minimum_travel_time)
    row += 1
    x = 0
    y = 0

workbook.close()
import json
import csv
from Buildings import Buildings
from Elevator import Elevator

rows = []
with open('Ex1_Calls/Calls_a.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    rows = list(csv_reader)
    for x in range(len(rows)):
        rows[x][5] = 0
    print(rows)

with open('Ex1_Output/Ex1_Calls_case_1_b.csv', 'w', encoding='UTF8', newline='') as csv_file:
    write = csv.writer(csv_file)
    write.writerows(rows)

B1 = Buildings.from_json('Ex1_Buildings/B2.json')
Elist = (B1['_elevators'])
Elevator_list = []
for x in range(len(Elist)):
    Elevator_list.append(Elevator(Elist, x))
for x in range(len(Elevator_list)):
    print(Elevator_list[x].printelev())
print("-------------------------------------------------------")

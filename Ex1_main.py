import json
import csv
from Buildings import Buildings
from Elevator import Elevator
from Calls import Calls

call_list = Calls.from_csvTolist('Ex1_Calls/Calls_b.csv')
print(call_list)

B1 = Buildings.from_json('Ex1_Buildings/B2.json')
Elist = (B1['_elevators'])
Elevator_list = []
for x in range(len(Elist)):
    Elevator_list.append(Elevator(Elist, x))
print("-------------------------------------------------------")
for ilan in range(len(call_list)):
    x=Calls.allocate(call_list[ilan][2],call_list[ilan][3])
    call_list[ilan][5] = x

print(call_list)

with open('Ex1_Output/Ex1_Calls_case_1_b.csv', 'w', encoding='UTF8', newline='') as csv_file:
    write = csv.writer(csv_file)
    write.writerows(call_list)
import json
import csv
from Buildings import Buildings
from Elevator import *
from Calls import Calls


def takeSecond(elem):
    return elem[1]


call_list = Calls.from_csvTolist('Ex1_Calls/Calls_b.csv')
print(call_list)

B1 = Buildings.from_json('Ex1_Buildings/B1.json')
Elist = (B1['_elevators'])
Elevator_list = []
for x in range(len(Elist)):
    ele = Elevator(Elist, x)
    Elevator_list.append(Elevator(Elist, x))
Elevator_list = sorted(Elevator_list)  # sort the list according to speed
print("-------------------------------------------------------")
for ilan in range(len(call_list)):
    Calls.allocate(call_list[ilan], Elevator_list)


print(Elevator_list)
Elevator_list = sorted(Elevator_list)
print("----------------------------")
print(Elevator_list)

Calls.write_tofile('Ex1_Output/Ex1_Calls_case_1_b.csv', call_list)

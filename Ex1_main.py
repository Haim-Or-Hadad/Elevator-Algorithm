import json
import csv
from Buildings import Buildings
from Elevator import *
from Calls import Calls
from ElevatorAlgo import ElevatorAlgo
#קובץ שינויים בזמנים
#https://docs.google.com/spreadsheets/d/1NX_Lc0m9B4Oq4dq6bJPWMefnu866tttoPFz2NCJicxw/edit#gid=0
algo1 = ElevatorAlgo('Ex1_Buildings/B5.json', 'Ex1_Calls/Calls_c.csv', 'out.csv')
algo1.allocate()
algo1.write_tofile('Ex1_Output\Ex1_Calls_case_1_b.csv')

# def takeSecond(elem):
#     return elem[1]
#
#
# call_list = Calls.from_csvTolist('Ex1_Calls/Calls_b.csv')
# print(call_list)
#
# B1 = Buildings.from_json('Ex1_Buildings/B1.json')
# Elist = (B1['_elevators'])
# Elevator_list = []
# for x in range(len(Elist)):
#     ele = Elevator(Elist, x)
#     Elevator_list.append(Elevator(Elist, x))
# Elevator_list = sorted(Elevator_list)  # sort the list according to speed
# print("-------------------------------------------------------")
# for ilan in range(len(call_list)):
#     Calls.allocate(call_list[ilan], Elevator_list)
#
#
# print(Elevator_list)
# Elevator_list = sorted(Elevator_list)
# print("----------------------------")
# print(Elevator_list)
#
# Calls.write_tofile('Ex1_Output/Ex1_Calls_case_1_b.csv', call_list)

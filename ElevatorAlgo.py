import json
import csv
from Buildings import Buildings
from Elevator import *
from Calls import Calls


class ElevatorAlgo:
    def __init__(self, building, calls, output):
        b = Buildings.from_json(building)
        Elist = (b['_elevators'])
        Elevator_list = []
        for x in range(len(Elist)):
            ele = Elevator(Elist, x)
            Elevator_list.append(Elevator(Elist, x))
        call_list = Calls.from_csvTolist(calls)

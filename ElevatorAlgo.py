import json
import csv
import math

from Buildings import Buildings
from Elevator import *
from Calls import Calls


class ElevatorAlgo:
    def __init__(self, building, calls, output):
        b = Buildings.from_json(building)
        Elist = (b['_elevators'])
        self.Elevator_list = []
        for x in range(len(Elist)):
            ele = Elevator(Elist, x)
            self.Elevator_list.append(Elevator(Elist, x))
        self.call_list = Calls.from_csvTolist(calls)
        self.elev_time_status = []
        for x in range(len(self.Elevator_list)):
            self.elev_time_status.append(0)

    def write_tofile(self, output):
        Calls.write_tofile(self.call_list, output)

    def allocate(self):
        for i in self.call_list:
            self.update_position(i)
            min = self.Elevator_list[0].currfloor
            sel_elev = 0
            num = 0
            for e in self.Elevator_list:
                if i.status == 1:
                    if e.status == 1 or e.status == 0:
                        if (abs(e.currfloor - i.src) < abs(min - i.src)):
                            min = abs(e.currfloor - i.src)
                            sel_elev = num
                else:
                    if e.status == -1 or e.status == 0:
                        if (abs(e.currfloor - i.src) < abs(min - i.src)):
                            min = abs(e.currfloor - i.src)
                            sel_elev = num
                num += 1

            i.selected_elev = sel_elev
            self.Elevator_list[sel_elev].status = i.status
        afads = 3
        dasfasd = 4

    def update_position(self, call: Calls):
        time = call.time
        i = 0
        for x in self.Elevator_list:
            time_passed = self.elev_time_status[i]
            time_passed = abs(time_passed - call.time)
            self.elev_time_status[i] = call.time
            self.elev_time_status[i] = call.time
            if x.status == 1:
                curr_floor = x.currfloor
                delay_time = x._startTime + x._openTime
                elev_speed = x._speed
                if (time_passed - delay_time) * elev_speed > 0:
                    x.currfloor = curr_floor + (time_passed - delay_time) * elev_speed
            elif x.status == -1:
                curr_floor = x.currfloor
                delay_time = x._startTime + x._openTime
                elev_speed = x._speed
                if (time_passed - delay_time) > 0:
                    x.currfloor = math.ceil(curr_floor - (time_passed - delay_time) * elev_speed)
        i += 1

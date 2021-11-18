import json
import csv
import math
import queue

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
            min = 9999999999999
            sel_elev = 0
            num = 0 #elevator index
            for e in self.Elevator_list:
                if i.status == 1:
                    if e.status == 1 or e.status == 0:
                        if self.time_to(e, i.src) + len(e.dest) < min:
                            min = self.time_to(e, i.src) + len(e.dest)
                            sel_elev = num
                else:
                    if e.status == -1 or e.status == 0:
                        if self.time_to(e, i.src) + len(e.dest) < min:
                            min = self.time_to(e, i.src) + len(e.dest)
                            sel_elev = num
                num += 1

            i.selected_elev = sel_elev
            if (i.src < self.Elevator_list[sel_elev].currfloor):
                self.Elevator_list[sel_elev].status = -1
            else:
                self.Elevator_list[sel_elev].status = 1
            self.Elevator_list[sel_elev].dest.append(i.src)
            self.Elevator_list[sel_elev].dest.append(i.dest)

    def update_position(self, call: Calls):
        time = call.time
        i = 0
        for x in self.Elevator_list:
            time_passed = self.elev_time_status[i]
            time_passed = abs(time_passed - call.time)
            self.elev_time_status[i] = call.time
            curr_floor = x.currfloor
            delay_time = x._startTime + x._openTime
            elev_speed = x._speed
            if len(x.dest) > 0:
                timeneed = (abs(x.dest[0] - curr_floor) / elev_speed) + delay_time
                if x.status == 1:
                    self.update_up(x, time_passed, timeneed)

                elif x.status == -1:
                    self.update_down(x, time_passed, timeneed)

            i += 1


    # Function the calculate the time for the elevator current floor to the dest floor
    def time_to(self, elevator: Elevator, dest: int):
        dist = abs(dest - elevator.currfloor)
        return dist / elevator._speed

    def update_up(self, elev: Elevator, total_time_since: int, time_need4call):
        curr_floor = elev.currfloor
        delay_time = elev._startTime + elev._openTime
        elev_speed = elev._speed
        timeleft = total_time_since - time_need4call
        dest = elev.dest[0]
        if timeleft > 0:  # if there's more time left then we need then send the elevator with the time she need
            check = math.floor(curr_floor + (time_need4call - delay_time) * elev_speed)
            elev.currfloor = math.ceil(curr_floor + abs(time_need4call - delay_time) * elev_speed)
            if elev.currfloor >= dest:
                elev.currfloor=dest
            timeleft = total_time_since - time_need4call  # update time
        else:  # else the elevator need more time so send her with all the time
            check = elev.currfloor = math.ceil(curr_floor + abs(total_time_since - delay_time) * elev_speed)
            elev.currfloor = math.floor(curr_floor + abs(total_time_since - delay_time) * elev_speed)
            if elev.currfloor >= dest:
                elev.currfloor = dest
            timeleft = time_need4call - total_time_since  # update time
        check12 = elev.dest[0]
        if elev.currfloor >= elev.dest[0]:  # if the elevator passed the closest floor she need to go
            elev.dest.pop(0)  # delete the floor that she passed
            if len(elev.dest) == 0:  # if theres no more calls for the elevator then make her status 0
                elev.status = 0
            else:
                if elev.dest[0] > elev.currfloor:  # else make her status according to her next call
                    elev.status = 1
                else:
                    elev.status = -1
                if timeleft > 0:  # if theres time left after she got to her closest call then
                    # the elevator will get closer to the next floor in the time that left
                    if elev.dest[0] > elev.currfloor:  # test formula to calc the floor
                        # if the elevator need to go up
                        elev.currfloor = math.ceil(curr_floor + abs(timeleft - delay_time) * elev_speed)
                        if elev.currfloor >= elev.dest[0]:
                            elev.currfloor = elev.dest[0]
                            elev.dest.pop(0)
                    else:
                        # if the elevator need to go down
                        elev.currfloor = math.floor(curr_floor - (abs(timeleft - delay_time)) * elev_speed)
                        if elev.currfloor <= elev.dest[0]:
                            elev.currfloor = elev.dest[0]
                            elev.dest.pop(0)



    def update_down(self, elev: Elevator, total_time_since: int, time_need4call):
        curr_floor = elev.currfloor
        delay_time = elev._startTime + elev._openTime
        elev_speed = elev._speed
        timeleft = total_time_since - time_need4call
        if total_time_since > 0:
            if timeleft > 0:  # if there's more time left then we need then send the elevator with the time she need
                check = math.floor(curr_floor - abs(time_need4call - delay_time) * elev_speed)
                elev.currfloor = math.floor(curr_floor - (abs(time_need4call - delay_time)) * elev_speed)
                if elev.currfloor <= elev.dest[0]:
                    elev.currfloor = elev.dest[0]
                timeleft = total_time_since - time_need4call
            else:  # else the elevator need more time so send her with all the time
                check = math.floor(curr_floor - (abs(total_time_since - delay_time)) * elev_speed)
                elev.currfloor = math.ceil(curr_floor - (abs(total_time_since - delay_time)) * elev_speed)
                if elev.currfloor <= elev.dest[0]:
                    elev.currfloor = elev.dest[0]
                timeleft = time_need4call - total_time_since
            if elev.currfloor <= elev.dest[0]:  # if the elevator passed the closest floor she need to go
                elev.dest.pop(0)  # delete the floor that she passed
                if len(elev.dest) == 0:  # if theres no more calls for the elevator then make her status 0
                    elev.status = 0
                else:
                    if elev.dest[0] > elev.currfloor:  # else make her status according to her next call
                        elev.status = 1
                    else:
                        elev.status = -1
                    if timeleft > 0:  # if theres time left after she got to her closest call then
                        # the elevator will get closer to the next floor in the time that left
                        if elev.dest[0] > elev.currfloor:  # test formula to calc the floor
                            # if the elevator need to go up
                            elev.currfloor = math.ceil(curr_floor + abs(timeleft - delay_time) * elev_speed)
                            if elev.currfloor >= elev.dest[0]:
                                elev.currfloor = elev.dest[0]
                                elev.dest.pop(0)
                        else:
                            # if the elevator need to go down
                            elev.currfloor = math.floor(curr_floor - (abs(timeleft - delay_time)) * elev_speed)
                            if elev.currfloor <= elev.dest[0]:
                                elev.currfloor = elev.dest[0]
                                elev.dest.pop(0)


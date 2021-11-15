import csv
from Elevator import *


def speedtoelev(elevator_list: list):
    min = 9999999
    select = 0
    for x in range(len(elevator_list)):
        elev = elevator_list[x]
        if (elev.numberofcalls == 0):
            speed = ((elev.numberofcalls + 1) / (elev._speed + elev._closeTime + elev._openTime))
        else:
            speed = ((elev.numberofcalls) / (elev._speed + elev._closeTime + elev._openTime))
        if (speed < min):
            min = speed
            select = x
    elevator_list[select].numberofcalls = elevator_list[select].numberofcalls + 1
    return select


class Calls:
    def from_csvTolist(csvFile):
        with open(csvFile) as csv_file:
            csv_reader = csv.reader(csv_file)
            call_list = list(csv_reader)
        return call_list

    def allocate(call_list, elevator_list: list):
        src = int(call_list[2])
        dest = int(call_list[3])
        minfloor = elevator_list[0].getMinFloor()
        maxfloor = elevator_list[0].getMaxFloor()
        if src > maxfloor or src < minfloor or dest > maxfloor or dest < minfloor:
            raise Exception("Elevator Calls are not in bullding floor range")
        if src < dest:  # Up
            call_list[5] = speedtoelev(elevator_list)
            call_list[4] = 1

        else:
            call_list[5] = speedtoelev(elevator_list)
            call_list[4] = -1

    def write_tofile(rows, calllist):
        with open(rows, 'w', encoding='UTF8', newline='') as csv_file:
            write = csv.writer(csv_file)
            write.writerows(calllist)

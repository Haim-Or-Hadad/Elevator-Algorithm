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
    def __init__(self, time, src, dest, status, selected_elev):
        self.time = time
        self.src = src
        self.dest = dest
        self.status = status
        self.selected_elev = selected_elev

    def from_csvTolist(csvFile):
        with open(csvFile) as csv_file:
            csv_reader = csv.reader(csv_file)
            call_list = list(csv_reader)
            calls_arr = []
            for row in call_list:
                newcall = Calls(float(row[1]),
                                int(row[2]),
                                int(row[3]),
                                int(row[4]),
                                int(row[5]))
                calls_arr.append(newcall)

        return calls_arr

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

    def __str__(self):
        return f"Time: {self.time}, Src: {self.src} dest: {self._dest} allocated to {self.selected_elev}"

    def __repr__(self):
        return str(self)

import csv
from Elevator import *


def speedtoelev(elevator_list: list):
    min = 9999999
    select = 0
    for x in range(len(elevator_list)):
        elev = elevator_list[x]
        if(elev.numberofcalls==0):
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

    def allocate(src: int, dest: int, elevator_list: list):
        if src < dest:  # Up
            return speedtoelev(elevator_list)
        else:
            return speedtoelev(elevator_list)

    def write_tofile(rows):
        with open('Ex1_Output/Ex1_Calls_case_1_b.csv', 'w', encoding='UTF8', newline='') as csv_file:
            write = csv.writer(csv_file)
            write.writerows(rows)

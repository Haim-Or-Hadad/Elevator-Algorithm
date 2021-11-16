import csv
from Elevator import *


class Calls:
    def __init__(self, time, src, dest, status, selected_elev):
        self.time = time
        self.src = src
        self.dest = dest
        if src<dest:
            self.status = 1
        else:
            self.status = -1
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

    def __str__(self):
        return f"Elevator call,{self.time},{self.src},{self.dest},{self.status},{self.selected_elev}"

    def __repr__(self):
        return str(self)

    def write_tofile(call_list, output):
        with open(output, 'w', encoding='UTF8', newline='') as csv_file:
            write = csv.writer(csv_file)
            #for x in call_list:
                #y = x
            write.writerow(call_list)

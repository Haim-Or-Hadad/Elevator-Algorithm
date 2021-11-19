import json
import csv
import sys

from Buildings import Buildings
from Elevator import *
from Calls import Calls
from ElevatorAlgo import ElevatorAlgo





if __name__ == "__main__":
    if len(sys.argv) == 4:
        algo1 = ElevatorAlgo(sys.argv[1], sys.argv[2], sys.argv[3])
        algo1.allocate()
        algo1.write_tofile(sys.argv[3])
    else:
        algo1 = ElevatorAlgo('Ex1_Buildings/B4.json', 'Ex1_Calls/Calls_c.csv', 'out.csv')
        algo1.allocate()
        algo1.write_tofile('Ex1_Output/out.csv')


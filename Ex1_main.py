import json
import csv
from Buildings import Buildings
from Elevator import *
from Calls import Calls
from ElevatorAlgo import ElevatorAlgo

algo1 = ElevatorAlgo('Ex1_Buildings/B4.json', 'Ex1_Calls/Calls_c.csv', 'out.csv')
algo1.allocate()
algo1.write_tofile('Ex1_Output\Ex1_Calls_case_1_b.csv')

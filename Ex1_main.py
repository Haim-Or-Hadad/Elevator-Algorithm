import json
import csv
import subprocess
import sys

from Buildings import Buildings
from Elevator import *
from Calls import Calls
from ElevatorAlgo import ElevatorAlgo

algo1 = ElevatorAlgo(sys.argv[1], sys.argv[2], sys.argv[3])
algo1.allocate()
algo1.write_tofile(sys.argv[3])

subprocess.Popen(["powershell.exe",
                  "java -jar Ex1_checker_V1.2_obf.jar 315804583,319147419 " + sys.argv[1] + " " + sys.argv[3] + " out.log"])

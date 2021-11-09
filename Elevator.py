import json
from Buildings import Buildings


class Elevator:

    def __init__(self, list, i):
        self._id = list[i]['_id']
        self._speed = list[i]['_speed']
        self._minFloor = list[i]['_minFloor']
        self._maxFloor = list[i]['_maxFloor']
        self._closeTime = list[i]['_closeTime']
        self._openTime = list[i]['_openTime']
        self._startTime = list[i]['_startTime']
        self._currfloor = list[i]['_minFloor']
        self._nextfloor = list[i]['_minFloor']

    def printelev(self):  # Print the elevator details
        print("id")
        print(self._id)
        print(self._speed)
        print(self._minFloor)
        print(self._maxFloor)
        print(self._closeTime)
        print(self._openTime)
        print(self._currfloor)
        print(self._nextfloor)
        return "--------------"

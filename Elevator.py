import json
import queue

from Buildings import Buildings


class Elevator:

    def __init__(self, list: list, i: int):
        self._id = list[i]['_id']
        self._speed = float(list[i]['_speed'])
        self._minFloor = int(list[i]['_minFloor'])
        self._maxFloor = int(list[i]['_maxFloor'])
        self._closeTime = float(list[i]['_closeTime'])
        self._openTime = float(list[i]['_openTime'])
        self._startTime = float(list[i]['_startTime'])
        self._stopTime = float(list[i]['_stopTime'])
        self.currfloor = 0
        self.status = 0
        self.dest = []


    def getMinFloor(self):
        return int(self._minFloor)

    def getMaxFloor(self):
        return int(self._maxFloor)

    def __str__(self):
        return f"Elevator: _id:{self._id} , _speed: {self._speed} , _minFloor:{self._minFloor} , _maxFloor:{self._maxFloor} , _closeTime:{self._closeTime} , _openTime:{self._openTime} , _startTime:{self._startTime} \n"

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return self._speed >= other._speed

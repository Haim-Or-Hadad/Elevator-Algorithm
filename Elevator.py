import json
from Buildings import Buildings


class Elevator:

    def __init__(self, list: list, i: int):
        self._id = list[i]['_id']
        self._speed = list[i]['_speed']
        self._minFloor = list[i]['_minFloor']
        self._maxFloor = list[i]['_maxFloor']
        self._closeTime = list[i]['_closeTime']
        self._openTime = list[i]['_openTime']
        self._startTime = list[i]['_startTime']
        self._currfloor = list[i]['_minFloor']
        self.numberofcalls = 0;

    def __str__(self):
        return f"Elevator: _id:{self._id} , _speed: {self._speed} , _minFloor:{self._minFloor} , _maxFloor:{self._maxFloor} , _closeTime:{self._closeTime} , _openTime:{self._openTime} , _startTime:{self._startTime} \n"

    def __repr__(self):
        return  str(self)

    def __lt__(self, other):
        return self._speed >= other._speed

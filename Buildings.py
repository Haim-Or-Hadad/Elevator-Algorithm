import json
import csv


class Buildings:

    def __init__(self, _minFloor, _maxFloor, _elevators):
        self._minFloor = _minFloor
        self._maxFloor = _maxFloor
        self._elevators = _elevators

    def from_json(Json_string):
        with open(Json_string) as myjsonfile:
            Building_Dict = json.load(myjsonfile)
        return Building_Dict





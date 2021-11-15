import json
import csv


class Buildings:

    def __init__(self, _minFloor, _maxFloor, _elevators):
        self._minFloor = _minFloor
        self._maxFloor = _maxFloor
        self._elevators = _elevators

    def from_json(Json_String):
        with open(Json_String) as myjsonfile:
            myjsonfile = open(Json_String)
            # jasondata = myjsonfile.read()
            Building_Dict = json.load(myjsonfile)
        return Building_Dict

    def __repr__(self):
        return f'<Buildings {self._minFloor}>'




# # with open('Ex1_Buildings/B1.json') as f:
# b1 = Buildings.from_json('Ex1_Buildings/B2.json')
# jasondata=f.read()
# b1 =json.loads(jasondata)
# print(str(b1['_minFloor']))
# print(str(b1['_maxFloor']))
# print(str(b1['_elevators']))
# Elist = (b1['_elevators'])
# Elev = Elist[1]['_id'], Elist[1]['_speed']
# print(len(Elev))
#print("Type:", type(Elist))

# self._speed = b1["_speed"]
# realbuild = Buildings.from_json(b1)
# print(type(b1))

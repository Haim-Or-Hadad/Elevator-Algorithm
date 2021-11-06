import json
import csv

class Buildings:
  def __init__(self, _minFloor, _maxFloor, _elevators):
    self._minFloor = _minFloor
    self._maxFloor = _maxFloor
    self._elevators = _elevators


  @classmethod
  def from_json(cls, Json_String):
      myjsonfile=open(Json_String)
      jasondata = myjsonfile.read()
      Building_Dict = json.loads(jasondata)
      return cls(**Building_Dict)

  def __repr__(self):
      return f'<Buildings { self._minFloor }>'

  def getElevator(self):
      return self._elevators

with open('Ex1_Buildings/B1.json') as f:
  b1=Buildings.from_json(f)
  #jasondata=myjsonfile.read()
  #b1 =json.loads(jasondata)
  print(str(b1['_minFloor']))
  print(str(b1['_maxFloor']))
  print(str(b1['_elevators']))
   # self._speed = b1["_speed"]
   # realbuild = Buildings.from_json(b1)
   # print(type(b1))


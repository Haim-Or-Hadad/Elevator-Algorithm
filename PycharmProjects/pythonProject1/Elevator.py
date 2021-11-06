import json
from Buildings import Buildings

class Elevator(Buildings):


 def __init__(self,  B1):
     B1 = Buildings.from_json(B1)
     list = B1['_elevators']
     self._id = list.get('_id')
     self._speed = list.get('_speed')
     self._minFloor = list.get('_minFloor')
     self._maxFloor = list.get('_maxFloor')
     self._closeTime = list.get('_closeTime')
     self._openTime = list.get('_openTime')
     self._startTime = list.get('_startTime')



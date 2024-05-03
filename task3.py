class Buiding:
   def __init__(self, numberOfFloors, buildingType):
      self.numberOfFloors = int(numberOfFloors)
      self.buildingType = str(buildingType)


   def __eq__(self, numberOfFloors, buildingType):
      return self.numberOfFloors == self.buildingType


buiding = Buiding(numberOfFloors=22, buildingType='22')
buiding1 = Buiding(numberOfFloors=33, buildingType=33)
print(buiding)
if buiding.__eq__(buiding.numberOfFloors, type(buiding.buildingType)):
   print('одинаковы',type(buiding.numberOfFloors), buiding.buildingType)
else:
   print('не одинаковы', type(buiding.buildingType))
   print(type(buiding.numberOfFloors), buiding.numberOfFloors, type(buiding.buildingType), buiding.buildingType)

if buiding.__eq__(buiding1.numberOfFloors, type(buiding1.buildingType)):
   print('одинаковы',type(buiding1.numberOfFloors), buiding1.buildingType)
else:
   print('не одинаковы', type(buiding1.buildingType))
   print(type(buiding1.numberOfFloors), buiding1.numberOfFloors, type(buiding1.buildingType), buiding1.buildingType)
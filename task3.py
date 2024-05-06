class Buiding:
   def __init__(self, numberOfFloors, buildingType):
      self.numberOfFloors = int(numberOfFloors)
      self.buildingType = str(buildingType)


   def __eq__(self, other):
       return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType



number_= Buiding(1, '1')
namber2_ = Buiding(2,'1')



if Buiding. __eq__(self= number_, other= namber2_):
    print('одинаковы')

else:
   print('не одинаковы ')



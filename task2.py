class House:
   def __init__(self):
      self.numberOfFloors = 0


   def setNewNumberOfFloors(floors):
      numberOfFloors = floors
      print(numberOfFloors)

   def setNewNumberOfFloors1(self, floors):
      numberOfFloors = floors
      print('Этаж', numberOfFloors)

house = House()
house.setNewNumberOfFloors()
house.setNewNumberOfFloors1(33)

class House:
   def __init__(self):
      self.numberOfFloors = 0


   def setNewNumberOfFloors(self, floors):
      self.numberOfFloors = floors
      print( 'Этаж ', self.numberOfFloors)
#      print('ЭТАЖ', numberOfFloors)
#      return numberOfFloors

house = House()
house.setNewNumberOfFloors(floors=34)
#print('Этаж=', house.setNewNumberOfFloors(floors=22))


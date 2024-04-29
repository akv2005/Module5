class House:
   numberOfFloors = 10

house = House()

while house.numberOfFloors > 1:
#    print('Текущий этаж равен', house.numberOfFloors)
    house.numberOfFloors -= 1
print('Текущий этаж равен', house.numberOfFloors)



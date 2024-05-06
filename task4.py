class Buiding:
   total = 0

   def __init__(self):
      Buiding.total += 1

i = 1

for i in range(40):
   building = Buiding()
   objs = building.total
   print(objs)




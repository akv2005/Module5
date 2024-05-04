class Buiding:
   total = 0

   def __init__(self):
      Buiding.total += 1

build = []
i = 1
while i < 40:
   buildind = Buiding()
   build.append(buildind.total)
#   print(build)
   i = buildind.total

print(build)
with open('input.txt') as f:
  lineList = f.readlines()

def fuelcost(y):
  if (((y / 3) - 2) <=  0):
    print "foo"
    return 0
  else:
    print "bar"
    return (((y / 3) - 2) + fuelcost((y / 3) - 2))

total = 0
for x in lineList:
  total = total + fuelcost(int(x.strip()))

print total

value = int(input("Enter a number: "))
steps = 0

while value > 1:
  steps = steps + 1
  if value%2 == 0: 
    value = value/2
  else:
    value = value*3 + 1
  print("   " + str(value))

print("steps: " +  str(steps))


#https://en.wikipedia.org/wiki/Collatz_conjecture


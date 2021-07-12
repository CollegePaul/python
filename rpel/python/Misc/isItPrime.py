#is it a number prime
import math
num = int(input("Enter a number: "))
prime = True
print (num)


fact = 2
while fact < math.sqrt(num):
  if(num%fact == 0):
    print("Divisiable by: " + str(fact))
    print("Not a prime")
    prime = False
    break
  fact = fact + 1

if(prime == True):
  print("Number is prime")
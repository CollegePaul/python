#factorial function version 2
#this version checks for negative and fractional
def factorial(n):
  if n<0:
    print("Please enter a positive number")
    return
  if n.is_integer() == False:
    print ("Please enter a whole number")
    return
  total = 1
  for i in range (1,n+1):
    total = total * i
  print(total)


factorial(4.6)

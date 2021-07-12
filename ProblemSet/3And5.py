#find the sum of multiples of 3 and 5 below a given value

max  = 100
total = 0 

for n in range(1,max):
  if(n%3 == 0 or n%5==0):
    total+=int(n)
    print(n)

print (total)

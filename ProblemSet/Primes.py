#Find prime numbers below 200
upper = 200
calc = 0

for num in range(2, upper + 1):
       for i in range(2, num):
          calc = calc + 1
          if (num % i) == 0:
               break
       else:
           print(num)


print("Calculations: " + str(calc))
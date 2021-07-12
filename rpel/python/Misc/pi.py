terms =1000000
sign = False
total = 1
term = 3

for i in range(terms):
  if sign == True:
    total = total + (1/term)
  else:
    total = total - (1/term)
  term = term + 2
  sign = not(sign)


print (total*4)


#requires 5 billion for 10 dp
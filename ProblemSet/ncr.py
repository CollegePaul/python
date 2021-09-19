#factorial function version 1
def fact(n):
  total = 1
  for i in range (1,n+1):
    total = total * i
  return total

#the c choose r combinational formula
def ncr(n,r):
  return int (fact(n) / (fact(r)*fact(n-r)))

#this function performs a binomial expansion of (a + b)^p
def binomial(p):
  for n in range(0,p+1):
    print(str(ncr(p,n)) + "a" + str(p-n) + "b" + str(n))


binomial(2)


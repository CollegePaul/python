#area of a square lambda
area = lambda s : s * s
print(area(6)) #36

def myfunc(n):
  return lambda a : a * n

triple = myfunc(3)
print(triple(5)) #15

double = myfunc(2)
print(double(5)) #19
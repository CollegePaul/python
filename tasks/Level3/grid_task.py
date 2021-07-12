#1d data used for 2d game world

#  0 0 0 0
#  0 0 0 0
#  0 1 0 0
#  0 0 0 0 

# 0000000001000000

x = 1  #2 across
y = 2  #2 down

#  2dData[x,y]
#what element is this in 1d

# 1ddata[?]
point = x + y*4
print(point)

#if char is at point 7 what is this in 2d x,y ?
point = 7
x = point%4
y = int(point/4)
print(str(x) + "," + str(y))

#design function that will accept an x,y, and gridWidth, and will return a 1d int.
#design a function that will accept a int, and gridwidth.

#eg

# def 2Dto1D(x,y,gridWidth):
#    your code here
#    --------------
#    return point

#then call your function and test
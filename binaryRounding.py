#Round to nearest, ties to even
from binaryAdd import BinaryAdd

num = "0.11011"
points = 2   #how many points affer the radax to round too

#is it  0.11 or does it round up to 1.00 ?

#0.11             mid              #1.00
#|                |                 |
#____________________________________

#find the low and upper limmit
lower = num[:(points+2)]   # +2 to account for msb and radax
print(lower)  #0.11

start = num[:(points+2)]   #0.11
add = "0."
for x in range(0,points):
    if x == points-1:
        add += "1"
    else:
        add += "0"
print(add)

print(BinaryAdd.add("h","i"))
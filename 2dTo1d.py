#convert a 2d list to 1d.

map = [
    [1,1,1,1,1,1],
    [1,0,0,0,2,1],
    [1,0,0,0,0,1],
    [1,3,0,0,0,1],
    [1,1,1,1,1,1]
]

def twoD_to_oneD(x,y):
    n = y*6 + x
    print(n)
    return(n)

def oneD_to_twoD(n):
    x = n%6
    y = n//6
    print("(",x,",",y,")")
   
def map_to_1d(map2d):
    map1d = []
    for row in map:
        map1d += row
    print(map1d)

def print_map2d(map2D):
    for row in map2D:
        print(row)

def next_to_fruit(x,y, map2D):
    fruit = False
    if map2D[y][x+1]==2:
        fruit = True
    elif map2D[y][x-1]==2:
        fruit = True 
    elif map2D[y+1][x]==2:
        fruit = True 
    elif map2D[y-1][x]==2:
        fruit = True
    else:
        fruit = False
    print(fruit)
    return fruit

def getXY():
    pass  #for you to do

next_to_fruit(3,3,map)


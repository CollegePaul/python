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
    return n

def oneD_to_twoD(n):
    y = n//6
    x = n%6 #remainder
    print("(",x,",",y,")")
    return n

def map_to_1d(map2d):
    map1d  = []
    for row in map2d:
        map1d += row
    print(map1d)
    return map1d

def print_map2d(map2d):
    for row in map2d:
        print(row)

def next_to(x,y, map2d, object):
    chest = False
    if map2d[y][x+1] == object:
       chest = True
    if map2d[y][x-1] == object:
       chest = True
    if map2d[y-1][x] == object:
       chest = True
    if map2d[y+1][x] == object:
       chest = True
    print(chest)
    return chest


next_to(1,2,map,3)


def getXY(x,y,map2d):
    return map2d[y][x]


print(getXY(1,3,map))

# test



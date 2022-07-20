state = [2,3,True]


def setPoints(points):
    point = points[0]
    value = points[1]

    print("setting point " + str(point))

    if value:
        print("Print setting Left")
    else:
        print("Setting Right")


if state[0] == 2: #this pico
    setPoints([state[1],state[2]])


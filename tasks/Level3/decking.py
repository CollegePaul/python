#Decking calculator
DECKING_COST = 8.99

while True:
    length = input("Please enter length: ")
    width = input("Please enter width: ")

    try:
        length = float(length)
        width = float(width)
        if length > 0 and width > 0:
            break
        else:
            print("Please enter a postive lenght and width")
    except:
        print("Please enter a valid number.")

area = length * width
cost = DECKING_COST * area
cost = round(cost,2)

print("Total Cost: £" + str(cost))


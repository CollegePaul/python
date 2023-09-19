
#validate an int 0-100
def validateInt():
    #check an int is entered 0 - 100
    while True:
        num = input("Enter number 0-100: ")
        try:
            num = int(num)
            if num >= 0 and num <= 100:
                break
            else:
                print("Print must be 1-100")
        except:
            print("Please input a whole number")
    
    return num

def validateSize():
    while True:
        s = input("Enter size (s,m,l): ")
        if s == "s" or s == "m" or s == "l":
            break
        else:
            print("Must be (s,m,l) please do it right!")
    return s

def output(age, size):
    cost = 0
    if size == "s":
        cost = 1.25
    elif size == "m":
        cost = 2.53
    elif size == "l":
        cost = 4.03
    else:
        print("Error: size is not valid")
    
    print("Order for " + str(age) + "yr old costs £" + str(cost))
    
    
#------------------------------ main --------------
for i in range(0,5):
    age = validateInt()
    size = validateSize()   # "s","m","l"
    output(age,size) #pass the arguments



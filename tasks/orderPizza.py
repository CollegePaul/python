
"""
The pizza function will process the order of 1 pizza.
Validating size and number of toppings. The function
will return a list consisting of a string containing the order, and 
a cost for the pizza.
"""
def orderPizza():
    #initialise varibles that will be used for the return value
    cost = 0.0  #float
    order = ""  #string

    #validate and process the pizza size
    while True:
        size = input("What size pizza would you like (s/m/l)? ")
        if size == "s":
            cost +=3.25
            order = "Small pizza"
            break
        elif size == "m":
            cost += 5.50
            order = "Medium pizza"
            break
        elif size == "l":
            cost += 7.15
            order = "Large pizza"
            break
        else:
            print("Please enter a vailid size s/m/l")

    #validate and process the toppings 0-4
    while True:
        topping_count = input("How many extra toppings would you like (0 - 4)? ")
        try:
            topping_count = int(topping_count)
            if topping_count >= 0 and topping_count <=4:
                break
            else:
                print("Please enter a valid amount 0 to 4")
        except:
            print("Please enter a valid number (0-4)")

    #topping is valid, calulate the price and add to reciept
    if topping_count == 0:
        order +=  " with no toppings totaling £" + str(cost)
    elif topping_count == 1:
        cost += 0.75
        order +=  " with 1 extra topping totaling £" + str(cost)
    elif topping_count == 2:
        cost += 1.35
        order +=  " with 2 extra toppings totaling £" + str(cost)
    elif topping_count == 3:
        cost += 2.00
        order +=  " with 3 extra toppings totaling £" + str(cost)
    elif topping_count == 4:
        cost += 2.50
        order +=  " with 4 extra toppings totaling £" + str(cost)
    
    #output the order as feedback to the customer
    print(order)

    #return the order as a string, and cost as float
    #value is rounded to 2dp to mitigate any floating point errors
    return [order, round(cost,2)]




  

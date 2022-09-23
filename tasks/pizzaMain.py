"""
The order pizza function will process 1 order and return a description of the 
order and a price.
This has been kept seperate to test sepeatley, and to show that the main concept of the 
main program and the order of pizzas is a repeted function.
"""
from orderPizza import orderPizza

total_cost = 0   #float - the total order value
reciept = []     #a list of strings conatining order descriptions

#get customer details before pizza ordering
name = input("Please enter your name: ") 
reciept.append("Customer Name: " + name)

address = input("Please enter your adress: ")
reciept.append("Customer Address: " + address)

phone_number = input("Please enter phone number: ")  #this will be left as a string
reciept.append("Customer Phone Number: " + phone_number)

#how many pizzas would the customer like to order
while True:
    pizza_quantity = input("How many pizzas would you like to order (1 - 6)? ")
    try:
        pizza_quantity = int(pizza_quantity)
        if pizza_quantity >=1 and pizza_quantity <=6:
            break
        else:
            print("The number of pizzas should be 1 to 6")
    except:
        print("Please enter a vailid amount of pizza's 1 - 6")

#valid number of pizza is ordered. Loop over the quanity adding each order to the recipt and total_cost
for orders in range(0, pizza_quantity):
    #run the order function. returning the recipt text and the cost in a list
    print("\n" + "Pizza number " + str(orders+1))  #user feedback so they can see the pizza number they are ordering.
                                                   #1 is added as the index is 0, but for the user the pizza is 1
    order = orderPizza()
    reciept.append(order[0])    #List Element 0 is the recipt text, add this to the reciept
    total_cost += order[1]      #List Element 1 is the cost of the pizza, add this to the total_cost

#apply discount if total_cost is more than £20
if total_cost > 20.0:
    discount = round(total_cost * 0.1,2)        #discount value calulated for printing out
    total_cost -= discount                      #discount applied to total cost, with rounding as this represents money
    print("\nDiscount of £ " + str(discount))   #print value as user feedback
    reciept.append("Discount of 10% added: £" + str(discount))

#delivery, y or n, 
while True:
    delivery = input("would you like delivery (y/n)? ")
    if delivery == "y":
        print("\nDelivery added at a cost of £2.50")
        total_cost += 2.5
        reciept.append("Delivery: £2.50")
        break
    elif delivery == "n":
        print("\nNo delivery (collect only) selected")
        reciept.append("Delivery: none")
        break
    else:
        print("Delivery is y or n")

#add the order total to the recipt
print("\n------RECIEPT--------\n")
reciept.append("Order Total: £" + str(round(total_cost,2)))  #make sure the output is suitable for a monetry value

#print out the final recipt
for line in reciept:
    print(line)

print("\n")







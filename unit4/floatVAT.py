"""
        Input 5 floats. Add 20% VAT to each
        print out the 5 original floats, with the VAT in brackets
        eg.  26.54 is entered,   26.54(31.85) is printed
"""

values = [] #hold the inputted float values

#Inputs
for i in range(0,5):  #loop 5 times
    while True:
        value = input("Pleas input a number: ") #string
        try:
            value = float(value) #validate is a number
            values.append(value) #add to the list
            break
        except:
            print("Please enter a valid number") #handel error

#Process
for i in range(0,5): #loop over the list
    value = values[i] #get a value from the list
    value_VAT = value * 1.2 #120%   100%  + 20%
    value_VAT = round(value_VAT,2) #round to 2dp
    
    #output
    print(str(value) + "(" + str(value_VAT) + ")")
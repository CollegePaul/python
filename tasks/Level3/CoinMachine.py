"""
Car parking machine, charges 80p
Gives change if possible, message to say no change available otherwise
Accepts £2,£1,50p,20p,10p,5p,2p,1p
Customer shoud enter coins until they have paid enough
"""


coins = [2.00, 1.00, 0.50, 0.20, 0.10, 0.05, 0.01]
total_payment = 0

while total_payment < 0.80:
    
    #input 1 coin at a time
    while True:
        inserted = input("Input a coin: ")
        try:
            inserted = float(inserted)
            if inserted in coins:
                total_payment += inserted
                total_payment = round(total_payment,2)
                print("Total entered: " + str(total_payment))
                break
            else:
                print("Not a valid amount")
        except:
            print("Not a vaild amount")

#Now we should have the payment in the correct coins

#calculate the change
change = total_payment - 0.80
change = round(total_payment)





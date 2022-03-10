# ctrl-c to exit running program

import math


units = ["zero", "one", "two", "three", "four","five","six","seven","eight", "nine"]
tens = ["zero", "ten", "twenty", "thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
teens = ["ten","eleven", "twelve", "thirteen", "fourteen","fifteen","sixteen", "seventeen", "eighteen","nineteen"]

# while True:

    # while True:
    #     num = input("enter number (0 - 999): ")

    #     try:
    #         num = int(num)

    #         if num >= 0 and num <1000:
    #             break
    #         else:
    #             print("Number should be 0-999")

    #     except:
    #         print("Must be a vaild number 0-999")
           
for num in range(1,1000):

    if num<10:
        print(units[num])

    elif num<20:
        print(teens[num-10])

    elif num<100:
        t = math.floor(num/10)
        u = num - (t*10)
        if u > 0:
            print(tens[t] + " " + units [u])
        else:
            print(tens[t])

    elif num<1000:
        h = math.floor(num/100)  # 569  5.69 5
        t = math.floor((num - h*100)/10)
        u = num%10
        
        # h,t,u are all >0  print all digits
        if u > 0 and t > 0:
            print(units[h] + " hundred and " + tens[t] + " " + units [u])
        
        #if t = 0  and u = 0  print 100's     700 seven hundred 
        elif t==0 and u==0:
            print(units[h] + " hundred")
                
        #if t= 0 but u is not    706   seven hundred and six
        else:
            print(units[h] + " hundred and " + units [u])

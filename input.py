'''
Inputing information via the console.

in this example we will load in some numbers for addition

'''


#this will not work as expected
n1 = input("Enter a number: ")
n2 = input("Enter 2nd number: ")
answer = n1 + n2
print(answer)

#this will work as expected but if you enter a letter it will crash
# n1 = int(input("Enter a number: "))
# n2 = int(input("Enter 2nd number: "))
# answer = n1 + n2
# print(answer)

# this will work
# while True:
#     n1 = input("Enter a number: ")
#     n2 = input("Enter 2nd number: ")
#     try:
#         n1 = int(n1)
#         n2 = int(n2)
#         break
#     except:
#         print("you must enter a number")
 

#you could also write this in a reusable funtion to accept only numbers
# def getIntInput(message: str) -> int:
#     '''Takes a string message and validates integer output from user'''
#     while True:
#         i = input(message)
#         try:
#             i = int(i)
#             break
#         except:
#             print("must be a number")
    
#     return i


# n1 = getIntInput("number1:")
# n2 = getIntInput("number2:")
# answer = n1+n2
# print(answer)



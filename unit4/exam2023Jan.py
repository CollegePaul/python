#2023 Exam on passwords

#print( ord("0") )   #97     #65   #48
#print( ord("9") )   #122    #90   #57

import os
 
# Clearing the Screen
os.system('cls')

#input
while True:
    password = input("Please enter a password to be rated (8 - 15 characters): ")

    if password == "": #presence check
        print("Please enter a password")
    elif len(password) <8 or len(password) > 15: #range check
        print("please enter a password having 8 - 15 characters")
    else:
        break #valid

#processing
points = 0

special_characters = ["!","%", "&", "*", "+", "="]



if len(password) >= 10:
    points += 20


lowerChrCounter = 0
upperChrCounter = 0
numberChrCounter = 0
specialChrCounter = 0

lowerDeducted = 0
upperDeducted = 0
numberDeducted = 0



#loop over the characters
for character in password:

    #lower case points
    if ord(character) >=97 and ord(character) <= 122:
        lowerChrCounter += 1
        points += 5

    #upper case points
    if ord(character) >=65 and ord(character) <=90:
        upperChrCounter += 1
        points += 5

    #numberic characters
    if ord(character) >=48 and ord(character) <=57:
        numberChrCounter += 1
        points += 10
        

    #special characters
    if character in special_characters:
        specialChrCounter = 1
        points += 10

passwordLength = len(password)
#negative scores
if lowerChrCounter == passwordLength:
    lowerDeducted = passwordLength * 3
    points -= lowerDeducted

if upperChrCounter == passwordLength:
    upperDeducted = passwordLength * 3
    points -= upperDeducted

if numberChrCounter == passwordLength:
    numberDeducted = passwordLength * 5
    points -= numberDeducted

#calculate rating
if points <=20:
    rating = "Very Low"
elif points < 40:
    rating = "Low"
elif points < 70:
    rating = "Medium"
elif points < 80:
    rating = "High"
else:
    rating = "Very High"

#output
print("\nScores for your password")
print("Your password: " + password)

print("Points breakdown:")
print("points for Lower case letter: " + str(lowerChrCounter * 5))
print("points for Upper case letter: " + str(upperChrCounter * 5))
print("points for Numbers: " + str(numberChrCounter * 10))
print("points for Special Characters " + str(specialChrCounter * 5))
print("")
print("Points dedcuctions:")
print("Point deducted for only Low case: " + str(lowerDeducted))
print("Point deducted for only Upper case: " + str(upperDeducted))
print("Point deducted for only Numbers: " + str(numberDeducted))
print("")
print("Points for password: " + str(points))
print("Rating for password:  " + rating)

 





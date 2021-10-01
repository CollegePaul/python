"""Reading in lines of a text file"""

lines = []  #list to store the lines of the file

#open and load the lines
with open('in.txt') as f:
    lines = f.readlines()

#print out the lines
for i in range(0, len(lines)):
    print(lines[i])              #there are \n characters
    print(lines[i].rstrip())     #remove \n characters

"""This example shows different for loop syntax, 
ans also how the data can be split by the comma (csv) 
this make a new list called game[] and it has 2 elements,
the game and the company"""
# for line in lines:
#     game = line.split(",")
#     print(game[1])
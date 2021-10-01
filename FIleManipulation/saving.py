"""
Saving data to a file, in this example we load in a file,
delete its contents and write out a list, the newline
character is needed, to seperate lins of the text file.
"""
names = ["mario", "luigi", "bowser", "toad"]

with open('characters.txt', 'a') as f:
    f.truncate(0) #this will erase the file
    for name in names:
        f.write(name + "\n") #A new line character terminates each line

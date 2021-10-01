"""Reading in lines of a text file, and adding numbers"""

lines = []
output = []
with open('in.txt') as f:
    lines = f.readlines()

count = 0
for line in lines:
    count +=1
    game = line.split(",")
    #The line below is for testing and prints the output in the console.
    #print(f'{count}:\t{game[0]}') 
    output.append(f'{count}:\t{game[0]}')  


with open('out.txt', 'a') as f:
    f.truncate(0) #this will erase the file
    for o in output:
        f.write(o + "\n") #A new line character terminates each line




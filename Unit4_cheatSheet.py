"""
Paul's Python cheet sheet V1
please send request for me to add on.
This content is what I think you will need for exam.
"""


#a basic input with a presence check
name = input("name: ")  #ask for name
while len(name) == 0:   #if nothing is entered ask again, untill it is
    name = input("name: ")

#validate a input is a number
while True:
    money = input("Amount: ")
    try:
        money = float(money)
        break
    except: 
        print("Please input a valid amount")

#a for loop   this will print 0,1,2,3,4
for i in range(0,5):
    print(i)

# a list 
colours = ["red","blue", "green"]

#loop over a list
for c in colours:
    print(c)
#this prints  "red","blue","green"

#sorting a list
print(sorted(colours))
print(sorted(colours, reverse=True))


#a Dictionary
sizes = { "small": 1.4,
          "medium": 2.5,
          "large": 3.2}

#print a value for a given key
print(sizes["medium"])

#print the keys
for key in sizes:
    print(key)

#print the values 
for key in sizes:
    print(sizes[key])

#check if a key is in the list
if "large" in sizes:
    print("large pizza found")

#rounding
value = 3.14159245
print(round(value,2)) #3.14

value = 1.3
print(round(value,2))  #1.3
print(f"{value:.2f}") #1.30  aways shows 2dp (f string)

#load
data = [] #empty list
with open("test.txt","r") as f:  #open file in read mode
    lines = f.readlines()         #read the lines into list
    for line in lines:             #loop over the lines
        data.append(line)            #add the line to the data

print(data)
#['testing upload, now making a change\n', 'new line of stuff']

#remove a \n  (it is best to do this in the step above   line.strip())
cleandata = []
for line in data:
    cleandata.append( line.rstrip())

print(cleandata)
#['testing upload, now making a change', 'new line of stuff']


#save
with open("saved.txt" , "a") as f:
    f.truncate(0)                       #delete previous content
    for line in cleandata:              #loop over your data
        f.write(line + "\n")            #add the \n for newlines


#I don't think you will need csv - but just incase
#csvs
csv = "one, two, three, four, five"
seperate_list = csv.split(",")  #split() - with no "," will split spaces
print(seperate_list)
#['one', ' two', ' three', ' four', ' five']

#load csv
""" Example csv data
small, 2
meduim, 4
large, 7

"""
import csv     #import the csv module
loaded_data = []
with open('stuff.csv', 'r') as f:
    data = csv.reader(f)   #use csv reader
    for row in data:
        loaded_data.append(row)
        print(row)
    #this will output a list [] for each row
    #['small', ' 2']
    #['meduim', ' 4']
    #['large', ' 7']

    print(loaded_data) #[['small', ' 2'], ['meduim', ' 4'], ['large', ' 7']]
    print(loaded_data[1]) #['meduim', ' 4']
    print(loaded_data[1][1]) #4







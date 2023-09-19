#load the data
data = []
header = []

with open("data.txt", "r") as f:
    lines = f.readlines()
    header = lines[0] # save the header row

    for i in range(1,len(lines)): #loop over the data getting 1 line at a time

        #get 1 line and strip and split it.
        newLine = lines[i].rstrip() #remove the newline character

        # I need to split the string 
        # "UBG Mobile,Mobile,$4 422 220,851780"
        # so it will be    ["UBG Mobile","Mobile","$4 422 220","851780"]
        newLine = newLine.split(",")

        data.append(newLine)

# what we need to do is now sort the data by the viewers
def get_views(e):
    return e[3]

data.sort(key=get_views, reverse=True)

with open("data_sorted_by_views.txt","a") as f:
    f.truncate(0)  #clear all contents of the file

    f.write(header)# put the header back

    for line in data: #loop over all the lines
        #the data will be a list
        #["UBG Mobile","Mobile","$4 422 220","851780"]
        #we need to print out each word in the list with the newline

        newline = line[0] + "," + line[1] + "," + line[2] + "," + line[3] + "\n"
        f.write(newline)
    



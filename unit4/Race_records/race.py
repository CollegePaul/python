#World records solution from exam question from May 2018

#global variabls
gender = None
lanes = None
lane_times = []

mens_records = {
    "World Record": 9.58,
    "European Record Time": 9.86,
    "British Record Time": 9.87
}

womens_records = {
    "World Record": 10.49,
    "European Record Time": 10.73,
    "British Record Time": 10.99
}


#Validate if Race is Male or Female
valid = False
while valid == False:
    gender = input("Race (m - male ,f - female)")
    if gender == "m" or gender == "f":
        valid = True
    else:
        print("Please enter m or f")

#validate number of lanes in the race

valid = False
while valid == False:

    lanes = input("How many lanes (4 -8)") #string value
    try:
        lanes = int(lanes)  #conver to whole number
        if lanes >= 4 and lanes <= 8:   #validate range
            valid = True
        else:
            print("Please enter a number beteeen 4 and 8")
    except:
        print("Please enter a vaild number")

#entering the data for the race
print("You will now be asked to enter the racce times in seconds for each lane.")

#loop over the number of lanes
for i in range(1, lanes + 1): 

    while True:
        lane_time = input("Enter time for lane " + str(i) + ": ")
        try:
            lane_time = float(lane_time)
            if lane_time >0:
                break
            else:
                print("please enter a positive time")
        except:
            print("please enter a valid lane time")

    #add the lane time to the array
    lane_times.append(lane_time)

#sort the data
lane_times.sort()

#print the information and set the record to use
if gender == "m":
    records = mens_records
else:
    records = womens_records


#loop over and print the record times in order, with 2dp formatting
print("The results are as follows - odered fastest to slowest")
for i in range(0, len(lane_times)):
    print(f'{lane_times[i]:.2f}')


#check if a record has been broken and add it to an output string
#it is only neccesery to check the fastest, as this will be the new record.  
record_string = ""   
for key in records:
    if lane_times[0] < records[key]:
        record_string += ", " + key

#output if and whichrecords have been broken
if record_string == "":
    print("No Records have been broken")
else:
    print("The following records have been broken:")
    print("New Record with a time of " + f'{lane_times[0]:.2f}'+ record_string)

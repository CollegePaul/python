import csv

#take a look at the 2 files sheet1 and sheet 2 before running!

data = []  #to store the data

#opening the file and reading it
with open('sheet1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            data.append([row[0], row[1], row[2]])  #Headings row
            line_count += 1
        else:
            total = (
                int(row[0]) + int(row[1]))  #loop over the rows get the totals
            data.append([row[0], row[1],
                         total])  #save the information in an array
            line_count += 1

#opening the file to write the data
with open('sheet2.csv', mode='w') as myFile:
    myFile_writer = csv.writer(myFile, delimiter=',', lineterminator='\n')
    for row in range(len(data)):
        myFile_writer.writerow(data[row])
        pass

print("Completed")                                                           

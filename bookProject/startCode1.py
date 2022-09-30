import csv #the CSV library

data = []  #we load our books into here,and the we can loop over them
output_data = []

#The list of all the book subject key words.
subject_list = ["Fiction", "fiction","Fantasy", "Drama", "Biography","Humor","Handbooks","science","Art","Biology","Economics", "Poetry","Philosophy","Political","English","French","drama","History","Bible","Classical","Mythology","Socialism","African"]
     
#load in the book, add the data to the data list
with open("books.csv", 'r', encoding='utf-8') as f:
    bookdata = csv.reader(f)
    for row in bookdata: #1 row at a time
        data.append(row) #add the data to the data list

for book in range (1,11):

    for subject in subject_list: #loop over the subjects and see if the book has that subject
        if subject in data[book][2]: #this is the book subject. check if 1 word is in the list
            # print(book)
            # print(subject)
            # print(data[book][3])  #title
            # print(data[book][11]) #Author
            # print(data[book][8])  #url
            # print(data[book][16]) #year

            #make a row of data
            row = [subject, data[book][3], data[book][11],data[book][8], data[book][16]]
            print(row)
            output_data.append(row)
            break
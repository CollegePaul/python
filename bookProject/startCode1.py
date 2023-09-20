import csv 

data = [] 
output_data = []


subject_list = ["Fiction", "fiction","Fantasy", "Drama", "Biography","Humor","Handbooks","science","Art","Biology","Economics", "Poetry","Philosophy","Political","English","French","drama","History","Bible","Classical","Mythology","Socialism","African"]
     

with open("books.csv", 'r', encoding='utf-8') as f:
    bookdata = csv.reader(f)
    for row in bookdata: 
        data.append(row) 

for book in range (1,11):

    for subject in subject_list: 
        if subject in data[book][2]: 
            # print(book)
            # print(subject)
            # print(data[book][3])  #title
            
           
            row = [subject, data[book][3], data[book][11]]
            print(row)
            output_data.append(row)
            break
    
with open('save.csv', 'w', newline='') as f:
    f.truncate(0)
    writer  = csv.writer(f)
    writer.writerow(["Code","Title","Author","URL","Year"])
    for row in output_data:
        writer.writerow(row)


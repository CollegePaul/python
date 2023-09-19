#Exam Jan 2021 
#Teacher inputs student scores

#inputs --------------------------------

    #how many students
    #names
    #scores

#processing ----------------------------

    #sort by scores
    #assign a grade

#output ---------------------------------

    #print students, score, grade in decending score order
    #print list of distinction students
    #output all this data to a text file

names = ["mario", "Toad","yoshi","Daisy"]  #our output data

with open("output.txt", 'a') as f:
    f.truncate(0)  #delete the contents of file (optional) 
    for name in names:
        f.write(name + "\n")

        
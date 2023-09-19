num_students = input("How many students in the class? ")
# add vaidation and try except
num_students = int(num_students)

students = []


#this function validates an inputted score, with a custom caption
#the score is then returned as a percentage, rounded to 2dp
def input_score(caption):
    while True:
        score = input(caption)
        try:
            score = int(score)
            score = (score/40)  * 100
            score = round(score,2)
            return score
        except:
            print("Please enter a vaild score")

    

#---entering grades----
for s in range(0,num_students):
    
    name = input("Student Name: ")
    score_1 = input_score("Score 1: ")
    score_2 = input_score("Score 2: ")
    score_3 = input_score("Score 3: ")

    total = score_1 + score_2 + score_3
    average = total / 3
    average = round(average,2) 

    description = "Needs Improvement"
    if average >= 70:
        description = "Exceeded"
    elif average >= 40:
        description = "On Target"

    #add data into student list
    students.append([name, score_1, score_2, score_3, average, description])

#----sorting the data

def sort_data(e):
    return e[4]

students.sort(key=sort_data,reverse=True)


#-----outputting the data
print("\n")
print("All score are percentages")
print("Name , Score 1, Score 2, Score 3, Average, Grade Description")

for student in students:
    print(student[0],student[1],student[2],student[3],student[4],student[5])

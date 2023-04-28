
# I will need to add type checking and other validation to this
people = int(input("How many people are being surveyed"))

#a list to store all the responses given
responses = []


#main loop
for i in range(0,people):
    #string data - will have to add presence checks
    name = input("Name: ")
    game = input("Favourite game")
    character = input("Character: ")

    #number data - to add validation
    hours = int(input("How many hours a week do you play: "))

    #add the data to the responses as a list
    responses.append([name,game,character,hours])


def sort_by_hours(data):
    return data[3]

responses.sort(key=sort_by_hours,reverse=True)



print(responses)


#output all the data - not very well formatted but functional
with open("output.txt", 'a') as f:
    f.truncate(0)
    f.writelines("Survay of peoples game playing by sorted by hours \n\n")
    for i in range(0, people):
        f.writelines(str(responses[i][0]) + ":\n")
        f.writelines("  Game:" + responses[i][1] + "\n")
        f.writelines("  Character:" + responses[i][2] + "\n")
        f.writelines("  Hours:" + str(responses[i][3]) + "\n\n")
    

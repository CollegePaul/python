# Make a programme that will take a word input by the user

while True:

    word = input("Word: ")

    if len(word)<1:
        print("Please enter a word")
        continue
    elif len(word)<6:
        print(str(len(word))+"_"+word)
    else:
        print(word + "_" + str(len(word)))
colours = ["red", "blue", "pink"]

while True:
    colour = input("Enter a colour: ")
    if colour in colours:
        break
    else:
        print("colour not found")

print("good choice")
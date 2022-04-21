import random

rd = random.randint(1,9)
c=1
guess = "exit"


while guess != rd and guess != "exit":
    guess = int( input("Enter a guess between 1 to 9"))

    if guess > rd:
        print("Too High")

    if guess == rd:
        print("Right")
        print("You only took ", c , " tries!")
    else:
        print("Too Low")

    c += 1
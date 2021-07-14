'''Rock Paper Sissors'''
import random

hand = ['Paper','Rock', 'Sissors']
h = ['p','r','s']

while True:
    x = random.randint(0, 2)
  
    guess = input("R,P,S ? ")
    
    index = h.index(guess)

    print("You: " + hand[index] + "    Me: " + hand[x])
    
    if index + 1 == x or (index ==2 and x==0):
        print("you win")
    elif index == x:
        print("Its a draw")
    else:
        print("you lose")






# pig game console version
# 2 to 4 players, in turn role 6 sided dice, each time accumulate score untill you want to add to total
# If you role a 1 lose all accumulated score this turn, pass die
# First person to reach 100 wins

import random

def roll():
    return random.randint(1,6)

def check_win(player):
    global scores
    if scores[player] >= 100:
        print("player", player,"wins the game")
        exit()
        #sys.exit()

players = int(input("How many players? "))
print("Number of players is",players)

scores = [0] * players

while True:
    #game round
    for player in range(0,players):
        print("\n------ PLAYER", player, "-----------\n")
        print("Your current game score: ", scores[player])
        total = 0
        while True:
            
            print("Total this round: ", total)
            dice_roll = roll()
            print("You have rolled ", dice_roll)
            if dice_roll ==1:
                print("Bad luck, you got a 1, so that means no score this round")
                break
                

            end = input("Do you want to end your turn and add to your score (y/n)")
            if end == "y":
                scores[player] += dice_roll + total
                print("Your game score is now: " , scores[player])
                check_win(player)
                break
            elif end =="n":
                total = total + dice_roll



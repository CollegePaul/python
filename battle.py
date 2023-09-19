import random
import os
from colour_print import PrintCol as col
os.system('cls')


def d6_roll():
    return random.randint(1, 6)


#1 Hit Roll
def hit(BS):
    hit_roll = d6_roll()
    if hit_roll >= BS:
        print(f'{col.green}ROLL {hit_roll} >= {BS} (HIT)')
        wound(4,5)
    else:
        print(f'{col.red}HIT ROLL {hit_roll} < {BS} (MISS)')

#2 Wound Roll
def wound(S, T): #attacker Strength, Target Toughness
    required = 0
    if S >= T*2:
        required = 2
    elif S > T:
        required = 3
    elif S == T:
        required = 4
    elif S == T/2:
        required = 6
    else:
        required = 5

    w_roll = d6_roll()
    if w_roll == 1: # 1 is always fail
        print(f'{col.red}WOUND ROLL {w_roll} (FAIL))')
    elif w_roll == 6: # 6 is always hit
        print(f'{col.green}HIT ROLL {w_roll} (HIT)')
    else:
        #is the wound roll higher or equal to required
        if w_roll >= required:
            print(f'{col.green}HIT ROLL {w_roll} (HIT)')
        else:
            print(f'{col.red}WOUND ROLL {w_roll} (FAIL))')


for rolls in range(0,5):
    print(f'{col.white}Model {rolls} ---------------')
    hit(3)


#put the terminal colour back to white
print(f'{col.white}')
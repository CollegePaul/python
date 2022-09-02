from random import randint


board =[
    [0,0,0],
    [0,0,0],
    [0,0,0],
]



def checkWin():
    
    #do you have a row
    for row in board:
        total=0
        for col in row:
            total += col
        if total == 3:
            return 1
        if total == 15:
            return 2

    for col in range(0,3):
        for row in range(0,3):
            total = board[row][col] + board[1][col] + board[2][col]
        if total == 3:
            return 1
        if total == 15:
            return 2

    return -1

playing = True
current_player = 1 #0: human  1: Computer

def draw_game():
    for row in board:
        print(row)
    print("\n")




while playing:
    draw_game()

    if current_player == 1:
        #human
        x= int(input("Column(1,2,3): "))
        y= int(input("Row(1,2,3): "))
        board[y-1][x-1] = 1
        current_player = 5
    else:
        moved = False
        while not moved:
            x = randint(0,2)
            y = randint(0,2)
            if(board[y][x]==0):
                board[y][x]=5
                moved= True
                current_player = 1
                print("Player 2 has moved")
            
    
    winner = checkWin()
    if winner >0:
        print("Player " + str(winner) + " Won")
        playing = False
        draw_game()

  













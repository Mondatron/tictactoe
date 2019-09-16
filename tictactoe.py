# Udemy course milestone project
# TICTACTOE

#import modules
import random
import os


#functions
# funtion for players to select marker X or O
def MarkerSelect(p1,p2):
        marker1 = "a"
        marker2 = "a"
        
        while marker1 !="X" and marker1 !="O":
            marker1 = input (f"{p1}, please select your marker, X or O: ").upper()
        
        if marker1 == "X":
            marker2 = "O"
        else:
            marker2 = "X"
        
        return marker1, marker2

#function to select which player goes first
def GoFirst():
    # selecting which player goes first
    print("choosing the which player is to start..........................................\n...............................................")
    return random.randint(1,2)

#function which enables player to place his marker    
def PlayerMove(m,t,brd):
    m=0
    if t==1:
        player=player1_name
    else:
        player=player2_name
    
    while brd[m]=="X" or brd[m]=="O":
        m=0
        while m not in position:
            m=input(f"{player} please select a number between 1-9: ")
        m = int(m)
    
    if t==1:
        t=2
        return m, t
    else:
        t=1
        return m, t

# function which prints the tictactoe board
def print_board(brd):
    clear()
    print(f"   {brd[1]}   |   {brd[2]}   |   {brd[3]}   ")
    print("-------|-------|------")
    print(f"   {brd[4]}   |   {brd[5]}   |   {brd[6]}   ")
    print("-------|-------|------")
    print(f"   {brd[7]}   |   {brd[8]}   |   {brd[9]}   ")
    print("       |       |      ")

# clear screen function
def clear():
    os.system("clear") # clear unix or cls for windows

# function which checks if anyone has won yet 
def WhoWon(tc, brd):
    w=0
    if (brd[1]==brd[2]==brd[3]) or  (brd[1]==brd[4]==brd[7]) or (brd[1]==brd[5]==brd[9]):
        if brd[1]==player1_marker:
            w=1
        else:
            w=2
    if (brd[4]==brd[5]==brd[6]) or  (brd[3]==brd[5]==brd[7]) or (brd[2]==brd[5]==brd[8]):
        if brd[5]==player1_marker:
            w=1
        else:
            w=2
    if (brd[7]==brd[8]==brd[9]) or  (brd[3]==brd[6]==brd[9]):
        if brd[9]==player1_marker:
            w=1
        else:
            w=2      
    
    if tc==9 and w==0:
        w=3
   
    return w 


again = "Y" # the play variable "Y" yes any other string is no. Default is yes 
# introduction
print ("WELCOME TO TICTACTOE!\n")

#input player names
player1_name = input ("Player 1 please input your name: ")
print (f"\nHi {player1_name}\n")
player2_name = input ("Player 2 please enter your name: ")
print (f"\nHi {player2_name}\n")

# players to select marker
player1_marker, player2_marker = MarkerSelect(player1_name, player2_name)

# the program run loop
while again=="Y":

    #variables
    position=["1","2","3","4","5","6","7","8","9"]
    board=["X",1,2,3,4,5,6,7,8,9]
    winner=0 # who has won
    move=0 #where to place marker
    turn=0 #whose turn is it 1=player1 and 2=player2
    turn_count=0

    print (f"{player1_name} you are playing with {player1_marker}")
    print (f"{player2_name} you are playing with {player2_marker}")

    #which player goes first
    turn = GoFirst()

    if turn==1:
        print(f"{player1_name} to start....")
    else:
        print(f"{player2_name} to start.....")
    
    #print board

    input("Press enter")
    print_board(board)

    print("Lets start!!!!")
    #start the main game while loop

    while winner==0:
        move=0
        if turn==1:
            move, turn=PlayerMove(move,turn,board)
            board[move]=player1_marker
            print_board(board)
            turn_count = turn_count+1
        else:
            move, turn=PlayerMove(move,turn,board)
            board[move]=player2_marker
            print_board(board)
            turn_count = turn_count+1
                
        winner = WhoWon(turn_count, board)
   
    if winner==1:
        print(f"And the winner is {player1_name}")
    elif winner==2:
        print(f"And the winner is {player2_name}")
    elif winner==3:
        print("The END!! Its as draw!!")
    else:
        print("Uh....no idea!")
        
    again = input("Do you wish to play again? (Y/N)").upper() 
    
# again variable does not equal "Y" and the game exits
print("Good-Bye!!")
# TicTacToe game version 1.0
# Completion Date 19th July 2025
# Written by Ian Gaetano Monda
# Milestone Project 1 for "The Complete Python Bootcamp From Zero to Hero in Python" by Jose Portilla (Udemy)

# print the board on the screen function
def display_board(board):
	
	print("    " + " | " + "   " + " | ")
	print("  " + board[1] + "  |  " + board[2] + "  |  " + board[3])
	print("    " + " | " + "   " + " | ")
	print("-----" + "|" + "-----" + "|" + "-----")
	print("    " + " | " + "   " + " | ")
	print("  " + board[4] + "  |  " + board[5] + "  |  " + board[6])
	print("    " + " | " + "   " + " | ")
	print("-----" + "|" + "-----" + "|" + "-----")
	print("    " + " | " + "   " + " | ")
	print("  " + board[7] + "  |  " + board[8] + "  |  " + board[9])
	print("    " + " | " + "   " + " | ")
	print("\n")


# player to choose player X or O
def player_marker():

	marker=""
	
	#keep asking player 1 to choose

	while marker.upper()!= "X" and marker.upper()!= "O":
		marker = input("Player1, choose your marker, X or O: ")

		if marker.upper()!= "X" and marker.upper()!= "O":
			print("Invalid choice! Please try again.")

	player1 = marker.upper()
	
	if player1 == "X":
		player2 = "O"
	elif player1 == "O":
		player2 = "X"


	return (player1,player2)


# take player input and add to board
def player_move(playing,board_state):

	move="100"
	moved = False

	while moved ==  False:

		move = input(f"Player {playing}, Make your move indicating an availale space 1-9:")
		print(moved)

		if move not in board_state:
			print("Sorry that space is not available!")
		else:
			print("Cunning move! :o)")
			board_state[int(move)] = playing
			moved = True

		print(moved)			

	return board_state


# check if there is a winner
def winner_check(player, board_state):

	winner_ce=False

	if board_state[1]==board_state[2]==board_state[3] or board_state[4]==board_state[5]==board_state[6] or \
	board_state[7]==board_state[8]==board_state[9]:
		winner_ce = True
		print(f"Player {player} is the WINNER! Congratulations!")
	elif board_state[1]==board_state[4]==board_state[7] or board_state[2]==board_state[5]==board_state[8] or \
	board_state[3]==board_state[6]==board_state[9]:
		winner_ce = True
		print(f"Player {player} is the WINNER! Congratulations!")
	elif board_state[1]==board_state[5]==board_state[9] or board_state[3]==board_state[5]==board_state[7]:
		winner_ce = True
		print(f"Player {player} is the WINNER! Congratulations!")
	else:
		winner_ce = False
		print("Still no winner! Next Move!")

	return winner_ce


# game variable intialisation

board = ["-","1","2","3","4","5","6","7","8","9"]
winner_status = False
play_desire = True
turn = 1

print("!!!!!!!!!!!!!!!!!!!!!\n")
print("WELCOME TO TICTACTOE!\n")
print("!!!!!!!!!!!!!!!!!!!!!\n")

while play_desire:

	desire = input("Would you like to play? Y for yes or N for no: ")

	if desire =="Y" or desire=="y":
		print("\nGreat! Lets Play!")
		
		# ensure game variables are initialised
		board = ["-","1","2","3","4","5","6","7","8","9"]
		winner_status = False
		play_desire = True
		turn = 1

		# set up players
		player1_marker, player2_marker = player_marker()
		print(f"Player 1 is: {player1_marker}\n")
		print(f"Player 2 is: {player2_marker}\n")

		# display board
		display_board(board)

	elif desire == "N" or desire=="n":
		print("\nOkay! See you again soon!")
		play_desire = False
	else:
		print("Doh! Sorry but that was not a valid response!\n")
		winner_status=True		


	# run game and loop
	while winner_status==False and play_desire == True:

		#player makes move
		if turn%2==0 and turn<10:
			board = player_move(player2_marker, board)
			turn +=1
			print(" \n " *100 )
			display_board(board)
			winner_status = winner_check(player2_marker, board)	
		elif turn%2 !=0 and turn<10:
			board = player_move(player1_marker, board)
			turn +=1
			print(" \n " *100 )
			display_board(board)
			winner_status = winner_check(player1_marker, board)
		else:
			print("GAME OVER!! \n With NO WINNER this time!!! \n Better luck next time!")
			break




		





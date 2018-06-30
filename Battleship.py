from random import randint
board =[]
for x in range(0, 5):
	board.append(["O"] * 5)
print(board)

def print_board(board_in):
	for row in board_in:
		print(" ".join(row))

print_board

def random_row(board_in):
	rownum = randint(0, len(board_in) -1)
	return rownum

def random_col(board_in):
	colnum = randint(0, len(board_in[0]) -1)
	return colnum

ship_row = random_row(board)
ship_col = random_col(board)
#print(ship_row)
#print(ship_col)
turn = 0
for turn in range(4):
	print ("Turn:", turn + 1)

	guess_row = int(raw_input("Guess Row:  "))
	guess_col = int(raw_input("Guess Column:  "))


	if guess_row == ship_row and guess_col == ship_col:
		print("You sunk my battleship!")
	elif turn == 3:
		print("Game Over")
	elif guess_row not in range(5) or guess_col not in range(5):
		print("Thats not even in the ocean!")
	elif board[guess_row][guess_col] == "X":
		print("You already guessed that.")
	else:
		print("Missed")
		board[guess_row][guess_col] = "X"
		print_board(board)



board = [" " for i in range(10)]
def insert_letter(letter, position):
    board[position] = letter

def space_is_free(position):
    return board[position] == " "

def print_board():
    print(f"   |   |   ")
    print(f" {board[7]} | {board[8]} | {board[9] }")
    print(f"   |   |   ")
    print(f"-----------")
    print(f"   |   |   ")
    print(f" {board[4]} | {board[5]} | {board[6]}")
    print(f"   |   |   ")
    print(f"-----------")
    print(f"   |   |   ")
    print(f" {board[1]} | {board[2]} | {board[3]}")
    print(f"   |   |   ")

def is_winner(boa, lett):
    return (boa[7] == lett and boa[8] == lett and boa[9] == lett) or\
           (boa[4] == lett and boa[5] == lett and boa[6] == lett) or\
           (boa[1] == lett and boa[2] == lett and boa[3] == lett) or\
           (boa[1] == lett and boa[4] == lett and boa[7] == lett) or\
           (boa[2] == lett and boa[5] == lett and boa[8] == lett) or\
           (boa[3] == lett and boa[6] == lett and boa[9] == lett) or\
           (boa[1] == lett and boa[5] == lett and boa[9] == lett) or\
           (boa[3] == lett and boa[5] == lett and boa[7] == lett)

def is_board_full(board):
    if board.count(" ") > 1:
        return True
    else:
        return False

print("WELCOME TO TIC TAC TOE GAME! ")
print("Press 'q' to quit any time")
player_x = "active"
player_o = "not active"
print_board()
while True:
    if is_board_full(board) == False:
        print("It's a Tie! ")
        break

    if player_x == "active":
        if is_winner(board, "O") == True:
            print("O's wins")
            break
        try:
            user_x_move = input("Enter the position for X's : ")
            if user_x_move == "q":
                print("Thanks for playing! ")
                quit()
            if space_is_free(int(user_x_move)) == True:
                insert_letter("X", int(user_x_move))
                player_x = "not active"
                player_o = "active"
            else:
                print("Already occupied")
        except Exception:
            print("(Only enter digits between 1-9 !)")

    elif player_o == "active":
        if is_winner(board, "X") == True:
            print("X's wins")
            break
        try:
            user_o_move = input("Enter the position for O's : ")
            if user_o_move == "q":
                print("Thanks for playing! ")
                quit()
            if space_is_free(int(user_o_move)) == True:
                insert_letter("O", int(user_o_move))
                player_o = "not active"
                player_x = "active"
            else:
                print("Already occupied")
        except Exception:
            print("(Only enter digits between 1-9 !)")


    print_board()




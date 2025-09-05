

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

def player_move():
    pass

def comp_move():
    pass

def computer_algo(bord):
    return (bord[1] == "X" and bord[2] == "X")


def is_board_full(board):
    if board.count(" ") > 1:
        return True
    else:
        return False

print("Welcome to TIC TAC TOE GAME")
player = "active"
computer = "inactive"
while True:
    if is_board_full(board) == False:
        print("It's a tie")
        break
    if player == "active":
        if is_winner(board, "O") == True:
            print("O's (computer wins), Try next time")
            break
        try:
            player_x_move = int(input("Enter the position for 'X'(1-9): "))
        except Exception:
            print("Only Enter number between (1-9)")
        if space_is_free(player_x_move) == True:
            insert_letter("X", player_x_move)
            computer = "active"
            player = "inactive"
        else:
            print("space Occupied")

    elif computer == "active":
        if is_winner(board, "X") == True:
            print("X's wins, Good Job! ")
            break

















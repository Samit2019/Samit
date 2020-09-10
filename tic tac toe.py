board = [
    '-', '-', '-',
    '-', '-', '-',
    '-', '-', '-'
]
user_player = input("enter what you what to be (X) or (O): ").upper()
while user_player not in ["X", "O"]:
    user_player = input("enter what you what to be (X) or (O): ").upper()


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def handling_turn(user_player):
    print(f"{user_player} trun")
    while True:
        position = input("Enter the number from 1-9: ")
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Enter the number from 1-9: ")
        position = int(position) - 1
        if board[position] == "-":
            board[position] = user_player
            display_board()
            break


def checking_if_there_is_winner():
    if (board[0] == board[1] == board[2] == user_player) or (      # row 1
            board[3] == board[4] == board[5] == user_player) or (  # row 2
            board[6] == board[7] == board[8] == user_player) or (  # row 1
            board[0] == board[3] == board[6] == user_player) or (  # column 1
            board[1] == board[4] == board[7] == user_player) or (  # column 2
            board[2] == board[5] == board[8] == user_player) or (  # column 3
            board[0] == board[4] == board[8] == user_player) or (  # diagonal 1
            board[2] == board[4] == board[6] == user_player):      # diagonal2
        print(f"player {user_player} won")
        exit()


def flipping_turn():
    global user_player
    if user_player == "X":
        user_player = "O"
    elif user_player == "O":
        user_player = "X"


def play_game():
    display_board()
    for i in range(9):
        handling_turn(user_player)
        checking_if_there_is_winner()
        flipping_turn()
    print("Draw")


play_game()

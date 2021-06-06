grid = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

game_running = True
winner = None
cur_player = "X"


def display_grid():
    print("\n")
    print(grid[0] + " | " + grid[1] + " | " + grid[2] + "     1 | 2 | 3")
    print(grid[3] + " | " + grid[4] + " | " + grid[5] + "     4 | 5 | 6")
    print(grid[6] + " | " + grid[7] + " | " + grid[8] + "     7 | 8 | 9")
    print("\n")


def handle_turn(player):
    print(player + "'s Turn")
    pos = input("Choose a position from 1-9 : ")

    valid = False
    while not valid:

        while pos not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            pos = input("Choose a position from 1-9 : ")
        pos = int(pos) - 1

        if grid[pos] == "-":
            valid = True
        else:
            print("You can't go there. try again.")

    grid[pos] = player
    display_grid()


def flip_player():
    global cur_player
    if cur_player == "X":
        cur_player = "O"
    elif cur_player == "O":
        cur_player = "X"


def play_game():
    display_grid()

    while game_running:
        handle_turn(cur_player)
        check_if_game_over()
        flip_player()

    if winner == "X" or winner == "O":
        print(winner + " Won")
    elif winner is None:
        print("Tie")


def check_if_game_over():
    check_winner()
    check_tie()


def check_tie():
    global game_running
    if "-" not in grid:
        game_running = False
        return True
    else:
        return False


def check_winner():
    global winner

    row_winner = check_row()
    col_winner = check_col()
    diagonal_winner = check_diagonal()
    # Get the winner
    if row_winner:
        winner = row_winner
    elif col_winner:
        winner = col_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_row():
    global game_running

    row1 = grid[0] == grid[1] == grid[2] != "-"
    row2 = grid[3] == grid[4] == grid[5] != "-"
    row3 = grid[6] == grid[7] == grid[8] != "-"

    if row1 or row2 or row3:
        game_running = False
    if row1:
        return grid[0]
    elif row2:
        return grid[3]
    elif row3:
        return grid[6]
    else:
        return None


def check_col():
    global game_running

    col1 = grid[0] == grid[3] == grid[6] != "-"
    col2 = grid[1] == grid[4] == grid[7] != "-"
    col3 = grid[2] == grid[5] == grid[8] != "-"

    if col1 or col2 or col3:
        game_running = False
    if col1:
        return grid[0]
    elif col2:
        return grid[1]
    elif col3:
        return grid[2]
    else:
        return None


def check_diagonal():
    global game_running

    diagonal1 = grid[0] == grid[4] == grid[8] != "-"
    diagonal2 = grid[2] == grid[4] == grid[6] != "-"

    if diagonal1 or diagonal2:
        game_running = False
    if diagonal1:
        return grid[0]
    elif diagonal2:
        return grid[2]
    else:
        return None


play_game()

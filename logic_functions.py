from colorama import Fore, Back
from variables import players, ROWS, COLUMNS
from validation_functions import is_empty_spaces,is_empty_spaces_in_the_column, \
    is_valid_digit, is_valid_column, is_valid_input


# A function to position the player's move
def player_move(field, column):
    row = len(field) - 1

    while row >= 0:
        if field[row][column] == 0:
            break
        else:
            row -= 1

    return [row, column]


# A function that checks for the winner
def winner_checking(field, current_row, current_col, current_sign):
    result = list()

    result.append(check_row(field, current_row, current_sign))
    result.append(check_column(field, current_col, current_sign))
    result.append(check_primary_diagonal(field, current_row, current_col, current_sign))
    result.append(check_secondary_diagonal(field, current_row, current_col, current_sign))

    if any(result):
        return True

    return False


# A function that checks positions (row, column, first and second diagonal
def check_positions(field, row, col, sign, is_r=False, is_c=False, is_pd=False, is_sd=False):
    count = 0
    indices = []

    while True:
        if field[row][col] == sign:
            count += 1
            indices.append([row, col])

        if count == 4:
            for r, c in indices:
                field[r][c] = Back.WHITE + sign + Back.RESET
            return True

        if is_r and 0 <= col + 1 < COLUMNS:
            col += 1

        elif is_c and 0 <= row + 1 < ROWS:
            row += 1

        elif is_pd and (0 <= row + 1 < ROWS and 0 <= col + 1 < COLUMNS):
            row += 1
            col += 1

        elif is_sd and (0 <= row + 1 < ROWS and 0 <= col - 1 < COLUMNS):
            row += 1
            col -= 1

        else:
            return False

        if field[row][col] != sign:
            count = 0
            indices = []


# A function that checks if winner is at the given row
def check_row(field, row, sign):
    col = 0
    return check_positions(field, row, col, sign, is_r=True)


# A function that checks if winner is at the given column
def check_column(field, col, sign):
    row = 0
    return check_positions(field, row, col, sign, is_c=True)


# A function that checks if winner is at the primary diagonal
def check_primary_diagonal(field, row, col, sign):
    step = min(row, col)
    row -= step
    col -= step

    return check_positions(field, row, col, sign, is_pd=True)


# A function that checks if winner is at the secondary diagonal
def check_secondary_diagonal(field, row, col, sign):
    step = min(row, COLUMNS - 1 - col)
    row -= step
    col += step

    return check_positions(field, row, col, sign, is_sd=True)


# A function for start the game
def start_game(field):
    is_winner = False

    while is_empty_spaces(field) and not is_winner:

        for name, sign in players.items():

            while True:
                chosen_column = input(Fore.BLACK + f"{name}, please choose the column from 1 to {COLUMNS}: ")
                if is_valid_digit(chosen_column) and is_valid_input(chosen_column):
                    chosen_column = int(chosen_column) - 1
                    break
                print(Fore.RED + "The input is not valid. Try again...")

            if not is_valid_column(chosen_column, field):
                print(Fore.RED + f"{name}, you miss your turn. The column is not valid.")
                continue

            if is_empty_spaces_in_the_column(field, chosen_column):
                row, col = player_move(field, chosen_column)
                field[row][col] = sign

                is_winner = winner_checking(field, row, col, sign)

            else:
                print(Fore.RED + f"{name}, you miss your turn. The column is full.")

            [print(*row) for row in field]

            if is_winner:
                print(Fore.GREEN + f"The winner is {name}. Congratulation!")
                break

            if not is_empty_spaces(field):
                print(Fore.BLUE + "There is no more empty spaces. The game is over!")
                break

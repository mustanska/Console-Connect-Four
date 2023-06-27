from parameters import players_signs, ROWS, COLUMNS
from validation_functions import is_empty_spaces, is_valid_input, is_valid_column, is_empty_spaces_in_the_column


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
    result.append((check_primary_diagonal(field, current_row, current_col, current_sign)))
    result.append(check_secondary_diagonal(field, current_row, current_col, current_sign))

    if any(result):
        return True

    return False


# A function that checks if winner is at the given row
def check_row(field, row, sign):
    count = 0

    for column in range(COLUMNS):
        if field[row][column] == sign:
            count += 1

        if 0 <= column + 1 < COLUMNS and count < 4:
            if field[row][column + 1] != sign:
                count = 0

        if count == 4:
            return True

    return False


# A function that checks if winner is at the given column
def check_column(field, column, sign):
    count = 0

    for row in range(ROWS):
        if field[row][column] == sign:
            count += 1

        if 0 <= row + 1 < ROWS and count < 4:
            if field[row + 1][column] != sign:
                count = 0

        if count == 4:
            return True

    return False


# A function that checks if winner is at the primary diagonal
def check_primary_diagonal(field, row, column, sign):
    count = 0

    step = min(row, column)
    start_row = row - step
    start_col = column - step

    while 0 <= start_row < ROWS and 0 <= start_col < COLUMNS:
        if field[start_row][start_col] == sign:
            count += 1

        if 0 <= start_row + 1 < ROWS and 0 <= start_col + 1 < COLUMNS and count < 4:
            if field[start_row + 1][start_col + 1] != sign:
                count = 0

        if count == 4:
            return True

        start_row += 1
        start_col += 1

    return False


# A function that checks if winner is at the secondary diagonal
def check_secondary_diagonal(field, row, column, sign):
    count = 0

    step = min(row, COLUMNS - 1 - column)
    start_row = row - step
    start_col = column + step

    while 0 <= start_row < ROWS and 0 <= start_col < COLUMNS:
        if field[start_row][start_col] == sign:
            count += 1

        if 0 <= start_row + 1 < ROWS and 0 <= start_col - 1 < COLUMNS and count < 4:
            if field[start_row + 1][start_col - 1] != sign:
                count = 0

        if count == 4:
            return True

        start_row += 1
        start_col -= 1

    return False


# A function for start the game
def start_game(field):
    is_winner = False

    while is_empty_spaces(field) and not is_winner:

        for name, sign in players_signs.items():

            while True:
                chosen_column = input(f"{name}, please choose the column from 1 to {COLUMNS}")
                if is_valid_input(chosen_column):
                    chosen_column = int(chosen_column) - 1
                    break
                print("The input is not valid. Try again...")

            if not is_valid_column(chosen_column, field):
                print(f"{name}, you miss your turn. The column is not valid.")
                continue

            if is_empty_spaces_in_the_column(field, chosen_column):
                row, col = player_move(field, chosen_column)
                field[row][col] = sign

                is_winner = winner_checking(field, row, col, sign)

            else:
                print(f"{name}, you miss your turn. The column is full.")

            [print(*row) for row in field]

            if is_winner:
                print(f"The winner is {name}. Congratulation!")
                break

            if not is_empty_spaces(field):
                print(f"There is no more empty spaces. The game is over!")
                break

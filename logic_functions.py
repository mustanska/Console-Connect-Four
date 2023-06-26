from parameters import players_signs, COLUMNS
from validation_functions import is_empty_spaces, is_valid_input, is_valid_column, is_empty_spaces_in_the_column


# A function to position the player's move
def player_move(field, sign, column):
    row = len(field) - 1

    while row >= 0:
        if field[row][column] == 0:
            field[row][column] = sign
            break
        else:
            row -= 1

    return field


# A function that checks for the winner
def winner_checking(field):
    pass


# A function for start the game
def start_game(field):
    while is_empty_spaces(field) and not winner_checking(field):

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
                field = player_move(field, sign, chosen_column)
            else:
                print(f"{name}, you miss your turn. The column is full.")

            [print(*row) for row in field]

            if winner_checking(field):
                print(f"The winner is {name}. Congratulation!")
                break

            if not is_empty_spaces(field):
                print(f"There is no more empty spaces. The game is over!")
                break

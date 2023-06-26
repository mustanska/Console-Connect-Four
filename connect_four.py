from functions import is_valid_column, is_empty_spaces, is_empty_spaces_in_the_column, player_move
from parameters import field, ROWS, COLUMNS, players_signs

# Start the game
# TODO: add the logic about the winner
while is_empty_spaces(field):
    for name, sign in players_signs.items():
        chosen_column = int(input(f"{name}, please choose the column from 1 to {COLUMNS}")) - 1

        if not is_valid_column(chosen_column, field):
            print(f"{name}, you miss your turn. The column is not valid.")
            continue

        if is_empty_spaces_in_the_column(field, chosen_column):
            field = player_move(field, sign, chosen_column)
        else:
            print(f"{name}, you miss your turn. The column is full.")

        [print(*row) for row in field]

        if not is_empty_spaces(field):
            break


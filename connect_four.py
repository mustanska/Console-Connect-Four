from functions import check_unique_value, is_empty_spaces_in_the_column, player_move

ROWS = 6    # the field rows
COLUMNS = 7     # the field columns

field = [[0] * COLUMNS for row in range(ROWS)]

players = int(input("How many people will you play?"))

# Create the dictionary with information about name of player and its sign
players_signs = {}
number = 1

while number <= players:
    name = input(f"Player {number} please write your name: ")
    sign = input("Choose sign: ")

    if check_unique_value(name, players_signs.keys()) and check_unique_value(sign, players_signs.values()):
        players_signs[name] = sign
        number += 1
    else:
        print("The name or the sign is already taken. Please write them again.")

# Start the game
# TODO: make while loop stopping when the field is full
# TODO: add the logic about the winner
while True:
    for name, sign in players_signs.items():
        chosen_column = int(input(f"{name}, please choose the column from 1 to {COLUMNS}")) - 1

        if is_empty_spaces_in_the_column(field, chosen_column):
            field = player_move(field, sign, chosen_column)
        else:
            print("You miss your turn. The column is full.")

        [print(*row) for row in field]


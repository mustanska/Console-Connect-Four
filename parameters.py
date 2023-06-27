from validation_functions import is_unique_value, is_valid_input

ROWS = 6    # the field rows
COLUMNS = 7     # the field columns

empty_field = [[0] * COLUMNS for row in range(ROWS)]

while True:
    players = input("How many people will you play?")
    if is_valid_input(players):
        players = int(players)
        break

    print("The input is not valid. Try again...")


# Create the dictionary with information about name of player and its sign
players_signs = {}
number = 1

while number <= players:
    name = input(f"Player {number} please write your name: ")
    sign = input("Choose sign: ")

    if is_unique_value(name, players_signs.keys()) and is_unique_value(sign, players_signs.values()):
        players_signs[name] = sign
        number += 1
    else:
        print("The name or the sign is already taken. Please write them again.")

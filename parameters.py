from colorama import Fore
from validation_functions import is_unique_value, is_valid_input

ROWS = 6    # the field rows
COLUMNS = 7     # the field columns
COLORS = [Fore.RED, Fore.BLUE, Fore.CYAN, Fore.MAGENTA, Fore.YELLOW]

empty_field = [[0] * COLUMNS for row in range(ROWS)]

while True:
    players = input(Fore.BLACK + "How many people will you play? Choose from 2 to 5: ")

    if is_valid_input(players):
        players = int(players)
        if 1 < players <= 5:
            break

    print(Fore.RED + "The input is not valid. Try again...")


# Create the dictionary with information about name of player and its sign
players_signs = {}
number = 1

while number <= players:
    name = input(Fore.BLACK + f"Player {number} please write your name: ")
    sign = input("Choose sign: ")

    if is_unique_value(name, players_signs.keys()) and is_unique_value(sign, players_signs.values()):
        players_signs[name] = COLORS[number - 1] + sign + Fore.BLACK
        number += 1
    else:
        print(Fore.RED + "The name or the sign is already taken. Please write them again.")

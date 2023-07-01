from colorama import Fore
from validation_functions import is_valid_input, is_unique_value


def set_players_count():
    while True:
        players = input(Fore.BLACK + "How many people will you play? Choose from 2 to 5: ")

        if is_valid_input(players):
            players = int(players)
            if 1 < players <= 5:
                return players

        print(Fore.RED + "The input is not valid. Try again...")


def set_players_data(players):
    number = 1
    players_signs = {}
    COLORS = [Fore.RED, Fore.BLUE, Fore.CYAN, Fore.MAGENTA, Fore.YELLOW]

    while number <= players:
        name = input(Fore.BLACK + f"Player {number} please write your name: ")
        sign = input("Choose sign: ")

        # Checks if name and sign is unique
        # When checks the sign, the other players signs are player_sign[5:6]
        # Because we want only unique signs without color
        if is_unique_value(name, players_signs.keys()) and \
                is_unique_value(sign, [player_sign[5:6] for player_sign in players_signs.values()]):

            players_signs[name] = COLORS[number - 1] + sign + Fore.BLACK
            number += 1
        else:
            print(Fore.RED + "The name or the sign is already taken. Please write them again.")

    return players_signs

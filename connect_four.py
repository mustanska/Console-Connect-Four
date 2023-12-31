from colorama import Fore
from copy import deepcopy
from logic_functions import start_game
from variables import empty_field

start = input('Press "Y" if you want to start the game or something else if you want to leave: ').lower()

while start == "y":
    field = deepcopy(empty_field)
    start_game(field)

    start = input(Fore.BLACK + 'Press "Y" to restart the game or something else to leave: ').lower()
else:
    print("Bye. See you soon.")

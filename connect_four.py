from colorama import Fore
from copy import deepcopy
from logic_functions import start_game
from parameters import empty_field

start = input('Press "Y" if you want to start the game or something else if you want to leave:').lower()

while start == "y":
    field = deepcopy(empty_field)
    start_game(field)

    start = input(Fore.BLACK + 'Press "Y" if you want to restart the game or "N" if you want to leave:').lower()
else:
    print("Bye. See you soon.")
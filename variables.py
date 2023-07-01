from input_validation import set_players_count, set_players_data

ROWS = 6    # the field rows
COLUMNS = 7     # the field columns

empty_field = [[0] * COLUMNS for row in range(ROWS)]

players_count = set_players_count()   # players count
players = set_players_data(players_count)  # dictionary with information about name of player and its sign

# A function that checks for a unique player name and sign
def check_unique_value(current_value, current_list):
    if current_value not in current_list:
        return True
    return False


# A function that checks for empty space in column
def is_empty_spaces_in_the_column(field, column):
    for row in range(len(field)):
        if field[row][column] == 0:
            return True
    return False


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

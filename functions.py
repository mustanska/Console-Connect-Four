# A function that checks for a unique player name and sign
def is_valid_column(current_column, current_list):
    for row in range(len(current_list)):
        if 0 <= current_column < len(current_list[row]):
            return True
    return False


# A function that checks for a unique player name and sign
def is_unique_value(current_value, current_list):
    if current_value not in current_list:
        return True
    return False


# A function that checks for empty space in column
def is_empty_spaces_in_the_column(field, column):
    for row in range(len(field)):
        if field[row][column] == 0:
            return True
    return False


# A function that checks for empty space in field
def is_empty_spaces(field):
    for row in range(len(field)):
        for col in range(len(field[row])):
            if is_empty_spaces_in_the_column(field, col):
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

# A function that checks for the winner

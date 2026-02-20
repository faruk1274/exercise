# The longest string

def longest(names: list):
    longest_string = names[0]

    for name in names:
        if len(name) > len(longest_string):
            longest_string = name

    return longest_string

# (2)

def who_won(game_board: list):
    player1 = 0
    player2 = 0

    for row in game_board:
        for cell in row:
            if cell == 1:
                player1 += 1
            elif cell == 2:
                player2 += 1

    if player1 > player2:
        return 1
    elif player2 > player1:
        return 2
    else:
        return 0

# (3)
def row_correct(sudoku: list, row_no: int):
    seen = set()
    for num in sudoku[row_no]:
        if num != 0:
             if num in seen:
                return False
             seen.add(num)
    return True

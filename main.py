import constants

# 1. Create the "Source of Truth" (The Board)
# This is a list of 9 lists, each containing 9 dots.
size = 9
board = [["." for _ in range(size)] for _ in range(size)]

# 2. The Display Logic (A function you can call anytime)
def display_board(board_data):
    for row in board_data:
        # This takes each list and turns it into a string like ". . . ."
        print(" ".join(row))

# 3. In your main logic:
display_board(board)
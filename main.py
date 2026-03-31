import constants

# 1. Create the "Source of Truth" (The Board)
# This is a list of 9 lists, each containing 9 dots.
size = 13
board = [["." for _ in range(size)] for _ in range(size)]

# 2. The Display Logic (A function you can call anytime)
def display_board(board_data):
    for row in board_data:
        # This takes each list and turns it into a string like ". . . ."
        print(" ".join(row))

def main():
    print("Welcome to the Go Logger!")
    
    # 1. Ask the user for the board size
    user_choice = input("Enter board size (9, 13, or 19): ")
    
    # 2. Convert the string to an integer
    size = int(user_choice)
    
    # 3. Create the board based on that size
    board = [["." for _ in range(size)] for _ in range(size)]
    
    # 4. Show the empty board
    display_board(board)

main()
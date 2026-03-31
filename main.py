from engine import GoEngine

def display_board(board_data):
    for row in board_data:
        print(" ".join(row))

def main():
    size = int(input("Enter size: "))
    engine = GoEngine(size)
    
    current_board = engine.get_board()
    display_board(current_board)

main()
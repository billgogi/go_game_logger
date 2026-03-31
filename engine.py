import constants

class GoEngine:
    def __init__(self, size):
        self.size = size
        self.board = [["." for _ in range(size)] for _ in range(size)]

    def get_board(self):
        return self.board
import Space
from enums import SpaceType
def Board():
    def __init__(self):
        self.board = [None] * 40
        self.board[0] = Space("Go", SpaceType.GO)

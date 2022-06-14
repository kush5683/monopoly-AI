from Board import Board

if __name__ == '__main__':
    board = Board()
    for _ in range(40):
        print(f"{next(board)}")

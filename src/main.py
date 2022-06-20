from rich import print

from Board import Board
from Player import Player
from PlayerOrder import PlayerOrder

if __name__ == '__main__':
    board = Board()
    board.set_debug(True)
    with open("../space data/PlayerConfig.txt", "r") as file:
        lines = file.readlines()
        num_players = int(lines[0].strip())
        player_start_balance = float(lines[1].strip())
    print(f"{num_players} players, starting with ${player_start_balance}")
    p = []
    for i in range(num_players):
        temp_p = Player(player_id=i + 1, balance=player_start_balance, properties=[],
                        current_space=board.get_go_space())
        p.append(temp_p)
    players = PlayerOrder(p)
    board.place_players(players)

    print(board)

    for p in board.get_players():
        print(p)
    print()

    for _ in range(3):
        board.play_turn()

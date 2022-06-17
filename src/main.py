from Board import Board
from Player import Player
from PlayerOrder import PlayerOrder
from rich import print

if __name__ == '__main__':
    board = Board()

    with open("../space data/PlayerConfig.txt", "r") as file:
        lines = file.readlines()
        num_players = int(lines[0].strip())
        player_start_balance = float(lines[1].strip())
    print(f"{num_players} players, starting with ${player_start_balance}")
    p = []
    for i in range(num_players):
        p.append(Player(player_id=i + 1, balance=player_start_balance, properties=[],
                        current_space=board.get_go_space()))
    players = PlayerOrder(p)
    board.place_players(players)
    # print(f"{board.BankerPlayer}")
    for player in board.get_players():
        print(f"{player}")

    print(board)

    for _ in range(num_players):
        print(next(board.player_order))



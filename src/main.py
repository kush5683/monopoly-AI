from Board import Board
from Player import Player
from PlayerOrder import PlayerOrder
if __name__ == '__main__':
    board = Board()
    for _ in range(40):
        print(f"{next(board)}")
    num_players = 0
    player_start_balance = 0.0
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

    for player in players:
        print(f"{player}")

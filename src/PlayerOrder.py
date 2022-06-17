from random import randint
from Player import Player


class PlayerOrder:
    def __init__(self, players: list[Player]):
        self.next_player = None
        self.players = players
        self.init_player_order()

    def __next__(self) -> Player:
        try:
            return next(self.next_player)
        except StopIteration:
            self.next_player = iter(self.players)
            return next(self.next_player)

    def __iter__(self) -> Player:
        return self.next_player

    """
    Rolls a die for each player and then sorts by each player's roll.
    """

    def init_player_order(self) -> None:
        rolls = [randint(1, 6) for _ in range(len(self.players))]
        new_order = sorted(list(zip(self.players, rolls)), key=lambda x: x[1])
        self.players = [x[0] for x in new_order]
        self.next_player = iter(self.players)

    def get_player_order(self) -> list[Player]:
        return self.players

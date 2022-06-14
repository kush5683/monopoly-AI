from Player import Player
from Space import Space


class Banker(Player):
    def __init__(self, player_id=0, money=float('inf')):
        super().__init__(player_id=player_id, balance=money, properties=[], current_space=None)

    def __repr__(self):
        return f"Banker({self.id=}, {self.balance=}, {self.properties=})"

    def put_in_jail(self, jail_space: Space) -> None:
        return None

    def get_properties(self) -> list[Space]:
        return self.properties

import Space
from random import randint

class Player:
    def __init__(self, player_id: int, balance: float = 1500.0, properties=None, current_space: Space = None):
        if properties is None:
            properties = []
        self.id = player_id
        self.balance = balance
        self.properties = properties
        self.current_space = current_space
        self.in_jail = False
        self.turns_left_in_jail = 0

    def __repr__(self):
        if self.id == 0:
            return "Banker"
        return f"Player {self.id}"

    def __str__(self):
        return f"Player({self.id=},{self.current_space=},{self.balance=}, {self.properties=})"

    def get_id(self) -> int:
        return self.id

    def get_current_space(self) -> Space:
        return self.current_space

    def get_balance(self) -> float:
        return self.balance

    def get_properties(self) -> list[Space]:
        return self.properties

    def add_property(self, property: Space) -> list[Space]:
        self.properties.append(property)
        return self.properties

    def remove_property(self, property: Space) -> list[Space]:
        self.properties.remove(property)
        return self.properties

    def add_balance(self, amount: float) -> float:
        self.balance += amount
        return self.balance

    def remove_balance(self, amount: float) -> float:
        self.balance -= amount
        return self.balance

    def put_in_jail(self, jail_space: Space) -> Space:
        self.in_jail = True
        self.current_space = jail_space
        return self.current_space


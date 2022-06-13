from typing import List
from random import randint
from src.property import Property
from src.Space import Space


class Player:
    def __init__(self, player_id: int, balance: float, properties: List[Property], current_space: Space):
        self.id = player_id
        self.balance = balance
        self.properties = properties
        self.current_space = current_space

    def get_id(self) -> int:
        return self.id

    def get_current_space(self) -> Space:
        return self.current_space

    def get_balance(self) -> float:
        return self.balance

    def get_properties(self) -> List[Property]:
        return self.properties

    def add_property(self, property: Property) -> List[Property]:
        self.properties.append(property)
        return self.properties

    def remove_property(self, property: Property) -> List[Property]:
        self.properties.remove(property)
        return self.properties

    def add_balance(self, amount: float) -> float:
        self.balance += amount
        return self.balance

    def remove_balance(self, amount: float) -> float:
        self.balance -= amount
        return self.balance

    def roll_dice(self) -> int:
        return randint(1, 6)


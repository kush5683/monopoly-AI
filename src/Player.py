from typing import List

from src.property import Property


class Player:
    def __init__(self, player_id, balance, properties):
        self.id = player_id
        self.balance = balance
        self.properties = properties

    def get_id(self) -> int:
        return self.id

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


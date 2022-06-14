from dataclasses import dataclass
from typing import List

import Player
from enums import Color, SpaceType
from Property import Property
from Space import Space


@dataclass
class Go(Space):
    name: str
    color: Color
    type: SpaceType
    rent: float
    visitors: list[Player]
    most_recent_visitor: Player

    def land(self) -> float:
        """
        Collect $200 from the bank.
        :return:
        """
        self.most_recent_visitor.add_balance(self.rent)
        return self.most_recent_visitor.get_balance()

    def add_visitor(self, visitor: Player) -> Space:
        """
        Adds a visitor to the property.
        """
        self.visitors.append(visitor)
        self.most_recent_visitor = visitor
        return self

    def remove_visitor(self, visitor: Player) -> Space:
        """
        Removes a visitor from the property.
        """
        self.visitors.remove(visitor)
        return self

    def get_visitors(self) -> list[Player]:
        """
        Returns the list of visitors.
        """
        return self.visitors

from __future__ import annotations

from dataclasses import dataclass
from typing import List

import Player
import Space
from enums import Color


@dataclass
class Property(Space):
    name: str  # name of the property
    color: Color  # color of the property
    cost: float  # initial cost of the property
    rent: float  # dictionary of rent for each house {0:0, 1:0, 2:0, 3:0, 4:0, 5:0}; where 0 is no houses, 1 is one
    # house, 2 is two houses, 3 is three houses, 4 is four houses and 5 is a hotel
    mortgage: float  # mortgage value of the property
    house_cost: float  # cost to buy a house
    hotel_cost: float  # cost to buy a hotel
    owner: Player  # owner of the property
    visitors: list  # list of players who are visiting the property
    most_recent_visitor: Player  # most recent visitor of the property

    def pay_rent(self) -> float:
        """
        Pay the rent of the property.
        """
        self.owner.add_balance(self.rent)
        self.most_recent_visitor.remove_balance(self.rent)
        return self.most_recent_visitor.get_balance()

    def add_visitor(self, visitor: Player) -> Property:
        """
        Adds a visitor to the property.
        """
        self.visitors.append(visitor)
        self.most_recent_visitor = visitor
        return self

    def get_visitors(self) -> List[Player]:
        """
        Returns the list of visitors.
        """
        return self.visitors

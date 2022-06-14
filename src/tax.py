from dataclasses import dataclass
from typing import List

import Player
from enums import Color
import Property
import Space

@dataclass
class Tax(Space):
    name: str
    color: Color
    rent: float
    visitors: List[Player]
    most_recent_visitor: Player

    def land(self) -> float:
        """
        Pay the tax.
        """
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

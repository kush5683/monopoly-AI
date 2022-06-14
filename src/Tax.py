from dataclasses import dataclass

import Player
from enums import Color, SpaceType
from Space import Space
from ColorPrinting import *

@dataclass
class Tax(Space):
    name: str
    color: Color
    type: SpaceType
    rent: float
    visitors: list[Player]
    most_recent_visitor: Player

    def __repr__(self):
        if self.color == Color.BROWN:
            return brown(self.name)
        elif self.color == Color.LIGHT_BLUE:
            return light_blue(self.name)
        elif self.color == Color.PINK:
            return pink(self.name)
        elif self.color == Color.ORANGE:
            return orange(self.name)
        elif self.color == Color.RED:
            return red(self.name)
        elif self.color == Color.YELLOW:
            return yellow(self.name)
        elif self.color == Color.GREEN:
            return green(self.name)
        elif self.color == Color.DARK_BLUE:
            return dark_blue(self.name)
        elif self.color == Color.BLANK:
            return blank(self.name)

    def land(self) -> float:
        """
        Pay the tax.
        """
        self.most_recent_visitor.remove_balance(self.rent)
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

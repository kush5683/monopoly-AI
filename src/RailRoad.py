from dataclasses import dataclass
from Property import Property
from Player import Player
from enums import Color, SpaceType
from ColorPrinting import *

@dataclass
class RailRoad(Property):
    pass

    def land(self, visitor: Player, *args, **kwargs) -> float:
        """
        Pay the rent.
        """
        owned = len(list(filter(lambda x: x.type == SpaceType.RAILROAD, self.owner.get_properties())))
        self.most_recent_visitor = visitor
        self.current_rent = self.rent[owned - 1]
        visitor.remove_balance(self.current_rent)
        self.owner.add_balance(self.current_rent)
        return visitor.get_balance()

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

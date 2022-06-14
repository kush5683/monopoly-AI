from dataclasses import dataclass
from enums import Color, SpaceType
from ColorPrinting import *

from Property import Property
from Player import Player


@dataclass
class Utility(Property):
    pass

    def land(self, visitor: Player, rolled: int) -> float:
        """
        Pay the tax.
        """
        if len(list(filter(lambda x: x.type == SpaceType.UTILITY, self.owner.get_properties()))) == 1:
            return rolled * 4
        else:
            return rolled * 10

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

from dataclasses import dataclass

import Player
from ColorPrinting import *
from Space import Space
from enums import Color, SpaceType


@dataclass
class GoToJail(Space):
    name: str
    color: Color
    type: SpaceType
    rent: float
    visitors: list[Player]
    most_recent_visitor: Player
    jail_space: Space

    def land(self) -> Space:
        """
        Go to jail.
        """
        self.most_recent_visitor.put_in_jail(self.jail_space)
        self.most_recent_visitor.turns_left_in_jail = 3
        return self.jail_space

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

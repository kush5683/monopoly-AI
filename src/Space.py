from __future__ import annotations

from abc import ABC, abstractmethod
from enums import Color, SpaceType
from ColorPrinting import *


class Space(ABC):
    type: SpaceType
    color: Color
    name: str

    @abstractmethod
    def land(self, *args, **kwargs) -> Space:
        pass

    @abstractmethod
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

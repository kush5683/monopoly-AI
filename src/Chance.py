from dataclasses import dataclass

from Space import Space
import Player
from enums import Color, SpaceType
import json
from random import choice
from ColorPrinting import *

@dataclass
class Chance(Space):
    name: str
    color: Color
    type: SpaceType
    rent: float
    visitors: list[Player]
    most_recent_visitor: Player

    def land(self) -> str:
        with open("../space data/chance jsons/chance.json", "r") as file:
            community_json = json.load(file)
            return choice(community_json["CARD_TEXTS"])

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

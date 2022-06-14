from dataclasses import dataclass, field

from Player import Player
from enums import Color, SpaceType
from Space import Space
from ColorPrinting import *


@dataclass
class Property(Space):
    name: str  # name of the property
    color: Color  # color of the property
    type: SpaceType  # type of the property
    cost: float  # initial cost of the property
    rent: dict  # dictionary of rent for each house {0:0, 1:0, 2:0, 3:0, 4:0, 5:0}; where 0 is no houses, 1 is one
    # house, 2 is two houses, 3 is three houses, 4 is four houses and 5 is a hotel
    mortgage: float  # mortgage value of the property
    house_cost: float  # cost to buy a house
    hotel_cost: float  # cost to buy a hotel
    owner: Player = None  # owner of the property
    visitors: list[Player] = field(default_factory=list)  # list of players who are visiting the property
    most_recent_visitor: Player = None  # most recent visitor of the property
    houses_built: int = 0  # number of houses built on the property
    current_rent: float = None  # current rent of the property

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

    def init_prop(self) -> Space:
        """
        Returns the current rent of the property.
        """
        if self.current_rent is None:
            self.current_rent = self.rent[self.houses_built]
        return self

    def land(self, visitor: Player, *args, **kwargs) -> float:
        """
        Pay the rent of the property.
        """
        self.most_recent_visitor = visitor
        self.owner.add_balance(self.current_rent)
        self.most_recent_visitor.remove_balance(self.current_rent)
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

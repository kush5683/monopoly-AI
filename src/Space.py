from __future__ import annotations

from dataclasses import dataclass, field

import Player
from ColorPrinting import *
from enums import Color, SpaceType
import logger


@dataclass
class Space:
    name: str
    color: Color
    type: SpaceType
    cost: float
    mortgage: float
    house_cost: float
    hotel_cost: float
    rent: dict
    owner: Player = None  # owner of the property
    houses_built: int = 0  # number of houses built on the property
    current_rent: int = 0
    visitors: list[Player.Player] = field(default_factory=list)  # list of players who are visiting the property
    most_recent_visitor: Player.Player = None  # most recent visitor of the property
    debug_flag: bool = True
    for_sale: bool = True

    def land(self, visitor: Player.Player, *args, **kwargs) -> Space:
        self.debug(f"\tPlayer #{visitor.id} landed on {self.name}")
        self.most_recent_visitor = visitor
        if kwargs.get('want_to_buy') and self.for_sale:
            self.debug(f"Player #{visitor.id} wants to buy {self.name}")
            if visitor.get_balance() >= self.cost:
                self.debug(f"Player #{visitor.id} has enough money to buy {self.name}")
                self.sell_to(visitor)
                self.debug(f"Player #{self.owner.id} bought {self.name}")
        return self

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

    def __hash__(self):
        return hash(self.name)

    def add_visitor(self, visitor: Player.Player) -> Space:
        """
        Adds a visitor to the property.
        """
        self.visitors.append(visitor)
        self.most_recent_visitor = visitor
        return self

    def remove_visitor(self, visitor: Player.Player) -> Space:
        """
        Removes a visitor from the property.
        """
        self.visitors.remove(visitor)
        return self

    def get_visitors(self) -> list[Player.Player]:
        """
        Returns the list of visitors.
        """
        return self.visitors

    def sell_to(self, player: Player.Player) -> bool:
        """
        Sells the property to the player.
        """
        if self.type == SpaceType.PROPERTY or self.type == SpaceType.UTILITY or self.type == SpaceType.RAILROAD:
            player.remove_balance(self.cost)
            self.owner.add_balance(self.cost)
            self.owner.properties.remove(self)
            self.owner = player
            self.owner.properties.append(self)
            self.for_sale = False
            return True

    def put_on_market(self, cost: float):
        self.for_sale = True
        self.cost = cost

    def set_debug(self, val: bool) -> bool:
        self.debug_flag = val
        return self.debug_flag

    def debug(self, message: str) -> None:
        if self.debug_flag:
            logger.log(message)
        return

from dataclasses import dataclass
from typing import List
import Player
from enums import Color, SpaceType
from Property import Property
from Space import Space


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

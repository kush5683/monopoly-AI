import Player
from Space import Space
from enums import Color, SpaceType


class GoToJail(Space):

    def __init__(self, name: str, color: Color, type: SpaceType, rent: dict, owner: Player, jail_space: Space):
        super().__init__(name=name, color=color, cost=float("inf"), mortgage=float("inf"), house_cost=float("inf"),
                         hotel_cost=float("inf"), type=type, rent=rent, owner=owner)
        self.jail_space: Space = jail_space

    def land(self, visitor: Player.Player, *args, **kwargs) -> Space:
        """
        Go to jail.
        """
        super().land(visitor, *args, **kwargs)
        self.most_recent_visitor.put_in_jail(self.jail_space)
        self.most_recent_visitor.turns_left_in_jail = 3
        return self

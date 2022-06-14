from dataclasses import dataclass

import Player
from Space import Space


@dataclass
class GoToJail(Space):
    visitors: list[Player]
    most_recent_visitor: Player
    jail_space: Space
    owner: Player = None

    def land(self) -> Space:
        """
        Go to jail.
        """
        self.most_recent_visitor.put_in_jail(self.jail_space)
        self.most_recent_visitor.turns_left_in_jail = 3
        return self.jail_space

    def __repr__(self):
        return super().__repr__()

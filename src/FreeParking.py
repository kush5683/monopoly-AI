from dataclasses import dataclass

import Player
from Space import Space


@dataclass
class FreeParking(Space):
    visitors: list[Player]
    most_recent_visitor: Player
    owner: Player = None

    def land(self) -> None:
        pass

    def __repr__(self):
        return super().__repr__()


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

from dataclasses import dataclass

from Player import *
from Space import Space
from enums import *


@dataclass
class Tax(Space):
    visitors: list[Player]
    most_recent_visitor: Player
    owner: Player = None

    def __repr__(self):
        return super().__repr__()

    def land(self) -> float:
        """
        Pay the tax.
        """
        # 6/15/22 Added functionality so taxes were added to the FreeParkingPot.
        # Did some testing to quickly confirm it worked - KD
        self.most_recent_visitor.remove_balance(self.rent)
        #TODO Isn't rent a dictionary? So unless its updated to be the current rent we'll
        # need to specify a key for the current rent
        with open("../space data/FreeParkingTotal.txt", "r") as file:
        # TODO there is 1000000% a way to do this without opening the file twice but im lazy
            pot = int(file.readline())
        with open("../space data/FreeParkingTotal.txt", "w") as file:
            file.write(str(pot + self.rent[0]))
            #TODO The first rent should be the only one for Taxes so I used key 0 to get the value (see line 24 TODO) - KD

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

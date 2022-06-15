from dataclasses import dataclass

from Player import Player
from Space import Space
from enums import *


@dataclass
class FreeParking(Space):
    visitors: list[Player]
    most_recent_visitor: Player
    owner: Player = None

    def land(self) -> None:
        """
        Adds the free parking pot saved in space data/FreeParkingTotal.txt to
        the visitors balance and resets the pot.
        """
        winner = self.most_recent_visitor
        with open("../space data/FreeParkingTotal.txt", "r") as file:
        # TODO there is 1000000% a way to do this without opening the file twice but im lazy
            free_parking_pot = int(file.readline())
        with open("../space data/FreeParkingTotal.txt", "w") as file:
            file.write('0')
        print(f"Player {winner.id} won {free_parking_pot} at free parking!")
        winner.add_balance(free_parking_pot)
        return


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

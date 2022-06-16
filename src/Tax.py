from Player import Player
from Space import Space


class Tax(Space):

    def land(self, visitor: Player, *args, **kwargs) -> float:
        """
        Pay the tax.
        """
        super().land(visitor, *args, **kwargs)
        # 6/15/22 Added functionality so taxes were added to the FreeParkingPot.
        # Did some testing to quickly confirm it worked - KD
        self.most_recent_visitor.remove_balance(self.rent.get(self.current_rent))
        # TODO Isn't rent a dictionary? So unless its updated to be the current rent we'll
        # need to specify a key for the current rent
        with open("../space data/FreeParkingTotal.txt", "r") as file:
            # TODO there is 1000000% a way to do this without opening the file twice but im lazy
            pot = int(file.readline())
        with open("../space data/FreeParkingTotal.txt", "w") as file:
            file.write(str(pot + self.rent.get(self.current_rent)))
            # TODO The first rent should be the only one for Taxes so I used key 0 to get the value (see line 16 TODO) - KD

        return self.most_recent_visitor.get_balance()

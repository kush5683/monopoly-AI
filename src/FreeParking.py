from Player import Player
from Space import Space


class FreeParking(Space):

    def land(self, visitor: Player, *args, **kwargs) -> None:
        """
        Adds the free parking pot saved in space data/FreeParkingTotal.txt to
        the visitors balance and resets the pot.
        """
        super().land(visitor, *args, **kwargs)
        winner = self.most_recent_visitor
        with open("../space data/FreeParkingTotal.txt", "r") as file:
            # TODO there is 1000000% a way to do this without opening the file twice but im lazy
            free_parking_pot = int(file.readline())
        with open("../space data/FreeParkingTotal.txt", "w") as file:
            file.write('0')
        print(f"Player {winner.id} won {free_parking_pot} at free parking!")
        winner.add_balance(free_parking_pot)
        return

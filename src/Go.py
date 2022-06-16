import Player
from Space import Space


class Go(Space):

    def land(self, visitor: Player, *args, **kwargs) -> float:
        """
        Collect $200 from the bank.
        :return:
        """
        super().land(visitor, *args, **kwargs)
        self.most_recent_visitor.add_balance(self.rent.get(self.current_rent))
        return self.most_recent_visitor.get_balance()

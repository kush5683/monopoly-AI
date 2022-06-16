from Player import Player
from Space import Space


class Property(Space):

    def init_prop(self) -> Space:
        """
        Returns the current rent of the property.
        """
        if self.current_rent is None:
            self.current_rent = self.rent[self.houses_built]
        return self

    def land(self, visitor: Player, *args, **kwargs) -> float:
        """
        Pay the rent of the property.
        """
        super().land(visitor, *args, **kwargs)
        self.owner.add_balance(self.current_rent)
        self.most_recent_visitor.remove_balance(self.current_rent)
        return self.most_recent_visitor.get_balance()

from dataclasses import dataclass
from Property import Property
from Player import Player
from enums import Color, SpaceType


@dataclass
class RailRoad(Property):
    pass

    def land(self, visitor: Player, *args, **kwargs) -> float:
        """
        Pay the rent.
        """
        owned = len(list(filter(lambda x: x.type == SpaceType.RAILROAD, self.owner.get_properties())))
        self.most_recent_visitor = visitor
        self.current_rent = self.rent[owned - 1]
        visitor.remove_balance(self.current_rent)
        self.owner.add_balance(self.current_rent)
        return visitor.get_balance()

from dataclasses import dataclass

from Player import Player
from Property import Property
from enums import SpaceType


@dataclass
class Utility(Property):
    pass

    def land(self, visitor: Player, rolled: int) -> float:
        """
        Pay the tax.
        """
        if len(list(filter(lambda x: x.type == SpaceType.UTILITY, self.owner.get_properties()))) == 1:
            return rolled * 4
        else:
            return rolled * 10

    def __repr__(self):
        return super().__repr__()

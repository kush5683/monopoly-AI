from dataclasses import dataclass
from enums import Color, SpaceType
from _distutils_hack import override

from Property import Property
from Player import Player


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

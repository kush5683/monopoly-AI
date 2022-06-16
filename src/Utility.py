from Player import Player
from Property import Property
from enums import SpaceType


class Utility(Property):

    def land(self, visitor: Player, *args, **kwargs) -> float:
        """
        Pay the tax.
        """
        super().land(visitor, *args, **kwargs)
        rolled = kwargs.get('rolled')
        if len(list(filter(lambda x: x.type == SpaceType.UTILITY, self.owner.get_properties()))) == 1:
            return rolled * 4
        else:
            return rolled * 10

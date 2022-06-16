from Player import Player
from Property import Property
from enums import SpaceType, Color


class RailRoad(Property):
    def __init__(self, name: str, color: Color, type: SpaceType, cost: float, rent: dict, mortgage: float,
                 house_cost: float, hotel_cost: float, owner: Player = None, houses_built: int = 0,
                 current_rent: float = None):
        super().__init__(name=name, color=color, type=type, cost=cost, mortgage=mortgage, house_cost=house_cost,
                         hotel_cost=hotel_cost, rent=rent, owner=owner, houses_built=houses_built,
                         current_rent=current_rent)
        self.owned = None

    def land(self, visitor: Player, *args, **kwargs) -> float:
        """
        Pay the rent.
        """
        self.owned = len(list(filter(lambda x: x.type == SpaceType.RAILROAD, self.owner.get_properties())))
        self.most_recent_visitor = visitor
        self.current_rent = self.rent[self.owned - 1]
        visitor.remove_balance(self.current_rent)
        self.owner.add_balance(self.current_rent)
        return visitor.get_balance()

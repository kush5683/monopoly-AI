from dataclasses import dataclass, field

from Player import Player
from Space import Space


@dataclass
class Property(Space):
    cost: float  # initial cost of the property
    mortgage: float  # mortgage value of the property
    house_cost: float  # cost to buy a house
    hotel_cost: float  # cost to buy a hotel
    visitors: list[Player] = field(default_factory=list)  # list of players who are visiting the property
    most_recent_visitor: Player = None  # most recent visitor of the property
    owner: Player = None # owner of the property
    houses_built: int = 0  # number of houses built on the property
    current_rent: float = None  # current rent of the property

    def __repr__(self):
        return super().__repr__()

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
        self.most_recent_visitor = visitor
        self.owner.add_balance(self.current_rent)
        self.most_recent_visitor.remove_balance(self.current_rent)
        return self.most_recent_visitor.get_balance()

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

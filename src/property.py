from dataclasses import dataclass
from enums import Color
import Space


@dataclass
class Property(Space):
    name: str  # name of the property
    color: Color  # color of the property
    cost: float  # initial cost of the property
    rent: float  # dictionary of rent for each house {0:0, 1:0, 2:0, 3:0, 4:0, 5:0}; where 0 is no houses, 1 is one
    # house, 2 is two houses, 3 is three houses, 4 is four houses and 5 is a hotel
    mortgage: float  # mortgage value of the property
    house_cost: float  # cost to buy a house
    hotel_cost: float  # cost to buy a hotel

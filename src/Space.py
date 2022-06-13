from enums import SpaceType
from abc import ABC, abstractmethod


class Space(ABC):
    """
    Abstract class for spaces in the game.
    """

    def __init__(self, name, space_type):
        self.space_type = space_type

    @abstractmethod
    def get_name(self):
        """
        Returns the name of the space.
        """
        pass

    @abstractmethod
    def get_space_type(self):
        """
        Returns the type of the space.
        """
        pass

    @abstractmethod
    def get_rent(self):
        """
        Returns the rent of the space.
        """
        pass

    @abstractmethod
    def get_mortgage(self):
        """
        Returns the mortgage value of the space.
        """
        pass

    @abstractmethod
    def get_house_cost(self):
        """
        Returns the cost to buy a house.
        """
        pass

    @abstractmethod
    def get_hotel_cost(self):
        """
        Returns the cost to buy a hotel.
        """
        pass

    @abstractmethod
    def get_color(self):
        """
        Returns the color of the space.
        """
        pass

    @abstractmethod
    def get_cost(self):
        """
        Returns the cost of the space.
        """
        pass

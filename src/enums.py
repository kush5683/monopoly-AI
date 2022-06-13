import enum


class SpaceType(enum.Enum):
    """
    Enum for the different spaces in the game.
    """
    PROPERTY = 0
    UTILITY = 1
    VISITING_JAIL = 2
    GO = 3
    FREE_PARKING = 4
    GO_TO_JAIL = 5
    TAX = 6
    CHANCE = 7
    COMMUNITY = 8


class Color(enum.Enum):
    """
    Enum for the different colors in the game.
    """
    BLANK = -1
    BROWN = 0
    LIGHT_BLUE = 1
    PINK = 2
    ORANGE = 3
    RED = 4
    YELLOW = 5
    GREEN = 6
    DARK_BLUE = 7

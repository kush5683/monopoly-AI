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
    COMMUNITY_CHEST = 8
    JAIL = 9
    RAILROAD = 10


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


class ExitStrategy(enum.Enum):
    """
    Enum for the different exit strategies in the game.
    """
    EXIT_VIA_PAYMENT = 0
    EXIT_VIA_DOUBLE_ROLL = 1
    EXIT_VIA_TIME_SERVED = 2
    EXIT_NOT_IN_JAIL = 3
    EXIT_NOT_SUCCESSFUL = 4

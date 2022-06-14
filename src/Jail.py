from dataclasses import dataclass
from random import randint

import Player
from Space import Space
from enums import ExitStrategy


@dataclass
class Jail(Space):
    visitors: list[Player]
    most_recent_visitor: Player
    owner: Player = None

    def land(self, visitor: Player, payment: bool) -> ExitStrategy:
        self.most_recent_visitor = visitor
        if visitor.in_jail:
            if payment:  # in jail but wants to pay $50 to get out
                visitor.remove_balance(self.rent)
                visitor.in_jail = False
                visitor.turns_left_in_jail = 0
                return ExitStrategy.EXIT_VIA_PAYMENT
            elif visitor.turns_left_in_jail - 1 <= 0:  # last turn in jail
                visitor.in_jail = False
                visitor.turns_left_in_jail = 0
                return ExitStrategy.EXIT_VIA_TIME_SERVED
            elif visitor.turns_left_in_jail - 1 > 0:  # more than one turn left, roll for doubles
                die1 = randint(1, 6)
                die2 = randint(1, 6)
                if die1 == die2:
                    visitor.in_jail = False
                    visitor.turns_left_in_jail = 0
                    return ExitStrategy.EXIT_VIA_DOUBLE_ROLL
                return ExitStrategy.EXIT_NOT_SUCCESSFUL
        else:
            return ExitStrategy.EXIT_NOT_IN_JAIL

    def __repr__(self):
        return super().__repr__()

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

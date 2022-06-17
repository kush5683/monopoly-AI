from random import randint

import Player
from Space import Space
from enums import ExitStrategy


class Jail(Space):

    def land(self, visitor: Player, *args, **kwargs) -> ExitStrategy:
        payment = kwargs.get('payment')
        self.most_recent_visitor = visitor
        if visitor.in_jail:
            if payment:  # in jail but wants to pay $50 to get out
                visitor.remove_balance(self.rent.get(self.current_rent))
                visitor.in_jail = False
                visitor.turns_left_in_jail = 0
                return ExitStrategy.EXIT_VIA_PAYMENT
            elif visitor.turns_left_in_jail - 1 <= 0:  # last turn in jail
                visitor.in_jail = False
                visitor.turns_left_in_jail = 0
                return ExitStrategy.EXIT_VIA_TIME_SERVED
            elif visitor.turns_left_in_jail - 1 > 0:  # more than one turn left, roll for doubles
                visitor.turns_left_in_jail -= 1
                die1 = randint(1, 6)
                die2 = randint(1, 6)
                if die1 == die2:
                    visitor.in_jail = False
                    visitor.turns_left_in_jail = 0
                    return ExitStrategy.EXIT_VIA_DOUBLE_ROLL
                return ExitStrategy.EXIT_NOT_SUCCESSFUL
        else:
            return ExitStrategy.EXIT_NOT_IN_JAIL

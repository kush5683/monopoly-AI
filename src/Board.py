import json

from Banker import Banker
from Chance import Chance
from CommunityChest import CommunityChest
from Dice import roll as roll_dice
from FreeParking import FreeParking
from Go import Go
from GoToJail import GoToJail
from Jail import Jail
from Player import Player
from PlayerOrder import PlayerOrder
from Property import Property
from RailRoad import RailRoad
from Space import Space
from Tax import Tax
from Utility import Utility
from enums import SpaceType, Color, ExitStrategy
import logger


class Board:
    def __init__(self):
        self._board = []
        self._board_iterator = iter(self._board)
        self.active_board = dict()
        self.BankerPlayer = Banker()
        self.player_order = None
        self.active_player = None
        self.double_roll_count = 0
        self.GoSpace = Go(name="Go", color=Color.BLANK, type=SpaceType.GO, rent={0: 200},
                          cost=float("inf"), mortgage=float("inf"),
                          house_cost=float("inf"), hotel_cost=float("inf"))
        self.JailSpace = Jail(name="Jail", color=Color.BLANK, type=SpaceType.JAIL, rent={0: 0},
                              cost=float("inf"), mortgage=float("inf"),
                              house_cost=float("inf"), hotel_cost=float("inf"))
        self.FreeParkingSpace = FreeParking(name="Free Parking", color=Color.BLANK, type=SpaceType.FREE_PARKING,
                                            rent={0: 0},
                                            cost=float("inf"), mortgage=float("inf"),
                                            house_cost=float("inf"), hotel_cost=float("inf"))
        self.GoToJailSpace = GoToJail(name="Go To Jail", color=Color.BLANK, type=SpaceType.GO_TO_JAIL, rent={0: 0},
                                      jail_space=self.JailSpace, owner=self.BankerPlayer)

        self.debug_flag = False
        property_count = 0
        RR_count = 0
        U_count = 0
        T_count = 0
        # read the board from a file
        with open("../space data/BoardSpaceOrder.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line == "GO":
                    self._board.append(self.GoSpace)
                    self.active_board.update({self.GoSpace: []})
                elif line == "P":
                    filename = "../space data/property jsons/property" + str(property_count) + ".json"
                    with open(filename, "r") as property_file:
                        property_json = json.load(property_file)
                        color = None
                        match property_json["COLOR"].upper():
                            case "BLANK":
                                color = Color.BLANK
                            case "BROWN":
                                color = Color.BROWN
                            case "LIGHT_BLUE":
                                color = Color.LIGHT_BLUE
                            case "PINK":
                                color = Color.PINK
                            case "ORANGE":
                                color = Color.ORANGE
                            case "RED":
                                color = Color.RED
                            case "YELLOW":
                                color = Color.YELLOW
                            case "GREEN":
                                color = Color.GREEN
                            case "DARK_BLUE":
                                color = Color.DARK_BLUE
                        p = Property(name=property_json["NAME"], color=color, type=SpaceType.PROPERTY,
                                     cost=property_json["PRICE"],
                                     rent={0: property_json["RENT"],
                                           1: property_json["RENT_1"],
                                           2: property_json["RENT_2"],
                                           3: property_json["RENT_3"],
                                           4: property_json["RENT_4"],
                                           5: property_json["RENT_5"]},
                                     mortgage=property_json["MORTGAGE"], house_cost=property_json["HOUSE_PRICE"],
                                     hotel_cost=property_json["HOTEL_PRICE"],
                                     owner=self.BankerPlayer)
                        p.init_prop()
                        self.BankerPlayer.add_property(p)
                        self._board.append(p)
                        self.active_board.update({p: []})
                        property_count += 1
                elif line == "CC":
                    cc = CommunityChest(name="Community Chest", color=Color.BLANK, type=SpaceType.COMMUNITY_CHEST,
                                        rent={0: 0}, cost=float("inf"), mortgage=float("inf"),
                                        house_cost=float("inf"), hotel_cost=float("inf"))
                    self._board.append(cc)
                    self.active_board.update({cc: []})
                elif line == "T":
                    filename = "../space data/tax space jsons/tax" + str(T_count) + ".json"
                    with open(filename, "r") as tax_file:
                        tax_json = json.load(tax_file)
                        t = Tax(name=tax_json["NAME"], color=Color.BLANK, type=SpaceType.TAX,
                                rent=tax_json["COST"], cost=float("inf"), mortgage=float("inf"),
                                house_cost=float("inf"), hotel_cost=float("inf"))
                        self._board.append(t)
                        self.active_board.update({t: []})
                        T_count += 1
                elif line == "RR":
                    filename = "../space data/railroad jsons/railroad" + str(RR_count) + ".json"
                    with open(filename, "r") as railroad_file:
                        railroad_json = json.load(railroad_file)
                        rr = RailRoad(name=railroad_json["NAME"], color=Color.BLANK, type=SpaceType.RAILROAD,
                                      cost=railroad_json["PRICE"], rent={0: railroad_json["RENT"],
                                                                         1: railroad_json["RENT_1"],
                                                                         2: railroad_json["RENT_2"],
                                                                         3: railroad_json["RENT_3"], },
                                      mortgage=railroad_json["MORTGAGE"], house_cost=float('inf'),
                                      hotel_cost=float('inf'))
                        rr.init_prop()
                        self.BankerPlayer.add_property(rr)
                        self._board.append(rr)
                        self.active_board.update({rr: []})
                        RR_count += 1
                elif line == "CH":
                    ch = Chance(name="Chance", color=Color.BLANK, type=SpaceType.CHANCE, rent={0: 0},
                                cost=float("inf"), mortgage=float("inf"),
                                house_cost=float("inf"), hotel_cost=float("inf"))
                    self._board.append(ch)
                    self.active_board.update({ch: []})
                elif line == "J":
                    self._board.append(self.JailSpace)
                    self.active_board.update({self.JailSpace: []})
                elif line == "U":
                    filename = "../space data/utility jsons/utility" + str(U_count) + ".json"
                    with open(filename, "r") as utility_file:
                        utility_json = json.load(utility_file)
                        u = Utility(name=utility_json["NAME"], color=Color.BLANK, type=SpaceType.UTILITY,
                                    cost=utility_json["PRICE"], rent={0: 0}, mortgage=utility_json["MORTGAGE"],
                                    house_cost=float('inf'), hotel_cost=float('inf'))
                        self._board.append(u)
                        self.active_board.update({u: []})
                        self.BankerPlayer.add_property(u)
                        U_count += 1
                elif line == "FP":
                    self._board.append(self.FreeParkingSpace)
                    self.active_board.update({self.FreeParkingSpace: []})
                elif line == "GJ":
                    self._board.append(self.GoToJailSpace)
                    self.active_board.update({self.GoToJailSpace: []})
                else:
                    exit()

    def __repr__(self):
        return_string = ""
        for space in self.active_board.items():
            return_string += f"({space[0]}, {space[1] if space[1] else 'Vacant'})\n"
        return return_string

    def __next__(self):
        try:
            return self._board_iterator.__next__()
        except StopIteration:
            self._board_iterator = iter(self._board)
            return self._board_iterator.__next__()

    def place_players(self, players: PlayerOrder) -> None:
        self.debug(f"Placing Players: \n{players.get_player_order()}")
        self.player_order = players
        for p in players.get_player_order():
            self.active_board[self.GoSpace].append(p)
        self.active_player = next(self.player_order)
        # self.active_player = next(self.player_order)
        self.debug(f"First player is Player #{self.active_player.id}")

    def get_players(self):
        for player in self.player_order.players:
            yield player

    def get_banker(self) -> Banker:
        return self.BankerPlayer

    def get_go_space(self) -> Go:
        return self.GoSpace

    def get_free_parking_space(self) -> FreeParking:
        return self.FreeParkingSpace

    def get_go_to_jail_space(self) -> GoToJail:
        return self.GoToJailSpace

    def get_jail_space(self) -> Jail:
        return self.JailSpace

    def get_next_space(self, offset: int):
        player = self.active_player
        current_space = player.get_current_space()
        next_space = self._board[(self._board.index(current_space) + offset) % len(self._board)]
        return next_space

    def move_player(self, player: Player, new_space: Space) -> None:
        self.active_board[player.get_current_space()].remove(player)
        self.active_board[new_space].append(player)
        player.current_space = new_space

    def play_turn(self) -> Player:
        # TODO: I think this works but im not sure
        player = self.active_player
        self.debug(f"It is Player #{player.id}'s turn")

        if player.is_in_jail:
            self.debug("\tPlayer in jail")
            exit_code = player.current_space.land()
            if exit_code == ExitStrategy.EXIT_NOT_SUCCESSFUL:  # player did not exit jail; do nothing
                self.debug("\tPlayer did NOT exit Jail")
                self.active_player = next(self.player_order)
                self.debug(f"\tNext player is Player #{self.active_player.id}")
                return self.active_player
            if exit_code == ExitStrategy.EXIT_VIA_DOUBLE_ROLL or exit_code == ExitStrategy.EXIT_NOT_IN_JAIL:
                self.debug("Player exited jail")
                # allow for roll
                pass
        self.debug("\tRolling Dice")
        dice = roll_dice()
        self.debug(f"Rolled {dice[0]} and {dice[1]} for a total of {sum(list(dice))}")
        if dice[0] == dice[1]:  # if double handle it
            self.debug("\tDouble roll!")
            if self.double_roll_count + 1 >= 3:  # if it's the 3rd double send the player to jail
                self.debug("\tThird double in a row. Sending player to jail")
                player.put_in_jail(self.get_jail_space())
                self.double_roll_count = 0
                self.active_player = next(self.player_order)
                self.debug(f"\tNext player is Player #{self.active_player.id}")
                return self.active_player
            self.double_roll_count += 1  # if it's not the third double increment the double roll count
            self.debug("\tIncreasing double roll counter")
            next_space = self.get_next_space(dice[0] + dice[1])
            self.debug(f"\tMoving player to {next_space}")
            self.move_player(player, next_space)
            self.debug(f"\tPlayer is now at {player.current_space}")
            self.debug(f"\tNext player is Player #{self.active_player.id}")
            return self.active_player  # return the same player to allow for their second turn due to double roll
        else:  # no double
            self.debug("\tNot a double roll")
            self.double_roll_count = 0
            next_space = self.get_next_space(dice[0] + dice[1])
            self.debug(f"\tMoving player to {next_space}")
            self.move_player(player, next_space)
            self.debug(f"\tPlayer is now at {player.current_space}")
            self.active_player = next(self.player_order)
            self.debug(f"\tNext player is Player #{self.active_player.id}")
            return self.active_player  # return the next player in the order

    def set_debug(self, val: bool) -> bool:
        self.debug_flag = val
        return self.debug_flag

    def debug(self, message: str) -> None:
        if self.debug_flag:
            logger.log(message)
        return

import json

from Banker import Banker
from Chance import Chance
from CommunityChest import CommunityChest
from FreeParking import FreeParking
from Go import Go
from GoToJail import GoToJail
from Jail import Jail
from Property import Property
from RailRoad import RailRoad
from Tax import Tax
from Utility import Utility
from enums import SpaceType, Color
from Player import Player
from PlayerOrder import PlayerOrder


class Board:
    def __init__(self):
        self._board = []
        self._board_iterator = iter(self._board)
        self.active_board = dict()
        self.BankerPlayer = Banker()
        self.player_order = None
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
        self.player_order = players
        for p in players.get_player_order():
            self.active_board[self.GoSpace].append(p)

    def get_players(self) -> list[Player]:
        for player in self.player_order:
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

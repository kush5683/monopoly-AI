from Space import Space
from Go import Go
from FreeParking import FreeParking
from Jail import Jail
from GoToJail import GoToJail
from Property import Property
from CommunityChest import CommunityChest
from Tax import Tax
from RailRoad import RailRoad
from Chance import Chance
from Utility import Utility
from enums import SpaceType, Color
import json


class Board:
    def __init__(self):
        self.board = []
        GoSpace = Go(name="Go", color=Color.BLANK, type=SpaceType.GO, rent=200,
                     visitors=[], most_recent_visitor=None)
        JailSpace = Jail(name="Jail", color=Color.BLANK, type=SpaceType.JAIL, rent=0,
                         visitors=[], most_recent_visitor=None)
        FreeParkingSpace = FreeParking(name="Free Parking", color=Color.BLANK, type=SpaceType.FREE_PARKING, rent=0,
                                       visitors=[], most_recent_visitor=None)
        GoToJailSpace = GoToJail(name="Go To Jail", color=Color.BLANK, type=SpaceType.GO_TO_JAIL, rent=0,
                                 visitors=[], most_recent_visitor=None, jail_space=JailSpace)
        property_count = 0
        RR_count = 0
        U_count = 0
        T_count = 0
        # read the board from a file
        with open("../space data/BoardSpaceOrder.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line == "GO":
                    self.board.append(GoSpace)
                    # print(GoSpace)
                elif line == "P":
                    filename = "../space data/property jsons/property" + str(property_count) + ".json"
                    with open(filename, "r") as property_file:
                        property_json = json.load(property_file)
                        p = Property(name=property_json["NAME"], color=property_json["COLOR"], type=SpaceType.PROPERTY,
                                     cost=property_json["PRICE"],
                                     rent={0: property_json["RENT"],
                                           1: property_json["RENT_1"],
                                           2: property_json["RENT_2"],
                                           3: property_json["RENT_3"],
                                           4: property_json["RENT_4"],
                                           5: property_json["RENT_5"]},
                                     mortgage=property_json["MORTGAGE"], house_cost=property_json["HOUSE_PRICE"],
                                     hotel_cost=property_json["HOTEL_PRICE"])
                        p.init_prop()
                        self.board.append(p)
                        property_count += 1
                        # print(p)
                elif line == "CC":
                    cc = CommunityChest(name="Community Chest", color=Color.BLANK, type=SpaceType.COMMUNITY_CHEST,
                                        rent=0, visitors=[], most_recent_visitor=None)
                    self.board.append(cc)
                    # print(cc)
                elif line == "T":
                    filename = "../space data/tax space jsons/tax" + str(T_count) + ".json"
                    with open(filename, "r") as tax_file:
                        tax_json = json.load(tax_file)
                        t = Tax(name=tax_json["NAME"], color=Color.BLANK, type=SpaceType.TAX,
                                rent=tax_json["COST"], visitors=[], most_recent_visitor=None)
                        self.board.append(t)
                        T_count += 1
                        # print(t)
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
                        self.board.append(rr)
                        RR_count += 1
                        # print(rr)
                elif line == "CH":
                    ch = Chance(name="Chance", color=Color.BLANK, type=SpaceType.CHANCE, rent=0,
                                visitors=[], most_recent_visitor=None)
                    self.board.append(ch)
                    # print(ch)
                elif line == "J":
                    self.board.append(JailSpace)
                    # print(JailSpace)
                elif line == "U":
                    filename = "../space data/utility jsons/utility" + str(U_count) + ".json"
                    with open(filename, "r") as utility_file:
                        utility_json = json.load(utility_file)
                        u = Utility(name=utility_json["NAME"], color=Color.BLANK, type=SpaceType.UTILITY,
                                    cost=utility_json["PRICE"], rent={0: 0}, mortgage=utility_json["MORTGAGE"],
                                    house_cost=float('inf'), hotel_cost=float('inf'))
                        self.board.append(u)
                        U_count += 1
                        # print(u)
                elif line == "FP":
                    self.board.append(FreeParkingSpace)
                    # print(FreeParkingSpace)
                elif line == "GJ":
                    self.board.append(GoToJailSpace)
                    # print(GoToJailSpace)
                else:
                    # print("Error: " + line + " is not a valid space")
                    exit()

    def __repr__(self):
        return_string = ""
        for space in self.board:
            return_string += str(space) + "\n"
        return return_string

import json
from random import choice

import Player
from Space import Space


class Chance(Space):

    def land(self, visitor: Player, *args, **kwargs) -> str:
        super().land(visitor, *args, **kwargs)
        with open("../space data/chance jsons/chance.json", "r") as file:
            community_json = json.load(file)
            return choice(community_json["CARD_TEXTS"])

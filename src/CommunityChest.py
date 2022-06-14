import json
from dataclasses import dataclass
from random import choice

import Player
from Space import Space


@dataclass
class CommunityChest(Space):
    visitors: list[Player]
    most_recent_visitor: Player
    owner: Player = None

    def land(self) -> str:
        with open("../space data/community chest jsons/community.json", "r") as file:
            community_json = json.load(file)
            return choice(community_json["CARD_TEXTS"])

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

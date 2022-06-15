import json
from dataclasses import dataclass
from random import choice

import Player
from Space import Space


@dataclass
class CommunityChest(Space):
    visitors: list[Player]
    most_recent_visitor: Player
    # TODO how is most recent visitor updated? When there are no players it also must be set to None right?
    #  Unless it is for sure only ever used when there is a player on the square (lines 21-22 must only be called
    #  if there is a player on the space. I may just be misunderstanding this though so I'm not going to edit anything.
    #  If it does need to be fixed though I think it would prob need to be fixed on all the special Spaces
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
        # TODO Check if visitors is empty and if so set most_recent_visitor to None
        #  (this would lead to error checking in places where most_recent_visitor is used)
        #  maybe im misunderstanding and this isnt necessary, but just want to make sure
        #  the most_recent_visitor is kept up to date
        return self

    def get_visitors(self) -> list[Player]:
        """
        Returns the list of visitors.
        """
        return self.visitors

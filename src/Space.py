from __future__ import annotations

from abc import ABC, abstractmethod
from enums import Color, SpaceType


class Space(ABC):
    type: SpaceType

    @abstractmethod
    def land(self, *args, **kwargs) -> Space:
        pass

    pass

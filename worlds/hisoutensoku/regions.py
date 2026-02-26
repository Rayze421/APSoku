from __future__ import annotations
from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import SokuWorld



def create_and_connect_regions(world: SokuWorld) -> None:
    create_all_regions(world)
#   connect_regions(world)

def create_all_regions(world: SokuWorld) -> None:
    reimu_cards = world.get_region("Reimu Cardsanity")



#def connect_regions(world: SokuWorld) -> None:
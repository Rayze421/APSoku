"""
Archipelago init file for Touhou 12.3 - Hisoutensoku
"""
from typing import List, Dict

from worlds.Autoworld import World
from worlds.LauncherComponents import Component, components, launch_subprocess, Type

from BaseClasses import Item, Location, Region, Tutorial, Multiworld
from worlds.AutoWorld import WebWorld, World
from worlds.generic.Rules import set_rule, forbid_item

from .options import SokuOptions
from .locations import location_table, setup_locations, all_locations, location_groups, lookup_id_to_name, create_region
from .items import item_table, all_items, item_groups
from .world import SokuWorld as SokuWorld

class SokuWorld(World):

    """
    "Touhou 12.3 - Hisoutensoku", often abreviated as "Soku", is a 2009 2D Fighting 
    Game from the Touhou franchise, including a cycling Weather mechanic, 
    Deckbuilding, and a robust projectile system.
    """
    game = "Touhou 12.3 - Hisoutensoku"
    options: SokuOptions
    options_dataclass = SokuOptions

    item_name_groups = item_groups
    location_name_groups = location_groups
    item_name_to_id = all_items
    location_name_to_id = all_locations

    location_table: Dict[str, int]

    def create_regions(self) -> None:
        create_region(self)
        setup_locations(self)
      
        self.location_table = setup_locations(self, self.player)
    



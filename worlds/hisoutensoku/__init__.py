"""
Archipelago init file for Touhou 12.3 - Hisoutensoku
"""
from typing import List, Dict


from worlds.LauncherComponents import Component, components, launch_subprocess, Type

from BaseClasses import Item, Location, Region, Tutorial, MultiWorld
from worlds.AutoWorld import WebWorld, World
from worlds.generic.Rules import set_rule, forbid_item


from .locations import setup_locations, all_locations, location_groups, lookup_id_to_name, create_region
from .items import all_items, item_groups
from . import options as soku_options

class SokuWeb(WebWorld):
    theme = "partyTime"
    option_groups = soku_options.soku_option_groups

class SokuWorld(World):

    """
    "Touhou 12.3 - Hisoutensoku", often abreviated as "Soku", is a 2009 2D Fighting 
    Game from the Touhou franchise, including a cycling Weather mechanic, 
    Deckbuilding, and a robust projectile system.
    """
    game = "Touhou 12.3 - Hisoutensoku"
    options_dataclass = soku_options.SokuOptions
    options: soku_options.SokuOptions

    item_name_groups = item_groups
    location_name_groups = location_groups
    item_name_to_id = all_items
    location_name_to_id = all_locations

    location_table: Dict[str, int]

def create_region(world: SokuWorld) -> None:
    start_region = Region("Start Region", world.player, world.multiworld)
    start_region.locations += [all_locations(lookup_id_to_name)]
    regions = [start_region]

    world.multiworld.regions += regions
    



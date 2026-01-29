"""
Archipelago init file for Touhou 12.3 - Hisoutensoku
"""
from typing import List
from .variables import *

from worlds.Autoworld import World
from worlds.LauncherComponents import Component, components, launch_subprocess, Type

from BaseClasses import Item, Location, Region, Tutorial, Multiworld
from worlds.AutoWorld import WebWorld, World
from worlds.generic.Rules import set_rule, forbid_item

from .options import SokuOptions
from .groups import itemgroups, locationgroups

class Tworld(World):
    game = "Touhou 12.3 - Hisoutensoku"
    options: SokuOptions
    options_dataclass = SokuOptions

    
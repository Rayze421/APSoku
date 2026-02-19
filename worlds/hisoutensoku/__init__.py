"""
Archipelago init file for Touhou 12.3 - Hisoutensoku
"""
from typing import List

from worlds.Autoworld import World
from worlds.LauncherComponents import Component, components, launch_subprocess, Type

from BaseClasses import Item, Location, Region, Tutorial, Multiworld
from worlds.AutoWorld import WebWorld, World
from worlds.generic.Rules import set_rule, forbid_item

from .options import SokuOptions
from .locations import *
from .items import item_table, characters_table, arcade_table, difficulty_table, system_card_table, reimu_skill_table,  reimu_spell_table, \
                   marisa_skill_table, marisa_spell_table, sakuya_skill_table, sakuya_spell_table, alice_skill_table, alice_spell_table, \
                   patchouli_skill_table, patchouli_spell_table, youmu_skill_table, youmu_spell_table, remilia_skill_table, remilia_spell_table, \
                   yuyuko_skill_table, yuyuko_spell_table, yukari_skill_table, yukari_spell_table, suika_skill_table, suika_spell_table, \
                   reisen_skill_table, reisen_spell_table, aya_skill_table, aya_spell_table, komachi_skill_table, komachi_spell_table, \
                   iku_skill_table, iku_spell_table, tenshi_skill_table, tenshi_spell_table, sanae_skill_table, sanae_spell_table, \
                   cirno_skill_table, cirno_spell_table, meiling_skill_table, meiling_spell_table, okuu_skill_table, okuu_spell_table, \
                   suwako_skill_table, suwako_spell_table, filler_table, trap_table, item_groups
from .world import SokuWorld as SokuWorld

class SokuWorld(World):
    game = "Touhou 12.3 - Hisoutensoku"
    options: SokuOptions
    options_dataclass = SokuOptions

    item_name_groups = item_groups

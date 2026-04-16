"""
Archipelago init file for Touhou 12.3 - Hisoutensoku
"""
from typing import List, Dict


from worlds.LauncherComponents import Component, components, launch_subprocess, Type

from BaseClasses import Item, Location, Region, Tutorial, MultiWorld
from worlds.AutoWorld import WebWorld, World
from worlds.generic.Rules import set_rule, forbid_item


from .locations import setup_locations, all_locations, location_groups, lookup_id_to_name, create_region
from .items import all_items, item_groups, item_table
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
    item_name_to_id = {name: data.code for name, data in all_items.items()}
    location_name_to_id = all_locations

    location_table: Dict[str, int]

    def fill_slot_data(self) -> dict:
        return {
            "PlayerNum": self.player,
            "ModVersion": 1,
            "Goal": self.options.goal.value,
            "StoryModeCount": self.options.story_mode_count.value, 
            "ArcadeModeCount": self.options.arcade_mode_count.value,
            "CardCollectorCount": self.options.card_collector_count.value,
            "CardMasterCount": self.options.card_master_count.value,
            "StartingCharacter": self.options.starting_character.value,
            "VSModeWins": self.options.vs_mode_character_wins.value,
            "VSModeWinCount": self.options.vs_mode_win_count.value,
            "StoryChecks": self.options.story_mode_checks.value,
            "StoryStageUnlocks": self.options.story_stage_unlocks.value,
            "ArcadeChecks": self.options.arcade_mode_checks.value,
            "ArcadeStageUnlocks": self.options.arcade_stage_unlocks.value,
            "CardsanitySkills": self.options.cardsanity_skills.value,
            "CardsanitySpells": self.options.cardsanity_spells.value,
            "CardsanitySpellCount": self.options.cardsanity_spell_count.value, 
            "CardsanityStartCards": self.options.cardsanity_starting_cards.value,
            "SystemCardCheckCount": self.options.system_card_check_count.value,
            "SystemCardCharacterChecks": self.options.system_card_character_checks.value,
            "NoDeckLimit": self.options.no_deck_limit.value, 
            "DifficultyItems": self.options.difficulty_items.value,
            "DifficultyStart": self.options.difficulty_start.value,
            "ExcludeLunatic": self.options.exclude_lunatic.value,
            "OnlyLunatic": self.options.only_lunatic.value,

            "CharacterFullBlacklist": self.options.character_full_blacklist.value, 
            "VSBlacklistPlayer": self.options.vs_blacklist_player.value,
            "VSBlacklistOpponent": self.options.vs_blacklist_opponent.value,
            "ArcadeBlacklist": self.options.arcade_mode_blacklist.value,
            "CardsanityBlacklist": self.options.cardsanity_blacklist.value
        }

    def create_region(world: SokuWorld) -> None:
        start_region = Region("Start Region", world.player, world.multiworld)
        start_region.locations += [all_locations(lookup_id_to_name)]
        regions = [start_region]
    
        world.multiworld.regions += regions
    



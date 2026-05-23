"""
Archipelago init file for Touhou 12.3 - Hisoutensoku
"""
from typing import List, Dict


from BaseClasses import Item, Location, Region, Tutorial, MultiWorld
from worlds.AutoWorld import WebWorld, World
from worlds.generic.Rules import set_rule, forbid_item

from .data import itemnames, locationnames


from .locations import setup_locations, all_locations, location_groups, lookup_id_to_name, create_region
from .items import (all_items, item_groups,
                    item_table, characters_table, story_table, arcade_table, difficulty_table,
                    )
from . import options as soku_options

class SokuItem(Item):
    """A Single Item for Hisoutensoku"""
    game: str = "Touhou 12.3 - Hisoutensoku"


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
    
    def create_item(self, name: str) -> SokuItem:
        """Create a single AP Item by name"""
        data = all_items[name]
        return SokuItem(
            name,
            data[1],
            self.item_name_to_id[name],
            self.player,
        )
    
    def create_items(self):
        multiworld = self.multiworld
        player = self.player

        itempool: list[Item] = []


        if self.option.story_mode_checks  == 'Sanae':
            itempool += [self.create_item({itemnames.sanae_story}) for _ in range(5)]
        if self.option.story_mode_checks  == 'Cirno':
            itempool += [self.create_item({itemnames.cirno_story}) for _ in range(5)]
        if self.option.story_mode_checks  == 'Meiling':
            itempool += [self.create_item({itemnames.meiling_story}) for _ in range(5)]
        
        
        itempool += [self.create_item({characters_table.items})] #Add all characters to the pool

        match self.option.starting_character: #Add selected character to Precollected, and remove them from the pool
            case 0: #Reimu
                self.push_precollected(characters_table.reimu)
                itempool.remove[characters_table.reimu]
            case 1: #Marisa
                self.push_precollected(characters_table.marisa)
                itempool.remove[characters_table.marisa]
            case 2: #Sakuya
                self.push_precollected(characters_table.sakuya)
                itempool.remove[characters_table.sakuya]
            case 3: #Alice
                self.push_precollected(characters_table.alice)
                itempool.remove[characters_table.alice]
            case 4: #Patchouli
                self.push_precollected(characters_table.patchouli)
                itempool.remove[characters_table.patchouli]
            case 5: #Youmu
                self.push_precollected(characters_table.youmu)
                itempool.remove[characters_table.youmu]
            case 6: #Remilia
                self.push_precollected(characters_table.remilia)
                itempool.remove[characters_table.remilia]
            case 7: #Yuyuko
                self.push_precollected(characters_table.yuyuko)
                itempool.remove[characters_table.yuyuko]
            case 8: #Yukari
                self.push_precollected(characters_table.yukari)
                itempool.remove[characters_table.yukari]
            case 9: #Suika
                self.push_precollected(characters_table.suika)
                itempool.remove[characters_table.suika]
            case 10: #Reisen
                self.push_precollected(characters_table.reisen)
                itempool.remove[characters_table.reisen]
            case 11: #Aya
                self.push_precollected(characters_table.aya)
                itempool.remove[characters_table.aya]
            case 12: #Komachi
                self.push_precollected(characters_table.komachi)
                itempool.remove[characters_table.komachi]
            case 13: #Iku
                self.push_precollected(characters_table.iku)
                itempool.remove[characters_table.iku]
            case 14: #Tenshi
                self.push_precollected(characters_table.tenshi)
                itempool.remove[characters_table.tenshi]
            case 15: #Sanae
                self.push_precollected(characters_table.sanae)
                itempool.remove[characters_table.sanae]
            case 16: #Cirno
                self.push_precollected(characters_table.cirno)
                itempool.remove[characters_table.cirno]
            case 17: #Meiling
                self.push_precollected(characters_table.meiling)
                itempool.remove[characters_table.meiling]
            case 18: #Utsuho
                self.push_precollected(characters_table.okuu)
                itempool.remove[characters_table.okuu]
            case 19: #Suwako
                self.push_precollected(characters_table.suwako)
                itempool.remove[characters_table.suwako]

        if self.option.arcade_mode_checks == 'True':
            if self.option.arcade_stage_unlocks == 1: #Add Universal Arcade Unlocks
                itempool += [self.create_item({itemnames.arcade_stage}) for _ in range(10)]
            if self.option.arcade_stage_unlocks == 0: #Add Character Specific Arcade Unlocks
                itempool += [self.create_item({
                    arcade_table.alice_arcade,
                    arcade_table.aya_arcade,
                    arcade_table.cirno_arcade,
                    arcade_table.iku_arcade,
                    arcade_table.komachi_arcade,
                    arcade_table.marisa_arcade,
                    arcade_table.meiling_arcade,
                    arcade_table.patchouli_arcade,
                    arcade_table.reimu_arcade,
                    arcade_table.reisen_arcade,
                    arcade_table.remilia_arcade,
                    arcade_table.sakuya_arcade,
                    arcade_table.sanae_arcade,
                    arcade_table.suika_arcade,
                    arcade_table.suwako_arcade,
                    arcade_table.tenshi_arcade,
                    arcade_table.okuu_arcade,
                    arcade_table.youmu_arcade,
                    arcade_table.yukari_arcade,
                    arcade_table.yuyuko_arcade
                    }) for _ in range(9)]
            
        match self.option.cardsanity_skills: #add Skill Cards to the itempool if enabled
            case 1 | 2 | 3:
                itempool += [self.create_item({
                    all_items.reimu_skill_table.items,
                    all_items.marisa_skill_table.items,
                    all_items.sakuya_skill_table.items,
                    all_items.alice_skill_table.items,
                    all_items.patchouli_skill_table.items,
                    all_items.youmu_skill_table.items,
                    all_items.remilia_skill_table.items,
                    all_items.yuyuko_skill_table.items,
                    all_items.yukari_skill_table.items,
                    all_items.suika_skill_table.items,
                    all_items.reisen_skill_table.items,
                    all_items.aya_skill_table.items,
                    all_items.komachi_skill_table.items,
                    all_items.iku_skill_table.items,
                    all_items.tenshi_skill_table.items,
                    all_items.sanae_skill_table.items,
                    all_items.cirno_skill_table.items,
                    all_items.meiling_skill_table.items,
                    all_items.okuu_skill_table.items,
                    all_items.suwako_skill_table.items
                    }) for _ in range(1)]
                    
        if self.option.cardsanity_spells == 1:
            itempool += [self.create_item({
                all_items.reimu_spell_table.items,
                all_items.marisa_spell_table.items,
                all_items.sakuya_spell_table.items,
                all_items.alice_skill_table.items,
                all_items.alice_spell_table.items,
                all_items.patchouli_spell_table.items,
                all_items.youmu_spell_table.items,
                all_items.remilia_spell_table.items,
                all_items.yuyuko_spell_table.items,
                all_items.yukari_spell_table.items,
                all_items.suika_spell_table.items,
                all_items.reisen_spell_table.items,
                all_items.aya_spell_table.items,
                all_items.komachi_spell_table.items,
                all_items.iku_spell_table.items,
                all_items.tenshi_spell_table.items,
                all_items.sanae_spell_table.items,
                all_items.cirno_spell_table.items,
                all_items.meiling_spell_table.items,
                all_items.okuu_spell_table.items
            }) for _ in range(1)]

        



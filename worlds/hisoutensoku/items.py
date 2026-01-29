from typing import Dict, NamedTuple, Optional
from .variables import *

from .charactercards import item_table
from .groups import itemgroups, locationgroups
from BaseClasses import Item, ItemClassification

class TItem(Item):
    game: str = DISPLAY_NAME

class TItemData(NamedTuple):
    category: str
    code: Optional[int] = None
    classification: ItemClassification = ItemClassification.filler
    max_quantity: int = 1
    weight: int = 1

def get_items_by_category(category: str) -> Dict[str, TItemData]:
    item_dict: Dict[str, TItemData] = {}
    for name, data in item_table.items():
        if data.category == category:
            item_dict.setdefault(name, data)

    return item_dict

item_table: Dict[str, TItemData] = {
    # Characters
    "Reimu Hakurei":            TItemData("Characters", STARTING_ID + 0, ItemClassification.progression, 1),
    "Marisa Kirisame":          TItemData("Characters", STARTING_ID + 1, ItemClassification.progression, 1),
    "Sakuya Izayoi":            TItemData("Characters", STARTING_ID + 2, ItemClassification.progression, 1),
    "Alice Margatroid":         TItemData("Characters", STARTING_ID + 3, ItemClassification.progression, 1),
    "Patchouli Knowledge":      TItemData("Characters", STARTING_ID + 4, ItemClassification.progression, 1),
    "Youmu Konpaku":            TItemData("Characters", STARTING_ID + 5, ItemClassification.progression, 1),
    "Remilia Scarlet":          TItemData("Characters", STARTING_ID + 6, ItemClassification.progression, 1),
    "Yuyuko Saigyougi":         TItemData("Characters", STARTING_ID + 7, ItemClassification.progression, 1),
    "Yukari Yakumo":            TItemData("Characters", STARTING_ID + 8, ItemClassification.progression, 1),
    "Suika Ibuki":              TItemData("Characters", STARTING_ID + 9, ItemClassification.progression, 1),
    "Reisen Udongein Inaba":    TItemData("Characters", STARTING_ID + 10, ItemClassification.progression, 1),
    "Aya Shameimaru":           TItemData("Characters", STARTING_ID + 11, ItemClassification.progression, 1),
    "Komachi Onozuka":          TItemData("Characters", STARTING_ID + 12, ItemClassification.progression, 1),
    "Iku Nagae":                TItemData("Characters", STARTING_ID + 13, ItemClassification.progression, 1),
    "Tenshi Hinanawi":          TItemData("Characters", STARTING_ID + 14, ItemClassification.progression, 1),
    "Sanae Kochiya":            TItemData("[Story] Characters", STARTING_ID + 15, ItemClassification.progression, 1),
    "Cirno":                    TItemData("[Story] Characters", STARTING_ID + 16, ItemClassification.progression, 1),
    "Hong Meiling":             TItemData("[Story] Characters", STARTING_ID + 17, ItemClassification.progression, 1),
    "Utsuho Reiuji":            TItemData("Characters", STARTING_ID + 18, ItemClassification.progression, 1),
    "Suwako Moriya":            TItemData("Characters", STARTING_ID + 19, ItemClassification.progression, 1),

    # Story Unlocks
    "Progressive Story Stage":
    "Progressive Sanae Story Stage":
    "Progressive Cirno Story Stage":
    "Progressive Meiling Story Stage":

    # Arcade Unlocks
    "Progressive Arcade Stage":
    "Progressive Alice Arcade Stage":
    "Progressive Aya Arcade Stage":
    "Progressive Ciro Arcade Stage":
    "Progressive Iku Arcade Stage":
    "Progressive Komachi Arcade Stage":
    "Progressive Marisa Arcade Stage":
    "Progressive Meiling Arcade Stage":
    "Progressive Patchouli Arcade Stage":
    "Progressive Reimu Arcade Stage":
    "Progressive Reisen Arcade Stage":
    "Progressive Remilia Arcade Stage":
    "Progressive Sakuya Arcade Stage":
    "Progressive Sanae Arcade Stage":
    "Progressive Suika Arcade Stage":
    "Progressive Suwako Arcade Stage":
    "Progressive Tenshi Arcade Stage":
    "Progressive Utsuho Arcade Stage":
    "Progressive Youmu Arcade Stage":
    "Progressive Yukari Arcade Stage":
    "Progressive Yuyuko Arcade Stage":

    # Filler


    # Traps


}

item_groups: Dict[str, str] = {
    "Characters": [
        "Reimu Hakurei", 
        "Marisa Kirisame", 
        "Sakuya Izayoi",
        "Alice Margatroid",
        "Patchouli Knowledge",
        "Youmu Konpaku",
        "Remilia Scarlet",
        "Yuyuko Saigyougi",
        "Yukari Yakumo",
        "Suika Ibuki",
        "Reisen Udongein Inaba",
        "Aya Shameimaru",
        "Komachi Onozuka",
        "Iku Nagae",
        "Tenshi Hinanawi",
        "Sanae Kochiya",
        "Cirno",
        "Hong Meiling",
        "Utsuho Reiuji",
        "Suwako Moriya"
        ],

    # Card groups

    "Special Cards": [],
    "Spell Cards": [],

    "Reimu Cards": [],
    "Reimu Specials": [],
    "Reimu Spellcards": [],

    "Alice Cards": [],
    "Alice Specials": [],
    "Alice Spellcards": [],

    "Cirno Cards": [],
    "Cirno Specials": [],
    "Cirno Spellcards": [],

    "Iku Cards": [],
    "Iku Specials": [],
    "Iku Spellcards": [],

    "Komachi Cards": [],
    "Komachi Specials": [],
    "Komachi Spellcards": [],

    "Marisa Cards": [],
    "Marisa Specials": [],
    "Marisa Spellcards": [],

    "Meiling Cards": [],
    "Meiling Specials": [],
    "Meiling Spellcards": [],

    "Patchouli Cards": [],
    "Patchouli Specials": [],
    "Patchouli Spellcards": [],

    "Reisen Cards": [],
    "Reisen Specials": [], 
    "Reisen Spellcards": [],

    "Remilia Cards": [],
    "Remilia Specials": [],
    "Remilia Spellcards": [],

    "Sakuya Cards": [],
    "Sakuya Specials": [],
    "Sakuya Spellcards": [],

    "Sanae Cards": [],
    "Sanae Specials": [],
    "Sanae Spellcards": [],

    "Suika Cards": [],
    "Suika Specials": [],
    "Suika Spellcards": [],

    "Suwako Cards": [],
    "Suwako Specials": [],
    "Suwako Spellcards": [],

    "Tenshi Cards": [],
    "Tenshi Specials": [],
    "Tenshi Spellcards": [],

    "Utsuho Cards": [],
    "Utsuho Specials": [],
    "Utsuho Spellcards": [],
    "Oku Cards": [],
    "Oku Specials": [],
    "Oku Spellcards": [],

    "Youmu Cards": [],
    "Youmu Specials": [],
    "Youmu Specials": [],

    "Yukari Cards": [],
    "Yukari Specials": [],
    "Yukari Spellcards": [],

    "Yuyuko Cards": [],
    "Yuyuko Specials": [],
    "Yuyuko Spellcards": [],

}
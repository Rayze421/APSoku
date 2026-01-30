from typing import Dict, NamedTuple, Optional
from .variables import *

from .charactercards import item_table
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
    "Progressive Story Stage":          TItemData("[Universal][Story] Stages", STARTING_ID + 20, ItemClassification.progression, ),
    "Progressive Sanae Story Stage":    TItemData("[Sanae][Individual][Story] Stages", STARTING_ID + 21, ItemClassification.progression, ),
    "Progressive Cirno Story Stage":    TItemData("[Cirno][Individual][Story] Stages", STARTING_ID + 22, ItemClassification.progression, ),
    "Progressive Meiling Story Stage":  TItemData("[Meiling][Individual][Story] Stages", STARTING_ID + 23, ItemClassification.progression, ),

    # Arcade Unlocks
    "Progressive Arcade Stage":           TItemData("[Universal][Arcade] Stages", STARTIND_ID + 24, ItemClassification.progression, 9),
    "Progressive Alice Arcade Stage":     TItemData("[Alice][Individual][Arcade] Stages", STARTIND_ID + 25, ItemClassification.progression, 9),
    "Progressive Aya Arcade Stage":       TItemData("[Aya][Individual][Arcade] Stages", STARTIND_ID + 26, ItemClassification.progression, 9),
    "Progressive Cirno Arcade Stage":      TItemData("[Cirno][Individual][Arcade] Stages", STARTIND_ID + 27, ItemClassification.progression, 9),
    "Progressive Iku Arcade Stage":       TItemData("[Iku][Individual][Arcade] Stages", STARTIND_ID + 28, ItemClassification.progression, 9),
    "Progressive Komachi Arcade Stage":   TItemData("[Komachi][Individual][Arcade] Stages", STARTIND_ID + 29, ItemClassification.progression, 9),
    "Progressive Marisa Arcade Stage":    TItemData("[Marisa][Individual][Arcade] Stages", STARTIND_ID + 30, ItemClassification.progression, 9),
    "Progressive Meiling Arcade Stage":   TItemData("[Meiling][Individual][Arcade] Stages", STARTIND_ID + 31, ItemClassification.progression, 9),
    "Progressive Patchouli Arcade Stage": TItemData("[Patchouli][Individual][Arcade] Stages", STARTIND_ID + 32, ItemClassification.progression, 9),
    "Progressive Reimu Arcade Stage":     TItemData("[Reimu][Individual][Arcade] Stages", STARTIND_ID + 33, ItemClassification.progression, 9),
    "Progressive Reisen Arcade Stage":    TItemData("[Reisen][Individual][Arcade] Stages", STARTIND_ID + 34, ItemClassification.progression, 9),
    "Progressive Remilia Arcade Stage":   TItemData("[Remilia][Individual][Arcade] Stages", STARTIND_ID + 35, ItemClassification.progression, 9), 
    "Progressive Sakuya Arcade Stage":    TItemData("[Sakuya][Individual][Arcade] Stages", STARTIND_ID + 36, ItemClassification.progression, 9),
    "Progressive Sanae Arcade Stage":     TItemData("[Sanae][Individual][Arcade] Stages", STARTIND_ID + 37, ItemClassification.progression, 9),
    "Progressive Suika Arcade Stage":     TItemData("[Suika][Individual][Arcade] Stages", STARTIND_ID + 38, ItemClassification.progression, 9),
    "Progressive Suwako Arcade Stage":    TItemData("[Suwako][Individual][Arcade] Stages", STARTIND_ID + 39, ItemClassification.progression, 9),
    "Progressive Tenshi Arcade Stage":    TItemData("[Tenshi][Individual][Arcade] Stages", STARTIND_ID + 40, ItemClassification.progression, 9),
    "Progressive Utsuho Arcade Stage":    TItemData("[Utsuho][Individual][Arcade] Stages", STARTIND_ID + 41, ItemClassification.progression, 9),
    "Progressive Youmu Arcade Stage":     TItemData("[Youmu][Individual][Arcade] Stages", STARTIND_ID + 42, ItemClassification.progression, 9),
    "Progressive Yukari Arcade Stage":    TItemData("[Yukari][Individual][Arcade] Stages", STARTIND_ID + 43, ItemClassification.progression, 9),
    "Progressive Yuyuko Arcade Stage":    TItemData("[Yuyuko][Individual][Arcade] Stages", STARTIND_ID + 44, ItemClassification.progression, 9),

    # Misc
    "Lower Difficulty":        TItemData("[Progressive Lower] Difficulty", STARTING_ID + 45, ItemClassification.useful, 3),
    "Higher Difficulty":       TItemData("[Progressive Higher] Difficulty", STARTING_ID + 46, ItemClassification.useful, 3),
    "Easy Difficulty":         TItemData("[DIndividual] Difficulty", STARTING_ID + 47, ItemClassification.useful, 1),
    "Medium Difficulty":       TItemData("[DIndividual] Difficulty", STARTING_ID + 48, ItemClassification.useful, 1),
    "Hard Difficulty":         TItemData("[DIndividual] Difficulty", STARTING_ID + 49, ItemClassification.useful, 1),
    "Lunatic Difficulty":      TItemData("[DIndividual][Lunatic] Difficulty", STARTING_ID + 50, ItemClassification.useful, 1),


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
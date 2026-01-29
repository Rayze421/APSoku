from typing import Dict, NamedTuple, Optional
from .variables import *

from BaseClasses import Item, ItemClassification

class TItem(Item):
    game: str = "Touhou 12.3 - Hisoutensoku"


reimu_cards: Dict[str, TItemData] = {
    #236X

    "Reimu 236: Hakurei Amulet": TItemData("[Reimu][Special][236] Cards", STARTING_ID + 50, ItemClassification.useful),
    "Reimu 236: Youkai Buster": TItemData("[Reimu][Special][236] Cards", STARTING_ID + 50, ItemClassification.useful),
    "Reimu 236: Spread Amulet": TItemData("[Reimu][Special][236] Cards", STARTING_ID + 50, ItemClassification.useful),

    #623X

    "Reimu 623: Ascension Kick": TItemData("[Reimu][Special][623] Cards", STARTING_ID + 50, ItemClassification.useful),
    "Reimu 623: Sliding Ascension Kick": TItemData("[Reimu][Special][623] Cards", STARTING_ID + 50, ItemClassification.useful),
    "Reimu 623 Rain Dance": TItemData("[Reimu][Special][623] Cards", STARTING_ID + 50, ItemClassification.useful),

    #214

    "Reimu 214: Cautionary Border": TItemData("[Reimu][Special][214] Cards", STARTING_ID + 50, ItemClassification.useful),
    "Reimu 214: Binding Border": TItemData("[Reimu][Special][214] Cards", STARTING_ID + 50, ItemClassification.useful),
    "Reimu 214: Permanent Border": TItemData("[Reimu][Special][214] Cards", STARTING_ID + 50, ItemClassification.useful),

    #421

    "Reimu 421: Dimensional Rift": TItemData("[Reimu][Special][421] Cards", STARTING_ID + 50, ItemClassification.useful),
    "Reimu 421: Demon Sealing Dimensional Rift": TItemData("[Reimu][Special][421] Cards", STARTING_ID + 50, ItemClassification.useful),
    "Reimu 421: Instant Dimensional Rift": TItemData("[Reimu][Special][421] Cards", STARTING_ID + 50, ItemClassification.useful),

    #Spell Cards

    'Reimu 1SC: Jewel Sign "Concealed Orbs of Light"': TItemData("Reimu][Spell][1SC] Cards", STARTING_ID + 50, ItemClassification.useful),
    'Reimu 2SC: Spirit Sign "Fantasy Orb"': TItemData("Reimu][Spell][2SC] Cards", STARTING_ID + 50, ItemClassification.useful),
    'Reimu 2SC: Dream Sign "Demon Binding Array"': TItemData("Reimu][Spell][2SC] Cards", STARTING_ID + 50, ItemClassification.useful),
    'Reimu 2SC: Treasure Sign "Ying-Yang Orb"': TItemData("Reimu][Spell][2SC] Cards", STARTING_ID + 50, ItemClassification.useful),
    'Reimu 3SC: Boundary "Expanding Boundary"': TItemData("Reimu][Spell][3SC] Cards", STARTING_ID + 50, ItemClassification.useful),
    'Reimu 3SC: Divine Arts "Wind God Kick"': TItemData("Reimu][Spell][3SC] Cards", STARTING_ID + 50, ItemClassification.useful),
    'Reimu 4SC: Divine Arts "Demon Binding Circle"': TItemData("Reimu][Spell][4SC] Cards", STARTING_ID + 50, ItemClassification.useful),
    'Reimu 4SC: Holy Relic "Ying Yang Sanctifier Orb"': TItemData("Reimu][Spell][4SC] Cards", STARTING_ID + 50, ItemClassification.useful),
    'Reimu 5SC: Divine Spirit "Fantasy Seal"': TItemData("Reimu][Spell][5SC] Cards", STARTING_ID + 50, ItemClassification.useful),
    'Reimu 5SC: "Fantasy Heaven"': TItemData("Reimu][Spell][5SC] Cards", STARTING_ID + 50, ItemClassification.useful)
}
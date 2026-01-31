from typing import Dict, NamedTuple, Optional
from .variables import *
from .data import itemnames
from BaseClasses import Item, ItemClassification

class SokuItem(Item):
    game = "Touhou 12.3 - Hisoutensoku"

class SokuItemData(NamedTuple):
    category: str
    code: Optional[int] = None
    classification: ItemClassification = ItemClassification.filler

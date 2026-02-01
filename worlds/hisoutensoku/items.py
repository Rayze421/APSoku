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


characters_table = {
    itemnames.reimu: SokuItemData(1230001, ItemClassification.progression),
    itemnames.marisa: SokuItemData(1230002, ItemClassification.progression),
    itemnames.sakuya: SokuItemData(1230003, ItemClassification.progression),
    itemnames.alice: SokuItemData(1230004, ItemClassification.progression),
    itemnames.patchouli: SokuItemData(1230005, ItemClassification.progression),
    itemnames.youmu: SokuItemData(1230006, ItemClassification.progression),
    itemnames.remilia: SokuItemData(1230007, ItemClassification.progression),
    itemnames.yuyuko: SokuItemData(1230008, ItemClassification.progression),
    itemnames.yukari: SokuItemData(1230009, ItemClassification.progression),
    itemnames.suika: SokuItemData(1230010, ItemClassification.progression),
    itemnames.reisen: SokuItemData(1230011, ItemClassification.progression),
    itemnames.aya: SokuItemData(1230012, ItemClassification.progression),
    itemnames.komachi: SokuItemData(1230013, ItemClassification.progression),
    itemnames.iku: SokuItemData(1230014, ItemClassification.progression),
    itemnames.tenshi: SokuItemData(1230015, ItemClassification.progression),
    itemnames.sanae: SokuItemData(1230016, ItemClassification.progression),
    itemnames.cirno: SokuItemData(1230017, ItemClassification.progression),
    itemnames.meiling: SokuItemData(1230018, ItemClassification.progression),
    itemnames.okuu: SokuItemData(1230019, ItemClassification.progression),
    itemnames.suwako: SokuItemData(1230020, ItemClassification.progression),

    itemnames.sanae_story: SokuItemData(1230021, ItemClassification.progression),
    itemnames.cirno_story: SokuItemData(1230022, ItemClassification.progression),
    itemnames.meiling_story: SokuItemData(1230023, ItemClassification.progression)

}
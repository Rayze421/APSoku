from typing import Dict, NamedTuple, Optional
from .variables import *
from .data import itemnames
from BaseClasses import Item, ItemClassification

class SokuItem(Item):
    game: str = "Touhou 12.3 - Hisoutensoku"

class SokuItemData(NamedTuple):
    category: str
    code: Optional[int] = None
    classification: ItemClassification = ItemClassification.filler

#Item ID's in hexadecimal bc it makes me feel smart
characters_table = {
    #Character IDs Range 0xFF0001-FF0014
    itemnames.reimu: SokuItemData(0xFF0001, ItemClassification.progression),
    itemnames.marisa: SokuItemData(0xFF0002, ItemClassification.progression),
    itemnames.sakuya: SokuItemData(0xFF0003, ItemClassification.progression),
    itemnames.alice: SokuItemData(0xFF0004, ItemClassification.progression),
    itemnames.patchouli: SokuItemData(0xFF0005, ItemClassification.progression),
    itemnames.youmu: SokuItemData(0xFF0006, ItemClassification.progression),
    itemnames.remilia: SokuItemData(0xFF0007, ItemClassification.progression),
    itemnames.yuyuko: SokuItemData(0xFF0008, ItemClassification.progression),
    itemnames.yukari: SokuItemData(0xFF0009, ItemClassification.progression),
    itemnames.suika: SokuItemData(0xFF000A, ItemClassification.progression),
    itemnames.reisen: SokuItemData(0xFF000B, ItemClassification.progression),
    itemnames.aya: SokuItemData(0xFF000C, ItemClassification.progression),
    itemnames.komachi: SokuItemData(0xFF000D, ItemClassification.progression),
    itemnames.iku: SokuItemData(0xFF000E, ItemClassification.progression),
    itemnames.tenshi: SokuItemData(0xFF000F, ItemClassification.progression),
    itemnames.sanae: SokuItemData(0xFF0010, ItemClassification.progression),
    itemnames.cirno: SokuItemData(0xFF0011, ItemClassification.progression),
    itemnames.meiling: SokuItemData(0xFF0012, ItemClassification.progression),
    itemnames.okuu: SokuItemData(0xFF0013, ItemClassification.progression), #Utsuho, also affectionately reffered to as "Okuu"
    itemnames.suwako: SokuItemData(0xFF0014, ItemClassification.progression),
    
    #Story Character IDs Range 0xFF0015-FF0017
    itemnames.sanae_story: SokuItemData(0xFF0015, ItemClassification.progression),
    itemnames.cirno_story: SokuItemData(0xFF0016, ItemClassification.progression),
    itemnames.meiling_story: SokuItemData(0xFF0017, ItemClassification.progression)

}

arcade_table = { #Arcade IDs Range 0xFF0020-FF0034
    itemnames.arcade_stage: SokuItemData(0xFF0020, ItemClassification.progression),
    itemnames.alice_arcade: SokuItemData(0xFF0021, ItemClassification.progression),
    itemnames.aya_arcade: SokuItemData(0xFF0022, ItemClassification.progression),
    itemnames.cirno_arcade: SokuItemData(0xFF0023, ItemClassification.progression),
    itemnames.iku_arcade: SokuItemData(0xFF0024, ItemClassification.progression),
    itemnames.komachi_arcade: SokuItemData(0xFF0025, ItemClassification.progression),
    itemnames.marisa_arcade: SokuItemData(0xFF0026, ItemClassification.progression),
    itemnames.meiling_arcade: SokuItemData(0xFF0027, ItemClassification.progression),
    itemnames.patchouli_arcade: SokuItemData(0xFF0028, ItemClassification.progression),
    itemnames.reimu_arcade: SokuItemData(0xFF0029, ItemClassification.progression),
    itemnames.reisen_arcade: SokuItemData(0xFF002A, ItemClassification.progression),
    itemnames.remilia_arcade: SokuItemData(0xFF002B, ItemClassification.progression),
    itemnames.sakuya_arcade: SokuItemData(0xFF002C, ItemClassification.progression),
    itemnames.sanae_arcade: SokuItemData(0xFF002D, ItemClassification.progression),
    itemnames.suika_arcade: SokuItemData(0xFF002E, ItemClassification.progression),
    itemnames.suwako_arcade: SokuItemData(0xFF002F, ItemClassification.progression), 
    itemnames.tenshi_arcade: SokuItemData(0xFF0030, ItemClassification.progression),
    itemnames.okuu_arcade: SokuItemData(0xFF0031, ItemClassification.progression), #Utsuho, also affectionately reffered to as "Okuu"
    itemnames.youmu_arcade: SokuItemData(0xFF0032, ItemClassification.progression),
    itemnames.yukari_arcade: SokuItemData(0xFF0033, ItemClassification.progression),
    itemnames.yuyuko_arcade: SokuItemData(0xFF0034, ItemClassification.progression)
}

difficulty_table = { #Difficulty IDs Range 0xFF000-FF005
    itemnames.lower_diff: SokuItemData(0xFF000, ItemClassification.useful),
    itemnames.higher_diff: SokuItemData(0XFF001, ItemClassification.useful),
    itemnames.easy_diff: SokuItemData(0xFF002, ItemClassification.useful),
    itemnames.medium_diff: SokuItemData(0xFF003, ItemClassification.useful),
    itemnames.hard_diff: SokuItemData(0xFF004, ItemClassification.useful),
    itemnames.lunatic_diff: SokuItemData(0xFF005, ItemClassification.useful),
}

system_card_table = {
    itemnames.sys_talisman: SokuItemData(0xFF0035, ItemClassification.progression),
    itemnames.sys_potion: SokuItemData(0xFF0036, ItemClassification.progression),
    itemnames.sys_stopwatch: SokuItemData(0xFF0037, ItemClassification.progression),
    itemnames.sys_haku: SokuItemData(0xFF0038, ItemClassification.progression),
    itemnames.sys_doll: SokuItemData(0xFF0039, ItemClassification.progression),
    itemnames.sys_grimoire: SokuItemData(0xFF0040, ItemClassification.progression),
    itemnames.sys_parasol: SokuItemData(0xFF0041, ItemClassification.progression),
    itemnames.sys_torch: SokuItemData(0xFF0042, ItemClassification.progression),
    itemnames.sys_folding: SokuItemData(0xFF0043, ItemClassification.progression),
    itemnames.sys_gourd: SokuItemData(0xFF0044, ItemClassification.progression),
    itemnames.sys_fan: SokuItemData(0xFF0045, ItemClassification.progression),
    itemnames.sys_drug: SokuItemData(0xFF0046, ItemClassification.progression),
    itemnames.sys_coin: SokuItemData(0xFF0047, ItemClassification.progression),
    itemnames.sys_raiment: SokuItemData(0xFF0048, ItemClassification.progression),
    itemnames.sys_sword: SokuItemData(0xFF0049, ItemClassification.progression),
    itemnames.sys_charm: SokuItemData(0xFF0050, ItemClassification.progression),
    itemnames.sys_frog: SokuItemData(0xFF0051, ItemClassification.progression),
    itemnames.sys_star: SokuItemData(0xFF0052, ItemClassification.progression),
    itemnames.sys_rod: SokuItemData(0xFF0053, ItemClassification.progression),
    itemnames.sys_drops: SokuItemData(0xFF0054, ItemClassification.progression),
    itemnames.sys_fish: SokuItemData(0xFF0055, ItemClassification.progression),

}

reimu_skill_table = {
    itemnames.reimu_236d: SokuItemData(0xFF0100, ItemClassification.progression),
    itemnames.reimu_236a1: SokuItemData(0xFF0101, ItemClassification.progression),
    itemnames.reimu_236a2: SokuItemData(0xFF0102, ItemClassification.progression),
    itemnames.reimu_623d: SokuItemData(0xFF0103, ItemClassification.progression),
    itemnames.reimu_623a1: SokuItemData(0xFF0104, ItemClassification.progression),
    itemnames.reimu_623a2: SokuItemData(0xFF0105, ItemClassification.progression),
    itemnames.reimu_214d: SokuItemData(0xFF0106, ItemClassification.progression),
    itemnames.reimu_214a1: SokuItemData(0xFF0107, ItemClassification.progression),
    itemnames.reimu_214a2: SokuItemData(0xFF0108, ItemClassification.progression),
    itemnames.reimu_421d: SokuItemData(0xFF0109, ItemClassification.progression),
    itemnames.reimu_421a1: SokuItemData(0xFF0110, ItemClassification.progression),
    itemnames.reimu_421a2: SokuItemData(0xFF0111, ItemClassification.progression),

}

reimu_spell_table = {
    itemnames.reimu_1sc: SokuItemData(0xFF0112, ItemClassification.progression),
    itemnames.reimu_2sc_fo: SokuItemData(0xFF0113, ItemClassification.progression),
    itemnames.reimu_2sc_dba: SokuItemData(0xFF0114, ItemClassification.progression),
    itemnames.reimu_2sc_yyo: SokuItemData(0xFF0115, ItemClassification.progression),
    itemnames.reimu_3sc_eb: SokuItemData(0xFF0116, ItemClassification.progression),
    itemnames.reimu_3sc_wgk: SokuItemData(0xFF0117, ItemClassification.progression),
    itemnames.reimu_4sc_dbc: SokuItemData(0xFF0118, ItemClassification.progression),
    itemnames.reimu_4sc_yyso: SokuItemData(0xFF0119, ItemClassification.progression),
    itemnames.reimu_5sc_fs: SokuItemData(0xFF0120, ItemClassification.progression),
    itemnames.reimu_5sc_fh: SokuItemData(0xFF0121, ItemClassification.progression),

}

marisa_card_table = {

}

sakuya_card_table = {

}

alice_card_table = {

}

patchouli_card_table = {

}

youmu_card_table = {

}

remilia_card_table = {

}

yuyuko_card_table = {

}
yukari_card_table = {

}

suika_card_table = {

}

reisen_card_table = {

}

aya_card_table = {

}

komachi_card_table = {

}

iku_card_table = {

}

tenshi_card_table = {

}

sanae_card_table = {

}

cirno_card_table = {

}

meiling_card_table = {

}

okuu_card_table = { #Utsuho, also affectionately reffered to as "Okuu"

}

suwako_card_table = {

}

filler_table = {

}

trap_table = {

}

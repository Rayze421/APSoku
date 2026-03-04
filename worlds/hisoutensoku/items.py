from typing import Dict, NamedTuple, Optional, TYPE_CHECKING
from .data import itemnames
from worlds.AutoWorld import World
from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import SokuWorld

class SokuItem(Item):
    game: str = "Touhou 12.3 - Hisoutensoku"

class SokuItemData(NamedTuple):
    category: str
    code: Optional[int] = None
    classification: ItemClassification = ItemClassification.filler

#Item ID's in hexadecimal bc it makes me feel smart and this games sheer size will probably warrant it as far as sorting goes
characters_table = {
    #Character IDs Range 0xFF0001-FF0014
    itemnames.reimu:      SokuItemData(0xFF0001, ItemClassification.progression),
    itemnames.marisa:     SokuItemData(0xFF0002, ItemClassification.progression),
    itemnames.sakuya:     SokuItemData(0xFF0003, ItemClassification.progression),
    itemnames.alice:      SokuItemData(0xFF0004, ItemClassification.progression),
    itemnames.patchouli:  SokuItemData(0xFF0005, ItemClassification.progression),
    itemnames.youmu:      SokuItemData(0xFF0006, ItemClassification.progression),
    itemnames.remilia:    SokuItemData(0xFF0007, ItemClassification.progression),
    itemnames.yuyuko:     SokuItemData(0xFF0008, ItemClassification.progression),
    itemnames.yukari:     SokuItemData(0xFF0009, ItemClassification.progression),
    itemnames.suika:      SokuItemData(0xFF000A, ItemClassification.progression),
    itemnames.reisen:     SokuItemData(0xFF000B, ItemClassification.progression),
    itemnames.aya:        SokuItemData(0xFF000C, ItemClassification.progression),
    itemnames.komachi:    SokuItemData(0xFF000D, ItemClassification.progression),
    itemnames.iku:        SokuItemData(0xFF000E, ItemClassification.progression),
    itemnames.tenshi:     SokuItemData(0xFF000F, ItemClassification.progression),
    itemnames.sanae:      SokuItemData(0xFF0010, ItemClassification.progression),
    itemnames.cirno:      SokuItemData(0xFF0011, ItemClassification.progression),
    itemnames.meiling:    SokuItemData(0xFF0012, ItemClassification.progression),
    itemnames.okuu:       SokuItemData(0xFF0013, ItemClassification.progression), #Utsuho, also affectionately reffered to as "Okuu"
    itemnames.suwako:     SokuItemData(0xFF0014, ItemClassification.progression),
}

story_table = {
    #Story Character IDs Range 0xFF0015-FF0017
    itemnames.sanae_story:    SokuItemData(0xFF0015, ItemClassification.progression),
    itemnames.cirno_story:    SokuItemData(0xFF0016, ItemClassification.progression),
    itemnames.meiling_story:  SokuItemData(0xFF0017, ItemClassification.progression)

}

arcade_table = { #Arcade IDs Range 0xFF0020-FF0034
    itemnames.arcade_stage:     SokuItemData(0xFF0020, ItemClassification.progression),
    itemnames.alice_arcade:     SokuItemData(0xFF0021, ItemClassification.progression),
    itemnames.aya_arcade:       SokuItemData(0xFF0022, ItemClassification.progression),
    itemnames.cirno_arcade:     SokuItemData(0xFF0023, ItemClassification.progression),
    itemnames.iku_arcade:       SokuItemData(0xFF0024, ItemClassification.progression),
    itemnames.komachi_arcade:   SokuItemData(0xFF0025, ItemClassification.progression),
    itemnames.marisa_arcade:    SokuItemData(0xFF0026, ItemClassification.progression),
    itemnames.meiling_arcade:   SokuItemData(0xFF0027, ItemClassification.progression),
    itemnames.patchouli_arcade: SokuItemData(0xFF0028, ItemClassification.progression),
    itemnames.reimu_arcade:     SokuItemData(0xFF0029, ItemClassification.progression),
    itemnames.reisen_arcade:    SokuItemData(0xFF002A, ItemClassification.progression),
    itemnames.remilia_arcade:   SokuItemData(0xFF002B, ItemClassification.progression),
    itemnames.sakuya_arcade:    SokuItemData(0xFF002C, ItemClassification.progression),
    itemnames.sanae_arcade:     SokuItemData(0xFF002D, ItemClassification.progression),
    itemnames.suika_arcade:     SokuItemData(0xFF002E, ItemClassification.progression),
    itemnames.suwako_arcade:    SokuItemData(0xFF002F, ItemClassification.progression), 
    itemnames.tenshi_arcade:    SokuItemData(0xFF0030, ItemClassification.progression),
    itemnames.okuu_arcade:      SokuItemData(0xFF0031, ItemClassification.progression), #Utsuho, also affectionately reffered to as "Okuu"
    itemnames.youmu_arcade:     SokuItemData(0xFF0032, ItemClassification.progression),
    itemnames.yukari_arcade:    SokuItemData(0xFF0033, ItemClassification.progression),
    itemnames.yuyuko_arcade:    SokuItemData(0xFF0034, ItemClassification.progression)
}

difficulty_table = { #Difficulty IDs Range 0xFF000-FF005
    itemnames.lower_diff:   SokuItemData(0xFF000, ItemClassification.useful),
    itemnames.higher_diff:  SokuItemData(0XFF001, ItemClassification.useful),
    itemnames.easy_diff:    SokuItemData(0xFF002, ItemClassification.useful),
    itemnames.medium_diff:  SokuItemData(0xFF003, ItemClassification.useful),
    itemnames.hard_diff:    SokuItemData(0xFF004, ItemClassification.useful),
    itemnames.lunatic_diff: SokuItemData(0xFF005, ItemClassification.useful),
}

system_card_table = {
    itemnames.sys_talisman:   SokuItemData(0xFF0035, ItemClassification.progression),
    itemnames.sys_potion:     SokuItemData(0xFF0036, ItemClassification.progression),
    itemnames.sys_stopwatch:  SokuItemData(0xFF0037, ItemClassification.progression),
    itemnames.sys_haku:       SokuItemData(0xFF0038, ItemClassification.progression),
    itemnames.sys_doll:       SokuItemData(0xFF0039, ItemClassification.progression),
    itemnames.sys_grimoire:   SokuItemData(0xFF003A, ItemClassification.progression),
    itemnames.sys_parasol:    SokuItemData(0xFF003B, ItemClassification.progression),
    itemnames.sys_torch:      SokuItemData(0xFF003C, ItemClassification.progression),
    itemnames.sys_folding:    SokuItemData(0xFF003D, ItemClassification.progression),
    itemnames.sys_gourd:      SokuItemData(0xFF003E, ItemClassification.progression),
    itemnames.sys_fan:        SokuItemData(0xFF003F, ItemClassification.progression),
    itemnames.sys_drug:       SokuItemData(0xFF0040, ItemClassification.progression),
    itemnames.sys_coin:       SokuItemData(0xFF0041, ItemClassification.progression),
    itemnames.sys_raiment:    SokuItemData(0xFF0042, ItemClassification.progression),
    itemnames.sys_sword:      SokuItemData(0xFF0043, ItemClassification.progression),
    itemnames.sys_charm:      SokuItemData(0xFF0044, ItemClassification.progression),
    itemnames.sys_frog:       SokuItemData(0xFF0045, ItemClassification.progression),
    itemnames.sys_star:       SokuItemData(0xFF0046, ItemClassification.progression),
    itemnames.sys_rod:        SokuItemData(0xFF0047, ItemClassification.progression),
    itemnames.sys_drops:      SokuItemData(0xFF0048, ItemClassification.progression),
    itemnames.sys_fish:       SokuItemData(0xFF0049, ItemClassification.progression),

}

reimu_skill_table = {
    itemnames.reimu_236d:  SokuItemData(0xFF0100, ItemClassification.progression),
    itemnames.reimu_236a1: SokuItemData(0xFF0101, ItemClassification.progression),
    itemnames.reimu_236a2: SokuItemData(0xFF0102, ItemClassification.progression),
    itemnames.reimu_623d:  SokuItemData(0xFF0103, ItemClassification.progression),
    itemnames.reimu_623a1: SokuItemData(0xFF0104, ItemClassification.progression),
    itemnames.reimu_623a2: SokuItemData(0xFF0105, ItemClassification.progression),
    itemnames.reimu_214d:  SokuItemData(0xFF0106, ItemClassification.progression),
    itemnames.reimu_214a1: SokuItemData(0xFF0107, ItemClassification.progression),
    itemnames.reimu_214a2: SokuItemData(0xFF0108, ItemClassification.progression),
    itemnames.reimu_421d:  SokuItemData(0xFF0109, ItemClassification.progression),
    itemnames.reimu_421a1: SokuItemData(0xFF010A, ItemClassification.progression),
    itemnames.reimu_421a2: SokuItemData(0xFF010B, ItemClassification.progression),

}

reimu_spell_table = {
    itemnames.reimu_1sc:      SokuItemData(0xFF010C, ItemClassification.progression),
    itemnames.reimu_2sc_fo:   SokuItemData(0xFF010D, ItemClassification.progression),
    itemnames.reimu_2sc_dba:  SokuItemData(0xFF010E, ItemClassification.progression),
    itemnames.reimu_2sc_yyo:  SokuItemData(0xFF010F, ItemClassification.progression),
    itemnames.reimu_3sc_eb:   SokuItemData(0xFF0110, ItemClassification.progression),
    itemnames.reimu_3sc_wgk:  SokuItemData(0xFF0111, ItemClassification.progression),
    itemnames.reimu_4sc_dbc:  SokuItemData(0xFF0112, ItemClassification.progression),
    itemnames.reimu_4sc_yyso: SokuItemData(0xFF0113, ItemClassification.progression),
    itemnames.reimu_5sc_fs:   SokuItemData(0xFF0114, ItemClassification.progression),
    itemnames.reimu_5sc_fh:   SokuItemData(0xFF0115, ItemClassification.progression),

}

marisa_skill_table = {
    itemnames.marisa_236d:   SokuItemData(0xFF0200, ItemClassification.progression),
    itemnames.marisa_236a1:  SokuItemData(0xFF0201, ItemClassification.progression),
    itemnames.marisa_236a2:  SokuItemData(0xFF0202, ItemClassification.progression),
    itemnames.marisa_623d:   SokuItemData(0xFF0203, ItemClassification.progression),
    itemnames.marisa_623a1:  SokuItemData(0xFF0204, ItemClassification.progression),
    itemnames.marisa_623a2:  SokuItemData(0xFF0205, ItemClassification.progression),
    itemnames.marisa_214d:   SokuItemData(0xFF0206, ItemClassification.progression),
    itemnames.marisa_214a1:  SokuItemData(0xFF0207, ItemClassification.progression),
    itemnames.marisa_214a2:  SokuItemData(0xFF0208, ItemClassification.progression),
    itemnames.marisa_22d:    SokuItemData(0xFF0209, ItemClassification.progression),
    itemnames.marisa_22a1:   SokuItemData(0xFF020A, ItemClassification.progression),
    itemnames.marisa_22a2:   SokuItemData(0xFF020B, ItemClassification.progression),

}

marisa_spell_table = {    
    itemnames.marisa_1sc_ms:   SokuItemData(0xFF020C, ItemClassification.progression),
    itemnames.marisa_2sc_sr:   SokuItemData(0xFF020D, ItemClassification.progression),
    itemnames.marisa_2sc_ls:   SokuItemData(0xFF020E, ItemClassification.progression),
    itemnames.marisa_2sc_os:   SokuItemData(0xFF020F, ItemClassification.progression),
    itemnames.marisa_3sc_ms:   SokuItemData(0xFF0210, ItemClassification.progression),
    itemnames.marisa_3sc_ev:   SokuItemData(0xFF0211, ItemClassification.progression),
    itemnames.marisa_3sc_gb:   SokuItemData(0xFF0212, ItemClassification.progression),
    itemnames.marisa_3sc_er:   SokuItemData(0xFF0213, ItemClassification.progression),
    itemnames.marisa_4sc_ndl:  SokuItemData(0xFF0224, ItemClassification.progression),
    itemnames.marisa_4sc_deb:  SokuItemData(0xFF0225, ItemClassification.progression),
    itemnames.marisa_5sc_fs:   SokuItemData(0xFF0226, ItemClassification.progression),
    itemnames.marisa_5sc_dm:   SokuItemData(0xFF0227, ItemClassification.progression),
    itemnames.marisa_5sc_bs:   SokuItemData(0xFF0228, ItemClassification.progression),
    itemnames.marisa_5sc_sfms: SokuItemData(0xFF0229, ItemClassification.progression),
}

sakuya_skill_table = {
    itemnames.sakuya_236d:  SokuItemData(0xFF0300, ItemClassification.progression),
    itemnames.sakuya_236a1: SokuItemData(0xFF0301, ItemClassification.progression),
    itemnames.sakuya_236a2: SokuItemData(0xFF0302, ItemClassification.progression),
    itemnames.sakuya_623d:  SokuItemData(0xFF0303, ItemClassification.progression),
    itemnames.sakuya_623a1: SokuItemData(0xFF0304, ItemClassification.progression),
    itemnames.sakuya_623a2: SokuItemData(0xFF0305, ItemClassification.progression),
    itemnames.sakuya_214d:  SokuItemData(0xFF0306, ItemClassification.progression),
    itemnames.sakuya_214a1: SokuItemData(0xFF0307, ItemClassification.progression),
    itemnames.sakuya_214a2: SokuItemData(0xFF0308, ItemClassification.progression),
    itemnames.sakuya_22d:   SokuItemData(0xFF0309, ItemClassification.progression),
    itemnames.sakuya_22a1:  SokuItemData(0xFF030A, ItemClassification.progression),
    itemnames.sakuya_22a2:  SokuItemData(0xFF030B, ItemClassification.progression),

}

sakuya_spell_table = {
    itemnames.sakuya_2sc_kd:   SokuItemData(0xFF030C, ItemClassification.progression),
    itemnames.sakuya_2sc_sb:   SokuItemData(0xFF030D, ItemClassification.progression),
    itemnames.sakuya_2sc_em:   SokuItemData(0xFF030E, ItemClassification.progression),
    itemnames.sakuya_3sc_ps:   SokuItemData(0xFF030F, ItemClassification.progression),
    itemnames.sakuya_3sc_irs:  SokuItemData(0xFF0310, ItemClassification.progression),
    itemnames.sakuya_3sc_lr:   SokuItemData(0xFF0311, ItemClassification.progression),
    itemnames.sakuya_3sc_ivt:  SokuItemData(0xFF0312, ItemClassification.progression),
    itemnames.sakuya_3sc_ld:   SokuItemData(0xFF0313, ItemClassification.progression),
    itemnames.sakuya_4sc_pk:   SokuItemData(0xFF0314, ItemClassification.progression),
    itemnames.sakuya_4sc_ss:   SokuItemData(0xFF0315, ItemClassification.progression),
    itemnames.sakuya_4sc_sss:  SokuItemData(0xFF0316, ItemClassification.progression),
    itemnames.sakuya_4sc_cr:   SokuItemData(0xFF0317, ItemClassification.progression),
    itemnames.sakuya_5sc_sw:   SokuItemData(0xFF0318, ItemClassification.progression),

}

alice_skill_table = {
    itemnames.alice_236d:  SokuItemData(0xFF0400, ItemClassification.progression),
    itemnames.alice_236a1: SokuItemData(0xFF0401, ItemClassification.progression),
    itemnames.alice_236a2: SokuItemData(0xFF0402, ItemClassification.progression),
    itemnames.alice_623d:  SokuItemData(0xFF0403, ItemClassification.progression),
    itemnames.alice_623a1: SokuItemData(0xFF0404, ItemClassification.progression),
    itemnames.alice_623a2: SokuItemData(0xFF0405, ItemClassification.progression),
    itemnames.alice_214d:  SokuItemData(0xFF0406, ItemClassification.progression),
    itemnames.alice_214a1: SokuItemData(0xFF0407, ItemClassification.progression),
    itemnames.alice_214a2: SokuItemData(0xFF0408, ItemClassification.progression),
    itemnames.alice_22d:   SokuItemData(0xFF0409, ItemClassification.progression),
    itemnames.alice_22a1:  SokuItemData(0xFF040A, ItemClassification.progression),
    itemnames.alice_22a2:  SokuItemData(0xFF040B, ItemClassification.progression),

}

alice_spell_table = {
    itemnames.alice_1sc_as:  SokuItemData(0xFF040C, ItemClassification.progression),
    itemnames.alice_2sc_ll:  SokuItemData(0xFF040D, ItemClassification.progression),
    itemnames.alice_2sc_shd: SokuItemData(0xFF040E, ItemClassification.progression),
    itemnames.alice_2sc_sd:  SokuItemData(0xFF040F, ItemClassification.progression),
    itemnames.alice_2sc_tw:  SokuItemData(0xFF0400, ItemClassification.progression),
    itemnames.alice_3sc_ri:  SokuItemData(0xFF0401, ItemClassification.progression),
    itemnames.alice_3sc_fp:  SokuItemData(0xFF0402, ItemClassification.progression),
    itemnames.alice_4sc_dow: SokuItemData(0xFF0403, ItemClassification.progression),
    itemnames.alice_4sc_hd:  SokuItemData(0xFF0404, ItemClassification.progression),
    itemnames.alice_4sc_hld: SokuItemData(0xFF0405, ItemClassification.progression),
    itemnames.alice_4sc_cp:  SokuItemData(0xFF0406, ItemClassification.progression),
    itemnames.alice_5sc_lp:  SokuItemData(0xFF0407, ItemClassification.progression),
    
}

patchouli_skill_table = {
    itemnames.patchouli_236d:  SokuItemData(0xFF0500, ItemClassification.progression),
    itemnames.patchouli_236a1: SokuItemData(0xFF0501, ItemClassification.progression),
    itemnames.patchouli_236a2: SokuItemData(0xFF0502, ItemClassification.progression),
    itemnames.patchouli_623d:  SokuItemData(0xFF0503, ItemClassification.progression),
    itemnames.patchouli_623a1: SokuItemData(0xFF0504, ItemClassification.progression),
    itemnames.patchouli_623a2: SokuItemData(0xFF0505, ItemClassification.progression),
    itemnames.patchouli_214d:  SokuItemData(0xFF0506, ItemClassification.progression),
    itemnames.patchouli_214a1: SokuItemData(0xFF0507, ItemClassification.progression),
    itemnames.patchouli_214a2: SokuItemData(0xFF0508, ItemClassification.progression),
    itemnames.patchouli_421d:  SokuItemData(0xFF0509, ItemClassification.progression),
    itemnames.patchouli_421a1: SokuItemData(0xFF050A, ItemClassification.progression),
    itemnames.patchouli_421a2: SokuItemData(0xFF050B, ItemClassification.progression),
    itemnames.patchouli_22d:   SokuItemData(0xFF050C, ItemClassification.progression),
    itemnames.patchouli_22a1:  SokuItemData(0xFF050D, ItemClassification.progression),
    itemnames.patchouli_22a2:  SokuItemData(0xFF050E, ItemClassification.progression)

}

patchouli_spell_table = {
    itemnames.patchouli_2sc_nd:  SokuItemData(0xFF050F, ItemClassification.progression),
    itemnames.patchouli_2sc_eh:  SokuItemData(0xFF0510, ItemClassification.progression),
    itemnames.patchouli_3sc_sep: SokuItemData(0xFF0511, ItemClassification.progression),
    itemnames.patchouli_3sc_jp:  SokuItemData(0xFF0512, ItemClassification.progression),
    itemnames.patchouli_3sc_ss:  SokuItemData(0xFF0513, ItemClassification.progression),
    itemnames.patchouli_3sc_ps:  SokuItemData(0xFF0514, ItemClassification.progression),
    itemnames.patchouli_3sc_pp:  SokuItemData(0xFF0515, ItemClassification.progression),
    itemnames.patchouli_4sc_ss:  SokuItemData(0xFF0516, ItemClassification.progression),
    itemnames.patchouli_4sc_em:  SokuItemData(0xFF0517, ItemClassification.progression),
    itemnames.patchouli_5sc_rf:  SokuItemData(0xFF0518, ItemClassification.progression),
    itemnames.patchouli_5sc_ps:  SokuItemData(0xFF0519, ItemClassification.progression),
    itemnames.patchouli_5sc_rdr: SokuItemData(0xFF051A, ItemClassification.progression),

}

youmu_skill_table = {
    itemnames.youmu_236d:   SokuItemData(0xFF0600, ItemClassification.progression),
    itemnames.youmu_236a1:  SokuItemData(0xFF0601, ItemClassification.progression),
    itemnames.youmu_236a2:  SokuItemData(0xFF0602, ItemClassification.progression),
    itemnames.youmu_623d:   SokuItemData(0xFF0603, ItemClassification.progression),
    itemnames.youmu_623a1:  SokuItemData(0xFF0604, ItemClassification.progression),
    itemnames.youmu_623a2:  SokuItemData(0xFF0605, ItemClassification.progression),
    itemnames.youmu_214d:   SokuItemData(0xFF0606, ItemClassification.progression),
    itemnames.youmu_214a1:  SokuItemData(0xFF0607, ItemClassification.progression),
    itemnames.youmu_214a2:  SokuItemData(0xFF0608, ItemClassification.progression),
    itemnames.youmu_22d:    SokuItemData(0xFF0609, ItemClassification.progression),
    itemnames.youmu_22a1:   SokuItemData(0xFF060A, ItemClassification.progression),
    itemnames.youmu_22a2:   SokuItemData(0xFF060B, ItemClassification.progression),

}

youmu_spell_table = {
    itemnames.youmu_2sc_sop:    SokuItemData(0xFF060C, ItemClassification.progression),
    itemnames.youmu_2sc_gwop:   SokuItemData(0xFF060D, ItemClassification.progression),
    itemnames.youmu_3sc_m:      SokuItemData(0xFF060E, ItemClassification.progression),
    itemnames.youmu_3sc_tcb:    SokuItemData(0xFF060F, ItemClassification.progression),
    itemnames.youmu_3sc_soc:    SokuItemData(0xFF0610, ItemClassification.progression),
    itemnames.youmu_4sc_rfd:    SokuItemData(0xFF0611, ItemClassification.progression),
    itemnames.youmu_4sc_atn:    SokuItemData(0xFF0612, ItemClassification.progression),
    itemnames.youmu_5sc_soe:    SokuItemData(0xFF0613, ItemClassification.progression),
    itemnames.youmu_5sc_solad:  SokuItemData(0xFF0624, ItemClassification.progression),
    itemnames.youmu_5sc_src:    SokuItemData(0xFF0625, ItemClassification.progression),

}

remilia_skill_table = {
    itemnames.remilia_236d:    SokuItemData(0xFF0700, ItemClassification.progression),
    itemnames.remilia_236a1:   SokuItemData(0xFF0701, ItemClassification.progression),
    itemnames.remilia_236a2:   SokuItemData(0xFF0702, ItemClassification.progression),
    itemnames.remilia_623d:    SokuItemData(0xFF0703, ItemClassification.progression),
    itemnames.remilia_623a1:   SokuItemData(0xFF0704, ItemClassification.progression),
    itemnames.remilia_623a2:   SokuItemData(0xFF0705, ItemClassification.progression),
    itemnames.remilia_214d:    SokuItemData(0xFF0706, ItemClassification.progression),
    itemnames.remilia_214a1:   SokuItemData(0xFF0707, ItemClassification.progression),
    itemnames.remilia_214a2:   SokuItemData(0xFF0708, ItemClassification.progression),
    itemnames.remilia_22d:     SokuItemData(0xFF0709, ItemClassification.progression),
    itemnames.remilia_22a1:    SokuItemData(0xFF070A, ItemClassification.progression),
    itemnames.remilia_22a2:    SokuItemData(0xFF070B, ItemClassification.progression),

}

remilia_spell_table = {
    itemnames.remilia_2sc_hb:    SokuItemData(0xFF070C, ItemClassification.progression),
    itemnames.remilia_2sc_dkc:   SokuItemData(0xFF070D, ItemClassification.progression),
    itemnames.remilia_3sc_rtnc:  SokuItemData(0xFF070E, ItemClassification.progression),
    itemnames.remilia_3sc_bls:   SokuItemData(0xFF070F, ItemClassification.progression),
    itemnames.remilia_3sc_mf:    SokuItemData(0xFF0710, ItemClassification.progression),
    itemnames.remilia_4sc_stg:   SokuItemData(0xFF0711, ItemClassification.progression),
    itemnames.remilia_4sc_mv:    SokuItemData(0xFF0712, ItemClassification.progression),
    itemnames.remilia_4sc_rs:    SokuItemData(0xFF0713, ItemClassification.progression),
    itemnames.remilia_5sc_sd:    SokuItemData(0xFF0724, ItemClassification.progression),
    itemnames.remilia_5sc_dc:    SokuItemData(0xFF0725, ItemClassification.progression),

}

yuyuko_skill_table = {
    itemnames.yuyuko_236d:    SokuItemData(0xFF0800, ItemClassification.progression),
    itemnames.yuyuko_236a1:   SokuItemData(0xFF0801, ItemClassification.progression),
    itemnames.yuyuko_236a2:   SokuItemData(0xFF0802, ItemClassification.progression),
    itemnames.yuyuko_623d:    SokuItemData(0xFF0803, ItemClassification.progression),
    itemnames.yuyuko_623a1:   SokuItemData(0xFF0804, ItemClassification.progression),
    itemnames.yuyuko_623a2:   SokuItemData(0xFF0805, ItemClassification.progression),
    itemnames.yuyuko_214d:    SokuItemData(0xFF0806, ItemClassification.progression),
    itemnames.yuyuko_214a1:   SokuItemData(0xFF0807, ItemClassification.progression),
    itemnames.yuyuko_214a2:   SokuItemData(0xFF0808, ItemClassification.progression),
    itemnames.yuyuko_421d:    SokuItemData(0xFF0809, ItemClassification.progression),
    itemnames.yuyuko_421a1:   SokuItemData(0xFF080A, ItemClassification.progression),
    itemnames.yuyuko_421a2:   SokuItemData(0xFF080B, ItemClassification.progression),

}

yuyuko_spell_table = {
    itemnames.yuyuko_1sc_pttu:   SokuItemData(0xFF080C, ItemClassification.progression),
    itemnames.yuyuko_2sc_gd:     SokuItemData(0xFF080D, ItemClassification.progression),
    itemnames.yuyuko_2sc_ad:     SokuItemData(0xFF080E, ItemClassification.progression),
    itemnames.yuyuko_2sc_atbf:   SokuItemData(0xFF080F, ItemClassification.progression),
    itemnames.yuyuko_3sc_itta:   SokuItemData(0xFF0810, ItemClassification.progression),
    itemnames.yuyuko_3sc_rb:     SokuItemData(0xFF0811, ItemClassification.progression),
    itemnames.yuyuko_4sc_en:     SokuItemData(0xFF0812, ItemClassification.progression),
    itemnames.yuyuko_4sc_tttn:   SokuItemData(0xFF0813, ItemClassification.progression),
    itemnames.yuyuko_4sc_dl:     SokuItemData(0xFF0814, ItemClassification.progression),
    itemnames.yuyuko_5sc_gh:     SokuItemData(0xFF0815, ItemClassification.progression),
    itemnames.yuyuko_5sc_socb:   SokuItemData(0xFF0816, ItemClassification.progression),

}

yukari_skill_table = {
    itemnames.yukari_236d:    SokuItemData(0xFF0900, ItemClassification.progression),
    itemnames.yukari_236a1:   SokuItemData(0xFF0901, ItemClassification.progression),
    itemnames.yukari_236a2:   SokuItemData(0xFF0902, ItemClassification.progression),
    itemnames.yukari_623d:    SokuItemData(0xFF0903, ItemClassification.progression),
    itemnames.yukari_623a1:   SokuItemData(0xFF0904, ItemClassification.progression),
    itemnames.yukari_623a2:   SokuItemData(0xFF0905, ItemClassification.progression),
    itemnames.yukari_214d:    SokuItemData(0xFF0906, ItemClassification.progression),
    itemnames.yukari_214a1:   SokuItemData(0xFF0907, ItemClassification.progression),
    itemnames.yukari_214a2:   SokuItemData(0xFF0908, ItemClassification.progression),
    itemnames.yukari_421d:    SokuItemData(0xFF0909, ItemClassification.progression),
    itemnames.yukari_421a1:   SokuItemData(0xFF090A, ItemClassification.progression),
    itemnames.yukari_421a2:   SokuItemData(0xFF090B, ItemClassification.progression),

}

yukari_spell_table = {
    itemnames.yukari_1sc_bbtat:   SokuItemData(0xFF090C, ItemClassification.progression),
    itemnames.yukari_1sc_c:       SokuItemData(0xFF090D, ItemClassification.progression),
    itemnames.yukari_2sc_lwv:     SokuItemData(0xFF090E, ItemClassification.progression),
    itemnames.yukari_3sc_qb:      SokuItemData(0xFF090F, ItemClassification.progression),
    itemnames.yukari_3sc_ry:      SokuItemData(0xFF0910, ItemClassification.progression),
    itemnames.yukari_3sc_ob:      SokuItemData(0xFF0911, ItemClassification.progression),
    itemnames.yukari_3sc_nof:     SokuItemData(0xFF0912, ItemClassification.progression),
    itemnames.yukari_4sc_cqb:     SokuItemData(0xFF0913, ItemClassification.progression),
    itemnames.yukari_4sc_tmeol:   SokuItemData(0xFF0914, ItemClassification.progression),
    itemnames.yukari_5sc_tttos:   SokuItemData(0xFF0915, ItemClassification.progression),
}

suika_skill_table = {
    itemnames.suika_236d:    SokuItemData(0xFF0A00, ItemClassification.progression),
    itemnames.suika_236a1:   SokuItemData(0xFF0A01, ItemClassification.progression),
    itemnames.suika_236a2:   SokuItemData(0xFF0A02, ItemClassification.progression),
    itemnames.suika_623d:    SokuItemData(0xFF0A03, ItemClassification.progression),
    itemnames.suika_623a1:   SokuItemData(0xFF0A04, ItemClassification.progression),
    itemnames.suika_623a2:   SokuItemData(0xFF0A05, ItemClassification.progression),
    itemnames.suika_214d:    SokuItemData(0xFF0A06, ItemClassification.progression),
    itemnames.suika_214a1:   SokuItemData(0xFF0A07, ItemClassification.progression),
    itemnames.suika_214a2:   SokuItemData(0xFF0A08, ItemClassification.progression),
    itemnames.suika_22d:     SokuItemData(0xFF0A09, ItemClassification.progression),
    itemnames.suika_22a1:    SokuItemData(0xFF0A0A, ItemClassification.progression),
    itemnames.suika_22a2:    SokuItemData(0xFF0A0B, ItemClassification.progression),

}

suika_spell_table = {
    itemnames.suika_1sc_gad:     SokuItemData(0xFF0A0C, ItemClassification.progression),
    itemnames.suika_2sc_tmt:     SokuItemData(0xFF0A0D, ItemClassification.progression),
    itemnames.suika_2sc_aoob:    SokuItemData(0xFF0A0E, ItemClassification.progression),
    itemnames.suika_2sc_mp:      SokuItemData(0xFF0A0F, ItemClassification.progression),
    itemnames.suika_3sc_tsd:     SokuItemData(0xFF0A10, ItemClassification.progression),
    itemnames.suika_4sc_aogb:    SokuItemData(0xFF0A11, ItemClassification.progression),
    itemnames.suika_4sc_mpp:     SokuItemData(0xFF0A12, ItemClassification.progression),
    itemnames.suika_4sc_sc:      SokuItemData(0xFF0A13, ItemClassification.progression),
    itemnames.suika_5sc_ta:      SokuItemData(0xFF0A14, ItemClassification.progression),
    itemnames.suika_5sc_momo:    SokuItemData(0xFF0A15, ItemClassification.progression),

}

reisen_skill_table = {
    itemnames.reisen_236d:    SokuItemData(0xFF0B00, ItemClassification.progression),
    itemnames.reisen_236a1:   SokuItemData(0xFF0B01, ItemClassification.progression),
    itemnames.reisen_236a2:   SokuItemData(0xFF0B02, ItemClassification.progression),
    itemnames.reisen_623d:    SokuItemData(0xFF0B03, ItemClassification.progression),
    itemnames.reisen_623a1:   SokuItemData(0xFF0B04, ItemClassification.progression),
    itemnames.reisen_623a2:   SokuItemData(0xFF0B05, ItemClassification.progression),
    itemnames.reisen_214d:    SokuItemData(0xFF0B06, ItemClassification.progression),
    itemnames.reisen_214a1:   SokuItemData(0xFF0B07, ItemClassification.progression),
    itemnames.reisen_214a2:   SokuItemData(0xFF0B08, ItemClassification.progression),
    itemnames.reisen_22d:     SokuItemData(0xFF0B09, ItemClassification.progression),
    itemnames.reisen_22a1:    SokuItemData(0xFF0B0A, ItemClassification.progression),
    itemnames.reisen_22a2:    SokuItemData(0xFF0B0B, ItemClassification.progression),

}

reisen_spell_table = {
    itemnames.reisen_1sc_cv:     SokuItemData(0xFF0B0C, ItemClassification.progression),
    itemnames.reisen_1sc_d:      SokuItemData(0xFF0B0D, ItemClassification.progression),
    itemnames.reisen_2sc_gwo:    SokuItemData(0xFF0B0E, ItemClassification.progression),
    itemnames.reisen_2sc_im:     SokuItemData(0xFF0B0F, ItemClassification.progression),
    itemnames.reisen_3sc_ms:     SokuItemData(0xFF0B10, ItemClassification.progression),
    itemnames.reisen_3sc_cw:     SokuItemData(0xFF0B11, ItemClassification.progression),
    itemnames.reisen_3sc_d:      SokuItemData(0xFF0B12, ItemClassification.progression),
    itemnames.reisen_3sc_gpe:    SokuItemData(0xFF0B13, ItemClassification.progression),
    itemnames.reisen_3sc_xw:     SokuItemData(0xFF0B14, ItemClassification.progression),
    itemnames.reisen_4sc_lb:     SokuItemData(0xFF0B15, ItemClassification.progression),
    itemnames.reisen_5sc_lre:    SokuItemData(0xFF0B16, ItemClassification.progression),

}

aya_skill_table = {
    itemnames.aya_236d:    SokuItemData(0xFF0C00, ItemClassification.progression),
    itemnames.aya_236a1:   SokuItemData(0xFF0C01, ItemClassification.progression),
    itemnames.aya_236a2:   SokuItemData(0xFF0C02, ItemClassification.progression),
    itemnames.aya_214d:    SokuItemData(0xFF0C03, ItemClassification.progression),
    itemnames.aya_214a1:   SokuItemData(0xFF0C04, ItemClassification.progression),
    itemnames.aya_214a2:   SokuItemData(0xFF0C05, ItemClassification.progression),
    itemnames.aya_421d:    SokuItemData(0xFF0C06, ItemClassification.progression),
    itemnames.aya_421a1:   SokuItemData(0xFF0C07, ItemClassification.progression),
    itemnames.aya_421a2:   SokuItemData(0xFF0C08, ItemClassification.progression),
    itemnames.aya_22d:     SokuItemData(0xFF0C09, ItemClassification.progression),
    itemnames.aya_22a1:    SokuItemData(0xFF0C0A, ItemClassification.progression),
    itemnames.aya_22a2:    SokuItemData(0xFF0C0B, ItemClassification.progression),

}

aya_spell_table = {
    itemnames.aya_1sc_swv:      SokuItemData(0xFF0C0C, ItemClassification.progression),
    itemnames.aya_2sc_wottp:    SokuItemData(0xFF0C0D, ItemClassification.progression),
    itemnames.aya_2sc_tls:      SokuItemData(0xFF0C0E, ItemClassification.progression),
    itemnames.aya_3sc_mlf:      SokuItemData(0xFF0C0F, ItemClassification.progression),
    itemnames.aya_3sc_tm:       SokuItemData(0xFF0C10, ItemClassification.progression),
    itemnames.aya_3sc_sg:       SokuItemData(0xFF0C11, ItemClassification.progression),
    itemnames.aya_4sc_rftm:     SokuItemData(0xFF0C12, ItemClassification.progression),
    itemnames.aya_4sc_dd:       SokuItemData(0xFF0C13, ItemClassification.progression),
    itemnames.aya_5sc_ittd:     SokuItemData(0xFF0C14, ItemClassification.progression),
    itemnames.aya_5sc_id:       SokuItemData(0xFF0C15, ItemClassification.progression),

}

komachi_skill_table = {
    itemnames.komachi_236d:    SokuItemData(0xFF0D00, ItemClassification.progression),
    itemnames.komachi_236a1:   SokuItemData(0xFF0D01, ItemClassification.progression),
    itemnames.komachi_236a2:   SokuItemData(0xFF0D02, ItemClassification.progression),
    itemnames.komachi_623d:    SokuItemData(0xFF0D03, ItemClassification.progression),
    itemnames.komachi_623a1:   SokuItemData(0xFF0D04, ItemClassification.progression),
    itemnames.komachi_623a2:   SokuItemData(0xFF0D05, ItemClassification.progression),
    itemnames.komachi_214d:    SokuItemData(0xFF0D06, ItemClassification.progression),
    itemnames.komachi_214a1:   SokuItemData(0xFF0D07, ItemClassification.progression),
    itemnames.komachi_214a2:   SokuItemData(0xFF0D08, ItemClassification.progression),
    itemnames.komachi_22d:     SokuItemData(0xFF0D09, ItemClassification.progression),
    itemnames.komachi_22a1:    SokuItemData(0xFF0D0A, ItemClassification.progression),
    itemnames.komachi_22a2:    SokuItemData(0xFF0D0B, ItemClassification.progression),

}

komachi_spell_table = {
    itemnames.komachi_1sc_fotr:     SokuItemData(0xFF0D0C, ItemClassification.progression),
    itemnames.komachi_1sc_afs:      SokuItemData(0xFF0D0D, ItemClassification.progression),
    itemnames.komachi_3sc_fitdf:    SokuItemData(0xFF0D0E, ItemClassification.progression),
    itemnames.komachi_3sc_ibs:      SokuItemData(0xFF0D0F, ItemClassification.progression),
    itemnames.komachi_3sc_hcoa:     SokuItemData(0xFF0D10, ItemClassification.progression),
    itemnames.komachi_4sc_sofj:     SokuItemData(0xFF0D11, ItemClassification.progression),
    itemnames.komachi_4sc_sows:     SokuItemData(0xFF0D12, ItemClassification.progression),
    itemnames.komachi_5sc_sle:      SokuItemData(0xFF0D13, ItemClassification.progression),
    itemnames.komachi_5sc_upl:      SokuItemData(0xFF0D14, ItemClassification.progression),

}

iku_skill_table = {
    itemnames.iku_236d:    SokuItemData(0xFF0E00, ItemClassification.progression),
    itemnames.iku_236a1:   SokuItemData(0xFF0E01, ItemClassification.progression),
    itemnames.iku_236a2:   SokuItemData(0xFF0E02, ItemClassification.progression),
    itemnames.iku_623d:    SokuItemData(0xFF0E03, ItemClassification.progression),
    itemnames.iku_623a1:   SokuItemData(0xFF0E04, ItemClassification.progression),
    itemnames.iku_623a2:   SokuItemData(0xFF0E05, ItemClassification.progression),
    itemnames.iku_214d:    SokuItemData(0xFF0E06, ItemClassification.progression),
    itemnames.iku_214a1:   SokuItemData(0xFF0E07, ItemClassification.progression),
    itemnames.iku_214a2:   SokuItemData(0xFF0E08, ItemClassification.progression),
    itemnames.iku_22d:     SokuItemData(0xFF0E09, ItemClassification.progression),
    itemnames.iku_22a1:    SokuItemData(0xFF0E0A, ItemClassification.progression),
    itemnames.iku_22a2:    SokuItemData(0xFF0E0B, ItemClassification.progression),

}

iku_spell_table = {
    itemnames.iku_1sc_tds:       SokuItemData(0xFF0E0C, ItemClassification.progression),
    itemnames.iku_1sc_vlt:       SokuItemData(0xFF0E0D, ItemClassification.progression),
    itemnames.iku_2sc_sts:       SokuItemData(0xFF0E0E, ItemClassification.progression),
    itemnames.iku_3sc_dd:        SokuItemData(0xFF0E0F, ItemClassification.progression),
    itemnames.iku_3sc_edp:       SokuItemData(0xFF0E10, ItemClassification.progression),
    itemnames.iku_3sc_lds:       SokuItemData(0xFF0E11, ItemClassification.progression),
    itemnames.iku_3sc_ts:        SokuItemData(0xFF0E12, ItemClassification.progression),
    itemnames.iku_4sc_vls:       SokuItemData(0xFF0E13, ItemClassification.progression),
    itemnames.iku_4sc_ootfcd:    SokuItemData(0xFF0E14, ItemClassification.progression),
    itemnames.iku_5sc_sos:       SokuItemData(0xFF0E15, ItemClassification.progression),

}

tenshi_skill_table = {
    itemnames.tenshi_236d:    SokuItemData(0xFF0F00, ItemClassification.progression),
    itemnames.tenshi_236a1:   SokuItemData(0xFF0F01, ItemClassification.progression),
    itemnames.tenshi_236a2:   SokuItemData(0xFF0F02, ItemClassification.progression),
    itemnames.tenshi_623d:    SokuItemData(0xFF0F03, ItemClassification.progression),
    itemnames.tenshi_623a1:   SokuItemData(0xFF0F04, ItemClassification.progression),
    itemnames.tenshi_623a2:   SokuItemData(0xFF0F05, ItemClassification.progression),
    itemnames.tenshi_214d:    SokuItemData(0xFF0F06, ItemClassification.progression),
    itemnames.tenshi_214a1:   SokuItemData(0xFF0F07, ItemClassification.progression),
    itemnames.tenshi_214a2:   SokuItemData(0xFF0F08, ItemClassification.progression),
    itemnames.tenshi_22d:     SokuItemData(0xFF0F09, ItemClassification.progression),
    itemnames.tenshi_22a1:    SokuItemData(0xFF0F0A, ItemClassification.progression),
    itemnames.tenshi_22a2:    SokuItemData(0xFF0F0B, ItemClassification.progression),

}

tenshi_spell_table = {
    itemnames.tenshi_2sc_sous:     SokuItemData(0xFF0F0C, ItemClassification.progression),
    itemnames.tenshi_2sc_sor:      SokuItemData(0xFF0F0D, ItemClassification.progression),
    itemnames.tenshi_3sc_sodj:     SokuItemData(0xFF0F0E, ItemClassification.progression),
    itemnames.tenshi_3sc_sos:      SokuItemData(0xFF0F0F, ItemClassification.progression),
    itemnames.tenshi_3sc_swp:      SokuItemData(0xFF0F10, ItemClassification.progression),
    itemnames.tenshi_4sc_mr:       SokuItemData(0xFF0F11, ItemClassification.progression),
    itemnames.tenshi_4sc_soe:      SokuItemData(0xFF0F12, ItemClassification.progression),
    itemnames.tenshi_5sc_sowaj:    SokuItemData(0xFF0F13, ItemClassification.progression),
    itemnames.tenshi_5sc_wcp:      SokuItemData(0xFF0F14, ItemClassification.progression),
    itemnames.tenshi_5sc_swr:      SokuItemData(0xFF0F15, ItemClassification.progression),

}

sanae_skill_table = {
    itemnames.sanae_236d:    SokuItemData(0xFF1000, ItemClassification.progression),
    itemnames.sanae_236a1:   SokuItemData(0xFF1001, ItemClassification.progression),
    itemnames.sanae_236a2:   SokuItemData(0xFF1002, ItemClassification.progression),
    itemnames.sanae_623d:    SokuItemData(0xFF1003, ItemClassification.progression),
    itemnames.sanae_623a1:   SokuItemData(0xFF1004, ItemClassification.progression),
    itemnames.sanae_623a2:   SokuItemData(0xFF1005, ItemClassification.progression),
    itemnames.sanae_214d:    SokuItemData(0xFF1006, ItemClassification.progression),
    itemnames.sanae_214a1:   SokuItemData(0xFF1007, ItemClassification.progression),
    itemnames.sanae_214a2:   SokuItemData(0xFF1008, ItemClassification.progression),
    itemnames.sanae_22d:     SokuItemData(0xFF1009, ItemClassification.progression),
    itemnames.sanae_22a1:    SokuItemData(0xFF100A, ItemClassification.progression),
    itemnames.sanae_22a2:    SokuItemData(0xFF100B, ItemClassification.progression),

}

sanae_spell_table = {
    itemnames.sanae_2sc_cogc:     SokuItemData(0xFF100C, ItemClassification.progression),
    itemnames.sanae_2sc_gt:       SokuItemData(0xFF100D, ItemClassification.progression),
    itemnames.sanae_2sc_rob:      SokuItemData(0xFF100E, ItemClassification.progression),
    itemnames.sanae_3sc_tdtss:    SokuItemData(0xFF100F, ItemClassification.progression),
    itemnames.sanae_3sc_mds:      SokuItemData(0xFF1010, ItemClassification.progression),
    itemnames.sanae_4sc_fr:       SokuItemData(0xFF1011, ItemClassification.progression),
    itemnames.sanae_4sc_notss:    SokuItemData(0xFF1012, ItemClassification.progression),
    itemnames.sanae_5sc_mm:       SokuItemData(0xFF1013, ItemClassification.progression),
    itemnames.sanae_5sc_ncp:      SokuItemData(0xFF1014, ItemClassification.progression),

}

cirno_skill_table = {
    itemnames.cirno_236d:    SokuItemData(0xFF1100, ItemClassification.progression),
    itemnames.cirno_236a1:   SokuItemData(0xFF1101, ItemClassification.progression),
    itemnames.cirno_236a2:   SokuItemData(0xFF1102, ItemClassification.progression),
    itemnames.cirno_623d:    SokuItemData(0xFF1103, ItemClassification.progression),
    itemnames.cirno_623a1:   SokuItemData(0xFF1104, ItemClassification.progression),
    itemnames.cirno_623a2:   SokuItemData(0xFF1105, ItemClassification.progression),
    itemnames.cirno_214d:    SokuItemData(0xFF1106, ItemClassification.progression),
    itemnames.cirno_214a1:   SokuItemData(0xFF1107, ItemClassification.progression),
    itemnames.cirno_214a2:   SokuItemData(0xFF1108, ItemClassification.progression),
    itemnames.cirno_22d:     SokuItemData(0xFF1109, ItemClassification.progression),
    itemnames.cirno_22a1:    SokuItemData(0xFF110A, ItemClassification.progression),
    itemnames.cirno_22a2:    SokuItemData(0xFF110B, ItemClassification.progression),

}

cirno_spell_table = {
    itemnames.cirno_2sc_img:    SokuItemData(0xFF110C, ItemClassification.progression),
    itemnames.cirno_2sc_fs:     SokuItemData(0xFF110D, ItemClassification.progression),
    itemnames.cirno_3sc_cs:     SokuItemData(0xFF110E, ItemClassification.progression),
    itemnames.cirno_3sc_sik:    SokuItemData(0xFF110F, ItemClassification.progression),
    itemnames.cirno_3sc_sf:     SokuItemData(0xFF1110, ItemClassification.progression),
    itemnames.cirno_3sc_fa:     SokuItemData(0xFF1111, ItemClassification.progression),
    itemnames.cirno_3sc_ifb:    SokuItemData(0xFF1112, ItemClassification.progression),
    itemnames.cirno_4sc_fc:     SokuItemData(0xFF1113, ItemClassification.progression),
    itemnames.cirno_4sc_it:     SokuItemData(0xFF1114, ItemClassification.progression),
    itemnames.cirno_5sc_pf:     SokuItemData(0xFF1115, ItemClassification.progression),
    itemnames.cirno_5sc_gc:     SokuItemData(0xFF1116, ItemClassification.progression),

}

meiling_skill_table = {
    itemnames.meiling_236d:    SokuItemData(0xFF1200, ItemClassification.progression),
    itemnames.meiling_236a1:   SokuItemData(0xFF1201, ItemClassification.progression),
    itemnames.meiling_236a2:   SokuItemData(0xFF1202, ItemClassification.progression),
    itemnames.meiling_623d:    SokuItemData(0xFF1203, ItemClassification.progression),
    itemnames.meiling_623a1:   SokuItemData(0xFF1204, ItemClassification.progression),
    itemnames.meiling_623a2:   SokuItemData(0xFF1205, ItemClassification.progression),
    itemnames.meiling_214d:    SokuItemData(0xFF1206, ItemClassification.progression),
    itemnames.meiling_214a1:   SokuItemData(0xFF1207, ItemClassification.progression),
    itemnames.meiling_214a2:   SokuItemData(0xFF1208, ItemClassification.progression),
    itemnames.meiling_22d:     SokuItemData(0xFF1209, ItemClassification.progression),
    itemnames.meiling_22a1:    SokuItemData(0xFF120A, ItemClassification.progression),
    itemnames.meiling_22a2:    SokuItemData(0xFF120B, ItemClassification.progression),

}

meiling_spell_table = {
    itemnames.meiling_2sc_cw:       SokuItemData(0xFF120C, ItemClassification.progression),
    itemnames.meiling_2sc_irf:      SokuItemData(0xFF120D, ItemClassification.progression),
    itemnames.meiling_3sc_sb:       SokuItemData(0xFF120E, ItemClassification.progression),
    itemnames.meiling_3sc_rf:       SokuItemData(0xFF120F, ItemClassification.progression),
    itemnames.meiling_3sc_edsdk:    SokuItemData(0xFF1210, ItemClassification.progression),
    itemnames.meiling_4sc_mcd:      SokuItemData(0xFF1211, ItemClassification.progression),
    itemnames.meiling_4sc_rt:       SokuItemData(0xFF1212, ItemClassification.progression),
    itemnames.meiling_4sc_fter:     SokuItemData(0xFF1213, ItemClassification.progression),
    itemnames.meiling_5sc_emsb:     SokuItemData(0xFF1214, ItemClassification.progression),
    itemnames.meiling_5sc_rkf:      SokuItemData(0xFF1215, ItemClassification.progression),
    itemnames.meiling_5sc_rbr:      SokuItemData(0xFF1216, ItemClassification.progression),

}

okuu_skill_table = { #Utsuho, also affectionately reffered to as "Okuu"
    itemnames.okuu_236d:    SokuItemData(0xFF1300, ItemClassification.progression),
    itemnames.okuu_236a1:   SokuItemData(0xFF1301, ItemClassification.progression),
    itemnames.okuu_236a2:   SokuItemData(0xFF1302, ItemClassification.progression),
    itemnames.okuu_623d:    SokuItemData(0xFF1303, ItemClassification.progression),
    itemnames.okuu_623a1:   SokuItemData(0xFF1304, ItemClassification.progression),
    itemnames.okuu_623a2:   SokuItemData(0xFF1305, ItemClassification.progression),
    itemnames.okuu_214d:    SokuItemData(0xFF1306, ItemClassification.progression),
    itemnames.okuu_214a1:   SokuItemData(0xFF1307, ItemClassification.progression),
    itemnames.okuu_214a2:   SokuItemData(0xFF1308, ItemClassification.progression),
    itemnames.okuu_22d:     SokuItemData(0xFF1309, ItemClassification.progression),
    itemnames.okuu_22a1:    SokuItemData(0xFF130A, ItemClassification.progression),
    itemnames.okuu_22a2:    SokuItemData(0xFF130B, ItemClassification.progression),

}

okuu_spell_table = {
    itemnames.okuu_1sc_has:    SokuItemData(0xFF130C, ItemClassification.progression),
    itemnames.okuu_2sc_st:     SokuItemData(0xFF130D, ItemClassification.progression),
    itemnames.okuu_2sc_nv:     SokuItemData(0xFF130E, ItemClassification.progression),
    itemnames.okuu_3sc_mf:     SokuItemData(0xFF130F, ItemClassification.progression),
    itemnames.okuu_3sc_fs:     SokuItemData(0xFF1310, ItemClassification.progression),
    itemnames.okuu_3sc_cs:     SokuItemData(0xFF1311, ItemClassification.progression),
    itemnames.okuu_3sc_htb:    SokuItemData(0xFF1312, ItemClassification.progression),
    itemnames.okuu_4sc_tts:    SokuItemData(0xFF1313, ItemClassification.progression),
    itemnames.okuu_4sc_nbg:    SokuItemData(0xFF1314, ItemClassification.progression),
    itemnames.okuu_4sc_yd:     SokuItemData(0xFF1315, ItemClassification.progression),
    itemnames.okuu_4sc_ud:     SokuItemData(0xFF1316, ItemClassification.progression),
    itemnames.okuu_4sc_ss:     SokuItemData(0xFF1317, ItemClassification.progression),
    itemnames.okuu_5sc_gf:     SokuItemData(0xFF1318, ItemClassification.progression),
    itemnames.okuu_5sc_an:     SokuItemData(0xFF1319, ItemClassification.progression),

}

suwako_skill_table = {
    itemnames.suwako_236d:    SokuItemData(0xFF1400, ItemClassification.progression),
    itemnames.suwako_236a1:   SokuItemData(0xFF1401, ItemClassification.progression),
    itemnames.suwako_236a2:   SokuItemData(0xFF1402, ItemClassification.progression),
    itemnames.suwako_623d:    SokuItemData(0xFF1403, ItemClassification.progression),
    itemnames.suwako_623a1:   SokuItemData(0xFF1404, ItemClassification.progression),
    itemnames.suwako_623a2:   SokuItemData(0xFF1405, ItemClassification.progression),
    itemnames.suwako_214d:    SokuItemData(0xFF1406, ItemClassification.progression),
    itemnames.suwako_214a1:   SokuItemData(0xFF1407, ItemClassification.progression),
    itemnames.suwako_214a2:   SokuItemData(0xFF1408, ItemClassification.progression),
    itemnames.suwako_22d:     SokuItemData(0xFF1409, ItemClassification.progression),
    itemnames.suwako_22a1:    SokuItemData(0xFF140A, ItemClassification.progression),
    itemnames.suwako_22a2:    SokuItemData(0xFF140B, ItemClassification.progression),

}

suwako_spell_table = {
    itemnames.suwako_2sc_mcw:      SokuItemData(0xFF140C, ItemClassification.progression),
    itemnames.suwako_2sc_mmr:      SokuItemData(0xFF140D, ItemClassification.progression),
    itemnames.suwako_3sc_mg:       SokuItemData(0xFF140E, ItemClassification.progression),
    itemnames.suwako_3sc_bcb:      SokuItemData(0xFF140F, ItemClassification.progression),
    itemnames.suwako_3sc_fbte:     SokuItemData(0xFF1410, ItemClassification.progression),
    itemnames.suwako_4sc_hrj:      SokuItemData(0xFF1411, ItemClassification.progression),
    itemnames.suwako_4sc_shaef:    SokuItemData(0xFF1412, ItemClassification.progression),
    itemnames.suwako_4sc_ml:       SokuItemData(0xFF1413, ItemClassification.progression),
    itemnames.suwako_4sc_rfoh:     SokuItemData(0xFF1414, ItemClassification.progression),
    itemnames.suwako_4sc_cah:      SokuItemData(0xFF1415, ItemClassification.progression),
    itemnames.suwako_5sc_ms:       SokuItemData(0xFF1416, ItemClassification.progression),

}

filler_table = {
    itemnames.f_card_draw:            SokuItemData(0xFF2000, ItemClassification.filler),
    itemnames.f_two_card_draw:        SokuItemData(0xFF2001, ItemClassification.filler),
    itemnames.f_spirit_break_opp:     SokuItemData(0xFF2002, ItemClassification.filler),
    itemnames.f_card_break_opp:       SokuItemData(0xFF2003, ItemClassification.filler),
    itemnames.f_cycle_weather:        SokuItemData(0xFF2004, ItemClassification.filler),
    itemnames.f_trigger_weather:      SokuItemData(0xFF2005, ItemClassification.filler),
    itemnames.f_heal_self:            SokuItemData(0xFF2006, ItemClassification.filler),
    itemnames.f_heal_more_self:       SokuItemData(0xFF2007, ItemClassification.filler),
    itemnames.f_max_health:           SokuItemData(0xFF2008, ItemClassification.filler),
    itemnames.f_poke_opp:             SokuItemData(0xFF2009, ItemClassification.filler),
    itemnames.f_poke_more_opp:        SokuItemData(0xFF200A, ItemClassification.filler),
    itemnames.f_drain_opp:            SokuItemData(0xFF200B, ItemClassification.filler),
    itemnames.f_spirit_regen:         SokuItemData(0xFF200C, ItemClassification.filler),
    itemnames.f_heal_spirit:          SokuItemData(0xFF200D, ItemClassification.filler),

}

trap_table = {
    itemnames.t_poke_trap:              SokuItemData(0xFF2100, ItemClassification.filler),
    itemnames.t_drain_trap:             SokuItemData(0xFF2101, ItemClassification.filler),
    itemnames.t_half_hp_trap:           SokuItemData(0xFF2102, ItemClassification.filler),
    itemnames.t_card_trap:              SokuItemData(0xFF2103, ItemClassification.filler),
    itemnames.t_spirit_trap:            SokuItemData(0xFF2104, ItemClassification.filler),
    itemnames.t_heal_trap:              SokuItemData(0xFF2105, ItemClassification.filler),
    itemnames.t_heal_all_trap:          SokuItemData(0xFF2106, ItemClassification.filler),
    itemnames.t_draw_trap:              SokuItemData(0xFF2107, ItemClassification.filler),
    itemnames.t_pause_weather:          SokuItemData(0xFF2108, ItemClassification.filler),
    itemnames.t_randomize_weather:      SokuItemData(0xFF2109, ItemClassification.filler),

}

all_items = {
    **characters_table,
    **story_table,
    **arcade_table,
    **difficulty_table,
    **system_card_table,
    **reimu_skill_table,
    **reimu_spell_table,
    **marisa_skill_table,
    **marisa_spell_table,
    **sakuya_skill_table,
    **sakuya_spell_table,
    **alice_skill_table,
    **alice_spell_table,
    **patchouli_skill_table,
    **patchouli_spell_table,
    **youmu_skill_table,
    **youmu_spell_table,
    **remilia_skill_table,
    **remilia_spell_table,
    **yuyuko_skill_table,
    **yuyuko_spell_table,
    **yukari_skill_table,
    **yukari_spell_table,
    **suika_skill_table,
    **suika_spell_table,
    **reisen_skill_table,
    **reisen_spell_table,
    **aya_skill_table,
    **aya_spell_table,
    **komachi_skill_table,
    **komachi_spell_table,
    **iku_skill_table,
    **iku_spell_table,
    **tenshi_skill_table,
    **tenshi_spell_table,
    **sanae_skill_table,
    **sanae_spell_table,
    **cirno_skill_table,
    **cirno_spell_table,
    **meiling_skill_table,
    **meiling_spell_table,
    **okuu_skill_table,
    **okuu_spell_table,
    **suwako_skill_table,
    **suwako_spell_table

}

def setup_items(world: World, player: int):

    itempool: list[Item] = []
    
    if world.option.story_mode_checks == "Sanae":
        itempool += [world.create_item({itemnames.sanae_story}) for _ in range(5)]
    if world.option.story_mode_checks == "Cirno":
        itempool += [world.create_item({itemnames.cirno_story}) for _ in range(5)]
    if world.option.story_mode_checks == "Meiling":
        itempool += [world.create_item({itemnames.meiling_story}) for _ in range(5)]

    
    world.multiworld.itempool += itempool

    if world.option.starting_character == 0:
        start_reimu = world.create_item(itemnames.reimu)
        world.push_precollected(start_reimu)
    if world.option.starting_character == 1:
        start_marisa = world.create_item(itemnames.marisa)
        world.push_precollected(start_marisa)
    if world.option.starting_character == 2:
        start_sakuya = world.create_item(itemnames.sakuya)
        world.push_precollected(start_sakuya)
    if world.option.starting_character == 3:
        start_alice = world.create_item(itemnames.alice)
        world.push_precollected(start_alice)
    if world.option.starting_character == 4:
        start_patchouli = world.create_item(itemnames.patchouli)
        world.push_precollected(start_patchouli)
    if world.option.starting_character == 5:
        start_youmu = world.create_item(itemnames.youmu)
        world.push_precollected(start_youmu)
    if world.option.starting_character == 6:
        start_remilia = world.create_item(itemnames.remilia)
        world.push_precollected(start_remilia)
    if world.option.starting_character == 7:
        start_yuyuko = world.create_item(itemnames.yuyuko)
        world.push_precollected(start_yuyuko)
    if world.option.starting_character == 8:
        start_yukari = world.create_item(itemnames.yukari)
        world.push_precollected(start_yukari)
    if world.option.starting_character == 9:
        start_suika = world.create_item(itemnames.suika)
        world.push_precollected(start_suika)
    if world.option.starting_character == 10:
        start_reisen = world.create_item(itemnames.reisen)
        world.push_precollected(start_reisen)
    if world.option.starting_character == 11:
        start_aya = world.create_item(itemnames.aya)
        world.push_precollected(start_aya)
    if world.option.starting_character == 12:
        start_komachi = world.create_item(itemnames.komachi)
        world.push_precollected(start_komachi)
    if world.option.starting_character == 13:
        start_iku = world.create_item(itemnames.komachi)
        world.push_precollected(start_iku)
    if world.option.starting_character == 14:
        start_tenshi = world.create_item(itemnames.tenshi)
        world.push_precollected(start_tenshi)
    if world.option.starting_character == 15:
        start_sanae = world.create_item(itemnames.sanae)
        world.push_precollected(start_sanae)
    if world.option.starting_character == 16:
        start_cirno = world.create_item(itemnames.cirno)
        world.push_precollected(start_cirno)
    if world.option.starting_character == 17:
        start_meiling = world.create_item(itemnames.meiling)
        world.push_precollected(start_meiling)
    if world.option.starting_character == 18:
        start_okuu = world.create_item(itemnames.okuu)
        world.push_precollected(start_okuu)
    if world.option.starting_character == 19:
        start_suwako = world.create_item(itemnames.suwako)
        world.push_precollected(start_suwako)


item_groups: Dict[int, str] = {

    #General Item Groups
    "Characters": list(characters_table.keys()),
    "Story Characters": list(itemnames.sanae_story, itemnames.cirno_story, itemnames.meiling_story),
    "System Cards": list(system_card_table.keys()),
    "Reimu Skills": list(reimu_skill_table.keys()),
    "Reimu Spells": list(reimu_spell_table.keys()),
    "Reimu Cards": list(reimu_spell_table.keys(), reimu_skill_table.keys()),
    
    #Miscelaneous Slang
    "Reimu 236d": list(itemnames.reimu_236d),
    "Reimu 236a1": list(itemnames.reimu_236a1),
    "Reimu 236a2": list(itemnames.reimu_236a2),
    "Reimu Orbs": list(itemnames.reimu_2sc_fo),
    "Reimu Gems": list(itemnames.reimu_5sc_fs),
}

lookup_id_to_name: Dict[int, str] = {data.code: item_name for item_name, data in all_items.items() if data.code}


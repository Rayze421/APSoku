from typing import Dict, NamedTuple, Optional
from worlds.AutoWorld import World
from .data import locationnames
from BaseClasses import Location, Multiworld

class SokuLocation(Location):
    game: str = "Touhou 12.3 - Hisoutensoku"



goal_location_table = {
    locationnames.story_end: 0xFF0000,
    locationnames.sanae_story_end: 0xFF0001,
    locationnames.cirno_story_end: 0xFF0002,
    locationnames.meiling_story_end: 0xFF0003,
    
    locationnames.reimu_arcade_end:     0xFF0004,
    locationnames.marisa_arcade_end:    0xFF0005,
    locationnames.sakuya_arcade_end:    0xFF0006,
    locationnames.alice_arcade_end:     0xFF0007,
    locationnames.patchouli_arcade_end: 0xFF0008,
    locationnames.youmu_arcade_end:     0xFF0009,
    locationnames.remilia_arcade_end:   0xFF000A,
    locationnames.yuyuko_arcade_end:    0xFF000B,
    locationnames.yukari_arcade_end:    0xFF000C,
    locationnames.suika_arcade_end:     0xFF000D,
    locationnames.reisen_arcade_end:    0xFF000E,
    locationnames.aya_arcade_end:       0xFF000F,
    locationnames.komachi_arcade_end:   0xFF0010,
    locationnames.iku_arcade_end:       0xFF0011,
    locationnames.tenshi_arcade_end:    0xFF0012,
    locationnames.sanae_arcade_end:     0xFF0013,
    locationnames.cirno_arcade_end:     0xFF0014,
    locationnames.meiling_arcade_end:   0xFF0015,
    locationnames.okuu_arcade_end:      0xFF0016,
    locationnames.suwako_arcade_end:    0xFF0017,
    
    locationnames.collector_goal:    0xFF0018,
    locationnames.master_goal:       0xFF0019
}

sanae_story_stage_table = {
    locationnames.sanae_story_1: 0xFF1000,
    locationnames.sanae_story_2: 0xFF1001,
    locationnames.sanae_story_3: 0xFF1002,
    locationnames.sanae_story_4: 0xFF1003,
    locationnames.sanae_story_5: 0xFF1004

}

sanae_story_spell_table = {
    locationnames.sanae_cirno_s1: 0xFF1005,
    locationnames.sanae_cirno_s2: 0xFF1006,
    locationnames.sanae_meiling_s1: 0xFF1007,
    locationnames.sanae_meiling_s2: 0xFF1008,
    locationnames.sanae_reimu_s1: 0xFF1009,
    locationnames.sanae_reimu_s2: 0xFF100A,
    locationnames.sanae_reimu_s3: 0xFF100B,
    locationnames.sanae_okuu_s1: 0xFF100C,
    locationnames.sanae_okuu_s2: 0xFF100D,
    locationnames.sanae_okuu_s3: 0xFF100E,
    locationnames.sanae_okuu_s4: 0xFF100F,
    locationnames.sanae_suwako_s1: 0xFF1010,
    locationnames.sanae_suwako_s2: 0xFF1011,
    locationnames.sanae_suwako_s3: 0xFF1012,
    locationnames.sanae_suwako_s4: 0xFF1013,
    locationnames.sanae_suwako_s5: 0xFF1014

}

cirno_story_stage_table = {
    locationnames.cirno_story_1: 0xFF1100,
    locationnames.cirno_story_2: 0xFF1101,
    locationnames.cirno_story_3: 0xFF1102,
    locationnames.cirno_story_4: 0xFF1103,
    locationnames.cirno_story_5: 0xFF1104

}

cirno_story_spell_table = {
    locationnames.cirno_sanae_s1: 0xFF1105,
    locationnames.cirno_sanae_s2: 0xFF1106,
    locationnames.cirno_meiling_s1: 0xFF1107,
    locationnames.cirno_meiling_s2: 0xFF1108,
    locationnames.cirno_marisa_s1: 0xFF1109,
    locationnames.cirno_marisa_s2: 0xFF110A,
    locationnames.cirno_marisa_s3: 0xFF110B,
    locationnames.cirno_okuu_s1: 0xFF110C,
    locationnames.cirno_okuu_s2: 0xFF110D,
    locationnames.cirno_okuu_s3: 0xFF110E,
    locationnames.cirno_okuu_s4: 0xFF110F,
    locationnames.cirno_alice_s1: 0xFF1110,
    locationnames.cirno_alice_s2: 0xFF1111,
    locationnames.cirno_alice_s3: 0xFF1112,
    locationnames.cirno_alice_s4: 0xFF1113,
    locationnames.cirno_alice_s5: 0xFF1114

}

meiling_story_stage_table = {
    locationnames.meiling_story_1: 0xFF1200,
    locationnames.meiling_story_2: 0xFF1201,
    locationnames.meiling_story_3: 0xFF1202,
    locationnames.meiling_story_4: 0xFF1203,
    locationnames.meiling_story_5: 0xFF1204

}

meiling_story_spell_table = {
    locationnames.meiling_patchouli_s1: 0xFF1205,
    locationnames.meiling_patchouli_s2: 0xFF1206,
    locationnames.meiling_alice_s1: 0xFF1207,
    locationnames.meiling_alice_s2: 0xFF1208,
    locationnames.meiling_marisa_s1: 0xFF1209,
    locationnames.meiling_marisa_s2: 0xFF120A,
    locationnames.meiling_marisa_s3: 0xFF120B,
    locationnames.meiling_reimu_s1: 0xFF120C,
    locationnames.meiling_reimu_s2: 0xFF120D,
    locationnames.meiling_reimu_s3: 0xFF120E,
    locationnames.meiling_reimu_s4: 0xFF120F,
    locationnames.meiling_fish_s1: 0xFF1210,
    locationnames.meiling_fish_s2: 0xFF1211,
    locationnames.meiling_fish_s3: 0xFF1212,
    locationnames.meiling_fish_s4: 0xFF1213,
    locationnames.meiling_fish_s5: 0xFF1214

}

reimu_arcade_stage_table = {
    locationnames.reimu_arcade_1:  0xFF2000,
    locationnames.reimu_arcade_2:  0xFF2001,
    locationnames.reimu_arcade_3:  0xFF2002,
    locationnames.reimu_arcade_4:  0xFF2003,
    locationnames.reimu_arcade_5:  0xFF2004,
    locationnames.reimu_arcade_6:  0xFF2005,
    locationnames.reimu_arcade_7:  0xFF2006,
    locationnames.reimu_arcade_8:  0xFF2007,
    locationnames.reimu_arcade_9:  0xFF2008,
    locationnames.reimu_arcade_10: 0xFF2009

}

marisa_arcade_stage_table = {
    locationnames.marisa_arcade_1:  0xFF2010,
    locationnames.marisa_arcade_2:  0xFF2011,
    locationnames.marisa_arcade_3:  0xFF2012,
    locationnames.marisa_arcade_4:  0xFF2013,
    locationnames.marisa_arcade_5:  0xFF2014,
    locationnames.marisa_arcade_6:  0xFF2015,
    locationnames.marisa_arcade_7:  0xFF2016,
    locationnames.marisa_arcade_8:  0xFF2017,
    locationnames.marisa_arcade_9:  0xFF2018,
    locationnames.marisa_arcade_10: 0xFF2019,

}

sakuya_arcade_stage_table = {
    locationnames.sakuya_arcade_1:  0xFF2020,
    locationnames.sakuya_arcade_2:  0xFF2021,
    locationnames.sakuya_arcade_3:  0xFF2022,
    locationnames.sakuya_arcade_4:  0xFF2023,
    locationnames.sakuya_arcade_5:  0xFF2024,
    locationnames.sakuya_arcade_6:  0xFF2025,
    locationnames.sakuya_arcade_7:  0xFF2026,
    locationnames.sakuya_arcade_8:  0xFF2027,
    locationnames.sakuya_arcade_9:  0xFF2028,
    locationnames.sakuya_arcade_10: 0xFF2029

}

alice_arcade_stage_table = {
    locationnames.alice_arcade_1:  0xFF2030,
    locationnames.alice_arcade_2:  0xFF2031,
    locationnames.alice_arcade_3:  0xFF2032,
    locationnames.alice_arcade_4:  0xFF2033,
    locationnames.alice_arcade_5:  0xFF2034,
    locationnames.alice_arcade_6:  0xFF2035,
    locationnames.alice_arcade_7:  0xFF2036,
    locationnames.alice_arcade_8:  0xFF2037,
    locationnames.alice_arcade_9:  0xFF2038,
    locationnames.alice_arcade_10: 0xFF2039

}

patchouli_arcade_stage_table = {
    locationnames.patchouli_arcade_1:  0xFF2040,
    locationnames.patchouli_arcade_2:  0xFF2041,
    locationnames.patchouli_arcade_3:  0xFF2042,
    locationnames.patchouli_arcade_4:  0xFF2043,
    locationnames.patchouli_arcade_5:  0xFF2044,
    locationnames.patchouli_arcade_6:  0xFF2045,
    locationnames.patchouli_arcade_7:  0xFF2046,
    locationnames.patchouli_arcade_8:  0xFF2047,
    locationnames.patchouli_arcade_9:  0xFF2048,
    locationnames.patchouli_arcade_10: 0xFF2049

}

youmu_arcade_stage_table = {
    locationnames.youmu_arcade_1:  0xFF2050, 
    locationnames.youmu_arcade_2:  0xFF2051, 
    locationnames.youmu_arcade_3:  0xFF2052, 
    locationnames.youmu_arcade_4:  0xFF2053, 
    locationnames.youmu_arcade_5:  0xFF2054, 
    locationnames.youmu_arcade_6:  0xFF2055, 
    locationnames.youmu_arcade_7:  0xFF2056, 
    locationnames.youmu_arcade_8:  0xFF2057, 
    locationnames.youmu_arcade_9:  0xFF2058, 
    locationnames.youmu_arcade_10: 0xFF2059

}

remilia_arcade_stage_table = {
    locationnames.remilia_arcade_1:  0xFF2060,
    locationnames.remilia_arcade_2:  0xFF2061,
    locationnames.remilia_arcade_3:  0xFF2062,
    locationnames.remilia_arcade_4:  0xFF2063,
    locationnames.remilia_arcade_5:  0xFF2064,
    locationnames.remilia_arcade_6:  0xFF2065,
    locationnames.remilia_arcade_7:  0xFF2066,
    locationnames.remilia_arcade_8:  0xFF2067,
    locationnames.remilia_arcade_9:  0xFF2068,
    locationnames.remilia_arcade_10: 0xFF2069

}

yuyuko_arcade_stage_table = {
    locationnames.yuyuko_arcade_1:  0xFF2070,
    locationnames.yuyuko_arcade_2:  0xFF2071,
    locationnames.yuyuko_arcade_3:  0xFF2072,
    locationnames.yuyuko_arcade_4:  0xFF2073,
    locationnames.yuyuko_arcade_5:  0xFF2074,
    locationnames.yuyuko_arcade_6:  0xFF2075,
    locationnames.yuyuko_arcade_7:  0xFF2076,
    locationnames.yuyuko_arcade_8:  0xFF2077,
    locationnames.yuyuko_arcade_9:  0xFF2078,
    locationnames.yuyuko_arcade_10: 0xFF2079

}

yukari_arcade_stage_table = {
    locationnames.yukari_arcade_1:  0xFF2080,
    locationnames.yukari_arcade_2:  0xFF2081,
    locationnames.yukari_arcade_3:  0xFF2082,
    locationnames.yukari_arcade_4:  0xFF2083,
    locationnames.yukari_arcade_5:  0xFF2084,
    locationnames.yukari_arcade_6:  0xFF2085,
    locationnames.yukari_arcade_7:  0xFF2086,
    locationnames.yukari_arcade_8:  0xFF2087,
    locationnames.yukari_arcade_9:  0xFF2088,
    locationnames.yukari_arcade_10: 0xFF2089

}

suika_arcade_stage_table = {
    locationnames.suika_arcade_1:  0xFF2090,
    locationnames.suika_arcade_2:  0xFF2091,
    locationnames.suika_arcade_3:  0xFF2092,
    locationnames.suika_arcade_4:  0xFF2093,
    locationnames.suika_arcade_5:  0xFF2094,
    locationnames.suika_arcade_6:  0xFF2095,
    locationnames.suika_arcade_7:  0xFF2096,
    locationnames.suika_arcade_8:  0xFF2097,
    locationnames.suika_arcade_9:  0xFF2098,
    locationnames.suika_arcade_10: 0xFF2099

}

reisen_arcade_stage_table = {
    locationnames.reisen_arcade_1:  0xFF20A0, 
    locationnames.reisen_arcade_2:  0xFF20A1, 
    locationnames.reisen_arcade_3:  0xFF20A2, 
    locationnames.reisen_arcade_4:  0xFF20A3, 
    locationnames.reisen_arcade_5:  0xFF20A4, 
    locationnames.reisen_arcade_6:  0xFF20A5, 
    locationnames.reisen_arcade_7:  0xFF20A6, 
    locationnames.reisen_arcade_8:  0xFF20A7, 
    locationnames.reisen_arcade_9:  0xFF20A8, 
    locationnames.reisen_arcade_10: 0xFF20A9 

}

aya_arcade_stage_table = {
    locationnames.aya_arcade_1:  0xFF20B0,
    locationnames.aya_arcade_2:  0xFF20B2,
    locationnames.aya_arcade_3:  0xFF20B2,
    locationnames.aya_arcade_4:  0xFF20B3,
    locationnames.aya_arcade_5:  0xFF20B4,
    locationnames.aya_arcade_6:  0xFF20B5,
    locationnames.aya_arcade_7:  0xFF20B6,
    locationnames.aya_arcade_8:  0xFF20B7,
    locationnames.aya_arcade_9:  0xFF20B8,
    locationnames.aya_arcade_10: 0xFF20B9

}

komachi_arcade_stage_table = {
    locationnames.komachi_arcade_1:  0xFF20C0,
    locationnames.komachi_arcade_2:  0xFF20C1,
    locationnames.komachi_arcade_3:  0xFF20C2,
    locationnames.komachi_arcade_4:  0xFF20C3,
    locationnames.komachi_arcade_5:  0xFF20C4,
    locationnames.komachi_arcade_6:  0xFF20C5,
    locationnames.komachi_arcade_7:  0xFF20C6,
    locationnames.komachi_arcade_8:  0xFF20C7,
    locationnames.komachi_arcade_9:  0xFF20C8,
    locationnames.komachi_arcade_10: 0xFF20C9

}

iku_arcade_stage_table = {
    locationnames.iku_arcade_1:  0xFF20D0,
    locationnames.iku_arcade_2:  0xFF20D1,
    locationnames.iku_arcade_3:  0xFF20D2,
    locationnames.iku_arcade_4:  0xFF20D3,
    locationnames.iku_arcade_5:  0xFF20D4,
    locationnames.iku_arcade_6:  0xFF20D5,
    locationnames.iku_arcade_7:  0xFF20D6,
    locationnames.iku_arcade_8:  0xFF20D7,
    locationnames.iku_arcade_9:  0xFF20D8,
    locationnames.iku_arcade_10: 0xFF20D9

}

tenshi_arcade_stage_table = {
    locationnames.tenshi_arcade_1:  0xFF20E0,
    locationnames.tenshi_arcade_2:  0xFF20E1,
    locationnames.tenshi_arcade_3:  0xFF20E2,
    locationnames.tenshi_arcade_4:  0xFF20E3,
    locationnames.tenshi_arcade_5:  0xFF20E4,
    locationnames.tenshi_arcade_6:  0xFF20E5,
    locationnames.tenshi_arcade_7:  0xFF20E6,
    locationnames.tenshi_arcade_8:  0xFF20E7,
    locationnames.tenshi_arcade_9:  0xFF20E8,
    locationnames.tenshi_arcade_10: 0xFF20E9

}

sanae_arcade_stage_table = {
    locationnames.sanae_arcade_1:  0xFF20F0,
    locationnames.sanae_arcade_2:  0xFF20F1,
    locationnames.sanae_arcade_3:  0xFF20F2,
    locationnames.sanae_arcade_4:  0xFF20F3,
    locationnames.sanae_arcade_5:  0xFF20F4,
    locationnames.sanae_arcade_6:  0xFF20F5,
    locationnames.sanae_arcade_7:  0xFF20F6,
    locationnames.sanae_arcade_8:  0xFF20F7,
    locationnames.sanae_arcade_9:  0xFF20F8,
    locationnames.sanae_arcade_10: 0xFF20F9

}

cirno_arcade_stage_table = {
    locationnames.cirno_arcade_1:  0xFF2100,
    locationnames.cirno_arcade_2:  0xFF2101,
    locationnames.cirno_arcade_3:  0xFF2102,
    locationnames.cirno_arcade_4:  0xFF2103,
    locationnames.cirno_arcade_5:  0xFF2104,
    locationnames.cirno_arcade_6:  0xFF2105,
    locationnames.cirno_arcade_7:  0xFF2106,
    locationnames.cirno_arcade_8:  0xFF2107,
    locationnames.cirno_arcade_9:  0xFF2108,
    locationnames.cirno_arcade_10: 0xFF2109

}

meiling_arcade_stage_table = {
    locationnames.meiling_arcade_1:  0xFF2110,
    locationnames.meiling_arcade_2:  0xFF2111,
    locationnames.meiling_arcade_3:  0xFF2112,
    locationnames.meiling_arcade_4:  0xFF2113,
    locationnames.meiling_arcade_5:  0xFF2114,
    locationnames.meiling_arcade_6:  0xFF2115,
    locationnames.meiling_arcade_7:  0xFF2116,
    locationnames.meiling_arcade_8:  0xFF2117,
    locationnames.meiling_arcade_9:  0xFF2118,
    locationnames.meiling_arcade_10: 0xFF2119

}

okuu_arcade_stage_table = {
    locationnames.okuu_arcade_1:  0xFF2120, 
    locationnames.okuu_arcade_2:  0xFF2121, 
    locationnames.okuu_arcade_3:  0xFF2122, 
    locationnames.okuu_arcade_4:  0xFF2123, 
    locationnames.okuu_arcade_5:  0xFF2124, 
    locationnames.okuu_arcade_6:  0xFF2125, 
    locationnames.okuu_arcade_7:  0xFF2126, 
    locationnames.okuu_arcade_8:  0xFF2127, 
    locationnames.okuu_arcade_9:  0xFF2128, 
    locationnames.okuu_arcade_10: 0xFF2129

}

suwako_arcade_stage_table = {
    locationnames.suwako_arcade_1:  0xFF2130,
    locationnames.suwako_arcade_2:  0xFF2131,
    locationnames.suwako_arcade_3:  0xFF2132,
    locationnames.suwako_arcade_4:  0xFF2133,
    locationnames.suwako_arcade_5:  0xFF2134,
    locationnames.suwako_arcade_6:  0xFF2135,
    locationnames.suwako_arcade_7:  0xFF2136,
    locationnames.suwako_arcade_8:  0xFF2137,
    locationnames.suwako_arcade_9:  0xFF2138,
    locationnames.suwako_arcade_10: 0xFF2139

}
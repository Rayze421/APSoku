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

reimu_vs_win_table = {
    locationnames.reimu_vs_w1:  0xFF3000,
    locationnames.reimu_vs_w2:  0xFF3001,
    locationnames.reimu_vs_w3:  0xFF3002,
    locationnames.reimu_vs_w4:  0xFF3003,
    locationnames.reimu_vs_w5:  0xFF3004,
    locationnames.reimu_vs_w6:  0xFF3005,
    locationnames.reimu_vs_w7:  0xFF3006,
    locationnames.reimu_vs_w8:  0xFF3007,
    locationnames.reimu_vs_w9:  0xFF3008,
    locationnames.reimu_vs_w10: 0xFF3009

}

marisa_vs_win_table = {
    locationnames.marisa_vs_w1:  0xFF3010,
    locationnames.marisa_vs_w2:  0xFF3011,
    locationnames.marisa_vs_w3:  0xFF3012,
    locationnames.marisa_vs_w4:  0xFF3013,
    locationnames.marisa_vs_w5:  0xFF3014,
    locationnames.marisa_vs_w6:  0xFF3015,
    locationnames.marisa_vs_w7:  0xFF3016,
    locationnames.marisa_vs_w8:  0xFF3017,
    locationnames.marisa_vs_w9:  0xFF3018,
    locationnames.marisa_vs_w10: 0xFF3019

}

sakuya_vs_win_table = {
    locationnames.sakuya_vs_w1:  0xFF3020,
    locationnames.sakuya_vs_w2:  0xFF3021,
    locationnames.sakuya_vs_w3:  0xFF3022,
    locationnames.sakuya_vs_w4:  0xFF3023,
    locationnames.sakuya_vs_w5:  0xFF3024,
    locationnames.sakuya_vs_w6:  0xFF3025,
    locationnames.sakuya_vs_w7:  0xFF3026,
    locationnames.sakuya_vs_w8:  0xFF3027,
    locationnames.sakuya_vs_w9:  0xFF3028,
    locationnames.sakuya_vs_w10: 0xFF3029

}

alice_vs_win_table = {
    locationnames.alice_vs_w1:  0xFF3030,
    locationnames.alice_vs_w2:  0xFF3031,
    locationnames.alice_vs_w3:  0xFF3032,
    locationnames.alice_vs_w4:  0xFF3033,
    locationnames.alice_vs_w5:  0xFF3034,
    locationnames.alice_vs_w6:  0xFF3035,
    locationnames.alice_vs_w7:  0xFF3036,
    locationnames.alice_vs_w8:  0xFF3037,
    locationnames.alice_vs_w9:  0xFF3038,
    locationnames.alice_vs_w10: 0xFF3039

}

patchouli_vs_win_table = {
    locationnames.patchouli_vs_w1:  0xFF3040,
    locationnames.patchouli_vs_w2:  0xFF3041,
    locationnames.patchouli_vs_w3:  0xFF3042,
    locationnames.patchouli_vs_w4:  0xFF3043,
    locationnames.patchouli_vs_w5:  0xFF3044,
    locationnames.patchouli_vs_w6:  0xFF3045,
    locationnames.patchouli_vs_w7:  0xFF3046,
    locationnames.patchouli_vs_w8:  0xFF3047,
    locationnames.patchouli_vs_w9:  0xFF3048,
    locationnames.patchouli_vs_w10: 0xFF3049

}

youmu_vs_win_table = {
    locationnames.youmu_vs_w1:  0xFF3050,
    locationnames.youmu_vs_w2:  0xFF3051,
    locationnames.youmu_vs_w3:  0xFF3052,
    locationnames.youmu_vs_w4:  0xFF3053,
    locationnames.youmu_vs_w5:  0xFF3054,
    locationnames.youmu_vs_w6:  0xFF3055,
    locationnames.youmu_vs_w7:  0xFF3056,
    locationnames.youmu_vs_w8:  0xFF3057,
    locationnames.youmu_vs_w9:  0xFF3058,
    locationnames.youmu_vs_w10: 0xFF3059

}

remilia_vs_win_table = {
    locationnames.remilia_vs_w1:  0xFF3060,
    locationnames.remilia_vs_w2:  0xFF3061,
    locationnames.remilia_vs_w3:  0xFF3062,
    locationnames.remilia_vs_w4:  0xFF3063,
    locationnames.remilia_vs_w5:  0xFF3064,
    locationnames.remilia_vs_w6:  0xFF3065,
    locationnames.remilia_vs_w7:  0xFF3066,
    locationnames.remilia_vs_w8:  0xFF3067,
    locationnames.remilia_vs_w9:  0xFF3068,
    locationnames.remilia_vs_w10: 0xFF3069

}

yuyuko_vs_win_table = {
    locationnames.yuyuko_vs_w1:  0xFF3070,
    locationnames.yuyuko_vs_w2:  0xFF3071,
    locationnames.yuyuko_vs_w3:  0xFF3072,
    locationnames.yuyuko_vs_w4:  0xFF3073,
    locationnames.yuyuko_vs_w5:  0xFF3074,
    locationnames.yuyuko_vs_w6:  0xFF3075,
    locationnames.yuyuko_vs_w7:  0xFF3076,
    locationnames.yuyuko_vs_w8:  0xFF3077,
    locationnames.yuyuko_vs_w9:  0xFF3078,
    locationnames.yuyuko_vs_w10: 0xFF3079

}

yukari_vs_win_table = {
    locationnames.yukari_vs_w1:  0xFF3080,
    locationnames.yukari_vs_w2:  0xFF3081,
    locationnames.yukari_vs_w3:  0xFF3082,
    locationnames.yukari_vs_w4:  0xFF3083,
    locationnames.yukari_vs_w5:  0xFF3084,
    locationnames.yukari_vs_w6:  0xFF3085,
    locationnames.yukari_vs_w7:  0xFF3086,
    locationnames.yukari_vs_w8:  0xFF3087,
    locationnames.yukari_vs_w9:  0xFF3088,
    locationnames.yukari_vs_w10: 0xFF3089

}

suika_vs_win_table = {
    locationnames.suika_vs_w1:  0xFF3090, 
    locationnames.suika_vs_w2:  0xFF3091, 
    locationnames.suika_vs_w3:  0xFF3092, 
    locationnames.suika_vs_w4:  0xFF3093, 
    locationnames.suika_vs_w5:  0xFF3094, 
    locationnames.suika_vs_w6:  0xFF3095, 
    locationnames.suika_vs_w7:  0xFF3096, 
    locationnames.suika_vs_w8:  0xFF3097, 
    locationnames.suika_vs_w9:  0xFF3098, 
    locationnames.suika_vs_w10: 0xFF3099

}

reisen_vs_win_table = {
    locationnames.reisen_vs_w1:  0xFF30A0,
    locationnames.reisen_vs_w2:  0xFF30A1,
    locationnames.reisen_vs_w3:  0xFF30A2,
    locationnames.reisen_vs_w4:  0xFF30A3,
    locationnames.reisen_vs_w5:  0xFF30A4,
    locationnames.reisen_vs_w6:  0xFF30A5,
    locationnames.reisen_vs_w7:  0xFF30A6,
    locationnames.reisen_vs_w8:  0xFF30A7,
    locationnames.reisen_vs_w9:  0xFF30A8,
    locationnames.reisen_vs_w10: 0xFF30A9

}

aya_vs_win_table = {
    locationnames.aya_vs_w1:  0xFF30B0,
    locationnames.aya_vs_w2:  0xFF30B1,
    locationnames.aya_vs_w3:  0xFF30B2,
    locationnames.aya_vs_w4:  0xFF30B3,
    locationnames.aya_vs_w5:  0xFF30B4,
    locationnames.aya_vs_w6:  0xFF30B5,
    locationnames.aya_vs_w7:  0xFF30B6,
    locationnames.aya_vs_w8:  0xFF30B7,
    locationnames.aya_vs_w9:  0xFF30B8,
    locationnames.aya_vs_w10: 0xFF30B9

}

komachi_vs_win_table = {
    locationnames.komachi_vs_w1:  0xFF30C0,
    locationnames.komachi_vs_w2:  0xFF30C0,
    locationnames.komachi_vs_w3:  0xFF30C0,
    locationnames.komachi_vs_w4:  0xFF30C0,
    locationnames.komachi_vs_w5:  0xFF30C0,
    locationnames.komachi_vs_w6:  0xFF30C0,
    locationnames.komachi_vs_w7:  0xFF30C0,
    locationnames.komachi_vs_w8:  0xFF30C0,
    locationnames.komachi_vs_w9:  0xFF30C0,
    locationnames.komachi_vs_w10: 0xFF30C0

}

iku_vs_win_table = {
    locationnames.iku_vs_w1:  0xFF30D0,
    locationnames.iku_vs_w2:  0xFF30D1,
    locationnames.iku_vs_w3:  0xFF30D2,
    locationnames.iku_vs_w4:  0xFF30D3,
    locationnames.iku_vs_w5:  0xFF30D4,
    locationnames.iku_vs_w6:  0xFF30D5,
    locationnames.iku_vs_w7:  0xFF30D6,
    locationnames.iku_vs_w8:  0xFF30D7,
    locationnames.iku_vs_w9:  0xFF30D8,
    locationnames.iku_vs_w10: 0xFF30D9

}

tenshi_vs_win_table = {
    locationnames.tenshi_vs_w1:  0xFF30E0,
    locationnames.tenshi_vs_w2:  0xFF30E1,
    locationnames.tenshi_vs_w3:  0xFF30E2,
    locationnames.tenshi_vs_w4:  0xFF30E3,
    locationnames.tenshi_vs_w5:  0xFF30E4,
    locationnames.tenshi_vs_w6:  0xFF30E5,
    locationnames.tenshi_vs_w7:  0xFF30E6,
    locationnames.tenshi_vs_w8:  0xFF30E7,
    locationnames.tenshi_vs_w9:  0xFF30E8,
    locationnames.tenshi_vs_w10: 0xFF30E9

}

sanae_vs_win_table = {
    locationnames.sanae_vs_w1:  0xFF30F0,
    locationnames.sanae_vs_w2:  0xFF30F1,
    locationnames.sanae_vs_w3:  0xFF30F2,
    locationnames.sanae_vs_w4:  0xFF30F3,
    locationnames.sanae_vs_w5:  0xFF30F4,
    locationnames.sanae_vs_w6:  0xFF30F5,
    locationnames.sanae_vs_w7:  0xFF30F6,
    locationnames.sanae_vs_w8:  0xFF30F7,
    locationnames.sanae_vs_w9:  0xFF30F8,
    locationnames.sanae_vs_w10: 0xFF30F9

}

cirno_vs_win_table = {
    locationnames.cirno_vs_w1:  0xFF3100,
    locationnames.cirno_vs_w2:  0xFF3101,
    locationnames.cirno_vs_w3:  0xFF3102,
    locationnames.cirno_vs_w4:  0xFF3103,
    locationnames.cirno_vs_w5:  0xFF3104,
    locationnames.cirno_vs_w6:  0xFF3105,
    locationnames.cirno_vs_w7:  0xFF3106,
    locationnames.cirno_vs_w8:  0xFF3107,
    locationnames.cirno_vs_w9:  0xFF3108,
    locationnames.cirno_vs_w10: 0xFF3109

}

meiling_vs_win_table = {
    locationnames.meiling_vs_w1:  0xFF3110,
    locationnames.meiling_vs_w2:  0xFF3111,
    locationnames.meiling_vs_w3:  0xFF3112,
    locationnames.meiling_vs_w4:  0xFF3113,
    locationnames.meiling_vs_w5:  0xFF3114,
    locationnames.meiling_vs_w6:  0xFF3115,
    locationnames.meiling_vs_w7:  0xFF3116,
    locationnames.meiling_vs_w8:  0xFF3117,
    locationnames.meiling_vs_w9:  0xFF3118,
    locationnames.meiling_vs_w10: 0xFF3119

}

okuu_vs_win_table = {
    locationnames.okuu_vs_w1:  0xFF3120,
    locationnames.okuu_vs_w2:  0xFF3121,
    locationnames.okuu_vs_w3:  0xFF3122,
    locationnames.okuu_vs_w4:  0xFF3123,
    locationnames.okuu_vs_w5:  0xFF3124,
    locationnames.okuu_vs_w6:  0xFF3125,
    locationnames.okuu_vs_w7:  0xFF3126,
    locationnames.okuu_vs_w8:  0xFF3127,
    locationnames.okuu_vs_w9:  0xFF3128,
    locationnames.okuu_vs_w10: 0xFF3129

}

suwako_vs_win_table = {
    locationnames.suwako_vs_w1:  0xFF3130,
    locationnames.suwako_vs_w2:  0xFF3131,
    locationnames.suwako_vs_w3:  0xFF3132,
    locationnames.suwako_vs_w4:  0xFF3133,
    locationnames.suwako_vs_w5:  0xFF3134,
    locationnames.suwako_vs_w6:  0xFF3135,
    locationnames.suwako_vs_w7:  0xFF3136,
    locationnames.suwako_vs_w8:  0xFF3137,
    locationnames.suwako_vs_w9:  0xFF3138,
    locationnames.suwako_vs_w10: 0xFF3139

}

reimu_vs_defeat_table = {
    locationnames.reimu_vs_l1:  0xFF4000,
    locationnames.reimu_vs_l2:  0xFF4001,
    locationnames.reimu_vs_l3:  0xFF4002,
    locationnames.reimu_vs_l4:  0xFF4003,
    locationnames.reimu_vs_l5:  0xFF4004,
    locationnames.reimu_vs_l6:  0xFF4005,
    locationnames.reimu_vs_l7:  0xFF4006,
    locationnames.reimu_vs_l8:  0xFF4007,
    locationnames.reimu_vs_l9:  0xFF4008,
    locationnames.reimu_vs_l10: 0xFF4009

}

marisa_vs_defeat_table = {
    locationnames.marisa_vs_l1:  0xFF4010,
    locationnames.marisa_vs_l2:  0xFF4011,
    locationnames.marisa_vs_l3:  0xFF4012,
    locationnames.marisa_vs_l4:  0xFF4013,
    locationnames.marisa_vs_l5:  0xFF4014,
    locationnames.marisa_vs_l6:  0xFF4015,
    locationnames.marisa_vs_l7:  0xFF4016,
    locationnames.marisa_vs_l8:  0xFF4017,
    locationnames.marisa_vs_l9:  0xFF4018,
    locationnames.marisa_vs_l10: 0xFF4019

}

sakuya_vs_defeat_table = {
    locationnames.sakuya_vs_l1:  0xFF4020,
    locationnames.sakuya_vs_l2:  0xFF4021,
    locationnames.sakuya_vs_l3:  0xFF4022,
    locationnames.sakuya_vs_l4:  0xFF4023,
    locationnames.sakuya_vs_l5:  0xFF4024,
    locationnames.sakuya_vs_l6:  0xFF4025,
    locationnames.sakuya_vs_l7:  0xFF4026,
    locationnames.sakuya_vs_l8:  0xFF4027,
    locationnames.sakuya_vs_l9:  0xFF4028,
    locationnames.sakuya_vs_l10: 0xFF4029

}

alice_vs_defeat_table = {
    locationnames.alice_vs_l1:   0xFF4030,
    locationnames.alice_vs_l2:   0xFF4031,
    locationnames.alice_vs_l3:   0xFF4032,
    locationnames.alice_vs_l4:   0xFF4033,
    locationnames.alice_vs_l5:   0xFF4034,
    locationnames.alice_vs_l6:   0xFF4035,
    locationnames.alice_vs_l7:   0xFF4036,
    locationnames.alice_vs_l8:   0xFF4037,
    locationnames.alice_vs_l9:   0xFF4038,
    locationnames.alice_vs_l10:  0xFF4039

}

patchouli_vs_defeat_table = {
    locationnames.patchouli_vs_l1:  0xFF4040,
    locationnames.patchouli_vs_l2:  0xFF4041,
    locationnames.patchouli_vs_l3:  0xFF4042,
    locationnames.patchouli_vs_l4:  0xFF4043,
    locationnames.patchouli_vs_l5:  0xFF4044,
    locationnames.patchouli_vs_l6:  0xFF4045,
    locationnames.patchouli_vs_l7:  0xFF4046,
    locationnames.patchouli_vs_l8:  0xFF4047,
    locationnames.patchouli_vs_l9:  0xFF4048,
    locationnames.patchouli_vs_l10: 0xFF4049

}

youmu_vs_defeat_table = {
    locationnames.youmu_vs_l1:  0xFF4050,
    locationnames.youmu_vs_l2:  0xFF4051,
    locationnames.youmu_vs_l3:  0xFF4052,
    locationnames.youmu_vs_l4:  0xFF4053,
    locationnames.youmu_vs_l5:  0xFF4054,
    locationnames.youmu_vs_l6:  0xFF4055,
    locationnames.youmu_vs_l7:  0xFF4056,
    locationnames.youmu_vs_l8:  0xFF4057,
    locationnames.youmu_vs_l9:  0xFF4058,
    locationnames.youmu_vs_l10: 0xFF4059

}

remilia_vs_defeat_table = {
    locationnames.remilia_vs_l1:  0xFF4060,
    locationnames.remilia_vs_l2:  0xFF4061,
    locationnames.remilia_vs_l3:  0xFF4062,
    locationnames.remilia_vs_l4:  0xFF4063,
    locationnames.remilia_vs_l5:  0xFF4064,
    locationnames.remilia_vs_l6:  0xFF4065,
    locationnames.remilia_vs_l7:  0xFF4066,
    locationnames.remilia_vs_l8:  0xFF4067,
    locationnames.remilia_vs_l9:  0xFF4068,
    locationnames.remilia_vs_l10: 0xFF4069

}

yuyuko_vs_defeat_table = {
    locationnames.yuyuko_vs_l1:  0xFF4070,
    locationnames.yuyuko_vs_l2:  0xFF4071,
    locationnames.yuyuko_vs_l3:  0xFF4072,
    locationnames.yuyuko_vs_l4:  0xFF4073,
    locationnames.yuyuko_vs_l5:  0xFF4074,
    locationnames.yuyuko_vs_l6:  0xFF4075,
    locationnames.yuyuko_vs_l7:  0xFF4076,
    locationnames.yuyuko_vs_l8:  0xFF4077,
    locationnames.yuyuko_vs_l9:  0xFF4078,
    locationnames.yuyuko_vs_l10: 0xFF4079

}

yukari_vs_defeat_table = {
    locationnames.yukari_vs_l1:  0xFF4080,
    locationnames.yukari_vs_l2:  0xFF4081,
    locationnames.yukari_vs_l3:  0xFF4082,
    locationnames.yukari_vs_l4:  0xFF4083,
    locationnames.yukari_vs_l5:  0xFF4084,
    locationnames.yukari_vs_l6:  0xFF4085,
    locationnames.yukari_vs_l7:  0xFF4086,
    locationnames.yukari_vs_l8:  0xFF4087,
    locationnames.yukari_vs_l9:  0xFF4088,
    locationnames.yukari_vs_l10: 0xFF4089

}

suika_vs_defeat_table = {
    locationnames.suika_vs_l1:  0xFF4090,
    locationnames.suika_vs_l2:  0xFF4091,
    locationnames.suika_vs_l3:  0xFF4092,
    locationnames.suika_vs_l4:  0xFF4093,
    locationnames.suika_vs_l5:  0xFF4094,
    locationnames.suika_vs_l6:  0xFF4095,
    locationnames.suika_vs_l7:  0xFF4096,
    locationnames.suika_vs_l8:  0xFF4097,
    locationnames.suika_vs_l9:  0xFF4098,
    locationnames.suika_vs_l10: 0xFF4099

}

reisen_vs_defeat_table = {
    locationnames.reisen_vs_l1:  0xFF40A0,
    locationnames.reisen_vs_l2:  0xFF40A1,
    locationnames.reisen_vs_l3:  0xFF40A2,
    locationnames.reisen_vs_l4:  0xFF40A3,
    locationnames.reisen_vs_l5:  0xFF40A4,
    locationnames.reisen_vs_l6:  0xFF40A5,
    locationnames.reisen_vs_l7:  0xFF40A6,
    locationnames.reisen_vs_l8:  0xFF40A7,
    locationnames.reisen_vs_l9:  0xFF40A8,
    locationnames.reisen_vs_l10: 0xFF40A9

}

aya_vs_defeat_table = {
    locationnames.aya_vs_l1:  0xFF40B0,
    locationnames.aya_vs_l2:  0xFF40B1,
    locationnames.aya_vs_l3:  0xFF40B2,
    locationnames.aya_vs_l4:  0xFF40B3,
    locationnames.aya_vs_l5:  0xFF40B4,
    locationnames.aya_vs_l6:  0xFF40B5,
    locationnames.aya_vs_l7:  0xFF40B6,
    locationnames.aya_vs_l8:  0xFF40B7,
    locationnames.aya_vs_l9:  0xFF40B8,
    locationnames.aya_vs_l10: 0xFF40B9

}

komachi_vs_defeat_table = {
    locationnames.komachi_vs_l1:  0xFF40C0,
    locationnames.komachi_vs_l2:  0xFF40C1,
    locationnames.komachi_vs_l3:  0xFF40C2,
    locationnames.komachi_vs_l4:  0xFF40C3,
    locationnames.komachi_vs_l5:  0xFF40C4,
    locationnames.komachi_vs_l6:  0xFF40C5,
    locationnames.komachi_vs_l7:  0xFF40C6,
    locationnames.komachi_vs_l8:  0xFF40C7,
    locationnames.komachi_vs_l9:  0xFF40C8,
    locationnames.komachi_vs_l10: 0xFF40C9

}

iku_vs_defeat_table = {
    locationnames.iku_vs_l1:  0xFF40D0,
    locationnames.iku_vs_l2:  0xFF40D1,
    locationnames.iku_vs_l3:  0xFF40D2,
    locationnames.iku_vs_l4:  0xFF40D3,
    locationnames.iku_vs_l5:  0xFF40D4,
    locationnames.iku_vs_l6:  0xFF40D5,
    locationnames.iku_vs_l7:  0xFF40D6,
    locationnames.iku_vs_l8:  0xFF40D7,
    locationnames.iku_vs_l9:  0xFF40D8,
    locationnames.iku_vs_l10: 0xFF40D9

}

tenshi_vs_defeat_table = {
    locationnames.tenshi_vs_l1:  0xFF40E0,
    locationnames.tenshi_vs_l2:  0xFF40E1,
    locationnames.tenshi_vs_l3:  0xFF40E2,
    locationnames.tenshi_vs_l4:  0xFF40E3,
    locationnames.tenshi_vs_l5:  0xFF40E4,
    locationnames.tenshi_vs_l6:  0xFF40E5,
    locationnames.tenshi_vs_l7:  0xFF40E6,
    locationnames.tenshi_vs_l8:  0xFF40E7,
    locationnames.tenshi_vs_l9:  0xFF40E8,
    locationnames.tenshi_vs_l10: 0xFF40E9

}

sanae_vs_defeat_table = {
    locationnames.sanae_vs_l1:  0xFF40F0,
    locationnames.sanae_vs_l2:  0xFF40F1,
    locationnames.sanae_vs_l3:  0xFF40F2,
    locationnames.sanae_vs_l4:  0xFF40F3,
    locationnames.sanae_vs_l5:  0xFF40F4,
    locationnames.sanae_vs_l6:  0xFF40F5,
    locationnames.sanae_vs_l7:  0xFF40F6,
    locationnames.sanae_vs_l8:  0xFF40F7,
    locationnames.sanae_vs_l9:  0xFF40F8,
    locationnames.sanae_vs_l10: 0xFF40F9

}

cirno_vs_defeat_table = {
    locationnames.cirno_vs_l1:  0xFF4100,
    locationnames.cirno_vs_l2:  0xFF4101,
    locationnames.cirno_vs_l3:  0xFF4102,
    locationnames.cirno_vs_l4:  0xFF4103,
    locationnames.cirno_vs_l5:  0xFF4104,
    locationnames.cirno_vs_l6:  0xFF4105,
    locationnames.cirno_vs_l7:  0xFF4106,
    locationnames.cirno_vs_l8:  0xFF4107,
    locationnames.cirno_vs_l9:  0xFF4108,
    locationnames.cirno_vs_l10: 0xFF4109

}

meiling_vs_defeat_table = {
    locationnames.meiling_vs_l1:  0xFF4110,
    locationnames.meiling_vs_l2:  0xFF4111,
    locationnames.meiling_vs_l3:  0xFF4112,
    locationnames.meiling_vs_l4:  0xFF4113,
    locationnames.meiling_vs_l5:  0xFF4114,
    locationnames.meiling_vs_l6:  0xFF4115,
    locationnames.meiling_vs_l7:  0xFF4116,
    locationnames.meiling_vs_l8:  0xFF4117,
    locationnames.meiling_vs_l9:  0xFF4118,
    locationnames.meiling_vs_l10: 0xFF4119

}

okuu_vs_defeat_table = {
    locationnames.okuu_vs_l1:  0xFF4120,
    locationnames.okuu_vs_l2:  0xFF4121,
    locationnames.okuu_vs_l3:  0xFF4122,
    locationnames.okuu_vs_l4:  0xFF4123,
    locationnames.okuu_vs_l5:  0xFF4124,
    locationnames.okuu_vs_l6:  0xFF4125,
    locationnames.okuu_vs_l7:  0xFF4126,
    locationnames.okuu_vs_l8:  0xFF4127,
    locationnames.okuu_vs_l9:  0xFF4128,
    locationnames.okuu_vs_l10: 0xFF4129

}

suwako_vs_defeat_table = {
    locationnames.suwako_vs_l1:  0xFF4130,
    locationnames.suwako_vs_l2:  0xFF4131,
    locationnames.suwako_vs_l3:  0xFF4132,
    locationnames.suwako_vs_l4:  0xFF4133,
    locationnames.suwako_vs_l5:  0xFF4134,
    locationnames.suwako_vs_l6:  0xFF4135,
    locationnames.suwako_vs_l7:  0xFF4136,
    locationnames.suwako_vs_l8:  0xFF4137,
    locationnames.suwako_vs_l9:  0xFF4138,
    locationnames.suwako_vs_l10: 0xFF4139

}

start_sys_card_table = {
    locationnames.sys_start_card1:   0xFF50000,
    locationnames.sys_start_card2:   0xFF50001,
    locationnames.sys_start_card3:   0xFF50002,
    locationnames.sys_start_card4:   0xFF50003,
    locationnames.sys_start_card5:   0xFF50004,
    locationnames.sys_start_card6:   0xFF50005,
    locationnames.sys_start_card7:   0xFF50006,
    locationnames.sys_start_card8:   0xFF50007,
    locationnames.sys_start_card9:   0xFF50008,
    locationnames.sys_start_card10:  0xFF50009,
    locationnames.sys_start_card11:  0xFF5000A,
    locationnames.sys_start_card12:  0xFF5000B,
    locationnames.sys_start_card13:  0xFF5000C,
    locationnames.sys_start_card14:  0xFF5000D,
    locationnames.sys_start_card15:  0xFF5000E,
    locationnames.sys_start_card16:  0xFF5000F,
    locationnames.sys_start_card17:  0xFF50010,
    locationnames.sys_start_card18:  0xFF50011,
    locationnames.sys_start_card19:  0xFF50012,
    locationnames.sys_start_card20:  0xFF50013,
    locationnames.sys_start_card21:  0xFF50014

}

start_reimu_card_table = { #0xFF50100-FF50115
    locationnames.reimu_start_card1:   0xFF50100,
    locationnames.reimu_start_card2:   0xFF50101,
    locationnames.reimu_start_card3:   0xFF50102,
    locationnames.reimu_start_card4:   0xFF50103,
    locationnames.reimu_start_card5:   0xFF50104,
    locationnames.reimu_start_card6:   0xFF50105,
    locationnames.reimu_start_card7:   0xFF50106,
    locationnames.reimu_start_card8:   0xFF50107,
    locationnames.reimu_start_card9:   0xFF50108,
    locationnames.reimu_start_card10:  0xFF50109,
    locationnames.reimu_start_card11:  0xFF5010A,
    locationnames.reimu_start_card12:  0xFF5010B,
    locationnames.reimu_start_card13:  0xFF5010C,
    locationnames.reimu_start_card14:  0xFF5010D,
    locationnames.reimu_start_card15:  0xFF5010E,
    locationnames.reimu_start_card16:  0xFF5010F,
    locationnames.reimu_start_card17:  0xFF50110,
    locationnames.reimu_start_card18:  0xFF50111,
    locationnames.reimu_start_card19:  0xFF50112,
    locationnames.reimu_start_card20:  0xFF50113,
    locationnames.reimu_start_card21:  0xFF50114,
    locationnames.reimu_start_card22:  0xFF50115

}

start_marisa_card_table = { #0xFF50200-FF50219
    locationnames.marisa_start_card1:   0xFF50200,
    locationnames.marisa_start_card2:   0xFF50201,
    locationnames.marisa_start_card3:   0xFF50202,
    locationnames.marisa_start_card4:   0xFF50203,
    locationnames.marisa_start_card5:   0xFF50204,
    locationnames.marisa_start_card6:   0xFF50205,
    locationnames.marisa_start_card7:   0xFF50206,
    locationnames.marisa_start_card8:   0xFF50207,
    locationnames.marisa_start_card9:   0xFF50208,
    locationnames.marisa_start_card10:  0xFF50209,
    locationnames.marisa_start_card11:  0xFF5020A,
    locationnames.marisa_start_card12:  0xFF5020B,
    locationnames.marisa_start_card13:  0xFF5020C,
    locationnames.marisa_start_card14:  0xFF5020D,
    locationnames.marisa_start_card15:  0xFF5020E,
    locationnames.marisa_start_card16:  0xFF5020F,
    locationnames.marisa_start_card17:  0xFF50210,
    locationnames.marisa_start_card18:  0xFF50211,
    locationnames.marisa_start_card19:  0xFF50212,
    locationnames.marisa_start_card20:  0xFF50213,
    locationnames.marisa_start_card21:  0xFF50214,
    locationnames.marisa_start_card22:  0xFF50215,
    locationnames.marisa_start_card23:  0xFF50216,
    locationnames.marisa_start_card24:  0xFF50217,
    locationnames.marisa_start_card25:  0xFF50218,
    locationnames.marisa_start_card26:  0xFF50219

}

sakuya_start_card_table = { #0xFF50300 - FF50318
    locationnames.sakuya_start_card1:   0xFF50300,
    locationnames.sakuya_start_card2:   0xFF50301,
    locationnames.sakuya_start_card3:   0xFF50302,
    locationnames.sakuya_start_card4:   0xFF50303,
    locationnames.sakuya_start_card5:   0xFF50304,
    locationnames.sakuya_start_card6:   0xFF50305,
    locationnames.sakuya_start_card7:   0xFF50306,
    locationnames.sakuya_start_card8:   0xFF50307,
    locationnames.sakuya_start_card9:   0xFF50308,
    locationnames.sakuya_start_card10:  0xFF50309,
    locationnames.sakuya_start_card11:  0xFF5030A,
    locationnames.sakuya_start_card12:  0xFF5030B,
    locationnames.sakuya_start_card13:  0xFF5030C,
    locationnames.sakuya_start_card14:  0xFF5030D,
    locationnames.sakuya_start_card15:  0xFF5030E,
    locationnames.sakuya_start_card16:  0xFF5030F,
    locationnames.sakuya_start_card17:  0xFF50310,
    locationnames.sakuya_start_card18:  0xFF50311,
    locationnames.sakuya_start_card19:  0xFF50312,
    locationnames.sakuya_start_card20:  0xFF50313,
    locationnames.sakuya_start_card21:  0xFF50314,
    locationnames.sakuya_start_card22:  0xFF50315,
    locationnames.sakuya_start_card23:  0xFF50316,
    locationnames.sakuya_start_card24:  0xFF50317,
    locationnames.sakuya_start_card25:  0xFF50318

}

alice_start_card_table = { #0xFF50400 - FF50417
    locationnames.alice_start_card1:   0xFF50400,
    locationnames.alice_start_card2:   0xFF50401,
    locationnames.alice_start_card3:   0xFF50402,
    locationnames.alice_start_card4:   0xFF50403,
    locationnames.alice_start_card5:   0xFF50404,
    locationnames.alice_start_card6:   0xFF50405,
    locationnames.alice_start_card7:   0xFF50406,
    locationnames.alice_start_card8:   0xFF50407,
    locationnames.alice_start_card9:   0xFF50408,
    locationnames.alice_start_card10:  0xFF50409,
    locationnames.alice_start_card11:  0xFF5040A,
    locationnames.alice_start_card12:  0xFF5040B,
    locationnames.alice_start_card13:  0xFF5040C,
    locationnames.alice_start_card14:  0xFF5040D,
    locationnames.alice_start_card15:  0xFF5040E,
    locationnames.alice_start_card16:  0xFF5040F,
    locationnames.alice_start_card17:  0xFF50410,
    locationnames.alice_start_card18:  0xFF50411,
    locationnames.alice_start_card19:  0xFF50412,
    locationnames.alice_start_card20:  0xFF50413,
    locationnames.alice_start_card21:  0xFF50414,
    locationnames.alice_start_card22:  0xFF50415,
    locationnames.alice_start_card23:  0xFF50416,
    locationnames.alice_start_card24:  0xFF50417

}

patchouli_start_card_table = { #0xFF50500 - FF5051A
    locationnames.patchouli_start_card1:   0xFF50500, 
    locationnames.patchouli_start_card2:   0xFF50501, 
    locationnames.patchouli_start_card3:   0xFF50502, 
    locationnames.patchouli_start_card4:   0xFF50503, 
    locationnames.patchouli_start_card5:   0xFF50504, 
    locationnames.patchouli_start_card6:   0xFF50505, 
    locationnames.patchouli_start_card7:   0xFF50506, 
    locationnames.patchouli_start_card8:   0xFF50507, 
    locationnames.patchouli_start_card9:   0xFF50508, 
    locationnames.patchouli_start_card10:  0xFF50509, 
    locationnames.patchouli_start_card11:  0xFF5050A, 
    locationnames.patchouli_start_card12:  0xFF5050B, 
    locationnames.patchouli_start_card13:  0xFF5050C, 
    locationnames.patchouli_start_card14:  0xFF5050D, 
    locationnames.patchouli_start_card15:  0xFF5050E, 
    locationnames.patchouli_start_card16:  0xFF5050F, 
    locationnames.patchouli_start_card17:  0xFF50510, 
    locationnames.patchouli_start_card18:  0xFF50511, 
    locationnames.patchouli_start_card19:  0xFF50512, 
    locationnames.patchouli_start_card20:  0xFF50513, 
    locationnames.patchouli_start_card21:  0xFF50514, 
    locationnames.patchouli_start_card22:  0xFF50515, 
    locationnames.patchouli_start_card23:  0xFF50516, 
    locationnames.patchouli_start_card24:  0xFF50517, 
    locationnames.patchouli_start_card25:  0xFF50518, 
    locationnames.patchouli_start_card26:  0xFF50519, 
    locationnames.patchouli_start_card27:  0xFF5051A

}

youmu_start_card_table = { #0xFF50600 - FF50615
    locationnames.youmu_start_card1:   0xFF50600,
    locationnames.youmu_start_card2:   0xFF50601,
    locationnames.youmu_start_card3:   0xFF50602,
    locationnames.youmu_start_card4:   0xFF50603,
    locationnames.youmu_start_card5:   0xFF50604,
    locationnames.youmu_start_card6:   0xFF50605,
    locationnames.youmu_start_card7:   0xFF50606,
    locationnames.youmu_start_card8:   0xFF50607,
    locationnames.youmu_start_card9:   0xFF50608,
    locationnames.youmu_start_card10:  0xFF50609,
    locationnames.youmu_start_card11:  0xFF5060A,
    locationnames.youmu_start_card12:  0xFF5060B,
    locationnames.youmu_start_card13:  0xFF5060C,
    locationnames.youmu_start_card14:  0xFF5060D,
    locationnames.youmu_start_card15:  0xFF5060E,
    locationnames.youmu_start_card16:  0xFF5060F,
    locationnames.youmu_start_card17:  0xFF50610,
    locationnames.youmu_start_card18:  0xFF50611,
    locationnames.youmu_start_card19:  0xFF50612,
    locationnames.youmu_start_card20:  0xFF50613,
    locationnames.youmu_start_card21:  0xFF50614,
    locationnames.youmu_start_card22:  0xFF50615

}

remilia_start_card_table = { #0xFF50700 - FF50715
    locationnames.remilia_start_card1:   0xFF50700,
    locationnames.remilia_start_card2:   0xFF50701,
    locationnames.remilia_start_card3:   0xFF50702,
    locationnames.remilia_start_card4:   0xFF50703,
    locationnames.remilia_start_card5:   0xFF50704,
    locationnames.remilia_start_card6:   0xFF50705,
    locationnames.remilia_start_card7:   0xFF50706,
    locationnames.remilia_start_card8:   0xFF50707,
    locationnames.remilia_start_card9:   0xFF50708,
    locationnames.remilia_start_card10:  0xFF50709,
    locationnames.remilia_start_card11:  0xFF5070A,
    locationnames.remilia_start_card12:  0xFF5070B,
    locationnames.remilia_start_card13:  0xFF5070C,
    locationnames.remilia_start_card14:  0xFF5070D,
    locationnames.remilia_start_card15:  0xFF5070E,
    locationnames.remilia_start_card16:  0xFF5070F,
    locationnames.remilia_start_card17:  0xFF50710,
    locationnames.remilia_start_card18:  0xFF50711,
    locationnames.remilia_start_card19:  0xFF50712,
    locationnames.remilia_start_card20:  0xFF50713,
    locationnames.remilia_start_card21:  0xFF50714,
    locationnames.remilia_start_card22:  0xFF50715

}

yuyuko_start_card_table = { #0xFF50800 - FF50816
    locationnames.yuyuko_start_card1:   0xFF50800, 
    locationnames.yuyuko_start_card2:   0xFF50801, 
    locationnames.yuyuko_start_card3:   0xFF50802, 
    locationnames.yuyuko_start_card4:   0xFF50803, 
    locationnames.yuyuko_start_card5:   0xFF50804, 
    locationnames.yuyuko_start_card6:   0xFF50805, 
    locationnames.yuyuko_start_card7:   0xFF50806, 
    locationnames.yuyuko_start_card8:   0xFF50807, 
    locationnames.yuyuko_start_card9:   0xFF50808, 
    locationnames.yuyuko_start_card10:  0xFF50809, 
    locationnames.yuyuko_start_card11:  0xFF5080A, 
    locationnames.yuyuko_start_card12:  0xFF5080B, 
    locationnames.yuyuko_start_card13:  0xFF5080C, 
    locationnames.yuyuko_start_card14:  0xFF5080D, 
    locationnames.yuyuko_start_card15:  0xFF5080E, 
    locationnames.yuyuko_start_card16:  0xFF5080F, 
    locationnames.yuyuko_start_card17:  0xFF50810, 
    locationnames.yuyuko_start_card18:  0xFF50811, 
    locationnames.yuyuko_start_card19:  0xFF50812, 
    locationnames.yuyuko_start_card20:  0xFF50813, 
    locationnames.yuyuko_start_card21:  0xFF50814, 
    locationnames.yuyuko_start_card22:  0xFF50815, 
    locationnames.yuyuko_start_card23:  0xFF50816,

}

yukari_start_card_table = { #0xFF50900 - FF50915
    locationnames.yukari_start_card1:   0xFF50900,
    locationnames.yukari_start_card2:   0xFF50901,
    locationnames.yukari_start_card3:   0xFF50902,
    locationnames.yukari_start_card4:   0xFF50903,
    locationnames.yukari_start_card5:   0xFF50904,
    locationnames.yukari_start_card6:   0xFF50905,
    locationnames.yukari_start_card7:   0xFF50906,
    locationnames.yukari_start_card8:   0xFF50907,
    locationnames.yukari_start_card9:   0xFF50908,
    locationnames.yukari_start_card10:  0xFF50909,
    locationnames.yukari_start_card11:  0xFF5090A,
    locationnames.yukari_start_card12:  0xFF5090B,
    locationnames.yukari_start_card13:  0xFF5090C,
    locationnames.yukari_start_card14:  0xFF5090D,
    locationnames.yukari_start_card15:  0xFF5090E,
    locationnames.yukari_start_card16:  0xFF5090F,
    locationnames.yukari_start_card17:  0xFF50910,
    locationnames.yukari_start_card18:  0xFF50911,
    locationnames.yukari_start_card19:  0xFF50912,
    locationnames.yukari_start_card20:  0xFF50913,
    locationnames.yukari_start_card21:  0xFF50914,
    locationnames.yukari_start_card22:  0xFF50915
    
    }

suika_start_card_table = { #0xFF50A00 - FF50A15
    locationnames.suika_start_card1:   0xFF50A00, 
    locationnames.suika_start_card2:   0xFF50A01, 
    locationnames.suika_start_card3:   0xFF50A02, 
    locationnames.suika_start_card4:   0xFF50A03, 
    locationnames.suika_start_card5:   0xFF50A04, 
    locationnames.suika_start_card6:   0xFF50A05, 
    locationnames.suika_start_card7:   0xFF50A06, 
    locationnames.suika_start_card8:   0xFF50A07, 
    locationnames.suika_start_card9:   0xFF50A08, 
    locationnames.suika_start_card10:  0xFF50A09, 
    locationnames.suika_start_card11:  0xFF50A0A, 
    locationnames.suika_start_card12:  0xFF50A0B, 
    locationnames.suika_start_card13:  0xFF50A0C, 
    locationnames.suika_start_card14:  0xFF50A0D, 
    locationnames.suika_start_card15:  0xFF50A0E, 
    locationnames.suika_start_card16:  0xFF50A0F, 
    locationnames.suika_start_card17:  0xFF50A10, 
    locationnames.suika_start_card18:  0xFF50A11, 
    locationnames.suika_start_card19:  0xFF50A12, 
    locationnames.suika_start_card20:  0xFF50A13, 
    locationnames.suika_start_card21:  0xFF50A14, 
    locationnames.suika_start_card22:  0xFF50A15

}

reisen_start_card_table = { #0xFF50B00 - FF50B16
    locationnames.reisen_start_card1:   0xFF50B00,
    locationnames.reisen_start_card2:   0xFF50B01,
    locationnames.reisen_start_card3:   0xFF50B02,
    locationnames.reisen_start_card4:   0xFF50B03,
    locationnames.reisen_start_card5:   0xFF50B04,
    locationnames.reisen_start_card6:   0xFF50B05,
    locationnames.reisen_start_card7:   0xFF50B06,
    locationnames.reisen_start_card8:   0xFF50B07,
    locationnames.reisen_start_card9:   0xFF50B08,
    locationnames.reisen_start_card10:  0xFF50B09,
    locationnames.reisen_start_card11:  0xFF50B0A,
    locationnames.reisen_start_card12:  0xFF50B0B,
    locationnames.reisen_start_card13:  0xFF50B0C,
    locationnames.reisen_start_card14:  0xFF50B0D,
    locationnames.reisen_start_card15:  0xFF50B0E,
    locationnames.reisen_start_card16:  0xFF50B0F,
    locationnames.reisen_start_card17:  0xFF50B10,
    locationnames.reisen_start_card18:  0xFF50B11,
    locationnames.reisen_start_card19:  0xFF50B12,
    locationnames.reisen_start_card20:  0xFF50B13,
    locationnames.reisen_start_card21:  0xFF50B14,
    locationnames.reisen_start_card22:  0xFF50B15,
    locationnames.reisen_start_card23:  0xFF50B16,

}

aya_start_card_table = { #0xFF50C00 - FF50C15
    locationnames.aya_start_card1:   0xFF50C00,
    locationnames.aya_start_card2:   0xFF50C01,
    locationnames.aya_start_card3:   0xFF50C02,
    locationnames.aya_start_card4:   0xFF50C03,
    locationnames.aya_start_card5:   0xFF50C04,
    locationnames.aya_start_card6:   0xFF50C05,
    locationnames.aya_start_card7:   0xFF50C06,
    locationnames.aya_start_card8:   0xFF50C07,
    locationnames.aya_start_card9:   0xFF50C08,
    locationnames.aya_start_card10:  0xFF50C09,
    locationnames.aya_start_card11:  0xFF50C0A,
    locationnames.aya_start_card12:  0xFF50C0B,
    locationnames.aya_start_card13:  0xFF50C0C,
    locationnames.aya_start_card14:  0xFF50C0D,
    locationnames.aya_start_card15:  0xFF50C0E,
    locationnames.aya_start_card16:  0xFF50C0F,
    locationnames.aya_start_card17:  0xFF50C10,
    locationnames.aya_start_card18:  0xFF50C11,
    locationnames.aya_start_card19:  0xFF50C12,
    locationnames.aya_start_card20:  0xFF50C13,
    locationnames.aya_start_card21:  0xFF50C14,
    locationnames.aya_start_card22:  0xFF50C15,

}

komachi_start_card_table = { #0xFF50D00 - FF50D14
    locationnames.komachi_start_card1:   0xFF50D00,
    locationnames.komachi_start_card2:   0xFF50D01,
    locationnames.komachi_start_card3:   0xFF50D02,
    locationnames.komachi_start_card4:   0xFF50D03,
    locationnames.komachi_start_card5:   0xFF50D04,
    locationnames.komachi_start_card6:   0xFF50D05,
    locationnames.komachi_start_card7:   0xFF50D06,
    locationnames.komachi_start_card8:   0xFF50D07,
    locationnames.komachi_start_card9:   0xFF50D08,
    locationnames.komachi_start_card10:  0xFF50D09,
    locationnames.komachi_start_card11:  0xFF50D0A,
    locationnames.komachi_start_card12:  0xFF50D0B,
    locationnames.komachi_start_card13:  0xFF50D0C,
    locationnames.komachi_start_card14:  0xFF50D0D,
    locationnames.komachi_start_card15:  0xFF50D0E,
    locationnames.komachi_start_card16:  0xFF50D0F,
    locationnames.komachi_start_card17:  0xFF50D10,
    locationnames.komachi_start_card18:  0xFF50D11,
    locationnames.komachi_start_card19:  0xFF50D12,
    locationnames.komachi_start_card20:  0xFF50D13,
    locationnames.komachi_start_card21:  0xFF50D14

}

iku_start_card_table = { #0xFF50E00 - FF50E15
    locationnames.iku_start_card1:   0xFF50E00,
    locationnames.iku_start_card2:   0xFF50E01,
    locationnames.iku_start_card3:   0xFF50E02,
    locationnames.iku_start_card4:   0xFF50E03,
    locationnames.iku_start_card5:   0xFF50E04,
    locationnames.iku_start_card6:   0xFF50E05,
    locationnames.iku_start_card7:   0xFF50E06,
    locationnames.iku_start_card8:   0xFF50E07,
    locationnames.iku_start_card9:   0xFF50E08,
    locationnames.iku_start_card10:  0xFF50E09,
    locationnames.iku_start_card11:  0xFF50E0A,
    locationnames.iku_start_card12:  0xFF50E0B,
    locationnames.iku_start_card13:  0xFF50E0C,
    locationnames.iku_start_card14:  0xFF50E0D,
    locationnames.iku_start_card15:  0xFF50E0E,
    locationnames.iku_start_card16:  0xFF50E0F,
    locationnames.iku_start_card17:  0xFF50E10,
    locationnames.iku_start_card18:  0xFF50E11,
    locationnames.iku_start_card19:  0xFF50E12,
    locationnames.iku_start_card20:  0xFF50E13,
    locationnames.iku_start_card21:  0xFF50E14,
    locationnames.iku_start_card22:  0xFF50E15,

}

tenshi_start_card_table = { #0xFF50F00 - FF50F15
    locationnames.tenshi_start_card1:   0xFF50F00,
    locationnames.tenshi_start_card2:   0xFF50F01,
    locationnames.tenshi_start_card3:   0xFF50F02,
    locationnames.tenshi_start_card4:   0xFF50F03,
    locationnames.tenshi_start_card5:   0xFF50F04,
    locationnames.tenshi_start_card6:   0xFF50F05,
    locationnames.tenshi_start_card7:   0xFF50F06,
    locationnames.tenshi_start_card8:   0xFF50F07,
    locationnames.tenshi_start_card9:   0xFF50F08,
    locationnames.tenshi_start_card10:  0xFF50F09,
    locationnames.tenshi_start_card11:  0xFF50F0A,
    locationnames.tenshi_start_card12:  0xFF50F0B,
    locationnames.tenshi_start_card13:  0xFF50F0C,
    locationnames.tenshi_start_card14:  0xFF50F0D,
    locationnames.tenshi_start_card15:  0xFF50F0E,
    locationnames.tenshi_start_card16:  0xFF50F0F,
    locationnames.tenshi_start_card17:  0xFF50F10,
    locationnames.tenshi_start_card18:  0xFF50F11,
    locationnames.tenshi_start_card19:  0xFF50F12,
    locationnames.tenshi_start_card20:  0xFF50F13,
    locationnames.tenshi_start_card21:  0xFF50F14,
    locationnames.tenshi_start_card22:  0xFF50F15,

}

sanae_start_card_table = { #0xFF51000 - FF51000
    locationnames.sanae_start_card1:   0xFF51000,
    locationnames.sanae_start_card2:   0xFF51001,
    locationnames.sanae_start_card3:   0xFF51002,
    locationnames.sanae_start_card4:   0xFF51003,
    locationnames.sanae_start_card5:   0xFF51004,
    locationnames.sanae_start_card6:   0xFF51005,
    locationnames.sanae_start_card7:   0xFF51006,
    locationnames.sanae_start_card8:   0xFF51007,
    locationnames.sanae_start_card9:   0xFF51008,
    locationnames.sanae_start_card10:  0xFF51009,
    locationnames.sanae_start_card11:  0xFF5100A,
    locationnames.sanae_start_card12:  0xFF5100B,
    locationnames.sanae_start_card13:  0xFF5100C,
    locationnames.sanae_start_card14:  0xFF5100D,
    locationnames.sanae_start_card15:  0xFF5100E,
    locationnames.sanae_start_card16:  0xFF5100F,
    locationnames.sanae_start_card17:  0xFF51010,
    locationnames.sanae_start_card18:  0xFF51012,
    locationnames.sanae_start_card19:  0xFF51013,
    locationnames.sanae_start_card20:  0xFF51014,
    locationnames.sanae_start_card21:  0xFF51015,

}

cirno_start_card_table = { #0xFF51100 - FF51116
    locationnames.cirno_start_card1:   0xFF51100,
    locationnames.cirno_start_card2:   0xFF51101,
    locationnames.cirno_start_card3:   0xFF51102,
    locationnames.cirno_start_card4:   0xFF51103,
    locationnames.cirno_start_card5:   0xFF51104,
    locationnames.cirno_start_card6:   0xFF51105,
    locationnames.cirno_start_card7:   0xFF51106,
    locationnames.cirno_start_card8:   0xFF51107,
    locationnames.cirno_start_card9:   0xFF51108,
    locationnames.cirno_start_card10:  0xFF51109,
    locationnames.cirno_start_card11:  0xFF5110A,
    locationnames.cirno_start_card12:  0xFF5110B,
    locationnames.cirno_start_card13:  0xFF5110C,
    locationnames.cirno_start_card14:  0xFF5110D,
    locationnames.cirno_start_card15:  0xFF5110E,
    locationnames.cirno_start_card16:  0xFF5110F,
    locationnames.cirno_start_card17:  0xFF51110,
    locationnames.cirno_start_card18:  0xFF51111,
    locationnames.cirno_start_card19:  0xFF51112,
    locationnames.cirno_start_card20:  0xFF51113,
    locationnames.cirno_start_card21:  0xFF51114,
    locationnames.cirno_start_card22:  0xFF51115,
    locationnames.cirno_start_card23:  0xFF51116,

}

meiling_start_card_table = { #0xFF51200 - FF51216
    locationnames.meiling_start_card1:   0xFF51200,
    locationnames.meiling_start_card2:   0xFF51201,
    locationnames.meiling_start_card3:   0xFF51202,
    locationnames.meiling_start_card4:   0xFF51203,
    locationnames.meiling_start_card5:   0xFF51204,
    locationnames.meiling_start_card6:   0xFF51205,
    locationnames.meiling_start_card7:   0xFF51206,
    locationnames.meiling_start_card8:   0xFF51207,
    locationnames.meiling_start_card9:   0xFF51208,
    locationnames.meiling_start_card10:  0xFF51209,
    locationnames.meiling_start_card11:  0xFF5120A,
    locationnames.meiling_start_card12:  0xFF5120B,
    locationnames.meiling_start_card13:  0xFF5120C,
    locationnames.meiling_start_card14:  0xFF5120D,
    locationnames.meiling_start_card15:  0xFF5120E,
    locationnames.meiling_start_card16:  0xFF5120F,
    locationnames.meiling_start_card17:  0xFF51210,
    locationnames.meiling_start_card18:  0xFF51211,
    locationnames.meiling_start_card19:  0xFF51212,
    locationnames.meiling_start_card20:  0xFF51213,
    locationnames.meiling_start_card21:  0xFF51214,
    locationnames.meiling_start_card22:  0xFF51215,
    locationnames.meiling_start_card23:  0xFF51216,

}

okuu_start_card_table = { #0xFF51300 - FF51318
    locationnames.okuu_start_card1:   0xFF51300,
    locationnames.okuu_start_card2:   0xFF51301,
    locationnames.okuu_start_card3:   0xFF51302,
    locationnames.okuu_start_card4:   0xFF51303,
    locationnames.okuu_start_card5:   0xFF51304,
    locationnames.okuu_start_card6:   0xFF51305,
    locationnames.okuu_start_card7:   0xFF51306,
    locationnames.okuu_start_card8:   0xFF51307,
    locationnames.okuu_start_card9:   0xFF51308,
    locationnames.okuu_start_card10:  0xFF51309,
    locationnames.okuu_start_card11:  0xFF5130A,
    locationnames.okuu_start_card13:  0xFF5130B,
    locationnames.okuu_start_card14:  0xFF5130C,
    locationnames.okuu_start_card15:  0xFF5130D,
    locationnames.okuu_start_card16:  0xFF5130E,
    locationnames.okuu_start_card17:  0xFF5130F,
    locationnames.okuu_start_card18:  0xFF51310,
    locationnames.okuu_start_card19:  0xFF51311,
    locationnames.okuu_start_card20:  0xFF51312,
    locationnames.okuu_start_card21:  0xFF51313,
    locationnames.okuu_start_card22:  0xFF51314,
    locationnames.okuu_start_card23:  0xFF51315,
    locationnames.okuu_start_card24:  0xFF51316,
    locationnames.okuu_start_card25:  0xFF51317,
    locationnames.okuu_start_card26:  0xFF51318,

}

suwako_start_card_table = { #0xFF51400 - FF51416
    locationnames.suwako_start_card1:  0xFF51400,
    locationnames.suwako_start_card2:  0xFF51401,
    locationnames.suwako_start_card3:  0xFF51402,
    locationnames.suwako_start_card4:  0xFF51403,
    locationnames.suwako_start_card5:  0xFF51404,
    locationnames.suwako_start_card6:  0xFF51405,
    locationnames.suwako_start_card7:  0xFF51406,
    locationnames.suwako_start_card8:  0xFF51407,
    locationnames.suwako_start_card9:  0xFF51408,
    locationnames.suwako_start_card10: 0xFF51409,
    locationnames.suwako_start_card11: 0xFF5140A,
    locationnames.suwako_start_card12: 0xFF5140B,
    locationnames.suwako_start_card13: 0xFF5140C,
    locationnames.suwako_start_card14: 0xFF5140D,
    locationnames.suwako_start_card15: 0xFF5140E,
    locationnames.suwako_start_card16: 0xFF5140F,
    locationnames.suwako_start_card17: 0xFF51410,
    locationnames.suwako_start_card18: 0xFF51411,
    locationnames.suwako_start_card19: 0xFF51412,
    locationnames.suwako_start_card20: 0xFF51413,
    locationnames.suwako_start_card21: 0xFF51414,
    locationnames.suwako_start_card22: 0xFF51415,
    locationnames.suwako_start_card23: 0xFF51416,

}

reimu_skill_table = { #0xF00000 - F0002F
    locationnames.csl1_reimu_236d:  0xF00000,
    locationnames.csl2_reimu_236d:  0xF00001,
    locationnames.csl4_reimu_236d:  0xF00002,
    locationnames.csl3_reimu_236d:  0xF00003,
    locationnames.csl1_reimu_236a1: 0xF00004,
    locationnames.csl2_reimu_236a1: 0xF00005,
    locationnames.csl3_reimu_236a1: 0xF00006,
    locationnames.csl4_reimu_236a1: 0xF00007,
    locationnames.csl1_reimu_236a2: 0xF00008,
    locationnames.csl2_reimu_236a2: 0xF00009,
    locationnames.csl3_reimu_236a2: 0xF0000A,
    locationnames.csl4_reimu_236a2: 0xF0000B,
    locationnames.csl1_reimu_623d:  0xF0000C,
    locationnames.csl2_reimu_623d:  0xF0000D,
    locationnames.csl3_reimu_623d:  0xF0000E,
    locationnames.csl4_reimu_623d:  0xF0000F,
    locationnames.csl1_reimu_623a1: 0xF00010,
    locationnames.csl2_reimu_623a1: 0xF00011,
    locationnames.csl3_reimu_623a1: 0xF00012,
    locationnames.csl4_reimu_623a1: 0xF00013,
    locationnames.csl1_reimu_623a2: 0xF00014,
    locationnames.csl2_reimu_623a2: 0xF00015,
    locationnames.csl3_reimu_623a2: 0xF00016,
    locationnames.csl4_reimu_623a2: 0xF00017,
    locationnames.csl1_reimu_214d:  0xF00018,
    locationnames.csl2_reimu_214d:  0xF00019,
    locationnames.csl3_reimu_214d:  0xF0001A,
    locationnames.csl4_reimu_214d:  0xF0001B,
    locationnames.csl1_reimu_214a1: 0xF0001C,
    locationnames.csl2_reimu_214a1: 0xF0001D,
    locationnames.csl3_reimu_214a1: 0xF0001E,
    locationnames.csl4_reimu_214a1: 0xF0001F,
    locationnames.csl1_reimu_214a2: 0xF00020,
    locationnames.csl2_reimu_214a2: 0xF00021,
    locationnames.csl3_reimu_214a2: 0xF00022,
    locationnames.csl4_reimu_214a2: 0xF00023,
    locationnames.csl1_reimu_421d:  0xF00024,
    locationnames.csl2_reimu_421d:  0xF00025,
    locationnames.csl3_reimu_421d:  0xF00026,
    locationnames.csl4_reimu_421d:  0xF00027,
    locationnames.csl1_reimu_421a1: 0xF00028,
    locationnames.csl2_reimu_421a1: 0xF00029,
    locationnames.csl3_reimu_421a1: 0xF0002A,
    locationnames.csl4_reimu_421a1: 0xF0002B,
    locationnames.csl1_reimu_421a2: 0xF0002C,
    locationnames.csl2_reimu_421a2: 0xF0002D,
    locationnames.csl3_reimu_421a2: 0xF0002E,
    locationnames.csl4_reimu_421a2: 0xF0002F,

}

reimu_spell_table = { #0xF00030 - F00057
    locationnames.csl1_reimu_1sc:       0xF00030,
    locationnames.csl2_reimu_1sc:       0xF00031,
    locationnames.csl3_reimu_1sc:       0xF00032,
    locationnames.csl4_reimu_1sc:       0xF00033,
    locationnames.csl1_reimu_2sc_fo:    0xF00034,
    locationnames.csl2_reimu_2sc_fo:    0xF00035,
    locationnames.csl3_reimu_2sc_fo:    0xF00036,
    locationnames.csl4_reimu_2sc_fo:    0xF00037,
    locationnames.csl1_reimu_2sc_dba:   0xF00038,
    locationnames.csl2_reimu_2sc_dba:   0xF00039,
    locationnames.csl3_reimu_2sc_dba:   0xF0003A,
    locationnames.csl4_reimu_2sc_dba:   0xF0003B,
    locationnames.csl1_reimu_2sc_yyo:   0xF0003C,
    locationnames.csl2_reimu_2sc_yyo:   0xF0003D,
    locationnames.csl3_reimu_2sc_yyo:   0xF0003E,
    locationnames.csl4_reimu_2sc_yyo:   0xF0003F,
    locationnames.csl1_reimu_3sc_eb:    0xF00040,
    locationnames.csl2_reimu_3sc_eb:    0xF00041,
    locationnames.csl3_reimu_3sc_eb:    0xF00042,
    locationnames.csl4_reimu_3sc_eb:    0xF00043,
    locationnames.csl1_reimu_3sc_wgk:   0xF00044,
    locationnames.csl2_reimu_3sc_wgk:   0xF00045,
    locationnames.csl3_reimu_3sc_wgk:   0xF00046,
    locationnames.csl4_reimu_3sc_wgk:   0xF00047,
    locationnames.csl1_reimu_4sc_dbc:   0xF00048,
    locationnames.csl2_reimu_4sc_dbc:   0xF00049,
    locationnames.csl3_reimu_4sc_dbc:   0xF0004A,
    locationnames.csl4_reimu_4sc_dbc:   0xF0004B,
    locationnames.csl1_reimu_4sc_yyso:  0xF0004C,
    locationnames.csl2_reimu_4sc_yyso:  0xF0004D,
    locationnames.csl3_reimu_4sc_yyso:  0xF0004E,
    locationnames.csl4_reimu_4sc_yyso:  0xF0004F,
    locationnames.csl1_reimu_5sc_fs:    0xF00050,
    locationnames.csl2_reimu_5sc_fs:    0xF00051,
    locationnames.csl3_reimu_5sc_fs:    0xF00052,
    locationnames.csl4_reimu_5sc_fs:    0xF00053,
    locationnames.csl1_reimu_5sc_fh:    0xF00054,
    locationnames.csl2_reimu_5sc_fh:    0xF00055,
    locationnames.csl3_reimu_5sc_fh:    0xF00056,
    locationnames.csl4_reimu_5sc_fh:    0xF00057,

}

marisa_skill_table = { #0xF01000 - F0102F
    locationnames.csl1_marisa_236d:   0xF01000,
    locationnames.csl2_marisa_236d:   0xF01001,
    locationnames.csl3_marisa_236d:   0xF01002,
    locationnames.csl4_marisa_236d:   0xF01003,
    locationnames.csl1_marisa_236a1:  0xF01004,
    locationnames.csl2_marisa_236a1:  0xF01005,
    locationnames.csl3_marisa_236a1:  0xF01006,
    locationnames.csl4_marisa_236a1:  0xF01007,
    locationnames.csl1_marisa_236a2:  0xF01008,
    locationnames.csl2_marisa_236a2:  0xF01009,
    locationnames.csl3_marisa_236a2:  0xF0100A,
    locationnames.csl4_marisa_236a2:  0xF0100B,
    locationnames.csl1_marisa_623d:   0xF0100C,
    locationnames.csl2_marisa_623d:   0xF0100D,
    locationnames.csl3_marisa_623d:   0xF0100E,
    locationnames.csl4_marisa_623d:   0xF0100F,
    locationnames.csl1_marisa_623a1:  0xF01010,
    locationnames.csl2_marisa_623a1:  0xF01011,
    locationnames.csl3_marisa_623a1:  0xF01012,
    locationnames.csl4_marisa_623a1:  0xF01013,
    locationnames.csl1_marisa_623a2:  0xF01014,
    locationnames.csl2_marisa_623a2:  0xF01015,
    locationnames.csl3_marisa_623a2:  0xF01016,
    locationnames.csl4_marisa_623a2:  0xF01017,
    locationnames.csl1_marisa_214d:   0xF01018,
    locationnames.csl2_marisa_214d:   0xF01019,
    locationnames.csl3_marisa_214d:   0xF0101A,
    locationnames.csl4_marisa_214d:   0xF0101B,
    locationnames.csl1_marisa_214a1:  0xF0101C,
    locationnames.csl2_marisa_214a1:  0xF0101D,
    locationnames.csl3_marisa_214a1:  0xF0101E,
    locationnames.csl4_marisa_214a1:  0xF0101F,
    locationnames.csl1_marisa_214a2:  0xF01020,
    locationnames.csl2_marisa_214a2:  0xF01021,
    locationnames.csl3_marisa_214a2:  0xF01022,
    locationnames.csl4_marisa_214a2:  0xF01023,
    locationnames.csl1_marisa_22d:    0xF01024,
    locationnames.csl2_marisa_22d:    0xF01025,
    locationnames.csl3_marisa_22d:    0xF01026,
    locationnames.csl4_marisa_22d:    0xF01027,
    locationnames.csl1_marisa_22a1:   0xF01028,
    locationnames.csl2_marisa_22a1:   0xF01029,
    locationnames.csl3_marisa_22a1:   0xF0102A,
    locationnames.csl4_marisa_22a1:   0xF0102B,
    locationnames.csl1_marisa_22a2:   0xF0102C,
    locationnames.csl2_marisa_22a2:   0xF0102D,
    locationnames.csl3_marisa_22a2:   0xF0102E,
    locationnames.csl4_marisa_22a2:   0xF0102F,
}
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
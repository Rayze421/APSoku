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

reimu_skill_loc_table = { #0xFA0000 - FA002F
    locationnames.csl1_reimu_236d:  0xFA0000,
    locationnames.csl2_reimu_236d:  0xFA0001,
    locationnames.csl4_reimu_236d:  0xFA0002,
    locationnames.csl3_reimu_236d:  0xFA0003,
    locationnames.csl1_reimu_236a1: 0xFA0004,
    locationnames.csl2_reimu_236a1: 0xFA0005,
    locationnames.csl3_reimu_236a1: 0xFA0006,
    locationnames.csl4_reimu_236a1: 0xFA0007,
    locationnames.csl1_reimu_236a2: 0xFA0008,
    locationnames.csl2_reimu_236a2: 0xFA0009,
    locationnames.csl3_reimu_236a2: 0xFA000A,
    locationnames.csl4_reimu_236a2: 0xFA000B,
    locationnames.csl1_reimu_623d:  0xFA000C,
    locationnames.csl2_reimu_623d:  0xFA000D,
    locationnames.csl3_reimu_623d:  0xFA000E,
    locationnames.csl4_reimu_623d:  0xFA000F,
    locationnames.csl1_reimu_623a1: 0xFA0010,
    locationnames.csl2_reimu_623a1: 0xFA0011,
    locationnames.csl3_reimu_623a1: 0xFA0012,
    locationnames.csl4_reimu_623a1: 0xFA0013,
    locationnames.csl1_reimu_623a2: 0xFA0014,
    locationnames.csl2_reimu_623a2: 0xFA0015,
    locationnames.csl3_reimu_623a2: 0xFA0016,
    locationnames.csl4_reimu_623a2: 0xFA0017,
    locationnames.csl1_reimu_214d:  0xFA0018,
    locationnames.csl2_reimu_214d:  0xFA0019,
    locationnames.csl3_reimu_214d:  0xFA001A,
    locationnames.csl4_reimu_214d:  0xFA001B,
    locationnames.csl1_reimu_214a1: 0xFA001C,
    locationnames.csl2_reimu_214a1: 0xFA001D,
    locationnames.csl3_reimu_214a1: 0xFA001E,
    locationnames.csl4_reimu_214a1: 0xFA001F,
    locationnames.csl1_reimu_214a2: 0xFA0020,
    locationnames.csl2_reimu_214a2: 0xFA0021,
    locationnames.csl3_reimu_214a2: 0xFA0022,
    locationnames.csl4_reimu_214a2: 0xFA0023,
    locationnames.csl1_reimu_421d:  0xFA0024,
    locationnames.csl2_reimu_421d:  0xFA0025,
    locationnames.csl3_reimu_421d:  0xFA0026,
    locationnames.csl4_reimu_421d:  0xFA0027,
    locationnames.csl1_reimu_421a1: 0xFA0028,
    locationnames.csl2_reimu_421a1: 0xFA0029,
    locationnames.csl3_reimu_421a1: 0xFA002A,
    locationnames.csl4_reimu_421a1: 0xFA002B,
    locationnames.csl1_reimu_421a2: 0xFA002C,
    locationnames.csl2_reimu_421a2: 0xFA002D,
    locationnames.csl3_reimu_421a2: 0xFA002E,
    locationnames.csl4_reimu_421a2: 0xFA002F,

}

reimu_spell_loc_table = { #0xFA0030 - FA0057
    locationnames.csl1_reimu_1sc:       0xFA0030,
    locationnames.csl2_reimu_1sc:       0xFA0031,
    locationnames.csl3_reimu_1sc:       0xFA0032,
    locationnames.csl4_reimu_1sc:       0xFA0033,
    locationnames.csl1_reimu_2sc_fo:    0xFA0034,
    locationnames.csl2_reimu_2sc_fo:    0xFA0035,
    locationnames.csl3_reimu_2sc_fo:    0xFA0036,
    locationnames.csl4_reimu_2sc_fo:    0xFA0037,
    locationnames.csl1_reimu_2sc_dba:   0xFA0038,
    locationnames.csl2_reimu_2sc_dba:   0xFA0039,
    locationnames.csl3_reimu_2sc_dba:   0xFA003A,
    locationnames.csl4_reimu_2sc_dba:   0xFA003B,
    locationnames.csl1_reimu_2sc_yyo:   0xFA003C,
    locationnames.csl2_reimu_2sc_yyo:   0xFA003D,
    locationnames.csl3_reimu_2sc_yyo:   0xFA003E,
    locationnames.csl4_reimu_2sc_yyo:   0xFA003F,
    locationnames.csl1_reimu_3sc_eb:    0xFA0040,
    locationnames.csl2_reimu_3sc_eb:    0xFA0041,
    locationnames.csl3_reimu_3sc_eb:    0xFA0042,
    locationnames.csl4_reimu_3sc_eb:    0xFA0043,
    locationnames.csl1_reimu_3sc_wgk:   0xFA0044,
    locationnames.csl2_reimu_3sc_wgk:   0xFA0045,
    locationnames.csl3_reimu_3sc_wgk:   0xFA0046,
    locationnames.csl4_reimu_3sc_wgk:   0xFA0047,
    locationnames.csl1_reimu_4sc_dbc:   0xFA0048,
    locationnames.csl2_reimu_4sc_dbc:   0xFA0049,
    locationnames.csl3_reimu_4sc_dbc:   0xFA004A,
    locationnames.csl4_reimu_4sc_dbc:   0xFA004B,
    locationnames.csl1_reimu_4sc_yyso:  0xFA004C,
    locationnames.csl2_reimu_4sc_yyso:  0xFA004D,
    locationnames.csl3_reimu_4sc_yyso:  0xFA004E,
    locationnames.csl4_reimu_4sc_yyso:  0xFA004F,
    locationnames.csl1_reimu_5sc_fs:    0xFA0050,
    locationnames.csl2_reimu_5sc_fs:    0xFA0051,
    locationnames.csl3_reimu_5sc_fs:    0xFA0052,
    locationnames.csl4_reimu_5sc_fs:    0xFA0053,
    locationnames.csl1_reimu_5sc_fh:    0xFA0054,
    locationnames.csl2_reimu_5sc_fh:    0xFA0055,
    locationnames.csl3_reimu_5sc_fh:    0xFA0056,
    locationnames.csl4_reimu_5sc_fh:    0xFA0057,

}

marisa_skill_loc_table = { #0xFA0100 - FA012F
    locationnames.csl1_marisa_236d:   0xFA0100,
    locationnames.csl2_marisa_236d:   0xFA0101,
    locationnames.csl3_marisa_236d:   0xFA0102,
    locationnames.csl4_marisa_236d:   0xFA0103,
    locationnames.csl1_marisa_236a1:  0xFA0104,
    locationnames.csl2_marisa_236a1:  0xFA0105,
    locationnames.csl3_marisa_236a1:  0xFA0106,
    locationnames.csl4_marisa_236a1:  0xFA0107,
    locationnames.csl1_marisa_236a2:  0xFA0108,
    locationnames.csl2_marisa_236a2:  0xFA0109,
    locationnames.csl3_marisa_236a2:  0xFA010A,
    locationnames.csl4_marisa_236a2:  0xFA010B,
    locationnames.csl1_marisa_623d:   0xFA010C,
    locationnames.csl2_marisa_623d:   0xFA010D,
    locationnames.csl3_marisa_623d:   0xFA010E,
    locationnames.csl4_marisa_623d:   0xFA010F,
    locationnames.csl1_marisa_623a1:  0xFA0110,
    locationnames.csl2_marisa_623a1:  0xFA0111,
    locationnames.csl3_marisa_623a1:  0xFA0112,
    locationnames.csl4_marisa_623a1:  0xFA0113,
    locationnames.csl1_marisa_623a2:  0xFA0114,
    locationnames.csl2_marisa_623a2:  0xFA0115,
    locationnames.csl3_marisa_623a2:  0xFA0116,
    locationnames.csl4_marisa_623a2:  0xFA0117,
    locationnames.csl1_marisa_214d:   0xFA0118,
    locationnames.csl2_marisa_214d:   0xFA0119,
    locationnames.csl3_marisa_214d:   0xFA011A,
    locationnames.csl4_marisa_214d:   0xFA011B,
    locationnames.csl1_marisa_214a1:  0xFA011C,
    locationnames.csl2_marisa_214a1:  0xFA011D,
    locationnames.csl3_marisa_214a1:  0xFA011E,
    locationnames.csl4_marisa_214a1:  0xFA011F,
    locationnames.csl1_marisa_214a2:  0xFA0120,
    locationnames.csl2_marisa_214a2:  0xFA0121,
    locationnames.csl3_marisa_214a2:  0xFA0122,
    locationnames.csl4_marisa_214a2:  0xFA0123,
    locationnames.csl1_marisa_22d:    0xFA0124,
    locationnames.csl2_marisa_22d:    0xFA0125,
    locationnames.csl3_marisa_22d:    0xFA0126,
    locationnames.csl4_marisa_22d:    0xFA0127,
    locationnames.csl1_marisa_22a1:   0xFA0128,
    locationnames.csl2_marisa_22a1:   0xFA0129,
    locationnames.csl3_marisa_22a1:   0xFA012A,
    locationnames.csl4_marisa_22a1:   0xFA012B,
    locationnames.csl1_marisa_22a2:   0xFA012C,
    locationnames.csl2_marisa_22a2:   0xFA012D,
    locationnames.csl3_marisa_22a2:   0xFA012E,
    locationnames.csl4_marisa_22a2:   0xFA012F,
}

marisa_spell_loc_table = { #0xFA0130 - FA0167
    locationnames.csl1_marisa_1sc_ms:   0xFA0130,
    locationnames.csl2_marisa_1sc_ms:   0xFA0131,
    locationnames.csl3_marisa_1sc_ms:   0xFA0132,
    locationnames.csl4_marisa_1sc_ms:   0xFA0133,
    locationnames.csl1_marisa_2sc_sr:   0xFA0134,
    locationnames.csl2_marisa_2sc_sr:   0xFA0135,
    locationnames.csl3_marisa_2sc_sr:   0xFA0136,
    locationnames.csl4_marisa_2sc_sr:   0xFA0137,
    locationnames.csl1_marisa_2sc_ls:   0xFA0138,
    locationnames.csl2_marisa_2sc_ls:   0xFA0139,
    locationnames.csl3_marisa_2sc_ls:   0xFA013A,
    locationnames.csl4_marisa_2sc_ls:   0xFA013B,
    locationnames.csl1_marisa_2sc_os:   0xFA013C,
    locationnames.csl2_marisa_2sc_os:   0xFA013D,
    locationnames.csl3_marisa_2sc_os:   0xFA013E,
    locationnames.csl4_marisa_2sc_os:   0xFA013F,
    locationnames.csl1_marisa_3sc_ms:   0xFA0140,
    locationnames.csl2_marisa_3sc_ms:   0xFA0141,
    locationnames.csl3_marisa_3sc_ms:   0xFA0142,
    locationnames.csl4_marisa_3sc_ms:   0xFA0143,
    locationnames.csl1_marisa_3sc_ev:   0xFA0144,
    locationnames.csl2_marisa_3sc_ev:   0xFA0145,
    locationnames.csl3_marisa_3sc_ev:   0xFA0146,
    locationnames.csl4_marisa_3sc_ev:   0xFA0147,
    locationnames.csl1_marisa_3sc_gb:   0xFA0148,
    locationnames.csl2_marisa_3sc_gb:   0xFA0149,
    locationnames.csl3_marisa_3sc_gb:   0xFA014A,
    locationnames.csl4_marisa_3sc_gb:   0xFA014B,
    locationnames.csl1_marisa_3sc_er:   0xFA014C,
    locationnames.csl2_marisa_3sc_er:   0xFA014D,
    locationnames.csl3_marisa_3sc_er:   0xFA014E,
    locationnames.csl4_marisa_3sc_er:   0xFA014F,
    locationnames.csl1_marisa_4sc_ndl:  0xFA0150,
    locationnames.csl2_marisa_4sc_ndl:  0xFA0151,
    locationnames.csl3_marisa_4sc_ndl:  0xFA0152,
    locationnames.csl4_marisa_4sc_ndl:  0xFA0153,
    locationnames.csl1_marisa_4sc_deb:  0xFA0154,
    locationnames.csl2_marisa_4sc_deb:  0xFA0155,
    locationnames.csl3_marisa_4sc_deb:  0xFA0156,
    locationnames.csl4_marisa_4sc_deb:  0xFA0157,
    locationnames.csl1_marisa_5sc_fs:   0xFA0158,
    locationnames.csl2_marisa_5sc_fs:   0xFA0159,
    locationnames.csl3_marisa_5sc_fs:   0xFA015A,
    locationnames.csl4_marisa_5sc_fs:   0xFA015B,
    locationnames.csl1_marisa_5sc_dm:   0xFA015C,
    locationnames.csl2_marisa_5sc_dm:   0xFA015D,
    locationnames.csl3_marisa_5sc_dm:   0xFA015E,
    locationnames.csl4_marisa_5sc_dm:   0xFA015F,
    locationnames.csl1_marisa_5sc_bs:   0xFA0160,
    locationnames.csl2_marisa_5sc_bs:   0xFA0161,
    locationnames.csl3_marisa_5sc_bs:   0xFA0162,
    locationnames.csl4_marisa_5sc_bs:   0xFA0163,
    locationnames.csl1_marisa_5sc_sfms: 0xFA0164,
    locationnames.csl2_marisa_5sc_sfms: 0xFA0165,
    locationnames.csl3_marisa_5sc_sfms: 0xFA0166,
    locationnames.csl4_marisa_5sc_sfms: 0xFA0167,
}

sakuya_skill_loc_table = { #0xFA0200 - FA022F
    locationnames.csl1_sakuya_236d:   0xFA0200, 
    locationnames.csl2_sakuya_236d:   0xFA0201, 
    locationnames.csl3_sakuya_236d:   0xFA0202, 
    locationnames.csl4_sakuya_236d:   0xFA0203, 
    locationnames.csl1_sakuya_236a1:  0xFA0204, 
    locationnames.csl2_sakuya_236a1:  0xFA0205, 
    locationnames.csl3_sakuya_236a1:  0xFA0206, 
    locationnames.csl4_sakuya_236a1:  0xFA0207, 
    locationnames.csl1_sakuya_236a2:  0xFA0208, 
    locationnames.csl2_sakuya_236a2:  0xFA0209, 
    locationnames.csl3_sakuya_236a2:  0xFA020A, 
    locationnames.csl4_sakuya_236a2:  0xFA020B, 
    locationnames.csl1_sakuya_623d:   0xFA020C, 
    locationnames.csl2_sakuya_623d:   0xFA020D, 
    locationnames.csl3_sakuya_623d:   0xFA020E, 
    locationnames.csl4_sakuya_623d:   0xFA020F, 
    locationnames.csl1_sakuya_623a1:  0xFA0210, 
    locationnames.csl2_sakuya_623a1:  0xFA0211, 
    locationnames.csl3_sakuya_623a1:  0xFA0212, 
    locationnames.csl4_sakuya_623a1:  0xFA0213, 
    locationnames.csl1_sakuya_623a2:  0xFA0214, 
    locationnames.csl2_sakuya_623a2:  0xFA0215, 
    locationnames.csl3_sakuya_623a2:  0xFA0216, 
    locationnames.csl4_sakuya_623a2:  0xFA0217, 
    locationnames.csl1_sakuya_214d:   0xFA0218, 
    locationnames.csl2_sakuya_214d:   0xFA0219, 
    locationnames.csl3_sakuya_214d:   0xFA021A, 
    locationnames.csl4_sakuya_214d:   0xFA021B, 
    locationnames.csl1_sakuya_214a1:  0xFA021C, 
    locationnames.csl2_sakuya_214a1:  0xFA021D, 
    locationnames.csl3_sakuya_214a1:  0xFA021E, 
    locationnames.csl4_sakuya_214a1:  0xFA021F, 
    locationnames.csl1_sakuya_214a2:  0xFA0220, 
    locationnames.csl2_sakuya_214a2:  0xFA0221, 
    locationnames.csl3_sakuya_214a2:  0xFA0222, 
    locationnames.csl4_sakuya_214a2:  0xFA0223, 
    locationnames.csl1_sakuya_22d:    0xFA0224, 
    locationnames.csl2_sakuya_22d:    0xFA0225, 
    locationnames.csl3_sakuya_22d:    0xFA0226, 
    locationnames.csl4_sakuya_22d:    0xFA0227, 
    locationnames.csl1_sakuya_22a1:   0xFA0228, 
    locationnames.csl2_sakuya_22a1:   0xFA0229, 
    locationnames.csl3_sakuya_22a1:   0xFA022A, 
    locationnames.csl4_sakuya_22a1:   0xFA022B, 
    locationnames.csl1_sakuya_22a2:   0xFA022C, 
    locationnames.csl2_sakuya_22a2:   0xFA022D, 
    locationnames.csl3_sakuya_22a2:   0xFA022E, 
    locationnames.csl4_sakuya_22a2:   0xFA022F, 
}

sakuya_spell_loc_table = { #0xFA0230 - FA0263
    locationnames.csl1_sakuya_2sc_kd:   0xFA0230,
    locationnames.csl2_sakuya_2sc_kd:   0xFA0231,
    locationnames.csl3_sakuya_2sc_kd:   0xFA0232,
    locationnames.csl4_sakuya_2sc_kd:   0xFA0233,
    locationnames.csl1_sakuya_2sc_sb:   0xFA0234,
    locationnames.csl2_sakuya_2sc_sb:   0xFA0235,
    locationnames.csl3_sakuya_2sc_sb:   0xFA0236,
    locationnames.csl4_sakuya_2sc_sb:   0xFA0237,
    locationnames.csl1_sakuya_2sc_em:   0xFA0238,
    locationnames.csl2_sakuya_2sc_em:   0xFA0239,
    locationnames.csl3_sakuya_2sc_em:   0xFA023A,
    locationnames.csl4_sakuya_2sc_em:   0xFA023B,
    locationnames.csl1_sakuya_3sc_ps:   0xFA023C,
    locationnames.csl2_sakuya_3sc_ps:   0xFA023D,
    locationnames.csl3_sakuya_3sc_ps:   0xFA023E,
    locationnames.csl4_sakuya_3sc_ps:   0xFA023F,
    locationnames.csl1_sakuya_3sc_irs:  0xFA0240,
    locationnames.csl2_sakuya_3sc_irs:  0xFA0241,
    locationnames.csl3_sakuya_3sc_irs:  0xFA0242,
    locationnames.csl4_sakuya_3sc_irs:  0xFA0243,
    locationnames.csl1_sakuya_3sc_lr:   0xFA0244,
    locationnames.csl2_sakuya_3sc_lr:   0xFA0245,
    locationnames.csl3_sakuya_3sc_lr:   0xFA0246,
    locationnames.csl4_sakuya_3sc_lr:   0xFA0247,
    locationnames.csl1_sakuya_3sc_ivt:  0xFA0248,
    locationnames.csl2_sakuya_3sc_ivt:  0xFA0249,
    locationnames.csl3_sakuya_3sc_ivt:  0xFA024A,
    locationnames.csl4_sakuya_3sc_ivt:  0xFA024B,
    locationnames.csl1_sakuya_3sc_ld:   0xFA024C,
    locationnames.csl2_sakuya_3sc_ld:   0xFA024D,
    locationnames.csl3_sakuya_3sc_ld:   0xFA024E,
    locationnames.csl4_sakuya_3sc_ld:   0xFA024F,
    locationnames.csl1_sakuya_4sc_pk:   0xFA0250,
    locationnames.csl2_sakuya_4sc_pk:   0xFA0251,
    locationnames.csl3_sakuya_4sc_pk:   0xFA0252,
    locationnames.csl4_sakuya_4sc_pk:   0xFA0253,
    locationnames.csl1_sakuya_4sc_ss:   0xFA0254,
    locationnames.csl2_sakuya_4sc_ss:   0xFA0255,
    locationnames.csl3_sakuya_4sc_ss:   0xFA0256,
    locationnames.csl4_sakuya_4sc_ss:   0xFA0257,
    locationnames.csl1_sakuya_4sc_sss:  0xFA0258,
    locationnames.csl2_sakuya_4sc_sss:  0xFA0259,
    locationnames.csl3_sakuya_4sc_sss:  0xFA025A,
    locationnames.csl4_sakuya_4sc_sss:  0xFA025B,
    locationnames.csl1_sakuya_4sc_cr:   0xFA025C,
    locationnames.csl2_sakuya_4sc_cr:   0xFA025D,
    locationnames.csl3_sakuya_4sc_cr:   0xFA025E,
    locationnames.csl4_sakuya_4sc_cr:   0xFA025F,
    locationnames.csl1_sakuya_5sc_sw:   0xFA0260,
    locationnames.csl2_sakuya_5sc_sw:   0xFA0261,
    locationnames.csl3_sakuya_5sc_sw:   0xFA0262,
    locationnames.csl4_sakuya_5sc_sw:   0xFA0263,

}

alice_skill_loc_table = { #0xFA0300 - FA032F
    locationnames.csl1_alice_236d:    0xFA0300,
    locationnames.csl2_alice_236d:    0xFA0301,
    locationnames.csl3_alice_236d:    0xFA0302,
    locationnames.csl4_alice_236d:    0xFA0303,
    locationnames.csl1_alice_236a1:   0xFA0304,
    locationnames.csl2_alice_236a1:   0xFA0305,
    locationnames.csl3_alice_236a1:   0xFA0306,
    locationnames.csl4_alice_236a1:   0xFA0307,
    locationnames.csl1_alice_236a2:   0xFA0308,
    locationnames.csl2_alice_236a2:   0xFA0309,
    locationnames.csl3_alice_236a2:   0xFA030A,
    locationnames.csl4_alice_236a2:   0xFA030B,
    locationnames.csl1_alice_623d:    0xFA030C,
    locationnames.csl2_alice_623d:    0xFA030D,
    locationnames.csl3_alice_623d:    0xFA030E,
    locationnames.csl4_alice_623d:    0xFA030F,
    locationnames.csl1_alice_623a1:   0xFA0310,
    locationnames.csl2_alice_623a1:   0xFA0311,
    locationnames.csl3_alice_623a1:   0xFA0312,
    locationnames.csl4_alice_623a1:   0xFA0313,
    locationnames.csl1_alice_623a2:   0xFA0314,
    locationnames.csl2_alice_623a2:   0xFA0315,
    locationnames.csl3_alice_623a2:   0xFA0316,
    locationnames.csl4_alice_623a2:   0xFA0317,
    locationnames.csl1_alice_214d:    0xFA0318,
    locationnames.csl2_alice_214d:    0xFA0319,
    locationnames.csl3_alice_214d:    0xFA031A,
    locationnames.csl4_alice_214d:    0xFA031B,
    locationnames.csl1_alice_214a1:   0xFA031C,
    locationnames.csl2_alice_214a1:   0xFA031D,
    locationnames.csl3_alice_214a1:   0xFA031E,
    locationnames.csl4_alice_214a1:   0xFA031F,
    locationnames.csl1_alice_214a2:   0xFA0320,
    locationnames.csl2_alice_214a2:   0xFA0321,
    locationnames.csl3_alice_214a2:   0xFA0322,
    locationnames.csl4_alice_214a2:   0xFA0323,
    locationnames.csl1_alice_22d:     0xFA0324,
    locationnames.csl2_alice_22d:     0xFA0325,
    locationnames.csl3_alice_22d:     0xFA0326,
    locationnames.csl4_alice_22d:     0xFA0327,
    locationnames.csl1_alice_22a1:    0xFA0328,
    locationnames.csl2_alice_22a1:    0xFA0329,
    locationnames.csl3_alice_22a1:    0xFA032A,
    locationnames.csl4_alice_22a1:    0xFA032B,
    locationnames.csl1_alice_22a2:    0xFA032C,
    locationnames.csl2_alice_22a2:    0xFA032D,
    locationnames.csl3_alice_22a2:    0xFA032E,
    locationnames.csl4_alice_22a2:    0xFA032F,

}

alice_spell_loc_table = { #0xFA0330 - FA035F
    locationnames.csl1_alice_1sc_as:   0xFA0330,
    locationnames.csl2_alice_1sc_as:   0xFA0331,
    locationnames.csl3_alice_1sc_as:   0xFA0332,
    locationnames.csl4_alice_1sc_as:   0xFA0333,
    locationnames.csl1_alice_2sc_ll:   0xFA0334,
    locationnames.csl2_alice_2sc_ll:   0xFA0335,
    locationnames.csl3_alice_2sc_ll:   0xFA0336,
    locationnames.csl4_alice_2sc_ll:   0xFA0337,
    locationnames.csl1_alice_2sc_shd:  0xFA0338,
    locationnames.csl2_alice_2sc_shd:  0xFA0339,
    locationnames.csl3_alice_2sc_shd:  0xFA033A,
    locationnames.csl4_alice_2sc_shd:  0xFA033B,
    locationnames.csl1_alice_2sc_sd:   0xFA033C,
    locationnames.csl2_alice_2sc_sd:   0xFA033D,
    locationnames.csl3_alice_2sc_sd:   0xFA033E,
    locationnames.csl4_alice_2sc_sd:   0xFA033F,
    locationnames.csl1_alice_2sc_tw:   0xFA0340,
    locationnames.csl2_alice_2sc_tw:   0xFA0341,
    locationnames.csl3_alice_2sc_tw:   0xFA0342,
    locationnames.csl4_alice_2sc_tw:   0xFA0343,
    locationnames.csl1_alice_3sc_ri:   0xFA0344,
    locationnames.csl2_alice_3sc_ri:   0xFA0345,
    locationnames.csl3_alice_3sc_ri:   0xFA0346,
    locationnames.csl4_alice_3sc_ri:   0xFA0347,
    locationnames.csl1_alice_3sc_fp:   0xFA0348,
    locationnames.csl2_alice_3sc_fp:   0xFA0349,
    locationnames.csl3_alice_3sc_fp:   0xFA034A,
    locationnames.csl4_alice_3sc_fp:   0xFA034B,
    locationnames.csl1_alice_4sc_dow:  0xFA034C,
    locationnames.csl2_alice_4sc_dow:  0xFA034D,
    locationnames.csl3_alice_4sc_dow:  0xFA034E,
    locationnames.csl4_alice_4sc_dow:  0xFA034F,
    locationnames.csl1_alice_4sc_hd:   0xFA0350,
    locationnames.csl2_alice_4sc_hd:   0xFA0351,
    locationnames.csl3_alice_4sc_hd:   0xFA0352,
    locationnames.csl4_alice_4sc_hd:   0xFA0353,
    locationnames.csl1_alice_4sc_hld:  0xFA0354,
    locationnames.csl2_alice_4sc_hld:  0xFA0355,
    locationnames.csl3_alice_4sc_hld:  0xFA0356,
    locationnames.csl4_alice_4sc_hld:  0xFA0357,
    locationnames.csl1_alice_4sc_cp:   0xFA0358,
    locationnames.csl2_alice_4sc_cp:   0xFA0359,
    locationnames.csl3_alice_4sc_cp:   0xFA035A,
    locationnames.csl4_alice_4sc_cp:   0xFA035B,
    locationnames.csl1_alice_5sc_lp:   0xFA035C,
    locationnames.csl2_alice_5sc_lp:   0xFA035D,
    locationnames.csl3_alice_5sc_lp:   0xFA035E,
    locationnames.csl4_alice_5sc_lp:   0xFA035F

}

patchouli_skill_loc_table = { #0xFA0400 - FA043B
    locationnames.csl1_patchouli_236d:    0xFA0400,
    locationnames.csl2_patchouli_236d:    0xFA0401,
    locationnames.csl3_patchouli_236d:    0xFA0402,
    locationnames.csl4_patchouli_236d:    0xFA0403,
    locationnames.csl1_patchouli_236a1:   0xFA0404,
    locationnames.csl2_patchouli_236a1:   0xFA0405,
    locationnames.csl3_patchouli_236a1:   0xFA0406,
    locationnames.csl4_patchouli_236a1:   0xFA0407,
    locationnames.csl1_patchouli_236a2:   0xFA0408,
    locationnames.csl2_patchouli_236a2:   0xFA0409,
    locationnames.csl3_patchouli_236a2:   0xFA040A,
    locationnames.csl4_patchouli_236a2:   0xFA040B,
    locationnames.csl1_patchouli_623d:    0xFA040C,
    locationnames.csl2_patchouli_623d:    0xFA040D,
    locationnames.csl3_patchouli_623d:    0xFA040E,
    locationnames.csl4_patchouli_623d:    0xFA040F,
    locationnames.csl1_patchouli_623a1:   0xFA0410,
    locationnames.csl2_patchouli_623a1:   0xFA0411,
    locationnames.csl3_patchouli_623a1:   0xFA0412,
    locationnames.csl4_patchouli_623a1:   0xFA0413,
    locationnames.csl1_patchouli_623a2:   0xFA0414,
    locationnames.csl2_patchouli_623a2:   0xFA0415,
    locationnames.csl3_patchouli_623a2:   0xFA0416,
    locationnames.csl4_patchouli_623a2:   0xFA0417,
    locationnames.csl1_patchouli_214d:    0xFA0418,
    locationnames.csl4_patchouli_214d:    0xFA0419,
    locationnames.csl3_patchouli_214d:    0xFA041A,
    locationnames.csl4_patchouli_214d:    0xFA041B,
    locationnames.csl1_patchouli_214a1:   0xFA041C,
    locationnames.csl2_patchouli_214a1:   0xFA041D,
    locationnames.csl3_patchouli_214a1:   0xFA041E,
    locationnames.csl4_patchouli_214a1:   0xFA041F,
    locationnames.csl1_patchouli_214a2:   0xFA0420,
    locationnames.csl2_patchouli_214a2:   0xFA0421,
    locationnames.csl3_patchouli_214a2:   0xFA0422,
    locationnames.csl4_patchouli_214a2:   0xFA0423,
    locationnames.csl1_patchouli_421d:    0xFA0424,
    locationnames.csl2_patchouli_421d:    0xFA0425,
    locationnames.csl3_patchouli_421d:    0xFA0426,
    locationnames.csl4_patchouli_421d:    0xFA0427,
    locationnames.csl1_patchouli_421a1:   0xFA0428,
    locationnames.csl2_patchouli_421a1:   0xFA0429,
    locationnames.csl3_patchouli_421a1:   0xFA042A,
    locationnames.csl4_patchouli_421a1:   0xFA042B,
    locationnames.csl1_patchouli_421a2:   0xFA042C,
    locationnames.csl2_patchouli_421a2:   0xFA042D,
    locationnames.csl3_patchouli_421a2:   0xFA042E,
    locationnames.csl4_patchouli_421a2:   0xFA042F,
    locationnames.csl1_patchouli_22d:     0xFA0430,
    locationnames.csl2_patchouli_22d:     0xFA0431,
    locationnames.csl3_patchouli_22d:     0xFA0432,
    locationnames.csl4_patchouli_22d:     0xFA0433,
    locationnames.csl1_patchouli_22a1:    0xFA0434,
    locationnames.csl2_patchouli_22a1:    0xFA0435,
    locationnames.csl3_patchouli_22a1:    0xFA0436,
    locationnames.csl4_patchouli_22a1:    0xFA0437,
    locationnames.csl1_patchouli_22a2:    0xFA0438,
    locationnames.csl2_patchouli_22a2:    0xFA0439,
    locationnames.csl3_patchouli_22a2:    0xFA043A,
    locationnames.csl4_patchouli_22a2:    0xFA043B

}

patchouli_spell_loc_table = { #0xFA043C - FA046B
    locationnames.csl1_patchouli_2sc_nd:   0xFA043C,
    locationnames.csl2_patchouli_2sc_nd:   0xFA043D,
    locationnames.csl3_patchouli_2sc_nd:   0xFA043E,
    locationnames.csl4_patchouli_2sc_nd:   0xFA043F,
    locationnames.csl1_patchouli_2sc_eh:   0xFA0440,
    locationnames.csl2_patchouli_2sc_eh:   0xFA0441,
    locationnames.csl3_patchouli_2sc_eh:   0xFA0442,
    locationnames.csl4_patchouli_2sc_eh:   0xFA0443,
    locationnames.csl1_patchouli_3sc_sep:  0xFA0444,
    locationnames.csl2_patchouli_3sc_sep:  0xFA0445,
    locationnames.csl3_patchouli_3sc_sep:  0xFA0446,
    locationnames.csl4_patchouli_3sc_sep:  0xFA0447,
    locationnames.csl1_patchouli_3sc_jp:   0xFA0448,
    locationnames.csl2_patchouli_3sc_jp:   0xFA0449,
    locationnames.csl3_patchouli_3sc_jp:   0xFA044A,
    locationnames.csl4_patchouli_3sc_jp:   0xFA044B,
    locationnames.csl1_patchouli_3sc_ss:   0xFA044C,
    locationnames.csl2_patchouli_3sc_ss:   0xFA044D,
    locationnames.csl3_patchouli_3sc_ss:   0xFA044E,
    locationnames.csl4_patchouli_3sc_ss:   0xFA044F,
    locationnames.csl1_patchouli_3sc_ps:   0xFA0450,
    locationnames.csl2_patchouli_3sc_ps:   0xFA0451,
    locationnames.csl3_patchouli_3sc_ps:   0xFA0452,
    locationnames.csl4_patchouli_3sc_ps:   0xFA0453,
    locationnames.csl1_patchouli_3sc_pp:   0xFA0454,
    locationnames.csl2_patchouli_3sc_pp:   0xFA0455,
    locationnames.csl3_patchouli_3sc_pp:   0xFA0456,
    locationnames.csl4_patchouli_3sc_pp:   0xFA0457,
    locationnames.csl1_patchouli_4sc_ss:   0xFA0458,
    locationnames.csl2_patchouli_4sc_ss:   0xFA0459,
    locationnames.csl3_patchouli_4sc_ss:   0xFA045A,
    locationnames.csl4_patchouli_4sc_ss:   0xFA045B,
    locationnames.csl1_patchouli_4sc_em:   0xFA045C,
    locationnames.csl2_patchouli_4sc_em:   0xFA045D,
    locationnames.csl3_patchouli_4sc_em:   0xFA045E,
    locationnames.csl4_patchouli_4sc_em:   0xFA045F,
    locationnames.csl1_patchouli_5sc_rf:   0xFA0460,
    locationnames.csl2_patchouli_5sc_rf:   0xFA0461,
    locationnames.csl3_patchouli_5sc_rf:   0xFA0462,
    locationnames.csl4_patchouli_5sc_rf:   0xFA0463,
    locationnames.csl1_patchouli_5sc_ps:   0xFA0464,
    locationnames.csl2_patchouli_5sc_ps:   0xFA0465,
    locationnames.csl3_patchouli_5sc_ps:   0xFA0466,
    locationnames.csl4_patchouli_5sc_ps:   0xFA0467,
    locationnames.csl1_patchouli_5sc_rdr:  0xFA0468,
    locationnames.csl2_patchouli_5sc_rdr:  0xFA0469,
    locationnames.csl3_patchouli_5sc_rdr:  0xFA046A,
    locationnames.csl4_patchouli_5sc_rdr:  0xFA046B

}
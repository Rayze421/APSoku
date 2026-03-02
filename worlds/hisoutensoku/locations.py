from typing import Dict, int, str
from worlds.AutoWorld import World
from .data import locationnames
from BaseClasses import Location, Multiworld

class SokuLocation(Location):
    game: str = "Touhou 12.3 - Hisoutensoku"



goal_location_table = {
    locationnames.story_end:          0xFF0000,
    locationnames.sanae_story_end:    0xFF0001,
    locationnames.cirno_story_end:    0xFF0002,
    locationnames.meiling_story_end:  0xFF0003,
    
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
    locationnames.sanae_cirno_s1:   0xFF1005,
    locationnames.sanae_cirno_s2:   0xFF1006,
    locationnames.sanae_meiling_s1: 0xFF1007,
    locationnames.sanae_meiling_s2: 0xFF1008,
    locationnames.sanae_reimu_s1:   0xFF1009,
    locationnames.sanae_reimu_s2:   0xFF100A,
    locationnames.sanae_reimu_s3:   0xFF100B,
    locationnames.sanae_okuu_s1:    0xFF100C,
    locationnames.sanae_okuu_s2:    0xFF100D,
    locationnames.sanae_okuu_s3:    0xFF100E,
    locationnames.sanae_okuu_s4:    0xFF100F,
    locationnames.sanae_suwako_s1:  0xFF1010,
    locationnames.sanae_suwako_s2:  0xFF1011,
    locationnames.sanae_suwako_s3:  0xFF1012,
    locationnames.sanae_suwako_s4:  0xFF1013,
    locationnames.sanae_suwako_s5:  0xFF1014

}

cirno_story_stage_table = {
    locationnames.cirno_story_1: 0xFF1100,
    locationnames.cirno_story_2: 0xFF1101,
    locationnames.cirno_story_3: 0xFF1102,
    locationnames.cirno_story_4: 0xFF1103,
    locationnames.cirno_story_5: 0xFF1104

}

cirno_story_spell_table = {
    locationnames.cirno_sanae_s1:    0xFF1105,
    locationnames.cirno_sanae_s2:    0xFF1106,
    locationnames.cirno_meiling_s1:  0xFF1107,
    locationnames.cirno_meiling_s2:  0xFF1108,
    locationnames.cirno_marisa_s1:   0xFF1109,
    locationnames.cirno_marisa_s2:   0xFF110A,
    locationnames.cirno_marisa_s3:   0xFF110B,
    locationnames.cirno_okuu_s1:     0xFF110C,
    locationnames.cirno_okuu_s2:     0xFF110D,
    locationnames.cirno_okuu_s3:     0xFF110E,
    locationnames.cirno_okuu_s4:     0xFF110F,
    locationnames.cirno_alice_s1:    0xFF1110,
    locationnames.cirno_alice_s2:    0xFF1111,
    locationnames.cirno_alice_s3:    0xFF1112,
    locationnames.cirno_alice_s4:    0xFF1113,
    locationnames.cirno_alice_s5:    0xFF1114

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
    locationnames.meiling_alice_s1:     0xFF1207,
    locationnames.meiling_alice_s2:     0xFF1208,
    locationnames.meiling_marisa_s1:    0xFF1209,
    locationnames.meiling_marisa_s2:    0xFF120A,
    locationnames.meiling_marisa_s3:    0xFF120B,
    locationnames.meiling_reimu_s1:     0xFF120C,
    locationnames.meiling_reimu_s2:     0xFF120D,
    locationnames.meiling_reimu_s3:     0xFF120E,
    locationnames.meiling_reimu_s4:     0xFF120F,
    locationnames.meiling_fish_s1:      0xFF1210,
    locationnames.meiling_fish_s2:      0xFF1211,
    locationnames.meiling_fish_s3:      0xFF1212,
    locationnames.meiling_fish_s4:      0xFF1213,
    locationnames.meiling_fish_s5:      0xFF1214

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

reimu_start_card_table = { #0xFF50100-FF50115
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

marisa_start_card_table = { #0xFF50200-FF50219
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
    locationnames.cslk1_reimu_236d:  0xFA0000,
    locationnames.cslk2_reimu_236d:  0xFA0001,
    locationnames.cslk4_reimu_236d:  0xFA0002,
    locationnames.cslk3_reimu_236d:  0xFA0003,
    locationnames.cslk1_reimu_236a1: 0xFA0004,
    locationnames.cslk2_reimu_236a1: 0xFA0005,
    locationnames.cslk3_reimu_236a1: 0xFA0006,
    locationnames.cslk4_reimu_236a1: 0xFA0007,
    locationnames.cslk1_reimu_236a2: 0xFA0008,
    locationnames.cslk2_reimu_236a2: 0xFA0009,
    locationnames.cslk3_reimu_236a2: 0xFA000A,
    locationnames.cslk4_reimu_236a2: 0xFA000B,
    locationnames.cslk1_reimu_623d:  0xFA000C,
    locationnames.cslk2_reimu_623d:  0xFA000D,
    locationnames.cslk3_reimu_623d:  0xFA000E,
    locationnames.cslk4_reimu_623d:  0xFA000F,
    locationnames.cslk1_reimu_623a1: 0xFA0010,
    locationnames.cslk2_reimu_623a1: 0xFA0011,
    locationnames.cslk3_reimu_623a1: 0xFA0012,
    locationnames.cslk4_reimu_623a1: 0xFA0013,
    locationnames.cslk1_reimu_623a2: 0xFA0014,
    locationnames.cslk2_reimu_623a2: 0xFA0015,
    locationnames.cslk3_reimu_623a2: 0xFA0016,
    locationnames.cslk4_reimu_623a2: 0xFA0017,
    locationnames.cslk1_reimu_214d:  0xFA0018,
    locationnames.cslk2_reimu_214d:  0xFA0019,
    locationnames.cslk3_reimu_214d:  0xFA001A,
    locationnames.cslk4_reimu_214d:  0xFA001B,
    locationnames.cslk1_reimu_214a1: 0xFA001C,
    locationnames.cslk2_reimu_214a1: 0xFA001D,
    locationnames.cslk3_reimu_214a1: 0xFA001E,
    locationnames.cslk4_reimu_214a1: 0xFA001F,
    locationnames.cslk1_reimu_214a2: 0xFA0020,
    locationnames.cslk2_reimu_214a2: 0xFA0021,
    locationnames.cslk3_reimu_214a2: 0xFA0022,
    locationnames.cslk4_reimu_214a2: 0xFA0023,
    locationnames.cslk1_reimu_421d:  0xFA0024,
    locationnames.cslk2_reimu_421d:  0xFA0025,
    locationnames.cslk3_reimu_421d:  0xFA0026,
    locationnames.cslk4_reimu_421d:  0xFA0027,
    locationnames.cslk1_reimu_421a1: 0xFA0028,
    locationnames.cslk2_reimu_421a1: 0xFA0029,
    locationnames.cslk3_reimu_421a1: 0xFA002A,
    locationnames.cslk4_reimu_421a1: 0xFA002B,
    locationnames.cslk1_reimu_421a2: 0xFA002C,
    locationnames.cslk2_reimu_421a2: 0xFA002D,
    locationnames.cslk3_reimu_421a2: 0xFA002E,
    locationnames.cslk4_reimu_421a2: 0xFA002F,

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
    locationnames.cslk1_marisa_236d:   0xFA0100,
    locationnames.cslk2_marisa_236d:   0xFA0101,
    locationnames.cslk3_marisa_236d:   0xFA0102,
    locationnames.cslk4_marisa_236d:   0xFA0103,
    locationnames.cslk1_marisa_236a1:  0xFA0104,
    locationnames.cslk2_marisa_236a1:  0xFA0105,
    locationnames.cslk3_marisa_236a1:  0xFA0106,
    locationnames.cslk4_marisa_236a1:  0xFA0107,
    locationnames.cslk1_marisa_236a2:  0xFA0108,
    locationnames.cslk2_marisa_236a2:  0xFA0109,
    locationnames.cslk3_marisa_236a2:  0xFA010A,
    locationnames.cslk4_marisa_236a2:  0xFA010B,
    locationnames.cslk1_marisa_623d:   0xFA010C,
    locationnames.cslk2_marisa_623d:   0xFA010D,
    locationnames.cslk3_marisa_623d:   0xFA010E,
    locationnames.cslk4_marisa_623d:   0xFA010F,
    locationnames.cslk1_marisa_623a1:  0xFA0110,
    locationnames.cslk2_marisa_623a1:  0xFA0111,
    locationnames.cslk3_marisa_623a1:  0xFA0112,
    locationnames.cslk4_marisa_623a1:  0xFA0113,
    locationnames.cslk1_marisa_623a2:  0xFA0114,
    locationnames.cslk2_marisa_623a2:  0xFA0115,
    locationnames.cslk3_marisa_623a2:  0xFA0116,
    locationnames.cslk4_marisa_623a2:  0xFA0117,
    locationnames.cslk1_marisa_214d:   0xFA0118,
    locationnames.cslk2_marisa_214d:   0xFA0119,
    locationnames.cslk3_marisa_214d:   0xFA011A,
    locationnames.cslk4_marisa_214d:   0xFA011B,
    locationnames.cslk1_marisa_214a1:  0xFA011C,
    locationnames.cslk2_marisa_214a1:  0xFA011D,
    locationnames.cslk3_marisa_214a1:  0xFA011E,
    locationnames.cslk4_marisa_214a1:  0xFA011F,
    locationnames.cslk1_marisa_214a2:  0xFA0120,
    locationnames.cslk2_marisa_214a2:  0xFA0121,
    locationnames.cslk3_marisa_214a2:  0xFA0122,
    locationnames.cslk4_marisa_214a2:  0xFA0123,
    locationnames.cslk1_marisa_22d:    0xFA0124,
    locationnames.cslk2_marisa_22d:    0xFA0125,
    locationnames.cslk3_marisa_22d:    0xFA0126,
    locationnames.cslk4_marisa_22d:    0xFA0127,
    locationnames.cslk1_marisa_22a1:   0xFA0128,
    locationnames.cslk2_marisa_22a1:   0xFA0129,
    locationnames.cslk3_marisa_22a1:   0xFA012A,
    locationnames.cslk4_marisa_22a1:   0xFA012B,
    locationnames.cslk1_marisa_22a2:   0xFA012C,
    locationnames.cslk2_marisa_22a2:   0xFA012D,
    locationnames.cslk3_marisa_22a2:   0xFA012E,
    locationnames.cslk4_marisa_22a2:   0xFA012F,
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
    locationnames.cslk1_sakuya_236d:   0xFA0200, 
    locationnames.cslk2_sakuya_236d:   0xFA0201, 
    locationnames.cslk3_sakuya_236d:   0xFA0202, 
    locationnames.cslk4_sakuya_236d:   0xFA0203, 
    locationnames.cslk1_sakuya_236a1:  0xFA0204, 
    locationnames.cslk2_sakuya_236a1:  0xFA0205, 
    locationnames.cslk3_sakuya_236a1:  0xFA0206, 
    locationnames.cslk4_sakuya_236a1:  0xFA0207, 
    locationnames.cslk1_sakuya_236a2:  0xFA0208, 
    locationnames.cslk2_sakuya_236a2:  0xFA0209, 
    locationnames.cslk3_sakuya_236a2:  0xFA020A, 
    locationnames.cslk4_sakuya_236a2:  0xFA020B, 
    locationnames.cslk1_sakuya_623d:   0xFA020C, 
    locationnames.cslk2_sakuya_623d:   0xFA020D, 
    locationnames.cslk3_sakuya_623d:   0xFA020E, 
    locationnames.cslk4_sakuya_623d:   0xFA020F, 
    locationnames.cslk1_sakuya_623a1:  0xFA0210, 
    locationnames.cslk2_sakuya_623a1:  0xFA0211, 
    locationnames.cslk3_sakuya_623a1:  0xFA0212, 
    locationnames.cslk4_sakuya_623a1:  0xFA0213, 
    locationnames.cslk1_sakuya_623a2:  0xFA0214, 
    locationnames.cslk2_sakuya_623a2:  0xFA0215, 
    locationnames.cslk3_sakuya_623a2:  0xFA0216, 
    locationnames.cslk4_sakuya_623a2:  0xFA0217, 
    locationnames.cslk1_sakuya_214d:   0xFA0218, 
    locationnames.cslk2_sakuya_214d:   0xFA0219, 
    locationnames.cslk3_sakuya_214d:   0xFA021A, 
    locationnames.cslk4_sakuya_214d:   0xFA021B, 
    locationnames.cslk1_sakuya_214a1:  0xFA021C, 
    locationnames.cslk2_sakuya_214a1:  0xFA021D, 
    locationnames.cslk3_sakuya_214a1:  0xFA021E, 
    locationnames.cslk4_sakuya_214a1:  0xFA021F, 
    locationnames.cslk1_sakuya_214a2:  0xFA0220, 
    locationnames.cslk2_sakuya_214a2:  0xFA0221, 
    locationnames.cslk3_sakuya_214a2:  0xFA0222, 
    locationnames.cslk4_sakuya_214a2:  0xFA0223, 
    locationnames.cslk1_sakuya_22d:    0xFA0224, 
    locationnames.cslk2_sakuya_22d:    0xFA0225, 
    locationnames.cslk3_sakuya_22d:    0xFA0226, 
    locationnames.cslk4_sakuya_22d:    0xFA0227, 
    locationnames.cslk1_sakuya_22a1:   0xFA0228, 
    locationnames.cslk2_sakuya_22a1:   0xFA0229, 
    locationnames.cslk3_sakuya_22a1:   0xFA022A, 
    locationnames.cslk4_sakuya_22a1:   0xFA022B, 
    locationnames.cslk1_sakuya_22a2:   0xFA022C, 
    locationnames.cslk2_sakuya_22a2:   0xFA022D, 
    locationnames.cslk3_sakuya_22a2:   0xFA022E, 
    locationnames.cslk4_sakuya_22a2:   0xFA022F, 
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
    locationnames.cslk1_alice_236d:    0xFA0300,
    locationnames.cslk2_alice_236d:    0xFA0301,
    locationnames.cslk3_alice_236d:    0xFA0302,
    locationnames.cslk4_alice_236d:    0xFA0303,
    locationnames.cslk1_alice_236a1:   0xFA0304,
    locationnames.cslk2_alice_236a1:   0xFA0305,
    locationnames.cslk3_alice_236a1:   0xFA0306,
    locationnames.cslk4_alice_236a1:   0xFA0307,
    locationnames.cslk1_alice_236a2:   0xFA0308,
    locationnames.cslk2_alice_236a2:   0xFA0309,
    locationnames.cslk3_alice_236a2:   0xFA030A,
    locationnames.cslk4_alice_236a2:   0xFA030B,
    locationnames.cslk1_alice_623d:    0xFA030C,
    locationnames.cslk2_alice_623d:    0xFA030D,
    locationnames.cslk3_alice_623d:    0xFA030E,
    locationnames.cslk4_alice_623d:    0xFA030F,
    locationnames.cslk1_alice_623a1:   0xFA0310,
    locationnames.cslk2_alice_623a1:   0xFA0311,
    locationnames.cslk3_alice_623a1:   0xFA0312,
    locationnames.cslk4_alice_623a1:   0xFA0313,
    locationnames.cslk1_alice_623a2:   0xFA0314,
    locationnames.cslk2_alice_623a2:   0xFA0315,
    locationnames.cslk3_alice_623a2:   0xFA0316,
    locationnames.cslk4_alice_623a2:   0xFA0317,
    locationnames.cslk1_alice_214d:    0xFA0318,
    locationnames.cslk2_alice_214d:    0xFA0319,
    locationnames.cslk3_alice_214d:    0xFA031A,
    locationnames.cslk4_alice_214d:    0xFA031B,
    locationnames.cslk1_alice_214a1:   0xFA031C,
    locationnames.cslk2_alice_214a1:   0xFA031D,
    locationnames.cslk3_alice_214a1:   0xFA031E,
    locationnames.cslk4_alice_214a1:   0xFA031F,
    locationnames.cslk1_alice_214a2:   0xFA0320,
    locationnames.cslk2_alice_214a2:   0xFA0321,
    locationnames.cslk3_alice_214a2:   0xFA0322,
    locationnames.cslk4_alice_214a2:   0xFA0323,
    locationnames.cslk1_alice_22d:     0xFA0324,
    locationnames.cslk2_alice_22d:     0xFA0325,
    locationnames.cslk3_alice_22d:     0xFA0326,
    locationnames.cslk4_alice_22d:     0xFA0327,
    locationnames.cslk1_alice_22a1:    0xFA0328,
    locationnames.cslk2_alice_22a1:    0xFA0329,
    locationnames.cslk3_alice_22a1:    0xFA032A,
    locationnames.cslk4_alice_22a1:    0xFA032B,
    locationnames.cslk1_alice_22a2:    0xFA032C,
    locationnames.cslk2_alice_22a2:    0xFA032D,
    locationnames.cslk3_alice_22a2:    0xFA032E,
    locationnames.cslk4_alice_22a2:    0xFA032F,

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
    locationnames.cslk1_patchouli_236d:    0xFA0400,
    locationnames.cslk2_patchouli_236d:    0xFA0401,
    locationnames.cslk3_patchouli_236d:    0xFA0402,
    locationnames.cslk4_patchouli_236d:    0xFA0403,
    locationnames.cslk1_patchouli_236a1:   0xFA0404,
    locationnames.cslk2_patchouli_236a1:   0xFA0405,
    locationnames.cslk3_patchouli_236a1:   0xFA0406,
    locationnames.cslk4_patchouli_236a1:   0xFA0407,
    locationnames.cslk1_patchouli_236a2:   0xFA0408,
    locationnames.cslk2_patchouli_236a2:   0xFA0409,
    locationnames.cslk3_patchouli_236a2:   0xFA040A,
    locationnames.cslk4_patchouli_236a2:   0xFA040B,
    locationnames.cslk1_patchouli_623d:    0xFA040C,
    locationnames.cslk2_patchouli_623d:    0xFA040D,
    locationnames.cslk3_patchouli_623d:    0xFA040E,
    locationnames.cslk4_patchouli_623d:    0xFA040F,
    locationnames.cslk1_patchouli_623a1:   0xFA0410,
    locationnames.cslk2_patchouli_623a1:   0xFA0411,
    locationnames.cslk3_patchouli_623a1:   0xFA0412,
    locationnames.cslk4_patchouli_623a1:   0xFA0413,
    locationnames.cslk1_patchouli_623a2:   0xFA0414,
    locationnames.cslk2_patchouli_623a2:   0xFA0415,
    locationnames.cslk3_patchouli_623a2:   0xFA0416,
    locationnames.cslk4_patchouli_623a2:   0xFA0417,
    locationnames.cslk1_patchouli_214d:    0xFA0418,
    locationnames.cslk4_patchouli_214d:    0xFA0419,
    locationnames.cslk3_patchouli_214d:    0xFA041A,
    locationnames.cslk4_patchouli_214d:    0xFA041B,
    locationnames.cslk1_patchouli_214a1:   0xFA041C,
    locationnames.cslk2_patchouli_214a1:   0xFA041D,
    locationnames.cslk3_patchouli_214a1:   0xFA041E,
    locationnames.cslk4_patchouli_214a1:   0xFA041F,
    locationnames.cslk1_patchouli_214a2:   0xFA0420,
    locationnames.cslk2_patchouli_214a2:   0xFA0421,
    locationnames.cslk3_patchouli_214a2:   0xFA0422,
    locationnames.cslk4_patchouli_214a2:   0xFA0423,
    locationnames.cslk1_patchouli_421d:    0xFA0424,
    locationnames.cslk2_patchouli_421d:    0xFA0425,
    locationnames.cslk3_patchouli_421d:    0xFA0426,
    locationnames.cslk4_patchouli_421d:    0xFA0427,
    locationnames.cslk1_patchouli_421a1:   0xFA0428,
    locationnames.cslk2_patchouli_421a1:   0xFA0429,
    locationnames.cslk3_patchouli_421a1:   0xFA042A,
    locationnames.cslk4_patchouli_421a1:   0xFA042B,
    locationnames.cslk1_patchouli_421a2:   0xFA042C,
    locationnames.cslk2_patchouli_421a2:   0xFA042D,
    locationnames.cslk3_patchouli_421a2:   0xFA042E,
    locationnames.cslk4_patchouli_421a2:   0xFA042F,
    locationnames.cslk1_patchouli_22d:     0xFA0430,
    locationnames.cslk2_patchouli_22d:     0xFA0431,
    locationnames.cslk3_patchouli_22d:     0xFA0432,
    locationnames.cslk4_patchouli_22d:     0xFA0433,
    locationnames.cslk1_patchouli_22a1:    0xFA0434,
    locationnames.cslk2_patchouli_22a1:    0xFA0435,
    locationnames.cslk3_patchouli_22a1:    0xFA0436,
    locationnames.cslk4_patchouli_22a1:    0xFA0437,
    locationnames.cslk1_patchouli_22a2:    0xFA0438,
    locationnames.cslk2_patchouli_22a2:    0xFA0439,
    locationnames.cslk3_patchouli_22a2:    0xFA043A,
    locationnames.cslk4_patchouli_22a2:    0xFA043B

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

youmu_skill_loc_table = { #0xFA0500 - FA052F
    locationnames.cslk1_youmu_236d:   0xFA0500,
    locationnames.cslk2_youmu_236d:   0xFA0501,
    locationnames.cslk3_youmu_236d:   0xFA0502,
    locationnames.cslk4_youmu_236d:   0xFA0503,
    locationnames.cslk1_youmu_236a1:  0xFA0504,
    locationnames.cslk2_youmu_236a1:  0xFA0505,
    locationnames.cslk3_youmu_236a1:  0xFA0506,
    locationnames.cslk4_youmu_236a1:  0xFA0507,
    locationnames.cslk1_youmu_236a2:  0xFA0508,
    locationnames.cslk2_youmu_236a2:  0xFA0509,
    locationnames.cslk3_youmu_236a2:  0xFA050A,
    locationnames.cslk4_youmu_236a2:  0xFA050B,
    locationnames.cslk1_youmu_623d:   0xFA050C,
    locationnames.cslk2_youmu_623d:   0xFA050D,
    locationnames.cslk3_youmu_623d:   0xFA050E,
    locationnames.cslk4_youmu_623d:   0xFA050F,
    locationnames.cslk1_youmu_623a1:  0xFA0510,
    locationnames.cslk2_youmu_623a1:  0xFA0511,
    locationnames.cslk3_youmu_623a1:  0xFA0512,
    locationnames.cslk4_youmu_623a1:  0xFA0513,
    locationnames.cslk1_youmu_623a2:  0xFA0514,
    locationnames.cslk2_youmu_623a2:  0xFA0515,
    locationnames.cslk3_youmu_623a2:  0xFA0516,
    locationnames.cslk4_youmu_623a2:  0xFA0517,
    locationnames.cslk1_youmu_214d:   0xFA0518,
    locationnames.cslk2_youmu_214d:   0xFA0519,
    locationnames.cslk3_youmu_214d:   0xFA051A,
    locationnames.cslk4_youmu_214d:   0xFA051B,
    locationnames.cslk1_youmu_214a1:  0xFA051C,
    locationnames.cslk2_youmu_214a1:  0xFA051D,
    locationnames.cslk3_youmu_214a1:  0xFA051E,
    locationnames.cslk4_youmu_214a1:  0xFA051F,
    locationnames.cslk1_youmu_214a2:  0xFA0520,
    locationnames.cslk2_youmu_214a2:  0xFA0521,
    locationnames.cslk3_youmu_214a2:  0xFA0522,
    locationnames.cslk4_youmu_214a2:  0xFA0523,
    locationnames.cslk1_youmu_22d:    0xFA0524,
    locationnames.cslk2_youmu_22d:    0xFA0525,
    locationnames.cslk3_youmu_22d:    0xFA0526,
    locationnames.cslk4_youmu_22d:    0xFA0527,
    locationnames.cslk1_youmu_22a1:   0xFA0528,
    locationnames.cslk2_youmu_22a1:   0xFA0529,
    locationnames.cslk3_youmu_22a1:   0xFA052A,
    locationnames.cslk4_youmu_22a1:   0xFA052B,
    locationnames.cslk1_youmu_22a2:   0xFA052C,
    locationnames.cslk2_youmu_22a2:   0xFA052D,
    locationnames.cslk3_youmu_22a2:   0xFA052E,
    locationnames.cslk4_youmu_22a2:   0xFA052F,

}

youmu_spell_loc_table = { #0xFA0530 - FA0557
    locationnames.csl1_youmu_2sc_sop:    0xFA0530,
    locationnames.csl2_youmu_2sc_sop:    0xFA0531,
    locationnames.csl3_youmu_2sc_sop:    0xFA0532,
    locationnames.csl4_youmu_2sc_sop:    0xFA0533,
    locationnames.csl1_youmu_2sc_gwop:   0xFA0534,
    locationnames.csl2_youmu_2sc_gwop:   0xFA0535,
    locationnames.csl3_youmu_2sc_gwop:   0xFA0536,
    locationnames.csl4_youmu_2sc_gwop:   0xFA0537,
    locationnames.csl1_youmu_3sc_m:      0xFA0538,
    locationnames.csl2_youmu_3sc_m:      0xFA0539,
    locationnames.csl3_youmu_3sc_m:      0xFA053A,
    locationnames.csl4_youmu_3sc_m:      0xFA053B,
    locationnames.csl1_youmu_3sc_tcb:    0xFA053C,
    locationnames.csl2_youmu_3sc_tcb:    0xFA053D,
    locationnames.csl3_youmu_3sc_tcb:    0xFA053E,
    locationnames.csl4_youmu_3sc_tcb:    0xFA053F,
    locationnames.csl1_youmu_3sc_soc:    0xFA0540,
    locationnames.csl2_youmu_3sc_soc:    0xFA0541,
    locationnames.csl3_youmu_3sc_soc:    0xFA0542,
    locationnames.csl4_youmu_3sc_soc:    0xFA0543,
    locationnames.csl1_youmu_4sc_rfd:    0xFA0544,
    locationnames.csl2_youmu_4sc_rfd:    0xFA0545,
    locationnames.csl3_youmu_4sc_rfd:    0xFA0546,
    locationnames.csl4_youmu_4sc_rfd:    0xFA0547,
    locationnames.csl1_youmu_4sc_atn:    0xFA0548,
    locationnames.csl2_youmu_4sc_atn:    0xFA0549,
    locationnames.csl3_youmu_4sc_atn:    0xFA054A,
    locationnames.csl4_youmu_4sc_atn:    0xFA054B,
    locationnames.csl1_youmu_5sc_soe:    0xFA054C,
    locationnames.csl2_youmu_5sc_soe:    0xFA054D,
    locationnames.csl3_youmu_5sc_soe:    0xFA054E,
    locationnames.csl4_youmu_5sc_soe:    0xFA054F,
    locationnames.csl1_youmu_5sc_solad:  0xFA0550,
    locationnames.csl2_youmu_5sc_solad:  0xFA0551,
    locationnames.csl3_youmu_5sc_solad:  0xFA0552,
    locationnames.csl4_youmu_5sc_solad:  0xFA0553,
    locationnames.csl1_youmu_5sc_src:    0xFA0554,
    locationnames.csl2_youmu_5sc_src:    0xFA0555,
    locationnames.csl3_youmu_5sc_src:    0xFA0556,
    locationnames.csl4_youmu_5sc_src:    0xFA0557,

}

remilia_skill_loc_table = { #0xFA0600 - FA062F
    locationnames.cslk1_remilia_236d:   0xFA0600,
    locationnames.cslk2_remilia_236d:   0xFA0601,
    locationnames.cslk3_remilia_236d:   0xFA0602,
    locationnames.cslk4_remilia_236d:   0xFA0603,
    locationnames.cslk1_remilia_236a1:  0xFA0604,
    locationnames.cslk2_remilia_236a1:  0xFA0605,
    locationnames.cslk3_remilia_236a1:  0xFA0606,
    locationnames.cslk4_remilia_236a1:  0xFA0607,
    locationnames.cslk1_remilia_236a2:  0xFA0608,
    locationnames.cslk2_remilia_236a2:  0xFA0609,
    locationnames.cslk3_remilia_236a2:  0xFA060A,
    locationnames.cslk4_remilia_236a2:  0xFA060B,
    locationnames.cslk1_remilia_623d:   0xFA060C,
    locationnames.cslk2_remilia_623d:   0xFA060D,
    locationnames.cslk3_remilia_623d:   0xFA060E,
    locationnames.cslk4_remilia_623d:   0xFA060F,
    locationnames.cslk1_remilia_623a1:  0xFA0610,
    locationnames.cslk2_remilia_623a1:  0xFA0611,
    locationnames.cslk3_remilia_623a1:  0xFA0612,
    locationnames.cslk4_remilia_623a1:  0xFA0613,
    locationnames.cslk1_remilia_623a2:  0xFA0614,
    locationnames.cslk2_remilia_623a2:  0xFA0615,
    locationnames.cslk3_remilia_623a2:  0xFA0616,
    locationnames.cslk4_remilia_623a2:  0xFA0617,
    locationnames.cslk1_remilia_214d:   0xFA0618,
    locationnames.cslk2_remilia_214d:   0xFA0619,
    locationnames.cslk3_remilia_214d:   0xFA061A,
    locationnames.cslk4_remilia_214d:   0xFA061B,
    locationnames.cslk1_remilia_214a1:  0xFA061C,
    locationnames.cslk2_remilia_214a1:  0xFA061D,
    locationnames.cslk3_remilia_214a1:  0xFA061E,
    locationnames.cslk4_remilia_214a1:  0xFA061F,
    locationnames.cslk1_remilia_214a2:  0xFA0620,
    locationnames.cslk2_remilia_214a2:  0xFA0621,
    locationnames.cslk3_remilia_214a2:  0xFA0622,
    locationnames.cslk4_remilia_214a2:  0xFA0623,
    locationnames.cslk1_remilia_22d:    0xFA0624,
    locationnames.cslk2_remilia_22d:    0xFA0625,
    locationnames.cslk3_remilia_22d:    0xFA0626,
    locationnames.cslk4_remilia_22d:    0xFA0627,
    locationnames.cslk1_remilia_22a1:   0xFA0628,
    locationnames.cslk2_remilia_22a1:   0xFA0629,
    locationnames.cslk3_remilia_22a1:   0xFA062A,
    locationnames.cslk4_remilia_22a1:   0xFA062B,
    locationnames.cslk1_remilia_22a2:   0xFA062C,
    locationnames.cslk2_remilia_22a2:   0xFA062D,
    locationnames.cslk3_remilia_22a2:   0xFA062E,
    locationnames.cslk4_remilia_22a2:   0xFA062F,

}

remilia_spell_loc_table = { #0xFA0630 - FA0657
    locationnames.csl1_remilia_2sc_hb:    0xFA0630,
    locationnames.csl2_remilia_2sc_hb:    0xFA0631,
    locationnames.csl3_remilia_2sc_hb:    0xFA0632,
    locationnames.csl4_remilia_2sc_hb:    0xFA0633,
    locationnames.csl1_remilia_2sc_dkc:   0xFA0634,
    locationnames.csl2_remilia_2sc_dkc:   0xFA0635,
    locationnames.csl3_remilia_2sc_dkc:   0xFA0636,
    locationnames.csl4_remilia_2sc_dkc:   0xFA0637,
    locationnames.csl1_remilia_3sc_rtnc:  0xFA0638,
    locationnames.csl2_remilia_3sc_rtnc:  0xFA0639,
    locationnames.csl3_remilia_3sc_rtnc:  0xFA063A,
    locationnames.csl4_remilia_3sc_rtnc:  0xFA063B,
    locationnames.csl1_remilia_3sc_bls:   0xFA063C,
    locationnames.csl2_remilia_3sc_bls:   0xFA063D,
    locationnames.csl3_remilia_3sc_bls:   0xFA063E,
    locationnames.csl4_remilia_3sc_bls:   0xFA063F,
    locationnames.csl1_remilia_3sc_mf:    0xFA0640,
    locationnames.csl2_remilia_3sc_mf:    0xFA0641,
    locationnames.csl3_remilia_3sc_mf:    0xFA0642,
    locationnames.csl4_remilia_3sc_mf:    0xFA0643,
    locationnames.csl1_remilia_4sc_stg:   0xFA0644,
    locationnames.csl2_remilia_4sc_stg:   0xFA0645,
    locationnames.csl3_remilia_4sc_stg:   0xFA0646,
    locationnames.csl4_remilia_4sc_stg:   0xFA0647,
    locationnames.csl1_remilia_4sc_mv:    0xFA0648,
    locationnames.csl2_remilia_4sc_mv:    0xFA0649,
    locationnames.csl3_remilia_4sc_mv:    0xFA064A,
    locationnames.csl4_remilia_4sc_mv:    0xFA064B,
    locationnames.csl1_remilia_4sc_rs:    0xFA064C,
    locationnames.csl2_remilia_4sc_rs:    0xFA064D,
    locationnames.csl3_remilia_4sc_rs:    0xFA064E,
    locationnames.csl4_remilia_4sc_rs:    0xFA064F,
    locationnames.csl1_remilia_5sc_sd:    0xFA0650,
    locationnames.csl2_remilia_5sc_sd:    0xFA0651,
    locationnames.csl3_remilia_5sc_sd:    0xFA0652,
    locationnames.csl4_remilia_5sc_sd:    0xFA0653,
    locationnames.csl1_remilia_5sc_dc:    0xFA0654,
    locationnames.csl2_remilia_5sc_dc:    0xFA0655,
    locationnames.csl3_remilia_5sc_dc:    0xFA0656,
    locationnames.csl4_remilia_5sc_dc:    0xFA0657,

}

yuyuko_skill_loc_table = { #0xFA0700 - FA072F
    locationnames.cslk1_yuyuko_236d:   0xFA0700,
    locationnames.cslk2_yuyuko_236d:   0xFA0701,
    locationnames.cslk3_yuyuko_236d:   0xFA0702,
    locationnames.cslk4_yuyuko_236d:   0xFA0703,
    locationnames.cslk1_yuyuko_236a1:  0xFA0704,
    locationnames.cslk2_yuyuko_236a1:  0xFA0705,
    locationnames.cslk3_yuyuko_236a1:  0xFA0706,
    locationnames.cslk4_yuyuko_236a1:  0xFA0707,
    locationnames.cslk1_yuyuko_236a2:  0xFA0708,
    locationnames.cslk2_yuyuko_236a2:  0xFA0709,
    locationnames.cslk3_yuyuko_236a2:  0xFA070A,
    locationnames.cslk4_yuyuko_236a2:  0xFA070B,
    locationnames.cslk1_yuyuko_623d:   0xFA070C,
    locationnames.cslk2_yuyuko_623d:   0xFA070D,
    locationnames.cslk3_yuyuko_623d:   0xFA070E,
    locationnames.cslk4_yuyuko_623d:   0xFA070F,
    locationnames.cslk1_yuyuko_623a1:  0xFA0710,
    locationnames.cslk2_yuyuko_623a1:  0xFA0711,
    locationnames.cslk3_yuyuko_623a1:  0xFA0712,
    locationnames.cslk4_yuyuko_623a1:  0xFA0713,
    locationnames.cslk1_yuyuko_623a2:  0xFA0714,
    locationnames.cslk2_yuyuko_623a2:  0xFA0715,
    locationnames.cslk3_yuyuko_623a2:  0xFA0716,
    locationnames.cslk4_yuyuko_623a2:  0xFA0717,
    locationnames.cslk1_yuyuko_214d:   0xFA0718,
    locationnames.cslk2_yuyuko_214d:   0xFA0719,
    locationnames.cslk3_yuyuko_214d:   0xFA071A,
    locationnames.cslk4_yuyuko_214d:   0xFA071B,
    locationnames.cslk1_yuyuko_214a1:  0xFA071C,
    locationnames.cslk2_yuyuko_214a1:  0xFA071D,
    locationnames.cslk3_yuyuko_214a1:  0xFA071E,
    locationnames.cslk4_yuyuko_214a1:  0xFA071F,
    locationnames.cslk1_yuyuko_214a2:  0xFA0720,
    locationnames.cslk2_yuyuko_214a2:  0xFA0721,
    locationnames.cslk3_yuyuko_214a2:  0xFA0722,
    locationnames.cslk4_yuyuko_214a2:  0xFA0723,
    locationnames.cslk1_yuyuko_421d:   0xFA0724,
    locationnames.cslk2_yuyuko_421d:   0xFA0725,
    locationnames.cslk3_yuyuko_421d:   0xFA0726,
    locationnames.cslk4_yuyuko_421d:   0xFA0727,
    locationnames.cslk1_yuyuko_421a1:  0xFA0728,
    locationnames.cslk2_yuyuko_421a1:  0xFA0729,
    locationnames.cslk3_yuyuko_421a1:  0xFA072A,
    locationnames.cslk4_yuyuko_421a1:  0xFA072B,
    locationnames.cslk1_yuyuko_421a2:  0xFA072C,
    locationnames.cslk2_yuyuko_421a2:  0xFA072D,
    locationnames.cslk3_yuyuko_421a2:  0xFA072E,
    locationnames.cslk4_yuyuko_421a2:  0xFA072F,

}

yuyuko_spell_loc_table = { #0xFA0730 - FA075B
    locationnames.csl1_yuyuko_1sc_pttu:  0xFA0730,
    locationnames.csl2_yuyuko_1sc_pttu:  0xFA0731,
    locationnames.csl3_yuyuko_1sc_pttu:  0xFA0732,
    locationnames.csl4_yuyuko_1sc_pttu:  0xFA0733,
    locationnames.csl1_yuyuko_2sc_gd:    0xFA0734,
    locationnames.csl2_yuyuko_2sc_gd:    0xFA0735,
    locationnames.csl3_yuyuko_2sc_gd:    0xFA0736,
    locationnames.csl4_yuyuko_2sc_gd:    0xFA0737,
    locationnames.csl1_yuyuko_2sc_ad:    0xFA0738,
    locationnames.csl2_yuyuko_2sc_ad:    0xFA0739,
    locationnames.csl3_yuyuko_2sc_ad:    0xFA073A,
    locationnames.csl4_yuyuko_2sc_ad:    0xFA073B,
    locationnames.csl1_yuyuko_2sc_atbf:  0xFA073C,
    locationnames.csl2_yuyuko_2sc_atbf:  0xFA073D,
    locationnames.csl3_yuyuko_2sc_atbf:  0xFA073E,
    locationnames.csl4_yuyuko_2sc_atbf:  0xFA073F,
    locationnames.csl1_yuyuko_3sc_itta:  0xFA0740,
    locationnames.csl2_yuyuko_3sc_itta:  0xFA0741,
    locationnames.csl3_yuyuko_3sc_itta:  0xFA0742,
    locationnames.csl4_yuyuko_3sc_itta:  0xFA0743,
    locationnames.csl1_yuyuko_3sc_rb:    0xFA0744,
    locationnames.csl2_yuyuko_3sc_rb:    0xFA0745,
    locationnames.csl3_yuyuko_3sc_rb:    0xFA0746,
    locationnames.csl4_yuyuko_3sc_rb:    0xFA0747,
    locationnames.csl1_yuyuko_4sc_en:    0xFA0748,
    locationnames.csl2_yuyuko_4sc_en:    0xFA0749,
    locationnames.csl3_yuyuko_4sc_en:    0xFA074A,
    locationnames.csl4_yuyuko_4sc_en:    0xFA074B,
    locationnames.csl1_yuyuko_4sc_tttn:  0xFA074C,
    locationnames.csl2_yuyuko_4sc_tttn:  0xFA074D,
    locationnames.csl3_yuyuko_4sc_tttn:  0xFA074E,
    locationnames.csl4_yuyuko_4sc_tttn:  0xFA074F,
    locationnames.csl1_yuyuko_4sc_dl:    0xFA0750,
    locationnames.csl2_yuyuko_4sc_dl:    0xFA0751,
    locationnames.csl3_yuyuko_4sc_dl:    0xFA0752,
    locationnames.csl4_yuyuko_4sc_dl:    0xFA0753,
    locationnames.csl1_yuyuko_5sc_gh:    0xFA0754,
    locationnames.csl2_yuyuko_5sc_gh:    0xFA0755,
    locationnames.csl3_yuyuko_5sc_gh:    0xFA0756,
    locationnames.csl4_yuyuko_5sc_gh:    0xFA0757,
    locationnames.csl1_yuyuko_5sc_socb:  0xFA0758,
    locationnames.csl2_yuyuko_5sc_socb:  0xFA0759,
    locationnames.csl3_yuyuko_5sc_socb:  0xFA075A,
    locationnames.csl4_yuyuko_5sc_socb:  0xFA075B,

}

yukari_skill_loc_table = { #0xFA0800 - FA082F
    locationnames.cslk1_yukari_236d:   0xFA0800,
    locationnames.cslk2_yukari_236d:   0xFA0801,
    locationnames.cslk3_yukari_236d:   0xFA0802,
    locationnames.cslk4_yukari_236d:   0xFA0803,
    locationnames.cslk1_yukari_236a1:  0xFA0804,
    locationnames.cslk2_yukari_236a1:  0xFA0805,
    locationnames.cslk3_yukari_236a1:  0xFA0806,
    locationnames.cslk4_yukari_236a1:  0xFA0807,
    locationnames.cslk1_yukari_236a2:  0xFA0808,
    locationnames.cslk2_yukari_236a2:  0xFA0809,
    locationnames.cslk3_yukari_236a2:  0xFA080A,
    locationnames.cslk4_yukari_236a2:  0xFA080B,
    locationnames.cslk1_yukari_623d:   0xFA080C,
    locationnames.cslk2_yukari_623d:   0xFA080D,
    locationnames.cslk3_yukari_623d:   0xFA080E,
    locationnames.cslk4_yukari_623d:   0xFA080F,
    locationnames.cslk1_yukari_623a1:  0xFA0810,
    locationnames.cslk2_yukari_623a1:  0xFA0811,
    locationnames.cslk3_yukari_623a1:  0xFA0812,
    locationnames.cslk4_yukari_623a1:  0xFA0813,
    locationnames.cslk1_yukari_623a2:  0xFA0814,
    locationnames.cslk2_yukari_623a2:  0xFA0815,
    locationnames.cslk3_yukari_623a2:  0xFA0816,
    locationnames.cslk4_yukari_623a2:  0xFA0817,
    locationnames.cslk1_yukari_214d:   0xFA0818,
    locationnames.cslk2_yukari_214d:   0xFA0819,
    locationnames.cslk3_yukari_214d:   0xFA081A,
    locationnames.cslk4_yukari_214d:   0xFA081B,
    locationnames.cslk1_yukari_214a1:  0xFA081C,
    locationnames.cslk2_yukari_214a1:  0xFA081D,
    locationnames.cslk3_yukari_214a1:  0xFA081E,
    locationnames.cslk4_yukari_214a1:  0xFA081F,
    locationnames.cslk1_yukari_214a2:  0xFA0820,
    locationnames.cslk2_yukari_214a2:  0xFA0821,
    locationnames.cslk3_yukari_214a2:  0xFA0822,
    locationnames.cslk4_yukari_214a2:  0xFA0823,
    locationnames.cslk1_yukari_421d:   0xFA0824,
    locationnames.cslk2_yukari_421d:   0xFA0825,
    locationnames.cslk3_yukari_421d:   0xFA0826,
    locationnames.cslk4_yukari_421d:   0xFA0827,
    locationnames.cslk1_yukari_421a1:  0xFA0828,
    locationnames.cslk2_yukari_421a1:  0xFA0829,
    locationnames.cslk3_yukari_421a1:  0xFA082A,
    locationnames.cslk4_yukari_421a1:  0xFA082B,
    locationnames.cslk1_yukari_421a2:  0xFA082C,
    locationnames.cslk2_yukari_421a2:  0xFA082D,
    locationnames.cslk3_yukari_421a2:  0xFA082E,
    locationnames.cslk4_yukari_421a2:  0xFA082F,

}

yukari_spell_loc_table = { #0xFA0830 - FA0857
    locationnames.csl1_yukari_1sc_bbtat:  0xFA0830,
    locationnames.csl2_yukari_1sc_bbtat:  0xFA0831,
    locationnames.csl3_yukari_1sc_bbtat:  0xFA0832,
    locationnames.csl4_yukari_1sc_bbtat:  0xFA0833,
    locationnames.csl1_yukari_1sc_c:      0xFA0834,
    locationnames.csl2_yukari_1sc_c:      0xFA0835,
    locationnames.csl3_yukari_1sc_c:      0xFA0836,
    locationnames.csl4_yukari_1sc_c:      0xFA0837,
    locationnames.csl1_yukari_2sc_lwv:    0xFA0838,
    locationnames.csl2_yukari_2sc_lwv:    0xFA0839,
    locationnames.csl3_yukari_2sc_lwv:    0xFA083A,
    locationnames.csl4_yukari_2sc_lwv:    0xFA083B,
    locationnames.csl1_yukari_3sc_qb:     0xFA083C,
    locationnames.csl2_yukari_3sc_qb:     0xFA083D,
    locationnames.csl3_yukari_3sc_qb:     0xFA083E,
    locationnames.csl4_yukari_3sc_qb:     0xFA083F,
    locationnames.csl1_yukari_3sc_ry:     0xFA0840,
    locationnames.csl2_yukari_3sc_ry:     0xFA0841,
    locationnames.csl3_yukari_3sc_ry:     0xFA0842,
    locationnames.csl4_yukari_3sc_ry:     0xFA0843,
    locationnames.csl1_yukari_3sc_ob:     0xFA0844,
    locationnames.csl2_yukari_3sc_ob:     0xFA0845,
    locationnames.csl3_yukari_3sc_ob:     0xFA0846,
    locationnames.csl4_yukari_3sc_ob:     0xFA0847,
    locationnames.csl1_yukari_3sc_nof:    0xFA0848,
    locationnames.csl2_yukari_3sc_nof:    0xFA0849,
    locationnames.csl3_yukari_3sc_nof:    0xFA084A,
    locationnames.csl4_yukari_3sc_nof:    0xFA084B,
    locationnames.csl1_yukari_4sc_cqb:    0xFA084C,
    locationnames.csl2_yukari_4sc_cqb:    0xFA084D,
    locationnames.csl3_yukari_4sc_cqb:    0xFA084E,
    locationnames.csl4_yukari_4sc_cqb:    0xFA084F,
    locationnames.csl1_yukari_4sc_tmeol:  0xFA0850,
    locationnames.csl2_yukari_4sc_tmeol:  0xFA0851,
    locationnames.csl3_yukari_4sc_tmeol:  0xFA0852,
    locationnames.csl4_yukari_4sc_tmeol:  0xFA0853,
    locationnames.csl1_yukari_5sc_tttos:  0xFA0854,
    locationnames.csl2_yukari_5sc_tttos:  0xFA0855,
    locationnames.csl3_yukari_5sc_tttos:  0xFA0856,
    locationnames.csl4_yukari_5sc_tttos:  0xFA0857,

}

suika_skill_loc_table = { #0xFA0900 - FA092F
    locationnames.cslk1_suika_236d:   0xFA0900,
    locationnames.cslk2_suika_236d:   0xFA0901,
    locationnames.cslk3_suika_236d:   0xFA0902,
    locationnames.cslk4_suika_236d:   0xFA0903,
    locationnames.cslk1_suika_236a1:  0xFA0904,
    locationnames.cslk2_suika_236a1:  0xFA0905,
    locationnames.cslk3_suika_236a1:  0xFA0906,
    locationnames.cslk4_suika_236a1:  0xFA0907,
    locationnames.cslk1_suika_236a2:  0xFA0908,
    locationnames.cslk2_suika_236a2:  0xFA0909,
    locationnames.cslk3_suika_236a2:  0xFA090A,
    locationnames.cslk4_suika_236a2:  0xFA090B,
    locationnames.cslk1_suika_623d:   0xFA090C,
    locationnames.cslk2_suika_623d:   0xFA090D,
    locationnames.cslk3_suika_623d:   0xFA090E,
    locationnames.cslk4_suika_623d:   0xFA090F,
    locationnames.cslk1_suika_623a1:  0xFA0910,
    locationnames.cslk2_suika_623a1:  0xFA0911,
    locationnames.cslk3_suika_623a1:  0xFA0912,
    locationnames.cslk4_suika_623a1:  0xFA0913,
    locationnames.cslk1_suika_623a2:  0xFA0914,
    locationnames.cslk2_suika_623a2:  0xFA0915,
    locationnames.cslk3_suika_623a2:  0xFA0916,
    locationnames.cslk4_suika_623a2:  0xFA0917,
    locationnames.cslk1_suika_214d:   0xFA0918,
    locationnames.cslk2_suika_214d:   0xFA0919,
    locationnames.cslk3_suika_214d:   0xFA091A,
    locationnames.cslk4_suika_214d:   0xFA091B,
    locationnames.cslk1_suika_214a1:  0xFA091C,
    locationnames.cslk2_suika_214a1:  0xFA091D,
    locationnames.cslk3_suika_214a1:  0xFA091E,
    locationnames.cslk4_suika_214a1:  0xFA091F,
    locationnames.cslk1_suika_214a2:  0xFA0920,
    locationnames.cslk2_suika_214a2:  0xFA0921,
    locationnames.cslk3_suika_214a2:  0xFA0922,
    locationnames.cslk4_suika_214a2:  0xFA0923,
    locationnames.cslk1_suika_22d:    0xFA0924,
    locationnames.cslk2_suika_22d:    0xFA0925,
    locationnames.cslk3_suika_22d:    0xFA0926,
    locationnames.cslk4_suika_22d:    0xFA0927,
    locationnames.cslk1_suika_22a1:   0xFA0928,
    locationnames.cslk2_suika_22a1:   0xFA0929,
    locationnames.cslk3_suika_22a1:   0xFA092A,
    locationnames.cslk4_suika_22a1:   0xFA092B,
    locationnames.cslk1_suika_22a2:   0xFA092C,
    locationnames.cslk2_suika_22a2:   0xFA092D,
    locationnames.cslk3_suika_22a2:   0xFA092E,
    locationnames.cslk4_suika_22a2:   0xFA092F,

}

suika_spell_loc_table = { #0xFA0930 - FA0957
    locationnames.csl1_suika_1sc_gad:   0xFA0930,
    locationnames.csl2_suika_1sc_gad:   0xFA0931,
    locationnames.csl3_suika_1sc_gad:   0xFA0932,
    locationnames.csl4_suika_1sc_gad:   0xFA0933,
    locationnames.csl1_suika_2sc_tmt:   0xFA0934,
    locationnames.csl2_suika_2sc_tmt:   0xFA0935,
    locationnames.csl3_suika_2sc_tmt:   0xFA0936,
    locationnames.csl4_suika_2sc_tmt:   0xFA0937,
    locationnames.csl1_suika_2sc_aoob:  0xFA0938,
    locationnames.csl2_suika_2sc_aoob:  0xFA0939,
    locationnames.csl3_suika_2sc_aoob:  0xFA093A,
    locationnames.csl4_suika_2sc_aoob:  0xFA093B,
    locationnames.csl1_suika_2sc_mp:    0xFA093C,
    locationnames.csl2_suika_2sc_mp:    0xFA093D,
    locationnames.csl3_suika_2sc_mp:    0xFA093E,
    locationnames.csl4_suika_2sc_mp:    0xFA093F,
    locationnames.csl1_suika_3sc_tsd:   0xFA0940,
    locationnames.csl2_suika_3sc_tsd:   0xFA0941,
    locationnames.csl3_suika_3sc_tsd:   0xFA0942,
    locationnames.csl4_suika_3sc_tsd:   0xFA0943,
    locationnames.csl1_suika_4sc_aogb:  0xFA0944,
    locationnames.csl2_suika_4sc_aogb:  0xFA0945,
    locationnames.csl3_suika_4sc_aogb:  0xFA0946,
    locationnames.csl4_suika_4sc_aogb:  0xFA0947,
    locationnames.csl1_suika_4sc_mpp:   0xFA0948,
    locationnames.csl2_suika_4sc_mpp:   0xFA0949,
    locationnames.csl3_suika_4sc_mpp:   0xFA094A,
    locationnames.csl4_suika_4sc_mpp:   0xFA094B,
    locationnames.csl1_suika_4sc_sc:    0xFA094C,
    locationnames.csl2_suika_4sc_sc:    0xFA094D,
    locationnames.csl3_suika_4sc_sc:    0xFA094E,
    locationnames.csl4_suika_4sc_sc:    0xFA094F,
    locationnames.csl1_suika_5sc_ta:    0xFA0950,
    locationnames.csl2_suika_5sc_ta:    0xFA0951,
    locationnames.csl3_suika_5sc_ta:    0xFA0952,
    locationnames.csl4_suika_5sc_ta:    0xFA0953,
    locationnames.csl1_suika_5sc_momo:  0xFA0954,
    locationnames.csl2_suika_5sc_momo:  0xFA0955,
    locationnames.csl3_suika_5sc_momo:  0xFA0956,
    locationnames.csl4_suika_5sc_momo:  0xFA0957,

}

reisen_skill_loc_table = { #0xFA0A00 - FA0A2F
    locationnames.cslk1_reisen_236d:   0xFA0A00,
    locationnames.cslk2_reisen_236d:   0xFA0A01,
    locationnames.cslk3_reisen_236d:   0xFA0A02,
    locationnames.cslk4_reisen_236d:   0xFA0A03,
    locationnames.cslk1_reisen_236a1:  0xFA0A04,
    locationnames.cslk2_reisen_236a1:  0xFA0A05,
    locationnames.cslk3_reisen_236a1:  0xFA0A06,
    locationnames.cslk4_reisen_236a1:  0xFA0A07,
    locationnames.cslk1_reisen_236a2:  0xFA0A08,
    locationnames.cslk2_reisen_236a2:  0xFA0A09,
    locationnames.cslk3_reisen_236a2:  0xFA0A0A,
    locationnames.cslk4_reisen_236a2:  0xFA0A0B,
    locationnames.cslk1_reisen_623d:   0xFA0A0C,
    locationnames.cslk2_reisen_623d:   0xFA0A0D,
    locationnames.cslk3_reisen_623d:   0xFA0A0E,
    locationnames.cslk4_reisen_623d:   0xFA0A0F,
    locationnames.cslk1_reisen_623a1:  0xFA0A10,
    locationnames.cslk2_reisen_623a1:  0xFA0A11,
    locationnames.cslk3_reisen_623a1:  0xFA0A12,
    locationnames.cslk4_reisen_623a1:  0xFA0A13,
    locationnames.cslk1_reisen_623a2:  0xFA0A14,
    locationnames.cslk2_reisen_623a2:  0xFA0A15,
    locationnames.cslk3_reisen_623a2:  0xFA0A16,
    locationnames.cslk4_reisen_623a2:  0xFA0A17,
    locationnames.cslk1_reisen_214d:   0xFA0A18,
    locationnames.cslk2_reisen_214d:   0xFA0A19,
    locationnames.cslk3_reisen_214d:   0xFA0A1A,
    locationnames.cslk4_reisen_214d:   0xFA0A1B,
    locationnames.cslk1_reisen_214a1:  0xFA0A1C,
    locationnames.cslk2_reisen_214a1:  0xFA0A1D,
    locationnames.cslk3_reisen_214a1:  0xFA0A1E,
    locationnames.cslk4_reisen_214a1:  0xFA0A1F,
    locationnames.cslk1_reisen_214a2:  0xFA0A20,
    locationnames.cslk2_reisen_214a2:  0xFA0A21,
    locationnames.cslk3_reisen_214a2:  0xFA0A22,
    locationnames.cslk4_reisen_214a2:  0xFA0A23,
    locationnames.cslk1_reisen_22d:    0xFA0A24,
    locationnames.cslk2_reisen_22d:    0xFA0A25,
    locationnames.cslk3_reisen_22d:    0xFA0A26,
    locationnames.cslk4_reisen_22d:    0xFA0A27,
    locationnames.cslk1_reisen_22a1:   0xFA0A28,
    locationnames.cslk2_reisen_22a1:   0xFA0A29,
    locationnames.cslk3_reisen_22a1:   0xFA0A2A,
    locationnames.cslk4_reisen_22a1:   0xFA0A2B,
    locationnames.cslk1_reisen_22a2:   0xFA0A2C,
    locationnames.cslk2_reisen_22a2:   0xFA0A2D,
    locationnames.cslk3_reisen_22a2:   0xFA0A2E,
    locationnames.cslk4_reisen_22a2:   0xFA0A2F

}

reisen_spell_loc_table = {
    locationnames.csl1_reisen_1sc_cv:   0xFA0A30,
    locationnames.csl2_reisen_1sc_cv:   0xFA0A31,
    locationnames.csl3_reisen_1sc_cv:   0xFA0A32,
    locationnames.csl4_reisen_1sc_cv:   0xFA0A33,
    locationnames.csl1_reisen_1sc_d:    0xFA0A34,
    locationnames.csl2_reisen_1sc_d:    0xFA0A35,
    locationnames.csl3_reisen_1sc_d:    0xFA0A36,
    locationnames.csl4_reisen_1sc_d:    0xFA0A37,
    locationnames.csl1_reisen_2sc_gwo:  0xFA0A38,
    locationnames.csl2_reisen_2sc_gwo:  0xFA0A39,
    locationnames.csl3_reisen_2sc_gwo:  0xFA0A3A,
    locationnames.csl4_reisen_2sc_gwo:  0xFA0A3B,
    locationnames.csl1_reisen_2sc_im:   0xFA0A3C,
    locationnames.csl2_reisen_2sc_im:   0xFA0A3D,
    locationnames.csl3_reisen_2sc_im:   0xFA0A3E,
    locationnames.csl4_reisen_2sc_im:   0xFA0A3F,
    locationnames.csl1_reisen_3sc_ms:   0xFA0A40,
    locationnames.csl2_reisen_3sc_ms:   0xFA0A41,
    locationnames.csl3_reisen_3sc_ms:   0xFA0A42,
    locationnames.csl4_reisen_3sc_ms:   0xFA0A43,
    locationnames.csl1_reisen_3sc_cw:   0xFA0A44,
    locationnames.csl2_reisen_3sc_cw:   0xFA0A45,
    locationnames.csl3_reisen_3sc_cw:   0xFA0A46,
    locationnames.csl4_reisen_3sc_cw:   0xFA0A47,
    locationnames.csl1_reisen_3sc_d:    0xFA0A48,
    locationnames.csl2_reisen_3sc_d:    0xFA0A49,
    locationnames.csl3_reisen_3sc_d:    0xFA0A4A,
    locationnames.csl4_reisen_3sc_d:    0xFA0A4B,
    locationnames.csl1_reisen_3sc_gpe:  0xFA0A4C,
    locationnames.csl2_reisen_3sc_gpe:  0xFA0A4D,
    locationnames.csl3_reisen_3sc_gpe:  0xFA0A4E,
    locationnames.csl4_reisen_3sc_gpe:  0xFA0A4F,
    locationnames.csl1_reisen_3sc_xw:   0xFA0A50,
    locationnames.csl2_reisen_3sc_xw:   0xFA0A51,
    locationnames.csl3_reisen_3sc_xw:   0xFA0A52,
    locationnames.csl4_reisen_3sc_xw:   0xFA0A53,
    locationnames.csl1_reisen_4sc_lb:   0xFA0A54,
    locationnames.csl2_reisen_4sc_lb:   0xFA0A55,
    locationnames.csl3_reisen_4sc_lb:   0xFA0A56,
    locationnames.csl4_reisen_4sc_lb:   0xFA0A57,
    locationnames.csl1_reisen_5sc_lre:  0xFA0A58,
    locationnames.csl2_reisen_5sc_lre:  0xFA0A59,
    locationnames.csl3_reisen_5sc_lre:  0xFA0A5A,
    locationnames.csl4_reisen_5sc_lre:  0xFA0A5B

}

aya_skill_loc_table = { #0xFA0B00 - FA0B2F
    locationnames.cslk1_aya_236d:   0xFA0B00,
    locationnames.cslk2_aya_236d:   0xFA0B01,
    locationnames.cslk3_aya_236d:   0xFA0B02,
    locationnames.cslk4_aya_236d:   0xFA0B03,
    locationnames.cslk1_aya_236a1:  0xFA0B04,
    locationnames.cslk2_aya_236a1:  0xFA0B05,
    locationnames.cslk3_aya_236a1:  0xFA0B06,
    locationnames.cslk4_aya_236a1:  0xFA0B07,
    locationnames.cslk1_aya_236a2:  0xFA0B08,
    locationnames.cslk2_aya_236a2:  0xFA0B09,
    locationnames.cslk3_aya_236a2:  0xFA0B0A,
    locationnames.cslk4_aya_236a2:  0xFA0B0B,
    locationnames.cslk1_aya_214d:   0xFA0B0C,
    locationnames.cslk2_aya_214d:   0xFA0B0D,
    locationnames.cslk3_aya_214d:   0xFA0B0E,
    locationnames.cslk4_aya_214d:   0xFA0B0F,
    locationnames.cslk1_aya_214a1:  0xFA0B10,
    locationnames.cslk2_aya_214a1:  0xFA0B11,
    locationnames.cslk3_aya_214a1:  0xFA0B12,
    locationnames.cslk4_aya_214a1:  0xFA0B13,
    locationnames.cslk1_aya_214a2:  0xFA0B14,
    locationnames.cslk2_aya_214a2:  0xFA0B15,
    locationnames.cslk3_aya_214a2:  0xFA0B16,
    locationnames.cslk4_aya_214a2:  0xFA0B17,
    locationnames.cslk1_aya_421d:   0xFA0B18,
    locationnames.cslk2_aya_421d:   0xFA0B19,
    locationnames.cslk3_aya_421d:   0xFA0B1A,
    locationnames.cslk4_aya_421d:   0xFA0B1B,
    locationnames.cslk1_aya_421a1:  0xFA0B1C,
    locationnames.cslk2_aya_421a1:  0xFA0B1D,
    locationnames.cslk3_aya_421a1:  0xFA0B1E,
    locationnames.cslk4_aya_421a1:  0xFA0B1F,
    locationnames.cslk1_aya_421a2:  0xFA0B20,
    locationnames.cslk2_aya_421a2:  0xFA0B21,
    locationnames.cslk3_aya_421a2:  0xFA0B22,
    locationnames.cslk4_aya_421a2:  0xFA0B23,
    locationnames.cslk1_aya_22d:    0xFA0B24,
    locationnames.cslk2_aya_22d:    0xFA0B25,
    locationnames.cslk3_aya_22d:    0xFA0B26,
    locationnames.cslk4_aya_22d:    0xFA0B27,
    locationnames.cslk1_aya_22a1:   0xFA0B28,
    locationnames.cslk2_aya_22a1:   0xFA0B29,
    locationnames.cslk3_aya_22a1:   0xFA0B2A,
    locationnames.cslk4_aya_22a1:   0xFA0B2B,
    locationnames.cslk1_aya_22a2:   0xFA0B2C,
    locationnames.cslk2_aya_22a2:   0xFA0B2D,
    locationnames.cslk3_aya_22a2:   0xFA0B2E,
    locationnames.cslk4_aya_22a2:   0xFA0B2F

}

aya_spell_loc_table = { #FA0B30 - FA0B57
    locationnames.csl1_aya_1sc_swv:    0xFA0B30,
    locationnames.csl2_aya_1sc_swv:    0xFA0B31,
    locationnames.csl3_aya_1sc_swv:    0xFA0B32,
    locationnames.csl4_aya_1sc_swv:    0xFA0B33,
    locationnames.csl1_aya_2sc_wottp:  0xFA0B34,
    locationnames.csl2_aya_2sc_wottp:  0xFA0B35,
    locationnames.csl3_aya_2sc_wottp:  0xFA0B36,
    locationnames.csl4_aya_2sc_wottp:  0xFA0B37,
    locationnames.csl1_aya_2sc_tls:    0xFA0B38,
    locationnames.csl2_aya_2sc_tls:    0xFA0B39,
    locationnames.csl3_aya_2sc_tls:    0xFA0B3A,
    locationnames.csl4_aya_2sc_tls:    0xFA0B3B,
    locationnames.csl1_aya_3sc_mlf:    0xFA0B3C,
    locationnames.csl2_aya_3sc_mlf:    0xFA0B3D,
    locationnames.csl3_aya_3sc_mlf:    0xFA0B3E,
    locationnames.csl4_aya_3sc_mlf:    0xFA0B3F,
    locationnames.csl1_aya_3sc_tm:     0xFA0B40,
    locationnames.csl2_aya_3sc_tm:     0xFA0B41,
    locationnames.csl3_aya_3sc_tm:     0xFA0B42,
    locationnames.csl4_aya_3sc_tm:     0xFA0B43,
    locationnames.csl1_aya_3sc_sg:     0xFA0B44,
    locationnames.csl2_aya_3sc_sg:     0xFA0B45,
    locationnames.csl3_aya_3sc_sg:     0xFA0B46,
    locationnames.csl4_aya_3sc_sg:     0xFA0B47,
    locationnames.csl1_aya_4sc_rftm:   0xFA0B48,
    locationnames.csl2_aya_4sc_rftm:   0xFA0B49,
    locationnames.csl3_aya_4sc_rftm:   0xFA0B4A,
    locationnames.csl4_aya_4sc_rftm:   0xFA0B4B,
    locationnames.csl1_aya_4sc_dd:     0xFA0B4C,
    locationnames.csl2_aya_4sc_dd:     0xFA0B4D,
    locationnames.csl3_aya_4sc_dd:     0xFA0B4E,
    locationnames.csl4_aya_4sc_dd:     0xFA0B4F,
    locationnames.csl1_aya_5sc_ittd:   0xFA0B50,
    locationnames.csl2_aya_5sc_ittd:   0xFA0B51,
    locationnames.csl3_aya_5sc_ittd:   0xFA0B52,
    locationnames.csl4_aya_5sc_ittd:   0xFA0B53,
    locationnames.csl1_aya_5sc_id:     0xFA0B54,
    locationnames.csl2_aya_5sc_id:     0xFA0B55,
    locationnames.csl3_aya_5sc_id:     0xFA0B56,
    locationnames.csl4_aya_5sc_id:     0xFA0B57,

}

komachi_skill_loc_table = { #0xFA0C00 - FA0C2F
    locationnames.cslk1_komachi_236d:   0xFA0C00,
    locationnames.cslk2_komachi_236d:   0xFA0C01,
    locationnames.cslk3_komachi_236d:   0xFA0C02,
    locationnames.cslk4_komachi_236d:   0xFA0C03,
    locationnames.cslk1_komachi_236a1:  0xFA0C04,
    locationnames.cslk2_komachi_236a1:  0xFA0C05,
    locationnames.cslk3_komachi_236a1:  0xFA0C06,
    locationnames.cslk4_komachi_236a1:  0xFA0C07,
    locationnames.cslk1_komachi_236a2:  0xFA0C08,
    locationnames.cslk2_komachi_236a2:  0xFA0C09,
    locationnames.cslk3_komachi_236a2:  0xFA0C0A,
    locationnames.cslk4_komachi_236a2:  0xFA0C0B,
    locationnames.cslk1_komachi_623d:   0xFA0C0C,
    locationnames.cslk2_komachi_623d:   0xFA0C0D,
    locationnames.cslk3_komachi_623d:   0xFA0C0E,
    locationnames.cslk4_komachi_623d:   0xFA0C0F,
    locationnames.cslk1_komachi_623a1:  0xFA0C10,
    locationnames.cslk2_komachi_623a1:  0xFA0C11,
    locationnames.cslk3_komachi_623a1:  0xFA0C12,
    locationnames.cslk4_komachi_623a1:  0xFA0C13,
    locationnames.cslk1_komachi_623a2:  0xFA0C14,
    locationnames.cslk2_komachi_623a2:  0xFA0C15,
    locationnames.cslk3_komachi_623a2:  0xFA0C16,
    locationnames.cslk4_komachi_623a2:  0xFA0C17,
    locationnames.cslk1_komachi_214d:   0xFA0C18,
    locationnames.cslk2_komachi_214d:   0xFA0C19,
    locationnames.cslk3_komachi_214d:   0xFA0C1A,
    locationnames.cslk4_komachi_214d:   0xFA0C1B,
    locationnames.cslk1_komachi_214a1:  0xFA0C1C,
    locationnames.cslk2_komachi_214a1:  0xFA0C1D,
    locationnames.cslk3_komachi_214a1:  0xFA0C1E,
    locationnames.cslk4_komachi_214a1:  0xFA0C1F,
    locationnames.cslk1_komachi_214a2:  0xFA0C20,
    locationnames.cslk2_komachi_214a2:  0xFA0C21,
    locationnames.cslk3_komachi_214a2:  0xFA0C22,
    locationnames.cslk4_komachi_214a2:  0xFA0C23,
    locationnames.cslk1_komachi_22d:    0xFA0C24,
    locationnames.cslk2_komachi_22d:    0xFA0C25,
    locationnames.cslk3_komachi_22d:    0xFA0C26,
    locationnames.cslk4_komachi_22d:    0xFA0C27,
    locationnames.cslk1_komachi_22a1:   0xFA0C28,
    locationnames.cslk2_komachi_22a1:   0xFA0C29,
    locationnames.cslk3_komachi_22a1:   0xFA0C2A,
    locationnames.cslk4_komachi_22a1:   0xFA0C2B,
    locationnames.cslk1_komachi_22a2:   0xFA0C2C,
    locationnames.cslk2_komachi_22a2:   0xFA0C2D,
    locationnames.cslk3_komachi_22a2:   0xFA0C2E,
    locationnames.cslk4_komachi_22a2:   0xFA0C2F

}

komachi_spell_loc_table = { #0xFA0C30 - FA0C53
    locationnames.csl1_komachi_1sc_fotr:   0xFA0C30,
    locationnames.csl2_komachi_1sc_fotr:   0xFA0C31,
    locationnames.csl3_komachi_1sc_fotr:   0xFA0C32,
    locationnames.csl4_komachi_1sc_fotr:   0xFA0C33,
    locationnames.csl1_komachi_1sc_afs:    0xFA0C34,
    locationnames.csl2_komachi_1sc_afs:    0xFA0C35,
    locationnames.csl3_komachi_1sc_afs:    0xFA0C36,
    locationnames.csl4_komachi_1sc_afs:    0xFA0C37,
    locationnames.csl1_komachi_3sc_fitdf:  0xFA0C38,
    locationnames.csl2_komachi_3sc_fitdf:  0xFA0C39,
    locationnames.csl3_komachi_3sc_fitdf:  0xFA0C3A,
    locationnames.csl4_komachi_3sc_fitdf:  0xFA0C3B,
    locationnames.csl1_komachi_3sc_ibs:    0xFA0C3C,
    locationnames.csl2_komachi_3sc_ibs:    0xFA0C3D,
    locationnames.csl3_komachi_3sc_ibs:    0xFA0C3E,
    locationnames.csl4_komachi_3sc_ibs:    0xFA0C3F,
    locationnames.csl1_komachi_3sc_hcoa:   0xFA0C40,
    locationnames.csl2_komachi_3sc_hcoa:   0xFA0C41,
    locationnames.csl3_komachi_3sc_hcoa:   0xFA0C42,
    locationnames.csl4_komachi_3sc_hcoa:   0xFA0C43,
    locationnames.csl1_komachi_4sc_sofj:   0xFA0C44,
    locationnames.csl2_komachi_4sc_sofj:   0xFA0C45,
    locationnames.csl3_komachi_4sc_sofj:   0xFA0C46,
    locationnames.csl4_komachi_4sc_sofj:   0xFA0C47,
    locationnames.csl1_komachi_4sc_sows:   0xFA0C48,
    locationnames.csl2_komachi_4sc_sows:   0xFA0C49,
    locationnames.csl3_komachi_4sc_sows:   0xFA0C4A,
    locationnames.csl4_komachi_4sc_sows:   0xFA0C4B,
    locationnames.csl1_komachi_5sc_sle:    0xFA0C4C,
    locationnames.csl2_komachi_5sc_sle:    0xFA0C4D,
    locationnames.csl3_komachi_5sc_sle:    0xFA0C4E,
    locationnames.csl4_komachi_5sc_sle:    0xFA0C4F,
    locationnames.csl1_komachi_5sc_upl:    0xFA0C50,
    locationnames.csl2_komachi_5sc_upl:    0xFA0C51,
    locationnames.csl3_komachi_5sc_upl:    0xFA0C52,
    locationnames.csl4_komachi_5sc_upl:    0xFA0C53,

}

iku_skill_loc_table = { #0xFA0D00 - FA0D2F
    locationnames.cslk1_iku_236d:   0xFA0D00,
    locationnames.cslk2_iku_236d:   0xFA0D01,
    locationnames.cslk3_iku_236d:   0xFA0D02,
    locationnames.cslk4_iku_236d:   0xFA0D03,
    locationnames.cslk1_iku_236a1:  0xFA0D04,
    locationnames.cslk2_iku_236a1:  0xFA0D05,
    locationnames.cslk3_iku_236a1:  0xFA0D06,
    locationnames.cslk4_iku_236a1:  0xFA0D07,
    locationnames.cslk1_iku_236a2:  0xFA0D08,
    locationnames.cslk2_iku_236a2:  0xFA0D09,
    locationnames.cslk3_iku_236a2:  0xFA0D0A,
    locationnames.cslk4_iku_236a2:  0xFA0D0B,
    locationnames.cslk1_iku_623d:   0xFA0D0C,
    locationnames.cslk2_iku_623d:   0xFA0D0D,
    locationnames.cslk3_iku_623d:   0xFA0D0E,
    locationnames.cslk4_iku_623d:   0xFA0D0F,
    locationnames.cslk1_iku_623a1:  0xFA0D10,
    locationnames.cslk2_iku_623a1:  0xFA0D11,
    locationnames.cslk3_iku_623a1:  0xFA0D12,
    locationnames.cslk4_iku_623a1:  0xFA0D13,
    locationnames.cslk1_iku_623a2:  0xFA0D14,
    locationnames.cslk2_iku_623a2:  0xFA0D15,
    locationnames.cslk3_iku_623a2:  0xFA0D16,
    locationnames.cslk4_iku_623a2:  0xFA0D17,
    locationnames.cslk1_iku_214d:   0xFA0D18,
    locationnames.cslk2_iku_214d:   0xFA0D19,
    locationnames.cslk3_iku_214d:   0xFA0D1A,
    locationnames.cslk4_iku_214d:   0xFA0D1B,
    locationnames.cslk1_iku_214a1:  0xFA0D1C,
    locationnames.cslk2_iku_214a1:  0xFA0D1D,
    locationnames.cslk3_iku_214a1:  0xFA0D1E,
    locationnames.cslk4_iku_214a1:  0xFA0D1F,
    locationnames.cslk1_iku_214a2:  0xFA0D20,
    locationnames.cslk2_iku_214a2:  0xFA0D21,
    locationnames.cslk3_iku_214a2:  0xFA0D22,
    locationnames.cslk4_iku_214a2:  0xFA0D23,
    locationnames.cslk1_iku_22d:    0xFA0D24,
    locationnames.cslk2_iku_22d:    0xFA0D25,
    locationnames.cslk3_iku_22d:    0xFA0D26,
    locationnames.cslk4_iku_22d:    0xFA0D27,
    locationnames.cslk1_iku_22a1:   0xFA0D28,
    locationnames.cslk2_iku_22a1:   0xFA0D29,
    locationnames.cslk3_iku_22a1:   0xFA0D2A,
    locationnames.cslk4_iku_22a1:   0xFA0D2B,
    locationnames.cslk1_iku_22a2:   0xFA0D2C,
    locationnames.cslk2_iku_22a2:   0xFA0D2D,
    locationnames.cslk3_iku_22a2:   0xFA0D2E,
    locationnames.cslk4_iku_22a2:   0xFA0D2F,

}

iku_spell_loc_table = { #0xFA0D30 - FA0D57
    locationnames.csl1_iku_1sc_tds:     0xFA0D30,
    locationnames.csl2_iku_1sc_tds:     0xFA0D31,
    locationnames.csl3_iku_1sc_tds:     0xFA0D32,
    locationnames.csl4_iku_1sc_tds:     0xFA0D33,
    locationnames.csl1_iku_1sc_vlt:     0xFA0D34,
    locationnames.csl2_iku_1sc_vlt:     0xFA0D35,
    locationnames.csl3_iku_1sc_vlt:     0xFA0D36,
    locationnames.csl4_iku_1sc_vlt:     0xFA0D37,
    locationnames.csl1_iku_2sc_sts:     0xFA0D38,
    locationnames.csl2_iku_2sc_sts:     0xFA0D39,
    locationnames.csl3_iku_2sc_sts:     0xFA0D3A,
    locationnames.csl4_iku_2sc_sts:     0xFA0D3B,
    locationnames.csl1_iku_3sc_dd:      0xFA0D3C,
    locationnames.csl2_iku_3sc_dd:      0xFA0D3D,
    locationnames.csl3_iku_3sc_dd:      0xFA0D3E,
    locationnames.csl4_iku_3sc_dd:      0xFA0D3F,
    locationnames.csl1_iku_3sc_edp:     0xFA0D40,
    locationnames.csl2_iku_3sc_edp:     0xFA0D41,
    locationnames.csl3_iku_3sc_edp:     0xFA0D42,
    locationnames.csl4_iku_3sc_edp:     0xFA0D43,
    locationnames.csl1_iku_3sc_lds:     0xFA0D44,
    locationnames.csl2_iku_3sc_lds:     0xFA0D45,
    locationnames.csl3_iku_3sc_lds:     0xFA0D46,
    locationnames.csl4_iku_3sc_lds:     0xFA0D47,
    locationnames.csl1_iku_3sc_ts:      0xFA0D48,
    locationnames.csl2_iku_3sc_ts:      0xFA0D49,
    locationnames.csl3_iku_3sc_ts:      0xFA0D4A,
    locationnames.csl4_iku_3sc_ts:      0xFA0D4B,
    locationnames.csl1_iku_4sc_vls:     0xFA0D4C,
    locationnames.csl2_iku_4sc_vls:     0xFA0D4D,
    locationnames.csl3_iku_4sc_vls:     0xFA0D4E,
    locationnames.csl4_iku_4sc_vls:     0xFA0D4F,
    locationnames.csl1_iku_4sc_ootfcd:  0xFA0D50,
    locationnames.csl2_iku_4sc_ootfcd:  0xFA0D51,
    locationnames.csl3_iku_4sc_ootfcd:  0xFA0D52,
    locationnames.csl4_iku_4sc_ootfcd:  0xFA0D53,
    locationnames.csl1_iku_5sc_sos:     0xFA0D54,
    locationnames.csl2_iku_5sc_sos:     0xFA0D55,
    locationnames.csl3_iku_5sc_sos:     0xFA0D56,
    locationnames.csl4_iku_5sc_sos:     0xFA0D57

}

tenshi_skill_loc_table = { #0xFA0E00 - FA0E2F
    locationnames.cslk1_tenshi_236d:   0xFA0E00,
    locationnames.cslk2_tenshi_236d:   0xFA0E01,
    locationnames.cslk3_tenshi_236d:   0xFA0E02,
    locationnames.cslk4_tenshi_236d:   0xFA0E03,
    locationnames.cslk1_tenshi_236a1:  0xFA0E04,
    locationnames.cslk2_tenshi_236a1:  0xFA0E05,
    locationnames.cslk3_tenshi_236a1:  0xFA0E06,
    locationnames.cslk4_tenshi_236a1:  0xFA0E07,
    locationnames.cslk1_tenshi_236a2:  0xFA0E08,
    locationnames.cslk2_tenshi_236a2:  0xFA0E09,
    locationnames.cslk3_tenshi_236a2:  0xFA0E0A,
    locationnames.cslk4_tenshi_236a2:  0xFA0E0B,
    locationnames.cslk1_tenshi_623d:   0xFA0E0C,
    locationnames.cslk2_tenshi_623d:   0xFA0E0D,
    locationnames.cslk3_tenshi_623d:   0xFA0E0E,
    locationnames.cslk4_tenshi_623d:   0xFA0E0F,
    locationnames.cslk1_tenshi_623a1:  0xFA0E10,
    locationnames.cslk2_tenshi_623a1:  0xFA0E11,
    locationnames.cslk3_tenshi_623a1:  0xFA0E12,
    locationnames.cslk4_tenshi_623a1:  0xFA0E13,
    locationnames.cslk1_tenshi_623a2:  0xFA0E14,
    locationnames.cslk2_tenshi_623a2:  0xFA0E15,
    locationnames.cslk3_tenshi_623a2:  0xFA0E16,
    locationnames.cslk4_tenshi_623a2:  0xFA0E17,
    locationnames.cslk1_tenshi_214d:   0xFA0E18,
    locationnames.cslk2_tenshi_214d:   0xFA0E19,
    locationnames.cslk3_tenshi_214d:   0xFA0E1A,
    locationnames.cslk4_tenshi_214d:   0xFA0E1B,
    locationnames.cslk1_tenshi_214a1:  0xFA0E1C,
    locationnames.cslk2_tenshi_214a1:  0xFA0E1D,
    locationnames.cslk3_tenshi_214a1:  0xFA0E1E,
    locationnames.cslk4_tenshi_214a1:  0xFA0E1F,
    locationnames.cslk1_tenshi_214a2:  0xFA0E20,
    locationnames.cslk2_tenshi_214a2:  0xFA0E21,
    locationnames.cslk3_tenshi_214a2:  0xFA0E22,
    locationnames.cslk4_tenshi_214a2:  0xFA0E23,
    locationnames.cslk1_tenshi_22d:    0xFA0E24,
    locationnames.cslk2_tenshi_22d:    0xFA0E25,
    locationnames.cslk3_tenshi_22d:    0xFA0E26,
    locationnames.cslk4_tenshi_22d:    0xFA0E27,
    locationnames.cslk1_tenshi_22a1:   0xFA0E28,
    locationnames.cslk2_tenshi_22a1:   0xFA0E29,
    locationnames.cslk3_tenshi_22a1:   0xFA0E2A,
    locationnames.cslk4_tenshi_22a1:   0xFA0E2B,
    locationnames.cslk1_tenshi_22a2:   0xFA0E2C,
    locationnames.cslk2_tenshi_22a2:   0xFA0E2D,
    locationnames.cslk3_tenshi_22a2:   0xFA0E2E,
    locationnames.cslk4_tenshi_22a2:   0xFA0E2F,

}

tenshi_spell_loc_table = { #0xFA0E30 - FA0E57
    locationnames.csl1_tenshi_2sc_sous:   0xFA0E30,
    locationnames.csl2_tenshi_2sc_sous:   0xFA0E31,
    locationnames.csl3_tenshi_2sc_sous:   0xFA0E32,
    locationnames.csl4_tenshi_2sc_sous:   0xFA0E33,
    locationnames.csl1_tenshi_2sc_sor:    0xFA0E34,
    locationnames.csl2_tenshi_2sc_sor:    0xFA0E35,
    locationnames.csl3_tenshi_2sc_sor:    0xFA0E36,
    locationnames.csl4_tenshi_2sc_sor:    0xFA0E37,
    locationnames.csl1_tenshi_3sc_sodj:   0xFA0E38,
    locationnames.csl2_tenshi_3sc_sodj:   0xFA0E39,
    locationnames.csl3_tenshi_3sc_sodj:   0xFA0E3A,
    locationnames.csl4_tenshi_3sc_sodj:   0xFA0E3B,
    locationnames.csl1_tenshi_3sc_sos:    0xFA0E3C,
    locationnames.csl2_tenshi_3sc_sos:    0xFA0E3D,
    locationnames.csl3_tenshi_3sc_sos:    0xFA0E3E,
    locationnames.csl4_tenshi_3sc_sos:    0xFA0E3F,
    locationnames.csl1_tenshi_3sc_swp:    0xFA0E40,
    locationnames.csl2_tenshi_3sc_swp:    0xFA0E41,
    locationnames.csl3_tenshi_3sc_swp:    0xFA0E42,
    locationnames.csl4_tenshi_3sc_swp:    0xFA0E43,
    locationnames.csl1_tenshi_4sc_mr:     0xFA0E44,
    locationnames.csl2_tenshi_4sc_mr:     0xFA0E45,
    locationnames.csl3_tenshi_4sc_mr:     0xFA0E46,
    locationnames.csl4_tenshi_4sc_mr:     0xFA0E47,
    locationnames.csl1_tenshi_4sc_soe:    0xFA0E48,
    locationnames.csl2_tenshi_4sc_soe:    0xFA0E49,
    locationnames.csl3_tenshi_4sc_soe:    0xFA0E4A,
    locationnames.csl4_tenshi_4sc_soe:    0xFA0E4B,
    locationnames.csl1_tenshi_5sc_sowaj:  0xFA0E4C,
    locationnames.csl2_tenshi_5sc_sowaj:  0xFA0E4D,
    locationnames.csl3_tenshi_5sc_sowaj:  0xFA0E4E,
    locationnames.csl4_tenshi_5sc_sowaj:  0xFA0E4F,
    locationnames.csl1_tenshi_5sc_wcp:    0xFA0E50,
    locationnames.csl2_tenshi_5sc_wcp:    0xFA0E51,
    locationnames.csl3_tenshi_5sc_wcp:    0xFA0E52,
    locationnames.csl4_tenshi_5sc_wcp:    0xFA0E53,
    locationnames.csl1_tenshi_5sc_swr:    0xFA0E54,
    locationnames.csl2_tenshi_5sc_swr:    0xFA0E55,
    locationnames.csl3_tenshi_5sc_swr:    0xFA0E56,
    locationnames.csl4_tenshi_5sc_swr:    0xFA0E57,

}

sanae_skill_loc_table = { #0xFA0F00 - FA0F2F
    locationnames.cslk1_sanae_236d:   0xFA0F00,
    locationnames.cslk2_sanae_236d:   0xFA0F01,
    locationnames.cslk3_sanae_236d:   0xFA0F02,
    locationnames.cslk4_sanae_236d:   0xFA0F03,
    locationnames.cslk1_sanae_236a1:  0xFA0F04,
    locationnames.cslk2_sanae_236a1:  0xFA0F05,
    locationnames.cslk3_sanae_236a1:  0xFA0F06,
    locationnames.cslk4_sanae_236a1:  0xFA0F07,
    locationnames.cslk1_sanae_236a2:  0xFA0F08,
    locationnames.cslk2_sanae_236a2:  0xFA0F09,
    locationnames.cslk3_sanae_236a2:  0xFA0F0A,
    locationnames.cslk4_sanae_236a2:  0xFA0F0B,
    locationnames.cslk1_sanae_623d:   0xFA0F0C,
    locationnames.cslk2_sanae_623d:   0xFA0F0D,
    locationnames.cslk3_sanae_623d:   0xFA0F0E,
    locationnames.cslk4_sanae_623d:   0xFA0F0F,
    locationnames.cslk1_sanae_623a1:  0xFA0F10,
    locationnames.cslk2_sanae_623a1:  0xFA0F11,
    locationnames.cslk3_sanae_623a1:  0xFA0F12,
    locationnames.cslk4_sanae_623a1:  0xFA0F13,
    locationnames.cslk1_sanae_623a2:  0xFA0F14,
    locationnames.cslk2_sanae_623a2:  0xFA0F15,
    locationnames.cslk3_sanae_623a2:  0xFA0F16,
    locationnames.cslk4_sanae_623a2:  0xFA0F17,
    locationnames.cslk1_sanae_214d:   0xFA0F18,
    locationnames.cslk2_sanae_214d:   0xFA0F19,
    locationnames.cslk3_sanae_214d:   0xFA0F1A,
    locationnames.cslk4_sanae_214d:   0xFA0F1B,
    locationnames.cslk1_sanae_214a1:  0xFA0F1C,
    locationnames.cslk2_sanae_214a1:  0xFA0F1D,
    locationnames.cslk3_sanae_214a1:  0xFA0F1E,
    locationnames.cslk4_sanae_214a1:  0xFA0F1F,
    locationnames.cslk1_sanae_214a2:  0xFA0F20,
    locationnames.cslk2_sanae_214a2:  0xFA0F21,
    locationnames.cslk3_sanae_214a2:  0xFA0F22,
    locationnames.cslk4_sanae_214a2:  0xFA0F23,
    locationnames.cslk1_sanae_22d:    0xFA0F24,
    locationnames.cslk2_sanae_22d:    0xFA0F25,
    locationnames.cslk3_sanae_22d:    0xFA0F26,
    locationnames.cslk4_sanae_22d:    0xFA0F27,
    locationnames.cslk1_sanae_22a1:   0xFA0F28,
    locationnames.cslk2_sanae_22a1:   0xFA0F29,
    locationnames.cslk3_sanae_22a1:   0xFA0F2A,
    locationnames.cslk4_sanae_22a1:   0xFA0F2B,
    locationnames.cslk1_sanae_22a2:   0xFA0F2C,
    locationnames.cslk2_sanae_22a2:   0xFA0F2D,
    locationnames.cslk3_sanae_22a2:   0xFA0F2E,
    locationnames.cslk4_sanae_22a2:   0xFA0F2F,

}

sanae_spell_loc_table = { #0xFA0F30 - FA0F53
    locationnames.csl1_sanae_2sc_cogc:   0xFA0F30,
    locationnames.csl2_sanae_2sc_cogc:   0xFA0F31,
    locationnames.csl3_sanae_2sc_cogc:   0xFA0F32,
    locationnames.csl4_sanae_2sc_cogc:   0xFA0F33,
    locationnames.csl1_sanae_2sc_gt:     0xFA0F34,
    locationnames.csl2_sanae_2sc_gt:     0xFA0F35,
    locationnames.csl3_sanae_2sc_gt:     0xFA0F36,
    locationnames.csl4_sanae_2sc_gt:     0xFA0F37,
    locationnames.csl1_sanae_2sc_rob:    0xFA0F38,
    locationnames.csl2_sanae_2sc_rob:    0xFA0F39,
    locationnames.csl3_sanae_2sc_rob:    0xFA0F3A,
    locationnames.csl4_sanae_2sc_rob:    0xFA0F3B,
    locationnames.csl1_sanae_3sc_tdtss:  0xFA0F3C,
    locationnames.csl2_sanae_3sc_tdtss:  0xFA0F3D,
    locationnames.csl3_sanae_3sc_tdtss:  0xFA0F3E,
    locationnames.csl4_sanae_3sc_tdtss:  0xFA0F3F,
    locationnames.csl1_sanae_3sc_mds:    0xFA0F40,
    locationnames.csl2_sanae_3sc_mds:    0xFA0F41,
    locationnames.csl3_sanae_3sc_mds:    0xFA0F42,
    locationnames.csl4_sanae_3sc_mds:    0xFA0F43,
    locationnames.csl1_sanae_4sc_fr:     0xFA0F44,
    locationnames.csl2_sanae_4sc_fr:     0xFA0F45,
    locationnames.csl3_sanae_4sc_fr:     0xFA0F46,
    locationnames.csl4_sanae_4sc_fr:     0xFA0F47,
    locationnames.csl1_sanae_4sc_notss:  0xFA0F48,
    locationnames.csl2_sanae_4sc_notss:  0xFA0F49,
    locationnames.csl3_sanae_4sc_notss:  0xFA0F4A,
    locationnames.csl4_sanae_4sc_notss:  0xFA0F4B,
    locationnames.csl1_sanae_5sc_mm:     0xFA0F4C,
    locationnames.csl2_sanae_5sc_mm:     0xFA0F4D,
    locationnames.csl3_sanae_5sc_mm:     0xFA0F4E,
    locationnames.csl4_sanae_5sc_mm:     0xFA0F4F,
    locationnames.csl1_sanae_5sc_ncp:    0xFA0F50,
    locationnames.csl2_sanae_5sc_ncp:    0xFA0F51,
    locationnames.csl3_sanae_5sc_ncp:    0xFA0F52,
    locationnames.csl4_sanae_5sc_ncp:    0xFA0F53,

}

cirno_skill_loc_table = { #0xFA1000 - FA102F
    locationnames.cslk1_cirno_236d:   0xFA1000,
    locationnames.cslk2_cirno_236d:   0xFA1001,
    locationnames.cslk3_cirno_236d:   0xFA1002,
    locationnames.cslk4_cirno_236d:   0xFA1003,
    locationnames.cslk1_cirno_236a1:  0xFA1004,
    locationnames.cslk2_cirno_236a1:  0xFA1005,
    locationnames.cslk3_cirno_236a1:  0xFA1006,
    locationnames.cslk4_cirno_236a1:  0xFA1007,
    locationnames.cslk1_cirno_236a2:  0xFA1008,
    locationnames.cslk2_cirno_236a2:  0xFA1009,
    locationnames.cslk3_cirno_236a2:  0xFA100A,
    locationnames.cslk4_cirno_236a2:  0xFA100B,
    locationnames.cslk1_cirno_623d:   0xFA100C,
    locationnames.cslk2_cirno_623d:   0xFA100D,
    locationnames.cslk3_cirno_623d:   0xFA100E,
    locationnames.cslk4_cirno_623d:   0xFA100F,
    locationnames.cslk1_cirno_623a1:  0xFA1010,
    locationnames.cslk2_cirno_623a1:  0xFA1011,
    locationnames.cslk3_cirno_623a1:  0xFA1012,
    locationnames.cslk4_cirno_623a1:  0xFA1013,
    locationnames.cslk1_cirno_623a2:  0xFA1014,
    locationnames.cslk2_cirno_623a2:  0xFA1015,
    locationnames.cslk3_cirno_623a2:  0xFA1016,
    locationnames.cslk4_cirno_623a2:  0xFA1017,
    locationnames.cslk1_cirno_214d:   0xFA1018,
    locationnames.cslk2_cirno_214d:   0xFA1019,
    locationnames.cslk3_cirno_214d:   0xFA101A,
    locationnames.cslk4_cirno_214d:   0xFA101B,
    locationnames.cslk1_cirno_214a1:  0xFA101C,
    locationnames.cslk2_cirno_214a1:  0xFA101D,
    locationnames.cslk3_cirno_214a1:  0xFA101E,
    locationnames.cslk4_cirno_214a1:  0xFA101F,
    locationnames.cslk1_cirno_214a2:  0xFA1020,
    locationnames.cslk2_cirno_214a2:  0xFA1021,
    locationnames.cslk3_cirno_214a2:  0xFA1022,
    locationnames.cslk4_cirno_214a2:  0xFA1023,
    locationnames.cslk1_cirno_22d:    0xFA1024,
    locationnames.cslk2_cirno_22d:    0xFA1025,
    locationnames.cslk3_cirno_22d:    0xFA1026,
    locationnames.cslk4_cirno_22d:    0xFA1027,
    locationnames.cslk1_cirno_22a1:   0xFA1028,
    locationnames.cslk2_cirno_22a1:   0xFA1029,
    locationnames.cslk3_cirno_22a1:   0xFA102A,
    locationnames.cslk4_cirno_22a1:   0xFA102B,
    locationnames.cslk1_cirno_22a2:   0xFA102C,
    locationnames.cslk2_cirno_22a2:   0xFA102D,
    locationnames.cslk3_cirno_22a2:   0xFA102E,
    locationnames.cslk4_cirno_22a2:   0xFA102F,

}

cirno_spell_loc_table = { #0xFA1030 - FA105B
    locationnames.csl1_cirno_2sc_img:  0xFA1030,
    locationnames.csl2_cirno_2sc_img:  0xFA1031,
    locationnames.csl3_cirno_2sc_img:  0xFA1032,
    locationnames.csl4_cirno_2sc_img:  0xFA1033,
    locationnames.csl1_cirno_2sc_fs:   0xFA1034,
    locationnames.csl2_cirno_2sc_fs:   0xFA1035,
    locationnames.csl3_cirno_2sc_fs:   0xFA1036,
    locationnames.csl4_cirno_2sc_fs:   0xFA1037,
    locationnames.csl1_cirno_3sc_cs:   0xFA1038,
    locationnames.csl2_cirno_3sc_cs:   0xFA1039,
    locationnames.csl3_cirno_3sc_cs:   0xFA103A,
    locationnames.csl4_cirno_3sc_cs:   0xFA103B,
    locationnames.csl1_cirno_3sc_sik:  0xFA103C,
    locationnames.csl2_cirno_3sc_sik:  0xFA103D,
    locationnames.csl3_cirno_3sc_sik:  0xFA103E,
    locationnames.csl4_cirno_3sc_sik:  0xFA103F,
    locationnames.csl1_cirno_3sc_sf:   0xFA1040,
    locationnames.csl2_cirno_3sc_sf:   0xFA1041,
    locationnames.csl3_cirno_3sc_sf:   0xFA1042,
    locationnames.csl4_cirno_3sc_sf:   0xFA1043,
    locationnames.csl1_cirno_3sc_fa:   0xFA1044,
    locationnames.csl2_cirno_3sc_fa:   0xFA1045,
    locationnames.csl3_cirno_3sc_fa:   0xFA1046,
    locationnames.csl4_cirno_3sc_fa:   0xFA1047,
    locationnames.csl1_cirno_3sc_ifb:  0xFA1048,
    locationnames.csl2_cirno_3sc_ifb:  0xFA1049,
    locationnames.csl3_cirno_3sc_ifb:  0xFA104A,
    locationnames.csl4_cirno_3sc_ifb:  0xFA104B,
    locationnames.csl1_cirno_4sc_fc:   0xFA104C,
    locationnames.csl2_cirno_4sc_fc:   0xFA104D,
    locationnames.csl3_cirno_4sc_fc:   0xFA104E,
    locationnames.csl4_cirno_4sc_fc:   0xFA104F,
    locationnames.csl1_cirno_4sc_it:   0xFA1050,
    locationnames.csl2_cirno_4sc_it:   0xFA1051,
    locationnames.csl3_cirno_4sc_it:   0xFA1052,
    locationnames.csl4_cirno_4sc_it:   0xFA1053,
    locationnames.csl1_cirno_5sc_pf:   0xFA1054,
    locationnames.csl2_cirno_5sc_pf:   0xFA1055,
    locationnames.csl3_cirno_5sc_pf:   0xFA1056,
    locationnames.csl4_cirno_5sc_pf:   0xFA1057,
    locationnames.csl1_cirno_5sc_gc:   0xFA1058,
    locationnames.csl2_cirno_5sc_gc:   0xFA1059,
    locationnames.csl3_cirno_5sc_gc:   0xFA105A,
    locationnames.csl4_cirno_5sc_gc:   0xFA105B,

}

meiling_skill_loc_table = { #0xFA1100 - FA112F
    locationnames.cslk1_meiling_236d:   0xFA1100,
    locationnames.cslk2_meiling_236d:   0xFA1101,
    locationnames.cslk3_meiling_236d:   0xFA1102,
    locationnames.cslk4_meiling_236d:   0xFA1103,
    locationnames.cslk1_meiling_236a1:  0xFA1104,
    locationnames.cslk2_meiling_236a1:  0xFA1105,
    locationnames.cslk3_meiling_236a1:  0xFA1106,
    locationnames.cslk4_meiling_236a1:  0xFA1107,
    locationnames.cslk1_meiling_236a2:  0xFA1108,
    locationnames.cslk2_meiling_236a2:  0xFA1109,
    locationnames.cslk3_meiling_236a2:  0xFA110A,
    locationnames.cslk4_meiling_236a2:  0xFA110B,
    locationnames.cslk1_meiling_623d:   0xFA110C,
    locationnames.cslk2_meiling_623d:   0xFA110D,
    locationnames.cslk3_meiling_623d:   0xFA110E,
    locationnames.cslk4_meiling_623d:   0xFA110F,
    locationnames.cslk1_meiling_623a1:  0xFA1110,
    locationnames.cslk2_meiling_623a1:  0xFA1111,
    locationnames.cslk3_meiling_623a1:  0xFA1112,
    locationnames.cslk4_meiling_623a1:  0xFA1113,
    locationnames.cslk1_meiling_623a2:  0xFA1114,
    locationnames.cslk2_meiling_623a2:  0xFA1115,
    locationnames.cslk3_meiling_623a2:  0xFA1116,
    locationnames.cslk4_meiling_623a2:  0xFA1117,
    locationnames.cslk1_meiling_214d:   0xFA1118,
    locationnames.cslk2_meiling_214d:   0xFA1119,
    locationnames.cslk3_meiling_214d:   0xFA111A,
    locationnames.cslk4_meiling_214d:   0xFA111B,
    locationnames.cslk1_meiling_214a1:  0xFA111C,
    locationnames.cslk2_meiling_214a1:  0xFA111D,
    locationnames.cslk3_meiling_214a1:  0xFA111E,
    locationnames.cslk4_meiling_214a1:  0xFA111F,
    locationnames.cslk1_meiling_214a2:  0xFA1120,
    locationnames.cslk2_meiling_214a2:  0xFA1121,
    locationnames.cslk3_meiling_214a2:  0xFA1122,
    locationnames.cslk4_meiling_214a2:  0xFA1123,
    locationnames.cslk1_meiling_22d:    0xFA1124,
    locationnames.cslk2_meiling_22d:    0xFA1125,
    locationnames.cslk3_meiling_22d:    0xFA1126,
    locationnames.cslk4_meiling_22d:    0xFA1127,
    locationnames.cslk1_meiling_22a1:   0xFA1128,
    locationnames.cslk2_meiling_22a1:   0xFA1129,
    locationnames.cslk3_meiling_22a1:   0xFA112A,
    locationnames.cslk4_meiling_22a1:   0xFA112B,
    locationnames.cslk1_meiling_22a2:   0xFA112C,
    locationnames.cslk2_meiling_22a2:   0xFA112D,
    locationnames.cslk3_meiling_22a2:   0xFA112E,
    locationnames.cslk4_meiling_22a2:   0xFA112F,

}

meiling_spell_loc_table = { #0xFA1130 - FA115B
    locationnames.csl1_meiling_2sc_cw:     0xFA1130,
    locationnames.csl2_meiling_2sc_cw:     0xFA1131,
    locationnames.csl3_meiling_2sc_cw:     0xFA1132,
    locationnames.csl4_meiling_2sc_cw:     0xFA1133,
    locationnames.csl1_meiling_2sc_irf:    0xFA1134,
    locationnames.csl2_meiling_2sc_irf:    0xFA1135,
    locationnames.csl3_meiling_2sc_irf:    0xFA1136,
    locationnames.csl4_meiling_2sc_irf:    0xFA1137,
    locationnames.csl1_meiling_3sc_sb:     0xFA1138,
    locationnames.csl2_meiling_3sc_sb:     0xFA1139,
    locationnames.csl3_meiling_3sc_sb:     0xFA113A,
    locationnames.csl4_meiling_3sc_sb:     0xFA113B,
    locationnames.csl1_meiling_3sc_rf:     0xFA113C,
    locationnames.csl2_meiling_3sc_rf:     0xFA113D,
    locationnames.csl3_meiling_3sc_rf:     0xFA113E,
    locationnames.csl4_meiling_3sc_rf:     0xFA113F,
    locationnames.csl1_meiling_3sc_edsdk:  0xFA1140,
    locationnames.csl2_meiling_3sc_edsdk:  0xFA1141,
    locationnames.csl3_meiling_3sc_edsdk:  0xFA1142,
    locationnames.csl4_meiling_3sc_edsdk:  0xFA1143,
    locationnames.csl1_meiling_4sc_mcd:    0xFA1144,
    locationnames.csl2_meiling_4sc_mcd:    0xFA1145,
    locationnames.csl3_meiling_4sc_mcd:    0xFA1146,
    locationnames.csl4_meiling_4sc_mcd:    0xFA1147,
    locationnames.csl1_meiling_4sc_rt:     0xFA1148,
    locationnames.csl2_meiling_4sc_rt:     0xFA1149,
    locationnames.csl3_meiling_4sc_rt:     0xFA114A,
    locationnames.csl4_meiling_4sc_rt:     0xFA114B,
    locationnames.csl1_meiling_4sc_fter:   0xFA114C,
    locationnames.csl2_meiling_4sc_fter:   0xFA114D,
    locationnames.csl3_meiling_4sc_fter:   0xFA114E,
    locationnames.csl4_meiling_4sc_fter:   0xFA114F,
    locationnames.csl1_meiling_5sc_emsb:   0xFA1150,
    locationnames.csl2_meiling_5sc_emsb:   0xFA1151,
    locationnames.csl3_meiling_5sc_emsb:   0xFA1152,
    locationnames.csl4_meiling_5sc_emsb:   0xFA1153,
    locationnames.csl1_meiling_5sc_rkf:    0xFA1154,
    locationnames.csl2_meiling_5sc_rkf:    0xFA1155,
    locationnames.csl3_meiling_5sc_rkf:    0xFA1156,
    locationnames.csl4_meiling_5sc_rkf:    0xFA1157,
    locationnames.csl1_meiling_5sc_rbr:    0xFA1158,
    locationnames.csl2_meiling_5sc_rbr:    0xFA1159,
    locationnames.csl3_meiling_5sc_rbr:    0xFA115A,
    locationnames.csl4_meiling_5sc_rbr:    0xFA115B,

}

okuu_skill_loc_table = { #0xFA1200 - FA122F
    locationnames.cslk1_okuu_236d:   0xFA1200,
    locationnames.cslk2_okuu_236d:   0xFA1201,
    locationnames.cslk3_okuu_236d:   0xFA1202,
    locationnames.cslk4_okuu_236d:   0xFA1203,
    locationnames.cslk1_okuu_236a1:  0xFA1204,
    locationnames.cslk2_okuu_236a1:  0xFA1205,
    locationnames.cslk3_okuu_236a1:  0xFA1206,
    locationnames.cslk4_okuu_236a1:  0xFA1207,
    locationnames.cslk1_okuu_236a2:  0xFA1208,
    locationnames.cslk2_okuu_236a2:  0xFA1209,
    locationnames.cslk3_okuu_236a2:  0xFA120A,
    locationnames.cslk4_okuu_236a2:  0xFA120B,
    locationnames.cslk1_okuu_623d:   0xFA120C,
    locationnames.cslk2_okuu_623d:   0xFA120D,
    locationnames.cslk3_okuu_623d:   0xFA120E,
    locationnames.cslk4_okuu_623d:   0xFA120F,
    locationnames.cslk1_okuu_623a1:  0xFA1210,
    locationnames.cslk2_okuu_623a1:  0xFA1211,
    locationnames.cslk3_okuu_623a1:  0xFA1212,
    locationnames.cslk4_okuu_623a1:  0xFA1213,
    locationnames.cslk1_okuu_623a2:  0xFA1214,
    locationnames.cslk2_okuu_623a2:  0xFA1215,
    locationnames.cslk3_okuu_623a2:  0xFA1216,
    locationnames.cslk4_okuu_623a2:  0xFA1217,
    locationnames.cslk1_okuu_214d:   0xFA1218,
    locationnames.cslk2_okuu_214d:   0xFA1219,
    locationnames.cslk3_okuu_214d:   0xFA121A,
    locationnames.cslk4_okuu_214d:   0xFA121B,
    locationnames.cslk1_okuu_214a1:  0xFA121C,
    locationnames.cslk2_okuu_214a1:  0xFA121D,
    locationnames.cslk3_okuu_214a1:  0xFA121E,
    locationnames.cslk4_okuu_214a1:  0xFA121F,
    locationnames.cslk1_okuu_214a2:  0xFA1220,
    locationnames.cslk2_okuu_214a2:  0xFA1221,
    locationnames.cslk3_okuu_214a2:  0xFA1222,
    locationnames.cslk4_okuu_214a2:  0xFA1223,
    locationnames.cslk1_okuu_22d:    0xFA1224,
    locationnames.cslk2_okuu_22d:    0xFA1225,
    locationnames.cslk3_okuu_22d:    0xFA1226,
    locationnames.cslk4_okuu_22d:    0xFA1227,
    locationnames.cslk1_okuu_22a1:   0xFA1228,
    locationnames.cslk2_okuu_22a1:   0xFA1229,
    locationnames.cslk3_okuu_22a1:   0xFA122A,
    locationnames.cslk4_okuu_22a1:   0xFA122B,
    locationnames.cslk1_okuu_22a2:   0xFA122C,
    locationnames.cslk2_okuu_22a2:   0xFA122D,
    locationnames.cslk3_okuu_22a2:   0xFA122E,
    locationnames.cslk4_okuu_22a2:   0xFA122F,

}

okuu_spell_loc_table = { #0xFA1230 - FA1267
    locationnames.csl1_okuu_1sc_has:  0xFA1230,
    locationnames.csl2_okuu_1sc_has:  0xFA1231,
    locationnames.csl3_okuu_1sc_has:  0xFA1232,
    locationnames.csl4_okuu_1sc_has:  0xFA1233,
    locationnames.csl1_okuu_2sc_st:   0xFA1234,
    locationnames.csl2_okuu_2sc_st:   0xFA1235,
    locationnames.csl3_okuu_2sc_st:   0xFA1236,
    locationnames.csl4_okuu_2sc_st:   0xFA1237,
    locationnames.csl1_okuu_2sc_nv:   0xFA1238,
    locationnames.csl2_okuu_2sc_nv:   0xFA1239,
    locationnames.csl3_okuu_2sc_nv:   0xFA123A,
    locationnames.csl4_okuu_2sc_nv:   0xFA123B,
    locationnames.csl1_okuu_3sc_mf:   0xFA123C,
    locationnames.csl2_okuu_3sc_mf:   0xFA123D,
    locationnames.csl3_okuu_3sc_mf:   0xFA123E,
    locationnames.csl4_okuu_3sc_mf:   0xFA123F,
    locationnames.csl1_okuu_3sc_fs:   0xFA1240,
    locationnames.csl2_okuu_3sc_fs:   0xFA1241,
    locationnames.csl3_okuu_3sc_fs:   0xFA1242,
    locationnames.csl4_okuu_3sc_fs:   0xFA1243,
    locationnames.csl1_okuu_3sc_cs:   0xFA1244,
    locationnames.csl2_okuu_3sc_cs:   0xFA1245,
    locationnames.csl3_okuu_3sc_cs:   0xFA1246,
    locationnames.csl4_okuu_3sc_cs:   0xFA1247,
    locationnames.csl1_okuu_3sc_htb:  0xFA1248,
    locationnames.csl2_okuu_3sc_htb:  0xFA1249,
    locationnames.csl3_okuu_3sc_htb:  0xFA124A,
    locationnames.csl4_okuu_3sc_htb:  0xFA124B,
    locationnames.csl1_okuu_4sc_tts:  0xFA124C,
    locationnames.csl2_okuu_4sc_tts:  0xFA124D,
    locationnames.csl3_okuu_4sc_tts:  0xFA124E,
    locationnames.csl4_okuu_4sc_tts:  0xFA124F,
    locationnames.csl1_okuu_4sc_nbg:  0xFA1250,
    locationnames.csl2_okuu_4sc_nbg:  0xFA1251,
    locationnames.csl3_okuu_4sc_nbg:  0xFA1252,
    locationnames.csl4_okuu_4sc_nbg:  0xFA1253,
    locationnames.csl1_okuu_4sc_yd:   0xFA1254,
    locationnames.csl2_okuu_4sc_yd:   0xFA1255,
    locationnames.csl3_okuu_4sc_yd:   0xFA1256,
    locationnames.csl4_okuu_4sc_yd:   0xFA1257,
    locationnames.csl1_okuu_4sc_ud:   0xFA1258,
    locationnames.csl2_okuu_4sc_ud:   0xFA1259,
    locationnames.csl3_okuu_4sc_ud:   0xFA125A,
    locationnames.csl4_okuu_4sc_ud:   0xFA125B,
    locationnames.csl1_okuu_4sc_ss:   0xFA125C,
    locationnames.csl2_okuu_4sc_ss:   0xFA125D,
    locationnames.csl3_okuu_4sc_ss:   0xFA125E,
    locationnames.csl4_okuu_4sc_ss:   0xFA125F,
    locationnames.csl1_okuu_5sc_gf:   0xFA1260,
    locationnames.csl2_okuu_5sc_gf:   0xFA1261,
    locationnames.csl3_okuu_5sc_gf:   0xFA1262,
    locationnames.csl4_okuu_5sc_gf:   0xFA1263,
    locationnames.csl1_okuu_5sc_an:   0xFA1264,
    locationnames.csl2_okuu_5sc_an:   0xFA1265,
    locationnames.csl3_okuu_5sc_an:   0xFA1266,
    locationnames.csl4_okuu_5sc_an:   0xFA1267,

}

suwako_skill_loc_table = { #0xFA1300 - FA132F
    locationnames.cslk1_suwako_236d:   0xFA1300,
    locationnames.cslk2_suwako_236d:   0xFA1301,
    locationnames.cslk3_suwako_236d:   0xFA1302,
    locationnames.cslk4_suwako_236d:   0xFA1303,
    locationnames.cslk1_suwako_236a1:  0xFA1304,
    locationnames.cslk2_suwako_236a1:  0xFA1305,
    locationnames.cslk3_suwako_236a1:  0xFA1306,
    locationnames.cslk4_suwako_236a1:  0xFA1307,
    locationnames.cslk1_suwako_236a2:  0xFA1308,
    locationnames.cslk2_suwako_236a2:  0xFA1309,
    locationnames.cslk3_suwako_236a2:  0xFA130A,
    locationnames.cslk4_suwako_236a2:  0xFA130B,
    locationnames.cslk1_suwako_623d:   0xFA130C,
    locationnames.cslk2_suwako_623d:   0xFA130D,
    locationnames.cslk3_suwako_623d:   0xFA130E,
    locationnames.cslk4_suwako_623d:   0xFA130F,
    locationnames.cslk1_suwako_623a1:  0xFA1310,
    locationnames.cslk2_suwako_623a1:  0xFA1311,
    locationnames.cslk3_suwako_623a1:  0xFA1312,
    locationnames.cslk4_suwako_623a1:  0xFA1313,
    locationnames.cslk1_suwako_623a2:  0xFA1314,
    locationnames.cslk2_suwako_623a2:  0xFA1315,
    locationnames.cslk3_suwako_623a2:  0xFA1316,
    locationnames.cslk4_suwako_623a2:  0xFA1317,
    locationnames.cslk1_suwako_214d:   0xFA1318,
    locationnames.cslk2_suwako_214d:   0xFA1319,
    locationnames.cslk3_suwako_214d:   0xFA131A,
    locationnames.cslk4_suwako_214d:   0xFA131B,
    locationnames.cslk1_suwako_214a1:  0xFA131C,
    locationnames.cslk2_suwako_214a1:  0xFA131D,
    locationnames.cslk3_suwako_214a1:  0xFA131E,
    locationnames.cslk4_suwako_214a1:  0xFA131F,
    locationnames.cslk1_suwako_214a2:  0xFA1320,
    locationnames.cslk2_suwako_214a2:  0xFA1321,
    locationnames.cslk3_suwako_214a2:  0xFA1322,
    locationnames.cslk4_suwako_214a2:  0xFA1323,
    locationnames.cslk1_suwako_22d:    0xFA1324,
    locationnames.cslk2_suwako_22d:    0xFA1325,
    locationnames.cslk3_suwako_22d:    0xFA1326,
    locationnames.cslk4_suwako_22d:    0xFA1327,
    locationnames.cslk1_suwako_22a1:   0xFA1328,
    locationnames.cslk2_suwako_22a1:   0xFA1329,
    locationnames.cslk3_suwako_22a1:   0xFA132A,
    locationnames.cslk4_suwako_22a1:   0xFA132B,
    locationnames.cslk1_suwako_22a2:   0xFA132C,
    locationnames.cslk2_suwako_22a2:   0xFA132D,
    locationnames.cslk3_suwako_22a2:   0xFA132E,
    locationnames.cslk4_suwako_22a2:   0xFA132F,

}

suwako_spell_loc_table = { #0xFA1330 - FA135B
    locationnames.csl1_suwako_2sc_mcw:    0xFA1330,
    locationnames.csl2_suwako_2sc_mcw:    0xFA1331,
    locationnames.csl3_suwako_2sc_mcw:    0xFA1332,
    locationnames.csl4_suwako_2sc_mcw:    0xFA1333,
    locationnames.csl1_suwako_2sc_mmr:    0xFA1334,
    locationnames.csl2_suwako_2sc_mmr:    0xFA1335,
    locationnames.csl3_suwako_2sc_mmr:    0xFA1336,
    locationnames.csl4_suwako_2sc_mmr:    0xFA1337,
    locationnames.csl1_suwako_3sc_mg:     0xFA1338,
    locationnames.csl2_suwako_3sc_mg:     0xFA1339,
    locationnames.csl3_suwako_3sc_mg:     0xFA133A,
    locationnames.csl4_suwako_3sc_mg:     0xFA133B,
    locationnames.csl1_suwako_3sc_bcb:    0xFA133C,
    locationnames.csl2_suwako_3sc_bcb:    0xFA133D,
    locationnames.csl3_suwako_3sc_bcb:    0xFA133E,
    locationnames.csl4_suwako_3sc_bcb:    0xFA133F,
    locationnames.csl1_suwako_3sc_fbte:   0xFA1340,
    locationnames.csl2_suwako_3sc_fbte:   0xFA1341,
    locationnames.csl3_suwako_3sc_fbte:   0xFA1342,
    locationnames.csl4_suwako_3sc_fbte:   0xFA1343,
    locationnames.csl1_suwako_4sc_hrj:    0xFA1344,
    locationnames.csl2_suwako_4sc_hrj:    0xFA1345,
    locationnames.csl3_suwako_4sc_hrj:    0xFA1346,
    locationnames.csl4_suwako_4sc_hrj:    0xFA1347,
    locationnames.csl1_suwako_4sc_shaef:  0xFA1348,
    locationnames.csl2_suwako_4sc_shaef:  0xFA1349,
    locationnames.csl3_suwako_4sc_shaef:  0xFA134A,
    locationnames.csl4_suwako_4sc_shaef:  0xFA134B,
    locationnames.csl1_suwako_4sc_ml:     0xFA134C,
    locationnames.csl2_suwako_4sc_ml:     0xFA134D,
    locationnames.csl3_suwako_4sc_ml:     0xFA134E,
    locationnames.csl4_suwako_4sc_ml:     0xFA134F,
    locationnames.csl1_suwako_4sc_rfoh:   0xFA1350,
    locationnames.csl2_suwako_4sc_rfoh:   0xFA1351,
    locationnames.csl3_suwako_4sc_rfoh:   0xFA1352,
    locationnames.csl4_suwako_4sc_rfoh:   0xFA1353,
    locationnames.csl1_suwako_4sc_cah:    0xFA1354,
    locationnames.csl2_suwako_4sc_cah:    0xFA1355,
    locationnames.csl3_suwako_4sc_cah:    0xFA1356,
    locationnames.csl4_suwako_4sc_cah:    0xFA1357,
    locationnames.csl1_suwako_5sc_ms:     0xFA1358,
    locationnames.csl2_suwako_5sc_ms:     0xFA1359,
    locationnames.csl3_suwako_5sc_ms:     0xFA135A,
    locationnames.csl4_suwako_5sc_ms:     0xFA135B

}

all_locations = {
    **goal_location_table, #26
    **sanae_story_stage_table, #5
    **sanae_story_spell_table, #16
    **cirno_story_stage_table, #5
    **cirno_story_spell_table, #16
    **meiling_story_stage_table, #5
    **meiling_story_spell_table, #16

    **reimu_arcade_stage_table,
    **marisa_arcade_stage_table,
    **sakuya_arcade_stage_table,
    **alice_arcade_stage_table,
    **patchouli_arcade_stage_table,
    **youmu_arcade_stage_table,
    **remilia_arcade_stage_table,
    **yuyuko_arcade_stage_table,
    **yukari_arcade_stage_table,
    **suika_arcade_stage_table,
    **reisen_arcade_stage_table,
    **aya_arcade_stage_table,
    **komachi_arcade_stage_table,
    **iku_arcade_stage_table,
    **tenshi_arcade_stage_table,
    **sanae_arcade_stage_table,
    **cirno_arcade_stage_table,
    **meiling_arcade_stage_table,
    **okuu_arcade_stage_table,
    **suwako_arcade_stage_table,

    **reimu_vs_win_table,
    **marisa_vs_win_table,
    **sakuya_vs_win_table,
    **alice_vs_win_table,
    **patchouli_vs_win_table,
    **youmu_vs_win_table,
    **remilia_vs_win_table,
    **yuyuko_vs_win_table,
    **yukari_vs_win_table,
    **suika_vs_win_table,
    **reisen_vs_win_table,
    **aya_vs_win_table,
    **komachi_vs_win_table,
    **iku_vs_win_table,
    **tenshi_vs_win_table,
    **sanae_vs_win_table,
    **cirno_vs_win_table,
    **meiling_vs_win_table,
    **okuu_vs_win_table,
    **suwako_vs_win_table,

    **reimu_vs_defeat_table,
    **marisa_vs_defeat_table,
    **sakuya_vs_defeat_table,
    **alice_vs_defeat_table,
    **patchouli_vs_defeat_table,
    **youmu_vs_defeat_table,
    **remilia_vs_defeat_table,
    **yuyuko_vs_defeat_table,
    **yukari_vs_defeat_table,
    **suika_vs_defeat_table,
    **reisen_vs_defeat_table,
    **aya_vs_defeat_table,
    **komachi_vs_defeat_table,
    **iku_vs_defeat_table,
    **tenshi_vs_defeat_table,
    **sanae_vs_defeat_table,
    **cirno_vs_defeat_table,
    **meiling_vs_defeat_table,
    **okuu_vs_defeat_table,
    **suwako_vs_defeat_table,

    **start_sys_card_table,
    **reimu_start_card_table,
    **marisa_start_card_table,
    **sakuya_start_card_table,
    **alice_start_card_table,
    **patchouli_start_card_table,
    **youmu_start_card_table,
    **remilia_start_card_table,
    **yuyuko_start_card_table,
    **yukari_start_card_table,
    **suika_start_card_table,
    **reisen_start_card_table,
    **aya_start_card_table,
    **komachi_start_card_table,
    **iku_start_card_table,
    **tenshi_start_card_table,
    **sanae_start_card_table,
    **cirno_start_card_table,
    **meiling_start_card_table,
    **okuu_start_card_table,
    **suwako_start_card_table,

    **reimu_skill_loc_table,
    **reimu_spell_loc_table,
    **marisa_skill_loc_table,
    **marisa_spell_loc_table,
    **sakuya_skill_loc_table,
    **sakuya_spell_loc_table,
    **alice_skill_loc_table,
    **alice_spell_loc_table,
    **patchouli_skill_loc_table,
    **patchouli_spell_loc_table,
    **youmu_skill_loc_table,
    **youmu_spell_loc_table,
    **remilia_skill_loc_table,
    **remilia_spell_loc_table,
    **yuyuko_skill_loc_table,
    **yuyuko_spell_loc_table,
    **yukari_skill_loc_table,
    **yukari_spell_loc_table,
    **suika_skill_loc_table,
    **suika_spell_loc_table,
    **reisen_skill_loc_table,
    **reisen_spell_loc_table,
    **aya_skill_loc_table,
    **aya_spell_loc_table,
    **komachi_skill_loc_table,
    **komachi_spell_loc_table,
    **iku_skill_loc_table,
    **iku_spell_loc_table,
    **tenshi_skill_loc_table,
    **tenshi_spell_loc_table,
    **sanae_skill_loc_table,
    **sanae_spell_loc_table,
    **cirno_skill_loc_table,
    **cirno_spell_loc_table,
    **meiling_skill_loc_table,
    **meiling_spell_loc_table,
    **okuu_skill_loc_table,
    **okuu_spell_loc_table,
    **suwako_skill_loc_table,
    **suwako_spell_loc_table

}

lookup_id_to_name: Dict[int, str] = {id: name for name, _ in all_locations.items()}


def setup_locations(world: World, player: int):
    location_table = {}
    
    #Add Story stage and spell checks per the player setting
    if world.option.story_mode_checks == "Sanae":
        location_table.update({**sanae_story_stage_table})
        location_table.update({**sanae_story_spell_table})
    if world.option.story_mode_checks == "Cirno":
        location_table.update({**cirno_story_stage_table})
        location_table.update({**cirno_story_spell_table})
    if world.option.story_mode_checks == "Meiling":
        location_table.update({**meiling_story_stage_table})
        location_table.update({**meiling_story_spell_table})

    #Add VS mode locations per the player setting
    if world.options.vs_mode_character_wins == 1:
        if world.options.vs_mode_win_count == 1:
            for index, (key, value) in enumerate(locationnames.items()):
                if key[-3:] == "_w1":
                    location_table.update({locationnames[key]})
        if world.options.vs_mode_win_count == 2:
            for index, (key, value) in enumerate(locationnames.items()):
                if key[-3:] == "_w1":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w2":
                    location_table.update({locationnames[key]})
        if world.options.vs_mode_win_count == 3:
            for index, (key, value) in enumerate(locationnames.items()):
                if key[-3:] == "_w1":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w2":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w3":
                    location_table.update({locationnames[key]})
        if world.options.vs_mode_win_count == 4:
            for index, (key, value) in enumerate(locationnames.items()):
                if key[-3:] == "_w1":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w2":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w3":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w4":
                    location_table.update({locationnames[key]})
        if world.options.vs_mode_win_count == 5:
            for index, (key, value) in enumerate(locationnames.items()):
                if key[-3:] == "_w1":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w2":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w3":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w4":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w5":
                    location_table.update({locationnames[key]})
        if world.options.vs_mode_win_count == 6:
            for index, (key, value) in enumerate(locationnames.items()):
                if key[-3:] == "_w1":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w2":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w3":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w4":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w5":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w6":
                    location_table.update({locationnames[key]})
        if world.options.vs_mode_win_count == 7:
            for index, (key, value) in enumerate(locationnames.items()):
                if key[-3:] == "_w1":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w2":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w3":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w4":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w5":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w6":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w7":
                    location_table.update({locationnames[key]})
        if world.options.vs_mode_win_count == 8:
            for index, (key, value) in enumerate(locationnames.items()):
                if key[-3:] == "_w1":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w2":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w3":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w4":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w5":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w6":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w7":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w8":
                    location_table.update({locationnames[key]})
        if world.options.vs_mode_win_count == 9:
            for index, (key, value) in enumerate(locationnames.items()):
                if key[-3:] == "_w1":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w2":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w3":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w4":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w5":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w6":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w7":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w8":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w9":
                    location_table.update({locationnames[key]})
        if world.options.vs_mode_win_count == 10:
            for index, (key, value) in enumerate(locationnames.items()):
                if key[-3:] == "_w1":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w2":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w3":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w4":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w5":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w6":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w7":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w8":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w9":
                    location_table.update({locationnames[key]})
                if key[-3:] == "_w10":
                    location_table.update({locationnames[key]})

        #Check VS Mode Blacklist
        if world.option.vs_blacklist_player == "Reimu":
            del location_table[{**reimu_vs_win_table}]
        if world.option.vs_blacklist_player == "Marisa":
            del location_table[{**marisa_vs_win_table}]
        if world.option.vs_blacklist_player == "Sakuya":
            del location_table[{**sakuya_vs_win_table}]
        if world.option.vs_blacklist_player == "Alice":
            del location_table[{**alice_vs_win_table}]
        if world.option.vs_blacklist_player == "Patchouli":
            del location_table[{**patchouli_vs_win_table}]
        if world.option.vs_blacklist_player == "Youmu":
            del location_table[{**youmu_vs_win_table}]
        if world.option.vs_blacklist_player == "Remilia":
            del location_table[{**remilia_vs_win_table}]
        if world.option.vs_blacklist_player == "Yuyuko":
            del location_table[{**yuyuko_vs_win_table}]
        if world.option.vs_blacklist_player == "Yukari":
            del location_table[{**yukari_vs_win_table}]
        if world.option.vs_blacklist_player == "Suika":
            del location_table[{**suika_vs_win_table}]
        if world.option.vs_blacklist_player == "Reisen":
            del location_table[{**reisen_vs_win_table}]
        if world.option.vs_blacklist_player == "Aya":
            del location_table[{**aya_vs_win_table}]
        if world.option.vs_blacklist_player == "Komachi":
            del location_table[{**komachi_vs_win_table}]
        if world.option.vs_blacklist_player == "Iku":
            del location_table[{**iku_vs_win_table}]
        if world.option.vs_blacklist_player == "Tenshi":
            del location_table[{**tenshi_vs_win_table}]

    #Add all Arcade mode checks if enabled
    if world.option.arcade_mode_checks == 1:
        location_table.update({**reimu_arcade_stage_table})
        location_table.update({**marisa_arcade_stage_table})
        location_table.update({**sakuya_arcade_stage_table})
        location_table.update({**alice_arcade_stage_table})
        location_table.update({**patchouli_arcade_stage_table})
        location_table.update({**youmu_arcade_stage_table})
        location_table.update({**remilia_arcade_stage_table})
        location_table.update({**yuyuko_arcade_stage_table})
        location_table.update({**yukari_arcade_stage_table})
        location_table.update({**suika_arcade_stage_table})
        location_table.update({**reisen_arcade_stage_table})
        location_table.update({**aya_arcade_stage_table})
        location_table.update({**komachi_arcade_stage_table})
        location_table.update({**iku_arcade_stage_table})
        location_table.update({**tenshi_arcade_stage_table})
        location_table.update({**sanae_arcade_stage_table})
        location_table.update({**cirno_arcade_stage_table})
        location_table.update({**meiling_arcade_stage_table})
        location_table.update({**okuu_arcade_stage_table})
        location_table.update({**suwako_arcade_stage_table})

        #Check Arcade Mode Blacklist    
        if world.option.arcade_mode_blacklist == "Reimu":
            del location_table[{**reimu_arcade_stage_table}]
        if world.option.arcade_mode_blacklist == "Marisa":
            del location_table[{**marisa_arcade_stage_table}]
        if world.option.arcade_mode_blacklist == "Sakuya":
            del location_table[{**sakuya_arcade_stage_table}]
        if world.option.arcade_mode_blacklist == "Alice":
            del location_table[{**alice_arcade_stage_table}]
        if world.option.arcade_mode_blacklist == "Patchouli":
            del location_table[{**patchouli_arcade_stage_table}]
        if world.option.arcade_mode_blacklist == "Youmu":
            del location_table[{**youmu_arcade_stage_table}]
        if world.option.arcade_mode_blacklist == "Remilia":
            del location_table[{**remilia_arcade_stage_table}]
        if world.option.arcade_mode_blacklist == "Yuyuko":
            del location_table[{**yuyuko_arcade_stage_table}]
        if world.option.arcade_mode_blacklist == "Yukari":
            del location_table[{**yukari_arcade_stage_table}]
        if world.option.arcade_mode_blacklist == "Suika":
            del location_table[{**suika_arcade_stage_table}]
        if world.option.arcade_mode_blacklist == "Reisen":
            del location_table[{**reisen_arcade_stage_table}]
        if world.option.arcade_mode_blacklist == "Aya":
            del location_table[{**aya_arcade_stage_table}]
        if world.option.arcade_mode_blacklist == "Komachi":
            del location_table[{**komachi_arcade_stage_table}]
        if world.option.arcade_mode_blacklist == "Iku":
            del location_table[{**iku_arcade_stage_table}]
        if world.option.arcade_mode_blacklist == "Tenshi":
            del location_table[{**tenshi_arcade_stage_table}]
        if world.option.arcade_mode_blacklist == "Sanae":
            del location_table[{**sanae_arcade_stage_table}]
        if world.option.arcade_mode_blacklist == "Cirno":
            del location_table[{**cirno_arcade_stage_table}]
        if world.option.arcade_mode_blacklist == "Meiling":
            del location_table[{**meiling_arcade_stage_table}]
        if world.option.arcade_mode_blacklist == "Utsuho":
            del location_table[{**okuu_arcade_stage_table}]
        if world.option.arcade_mode_blacklist == "Suwako":
            del location_table[{**suwako_arcade_stage_table}]
    
    
    #Add Skillsanity checks per the player option
    if world.option.cardsanity_skills == 1:
        for index, (key, value) in enumerate(locationnames.items()):
            if key[+5:] == "cslk1":
                location_table.update({locationnames[key]})
    if world.option.cardsanity_skills == 2:
        for index, (key, value) in enumerate(locationnames.items()):
            if key[+5:] == "cslk4":
                location_table.update({locationnames[key]})
    if world.option.cardsanity_skills == 3:
        for index, (key, value) in enumerate(locationnames.items()):
            if key[+4:] == "cslk":
                location_table.update({locationnames[key]})

    #Check Spellsanity Count if Cardsanity Spells is enabled
    if world.option.cardsanity_spells == 1:
        if world.option.cardsanity_spell_count == 1:
            for index, (key, value) in enumerate(locationnames.items()):
                if key[+4:] == "csl1":
                    location_table.update({locationnames[key]})
        if world.option.cardsanity_spell_count == 2:
            for index, (key, value) in enumerate(locationnames.items()):
                if key[+4:] == "csl1":
                    location_table.update({locationnames[key]})
            for index, (key, value) in enumerate(locationnames.items()):
                if key[+4:] == "csl2":
                    location_table.update({locationnames[key]})
        if world.option.cardsanity_spell_count == 3:
            for index, (key, value) in enumerate(locationnames.items()):
                if key[+4:] == "csl1":
                    location_table.update({locationnames[key]})
            for index, (key, value) in enumerate(locationnames.items()):
                if key[+4:] == "csl2":
                    location_table.update({locationnames[key]})
            for index, (key, value) in enumerate(locationnames.items()):
                if key[+4:] == "csl3":
                    location_table.update({locationnames[key]})
        if world.option.cardsanity_spell_count == 4:
            for index, (key, value) in enumerate(locationnames.items()):
                if key[+4:] == "csl1":
                    location_table.update({locationnames[key]})
            for index, (key, value) in enumerate(locationnames.items()):
                if key[+4:] == "csl2":
                    location_table.update({locationnames[key]})
            for index, (key, value) in enumerate(locationnames.items()):
                if key[+4:] == "csl3":
                    location_table.update({locationnames[key]})
            for index, (key, value) in enumerate(locationnames.items()):
                if key[+4:] == "csl4":
                    location_table.update({locationnames[key]})

        
    #Check Cardsanity Blacklist
    if world.option.cardsanity_blacklist == "Reimu":
        del location_table[{**reimu_skill_loc_table}]
        del location_table[{**reimu_spell_loc_table}]
    if world.option.cardsanity_blacklist == "Marisa":
        del location_table[{**marisa_skill_loc_table}]
        del location_table[{**marisa_spell_loc_table}]
    if world.option.cardsanity_blacklist == "Sakuya":
        del location_table[{**sakuya_skill_loc_table}]
        del location_table[{**sakuya_spell_loc_table}]
    if world.option.cardsanity_blacklist == "Alice":
        del location_table[{**alice_skill_loc_table}]
        del location_table[{**alice_spell_loc_table}]
    if world.option.cardsanity_blacklist == "Patchouli":
        del location_table[{**patchouli_skill_loc_table}]
        del location_table[{**patchouli_spell_loc_table}]
    if world.option.cardsanity_blacklist == "Youmu":
        del location_table[{**youmu_skill_loc_table}]
        del location_table[{**youmu_spell_loc_table}]
    if world.option.cardsanity_blacklist == "Remilia":
        del location_table[{**remilia_skill_loc_table}]
        del location_table[{**remilia_spell_loc_table}]
    if world.option.cardsanity_blacklist == "Yuyuko":
        del location_table[{**yuyuko_skill_loc_table}]
        del location_table[{**yuyuko_spell_loc_table}]
    if world.option.cardsanity_blacklist == "Yukari":
        del location_table[{**yukari_skill_loc_table}]
        del location_table[{**yukari_spell_loc_table}]
    if world.option.cardsanity_blacklist == "Suika":
        del location_table[{**suika_skill_loc_table}]
        del location_table[{**suika_spell_loc_table}]
    if world.option.cardsanity_blacklist == "Reisen":
        del location_table[{**reisen_skill_loc_table}]
        del location_table[{**reisen_spell_loc_table}]
    if world.option.cardsanity_blacklist == "Aya":
        del location_table[{**aya_skill_loc_table}]
        del location_table[{**aya_spell_loc_table}]
    if world.option.cardsanity_blacklist == "Komachi":
        del location_table[{**komachi_skill_loc_table}]
        del location_table[{**komachi_spell_loc_table}]
    if world.option.cardsanity_blacklist == "Iku":
        del location_table[{**iku_skill_loc_table}]
        del location_table[{**iku_spell_loc_table}]
    if world.option.cardsanity_blacklist == "Tenshi":
        del location_table[{**tenshi_skill_loc_table}]
        del location_table[{**tenshi_spell_loc_table}]
    if world.option.cardsanity_blacklist == "Sanae":
        del location_table[{**sanae_skill_loc_table}]
        del location_table[{**sanae_spell_loc_table}]
    if world.option.cardsanity_blacklist == "Cirno":
        del location_table[{**cirno_skill_loc_table}]
        del location_table[{**cirno_spell_loc_table}]
    if world.option.cardsanity_blacklist == "Meiling":
        del location_table[{**meiling_skill_loc_table}]
        del location_table[{**meiling_spell_loc_table}]
    if world.option.cardsanity_blacklist == "Utsuho":
        del location_table[{**okuu_skill_loc_table}]
        del location_table[{**okuu_spell_loc_table}]
    if world.option.cardsanity_blacklist == "Suwako":
        del location_table[{**suwako_skill_loc_table}]
        del location_table[{**suwako_spell_loc_table}]


    return location_table
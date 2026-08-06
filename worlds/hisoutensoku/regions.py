from typing import TYPE_CHECKING
from BaseClasses import Region, Entrance
from .locations import location_table, lookup_id_to_name

if TYPE_CHECKING:
    from . import SokuWorld

def create_and_connect_regions(world: SokuWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: SokuWorld) -> None:
    menu = Region("Menu", world.player, world.multiworld)

    reimu =     Region("Reimu Select", world.player, world.multiworld)
    marisa =    Region("Marisa Select", world.player, world.multiworld)
    sakuya =    Region("Sakuya Select", world.player, world.multiworld)
    alice =     Region("Alice Select", world.player, world.multiworld)
    patchouli = Region("Patchouli Select", world.player, world.multiworld)
    youmu =     Region("Youmu Select", world.player, world.multiworld)
    remilia =   Region("Remilia Select", world.player, world.multiworld)
    yuyuko =    Region("Yuyuko Select", world.player, world.multiworld)
    yukari =    Region("Yukari Select", world.player, world.multiworld)
    suika =     Region("Suika Select", world.player, world.multiworld)
    reisen =    Region("Reisen Select", world.player, world.multiworld)
    aya =       Region("Aya Select", world.player, world.multiworld)
    komachi =   Region("Komachi Select", world.player, world.multiworld)
    iku =       Region("Iku Select", world.player, world.multiworld)
    tenshi =    Region("Tenshi Select", world.player, world.multiworld)
    sanae =     Region("Sanae Select", world.player, world.multiworld)
    cirno =     Region("Cirno Select", world.player, world.multiworld)
    meiling =   Region("Meiling Select", world.player, world.multiworld)
    utsuho =    Region("Utsuho Select", world.player, world.multiworld)
    suwako =    Region("Suwako Select", world.player, world.multiworld)

    soku_regions = [
        menu,

        reimu,
        marisa,
        sakuya,
        alice,
        patchouli,
        youmu,
        remilia,
        yuyuko,
        yukari,
        suika,
        reisen,
        aya,
        komachi,
        iku,
        tenshi,
        sanae,
        cirno,
        meiling,
        utsuho,
        suwako
    ]
   
    if world.option.story_mode_checks  == 'Sanae':
        sanae_s1 = Region("Sanae Story 1", world.player, world.multiworld)
        sanae_s2 = Region("Sanae Story 2", world.player, world.multiworld)
        sanae_s3 = Region("Sanae Story 3", world.player, world.multiworld)
        sanae_s4 = Region("Sanae Story 4", world.player, world.multiworld)
        sanae_s5 = Region("Sanae Story 5", world.player, world.multiworld)
        soku_regions.append(
            sanae_s1,
            sanae_s2,
            sanae_s3,
            sanae_s4,
            sanae_s5,
        )
    if world.option.story_mode_checks  == 'Cirno':
        cirno_s1 = Region("Cirno Story 1", world.player, world.multiworld)
        cirno_s2 = Region("Cirno Story 2", world.player, world.multiworld)
        cirno_s3 = Region("Cirno Story 3", world.player, world.multiworld)
        cirno_s4 = Region("Cirno Story 4", world.player, world.multiworld)
        cirno_s5 = Region("Cirno Story 5", world.player, world.multiworld)
        soku_regions.append(
            cirno_s1,
            cirno_s2,
            cirno_s3,
            cirno_s4,
            cirno_s5,
        )
    if world.option.story_mode_checks  == 'Meiling':
        meiling_s1 = Region("Meiling Story 1", world.player, world.multiworld)
        meiling_s2 = Region("Meiling Story 2", world.player, world.multiworld)
        meiling_s3 = Region("Meiling Story 3", world.player, world.multiworld)
        meiling_s4 = Region("Meiling Story 4", world.player, world.multiworld)
        meiling_s5 = Region("Meiling Story 5", world.player, world.multiworld)
        soku_regions.append(
            meiling_s1,
            meiling_s2,
            meiling_s3,
            meiling_s4,
            meiling_s5,
        )


    if world.option.arcade_mode_checks == 'True':
        reimu_ar =     Region("Reimu Arcade", world.player, world.multiworld)
        marisa_ar =    Region("Marisa Arcade", world.player, world.multiworld)
        sakuya_ar =    Region("Sakuya Arcade", world.player, world.multiworld)
        alice_ar =     Region("Alice Arcade", world.player, world.multiworld)
        patchouli_ar = Region("Patchouli Arcade", world.player, world.multiworld)
        youmu_ar =     Region("Youmu Arcade", world.player, world.multiworld)
        remilia_ar =   Region("Remilia Arcade", world.player, world.multiworld)
        yuyuko_ar =    Region("Yuyuko Arcade", world.player, world.multiworld)
        yukari_ar =    Region("Yukari Arcade", world.player, world.multiworld)
        suika_ar =     Region("Suika Arcade", world.player, world.multiworld)
        reisen_ar =    Region("Reisen Arcade", world.player, world.multiworld)
        aya_ar =       Region("Aya Arcade", world.player, world.multiworld)
        komachi_ar =   Region("Komachi Arcade", world.player, world.multiworld)
        iku_ar =       Region("Iku Arcade", world.player, world.multiworld)
        tenshi_ar =    Region("Tenshi Arcade", world.player, world.multiworld)
        sanae_ar =     Region("Sanae Arcade", world.player, world.multiworld)
        cirno_ar =     Region("Cirno Arcade", world.player, world.multiworld)
        meiling_ar =   Region("Meiling Arcade", world.player, world.multiworld)
        utsuho_ar =    Region("Utsuho Arcade", world.player, world.multiworld)
        suwako_ar =    Region("Suwako Arcade", world.player, world.multiworld)
        soku_regions.append(
            reimu_ar,
            marisa_ar,
            sakuya_ar,
            alice_ar,
            patchouli_ar,
            youmu_ar,
            remilia_ar,
            yuyuko_ar,
            yukari_ar,
            suika_ar,
            reisen_ar,
            aya_ar,
            komachi_ar,
            iku_ar,
            tenshi_ar,
            sanae_ar,
            cirno_ar,
            meiling_ar,
            utsuho_ar,
            suwako_ar
        )

    match world.option.cardsanity_skills:
        case 1 | 2 | 3:
            reimu_cdsk =     Region("Reimu Card Skills", world.player, world.multiworld)
            marisa_cdsk =    Region("Marisa Card Skills", world.player, world.multiworld)
            sakuya_cdsk =    Region("Sakuya Card Skills", world.player, world.multiworld)
            alice_cdsk =     Region("Alice Card Skills", world.player, world.multiworld)
            patchouli_cdsk = Region("Patchouli Card Skills", world.player, world.multiworld)
            youmu_cdsk =     Region("Youmu Card Skills", world.player, world.multiworld)
            remilia_cdsk =   Region("Remilia Card Skills", world.player, world.multiworld)
            yuyuko_cdsk =    Region("Yuyuko Card Skills", world.player, world.multiworld)
            yukari_cdsk =    Region("Yukari Card Skills", world.player, world.multiworld)
            suika_cdsk =     Region("Suika Card Skills", world.player, world.multiworld)
            reisen_cdsk =    Region("Reisen Card Skills", world.player, world.multiworld)
            aya_cdsk =       Region("Aya Card Skills", world.player, world.multiworld)
            komachi_cdsk =   Region("Komachi Card Skills", world.player, world.multiworld)
            iku_cdsk =       Region("Iku Card Skills", world.player, world.multiworld)
            tenshi_cdsk =    Region("Tenshi Card Skills", world.player, world.multiworld)
            sanae_cdsk =     Region("Sanae Card Skills", world.player, world.multiworld)
            cirno_cdsk =     Region("Cirno Card Skills", world.player, world.multiworld)
            meiling_cdsk =   Region("Meiling Card Skills", world.player, world.multiworld)
            utsuho_cdsk =    Region("Utsuho Card Skills", world.player, world.multiworld)
            suwako_cdsk =    Region("Suwako Card Skills", world.player, world.multiworld)
            soku_regions.append(
                reimu_cdsk,
                marisa_cdsk,
                sakuya_cdsk,
                alice_cdsk,
                patchouli_cdsk,
                youmu_cdsk,
                remilia_cdsk,
                yuyuko_cdsk,
                yukari_cdsk,
                suika_cdsk,
                reisen_cdsk,
                aya_cdsk,
                komachi_cdsk,
                iku_cdsk,
                tenshi_cdsk,
                sanae_cdsk,
                cirno_cdsk,
                meiling_cdsk,
                utsuho_cdsk,
                suwako_cdsk
            )
    match world.option.cardsanity_spells:
        case 1:
            reimu_cdsp =     Region("Reimu Card Spells", world.player, world.multiworld)
            marisa_cdsp =    Region("Marisa Card Spells", world.player, world.multiworld)
            sakuya_cdsp =    Region("Sakuya Card Spells", world.player, world.multiworld)
            alice_cdsp =     Region("Alice Card Spells", world.player, world.multiworld)
            patchouli_cdsp = Region("Patchouli Card Spells", world.player, world.multiworld)
            youmu_cdsp =     Region("Youmu Card Spells", world.player, world.multiworld)
            remilia_cdsp =   Region("Remilia Card Spells", world.player, world.multiworld)
            yuyuko_cdsp =    Region("Yuyuko Card Spells", world.player, world.multiworld)
            yukari_cdsp =    Region("Yukari Card Spells", world.player, world.multiworld)
            suika_cdsp =     Region("Suika Card Spells", world.player, world.multiworld)
            reisen_cdsp =    Region("Reisen Card Spells", world.player, world.multiworld)
            aya_cdsp =       Region("Aya Card Spells", world.player, world.multiworld)
            komachi_cdsp =   Region("Komachi Card Spells", world.player, world.multiworld)
            iku_cdsp =       Region("Iku Card Spells", world.player, world.multiworld)
            tenshi_cdsp =    Region("Tenshi Card Spells", world.player, world.multiworld)
            sanae_cdsp =     Region("Sanae Card Spells", world.player, world.multiworld)
            cirno_cdsp =     Region("Cirno Card Spells", world.player, world.multiworld)
            meiling_cdsp =   Region("Meiling Card Spells", world.player, world.multiworld)
            utsuho_cdsp =    Region("Utsuho Card Spells", world.player, world.multiworld)
            suwako_cdsp =    Region("Suwako Card Spells", world.player, world.multiworld)
            soku_regions.append(
                reimu_cdsp,
                marisa_cdsp,
                sakuya_cdsp,
                alice_cdsp,
                patchouli_cdsp,
                youmu_cdsp,
                remilia_cdsp,
                yuyuko_cdsp,
                yukari_cdsp,
                suika_cdsp,
                reisen_cdsp,
                aya_cdsp,
                komachi_cdsp,
                iku_cdsp,
                tenshi_cdsp,
                sanae_cdsp,
                cirno_cdsp,
                meiling_cdsp,
                utsuho_cdsp,
                suwako_cdsp
            )

    world.multiworld.regions += soku_regions


def connect_regions(world: SokuWorld) -> None:
    menu = world.get_region("Menu")



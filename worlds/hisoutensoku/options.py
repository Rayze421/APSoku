from dataclasses import dataclass

from options import Choice, List, Toggle, OptionSet, DefaultOnToggle, PerGameCommonOptions, Deathlink, Range

class Goal(OptionSet):
    """
    Determines your goal condition, list however many 

    Defining multiple goal conditions will mean that you must fulfill 
    all conditions before your game is marked as complete

    - Story: Find all required items to complete a number of the 3 
    characters' Story Modes. 
    * Each of the 3 characters need their own "Progressive Story 
    Stage" item to access each stage past the first, up to the final 
    stage.
    * (This will add "Sanae" to "Story Mode Checks" if the setting is otherwise empty)
    
    - Arcade (Default): Find all required items to complete Arcade Mode with a 
    number of characters
    * Each character needs their own "Progressive Arcade Stage" item 
    to access each stage past the first, up to the final stage 
    * (This will default "Arcade Mode Checks" to be true if listed)

    - Card Collector: Collect a number of Special or Spell cards from 
    any character, defined in "Card Collector Count". Requires cards 
    to be shuffled into the item pool.

    - Card Master: Obtain the checks for maxing out a number of 
    caracters' Special cards/activating Spellcards, defined in 
    "Card Master Count". Requires cards to be shuffled into the item pool.


    
    """
    display_name = "Goal"
    valid_keys = ["Story", "Arcade", "Card Collector", "Card Master"]
    default = ["Arcade"]

class StoryModeCount(Range):
    """
    If Story Mode is chosen as a goal condition, determine how many 
    Story paths must be completed to count towards the goal.
    """
    display_name = "Story Mode Count"
    range_start = 1
    range_end = 3
    
class ArcadeModeCount(Range):
    """
    If Arcade is selected as a goal condition, determine how many 
    characters you must complete all 10 rounds of Arcade Mode with 
    to count towards the goal
    """
    display_name = "Arcade Mode Count"
    range_start = 1
    range_end = 20

class CardCollectorCount(Range):
    """
    If "Card Collector" is selected as a goal condition, determines 
    what percentage of available character Special and Spell cards must be 
    collected to count towards the goal.
    """
    display_name = "Card Collector Goal"
    range_start = 1
    range_end = 100

class CardMasterCount(Range):
    """
    If "Card Master" is selected as a goal option, determines what 
    percentage of available special and spell card checks must be completed 
    to count towards the goal.
    """
    display_name = "Card Master Count"
    range_start = 1
    range_end = 100

class StartingCharacter(Choice):
    """
    Choose which character you wish to start with for modes other 
    than Story Mode. Only one can be chosen here, but additional 
    characters can be added to "Start Inventory From Pool".
    """
    display_name = "Starting Character"
    default = "random"
    option_alice = 0
    option_aya = 1
    option_cirno = 2
    option_iku = 3
    option_Komachi = 4
    option_marisa = 5
    option_meiling = 6
    option_patchouli = 7
    option_reimu = 8
    option_reisen = 9
    option_remilia = 10
    option_sakuya = 11
    option_sanae = 12
    option_suika = 13
    option_suwako = 14
    option_tenshi = 15
    option_utsuho = 16
    option_youmu = 17
    option_yukari = 18
    option_yuyuko = 19

class CharacterFullBlacklist(OptionSet):
    """
    DeterminesWhich Characters will be autofilled into all Character 
    Blacklist settings

    Characters listed will have no checks or items associated with 
    playing as them (In Arcade or VS Modes)

    (except for story mode Sanae, Cirno, and Meiling specifically. If 
    they are listed in this blacklist, they will still be exempt from 
    other settings)
    """
    display_name = "Character Full Blacklist"
    valid_keys = [
        "Reimu", 
        "Marisa", 
        "Sanae", 
        "Alice", 
        "Aya", 
        "Cirno", 
        "Iku", 
        "Komachi", 
        "Meiling", 
        "Patchouli", 
        "Reisen", 
        "Remilia", 
        "Sakuya", 
        "Suika", 
        "Suwako", 
        "Tenshi", 
        "Utsuho", 
        "Youmu", 
        "Yuyuko", 
        "Yukari"
        ]
    default = []

#VS Mode Options
class VSModeCharacterwins(Choice):
    """    
    Determines whether playing in VS Mode and winning AS and/or AGAINST 
    a given character
    example: Winning playing AGAINST Cirno once rewards a check (if "Opponent" 
    is chosen), as does winning playing AS Cirno (If "Player" is chosen)

    Note: These checks can also be gotten during Arcade Mode as long as 
    you have recieved the character associated with the check. In VS Mode, 
    you can only play as or against characters you already have recieved.
    """
    display_name = "VS Mode Checks"
    default = 0
    option_none = 0
    option_opponent = 1
    option_player = 2
    option_both = 3

class VSModeCount(Range):
    """
    Determine how many checks exist for winning as/against given characters 
    in VS Mode, from 1 to 10.
    """
    display_name = "VS Mode Win Count"
    range_start = 1
    range_end = 10


#Story Mode Options
class StoryModeChecks(OptionSet):
    """
    Determines which Story Modes will have checks behind completing 
    individual stages, as well as whether those stages will be split 
    up by "Progressive Story Stage" items.

    Only includes "Sanae", "Meiling", and "Cirno"
    """
    
    display_name = "Story Mode Checks"
    valid_keys = ["Sanae", "Meiling", "Cirno"]
    default = []


class StoryStageUnlocks(Choice):
    """
    Determines whether Story Mode stage unlock items will unlock 
    stages per individual character, or unlock the next stage for 
    each character
    """
    display_name = "Story Stage Unlocks"
    default = 0
    option_individual = 0
    option_universal = 1


#Arcade Mode Options
class ArcadeModeChecks(Toggle):
    """
    Determines whether each character will have checks for Arcade mode, 
    as well as locking different stages of Arcade Mode for each 
    character behind "Progressive Arcade Stage" items
    """

    display_name = "Arcade Mode Checks"
    default = True

class IndividualArcadeUnlocks(Choice):
    """
    Determines whether Arcade Mode stage unlocks will be per character, 
    or apply for all characters.

    True=Individual Unlocks
    False=Universal Unlocks
    """
    display_name = "Individual Arcade Unlocks"
    default = 1
    option_individual = 0
    option_universal = 1

class ArcadeBlacklist(OptionSet):
    """
    Determine which characters to exclude from having to do Arcade Mode 
    with. These characters will not have checks associated with Arcade 
    Mode.
    
    Example, "["Reimu", "Utsuho", "Meiling"]"
    """
    display_name = "Arcade Mode Blacklist"
    valid_keys = [
        "Reimu", 
        "Marisa", 
        "Sanae", 
        "Alice", 
        "Aya", 
        "Cirno", 
        "Iku", 
        "Komachi", 
        "Meiling", 
        "Patchouli", 
        "Reisen", 
        "Remilia", 
        "Sakuya", 
        "Suika", 
        "Suwako", 
        "Tenshi", 
        "Utsuho", 
        "Youmu", 
        "Yuyuko", 
        "Yukari"
        ]
    default = []

#Card Options

class CardsanitySkills(Choice):
    """
    Determines whether using Skill Cards (up to a given level) 
    in a game rewards a check. If enabled, Shuffles all characters' 
    Special Cards into the item pool.
    
    - Off: Using Skill Cards to level your Skills will not award 
    any checks.
    - Once: Skill cards only need to be used once in a game to reward 
    the check.
    - Max: Ranking up a character's Skill card to Rank 4 rewards a check.
    - Individual: Same as Max, but each level up to max also sends a 
    check, amounting to 4 checks per special.

    Importantly, These checks can be gotten while playing Arcade Mode, 
    Story Mode, VS Com, or VS Player. (VS Network reading TBD)

    Warning: This setting will add about 200+ checks associated with 
    each Special Card, Individual however multiplies this by 4. Enable
    with discretion.
    """
    display_name = "Cardsanity Skills"
    default = 0
    option_off = 0
    option_once = 1
    option_max = 2
    option_individual = 3
    
class CardsanitySpells(Toggle):
    """
    Determines whether activating specific Spell Cards in a game
    awards checks, And shuffles all characters' Spell Cards into the item pool.

    Importantly, These checks can be gotten while playing Arcade Mode, 
    Story Mode, VS Com, or VS Player.
    """
    display_name = "Cardsanity Spells"
    default = False

class CardsanitySpellCount(Range):
    """
    Determines how many times using a given Spell card will reward a 
    check, from 1 to 4.

    Warning: This setting will add about 200+ checks to the pool times 
    this value, so at max can get quite close to 900. Enable with discretion.
    """
    display_name = "Cardsanity Spell Count"
    range_start = 1
    range_end = 4

class CardsanityStartCards(Range):
    """
    If either Cardsanity setting is enabled, determines how 
    many of their cards each character starts with when you 
    recieve them, from 0 to 27.

    (Characters with less cards in the pool than the amount 
    listed will simply start with all available cards)
    """
    display_name = "Cardsanity Starting Cards"
    default = 0
    range_start = 0
    range_end = 27

class CardsanityBlacklist(OptionSet):
    """
    Determines which characters to exclude from Cardsanity settings.

    Characters listed will not have checks or items associated 
    with using cards.

    Example, "["Reimu", "Utsuho", "Meiling"]"
    """
    display_name = "Cardsanity Blacklist"
    valid_keys = [
        "Reimu", 
        "Marisa", 
        "Sanae", 
        "Alice", 
        "Aya", 
        "Cirno", 
        "Iku", 
        "Komachi", 
        "Meiling", 
        "Patchouli", 
        "Reisen", 
        "Remilia", 
        "Sakuya", 
        "Suika", 
        "Suwako", 
        "Tenshi", 
        "Utsuho", 
        "Youmu", 
        "Yuyuko", 
        "Yukari"
        ]
    default = []

class SystemCardCheckCount(Range):
    """
    Determines whether using a System Card a number of times rewards 
    a check. These are all availabe from the start
    """
    display_name = "System Card Check Count"
    default = 0
    range_start = 0
    range_end = 10

class SystemCardCharacterChecks(Choice):
    """
    Determines whether checks for using system cards is handled 
    per character, or universally.
    """
    display_name = "System Card Character Checks"
    default = 0
    option_universal = 0
    option_individual = 1

#Difficulty Settings

class DifficultyItems(Choice):
    """
    Determines whether Story/Arcade difficulty's will be locked 
    behind "Progressive Difficulty" checks

    - Open: All difficulties are available from the start.
    - Seperate: You start with one random/selected difficulty, 
    and the others are individual AP Items.
    - From Lunatic: Start with Lunatic, and "Progressive Difficulty" 
    items give you the next lowest difficulty
    - From Easy: Start with Easy, and "Progressive Difficulty" items 
    give you the next highest difficulty
    """
    display_name = "Difficulty Items"
    default = 0
    option_open = 0
    option_seperate = 1
    option_from_lunatic = 2
    option_from_easy = 3

class DifficultyStart(Choice):
    """
    Determines Which difficulty to start with if "Difficuly Items" is 
    set to "Seperate".
    """
    display_name = "Difficulty Start"
    default = "random"
    option_easy = 0
    option_medium = 1
    option_hard = 2
    option_lunatic = 3

class ExcludeLunatic(Toggle):
    """
    Determines whether Lunatic will be excluded from progressive difficulty. 

    If difficulty unlocks are progressive "From Lunatic", or set to "Seperate" 
    and you start with "Lunatic", you will also be given "Hard" if excluded
    """
    display_name = "Exclude Lunatic"
    default = True

class OnlyLunatic(Toggle):
    """
    All other difficulties will be disabled, and Lunatic will be the only 
    available difficulty.

    Enable at your own discretion
    """
    display_name = "Only Lunatic"
    default = False

# Misc Settings
class Traps(Range):
    """
    Determines what percentage of filer items get relaced with traps 
    for you.
    """
    display_name = "Traps"
    default = 0
    range_start = 0
    range_end = 100

class NoDeckLimit(Choice):
    """
    Determines whether the standard limit of 4 duplicates of a card in a deck 
    is in place.

    - Vanilla: The card limit of 4 is as normal.
    - Item: The card limit will be normal from the start, but recieve an item 
    that can unlimit cards in a characters deck.
    - Always: Decks will be allowed any number of cards you own.
    """


class Deathlink(Deathlink):
    """
    When you lose in Arcade Mode or Story Mode, everyone else with 
    deathlink enabled also dies in theirs. Of course, the reverse is 
    true as well.

    When you recieve a deathlink from another player, a round will 
    be immediately lost with your HP dropped to 0.
    """
    display_name = "Deathlink"
    default = False
    
class DeathlinkTrigger(Choice):
    """
    Determines what kind of loss sends a deathlink

    - Round Loss: when your HP drops to 0 and you become downed, send 
    a deathlink
    - Match Loss: Only send a deathlink when you lose a whole match 
    (best of 2 in Arcade Mode, and losing all 3 lives in Story Mode, 
    for context)
    """
    display_name = "Deathlink Trigger"
    default = 0
    option_round_loss = 0
    option_match_loss = 1

@dataclass
class SokuOptions(PerGameCommonOptions):
    # Goal Options
    goal: Goal
    story_mode_count: StoryModeCount
    arcade_mode_count: ArcadeModeCount
    card_collector_count: CardCollectorCount
    card_master_count: CardMasterCount

    #General Options
    starting_character: StartingCharacter
    character_full_blacklist: CharacterFullBlacklist

    # VS Mode Options
    vs_mode_character_wins: VSModeCharacterwins
    vs_mode_win_count: VSModeCount

    # Story Mode Options
    story_mode_checks: StoryModeChecks
    story_stage_unlocks: StoryStageUnlocks

    # Arcade Mode Options
    arcade_mode_checks: ArcadeModeChecks
    arcade_stage_unlocks: IndividualArcadeUnlocks
    arcade_mode_blacklist: ArcadeBlacklist

    # Card Options
    cardsanity_skills: CardsanitySkills
    cardsanity_spells: CardsanitySpells
    cardsanity_spell_count: CardsanitySpellCount
    cardsanity_starting_cards: CardsanityStartCards
    cardsanity_blacklist: CardsanityBlacklist
    system_card_check_count: SystemCardCheckCount
    system_card_character_checks: SystemCardCharacterChecks

    # Difficulty Options
    difficulty_items: DifficultyItems
    difficulty_start: DifficultyStart
    exclude_lunatic: ExcludeLunatic
    only_lunatic: OnlyLunatic

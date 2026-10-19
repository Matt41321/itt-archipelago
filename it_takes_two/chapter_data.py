from typing import NamedTuple


class Chapter(NamedTuple):
    index: int
    name: str
    group: str
    level: str
    progress_point: str
    is_minigame: bool
    minigame_id: str


CHAPTERS: list[Chapter] = [
    Chapter(0, 'Intro', 'The Shed', '/Game/Maps/RealWorld/RealWorld_House_Kitchen_Divorce_BP', 'RealWorld_House_Kitchen_Divorce', False, ''),
    Chapter(1, 'Wake-up Call', 'The Shed', '/Game/Maps/Shed/Awakening/Awakening_BP', 'Awakening_Start', False, ''),
    Chapter(2, 'Biting the Dust', 'The Shed', '/Game/Maps/Shed/Vacuum/Vacuum_BP', 'VacuumIntro', False, ''),
    Chapter(3, 'The Depths', 'The Shed', '/Game/Maps/Shed/Main/Main_Hammernails_BP', 'MineIntro', False, ''),
    Chapter(4, 'Whack-a-Cody', 'The Shed', '/Game/Maps/Shed/Main/Main_Hammernails_BP', 'WhackACody', True, 'Whack-A-Cody'),
    Chapter(5, 'Flip the Switch', 'The Shed', '/Game/Maps/Shed/Main/Main_Hammernails_BP', 'MINIGAME_NailWheel', True, 'The Nail Wheel'),
    Chapter(6, 'Wired Up', 'The Shed', '/Game/Maps/Shed/Main/Main_Grindsection_BP', 'GrindSection_Start', False, ''),
    Chapter(7, 'Fresh Air', 'The Tree', '/Game/Maps/Tree/Approach/Approach_BP', 'Tree_Approach_LevelIntro', False, ''),
    Chapter(8, 'Captured', 'The Tree', '/Game/Maps/Tree/SquirrelHome/SquirrelHome_BP_Mech', 'Entry', False, ''),
    Chapter(9, 'Tug of War', 'The Tree', '/Game/Maps/Tree/SquirrelHome/SquirrelHome_BP_Mech', 'MINIGAME_TugOfWar', True, 'Tug of War'),
    Chapter(10, 'Deeply Rooted', 'The Tree', '/Game/Maps/Tree/WaspNest/WaspsNest_BP', 'Entry', False, ''),
    Chapter(11, 'Plunger Dunger', 'The Tree', '/Game/Maps/Tree/WaspNest/WaspsNest_Elevator_BP', 'MINIGAME_Plunger', True, 'Plunger'),
    Chapter(12, 'Extermination', 'The Tree', '/Game/Maps/Tree/Boss/WaspQueenBoss_BP', 'StartWaspBossPhase1', False, ''),
    Chapter(13, 'Getaway', 'The Tree', '/Game/Maps/Tree/Escape/Escape_BP', 'Intro', False, ''),
    Chapter(14, 'Pillow Fort', "Rose's Room", '/Game/Maps/PlayRoom/PillowFort/PillowFort_BP', 'PillowFort', False, ''),
    Chapter(15, 'Tank Brothers', "Rose's Room", '/Game/Maps/PlayRoom/PillowFort/PillowFort_SideContent', 'MINIGAME_Hazeboy', True, 'Tank Brothers'),
    Chapter(16, 'Spaced Out', "Rose's Room", '/Game/Maps/PlayRoom/Spacestation/Spacestation_Hub_BP', 'SpaceStationIntro', False, ''),
    Chapter(17, 'Laser Tennis', "Rose's Room", '/Game/Maps/PlayRoom/Spacestation/SpaceStation_LaserGame_BP', 'MINIGAME_LaserTennis', True, 'Laser Tennis'),
    Chapter(18, 'Spacewalk', "Rose's Room", '/Game/Maps/PlayRoom/Spacestation/SpaceStation_LowGravity_BP', 'MINIGAME_LowGravity', True, 'Low Gravity Room'),
    Chapter(19, 'Hopscotch', "Rose's Room", '/Game/Maps/PlayRoom/Hopscotch/Hopscotch_BP', 'Intro', False, ''),
    Chapter(20, 'Batting Team', "Rose's Room", '/Game/Maps/PlayRoom/Hopscotch/Hopscotch_BP', 'MINIGAME_BaseBall', True, 'Baseball'),
    Chapter(21, 'Feed the Reptile', "Rose's Room", '/Game/Maps/PlayRoom/Hopscotch/Hopscotch_BP', 'MINIGAME_ThrowingHoops', True, 'Throwing Hoops'),
    Chapter(22, 'Rodeo', "Rose's Room", '/Game/Maps/PlayRoom/Hopscotch/Hopscotch_BP', 'MINIGAME_Rodeo', True, 'Rodeo'),
    Chapter(23, 'Train Station', "Rose's Room", '/Game/Maps/PlayRoom/Goldberg/Goldberg_Trainstation_BP', 'Trainstation_Start', False, ''),
    Chapter(24, 'Dino Land', "Rose's Room", '/Game/Maps/PlayRoom/Goldberg/Goldberg_Dinoland_BP', 'Dinoland_Start', False, ''),
    Chapter(25, 'Pirates Ahoy', "Rose's Room", '/Game/Maps/PlayRoom/Goldberg/Goldberg_Pirate_BP', 'Pirate_Part01_Start', False, ''),
    Chapter(26, 'The Greatest Show', "Rose's Room", '/Game/Maps/PlayRoom/Goldberg/Goldberg_Circus_BP', 'Circus_Start', False, ''),
    Chapter(27, 'Once Upon a Time', "Rose's Room", '/Game/Maps/PlayRoom/Courtyard/Castle_Courtyard_BP', 'Castle_Courtyard_Start', False, ''),
    Chapter(28, 'Birdstar', "Rose's Room", '/Game/Maps/PlayRoom/Courtyard/Castle_Courtyard_SideContent', 'MINIGAME_BirdStar', True, 'Birdstar'),
    Chapter(29, 'Dungeon Crawler', "Rose's Room", '/Game/Maps/PlayRoom/Dungeon/Castle_Dungeon_BP', 'Castle_Dungeon', False, ''),
    Chapter(30, 'The Queen', "Rose's Room", '/Game/Maps/PlayRoom/Shelf/Shelf_BP', 'Shelf_Cutie_Intro', False, ''),
    Chapter(31, 'Gates of Time', 'Cuckoo Clock', '/Game/Maps/Clockwork/Outside/Clockwork_Tutorial_BP', 'ClockworkIntro', False, ''),
    Chapter(32, 'Bomb Run', 'Cuckoo Clock', '/Game/Maps/Clockwork/Outside/Clockwork_Town_SideContent', 'MINIGAME_BombRun', True, 'Bomb Run'),
    Chapter(33, 'Horse Derby', 'Cuckoo Clock', '/Game/Maps/Clockwork/Outside/Clockwork_Town_SideContent', 'MINIGAME_HorseDerby', True, 'Horse Derby'),
    Chapter(34, 'Clockworks', 'Cuckoo Clock', '/Game/Maps/Clockwork/LowerTower/Clockwork_ClockTowerLower_CrushingTrapRoom_BP', 'Crusher Trap Room', False, ''),
    Chapter(35, 'A Blast from the Past', 'Cuckoo Clock', '/Game/Maps/Clockwork/UpperTower/Clockwork_ClockTowerLastBoss_BP', 'Boss Intro', False, ''),
    Chapter(36, 'Warming Up', 'Snow Globe', '/Game/Maps/SnowGlobe/Forest/SnowGlobe_Forest_BP', 'Forest Entry', False, ''),
    Chapter(37, 'Winter Village', 'Snow Globe', '/Game/Maps/SnowGlobe/Town/SnowGlobe_Town_BP', 'Town Entry', False, ''),
    Chapter(38, 'Snow Warfare', 'Snow Globe', '/Game/Maps/SnowGlobe/Town/SnowGlobe_Town_BP', 'MINIGAME_SnowballFight', True, 'Snowball Warfare'),
    Chapter(39, 'Shuffle Board', 'Snow Globe', '/Game/Maps/SnowGlobe/Town/SnowGlobe_Town_BP', 'MINIGAME_ShuffleBoard', True, 'Shuffle Board'),
    Chapter(40, 'Icicle Throwing', 'Snow Globe', '/Game/Maps/SnowGlobe/Town/SnowGlobe_Town_BP', 'MINIGAME_IcicleThrowing', True, 'Icicle Throwing'),
    Chapter(41, 'Beneath the Ice', 'Snow Globe', '/Game/Maps/SnowGlobe/Lake/Snowglobe_Lake_BP', 'Entry', False, ''),
    Chapter(42, 'Ice Race', 'Snow Globe', '/Game/Maps/SnowGlobe/Lake/Snowglobe_Lake_BP', 'MINIGAME_IceRace', True, 'Ice Race'),
    Chapter(43, 'Slippery Slopes', 'Snow Globe', '/Game/Maps/SnowGlobe/Mountain/SnowGlobe_Mountain_BP', '0. Entry', False, ''),
    Chapter(44, 'Green Fingers', 'Garden', '/Game/Maps/Garden/VegetablePatch/Garden_VegetablePatch_BP', 'Intro', False, ''),
    Chapter(45, 'Weed Whacking', 'Garden', '/Game/Maps/Garden/Shrubbery/Garden_Shrubbery_BP', 'Shrubbery_Enter', False, ''),
    Chapter(46, 'Larva Basket', 'Garden', '/Game/Maps/Garden/Shrubbery/Garden_Shrubbery_BP', 'MINIGAME_Basket', True, 'Larva Basket'),
    Chapter(47, 'Garden Swings', 'Garden', '/Game/Maps/Garden/Shrubbery/Garden_Shrubbery_BP', 'MINIGAME_Swings', True, 'Garden Swing'),
    Chapter(48, 'Trespassing', 'Garden', '/Game/Maps/Garden/MoleTunnels/Garden_MoleTunnels_Stealth_BP', 'MoleTunnels_Level_Intro', False, ''),
    Chapter(49, 'Frog Pond', 'Garden', '/Game/Maps/Garden/FrogPond/Garden_FrogPond_BP', 'Intro', False, ''),
    Chapter(50, 'Snail Race', 'Garden', '/Game/Maps/Garden/FrogPond/Garden_FrogPond_SnailRace_BP', 'Minigame_SnailRace', True, 'Snail Race'),
    Chapter(51, 'Affliction', 'Garden', '/Game/Maps/Garden/Greenhouse/Garden_Greenhouse_BP', 'Greenhouse_Intro', False, ''),
    Chapter(52, 'Setting the Stage', 'The Attic', '/Game/Maps/Music/ConcertHall/Music_ConcertHall_BP', 'ConcertHall_Backstage', False, ''),
    Chapter(53, 'Musical Chairs', 'The Attic', '/Game/Maps/Music/ConcertHall/Music_ConcertHall_BP', 'MINIGAME_MusicalChairs', True, 'Musical Chairs'),
    Chapter(54, 'Track Runner', 'The Attic', '/Game/Maps/Music/ConcertHall/Music_ConcertHall_BP', 'MINIGAME_TrackRunner', True, 'Track Runner'),
    Chapter(55, 'Slotcars', 'The Attic', '/Game/Maps/Music/ConcertHall/Music_ConcertHall_BP', 'MINIGAME_SlotCars', True, 'Slotcars'),
    Chapter(56, 'Chess', 'The Attic', '/Game/Maps/Music/ConcertHall/Music_ConcertHall_BP', 'MINIGAME_Chess', True, 'Chess'),
    Chapter(57, 'Rehearsal', 'The Attic', '/Game/Maps/Music/Backstage/Music_Backstage_Tutorial_BP', 'Tutorial_Intro', False, ''),
    Chapter(58, 'Symphony', 'The Attic', '/Game/Maps/Music/Classic/Music_Classic_Organ_BP', 'Classic_01_Attic_Intro', False, ''),
    Chapter(59, 'Volleyball', 'The Attic', '/Game/Maps/Music/Classic/Music_Classic_Ending_BP', 'MINIGAME_VolleyBall', True, 'Volleyball'),
    Chapter(60, 'Turn Up', 'The Attic', '/Game/Maps/Music/Nightclub/Music_Nightclub_BP', 'RainbowSlide', False, ''),
    Chapter(61, 'A Grand Finale', 'The Attic', '/Game/Maps/Music/Ending/Music_Ending_BP', 'EndingIntro', False, ''),
]

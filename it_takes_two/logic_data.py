# Logic node (a location name) -> its sub-chapter. A sub-chapter's first node is its start.
NODES: dict[str, str] = {
    'Intro Complete': 'Intro',
    'Wake-up Call - Cutscene': 'Wake-up Call',
    'Wake-up Call Complete': 'Wake-up Call',
    'Biting the Dust - Cutscene': 'Biting the Dust',
    'Biting the Dust - Checkpoint 1': 'Biting the Dust',
    'Biting the Dust - Checkpoint 2': 'Biting the Dust',
    'Biting the Dust - Checkpoint 3': 'Biting the Dust',
    'Biting the Dust - Checkpoint 4': 'Biting the Dust',
    'Biting the Dust - Checkpoint 5': 'Biting the Dust',
    'Biting the Dust - Checkpoint 6': 'Biting the Dust',
    'Biting the Dust - Checkpoint 7': 'Biting the Dust',
    'Biting the Dust - Checkpoint 8': 'Biting the Dust',
    'Biting the Dust - Boss Cutscene': 'Biting the Dust',
    'Biting the Dust Complete': 'Biting the Dust',
    'The Depths - Cutscene': 'The Depths',
    'The Depths - Checkpoint 1': 'The Depths',
    'The Depths - Checkpoint 2': 'The Depths',
    'The Depths - Checkpoint 3': 'The Depths',
    'The Depths - Checkpoint 4': 'The Depths',
    'The Depths - Checkpoint 5': 'The Depths',
    'The Depths - Checkpoint 6': 'The Depths',
    'The Depths - Checkpoint 7': 'The Depths',
    'The Depths - Checkpoint 8': 'The Depths',
    'The Depths - Checkpoint 9': 'The Depths',
    'The Depths - Checkpoint 10': 'The Depths',
    'The Depths - Boss Entry': 'The Depths',
    'The Depths - Checkpoint 12': 'The Depths',
    'The Depths - Checkpoint 13': 'The Depths',
    'The Depths - Checkpoint 14': 'The Depths',
    'The Depths - Checkpoint 15': 'The Depths',
    'The Depths - Boss Defeat': 'The Depths',
    'Whack-a-Cody Discovered': 'The Depths',
    'Flip the Switch Discovered': 'The Depths',
    'The Depths Complete': 'The Depths',
    'Wired Up - Entry': 'Wired Up',
    'Wired Up - Checkpoint 1': 'Wired Up',
    'Wired Up - Checkpoint 2': 'Wired Up',
    'Wired Up - Checkpoint 3': 'Wired Up',
    'Wired Up Complete': 'Wired Up',
    'Fresh Air - Cutscene': 'Fresh Air',
    'Fresh Air Complete': 'Fresh Air',
    'Captured - Cutscene': 'Captured',
    'Captured - Checkpoint 1': 'Captured',
    'Captured - Checkpoint 2': 'Captured',
    'Captured - Checkpoint 3': 'Captured',
    'Captured - Checkpoint 4': 'Captured',
    'Captured - Checkpoint 5': 'Captured',
    'Captured - Checkpoint 6': 'Captured',
    'Captured - Checkpoint 7': 'Captured',
    'Captured - Checkpoint 8': 'Captured',
    'Captured - Checkpoint 9': 'Captured',
    'Captured - Checkpoint 10': 'Captured',
    'Captured - Boss Entry': 'Captured',
    'Tug of War Discovered': 'Captured',
    'Captured Complete': 'Captured',
    'Deeply Rooted - Entry Cutscene': 'Deeply Rooted',
    'Deeply Rooted - Checkpoint 1': 'Deeply Rooted',
    'Deeply Rooted - Checkpoint 2': 'Deeply Rooted',
    'Deeply Rooted - Checkpoint 3': 'Deeply Rooted',
    'Deeply Rooted - Checkpoint 4': 'Deeply Rooted',
    'Deeply Rooted - Checkpoint 5': 'Deeply Rooted',
    'Deeply Rooted - Checkpoint 6': 'Deeply Rooted',
    'Deeply Rooted - Checkpoint 7': 'Deeply Rooted',
    'Deeply Rooted - Boat Cutscene': 'Deeply Rooted',
    'Deeply Rooted - Checkpoint 8': 'Deeply Rooted',
    'Deeply Rooted - Checkpoint 9': 'Deeply Rooted',
    'Deeply Rooted - Checkpoint 10': 'Deeply Rooted',
    'Deeply Rooted - Dark Room Cutscene': 'Deeply Rooted',
    'Deeply Rooted - Checkpoint 11': 'Deeply Rooted',
    'Deeply Rooted - Checkpoint 12': 'Deeply Rooted',
    'Deeply Rooted - Checkpoint 13': 'Deeply Rooted',
    'Deeply Rooted - Checkpoint 14': 'Deeply Rooted',
    'Deeply Rooted - Elevator Cutscene': 'Deeply Rooted',
    'Deeply Rooted - Checkpoint 15': 'Deeply Rooted',
    'Deeply Rooted - Checkpoint 16': 'Deeply Rooted',
    'Deeply Rooted - Checkpoint 17': 'Deeply Rooted',
    'Deeply Rooted - Checkpoint 18': 'Deeply Rooted',
    'Deeply Rooted - Checkpoint 19': 'Deeply Rooted',
    'Deeply Rooted - Checkpoint 20': 'Deeply Rooted',
    'Deeply Rooted - Checkpoint 21': 'Deeply Rooted',
    'Deeply Rooted - Checkpoint 22': 'Deeply Rooted',
    'Deeply Rooted - Checkpoint 23': 'Deeply Rooted',
    'Plunger Dunger Discovered': 'Deeply Rooted',
    'Deeply Rooted Complete': 'Deeply Rooted',
    'Extermination - Cutscene': 'Extermination',
    'Extermination - Phase 2': 'Extermination',
    'Extermination - Phase 3': 'Extermination',
    'Extermination Complete': 'Extermination',
    'Getaway - Entry': 'Getaway',
    'Getaway - Checkpoint 1': 'Getaway',
    'Getaway - Checkpoint 2': 'Getaway',
    'Getaway - Checkpoint 3': 'Getaway',
    'Getaway - Checkpoint 4': 'Getaway',
    'Getaway - Checkpoint 5': 'Getaway',
    'Getaway - Checkpoint 6': 'Getaway',
    'Getaway Complete': 'Getaway',
    'Pillow Fort - Cutscene': 'Pillow Fort',
    'Pillow Fort - Checkpoint 1': 'Pillow Fort',
    'Tank Brothers Discovered': 'Pillow Fort',
    'Pillow Fort Complete': 'Pillow Fort',
    'Spaced Out - Cutscene': 'Spaced Out',
    'Spaced Out - Checkpoint 1': 'Spaced Out',
    'Spaced Out - Checkpoint 2': 'Spaced Out',
    'Spaced Out - Checkpoint 3': 'Spaced Out',
    'Spaced Out - Checkpoint 4': 'Spaced Out',
    'Spaced Out - Boss Cutscene': 'Spaced Out',
    'Spaced Out - Checkpoint 5': 'Spaced Out',
    'Spaced Out - Checkpoint 6': 'Spaced Out',
    'Spaced Out - Checkpoint 7': 'Spaced Out',
    'Spaced Out - Checkpoint 8': 'Spaced Out',
    'Spaced Out - Checkpoint 9': 'Spaced Out',
    'Spaced Out - Checkpoint 10': 'Spaced Out',
    'Laser Tennis Discovered': 'Spaced Out',
    'Spacewalk Discovered': 'Spaced Out',
    'Spaced Out Complete': 'Spaced Out',
    'Hopscotch - Cutscene': 'Hopscotch',
    'Hopscotch - Checkpoint 1': 'Hopscotch',
    'Hopscotch - Checkpoint 2': 'Hopscotch',
    'Hopscotch - Checkpoint 3': 'Hopscotch',
    'Hopscotch - Checkpoint 4': 'Hopscotch',
    'Hopscotch - Checkpoint 5': 'Hopscotch',
    'Hopscotch - Checkpoint 6': 'Hopscotch',
    'Hopscotch - Checkpoint 7': 'Hopscotch',
    'Hopscotch - Checkpoint 8': 'Hopscotch',
    'Hopscotch - Checkpoint 9': 'Hopscotch',
    'Hopscotch - Checkpoint 10': 'Hopscotch',
    'Hopscotch - Checkpoint 11': 'Hopscotch',
    'Hopscotch - Checkpoint 12': 'Hopscotch',
    'Hopscotch - Checkpoint 13': 'Hopscotch',
    'Hopscotch - Checkpoint 14': 'Hopscotch',
    'Batting Team Discovered': 'Hopscotch',
    'Feed the Reptile Discovered': 'Hopscotch',
    'Rodeo Discovered': 'Hopscotch',
    'Hopscotch Complete': 'Hopscotch',
    'Train Station - Cutscene': 'Train Station',
    'Train Station Complete': 'Train Station',
    'Dino Land - Entry': 'Dino Land',
    'Dino Land - Checkpoint 1': 'Dino Land',
    'Dino Land - Checkpoint 2': 'Dino Land',
    'Dino Land - Checkpoint 3': 'Dino Land',
    'Dino Land Complete': 'Dino Land',
    'Pirates Ahoy - Cutscene': 'Pirates Ahoy',
    'Pirates Ahoy - Checkpoint 1': 'Pirates Ahoy',
    'Pirates Ahoy - Checkpoint 2': 'Pirates Ahoy',
    'Pirates Ahoy - Checkpoint 3': 'Pirates Ahoy',
    'Pirates Ahoy - Checkpoint 4': 'Pirates Ahoy',
    'Pirates Ahoy - Boss Entry': 'Pirates Ahoy',
    'Pirates Ahoy - Checkpoint 5': 'Pirates Ahoy',
    'Pirates Ahoy - Checkpoint 6': 'Pirates Ahoy',
    'Pirates Ahoy - Boss Defeat': 'Pirates Ahoy',
    'Pirates Ahoy Complete': 'Pirates Ahoy',
    'The Greatest Show - Entry': 'The Greatest Show',
    'The Greatest Show - Checkpoint 1': 'The Greatest Show',
    'The Greatest Show - Checkpoint 2': 'The Greatest Show',
    'The Greatest Show - Checkpoint 3': 'The Greatest Show',
    'The Greatest Show - Checkpoint 4': 'The Greatest Show',
    'The Greatest Show - Checkpoint 5': 'The Greatest Show',
    'The Greatest Show Complete': 'The Greatest Show',
    'Once Upon a Time - Cutscene': 'Once Upon a Time',
    'Once Upon a Time - Checkpoint 1': 'Once Upon a Time',
    'Birdstar Discovered': 'Once Upon a Time',
    'Once Upon a Time Complete': 'Once Upon a Time',
    'Dungeon Crawler - Cutscene': 'Dungeon Crawler',
    'Dungeon Crawler - Checkpoint 1': 'Dungeon Crawler',
    'Dungeon Crawler - Checkpoint 2': 'Dungeon Crawler',
    'Dungeon Crawler - Checkpoint 3': 'Dungeon Crawler',
    'Dungeon Crawler - Checkpoint 4': 'Dungeon Crawler',
    'Dungeon Crawler - Checkpoint 5': 'Dungeon Crawler',
    'Dungeon Crawler - Checkpoint 6': 'Dungeon Crawler',
    'Dungeon Crawler - Checkpoint 7': 'Dungeon Crawler',
    'Dungeon Crawler - Checkpoint 8': 'Dungeon Crawler',
    'Dungeon Crawler - Checkpoint 9': 'Dungeon Crawler',
    'Dungeon Crawler - Boss Cutscene': 'Dungeon Crawler',
    'Dungeon Crawler Complete': 'Dungeon Crawler',
    'The Queen - Cutscene': 'The Queen',
    'The Queen - Checkpoint 1': 'The Queen',
    'The Queen Complete': 'The Queen',
    'Gates of Time - Cutscene': 'Gates of Time',
    'Gates of Time - Town Cutscene': 'Gates of Time',
    'Gates of Time - Checkpoint 1': 'Gates of Time',
    'Gates of Time - Forest Cutscene': 'Gates of Time',
    'Gates of Time - Checkpoint 2': 'Gates of Time',
    'Gates of Time - Checkpoint 3': 'Gates of Time',
    'Bomb Run Discovered': 'Gates of Time',
    'Horse Derby Discovered': 'Gates of Time',
    'Gates of Time Complete': 'Gates of Time',
    'Clockworks - Cutscene': 'Clockworks',
    'Clockworks - Checkpoint 1': 'Clockworks',
    'Clockworks - Checkpoint 2': 'Clockworks',
    'Clockworks - Checkpoint 3': 'Clockworks',
    'Clockworks - Checkpoint 4': 'Clockworks',
    'Clockworks - Checkpoint 5': 'Clockworks',
    'Clockworks - Checkpoint 6': 'Clockworks',
    'Clockworks - Checkpoint 7': 'Clockworks',
    'Clockworks - Checkpoint 8': 'Clockworks',
    'Clockworks - Checkpoint 9': 'Clockworks',
    'Clockworks - Checkpoint 10': 'Clockworks',
    'Clockworks Complete': 'Clockworks',
    'A Blast from the Past - Entry': 'A Blast from the Past',
    'A Blast from the Past - Checkpoint 1': 'A Blast from the Past',
    'A Blast from the Past - Checkpoint 2': 'A Blast from the Past',
    'A Blast from the Past - Checkpoint 3': 'A Blast from the Past',
    'A Blast from the Past - Checkpoint 4': 'A Blast from the Past',
    'A Blast from the Past - Checkpoint 5': 'A Blast from the Past',
    'A Blast from the Past - Checkpoint 6': 'A Blast from the Past',
    'A Blast from the Past - Checkpoint 7': 'A Blast from the Past',
    'A Blast from the Past Complete': 'A Blast from the Past',
    'Warming Up - Entry': 'Warming Up',
    'Warming Up - Checkpoint 1': 'Warming Up',
    'Warming Up - Checkpoint 2': 'Warming Up',
    'Warming Up - Checkpoint 3': 'Warming Up',
    'Warming Up - Checkpoint 4': 'Warming Up',
    'Warming Up - Checkpoint 5': 'Warming Up',
    'Warming Up - Checkpoint 6': 'Warming Up',
    'Warming Up Complete': 'Warming Up',
    'Winter Village - Cutscene': 'Winter Village',
    'Winter Village - Checkpoint 1': 'Winter Village',
    'Winter Village - Checkpoint 2': 'Winter Village',
    'Snow Warfare Discovered': 'Winter Village',
    'Shuffle Board Discovered': 'Winter Village',
    'Icicle Throwing Discovered': 'Winter Village',
    'Winter Village Complete': 'Winter Village',
    'Beneath the Ice - Cutscene': 'Beneath the Ice',
    'Beneath the Ice - Checkpoint 1': 'Beneath the Ice',
    'Beneath the Ice - Checkpoint 2': 'Beneath the Ice',
    'Beneath the Ice - Checkpoint 3': 'Beneath the Ice',
    'Ice Race Discovered': 'Beneath the Ice',
    'Beneath the Ice Complete': 'Beneath the Ice',
    'Slippery Slopes - Cutscene': 'Slippery Slopes',
    'Slippery Slopes - Checkpoint 1': 'Slippery Slopes',
    'Slippery Slopes - Checkpoint 2': 'Slippery Slopes',
    'Slippery Slopes - Checkpoint 3': 'Slippery Slopes',
    'Slippery Slopes - Checkpoint 4': 'Slippery Slopes',
    'Slippery Slopes - Checkpoint 5': 'Slippery Slopes',
    'Slippery Slopes - Checkpoint 6': 'Slippery Slopes',
    'Slippery Slopes Complete': 'Slippery Slopes',
    'Green Fingers - Cutscene': 'Green Fingers',
    'Green Fingers - Checkpoint 1': 'Green Fingers',
    'Green Fingers - Checkpoint 2': 'Green Fingers',
    'Green Fingers - Checkpoint 3': 'Green Fingers',
    'Green Fingers - Checkpoint 4': 'Green Fingers',
    'Green Fingers - Checkpoint 5': 'Green Fingers',
    'Green Fingers Complete': 'Green Fingers',
    'Weed Whacking - Cutscene': 'Weed Whacking',
    'Weed Whacking - Checkpoint 1': 'Weed Whacking',
    'Weed Whacking - Checkpoint 2': 'Weed Whacking',
    'Weed Whacking - Checkpoint 3': 'Weed Whacking',
    'Weed Whacking - Checkpoint 4': 'Weed Whacking',
    'Weed Whacking - Checkpoint 5': 'Weed Whacking',
    'Weed Whacking - Checkpoint 6': 'Weed Whacking',
    'Weed Whacking - Checkpoint 7': 'Weed Whacking',
    'Weed Whacking - Checkpoint 8': 'Weed Whacking',
    'Weed Whacking - Checkpoint 9': 'Weed Whacking',
    'Weed Whacking - Checkpoint 10': 'Weed Whacking',
    'Weed Whacking - Checkpoint 11': 'Weed Whacking',
    'Weed Whacking - Checkpoint 12': 'Weed Whacking',
    'Larva Basket Discovered': 'Weed Whacking',
    'Garden Swings Discovered': 'Weed Whacking',
    'Weed Whacking Complete': 'Weed Whacking',
    'Trespassing - Cutscene': 'Trespassing',
    'Trespassing - Checkpoint 1': 'Trespassing',
    'Trespassing - Checkpoint 2': 'Trespassing',
    'Trespassing - Checkpoint 3': 'Trespassing',
    'Trespassing - Checkpoint 4': 'Trespassing',
    'Trespassing - Checkpoint 5': 'Trespassing',
    'Trespassing - Checkpoint 6': 'Trespassing',
    'Trespassing - Checkpoint 7': 'Trespassing',
    'Trespassing - Checkpoint 8': 'Trespassing',
    'Trespassing - Checkpoint 9': 'Trespassing',
    'Trespassing - Checkpoint 10': 'Trespassing',
    'Trespassing Complete': 'Trespassing',
    'Frog Pond - Cutscene': 'Frog Pond',
    'Frog Pond - Checkpoint 1': 'Frog Pond',
    'Frog Pond - Checkpoint 2': 'Frog Pond',
    'Frog Pond - Checkpoint 3': 'Frog Pond',
    'Frog Pond - Checkpoint 4': 'Frog Pond',
    'Frog Pond - Checkpoint 5': 'Frog Pond',
    'Frog Pond - Checkpoint 6': 'Frog Pond',
    'Frog Pond - Checkpoint 7': 'Frog Pond',
    'Frog Pond - Checkpoint 8': 'Frog Pond',
    'Frog Pond - Checkpoint 9': 'Frog Pond',
    'Snail Race Discovered': 'Frog Pond',
    'Frog Pond Complete': 'Frog Pond',
    'Affliction - Cutscene': 'Affliction',
    'Affliction - Checkpoint 1': 'Affliction',
    'Affliction - Joy Cutscene': 'Affliction',
    'Affliction - Checkpoint 2': 'Affliction',
    'Affliction - Checkpoint 3': 'Affliction',
    'Affliction - Checkpoint 4': 'Affliction',
    'Affliction - Checkpoint 5': 'Affliction',
    'Affliction - Checkpoint 6': 'Affliction',
    'Affliction - Checkpoint 7': 'Affliction',
    'Affliction Complete': 'Affliction',
    'Setting the Stage - Cutscene': 'Setting the Stage',
    'Musical Chairs Discovered': 'Setting the Stage',
    'Track Runner Discovered': 'Setting the Stage',
    'Slotcars Discovered': 'Setting the Stage',
    'Chess Discovered': 'Setting the Stage',
    'Setting the Stage Complete': 'Setting the Stage',
    'Rehearsal - Cutscene': 'Rehearsal',
    'Rehearsal - Checkpoint 1': 'Rehearsal',
    'Rehearsal - Checkpoint 2': 'Rehearsal',
    'Rehearsal - Checkpoint 3': 'Rehearsal',
    'Rehearsal - Checkpoint 4': 'Rehearsal',
    'Rehearsal - Checkpoint 5': 'Rehearsal',
    'Rehearsal - Checkpoint 6': 'Rehearsal',
    'Rehearsal - Checkpoint 7': 'Rehearsal',
    'Rehearsal - Checkpoint 8': 'Rehearsal',
    'Rehearsal - Checkpoint 9': 'Rehearsal',
    'Rehearsal - Checkpoint 10': 'Rehearsal',
    'Rehearsal - Checkpoint 11': 'Rehearsal',
    'Rehearsal - Checkpoint 12': 'Rehearsal',
    'Rehearsal - Checkpoint 13': 'Rehearsal',
    'Rehearsal - Checkpoint 14': 'Rehearsal',
    'Rehearsal - Checkpoint 15': 'Rehearsal',
    'Rehearsal - Checkpoint 16': 'Rehearsal',
    'Rehearsal - Checkpoint 17': 'Rehearsal',
    'Rehearsal - Stage Cutscene': 'Rehearsal',
    'Rehearsal - Checkpoint 18': 'Rehearsal',
    'Rehearsal Complete': 'Rehearsal',
    'Symphony - Cutscene': 'Symphony',
    'Symphony - Checkpoint 1': 'Symphony',
    'Symphony - Checkpoint 2': 'Symphony',
    'Symphony - Checkpoint 3': 'Symphony',
    'Symphony - Checkpoint 4': 'Symphony',
    'Symphony - Checkpoint 5': 'Symphony',
    'Symphony - Checkpoint 6': 'Symphony',
    'Symphony - Checkpoint 7': 'Symphony',
    'Symphony - Stage Cutscene': 'Symphony',
    'Symphony - Checkpoint 8': 'Symphony',
    'Volleyball Discovered': 'Symphony',
    'Symphony Complete': 'Symphony',
    'Turn Up - Cutscene': 'Turn Up',
    'Turn Up - Checkpoint 1': 'Turn Up',
    'Turn Up - Checkpoint 2': 'Turn Up',
    'Turn Up - Checkpoint 3': 'Turn Up',
    'Turn Up - Checkpoint 4': 'Turn Up',
    'Turn Up - Checkpoint 5': 'Turn Up',
    'Turn Up - Checkpoint 6': 'Turn Up',
    'Turn Up - Checkpoint 7': 'Turn Up',
    'Turn Up Complete': 'Turn Up',
}

# Node -> the ways in: (source node, or None for starting the sub-chapter from chapter select, items needed).
ENTRANCES: dict[str, list[tuple[str | None, tuple[str, ...]]]] = {
    'Intro Complete': [
        (None, ()),
    ],
    'Wake-up Call - Cutscene': [
        (None, ()),
    ],
    'Wake-up Call Complete': [
        ('Wake-up Call - Cutscene', ()),
    ],
    'Biting the Dust - Cutscene': [
        (None, ()),
    ],
    'Biting the Dust - Checkpoint 1': [
        ('Biting the Dust - Cutscene', ()),
    ],
    'Biting the Dust - Checkpoint 2': [
        ('Biting the Dust - Cutscene', ('Dash',)),
        ('Biting the Dust - Cutscene', ('Double Jump',)),
        ('Biting the Dust - Cutscene', ('Ground Pound', 'Slide', 'Sprint')),
    ],
    'Biting the Dust - Checkpoint 3': [
        ('Biting the Dust - Cutscene', ('Dash',)),
        ('Biting the Dust - Cutscene', ('Double Jump',)),
        ('Biting the Dust - Cutscene', ('Slide', 'Sprint')),
    ],
    'Biting the Dust - Checkpoint 4': [
        ('Biting the Dust - Checkpoint 3', ('Dash',)),
        ('Biting the Dust - Checkpoint 3', ('Double Jump',)),
        ('Biting the Dust - Checkpoint 3', ('Slide', 'Sprint')),
    ],
    'Biting the Dust - Checkpoint 5': [
        ('Biting the Dust - Checkpoint 3', ('Dash',)),
        ('Biting the Dust - Checkpoint 3', ('Double Jump',)),
        ('Biting the Dust - Checkpoint 4', ('Slide', 'Sprint', 'Wall Jump')),
    ],
    'Biting the Dust - Checkpoint 6': [
        ('Biting the Dust - Checkpoint 5', ('Dash',)),
        ('Biting the Dust - Checkpoint 5', ('Double Jump', 'Ground Pound', 'Wall Jump')),
        ('Biting the Dust - Checkpoint 5', ('Ground Pound', 'Slide', 'Sprint', 'Wall Jump')),
    ],
    'Biting the Dust - Checkpoint 7': [
        ('Biting the Dust - Checkpoint 6', ('Dash',)),
        ('Biting the Dust - Checkpoint 6', ('Double Jump', 'Ground Pound', 'Wall Jump')),
        ('Biting the Dust - Checkpoint 6', ('Ground Pound', 'Slide', 'Sprint', 'Wall Jump')),
    ],
    'Biting the Dust - Checkpoint 8': [
        ('Biting the Dust - Checkpoint 7', ('Dash', 'Ground Pound')),
        ('Biting the Dust - Checkpoint 7', ('Dash', 'Slide')),
        ('Biting the Dust - Checkpoint 7', ('Dash', 'Wall Jump')),
        ('Biting the Dust - Checkpoint 7', ('Double Jump', 'Ground Pound', 'Wall Jump')),
        ('Biting the Dust - Checkpoint 7', ('Ground Pound', 'Slide', 'Sprint', 'Wall Jump')),
    ],
    'Biting the Dust - Boss Cutscene': [
        ('Biting the Dust - Checkpoint 8', ('Dash', 'Ground Pound')),
        ('Biting the Dust - Checkpoint 8', ('Dash', 'Slide')),
        ('Biting the Dust - Checkpoint 8', ('Dash', 'Wall Jump')),
        ('Biting the Dust - Checkpoint 8', ('Double Jump', 'Ground Pound', 'Wall Jump')),
        ('Biting the Dust - Checkpoint 8', ('Ground Pound', 'Slide', 'Sprint', 'Wall Jump')),
    ],
    'Biting the Dust Complete': [
        ('Biting the Dust - Boss Cutscene', ('Dash', 'Ground Pound')),
        ('Biting the Dust - Boss Cutscene', ('Dash', 'Slide')),
        ('Biting the Dust - Boss Cutscene', ('Dash', 'Wall Jump')),
        ('Biting the Dust - Boss Cutscene', ('Double Jump', 'Ground Pound', 'Wall Jump')),
        ('Biting the Dust - Boss Cutscene', ('Ground Pound', 'Slide', 'Sprint', 'Wall Jump')),
    ],
    'The Depths - Cutscene': [
        (None, ()),
    ],
    'The Depths - Checkpoint 1': [
        ('The Depths - Cutscene', ('Dash',)),
        ('The Depths - Cutscene', ('Double Jump',)),
        ('The Depths - Cutscene', ('Slide', 'Sprint')),
        ('The Depths - Cutscene', ('Slide', 'Wall Jump')),
        ('The Depths - Cutscene', ('Ledge Grab', 'Slide')),
    ],
    'The Depths - Checkpoint 2': [
        ('The Depths - Cutscene', ('Dash',)),
        ('The Depths - Cutscene', ('Double Jump',)),
        ('The Depths - Checkpoint 1', ('Shed Cody Ability', 'Shed May Ability', 'Slide', 'Sprint')),
    ],
    'The Depths - Checkpoint 3': [
        ('The Depths - Cutscene', ('Dash',)),
        ('The Depths - Cutscene', ('Double Jump',)),
    ],
    'The Depths - Checkpoint 4': [
        ('The Depths - Cutscene', ('Dash', 'Shed Cody Ability', 'Shed May Ability')),
        ('The Depths - Checkpoint 3', ('Double Jump', 'Shed Cody Ability', 'Shed May Ability', 'Wall Jump')),
        ('The Depths - Checkpoint 3', ('Double Jump', 'Ledge Grab', 'Shed Cody Ability', 'Shed May Ability')),
    ],
    'The Depths - Checkpoint 5': [
        ('The Depths - Checkpoint 4', ('Dash', 'Shed Cody Ability', 'Shed May Ability')),
        ('The Depths - Checkpoint 4', ('Dash', 'Shed Cody Ability', 'Slide')),
        ('The Depths - Checkpoint 4', ('Double Jump', 'Shed Cody Ability', 'Shed May Ability', 'Wall Jump')),
        ('The Depths - Checkpoint 4', ('Double Jump', 'Ledge Grab', 'Shed Cody Ability', 'Shed May Ability')),
    ],
    'The Depths - Checkpoint 6': [
        ('The Depths - Checkpoint 5', ('Dash', 'Shed Cody Ability', 'Shed May Ability')),
        ('The Depths - Checkpoint 5', ('Dash', 'Shed Cody Ability', 'Slide')),
        ('The Depths - Checkpoint 5', ('Double Jump', 'Shed Cody Ability', 'Shed May Ability', 'Wall Jump')),
        ('The Depths - Checkpoint 5', ('Double Jump', 'Ledge Grab', 'Shed Cody Ability', 'Shed May Ability')),
    ],
    'The Depths - Checkpoint 7': [
        ('The Depths - Checkpoint 6', ('Dash', 'Shed Cody Ability', 'Shed May Ability')),
        ('The Depths - Checkpoint 6', ('Dash', 'Shed Cody Ability', 'Slide')),
        ('The Depths - Checkpoint 6', ('Double Jump', 'Shed Cody Ability', 'Shed May Ability', 'Wall Jump')),
        ('The Depths - Checkpoint 6', ('Double Jump', 'Ledge Grab', 'Shed Cody Ability', 'Shed May Ability')),
    ],
    'The Depths - Checkpoint 8': [
        ('The Depths - Checkpoint 7', ('Dash', 'Shed Cody Ability', 'Shed May Ability')),
        ('The Depths - Checkpoint 7', ('Double Jump', 'Shed Cody Ability', 'Shed May Ability', 'Wall Jump')),
        ('The Depths - Checkpoint 7', ('Double Jump', 'Ledge Grab', 'Shed Cody Ability', 'Shed May Ability')),
    ],
    'The Depths - Checkpoint 9': [
        ('The Depths - Cutscene', ('Double Jump',)),
        ('The Depths - Checkpoint 10', ('Double Jump',)),
        ('The Depths - Cutscene', ('Dash',)),
        ('The Depths - Checkpoint 10', ('Dash',)),
    ],
    'The Depths - Checkpoint 10': [
        ('The Depths - Cutscene', ('Double Jump',)),
        ('The Depths - Cutscene', ('Dash',)),
    ],
    'The Depths - Boss Entry': [
        ('The Depths - Cutscene', ('Double Jump',)),
        ('The Depths - Cutscene', ('Dash',)),
    ],
    'The Depths - Checkpoint 12': [
        ('The Depths - Boss Entry', ('Double Jump', 'Shed Cody Ability')),
        ('The Depths - Boss Entry', ('Dash', 'Shed Cody Ability')),
    ],
    'The Depths - Checkpoint 13': [
        ('The Depths - Checkpoint 12', ('Double Jump', 'Shed Cody Ability', 'Shed May Ability')),
        ('The Depths - Checkpoint 12', ('Dash', 'Shed Cody Ability', 'Shed May Ability')),
    ],
    'The Depths - Checkpoint 14': [
        ('The Depths - Checkpoint 13', ('Double Jump', 'Shed Cody Ability', 'Shed May Ability')),
        ('The Depths - Checkpoint 13', ('Dash', 'Shed Cody Ability', 'Shed May Ability')),
    ],
    'The Depths - Checkpoint 15': [
        ('The Depths - Checkpoint 14', ('Double Jump', 'Shed Cody Ability', 'Shed May Ability')),
        ('The Depths - Checkpoint 14', ('Dash', 'Shed Cody Ability', 'Shed May Ability')),
    ],
    'The Depths - Boss Defeat': [
        ('The Depths - Checkpoint 10', ('Dash', 'Shed Cody Ability')),
        ('The Depths - Checkpoint 10', ('Double Jump', 'Shed Cody Ability')),
    ],
    'Whack-a-Cody Discovered': [
        ('The Depths - Cutscene', ('Dash', 'Shed May Ability')),
        ('The Depths - Cutscene', ('Dash', 'Slide')),
        ('The Depths - Checkpoint 5', ('Double Jump', 'Shed Cody Ability', 'Shed May Ability', 'Wall Jump')),
        ('The Depths - Checkpoint 5', ('Double Jump', 'Ledge Grab', 'Shed Cody Ability', 'Shed May Ability')),
    ],
    'Flip the Switch Discovered': [
        ('The Depths - Cutscene', ('Dash', 'Shed Cody Ability', 'Shed May Ability')),
        ('The Depths - Cutscene', ('Dash', 'Shed Cody Ability', 'Slide')),
        ('The Depths - Checkpoint 7', ('Double Jump', 'Shed Cody Ability', 'Shed May Ability', 'Wall Jump')),
        ('The Depths - Checkpoint 7', ('Double Jump', 'Ledge Grab', 'Shed Cody Ability', 'Shed May Ability')),
    ],
    'The Depths Complete': [
        ('The Depths - Cutscene', ('Dash', 'Shed Cody Ability')),
        ('The Depths - Cutscene', ('Double Jump', 'Shed Cody Ability')),
    ],
    'Wired Up - Entry': [
        (None, ()),
    ],
    'Wired Up - Checkpoint 1': [
        ('Wired Up - Entry', ()),
    ],
    'Wired Up - Checkpoint 2': [
        ('Wired Up - Checkpoint 1', ()),
    ],
    'Wired Up - Checkpoint 3': [
        ('Wired Up - Checkpoint 2', ()),
    ],
    'Wired Up Complete': [
        ('Wired Up - Checkpoint 3', ('Ground Pound',)),
    ],
    'Fresh Air - Cutscene': [
        (None, ()),
    ],
    'Fresh Air Complete': [
        ('Fresh Air - Cutscene', ('Swinging', 'Wall Jump')),
        ('Fresh Air - Cutscene', ('Dash', 'Double Jump', 'Ground Pound', 'Slide')),
        ('Fresh Air - Cutscene', ('Dash', 'Double Jump', 'Slide', 'Swinging')),
    ],
    'Captured - Cutscene': [
        (None, ()),
    ],
    'Captured - Checkpoint 1': [
        ('Captured - Cutscene', ('Tree Cody Ability', 'Tree May Ability')),
    ],
    'Captured - Checkpoint 2': [
        ('Captured - Checkpoint 1', ('Dash', 'Tree Cody Ability', 'Tree May Ability')),
        ('Captured - Checkpoint 1', ('Double Jump', 'Tree Cody Ability', 'Tree May Ability')),
    ],
    'Captured - Checkpoint 3': [
        ('Captured - Checkpoint 2', ('Dash', 'Double Jump', 'Tree Cody Ability', 'Tree May Ability')),
        ('Captured - Checkpoint 2', ('Ground Pound', 'Swinging', 'Tree Cody Ability', 'Tree May Ability')),
        ('Captured - Checkpoint 2', ('Double Jump', 'Swinging', 'Tree Cody Ability', 'Tree May Ability')),
    ],
    'Captured - Checkpoint 4': [
        ('Captured - Checkpoint 3', ('Dash', 'Double Jump', 'Tree Cody Ability', 'Tree May Ability')),
        ('Captured - Checkpoint 3', ('Ground Pound', 'Swinging', 'Tree Cody Ability', 'Tree May Ability')),
        ('Captured - Checkpoint 3', ('Double Jump', 'Swinging', 'Tree Cody Ability', 'Tree May Ability')),
    ],
    'Captured - Checkpoint 5': [
        ('Captured - Checkpoint 4', ('Dash', 'Double Jump', 'Tree Cody Ability', 'Tree May Ability')),
        ('Captured - Checkpoint 4', ('Ground Pound', 'Swinging', 'Tree Cody Ability', 'Tree May Ability')),
        ('Captured - Checkpoint 4', ('Double Jump', 'Swinging', 'Tree Cody Ability', 'Tree May Ability')),
    ],
    'Captured - Checkpoint 6': [
        ('Captured - Checkpoint 5', ('Dash', 'Double Jump', 'Tree Cody Ability', 'Tree May Ability')),
        ('Captured - Checkpoint 5', ('Ground Pound', 'Swinging', 'Tree Cody Ability', 'Tree May Ability')),
        ('Captured - Checkpoint 5', ('Double Jump', 'Swinging', 'Tree Cody Ability', 'Tree May Ability')),
    ],
    'Captured - Checkpoint 7': [
        ('Captured - Checkpoint 6', ('Dash', 'Double Jump', 'Tree Cody Ability', 'Tree May Ability')),
        ('Captured - Checkpoint 6', ('Ground Pound', 'Swinging', 'Tree Cody Ability', 'Tree May Ability')),
        ('Captured - Checkpoint 6', ('Double Jump', 'Swinging', 'Tree Cody Ability', 'Tree May Ability')),
    ],
    'Captured - Checkpoint 8': [
        ('Captured - Checkpoint 7', ('Dash', 'Double Jump', 'Tree Cody Ability', 'Tree May Ability')),
        ('Captured - Checkpoint 7', ('Ground Pound', 'Swinging', 'Tree Cody Ability', 'Tree May Ability')),
        ('Captured - Checkpoint 7', ('Double Jump', 'Swinging', 'Tree Cody Ability', 'Tree May Ability')),
    ],
    'Captured - Checkpoint 9': [
        ('Captured - Checkpoint 8', ('Dash', 'Double Jump', 'Tree Cody Ability', 'Tree May Ability')),
        ('Captured - Checkpoint 8', ('Grinding', 'Ground Pound', 'Swinging', 'Tree Cody Ability', 'Tree May Ability')),
        ('Captured - Checkpoint 8', ('Double Jump', 'Grinding', 'Swinging', 'Tree Cody Ability', 'Tree May Ability')),
    ],
    'Captured - Checkpoint 10': [
        ('Captured - Checkpoint 9', ('Dash', 'Double Jump', 'Tree Cody Ability', 'Tree May Ability')),
        ('Captured - Checkpoint 9', ('Grinding', 'Ground Pound', 'Swinging', 'Tree Cody Ability', 'Tree May Ability')),
        ('Captured - Checkpoint 9', ('Double Jump', 'Grinding', 'Swinging', 'Tree Cody Ability', 'Tree May Ability')),
    ],
    'Captured - Boss Entry': [
        ('Captured - Checkpoint 10', ('Dash', 'Double Jump', 'Tree Cody Ability', 'Tree May Ability')),
        ('Captured - Checkpoint 10', ('Grinding', 'Ground Pound', 'Swinging', 'Tree Cody Ability', 'Tree May Ability')),
        ('Captured - Checkpoint 10', ('Double Jump', 'Grinding', 'Swinging', 'Tree Cody Ability', 'Tree May Ability')),
    ],
    'Tug of War Discovered': [
        ('Captured - Checkpoint 8', ('Dash', 'Double Jump', 'Tree Cody Ability', 'Tree May Ability')),
        ('Captured - Checkpoint 4', ('Dash', 'Double Jump', 'Tree Cody Ability', 'Tree May Ability')),
        ('Captured - Checkpoint 8', ('Ground Pound', 'Swinging', 'Tree Cody Ability', 'Tree May Ability')),
        ('Captured - Checkpoint 4', ('Ground Pound', 'Swinging', 'Tree Cody Ability', 'Tree May Ability')),
        ('Captured - Checkpoint 8', ('Double Jump', 'Swinging', 'Tree Cody Ability', 'Tree May Ability')),
        ('Captured - Checkpoint 4', ('Double Jump', 'Swinging', 'Tree Cody Ability', 'Tree May Ability')),
    ],
    'Captured Complete': [
        ('Captured - Boss Entry', ('Dash', 'Double Jump', 'Tree Cody Ability', 'Tree May Ability')),
        ('Captured - Boss Entry', ('Grinding', 'Ground Pound', 'Swinging', 'Tree Cody Ability', 'Tree May Ability')),
        ('Captured - Boss Entry', ('Double Jump', 'Grinding', 'Swinging', 'Tree Cody Ability', 'Tree May Ability')),
    ],
    'Deeply Rooted - Entry Cutscene': [
        (None, ()),
    ],
    'Deeply Rooted - Checkpoint 1': [
        ('Deeply Rooted - Entry Cutscene', ('Tree Cody Ability', 'Tree May Ability')),
        ('Deeply Rooted - Entry Cutscene', ('Double Jump', 'Ground Pound', 'Slide')),
        ('Deeply Rooted - Entry Cutscene', ('Dash', 'Double Jump', 'Slide')),
    ],
    'Deeply Rooted - Checkpoint 2': [
        ('Deeply Rooted - Checkpoint 1', ('Dash', 'Tree Cody Ability', 'Tree May Ability')),
        ('Deeply Rooted - Checkpoint 1', ('Double Jump', 'Tree Cody Ability', 'Tree May Ability')),
        ('Deeply Rooted - Checkpoint 1', ('Double Jump', 'Ground Pound', 'Slide')),
        ('Deeply Rooted - Checkpoint 1', ('Dash', 'Double Jump', 'Slide')),
    ],
    'Deeply Rooted - Checkpoint 3': [
        ('Deeply Rooted - Checkpoint 2', ('Dash', 'Tree Cody Ability', 'Tree May Ability')),
        ('Deeply Rooted - Checkpoint 2', ('Double Jump', 'Tree Cody Ability', 'Tree May Ability')),
        ('Deeply Rooted - Checkpoint 2', ('Double Jump', 'Ground Pound', 'Slide')),
        ('Deeply Rooted - Checkpoint 2', ('Dash', 'Double Jump', 'Slide')),
    ],
    'Deeply Rooted - Checkpoint 4': [
        ('Deeply Rooted - Checkpoint 3', ('Dash', 'Tree Cody Ability', 'Tree May Ability')),
        ('Deeply Rooted - Checkpoint 3', ('Double Jump', 'Tree Cody Ability', 'Tree May Ability')),
        ('Deeply Rooted - Checkpoint 3', ('Double Jump', 'Ground Pound', 'Slide', 'Tree Cody Ability', 'Tree May Ability')),
        ('Deeply Rooted - Checkpoint 3', ('Dash', 'Double Jump', 'Slide', 'Tree Cody Ability', 'Tree May Ability')),
    ],
    'Deeply Rooted - Checkpoint 5': [
        ('Deeply Rooted - Checkpoint 4', ('Dash', 'Tree Cody Ability', 'Tree May Ability')),
        ('Deeply Rooted - Checkpoint 4', ('Double Jump', 'Tree Cody Ability', 'Tree May Ability')),
        ('Deeply Rooted - Checkpoint 4', ('Double Jump', 'Ground Pound', 'Slide', 'Tree Cody Ability', 'Tree May Ability')),
        ('Deeply Rooted - Checkpoint 4', ('Dash', 'Double Jump', 'Slide', 'Tree Cody Ability', 'Tree May Ability')),
    ],
    'Deeply Rooted - Checkpoint 6': [
        ('Deeply Rooted - Checkpoint 5', ('Dash', 'Tree Cody Ability', 'Tree May Ability')),
        ('Deeply Rooted - Checkpoint 5', ('Double Jump', 'Tree Cody Ability', 'Tree May Ability')),
        ('Deeply Rooted - Checkpoint 5', ('Double Jump', 'Ground Pound', 'Slide', 'Tree Cody Ability', 'Tree May Ability')),
        ('Deeply Rooted - Checkpoint 5', ('Dash', 'Double Jump', 'Slide', 'Tree Cody Ability', 'Tree May Ability')),
    ],
    'Deeply Rooted - Checkpoint 7': [
        ('Deeply Rooted - Checkpoint 6', ('Dash', 'Tree Cody Ability', 'Tree May Ability')),
        ('Deeply Rooted - Checkpoint 6', ('Double Jump', 'Tree Cody Ability', 'Tree May Ability')),
        ('Deeply Rooted - Checkpoint 6', ('Double Jump', 'Ground Pound', 'Slide', 'Tree Cody Ability', 'Tree May Ability')),
        ('Deeply Rooted - Checkpoint 6', ('Dash', 'Double Jump', 'Slide', 'Tree Cody Ability', 'Tree May Ability')),
    ],
    'Deeply Rooted - Boat Cutscene': [
        ('Deeply Rooted - Entry Cutscene', ('Tree Cody Ability', 'Tree May Ability')),
        ('Deeply Rooted - Entry Cutscene', ('Double Jump', 'Ground Pound', 'Slide')),
        ('Deeply Rooted - Entry Cutscene', ('Dash', 'Double Jump', 'Slide')),
    ],
    'Deeply Rooted - Checkpoint 8': [
        ('Deeply Rooted - Boat Cutscene', ('Tree Cody Ability', 'Tree May Ability')),
        ('Deeply Rooted - Boat Cutscene', ('Double Jump', 'Ground Pound', 'Slide')),
        ('Deeply Rooted - Boat Cutscene', ('Dash', 'Double Jump', 'Slide')),
    ],
    'Deeply Rooted - Checkpoint 9': [
        ('Deeply Rooted - Checkpoint 8', ('Tree Cody Ability', 'Tree May Ability')),
    ],
    'Deeply Rooted - Checkpoint 10': [
        ('Deeply Rooted - Checkpoint 9', ('Tree Cody Ability', 'Tree May Ability')),
    ],
    'Deeply Rooted - Dark Room Cutscene': [
        ('Deeply Rooted - Checkpoint 10', ('Tree Cody Ability', 'Tree May Ability')),
    ],
    'Deeply Rooted - Checkpoint 11': [
        ('Deeply Rooted - Dark Room Cutscene', ('Tree Cody Ability', 'Tree May Ability')),
    ],
    'Deeply Rooted - Checkpoint 12': [
        ('Deeply Rooted - Checkpoint 11', ('Tree Cody Ability', 'Tree May Ability')),
    ],
    'Deeply Rooted - Checkpoint 13': [
        ('Deeply Rooted - Checkpoint 12', ('Tree Cody Ability', 'Tree May Ability')),
    ],
    'Deeply Rooted - Checkpoint 14': [
        ('Deeply Rooted - Checkpoint 13', ('Tree Cody Ability', 'Tree May Ability')),
    ],
    'Deeply Rooted - Elevator Cutscene': [
        ('Deeply Rooted - Checkpoint 14', ('Tree Cody Ability', 'Tree May Ability')),
    ],
    'Deeply Rooted - Checkpoint 15': [
        ('Deeply Rooted - Elevator Cutscene', ('Tree Cody Ability', 'Tree May Ability')),
    ],
    'Deeply Rooted - Checkpoint 16': [
        ('Deeply Rooted - Checkpoint 15', ('Tree Cody Ability', 'Tree May Ability')),
    ],
    'Deeply Rooted - Checkpoint 17': [
        ('Deeply Rooted - Checkpoint 16', ('Tree Cody Ability', 'Tree May Ability')),
    ],
    'Deeply Rooted - Checkpoint 18': [
        ('Deeply Rooted - Checkpoint 17', ('Tree Cody Ability', 'Tree May Ability')),
    ],
    'Deeply Rooted - Checkpoint 19': [
        ('Deeply Rooted - Checkpoint 18', ('Tree Cody Ability', 'Tree May Ability')),
    ],
    'Deeply Rooted - Checkpoint 20': [
        ('Deeply Rooted - Checkpoint 19', ('Tree Cody Ability', 'Tree May Ability')),
    ],
    'Deeply Rooted - Checkpoint 21': [
        ('Deeply Rooted - Checkpoint 20', ('Tree Cody Ability', 'Tree May Ability')),
    ],
    'Deeply Rooted - Checkpoint 22': [
        ('Deeply Rooted - Checkpoint 21', ('Tree Cody Ability', 'Tree May Ability')),
    ],
    'Deeply Rooted - Checkpoint 23': [
        ('Deeply Rooted - Checkpoint 22', ('Tree Cody Ability', 'Tree May Ability')),
    ],
    'Plunger Dunger Discovered': [
        ('Deeply Rooted - Checkpoint 8', ('Tree Cody Ability', 'Tree May Ability')),
    ],
    'Deeply Rooted Complete': [
        ('Deeply Rooted - Checkpoint 23', ('Tree Cody Ability', 'Tree May Ability')),
    ],
    'Extermination - Cutscene': [
        (None, ()),
    ],
    'Extermination - Phase 2': [
        ('Extermination - Cutscene', ('Tree Cody Ability', 'Tree May Ability')),
    ],
    'Extermination - Phase 3': [
        ('Extermination - Phase 2', ('Tree Cody Ability', 'Tree May Ability')),
    ],
    'Extermination Complete': [
        ('Extermination - Phase 3', ('Tree Cody Ability', 'Tree May Ability')),
    ],
    'Getaway - Entry': [
        (None, ()),
    ],
    'Getaway - Checkpoint 1': [
        ('Getaway - Entry', ()),
    ],
    'Getaway - Checkpoint 2': [
        ('Getaway - Checkpoint 1', ()),
    ],
    'Getaway - Checkpoint 3': [
        ('Getaway - Checkpoint 2', ()),
    ],
    'Getaway - Checkpoint 4': [
        ('Getaway - Checkpoint 3', ()),
    ],
    'Getaway - Checkpoint 5': [
        ('Getaway - Checkpoint 4', ()),
    ],
    'Getaway - Checkpoint 6': [
        ('Getaway - Checkpoint 5', ()),
    ],
    'Getaway Complete': [
        ('Getaway - Checkpoint 6', ()),
    ],
    'Pillow Fort - Cutscene': [
        (None, ()),
    ],
    'Pillow Fort - Checkpoint 1': [
        ('Pillow Fort - Cutscene', ()),
    ],
    'Tank Brothers Discovered': [
        ('Pillow Fort - Cutscene', ()),
    ],
    'Pillow Fort Complete': [
        ('Pillow Fort - Checkpoint 1', ()),
    ],
    'Spaced Out - Cutscene': [
        (None, ()),
    ],
    'Spaced Out - Checkpoint 1': [
        ('Spaced Out - Cutscene', ('Ground Pound', "Rose's Room Cody Ability", "Rose's Room May Ability")),
    ],
    'Spaced Out - Checkpoint 2': [
        ('Spaced Out - Checkpoint 1', ('Dash', 'Double Jump', 'Grinding', 'Ground Pound', "Rose's Room Cody Ability", "Rose's Room May Ability")),
        ('Spaced Out - Checkpoint 1', ('Dash', 'Grinding', 'Ground Pound', "Rose's Room Cody Ability", "Rose's Room May Ability", 'Swinging', 'Wall Jump')),
        ('Spaced Out - Checkpoint 1', ('Double Jump', 'Grinding', 'Ground Pound', "Rose's Room Cody Ability", "Rose's Room May Ability", 'Swinging', 'Wall Jump')),
    ],
    'Spaced Out - Checkpoint 3': [
        ('Spaced Out - Cutscene', ('Ground Pound', "Rose's Room Cody Ability", "Rose's Room May Ability")),
    ],
    'Spaced Out - Checkpoint 4': [
        ('Spaced Out - Checkpoint 3', ('Dash', 'Grinding', 'Ground Pound', "Rose's Room Cody Ability", "Rose's Room May Ability", 'Swinging', 'Wall Jump')),
        ('Spaced Out - Checkpoint 3', ('Double Jump', 'Grinding', 'Ground Pound', "Rose's Room Cody Ability", "Rose's Room May Ability", 'Swinging', 'Wall Jump')),
    ],
    'Spaced Out - Boss Cutscene': [
        ('Spaced Out - Cutscene', ('Dash', 'Double Jump', 'Ground Pound', "Rose's Room Cody Ability", "Rose's Room May Ability")),
    ],
    'Spaced Out - Checkpoint 5': [
        ('Spaced Out - Boss Cutscene', ('Dash', 'Double Jump', 'Ground Pound', "Rose's Room Cody Ability", "Rose's Room May Ability")),
    ],
    'Spaced Out - Checkpoint 6': [
        ('Spaced Out - Checkpoint 5', ('Dash', 'Double Jump', 'Ground Pound', "Rose's Room Cody Ability", "Rose's Room May Ability")),
    ],
    'Spaced Out - Checkpoint 7': [
        ('Spaced Out - Checkpoint 6', ('Dash', 'Double Jump', 'Ground Pound', "Rose's Room Cody Ability", "Rose's Room May Ability")),
    ],
    'Spaced Out - Checkpoint 8': [
        ('Spaced Out - Checkpoint 7', ('Dash', 'Double Jump', 'Ground Pound', "Rose's Room Cody Ability", "Rose's Room May Ability")),
    ],
    'Spaced Out - Checkpoint 9': [
        ('Spaced Out - Checkpoint 1', ('Ground Pound', "Rose's Room Cody Ability", "Rose's Room May Ability")),
    ],
    'Spaced Out - Checkpoint 10': [
        ('Spaced Out - Checkpoint 9', ('Ground Pound', "Rose's Room Cody Ability", "Rose's Room May Ability")),
    ],
    'Laser Tennis Discovered': [
        ('Spaced Out - Cutscene', ('Ground Pound', "Rose's Room Cody Ability", "Rose's Room May Ability")),
    ],
    'Spacewalk Discovered': [
        ('Spaced Out - Cutscene', ('Ground Pound', "Rose's Room Cody Ability", "Rose's Room May Ability")),
    ],
    'Spaced Out Complete': [
        ('Spaced Out - Checkpoint 10', ('Ground Pound', "Rose's Room Cody Ability", "Rose's Room May Ability")),
    ],
    'Hopscotch - Cutscene': [
        (None, ()),
    ],
    'Hopscotch - Checkpoint 1': [
        ('Hopscotch - Cutscene', ('Ground Pound', 'Swinging')),
        ('Hopscotch - Cutscene', ('Dash', 'Double Jump')),
        ('Hopscotch - Cutscene', ('Dash', 'Slide')),
        ('Hopscotch - Cutscene', ('Double Jump',)),
    ],
    'Hopscotch - Checkpoint 2': [
        ('Hopscotch - Checkpoint 1', ('Grinding', 'Ground Pound', 'Swinging')),
        ('Hopscotch - Checkpoint 1', ('Dash', 'Double Jump', 'Grinding')),
        ('Hopscotch - Checkpoint 1', ('Dash', 'Grinding', 'Slide')),
    ],
    'Hopscotch - Checkpoint 3': [
        ('Hopscotch - Checkpoint 2', ('Grinding', 'Ground Pound', 'Swinging')),
        ('Hopscotch - Checkpoint 2', ('Dash', 'Double Jump', 'Grinding')),
        ('Hopscotch - Checkpoint 2', ('Dash', 'Grinding', 'Slide')),
    ],
    'Hopscotch - Checkpoint 4': [
        ('Hopscotch - Checkpoint 3', ('Grinding', 'Ground Pound', 'Swinging')),
        ('Hopscotch - Checkpoint 3', ('Dash', 'Double Jump', 'Grinding')),
        ('Hopscotch - Checkpoint 3', ('Dash', 'Grinding', 'Slide')),
    ],
    'Hopscotch - Checkpoint 5': [
        ('Hopscotch - Checkpoint 4', ('Grinding', 'Ground Pound', 'Swinging')),
        ('Hopscotch - Checkpoint 4', ('Dash', 'Double Jump', 'Grinding', 'Ground Pound')),
        ('Hopscotch - Checkpoint 4', ('Dash', 'Grinding', 'Ground Pound', 'Slide')),
        ('Hopscotch - Checkpoint 4', ('Double Jump',)),
    ],
    'Hopscotch - Checkpoint 6': [
        ('Hopscotch - Checkpoint 5', ('Grinding', 'Ground Pound', 'Swinging', 'Wall Jump')),
        ('Hopscotch - Checkpoint 5', ('Dash', 'Double Jump', 'Grinding', 'Ground Pound', 'Wall Jump')),
        ('Hopscotch - Checkpoint 5', ('Dash', 'Grinding', 'Ground Pound', 'Slide', 'Wall Jump')),
        ('Hopscotch - Checkpoint 5', ('Dash', 'Double Jump', 'Grinding', 'Ground Pound', 'Slide')),
    ],
    'Hopscotch - Checkpoint 7': [
        ('Hopscotch - Checkpoint 6', ('Grinding', 'Ground Pound', 'Swinging', 'Wall Jump')),
        ('Hopscotch - Checkpoint 6', ('Dash', 'Double Jump', 'Grinding', 'Ground Pound', 'Wall Jump')),
        ('Hopscotch - Checkpoint 6', ('Dash', 'Grinding', 'Ground Pound', 'Slide', 'Wall Jump')),
        ('Hopscotch - Checkpoint 6', ('Dash', 'Double Jump', 'Grinding', 'Ground Pound', 'Slide')),
    ],
    'Hopscotch - Checkpoint 8': [
        ('Hopscotch - Checkpoint 7', ('Grinding', 'Ground Pound', 'Swinging', 'Wall Jump')),
        ('Hopscotch - Checkpoint 7', ('Dash', 'Double Jump', 'Grinding', 'Ground Pound', 'Wall Jump')),
        ('Hopscotch - Checkpoint 7', ('Dash', 'Grinding', 'Ground Pound', 'Slide', 'Wall Jump')),
        ('Hopscotch - Checkpoint 7', ('Dash', 'Double Jump', 'Grinding', 'Ground Pound', 'Slide')),
    ],
    'Hopscotch - Checkpoint 9': [
        ('Hopscotch - Checkpoint 8', ('Grinding', 'Ground Pound', 'Swinging', 'Wall Jump')),
        ('Hopscotch - Checkpoint 8', ('Dash', 'Double Jump', 'Grinding', 'Ground Pound', 'Wall Jump')),
        ('Hopscotch - Checkpoint 8', ('Dash', 'Grinding', 'Ground Pound', 'Slide', 'Wall Jump')),
        ('Hopscotch - Checkpoint 8', ('Dash', 'Double Jump', 'Grinding', 'Ground Pound', 'Slide')),
    ],
    'Hopscotch - Checkpoint 10': [
        ('Hopscotch - Checkpoint 9', ('Grinding', 'Ground Pound', 'Swinging', 'Wall Jump')),
        ('Hopscotch - Checkpoint 9', ('Dash', 'Double Jump', 'Grinding', 'Ground Pound', 'Wall Jump')),
        ('Hopscotch - Checkpoint 9', ('Dash', 'Grinding', 'Ground Pound', 'Slide', 'Wall Jump')),
        ('Hopscotch - Checkpoint 9', ('Dash', 'Double Jump', 'Grinding', 'Ground Pound', 'Slide')),
    ],
    'Hopscotch - Checkpoint 11': [
        ('Hopscotch - Checkpoint 10', ('Grinding', 'Ground Pound', 'Swinging', 'Wall Jump')),
        ('Hopscotch - Checkpoint 10', ('Dash', 'Double Jump', 'Grinding', 'Ground Pound', 'Wall Jump')),
        ('Hopscotch - Checkpoint 10', ('Dash', 'Grinding', 'Ground Pound', 'Slide', 'Wall Jump')),
        ('Hopscotch - Checkpoint 10', ('Dash', 'Double Jump', 'Grinding', 'Ground Pound', 'Slide')),
    ],
    'Hopscotch - Checkpoint 12': [
        ('Hopscotch - Checkpoint 11', ('Grinding', 'Ground Pound', 'Swinging', 'Wall Jump')),
        ('Hopscotch - Checkpoint 11', ('Dash', 'Double Jump', 'Grinding', 'Ground Pound', 'Wall Jump')),
        ('Hopscotch - Checkpoint 11', ('Dash', 'Grinding', 'Ground Pound', 'Slide', 'Wall Jump')),
        ('Hopscotch - Checkpoint 11', ('Dash', 'Double Jump', 'Grinding', 'Ground Pound', 'Slide')),
    ],
    'Hopscotch - Checkpoint 13': [
        ('Hopscotch - Checkpoint 12', ('Grinding', 'Ground Pound', 'Swinging', 'Wall Jump')),
        ('Hopscotch - Checkpoint 12', ('Dash', 'Double Jump', 'Grinding', 'Ground Pound', 'Wall Jump')),
        ('Hopscotch - Checkpoint 12', ('Dash', 'Grinding', 'Ground Pound', 'Slide', 'Wall Jump')),
        ('Hopscotch - Checkpoint 12', ('Dash', 'Double Jump', 'Grinding', 'Ground Pound', 'Slide')),
    ],
    'Hopscotch - Checkpoint 14': [
        ('Hopscotch - Checkpoint 13', ('Grinding', 'Ground Pound', 'Swinging', 'Wall Jump')),
        ('Hopscotch - Checkpoint 13', ('Dash', 'Double Jump', 'Grinding', 'Ground Pound', 'Wall Jump')),
        ('Hopscotch - Checkpoint 13', ('Dash', 'Grinding', 'Ground Pound', 'Slide', 'Wall Jump')),
        ('Hopscotch - Checkpoint 13', ('Dash', 'Double Jump', 'Grinding', 'Ground Pound', 'Slide')),
    ],
    'Batting Team Discovered': [
        ('Hopscotch - Checkpoint 1', ('Dash', 'Double Jump', 'Grinding')),
        ('Hopscotch - Checkpoint 9', ('Grinding', 'Ground Pound', 'Swinging', 'Wall Jump')),
        ('Hopscotch - Checkpoint 9', ('Dash', 'Grinding', 'Ground Pound', 'Slide', 'Wall Jump')),
        ('Hopscotch - Checkpoint 9', ('Dash', 'Double Jump', 'Grinding', 'Ground Pound', 'Slide')),
    ],
    'Feed the Reptile Discovered': [
        ('Hopscotch - Checkpoint 2', ('Grinding', 'Ground Pound', 'Swinging')),
        ('Hopscotch - Checkpoint 2', ('Dash', 'Double Jump', 'Grinding')),
        ('Hopscotch - Checkpoint 2', ('Dash', 'Grinding', 'Slide')),
        ('Hopscotch - Checkpoint 2', ('Double Jump',)),
    ],
    'Rodeo Discovered': [
        ('Hopscotch - Cutscene', ()),
    ],
    'Hopscotch Complete': [
        ('Hopscotch - Checkpoint 14', ('Dash', 'Double Jump', 'Grinding', 'Ground Pound', 'Wall Jump')),
        ('Hopscotch - Checkpoint 14', ('Dash', 'Grinding', 'Ground Pound', 'Slide', 'Wall Jump')),
        ('Hopscotch - Checkpoint 14', ('Dash', 'Double Jump', 'Grinding', 'Ground Pound', 'Slide')),
    ],
    'Train Station - Cutscene': [
        (None, ()),
    ],
    'Train Station Complete': [
        ('Train Station - Cutscene', ()),
    ],
    'Dino Land - Entry': [
        (None, ()),
    ],
    'Dino Land - Checkpoint 1': [
        ('Dino Land - Entry', ('Ground Pound',)),
        ('Dino Land - Entry', ('Double Jump',)),
        ('Dino Land - Entry', ('Dash',)),
    ],
    'Dino Land - Checkpoint 2': [
        ('Dino Land - Checkpoint 1', ('Ground Pound',)),
        ('Dino Land - Checkpoint 1', ('Double Jump',)),
        ('Dino Land - Checkpoint 1', ('Dash',)),
    ],
    'Dino Land - Checkpoint 3': [
        ('Dino Land - Checkpoint 2', ('Ground Pound',)),
        ('Dino Land - Checkpoint 2', ('Double Jump',)),
        ('Dino Land - Checkpoint 2', ('Dash',)),
    ],
    'Dino Land Complete': [
        ('Dino Land - Checkpoint 3', ('Ground Pound', 'Wall Jump')),
        ('Dino Land - Checkpoint 3', ('Double Jump', 'Wall Jump')),
        ('Dino Land - Checkpoint 3', ('Dash', 'Wall Jump')),
        ('Dino Land - Checkpoint 3', ('Dash', 'Double Jump')),
    ],
    'Pirates Ahoy - Cutscene': [
        (None, ()),
    ],
    'Pirates Ahoy - Checkpoint 1': [
        ('Pirates Ahoy - Cutscene', ()),
    ],
    'Pirates Ahoy - Checkpoint 2': [
        ('Pirates Ahoy - Checkpoint 1', ()),
    ],
    'Pirates Ahoy - Checkpoint 3': [
        ('Pirates Ahoy - Checkpoint 2', ()),
    ],
    'Pirates Ahoy - Checkpoint 4': [
        ('Pirates Ahoy - Checkpoint 3', ()),
    ],
    'Pirates Ahoy - Boss Entry': [
        ('Pirates Ahoy - Checkpoint 4', ()),
    ],
    'Pirates Ahoy - Checkpoint 5': [
        ('Pirates Ahoy - Boss Entry', ()),
    ],
    'Pirates Ahoy - Checkpoint 6': [
        ('Pirates Ahoy - Checkpoint 5', ()),
    ],
    'Pirates Ahoy - Boss Defeat': [
        ('Pirates Ahoy - Checkpoint 6', ()),
    ],
    'Pirates Ahoy Complete': [
        ('Pirates Ahoy - Boss Defeat', ()),
    ],
    'The Greatest Show - Entry': [
        (None, ()),
    ],
    'The Greatest Show - Checkpoint 1': [
        ('The Greatest Show - Entry', ('Ground Pound',)),
        ('The Greatest Show - Entry', ('Dash', 'Double Jump')),
    ],
    'The Greatest Show - Checkpoint 2': [
        ('The Greatest Show - Checkpoint 1', ('Ground Pound',)),
        ('The Greatest Show - Checkpoint 1', ('Dash', 'Double Jump')),
    ],
    'The Greatest Show - Checkpoint 3': [
        ('The Greatest Show - Checkpoint 2', ('Dash', 'Ground Pound')),
        ('The Greatest Show - Checkpoint 2', ('Double Jump', 'Ground Pound')),
        ('The Greatest Show - Checkpoint 2', ('Ground Pound', 'Slide')),
    ],
    'The Greatest Show - Checkpoint 4': [
        ('The Greatest Show - Checkpoint 3', ('Dash', 'Ground Pound')),
        ('The Greatest Show - Checkpoint 3', ('Double Jump', 'Ground Pound')),
        ('The Greatest Show - Checkpoint 3', ('Ground Pound', 'Slide')),
        ('The Greatest Show - Checkpoint 3', ('Dash', 'Double Jump')),
    ],
    'The Greatest Show - Checkpoint 5': [
        ('The Greatest Show - Checkpoint 4', ('Dash', 'Ground Pound')),
        ('The Greatest Show - Checkpoint 4', ('Double Jump', 'Ground Pound')),
        ('The Greatest Show - Checkpoint 4', ('Ground Pound', 'Slide')),
    ],
    'The Greatest Show Complete': [
        ('The Greatest Show - Checkpoint 5', ('Dash', 'Ground Pound')),
        ('The Greatest Show - Checkpoint 5', ('Double Jump', 'Ground Pound')),
        ('The Greatest Show - Checkpoint 5', ('Ground Pound', 'Slide')),
    ],
    'Once Upon a Time - Cutscene': [
        (None, ()),
    ],
    'Once Upon a Time - Checkpoint 1': [
        ('Once Upon a Time - Cutscene', ()),
    ],
    'Birdstar Discovered': [
        ('Once Upon a Time - Cutscene', ()),
    ],
    'Once Upon a Time Complete': [
        ('Once Upon a Time - Checkpoint 1', ()),
    ],
    'Dungeon Crawler - Cutscene': [
        (None, ()),
    ],
    'Dungeon Crawler - Checkpoint 1': [
        ('Dungeon Crawler - Cutscene', ()),
    ],
    'Dungeon Crawler - Checkpoint 2': [
        ('Dungeon Crawler - Checkpoint 1', ()),
    ],
    'Dungeon Crawler - Checkpoint 3': [
        ('Dungeon Crawler - Checkpoint 2', ()),
    ],
    'Dungeon Crawler - Checkpoint 4': [
        ('Dungeon Crawler - Checkpoint 3', ()),
    ],
    'Dungeon Crawler - Checkpoint 5': [
        ('Dungeon Crawler - Checkpoint 4', ()),
    ],
    'Dungeon Crawler - Checkpoint 6': [
        ('Dungeon Crawler - Checkpoint 5', ()),
    ],
    'Dungeon Crawler - Checkpoint 7': [
        ('Dungeon Crawler - Checkpoint 6', ()),
    ],
    'Dungeon Crawler - Checkpoint 8': [
        ('Dungeon Crawler - Checkpoint 7', ()),
    ],
    'Dungeon Crawler - Checkpoint 9': [
        ('Dungeon Crawler - Checkpoint 8', ()),
    ],
    'Dungeon Crawler - Boss Cutscene': [
        ('Dungeon Crawler - Checkpoint 9', ()),
    ],
    'Dungeon Crawler Complete': [
        ('Dungeon Crawler - Boss Cutscene', ()),
    ],
    'The Queen - Cutscene': [
        (None, ()),
    ],
    'The Queen - Checkpoint 1': [
        ('The Queen - Cutscene', ('Ground Pound',)),
    ],
    'The Queen Complete': [
        ('The Queen - Checkpoint 1', ('Ground Pound',)),
    ],
    'Gates of Time - Cutscene': [
        (None, ()),
    ],
    'Gates of Time - Town Cutscene': [
        ('Gates of Time - Cutscene', ('Dash', 'Double Jump')),
        ('Gates of Time - Cutscene', ('Dash', 'Ground Pound')),
        ('Gates of Time - Cutscene', ('Cuckoo Clock Cody Ability', 'Cuckoo Clock May Ability', 'Grinding', 'Ground Pound', 'Swinging')),
        ('Gates of Time - Cutscene', ('Cuckoo Clock May Ability', 'Double Jump')),
    ],
    'Gates of Time - Checkpoint 1': [
        ('Gates of Time - Town Cutscene', ('Cuckoo Clock Cody Ability', 'Cuckoo Clock May Ability', 'Dash', 'Double Jump')),
        ('Gates of Time - Town Cutscene', ('Cuckoo Clock Cody Ability', 'Cuckoo Clock May Ability', 'Dash', 'Ground Pound')),
        ('Gates of Time - Town Cutscene', ('Cuckoo Clock Cody Ability', 'Cuckoo Clock May Ability', 'Grinding', 'Ground Pound', 'Swinging')),
    ],
    'Gates of Time - Forest Cutscene': [
        ('Gates of Time - Checkpoint 1', ('Cuckoo Clock Cody Ability', 'Cuckoo Clock May Ability', 'Dash', 'Double Jump')),
        ('Gates of Time - Checkpoint 1', ('Cuckoo Clock Cody Ability', 'Cuckoo Clock May Ability', 'Dash', 'Ground Pound')),
        ('Gates of Time - Checkpoint 1', ('Cuckoo Clock Cody Ability', 'Cuckoo Clock May Ability', 'Grinding', 'Ground Pound', 'Swinging')),
    ],
    'Gates of Time - Checkpoint 2': [
        ('Gates of Time - Forest Cutscene', ('Cuckoo Clock Cody Ability', 'Cuckoo Clock May Ability', 'Dash', 'Double Jump')),
        ('Gates of Time - Forest Cutscene', ('Cuckoo Clock Cody Ability', 'Cuckoo Clock May Ability', 'Dash', 'Ground Pound')),
        ('Gates of Time - Forest Cutscene', ('Cuckoo Clock Cody Ability', 'Cuckoo Clock May Ability', 'Grinding', 'Ground Pound', 'Swinging')),
    ],
    'Gates of Time - Checkpoint 3': [
        ('Gates of Time - Checkpoint 2', ('Cuckoo Clock Cody Ability', 'Cuckoo Clock May Ability', 'Dash', 'Double Jump', 'Swinging')),
        ('Gates of Time - Checkpoint 2', ('Cuckoo Clock Cody Ability', 'Cuckoo Clock May Ability', 'Dash', 'Ground Pound', 'Swinging')),
        ('Gates of Time - Checkpoint 2', ('Cuckoo Clock Cody Ability', 'Cuckoo Clock May Ability', 'Grinding', 'Ground Pound', 'Swinging')),
    ],
    'Bomb Run Discovered': [
        ('Gates of Time - Town Cutscene', ('Cuckoo Clock Cody Ability', 'Cuckoo Clock May Ability', 'Dash', 'Double Jump')),
        ('Gates of Time - Town Cutscene', ('Cuckoo Clock Cody Ability', 'Cuckoo Clock May Ability', 'Dash', 'Ground Pound')),
        ('Gates of Time - Town Cutscene', ('Cuckoo Clock Cody Ability', 'Cuckoo Clock May Ability', 'Grinding', 'Ground Pound', 'Swinging')),
    ],
    'Horse Derby Discovered': [
        ('Gates of Time - Town Cutscene', ('Cuckoo Clock Cody Ability', 'Cuckoo Clock May Ability', 'Dash', 'Double Jump')),
        ('Gates of Time - Town Cutscene', ('Cuckoo Clock Cody Ability', 'Cuckoo Clock May Ability', 'Dash', 'Ground Pound')),
        ('Gates of Time - Town Cutscene', ('Cuckoo Clock Cody Ability', 'Cuckoo Clock May Ability', 'Grinding', 'Ground Pound', 'Swinging')),
    ],
    'Gates of Time Complete': [
        ('Gates of Time - Checkpoint 3', ('Cuckoo Clock Cody Ability', 'Cuckoo Clock May Ability', 'Dash', 'Double Jump', 'Swinging')),
        ('Gates of Time - Checkpoint 3', ('Cuckoo Clock Cody Ability', 'Cuckoo Clock May Ability', 'Dash', 'Ground Pound', 'Swinging')),
        ('Gates of Time - Checkpoint 3', ('Cuckoo Clock Cody Ability', 'Cuckoo Clock May Ability', 'Grinding', 'Ground Pound', 'Swinging')),
    ],
    'Clockworks - Cutscene': [
        (None, ()),
    ],
    'Clockworks - Checkpoint 1': [
        ('Clockworks - Cutscene', ('Cuckoo Clock May Ability',)),
    ],
    'Clockworks - Checkpoint 2': [
        ('Clockworks - Checkpoint 1', ('Cuckoo Clock May Ability',)),
    ],
    'Clockworks - Checkpoint 3': [
        ('Clockworks - Checkpoint 2', ('Cuckoo Clock Cody Ability', 'Cuckoo Clock May Ability', 'Grinding')),
        ('Clockworks - Checkpoint 2', ('Cuckoo Clock May Ability', 'Dash', 'Grinding', 'Slide')),
    ],
    'Clockworks - Checkpoint 4': [
        ('Clockworks - Checkpoint 3', ('Cuckoo Clock Cody Ability', 'Cuckoo Clock May Ability', 'Grinding')),
    ],
    'Clockworks - Checkpoint 5': [
        ('Clockworks - Checkpoint 4', ('Cuckoo Clock Cody Ability', 'Cuckoo Clock May Ability', 'Grinding')),
    ],
    'Clockworks - Checkpoint 6': [
        ('Clockworks - Checkpoint 5', ('Cuckoo Clock Cody Ability', 'Cuckoo Clock May Ability', 'Grinding', 'Wall Jump')),
    ],
    'Clockworks - Checkpoint 7': [
        ('Clockworks - Checkpoint 6', ('Cuckoo Clock Cody Ability', 'Cuckoo Clock May Ability', 'Grinding', 'Wall Jump')),
    ],
    'Clockworks - Checkpoint 8': [
        ('Clockworks - Checkpoint 7', ('Cuckoo Clock Cody Ability', 'Cuckoo Clock May Ability', 'Grinding', 'Swinging', 'Wall Jump')),
    ],
    'Clockworks - Checkpoint 9': [
        ('Clockworks - Checkpoint 8', ('Cuckoo Clock Cody Ability', 'Cuckoo Clock May Ability', 'Grinding', 'Swinging', 'Wall Jump')),
    ],
    'Clockworks - Checkpoint 10': [
        ('Clockworks - Checkpoint 9', ('Cuckoo Clock Cody Ability', 'Cuckoo Clock May Ability', 'Grinding', 'Swinging', 'Wall Jump')),
    ],
    'Clockworks Complete': [
        ('Clockworks - Checkpoint 10', ('Cuckoo Clock Cody Ability', 'Cuckoo Clock May Ability', 'Grinding', 'Swinging', 'Wall Jump')),
    ],
    'A Blast from the Past - Entry': [
        (None, ()),
    ],
    'A Blast from the Past - Checkpoint 1': [
        ('A Blast from the Past - Entry', ()),
    ],
    'A Blast from the Past - Checkpoint 2': [
        ('A Blast from the Past - Checkpoint 1', ()),
    ],
    'A Blast from the Past - Checkpoint 3': [
        ('A Blast from the Past - Checkpoint 2', ()),
    ],
    'A Blast from the Past - Checkpoint 4': [
        ('A Blast from the Past - Checkpoint 3', ()),
    ],
    'A Blast from the Past - Checkpoint 5': [
        ('A Blast from the Past - Checkpoint 4', ('Cuckoo Clock Cody Ability',)),
    ],
    'A Blast from the Past - Checkpoint 6': [
        ('A Blast from the Past - Checkpoint 5', ('Cuckoo Clock Cody Ability', 'Grinding')),
    ],
    'A Blast from the Past - Checkpoint 7': [
        ('A Blast from the Past - Checkpoint 6', ('Cuckoo Clock Cody Ability', 'Grinding')),
    ],
    'A Blast from the Past Complete': [
        ('A Blast from the Past - Checkpoint 7', ()),
    ],
    'Warming Up - Entry': [
        (None, ()),
    ],
    'Warming Up - Checkpoint 1': [
        ('Warming Up - Entry', ('Dash', 'Slide', 'Swinging')),
        ('Warming Up - Entry', ('Dash', 'Double Jump', 'Slide')),
        ('Warming Up - Entry', ('Double Jump', 'Snow Globe Ability', 'Swinging')),
        ('Warming Up - Entry', ('Dash', 'Snow Globe Ability', 'Swinging')),
        ('Warming Up - Entry', ('Slide', 'Snow Globe Ability', 'Sprint', 'Swinging')),
    ],
    'Warming Up - Checkpoint 2': [
        ('Warming Up - Checkpoint 1', ('Dash', 'Slide', 'Swinging')),
        ('Warming Up - Checkpoint 1', ('Dash', 'Double Jump', 'Slide')),
        ('Warming Up - Checkpoint 1', ('Double Jump', 'Snow Globe Ability', 'Swinging')),
        ('Warming Up - Checkpoint 1', ('Dash', 'Snow Globe Ability', 'Swinging')),
        ('Warming Up - Checkpoint 1', ('Slide', 'Snow Globe Ability', 'Sprint', 'Swinging')),
    ],
    'Warming Up - Checkpoint 3': [
        ('Warming Up - Checkpoint 2', ('Dash', 'Double Jump', 'Slide')),
        ('Warming Up - Checkpoint 2', ('Double Jump', 'Snow Globe Ability', 'Swinging')),
        ('Warming Up - Checkpoint 2', ('Dash', 'Snow Globe Ability', 'Swinging')),
        ('Warming Up - Checkpoint 2', ('Slide', 'Snow Globe Ability', 'Sprint', 'Swinging')),
    ],
    'Warming Up - Checkpoint 4': [
        ('Warming Up - Checkpoint 3', ('Dash', 'Double Jump', 'Slide')),
        ('Warming Up - Checkpoint 3', ('Double Jump', 'Snow Globe Ability', 'Swinging')),
        ('Warming Up - Checkpoint 3', ('Dash', 'Snow Globe Ability', 'Swinging')),
        ('Warming Up - Checkpoint 3', ('Slide', 'Snow Globe Ability', 'Sprint', 'Swinging')),
    ],
    'Warming Up - Checkpoint 5': [
        ('Warming Up - Checkpoint 4', ('Double Jump', 'Grinding', 'Snow Globe Ability', 'Swinging', 'Wall Jump')),
        ('Warming Up - Checkpoint 4', ('Dash', 'Grinding', 'Snow Globe Ability', 'Swinging', 'Wall Jump')),
        ('Warming Up - Checkpoint 4', ('Grinding', 'Slide', 'Snow Globe Ability', 'Sprint', 'Swinging', 'Wall Jump')),
    ],
    'Warming Up - Checkpoint 6': [
        ('Warming Up - Entry', ('Dash', 'Double Jump', 'Slide')),
        ('Warming Up - Checkpoint 5', ('Double Jump', 'Grinding', 'Snow Globe Ability', 'Swinging', 'Wall Jump')),
        ('Warming Up - Checkpoint 5', ('Dash', 'Grinding', 'Snow Globe Ability', 'Swinging', 'Wall Jump')),
        ('Warming Up - Checkpoint 5', ('Grinding', 'Slide', 'Snow Globe Ability', 'Sprint', 'Swinging', 'Wall Jump')),
    ],
    'Warming Up Complete': [
        ('Warming Up - Entry', ('Dash', 'Double Jump', 'Slide')),
        ('Warming Up - Checkpoint 6', ('Double Jump', 'Grinding', 'Snow Globe Ability', 'Swinging', 'Wall Jump')),
        ('Warming Up - Checkpoint 6', ('Dash', 'Grinding', 'Snow Globe Ability', 'Swinging', 'Wall Jump')),
        ('Warming Up - Checkpoint 6', ('Grinding', 'Slide', 'Snow Globe Ability', 'Sprint', 'Swinging', 'Wall Jump')),
    ],
    'Winter Village - Cutscene': [
        (None, ()),
    ],
    'Winter Village - Checkpoint 1': [
        ('Winter Village - Cutscene', ('Snow Globe Ability', 'Wall Jump')),
    ],
    'Winter Village - Checkpoint 2': [
        ('Winter Village - Checkpoint 1', ('Grinding', 'Snow Globe Ability', 'Wall Jump')),
    ],
    'Snow Warfare Discovered': [
        ('Winter Village - Cutscene', ('Grinding', 'Snow Globe Ability', 'Wall Jump')),
        ('Winter Village - Checkpoint 2', ('Grinding', 'Snow Globe Ability', 'Wall Jump')),
        ('Winter Village - Cutscene', ('Dash', 'Slide')),
    ],
    'Shuffle Board Discovered': [
        ('Winter Village - Checkpoint 2', ('Snow Globe Ability', 'Wall Jump')),
    ],
    'Icicle Throwing Discovered': [
        ('Winter Village - Checkpoint 2', ('Snow Globe Ability', 'Wall Jump')),
    ],
    'Winter Village Complete': [
        ('Winter Village - Checkpoint 2', ('Snow Globe Ability', 'Wall Jump')),
    ],
    'Beneath the Ice - Cutscene': [
        (None, ()),
    ],
    'Beneath the Ice - Checkpoint 1': [
        ('Beneath the Ice - Cutscene', ('Ground Pound',)),
    ],
    'Beneath the Ice - Checkpoint 2': [
        ('Beneath the Ice - Cutscene', ('Snow Globe Ability',)),
        ('Beneath the Ice - Checkpoint 1', ('Snow Globe Ability',)),
    ],
    'Beneath the Ice - Checkpoint 3': [
        ('Beneath the Ice - Checkpoint 1', ('Snow Globe Ability',)),
    ],
    'Ice Race Discovered': [
        ('Beneath the Ice - Cutscene', ()),
    ],
    'Beneath the Ice Complete': [
        ('Beneath the Ice - Checkpoint 3', ('Ground Pound', 'Snow Globe Ability')),
    ],
    'Slippery Slopes - Cutscene': [
        (None, ()),
    ],
    'Slippery Slopes - Checkpoint 1': [
        ('Slippery Slopes - Cutscene', ('Snow Globe Ability',)),
    ],
    'Slippery Slopes - Checkpoint 2': [
        ('Slippery Slopes - Checkpoint 1', ('Dash', 'Grinding', 'Snow Globe Ability')),
        ('Slippery Slopes - Checkpoint 1', ('Double Jump', 'Grinding', 'Snow Globe Ability')),
    ],
    'Slippery Slopes - Checkpoint 3': [
        ('Slippery Slopes - Cutscene', ('Dash',)),
        ('Slippery Slopes - Cutscene', ('Ground Pound',)),
        ('Slippery Slopes - Cutscene', ('Double Jump',)),
        ('Slippery Slopes - Checkpoint 2', ('Dash', 'Grinding', 'Snow Globe Ability')),
        ('Slippery Slopes - Checkpoint 2', ('Double Jump', 'Grinding', 'Snow Globe Ability')),
    ],
    'Slippery Slopes - Checkpoint 4': [
        ('Slippery Slopes - Checkpoint 3', ('Dash', 'Grinding', 'Snow Globe Ability')),
        ('Slippery Slopes - Checkpoint 3', ('Double Jump', 'Grinding', 'Snow Globe Ability')),
    ],
    'Slippery Slopes - Checkpoint 5': [
        ('Slippery Slopes - Checkpoint 4', ('Dash', 'Grinding', 'Snow Globe Ability')),
        ('Slippery Slopes - Checkpoint 4', ('Double Jump', 'Grinding', 'Snow Globe Ability')),
    ],
    'Slippery Slopes - Checkpoint 6': [
        ('Slippery Slopes - Checkpoint 5', ('Dash', 'Grinding', 'Snow Globe Ability')),
        ('Slippery Slopes - Checkpoint 5', ('Double Jump', 'Grinding', 'Snow Globe Ability')),
    ],
    'Slippery Slopes Complete': [
        ('Slippery Slopes - Checkpoint 6', ('Dash', 'Grinding', 'Snow Globe Ability')),
        ('Slippery Slopes - Checkpoint 6', ('Double Jump', 'Grinding', 'Snow Globe Ability')),
    ],
    'Green Fingers - Cutscene': [
        (None, ()),
    ],
    'Green Fingers - Checkpoint 1': [
        ('Green Fingers - Cutscene', ('Dash', 'Double Jump', 'Slide')),
        ('Green Fingers - Cutscene', ('Double Jump', 'Garden Cody Ability', 'Garden May Ability', 'Swinging')),
        ('Green Fingers - Cutscene', ('Garden Cody Ability', 'Garden May Ability', 'Ground Pound', 'Swinging')),
    ],
    'Green Fingers - Checkpoint 2': [
        ('Green Fingers - Checkpoint 1', ('Dash', 'Double Jump', 'Slide')),
        ('Green Fingers - Checkpoint 1', ('Garden Cody Ability', 'Garden May Ability', 'Ground Pound', 'Swinging')),
    ],
    'Green Fingers - Checkpoint 3': [
        ('Green Fingers - Checkpoint 2', ('Dash', 'Double Jump', 'Slide')),
        ('Green Fingers - Checkpoint 2', ('Garden Cody Ability', 'Garden May Ability', 'Grinding', 'Ground Pound', 'Swinging')),
    ],
    'Green Fingers - Checkpoint 4': [
        ('Green Fingers - Checkpoint 3', ('Dash', 'Double Jump', 'Slide')),
        ('Green Fingers - Checkpoint 3', ('Garden Cody Ability', 'Garden May Ability', 'Grinding', 'Ground Pound', 'Swinging')),
    ],
    'Green Fingers - Checkpoint 5': [
        ('Green Fingers - Checkpoint 4', ('Dash', 'Double Jump', 'Slide')),
        ('Green Fingers - Checkpoint 4', ('Garden Cody Ability', 'Garden May Ability', 'Grinding', 'Ground Pound', 'Swinging')),
    ],
    'Green Fingers Complete': [
        ('Green Fingers - Checkpoint 5', ('Dash', 'Double Jump', 'Slide')),
        ('Green Fingers - Checkpoint 5', ('Garden Cody Ability', 'Garden May Ability', 'Grinding', 'Ground Pound', 'Swinging')),
    ],
    'Weed Whacking - Cutscene': [
        (None, ()),
    ],
    'Weed Whacking - Checkpoint 1': [
        ('Weed Whacking - Cutscene', ('Garden May Ability',)),
        ('Weed Whacking - Cutscene', ('Dash', 'Double Jump', 'Wall Jump')),
    ],
    'Weed Whacking - Checkpoint 2': [
        ('Weed Whacking - Checkpoint 1', ('Garden Cody Ability', 'Garden May Ability')),
    ],
    'Weed Whacking - Checkpoint 3': [
        ('Weed Whacking - Checkpoint 2', ('Garden Cody Ability', 'Garden May Ability')),
    ],
    'Weed Whacking - Checkpoint 4': [
        ('Weed Whacking - Checkpoint 3', ('Garden Cody Ability', 'Garden May Ability', 'Ground Pound')),
    ],
    'Weed Whacking - Checkpoint 5': [
        ('Weed Whacking - Checkpoint 4', ('Garden Cody Ability', 'Garden May Ability', 'Ground Pound')),
    ],
    'Weed Whacking - Checkpoint 6': [
        ('Weed Whacking - Checkpoint 5', ('Garden Cody Ability', 'Garden May Ability', 'Ground Pound')),
    ],
    'Weed Whacking - Checkpoint 7': [
        ('Weed Whacking - Checkpoint 6', ('Garden Cody Ability', 'Garden May Ability', 'Ground Pound')),
    ],
    'Weed Whacking - Checkpoint 8': [
        ('Weed Whacking - Checkpoint 7', ('Garden Cody Ability', 'Garden May Ability', 'Ground Pound')),
    ],
    'Weed Whacking - Checkpoint 9': [
        ('Weed Whacking - Checkpoint 8', ('Garden Cody Ability', 'Garden May Ability', 'Ground Pound')),
    ],
    'Weed Whacking - Checkpoint 10': [
        ('Weed Whacking - Checkpoint 9', ('Garden Cody Ability', 'Garden May Ability', 'Ground Pound')),
    ],
    'Weed Whacking - Checkpoint 11': [
        ('Weed Whacking - Checkpoint 10', ('Garden Cody Ability', 'Garden May Ability', 'Grinding', 'Ground Pound')),
        ('Weed Whacking - Cutscene', ('Dash', 'Double Jump', 'Slide', 'Wall Jump')),
    ],
    'Weed Whacking - Checkpoint 12': [
        ('Weed Whacking - Checkpoint 11', ('Garden Cody Ability', 'Garden May Ability', 'Grinding', 'Ground Pound')),
        ('Weed Whacking - Checkpoint 11', ('Dash', 'Double Jump', 'Garden Cody Ability', 'Garden May Ability', 'Slide', 'Wall Jump')),
    ],
    'Larva Basket Discovered': [
        ('Weed Whacking - Checkpoint 1', ('Garden May Ability', 'Swinging')),
        ('Weed Whacking - Cutscene', ('Dash', 'Double Jump', 'Wall Jump')),
    ],
    'Garden Swings Discovered': [
        ('Weed Whacking - Cutscene', ('Double Jump',)),
        ('Weed Whacking - Cutscene', ('Ground Pound',)),
        ('Weed Whacking - Cutscene', ('Wall Jump',)),
        ('Weed Whacking - Cutscene', ('Garden May Ability',)),
        ('Weed Whacking - Cutscene', ('Dash', 'Slide')),
    ],
    'Weed Whacking Complete': [
        ('Weed Whacking - Checkpoint 12', ('Garden Cody Ability', 'Garden May Ability', 'Grinding', 'Ground Pound')),
        ('Weed Whacking - Checkpoint 12', ('Dash', 'Double Jump', 'Garden Cody Ability', 'Garden May Ability', 'Slide', 'Wall Jump')),
    ],
    'Trespassing - Cutscene': [
        (None, ()),
    ],
    'Trespassing - Checkpoint 1': [
        ('Trespassing - Cutscene', ()),
    ],
    'Trespassing - Checkpoint 2': [
        ('Trespassing - Checkpoint 1', ()),
    ],
    'Trespassing - Checkpoint 3': [
        ('Trespassing - Checkpoint 2', ('Garden May Ability', 'Ground Pound', 'Wall Jump')),
    ],
    'Trespassing - Checkpoint 4': [
        ('Trespassing - Checkpoint 3', ('Garden May Ability', 'Ground Pound', 'Swinging', 'Wall Jump')),
        ('Trespassing - Checkpoint 3', ('Dash', 'Garden May Ability', 'Ground Pound', 'Wall Jump')),
    ],
    'Trespassing - Checkpoint 5': [
        ('Trespassing - Checkpoint 4', ('Garden May Ability', 'Ground Pound', 'Swinging', 'Wall Jump')),
        ('Trespassing - Checkpoint 4', ('Dash', 'Garden May Ability', 'Ground Pound', 'Wall Jump')),
    ],
    'Trespassing - Checkpoint 6': [
        ('Trespassing - Checkpoint 5', ('Garden Cody Ability', 'Garden May Ability', 'Ground Pound', 'Swinging', 'Wall Jump')),
        ('Trespassing - Checkpoint 5', ('Dash', 'Garden Cody Ability', 'Garden May Ability', 'Ground Pound', 'Wall Jump')),
    ],
    'Trespassing - Checkpoint 7': [
        ('Trespassing - Checkpoint 6', ('Garden Cody Ability', 'Garden May Ability', 'Ground Pound', 'Swinging', 'Wall Jump')),
        ('Trespassing - Checkpoint 6', ('Dash', 'Garden Cody Ability', 'Garden May Ability', 'Ground Pound', 'Wall Jump')),
    ],
    'Trespassing - Checkpoint 8': [
        ('Trespassing - Checkpoint 7', ('Garden Cody Ability', 'Garden May Ability', 'Ground Pound', 'Swinging', 'Wall Jump')),
        ('Trespassing - Checkpoint 7', ('Dash', 'Garden Cody Ability', 'Garden May Ability', 'Ground Pound', 'Wall Jump')),
    ],
    'Trespassing - Checkpoint 9': [
        ('Trespassing - Checkpoint 8', ('Garden Cody Ability', 'Garden May Ability', 'Ground Pound', 'Swinging', 'Wall Jump')),
        ('Trespassing - Checkpoint 8', ('Dash', 'Garden Cody Ability', 'Garden May Ability', 'Ground Pound', 'Wall Jump')),
    ],
    'Trespassing - Checkpoint 10': [
        ('Trespassing - Checkpoint 9', ('Double Jump', 'Garden May Ability')),
        ('Trespassing - Checkpoint 9', ('Garden Cody Ability', 'Garden May Ability', 'Ground Pound', 'Swinging', 'Wall Jump')),
        ('Trespassing - Checkpoint 9', ('Dash', 'Garden Cody Ability', 'Garden May Ability', 'Ground Pound', 'Wall Jump')),
    ],
    'Trespassing Complete': [
        ('Trespassing - Checkpoint 10', ('Double Jump', 'Garden May Ability')),
        ('Trespassing - Checkpoint 10', ('Garden Cody Ability', 'Garden May Ability', 'Ground Pound', 'Swinging', 'Wall Jump')),
        ('Trespassing - Checkpoint 10', ('Dash', 'Garden Cody Ability', 'Garden May Ability', 'Ground Pound', 'Wall Jump')),
    ],
    'Frog Pond - Cutscene': [
        (None, ()),
    ],
    'Frog Pond - Checkpoint 1': [
        ('Frog Pond - Cutscene', ()),
    ],
    'Frog Pond - Checkpoint 2': [
        ('Frog Pond - Checkpoint 1', ()),
    ],
    'Frog Pond - Checkpoint 3': [
        ('Frog Pond - Checkpoint 2', ()),
    ],
    'Frog Pond - Checkpoint 4': [
        ('Frog Pond - Checkpoint 3', ()),
    ],
    'Frog Pond - Checkpoint 5': [
        ('Frog Pond - Checkpoint 4', ()),
    ],
    'Frog Pond - Checkpoint 6': [
        ('Frog Pond - Checkpoint 5', ()),
    ],
    'Frog Pond - Checkpoint 7': [
        ('Frog Pond - Checkpoint 6', ()),
    ],
    'Frog Pond - Checkpoint 8': [
        ('Frog Pond - Checkpoint 7', ('Garden Cody Ability', 'Garden May Ability')),
    ],
    'Frog Pond - Checkpoint 9': [
        ('Snail Race Discovered', ()),
    ],
    'Snail Race Discovered': [
        ('Frog Pond - Cutscene', ()),
    ],
    'Frog Pond Complete': [
        ('Frog Pond - Cutscene', ('Double Jump', 'Garden May Ability', 'Ground Pound')),
    ],
    'Affliction - Cutscene': [
        (None, ()),
    ],
    'Affliction - Checkpoint 1': [
        ('Affliction - Cutscene', ('Garden Cody Ability', 'Garden May Ability', 'Ground Pound')),
    ],
    'Affliction - Joy Cutscene': [
        ('Affliction - Checkpoint 1', ('Garden Cody Ability', 'Garden May Ability', 'Ground Pound')),
    ],
    'Affliction - Checkpoint 2': [
        ('Affliction - Joy Cutscene', ('Garden Cody Ability', 'Garden May Ability', 'Ground Pound')),
    ],
    'Affliction - Checkpoint 3': [
        ('Affliction - Checkpoint 2', ('Garden Cody Ability', 'Garden May Ability', 'Ground Pound')),
    ],
    'Affliction - Checkpoint 4': [
        ('Affliction - Checkpoint 3', ('Garden Cody Ability', 'Garden May Ability', 'Grinding', 'Ground Pound')),
    ],
    'Affliction - Checkpoint 5': [
        ('Affliction - Checkpoint 4', ('Garden Cody Ability', 'Garden May Ability', 'Grinding', 'Ground Pound')),
    ],
    'Affliction - Checkpoint 6': [
        ('Affliction - Checkpoint 5', ('Garden Cody Ability', 'Garden May Ability', 'Grinding', 'Ground Pound')),
    ],
    'Affliction - Checkpoint 7': [
        ('Affliction - Checkpoint 6', ('Garden Cody Ability', 'Garden May Ability', 'Grinding', 'Ground Pound')),
    ],
    'Affliction Complete': [
        ('Affliction - Checkpoint 7', ('Garden Cody Ability', 'Garden May Ability', 'Grinding', 'Ground Pound')),
    ],
    'Setting the Stage - Cutscene': [
        (None, ()),
    ],
    'Musical Chairs Discovered': [
        ('Setting the Stage - Cutscene', ('Dash', 'Double Jump', 'Slide', 'Swinging', 'Wall Jump')),
    ],
    'Track Runner Discovered': [
        ('Musical Chairs Discovered', ('Dash', 'Double Jump', 'Ground Pound', 'Swinging', 'Wall Jump')),
        ('Rehearsal - Checkpoint 18', ('Attic Cody Ability', 'Attic May Ability', 'Double Jump', 'Grinding', 'Ground Pound', 'Swinging', 'Wall Jump')),
    ],
    'Slotcars Discovered': [
        ('Setting the Stage - Cutscene', ()),
    ],
    'Chess Discovered': [
        ('Musical Chairs Discovered', ('Dash', 'Double Jump', 'Slide', 'Swinging', 'Wall Jump')),
        ('Symphony - Checkpoint 8', ('Double Jump', 'Grinding', 'Ground Pound', 'Swinging', 'Wall Jump')),
    ],
    'Setting the Stage Complete': [
        ('Setting the Stage - Cutscene', ()),
    ],
    'Rehearsal - Cutscene': [
        (None, ()),
    ],
    'Rehearsal - Checkpoint 1': [
        ('Rehearsal - Cutscene', ('Attic Cody Ability', 'Attic May Ability')),
    ],
    'Rehearsal - Checkpoint 2': [
        ('Rehearsal - Checkpoint 1', ('Attic Cody Ability', 'Attic May Ability', 'Double Jump')),
    ],
    'Rehearsal - Checkpoint 3': [
        ('Rehearsal - Checkpoint 2', ('Attic Cody Ability', 'Attic May Ability', 'Double Jump', 'Swinging')),
    ],
    'Rehearsal - Checkpoint 4': [
        ('Rehearsal - Checkpoint 3', ('Attic Cody Ability', 'Attic May Ability', 'Double Jump', 'Swinging')),
    ],
    'Rehearsal - Checkpoint 5': [
        ('Rehearsal - Checkpoint 4', ('Attic Cody Ability', 'Attic May Ability', 'Double Jump', 'Swinging')),
    ],
    'Rehearsal - Checkpoint 6': [
        ('Rehearsal - Checkpoint 5', ('Attic Cody Ability', 'Attic May Ability', 'Double Jump', 'Swinging')),
    ],
    'Rehearsal - Checkpoint 7': [
        ('Rehearsal - Checkpoint 6', ('Attic Cody Ability', 'Attic May Ability', 'Double Jump', 'Swinging')),
    ],
    'Rehearsal - Checkpoint 8': [
        ('Rehearsal - Checkpoint 7', ('Attic Cody Ability', 'Attic May Ability', 'Double Jump', 'Swinging')),
    ],
    'Rehearsal - Checkpoint 9': [
        ('Rehearsal - Checkpoint 8', ('Attic Cody Ability', 'Attic May Ability', 'Double Jump', 'Swinging')),
    ],
    'Rehearsal - Checkpoint 10': [
        ('Rehearsal - Checkpoint 9', ('Attic Cody Ability', 'Attic May Ability', 'Double Jump', 'Swinging')),
    ],
    'Rehearsal - Checkpoint 11': [
        ('Rehearsal - Checkpoint 10', ('Attic Cody Ability', 'Attic May Ability', 'Double Jump', 'Swinging', 'Wall Jump')),
    ],
    'Rehearsal - Checkpoint 12': [
        ('Rehearsal - Checkpoint 11', ('Attic Cody Ability', 'Attic May Ability', 'Double Jump', 'Grinding', 'Swinging', 'Wall Jump')),
    ],
    'Rehearsal - Checkpoint 13': [
        ('Rehearsal - Checkpoint 12', ('Attic Cody Ability', 'Attic May Ability', 'Double Jump', 'Grinding', 'Swinging', 'Wall Jump')),
    ],
    'Rehearsal - Checkpoint 14': [
        ('Rehearsal - Checkpoint 13', ('Attic Cody Ability', 'Attic May Ability', 'Double Jump', 'Grinding', 'Swinging', 'Wall Jump')),
    ],
    'Rehearsal - Checkpoint 15': [
        ('Rehearsal - Checkpoint 14', ('Attic Cody Ability', 'Attic May Ability', 'Double Jump', 'Grinding', 'Swinging', 'Wall Jump')),
    ],
    'Rehearsal - Checkpoint 16': [
        ('Rehearsal - Checkpoint 15', ('Attic Cody Ability', 'Attic May Ability', 'Double Jump', 'Grinding', 'Swinging', 'Wall Jump')),
    ],
    'Rehearsal - Checkpoint 17': [
        ('Rehearsal - Checkpoint 16', ('Attic Cody Ability', 'Attic May Ability', 'Double Jump', 'Grinding', 'Ground Pound', 'Swinging', 'Wall Jump')),
    ],
    'Rehearsal - Stage Cutscene': [
        ('Rehearsal - Checkpoint 17', ('Attic Cody Ability', 'Attic May Ability', 'Double Jump', 'Grinding', 'Ground Pound', 'Swinging', 'Wall Jump')),
    ],
    'Rehearsal - Checkpoint 18': [
        ('Rehearsal - Stage Cutscene', ('Attic Cody Ability', 'Attic May Ability', 'Double Jump', 'Grinding', 'Ground Pound', 'Swinging', 'Wall Jump')),
    ],
    'Rehearsal Complete': [
        ('Rehearsal - Checkpoint 18', ('Attic Cody Ability', 'Attic May Ability', 'Double Jump', 'Grinding', 'Ground Pound', 'Swinging', 'Wall Jump')),
    ],
    'Symphony - Cutscene': [
        (None, ()),
    ],
    'Symphony - Checkpoint 1': [
        ('Symphony - Cutscene', ('Attic Cody Ability', 'Attic May Ability', 'Swinging')),
    ],
    'Symphony - Checkpoint 2': [
        ('Symphony - Checkpoint 1', ('Attic Cody Ability', 'Attic May Ability', 'Swinging')),
        ('Symphony - Checkpoint 1', ('Attic May Ability', 'Dash', 'Double Jump', 'Slide', 'Swinging')),
    ],
    'Symphony - Checkpoint 3': [
        ('Symphony - Checkpoint 2', ('Attic Cody Ability', 'Attic May Ability', 'Swinging')),
        ('Symphony - Checkpoint 2', ('Attic May Ability', 'Dash', 'Double Jump', 'Slide', 'Swinging')),
    ],
    'Symphony - Checkpoint 4': [
        ('Symphony - Checkpoint 3', ('Attic Cody Ability', 'Attic May Ability', 'Swinging')),
        ('Symphony - Checkpoint 3', ('Attic May Ability', 'Dash', 'Double Jump', 'Slide', 'Swinging')),
    ],
    'Symphony - Checkpoint 5': [
        ('Symphony - Checkpoint 4', ('Attic Cody Ability', 'Attic May Ability', 'Swinging')),
        ('Symphony - Checkpoint 4', ('Attic May Ability', 'Dash', 'Double Jump', 'Slide', 'Swinging')),
    ],
    'Symphony - Checkpoint 6': [
        ('Symphony - Checkpoint 5', ('Attic Cody Ability', 'Attic May Ability', 'Swinging')),
        ('Symphony - Checkpoint 5', ('Attic May Ability', 'Dash', 'Double Jump', 'Slide', 'Swinging')),
    ],
    'Symphony - Checkpoint 7': [
        ('Symphony - Checkpoint 6', ('Attic Cody Ability', 'Attic May Ability', 'Swinging')),
        ('Symphony - Checkpoint 6', ('Attic May Ability', 'Dash', 'Double Jump', 'Slide', 'Swinging')),
    ],
    'Symphony - Stage Cutscene': [
        ('Symphony - Checkpoint 7', ('Attic Cody Ability', 'Attic May Ability', 'Swinging')),
        ('Symphony - Checkpoint 7', ('Attic May Ability', 'Dash', 'Double Jump', 'Slide', 'Swinging')),
    ],
    'Symphony - Checkpoint 8': [
        ('Symphony - Stage Cutscene', ('Attic Cody Ability', 'Attic May Ability', 'Swinging')),
        ('Symphony - Stage Cutscene', ('Attic May Ability', 'Dash', 'Double Jump', 'Slide', 'Swinging')),
    ],
    'Volleyball Discovered': [
        ('Symphony - Checkpoint 5', ('Attic Cody Ability', 'Attic May Ability', 'Swinging')),
        ('Symphony - Checkpoint 5', ('Attic May Ability', 'Dash', 'Double Jump', 'Slide', 'Swinging')),
    ],
    'Symphony Complete': [
        ('Symphony - Checkpoint 5', ('Attic Cody Ability', 'Attic May Ability', 'Swinging')),
        ('Symphony - Checkpoint 5', ('Attic May Ability', 'Dash', 'Double Jump', 'Slide', 'Swinging')),
    ],
    'Turn Up - Cutscene': [
        (None, ()),
    ],
    'Turn Up - Checkpoint 1': [
        ('Turn Up - Cutscene', ()),
    ],
    'Turn Up - Checkpoint 2': [
        ('Turn Up - Checkpoint 1', ()),
    ],
    'Turn Up - Checkpoint 3': [
        ('Turn Up - Checkpoint 2', ()),
    ],
    'Turn Up - Checkpoint 4': [
        ('Turn Up - Checkpoint 3', ('Dash', 'Double Jump', 'Ground Pound')),
        ('Turn Up - Checkpoint 3', ('Attic Cody Ability', 'Attic May Ability', 'Dash', 'Ground Pound', 'Swinging', 'Wall Jump')),
        ('Turn Up - Checkpoint 3', ('Attic Cody Ability', 'Attic May Ability', 'Double Jump', 'Ground Pound', 'Swinging', 'Wall Jump')),
    ],
    'Turn Up - Checkpoint 5': [
        ('Turn Up - Checkpoint 4', ('Dash', 'Double Jump', 'Ground Pound')),
        ('Turn Up - Checkpoint 4', ('Attic Cody Ability', 'Attic May Ability', 'Dash', 'Ground Pound', 'Swinging', 'Wall Jump')),
        ('Turn Up - Checkpoint 4', ('Attic Cody Ability', 'Attic May Ability', 'Double Jump', 'Ground Pound', 'Swinging', 'Wall Jump')),
    ],
    'Turn Up - Checkpoint 6': [
        ('Turn Up - Checkpoint 5', ('Dash', 'Double Jump', 'Ground Pound')),
        ('Turn Up - Checkpoint 5', ('Attic Cody Ability', 'Attic May Ability', 'Dash', 'Ground Pound', 'Swinging', 'Wall Jump')),
        ('Turn Up - Checkpoint 5', ('Attic Cody Ability', 'Attic May Ability', 'Double Jump', 'Ground Pound', 'Swinging', 'Wall Jump')),
    ],
    'Turn Up - Checkpoint 7': [
        ('Turn Up - Checkpoint 6', ('Dash', 'Double Jump', 'Ground Pound')),
        ('Turn Up - Checkpoint 6', ('Attic Cody Ability', 'Attic May Ability', 'Dash', 'Ground Pound', 'Swinging', 'Wall Jump')),
        ('Turn Up - Checkpoint 6', ('Attic Cody Ability', 'Attic May Ability', 'Double Jump', 'Ground Pound', 'Swinging', 'Wall Jump')),
    ],
    'Turn Up Complete': [
        ('Turn Up - Checkpoint 1', ('Attic Cody Ability', 'Dash')),
        ('Turn Up - Checkpoint 7', ('Dash', 'Double Jump', 'Ground Pound')),
        ('Turn Up - Checkpoint 7', ('Attic Cody Ability', 'Attic May Ability', 'Dash', 'Ground Pound', 'Swinging', 'Wall Jump')),
    ],
}


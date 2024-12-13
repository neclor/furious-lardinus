import pygame

import settings as Settings
import core.resource_manager as ResourceManager


BASE_TILE: dict = {
	"groups": {"Tile"},
	"class": "Tile",
	"collision_layer": Settings.WALL,
	"collidable": True,
	"static": True,
	"transparent": False,
	"texture": None,
	"position_z": 0.0,
	"height": 128,
	}


TRANSPARENT_TILE: dict = BASE_TILE | {
	"class": "TransparentTile",
	"collision_layer": Settings.OBSTACLE,
	"transparent": True,
}


SECRET_TILE: dict = BASE_TILE | {
	"class": "SecretTile",
	"collidable": False,
}


TILE_SET: dict = {
	"tile_size": pygame.Vector2(64, 64),
	"tiles": {
		"<": BASE_TILE | {
			"texture": pygame.image.load("src/assets/sprites/tiles/wall_move.png"),
		},
		"=": BASE_TILE | {
			"texture": pygame.image.load("src/assets/sprites/tiles/wall_weapons.png"),
		},
		"+": BASE_TILE | {
			"texture": pygame.image.load("src/assets/sprites/tiles/wall_shoot.png"),
		},
		">": BASE_TILE | {
			"texture": pygame.image.load("src/assets/sprites/tiles/wall_secret_tutorial.png"),
		},
		"1": BASE_TILE | {
			"texture": pygame.image.load("src/assets/sprites/tiles/wall_64_128.png"),
		},
		"#": TRANSPARENT_TILE | {
			"texture": pygame.image.load("src/assets/sprites/tiles/wall_transparent.png"),
		},
		"?": SECRET_TILE | {
			"texture": pygame.image.load("src/assets/sprites/tiles/secret_wall_64_128.png"),
		},
		"$": BASE_TILE | {
			"texture": pygame.image.load("src/assets/sprites/tiles/secret_message.png"),
		},
		"!": BASE_TILE | {
			"texture": pygame.image.load("src/assets/sprites/tiles/end_tile.png"),
		},


	}
}


OBJECT_SET: dict = {
	"objects": {
        "A": "Ammo",
		"M": "Medikit",
        "K": "Knight",
        "C": "Skull",
        "U": "Summoner",
        "W": "Wizzard",
        "E": "Exit",
	}
}


TUTORIAL_ROOM: str = '''
Tutorial/
#8D697A/
1111111=1+11/
1....1.....1/
1..E.#.....1/
1....1.S...</
1.1111.....1/
1..........1/
11111111?>11/
.....111.111/
...111A...A1/
...1K#..M..1/
...111A...A1/
.....1111111/
'''


B_37: str = '''
B37/
#0D2B45/
...11111111111111................................../
...1A...W1W....A1................................../
...1MU...1..U..M1................................../
...1.....1......111111$111111111111111111111111111./
...11111K1K111111....1MA1..U..1..W.1..1W..A1C...W1./
...1.................1AM?.....1....1..1...U1.....1./
...11111K1K1111111.M.11111111.1K1111.11.11111.1111./
...1.....1.....1.1.M.....W..........W.........A..1./
...1W...W1W...W111...1111111111111111111111111.1111/
...1111111111111.CC..1MM.....A.....U...A.....1A1.K1/
...............1.CC..1AA...U.....M........M..1....1/
...............111.1.1...W..K.......W........1A1.M1/
...............1...1.1.........U...K...U.....1.1..1/
...............1..K1W1....M...K...........W..1.1.U1/
...............1...1.1....A.......W..A.......1W1111/
...............1...1.1111.....U.........K....1.1.../
...............1A..1....1W.........M.........1.1.../
...............1...1.1..1..A.............A...1.1.../
...............1...1.1UA1....U...W.....M.....1K1.../
...............1...1W1111......K.............1.1.../
...............1..W1.1......K..A...U...K.....1K1.../
...............1...1.1.......................1M1.../
....1111111111111111.1..1111W.......M....W...1K1.../
....1....W...........1111..1A...W....A.......1M1.../
....1......................?MA............U..?K1.../
.1111.111..............K...1111111111111111111.1.../
1M......M1..111.111..........#W.E......MM...C..1.../
1....K...1..1......1........11111111111111111111.../
1........1..1K...K1........1......................./
1K..W.W.K1.....U.11111...111......................./
.1......111111AAA1...1.S.1........................./
.1.U.M..1.....111.....###........................../
..111111.........................................../
'''


END_ROOM: str = '''
END/
#203C56/
11111!111111/
1A.......A1/
1.........1/
1M.......M1/
1.........1/
!....S....!/
1.........1/
1M.......M1/
1.........1/
1A.......A1/
11111!111111/
'''




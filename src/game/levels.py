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
	"height": 64,
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
		"1": BASE_TILE | {
			"texture": ResourceManager.load_image("src/assets/sprites/wall_32.png"),
		},
		"#": TRANSPARENT_TILE | {
			"texture": ResourceManager.load_image("src/assets/sprites/wall_32_t.png"),
		},
		"?": SECRET_TILE | {
			"texture": ResourceManager.load_image("src/assets/sprites/wall_32.png"),
		}
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
	}
}


HUB: str = '''
HUB/
#ffffff/
....?.....1/
?....1....1/
..#S.1.K..1/
.....1....1/
.#.#.1....1/
'''


BACKROOMS: str = '''
#523c0b/





'''



TEST_LEVEL_1 = [
	"..........#....@",
	"##..#@#...#....@",
	".#........@....@",
	".###.###..#....@",
	"...#...#..#....@",
	"...###.####....@",
	".....#..........",
	".....###########",
]

TEST_LEVEL = [
	"................................",
	"................................",
	"................................",
	"................................",
	"................................",
	"................................",
	"................................",
	"................................",
	"#..#...........#................",
	".#..#..........#................",
	"..#..#.........#................",
	"...#..#........#................",
	"....#..#.......#................",
	".....#..#......#................",
	"......#..###.###................",
]

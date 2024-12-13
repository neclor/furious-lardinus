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
		"#": BASE_TILE | {
			"texture": ResourceManager.load_image("src/assets/sprites/wall_32.png"),
		},
		"@": {
			"transparent": True,
			"texture": ResourceManager.load_image("src/assets/sprites/wall_32_t.png"),
			"height": 64,
			"position_z" : 0.0,
		},
		"$": {
			"texture": ResourceManager.load_image("src/assets/sprites/wall_32.png"),
			"height": -64,
			"position_z" : -32.0},
		"1": {
			"texture": ResourceManager.load_image("src/assets/sprites/wall_32.png"),
			"height": 8,
			"position_z" : 0.0},
		"2": {
			"texture": ResourceManager.load_image("src/assets/sprites/wall_32.png"),
			"height": 4,
			"position_z" : 0.0},
	}
}



OBJECT_SET: dict = {
	"objects": {
		"M": "Medikit",
	}
}


HUB: str = '''
#ffffff/
.........../
.........../
....S....../
.........../
...........
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

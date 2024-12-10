import pygame


import game.objects.medikit as Medikit


TEST_LEVEL = [
	"...###.####....@",
	"##.###....#....@",
	".#...#....#....@",
	".###.###..#....@",
	"...#...#..#....@",
	"...###.####....@",
	".....#..........",
	".....###########",
]

TEST_LEVEL_2 = [
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

DUNGEON_TILE_SET: dict = {
	"tile_size": pygame.Vector2(32, 32),
	"tiles": {
		"#": {
			"texture": pygame.image.load("src/assets/sprites/wall_32.png"),
			"height": 32,
			"position_z" : 0.0},
		"@": {
			"texture": pygame.image.load("src/assets/sprites/wall_32.png"),
			"height": 64,
			"position_z" : 0.0},
		"$": {
			"texture": pygame.image.load("src/assets/sprites/wall_32.png"),
			"height": -64,
			"position_z" : -32.0},
		"1": {
			"texture": pygame.image.load("src/assets/sprites/wall_32.png"),
			"height": 8,
			"position_z" : 0.0},
		"2": {
			"texture": pygame.image.load("src/assets/sprites/wall_32.png"),
			"height": 4,
			"position_z" : 0.0},
	}
}
DUNGEON_OBJECT_SET: dict = {
	"objects": {
		"M": "Medikit",
	}
}


def load_level(data: list[str], tile_set: dict, object_set: dict) -> tuple[pygame.Vector2, pygame.Vector2, list[list[dict | None]], list[dict]]:
	tile_size: pygame.Vector2 = tile_set["tile_size"]
	tiles: dict = tile_set["tiles"]
	objects: dict = object_set["objects"]

	tile_map: list[list[dict | None]] = []
	object_conatiner: list[dict] = []
	y: int = 0
	x: int = 0
	for y, row in enumerate(data):
		tile_row: list[dict | None] = []
		for x, char in enumerate(row):
			game_object: dict | None = create_object(objects.get(char))
			if game_object is not None:
				game_object["position"] = pygame.Vector2(x * tile_size.x + tile_size.x / 2, y * tile_size.y + tile_size.y / 2)
				print(game_object["position"])
				object_conatiner.append(game_object)
			tile: dict | None = tiles.get(char)
			tile_row.append(tile)
		tile_map.append(tile_row)
	tile_map_size: pygame.Vector2 = pygame.Vector2(x + 1, y + 1)
	return (tile_size, tile_map_size, tile_map, object_conatiner)


def create_object(class_name: str | None) -> dict | None:
	match class_name:
		case "Medikit":
			return Medikit.new()
		case _:
			return None

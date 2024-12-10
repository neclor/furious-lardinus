import pygame

import game.game as Game
import game.levels as Levels


skybox: pygame.Surface = pygame.Surface((0, 0))
floor_color: pygame.Color = pygame.Color("#000000")

tile_size: pygame.Vector2 = pygame.Vector2()
tile_map_size: pygame.Vector2 = pygame.Vector2()
tile_map: list[list[dict | None]] = []

min_point_z: float = -64
max_point_z: float = 0


def change_level() -> None:
	global tile_size, tile_map_size, tile_map
	tile_size, tile_map_size, tile_map, Game.object_container = Levels.load_level(Levels.TEST_LEVEL, Levels.DUNGEON_TILE_SET, Levels.DUNGEON_OBJECT_SET)
	Game.object_container.append(Game.player)

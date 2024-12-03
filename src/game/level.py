import pygame

import game.game as Game
import game.levels as Levels


tile_size: pygame.Vector2 = pygame.Vector2()
tile_map_size: pygame.Vector2 = pygame.Vector2()
tile_map: list[list[dict | None]] = []

floor_color: pygame.Color | None = pygame.Color("#000000")


def change_level() -> None:
	global tile_size, tile_map_size, tile_map
	tile_size, tile_map_size, tile_map, Game.object_container = Levels.load_level(Levels.TEST_LEVEL, Levels.DUNGEON_TILE_SET, Levels.DUNGEON_OBJECT_SET)
	Game.object_container.append(Game.player)

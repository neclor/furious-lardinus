from typing import Tuple
import pygame

import settings as Settings
import game.rendering.display as Display
import game.game as Game


offset: pygame.Vector2 = pygame.Vector2(0.0, 0.0)
camera_position: pygame.Vector2 = pygame.Vector2(0.0, 0.0)


def init() -> None:
	global offset, camera_position
	offset = pygame.Vector2(Display.surface.get_size()) / 2
	camera_position = pygame.Vector2(0.0, 0.0)


def update() -> None:
	global camera_position
	camera_position = Game.player["position"]
	draw()


def draw() -> None:
	draw_level()
	draw_objects()
	draw_player()



def draw_level() -> None:
	camera_position
	screen_tile_size: float = Game.level["tile_size"] * Settings.SCALE
	y: float = offset.y - (camera_position.y * Settings.SCALE)
	screen_offset_x = offset.x - (camera_position.x * Settings.SCALE)
	for row in Game.Levels.b37_0["tile_map"]:
		x: float = screen_offset_x
		for tile in row:
			if tile is not None:
				Display.surface.blit(pygame.transform.scale_by(tile["texture"], Settings.SCALE), (x, y))
			x += screen_tile_size
		y += screen_tile_size


def draw_objects() -> None:
	for object in Game.object_container:
		draw_object(object)



def draw_player() -> None:
	draw_object(Game.player)



def draw_object(object: dict) -> None:
	screen_position: pygame.Vector2 = (object["position"] - camera_position) * Settings.SCALE + offset

	if Settings.VISIBLE_COLLISION:
		pygame.draw.circle(Display.surface, Settings.DEBUG_COLOR, screen_position, object["radius"] * Settings.SCALE)

	transformed_sprite: pygame.Surface = pygame.transform.scale_by(object["sprite"], Settings.SCALE)
	Display.surface.blit(transformed_sprite, screen_position - pygame.Vector2(transformed_sprite.get_size()) / 2)

import pygame

import settings as Settings
import game.rendering.display as Display
import game.game as Game


display_surface_center: pygame.Vector2 = pygame.Vector2()
camera_position: pygame.Vector2 = pygame.Vector2()


def init() -> None:
	global display_surface_center, camera_position
	display_surface_center = pygame.Vector2(Display.surface.get_size()) / 2
	camera_position = pygame.Vector2()


def update() -> None:
	global camera_position
	camera_position = Game.player["position"]
	draw()


def draw() -> None:
	draw_level()
	draw_objects()


def draw_level() -> None:
	tile_size: pygame.Vector2 = Game.level["tile_size"]
	tile_map: list[list[dict | None]] = Game.Levels.b37_0["tile_map"]

	scaled_tile_size: float = tile_size.x * Settings.SCALE

	tile_position_y: float = display_surface_center.y - (camera_position.y * Settings.SCALE)
	surface_offset_x = display_surface_center.x - (camera_position.x * Settings.SCALE)
	for row in tile_map:
		tile_position_x: float = surface_offset_x
		for tile in row:
			if tile is not None:
				Display.surface.blit(pygame.transform.scale_by(tile["texture"], Settings.SCALE), (tile_position_x, tile_position_y))
			tile_position_x += scaled_tile_size
		tile_position_y += scaled_tile_size


def draw_objects() -> None:
	for object in Game.object_container:
		draw_object(object)


def draw_object(object: dict) -> None:

	def scale_and_draw(surface: pygame.Surface, center_position: pygame.Vector2, ) -> None:
		scaled_surface: pygame.Surface = pygame.transform.scale(surface, pygame.Vector2(surface.get_size()) *Settings.SCALE) # pygame.Vector2(surface.get_size()) *
		surface_offset: pygame.Vector2 = pygame.Vector2(scaled_surface.get_size()) / 2
		position: pygame.Vector2 = display_surface_center + (center_position - camera_position) * Settings.SCALE - surface_offset
		Display.surface.blit(scaled_surface, position)

	position: pygame.Vector2 = object["position"]
	radius: int = object["radius"]
	sprite = object["sprite"]

	scale_and_draw(sprite, position)

	if Settings.VISIBLE_COLLISION:
		diameter: int = radius * 2
		circle_surface = pygame.Surface((100, 100), pygame.SRCALPHA)
		pygame.draw.circle(circle_surface, Settings.DEBUG_COLOR, (50, 50), radius)

		scale_and_draw(circle_surface, position)

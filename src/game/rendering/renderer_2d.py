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
	draw_enemies()
	draw_object(Game.player)
	draw_projectiles()


def draw_level() -> None:
	pass


def draw_objects() -> None:
	for object in Game.objects_container:
		draw_object(object)


def draw_enemies() -> None:
	for enemy in Game.enemies_container:
		draw_object(enemy)


def draw_projectiles() -> None:
	for projectile in Game.projectiles_container:
		draw_object(projectile)


def draw_object(object: dict) -> None:
	screen_position: pygame.Vector2 = (object["position"] - camera_position) * Settings.SCALE + offset

	if Settings.VISIBLE_COLLISION:
		pygame.draw.circle(Display.surface, Settings.DEBUG_COLOR, screen_position, object["radius"] * Settings.SCALE)

	transformed_sprite: pygame.Surface = pygame.transform.scale_by(object["sprite"], Settings.SCALE)
	Display.surface.blit(transformed_sprite, screen_position - pygame.Vector2(transformed_sprite.get_size()) / 2)

import pygame

import settings as Settings
import game.rendering.display as Display
import game.game as Game



def init() -> None:
	pass


def update() -> None:
	pass




def ray_cast() -> None:
	ray_rotation: float = Game.player["rotation"] - Settings.FOV_H / 2
	for ray in range(Settings.RAYS_NUMBER):
		ray_rotation =+ Settings.FOV_H / Settings.RAYS_NUMBER
		draw_walls(ray_rotation, Game.player["position"])


def draw_walls(angle: float) -> None:

	for row in Game.level["tile_map"]:
		for tile in row:
			if tile is not None:
				Display.surface.blit(pygame.transform.scale_by(tile["texture"], Settings.SCALE), (x, y))

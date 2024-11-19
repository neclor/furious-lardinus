import pygame

import settings as Settings
import game.rendering.display as Display
import game.game as Game


def init() -> None:
	pass


def update() -> None:
	pass




def ray_cast() -> None:


	ray_rotation: float = Game.player["roattion"] - Settings.FOV_H / 2
	for ray in range(Settings.RAYS_NUMBER):
		pass

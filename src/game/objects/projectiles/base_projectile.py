import pygame

import game.objects.base_object as BaseObject


def new() -> dict:
	projectile: dict = {
		"class": "BaseProjectile",
		"velocity": pygame.Vector2(0.0, 0.0),
		"damage": 100}

	return projectile

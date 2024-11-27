import pygame

import game.objects.base_object as BaseObject


def new(position: pygame.Vector2 = pygame.Vector2()) -> dict:
	projectile: dict = {
		"class": "BaseProjectile",
		"velocity": pygame.Vector2(),
		"damage": 100}

	return BaseObject.new(position) | projectile

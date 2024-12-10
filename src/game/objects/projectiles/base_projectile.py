import pygame

import game.objects.base_object as BaseObject


def new(velocity: pygame.Vector2, damage: int, position: pygame.Vector2 = pygame.Vector2()) -> dict:
	projectile: dict = {
		"group": "Projectile",
		"class": "BaseProjectile",
		"velocity": velocity,
		"damage": damage}

	return BaseObject.new(position) | projectile


def update(self: dict, delta: float) -> None:
	pass

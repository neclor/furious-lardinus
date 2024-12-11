import pygame

import game.objects.base_object as BaseObject


def new(position: pygame.Vector2, velocity: pygame.Vector2, damage: int) -> dict:
	base_projectile: dict = {
		"group": "Projectile",
		"class": "BaseProjectile",
		"velocity": velocity,
		"damage": damage,
	}
	return BaseObject.new(position) | base_projectile


def update(self: dict, delta: float) -> None:
	pass

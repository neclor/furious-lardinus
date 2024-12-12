import pygame


import game.objects.dynamic_objects.base_dynamic_object as BaseDynamicObject


def new(position: pygame.Vector2, velocity: pygame.Vector2, damage: int) -> dict:
	base_projectile: dict = {
		"group": "Projectile",
		"class": "BaseProjectile",

		"velocity": velocity,

		"damage": damage,
	}
	return BaseDynamicObject.new(position) | base_projectile


def update(self: dict, delta: float) -> None:
	pass

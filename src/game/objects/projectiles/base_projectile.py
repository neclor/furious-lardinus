import pygame

import game.objects.base_object as BaseObject


def new() -> dict:
	projectile: dict = {
		"class": "BaseProjectile",
		"velocity": pygame.Vector2(0.0, 0.0)}

	return BaseObject.new() | projectile


def update(self: dict, delta: float) -> None:
	pass



def move(self: dict, delta: float) -> None:
	self["position"] = pygame.Vector2(self["position"]) + self["velocity"] * delta

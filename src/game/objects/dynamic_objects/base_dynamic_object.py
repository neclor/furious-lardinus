import pygame


import game.objects.base_object as BaseObject


def new(position: pygame.Vector2 = pygame.Vector2()) -> dict:
	a: set
	base_dynamic_object: dict = {
		"group": "DynamicObject",
		"class": "BaseDynamicObject",

		"static": False,

		"velocity": pygame.Vector2(),
	}
	return BaseObject.new(position) | base_dynamic_object


def move_and_slide(self: dict, delta: float) -> None:
	self["position"] += self["velocity"] * delta

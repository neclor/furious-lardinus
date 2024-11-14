import pygame


def new() -> dict:
	object: dict = {
		"class": "BaseObject",
		"position": pygame.Vector3(0.0, 0.0, 0.0),
		"radius": 16,
		"height": 32,
		"sprite": None,
		"collision": False}

	return object


def update(self: dict, delta: float) -> None:
	pass

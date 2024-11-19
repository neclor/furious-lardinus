import pygame

import game.game as Game


def new() -> dict:
	object: dict = {
		"class": "BaseObject",
		"sprite": None,
		"collision": False,

		"position": pygame.Vector2(0.0, 0.0),
		"radius": 8,

		"position_z": 0.0,
		"height": 32}

	return object


def overlaps_object(self: dict, object: dict) -> bool:
	return circles_overlap(self["position"], self["radius"], object["position"], object["radius"])


def circles_overlap(position_1: pygame.Vector2, radius_1: int, position_2: pygame.Vector2, radius_2: int) -> bool:
	return position_1.distance_to(position_2) <= radius_1 + radius_2


def free(self: dict) -> None:
	Game.object_container.remove(self)

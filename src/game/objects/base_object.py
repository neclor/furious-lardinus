import pygame

import game.game as Game


def new(position: pygame.Vector2 = pygame.Vector2()) -> dict:
	object: dict = {
		"class": "BaseObject",
		"sprite": None,
		"collision": False,

		"position": position,
		"radius": 8,

		"position_z": 0.0,
		"height": 32}

	return object


def overlaps_object(self: dict, object: dict) -> bool:
	return self["position"].distance_to(object["position"]) < self["radius"] + object["radius"]


def free(self: dict) -> None:
	Game.object_container.remove(self)

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


def collides_object(self: dict, object: dict) -> bool:
	dist: float = self["position"].dist(object["position"])
	return dist <= self["radius"] + object["radius"]


def free(self: dict) -> None:
	Game.object_container.remove(self)

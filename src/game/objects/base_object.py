import pygame

import game.game as Game


def new(position: pygame.Vector2 = pygame.Vector2()) -> dict:
	base_object: dict = {
		"group": "Object",
		"class": "BaseObject",
		"sprite": None,
		"collision": False,

		"position": position,
		"radius": 4,

		"position_z": 0.0,
		"height": 16,
	}
	return base_object


def overlaps_object(self: dict, game_object: dict) -> bool:
	return self["position"].distance_to(game_object["position"]) < self["radius"] + game_object["radius"]


def free(self: dict) -> None:
	Game.object_container.remove(self)

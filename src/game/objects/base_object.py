import pygame

import game.game as Game


def new(position: pygame.Vector2 = pygame.Vector2()) -> dict:
	game_object: dict = {
		"class": "BaseObject",
		"sprite": None,
		"collision": False,

		"position": position,
		"radius": 8,

		"height": 16,
		"position_z": 0.0}

	return game_object


def overlaps_object(self: dict, game_object: dict) -> bool:
	return self["position"].distance_to(game_object["position"]) < self["radius"] + game_object["radius"]


def free(self: dict) -> None:
	Game.object_container.remove(self)

import pygame


def new() -> dict:
	new_game_object: dict = {
		"position": pygame.Vector3(0.0, 0.0, 0.0),
		"radius": 16,
		"height": 32,
		"sprite": None,}

	return new_game_object

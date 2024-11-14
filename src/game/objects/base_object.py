import pygame
import game


def new() -> dict:
	base_object: dict = {
		"position": pygame.Vector3(0.0, 0.0, 0.0),
		"radius": 16,
		"height": 32,
		"sprite": None}

	return base_object

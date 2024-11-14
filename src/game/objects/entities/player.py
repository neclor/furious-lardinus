import pygame
import game.objects.entities.base_entity as base_entity


def new() -> dict:
	new_player: dict = base_entity.new()
	new_player["rotation"] = 0.0
	new_player["max_stamina"] = 100
	new_player["stamina"] = new_player["max_stamina"]
	new_player["stamina_regen"] = 10

	return new_player

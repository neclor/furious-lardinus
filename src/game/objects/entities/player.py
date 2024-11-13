import pygame
import game.objects.entities.entity as entity


def new() -> dict:
	new_player: dict = entity.new()
	new_player["rotation"] = 0.0

	return new_player

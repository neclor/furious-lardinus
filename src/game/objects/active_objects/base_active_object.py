import pygame


import game.game as Game
import game.object_system.base_object as BaseObject


def new(position: pygame.Vector2 = pygame.Vector2()) -> dict:
	base_interactive_object: dict = {
		"group": "InteractiveObject",
		"class": "BaseInteractiveObject",
		"height": 4,
	}
	return BaseObject.new(position) | base_interactive_object


def overlaps_player(self: dict) -> bool:
	return BaseObject.overlaps_object(self, Game.player)

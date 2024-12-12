import pygame


import game.objects.interactive_objects.base_interactive_object as BaseInteractiveObject


def new(position: pygame.Vector2 = pygame.Vector2()) -> dict:
	base_exit: dict = {
		"group": "InteractiveObject",
		"class": "BaseExit",
	}
	return BaseInteractiveObject.new(position) | base_exit

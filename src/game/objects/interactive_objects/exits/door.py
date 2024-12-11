import pygame

import game.game as Game
import game.objects.interactive_objects.base_interactive_object as BaseInteractiveObject


DOOR_SPRITE: pygame.Surface = pygame.image.load("assets/sprites/objects/interactive_object/exits/door.png")


def new(position: pygame.Vector2 = pygame.Vector2()) -> dict:
	door: dict = {
		"group": "InteractiveObject",
		"class": "Door",
		"sprite": DOOR_SPRITE,
	}
	return BaseInteractiveObject.new(position) | door

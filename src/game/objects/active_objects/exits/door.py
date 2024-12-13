import pygame


import game.object_class_manager as ObjectClassManager
import game.object_manager as ObjectManager
import game.level_manager as LevelManager


import game.objects.active_objects.base_active_object as BaseActiveObject
import game.objects.active_objects.exits.base_exit as BaseExit


DOOR_SPRITE: pygame.Surface = pygame.image.load("assets/sprites/objects/interactive_object/exits/door.png")


def new(position: pygame.Vector2 = pygame.Vector2()) -> dict:
	return ObjectClassManager.new_object(BaseExit.new(position), {
		"class": "Door",

		"sprite": DOOR_SPRITE,
	})

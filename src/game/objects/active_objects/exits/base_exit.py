import pygame


import game.object_class_manager as ObjectClassManager
import game.object_manager as ObjectManager
import game.level_manager as LevelManager

import game.objects.active_objects.base_active_object as BaseActiveObject


def new(position: pygame.Vector2 = pygame.Vector2()) -> dict:
	return ObjectClassManager.new_object(BaseActiveObject.new(position), {
		"groups": "Exit",
		"class": "BaseExit",

		"radius": 16,

		"position_z": 0.0,
		"height": 48,
	})


def object_collided(self: dict, game_object: dict) -> None:
	groups: set = game_object["groups"]
	if "Player" in groups:
		pass

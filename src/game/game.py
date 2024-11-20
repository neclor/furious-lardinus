import sys
from typing import Tuple
import math
import pygame

import game.rendering.display as Display
import game.levels as Levels
import game.objects.base_object as BaseObject
#import game.objects.entities
import game.objects.entities.player as Player
import game.objects.medikit as Medikit

timer: float = 0.0
pause: bool = False


level: dict = Levels.b37_0



player: dict
object_container: list[dict] = []


def enter() -> None:
	init()
	Display.init()


def init() -> None:
	global timer, pause, object_container, player
	timer = 0.0
	pause = False
	object_container = []
	player = Player.new()

	create_objs()



def create_objs() -> None:
	med = Medikit.new()
	med["position"] = pygame.Vector2(-32, -32)
	object_container.append(med)




def update(delta: float) -> None:
	global timer
	timer += delta

	for object in object_container:
		match object["class"]:
			case "Medikit":
				Medikit.update(object, delta)

	Player.update(player, delta)
	Display.update()








def add_child(object: dict):
	object_container.append(object)




def exit() -> None:
	pass

import sys
from typing import Tuple
import math
import pygame

import game.rendering.display as Display
import game.levels as Levels
import game.objects.base_object as BaseObject
#import game.objects.entities
import game.objects.entities.player as Player


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


def update(delta: float) -> None:
	global timer
	timer += delta

	Player.update(player, delta)
	Display.update()


def exit() -> None:
	pass

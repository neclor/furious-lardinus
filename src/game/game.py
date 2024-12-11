import sys
import math
import pygame


import game.rendering.display as Display
import objects.class_manager as ClassManager
import game.level as Level

import game.objects.entities.player as Player



timer: float
pause: bool


player: dict
object_container: list[dict] = []


def enter() -> None:
	init()
	Display.init()


def init() -> None:
	global timer, pause, object_container, player
	timer = 0.0
	pause = False
	player = Player.new()
	object_container = [player]

	Level.change_level()

	hide_mouse()


def hide_mouse() -> None:
	pygame.mouse.set_visible(False)
	pygame.event.set_grab(True)


def toggle_pause() -> None:
	pause = not pause
	pygame.mouse.set_visible(pause)
	pygame.event.set_grab(not pause)


def update(delta: float) -> None:
	if pause: return

	global timer
	timer += delta
	for object in object_container:
		ClassManager.update(object, delta)

	Display.update()


def add_child(object: dict):
	object_container.append(object)


def exit() -> None:
	pass

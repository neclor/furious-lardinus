import sys
import math
import pygame


import game.object_manager as ObjectManager
import game.level_manager as LevelManager
import game.rendering.display as Display
import game.objects.dynamic_objects.entities.player as Player


timer: float
pause: bool


player: dict


def enter() -> None:
	global timer, pause
	timer = 0.0
	pause = False
	mouse_visible(False)
	Display.init()


def toggle_pause() -> None:
	pause = not pause
	mouse_visible(pause)


def mouse_visible(visible: bool) -> None:
	pygame.mouse.set_visible(visible)
	pygame.event.set_grab(not visible)


def start_game() -> None:
	global player
	player = Player.new()
	ObjectManager.add_object(player)


def update(delta: float) -> None:
	global timer
	if not pause:
		timer += delta
		ObjectManager.update(delta)
	Display.update()


def exit() -> None:
	pass

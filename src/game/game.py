import sys
import math
import pygame

import game.rendering.display as Display
import game.levels as Levels
import game.objects.base_object as BaseObject
import game.objects.entities.enemies.base_enemy as BaseEnemy
import game.objects.entities.player as Player
import game.objects.medikit as Medikit


timer: float = 0.0
pause: bool = False


floor_color: pygame.Color = pygame.Color("#000000")
tile_size: pygame.Vector2 = pygame.Vector2()
tile_map_size: pygame.Vector2 = pygame.Vector2()
tile_map: list[list[dict | None]] = []


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


	change_level()
	create_objs()


	pygame.mouse.set_visible(False)
	pygame.event.set_grab(True)



def pause_game() -> None:
	pause != pause
	pygame.mouse.set_visible(pause)
	pygame.event.set_grab(not pause)



def create_objs() -> None:
	object_container.append(Medikit.new(pygame.Vector2(-32, -32)))
	#object_container.append(BaseEnemy.new(pygame.Vector2(-32, -128)))


def change_level() -> None:
	global tile_size, tile_map_size, tile_map, object_container
	tile_size, tile_map_size, tile_map, object_container = Levels.load_level(Levels.TEST_LEVEL, Levels.DUNGEON_TILE_SET, Levels.DUNGEON_OBJECT_SET)
	object_container.append(player)



def update(delta: float) -> None:
	if pause:
		return

	global timer
	timer += delta

	for object in object_container:
		match object["class"]:
			case "Medikit":
				Medikit.update(object, delta)
			case "BaseEnemy":
				BaseEnemy.update(object, delta)

	Player.update(player, delta)
	Display.update()









def add_child(object: dict):
	object_container.append(object)

def exit() -> None:
	pass

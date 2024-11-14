import sys
from typing import Tuple
import math
import pygame

import game.levels as Levels
import game.objects.object as Object
#import game.objects.entities
import game.objects.entities.player as Player


timer: float = 0.0
pause: bool = False


level: dict


objects: list[dict] = []
enemies: list[dict] = []
projectiles: list[dict] = []
player: dict


def enter() -> None:
	global timer, pause, objects, enemies, projectiles, player
	timer = 0.0
	pause = False
	objects = []
	enemies = []
	projectiles = []
	player = Player.new()


def update(delta: float) -> None:
	global timer

	timer += delta

	Player.update(player, delta)


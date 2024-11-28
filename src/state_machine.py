import pygame

import menu.menu as Menu
import game.game as Game


# States
MENU: int = 0
GAME: int = 1

INITIAL_STATE: int = MENU
state: int = -1


def init() -> None:
	change_state(INITIAL_STATE)


def update(delta: float) -> None:
	match state:
		case 0: Menu.update(delta)
		case 1: Game.update(delta)


def change_state(new_state: int) -> None:
	global state
	if (new_state == state) or (new_state < 0 or 1 < new_state):
		return

	match state:
		case 0: Menu.exit()
		case 1: Game.exit()

	state = new_state
	match state:
		case 0: Menu.enter()
		case 1: Game.enter()

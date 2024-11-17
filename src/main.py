# Furious Lardinus
# Authors:
# me, he and another one


import sys
import pygame

import settings as Settings
import game.game as Game


# States
MENU: int = 0
GAME: int = 1
state: int = MENU


clock: pygame.time.Clock


def main() -> None:
	init()
	run()


def init() -> None:
	global clock
	pygame.init()
	pygame.display.set_mode(Settings.RESOLUTION)
	pygame.display.set_caption(Settings.NAME)
	clock = pygame.time.Clock()

	change_state(GAME)


def run() -> None:
	while True:
		delta: float = clock.get_time() / 1000
		match state:
			case 0: # MENU
				pass # menu.update(delta)
			case 1: # GAME
				Game.update(delta)

		clock.tick(Settings.FPS)
		check_events()

		pygame.display.set_caption(str(round(clock.get_fps())))


def change_state(new_state: int) -> None:
	global state
	if new_state == state:
		return

	match new_state:
		case 0: # MENU
			state = MENU
			# menu.enter()
		case 1: # GAME
			state = GAME
			Game.enter()


def check_events() -> None:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		if event.type == Settings.FULL_SCREEN:
			pygame.display.toggle_fullscreen()


def exit() -> None:
	pygame.quit()
	sys.exit()


if __name__ == "__main__":
	main()

# Furious Lardinus
# Authors:
# me, he and another one


import sys
import pygame

import settings
import game.game as game


# States
MENU: int = 0
GAME: int = 1
state: int = 0


clock: pygame.time.Clock


def main() -> None:
	init()
	run()


def init() -> None:
	global clock
	pygame.init()
	pygame.display.set_mode(settings.RESOLUTION)
	pygame.display.set_caption(settings.NAME)
	clock = pygame.time.Clock()

	change_state(MENU)


def run() -> None:
	while True:
		delta: float = clock.get_time() / 1000
		match state:
			case 0: # MENU
				pass # menu.update(delta)
			case 1: # GAME
				game.update(delta)

		clock.tick(settings.FPS)
		check_events()


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
			game.enter()


def check_events() -> None:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()


def exit() -> None:
	pygame.quit()
	sys.exit()


if __name__ == "__main__":
	main()

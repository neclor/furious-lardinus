# Furious Lardinus
# Authors:
#
#
#


import sys
import pygame


import settings
import game


# States
MENU: int = 0
GAME: int = 1
state: int = GAME


clock: pygame.time.Clock


def main() -> None:
	init()
	run()


def init() -> None:
	pygame.init()
	pygame.display.set_mode(settings.RESOLUTION)
	pygame.display.set_caption(settings.NAME)
	global clock
	clock = pygame.time.Clock()


def run() -> None:
	while True:
		match state:
			case 0: # MENU
				# menu.update()
				pass
			case 1: # GAME
				game.update()
		check_events()


def change_state(new_state: int) -> None:
	global state
	if new_state == state:
		return

	match new_state:
		case 0: # MENU
			# menu.enter()
			state = MENU
			pass
		case 1: # GAME
			# game.enter()
			state = GAME
			pass


def check_events() -> None:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()


def exit() -> None:
	pygame.quit()
	sys.exit()


if __name__ == "__main__":
	main()

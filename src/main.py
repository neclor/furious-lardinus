import sys
import pygame
import settings
import enum



States: dict = {
	"MENU": 0,
	"GAME": 0,}




state: int = States["GAME"]



def main() -> None:
	init()
	run()


def init() -> None:
	pygame.init()
	pygame.display.set_mode(settings.RESOLUTION)
	pygame.display.set_caption(settings.NAME)


def run() -> None:
	while True:






		#menu
		#game
		check_events()


def check_events() -> None:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()


def exit() -> None:
	pygame.quit()
	sys.exit()


if __name__ == "__main__":
	main()

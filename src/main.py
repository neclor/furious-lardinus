# Furious Lardinus
# Authors:
# me, he and another one

#TODO: To finish
import sys
import pygame

import settings as Settings
import events as Events
import state_machine as StateMachine


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

	StateMachine.init()


def run() -> None:
	while True:
		delta: float = clock.get_time() / 1000
		Events.update()
		StateMachine.update(delta)

		handle_events()

		clock.tick(Settings.FPS)

		# for debug
		pygame.display.set_caption(str(round(clock.get_fps())))


def handle_events() -> None:
	for event in Events.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == Settings.FULL_SCREEN:
				pygame.display.toggle_fullscreen()


if __name__ == "__main__":
	main()

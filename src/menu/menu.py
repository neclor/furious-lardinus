import pygame


import state_machine as StateMachine



button_container: list[dict] = []


def enter() -> None:
	pygame.mouse.set_visible(False)
	pygame.event.set_grab(True)
	StateMachine.change_state(StateMachine.GAME)


def update(delta: float) -> None:







	pass


def check_buttons() -> None:
	for button in button_container:
		pass






def exit() -> None:
	pass

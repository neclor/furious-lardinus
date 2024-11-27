#TODO: To finish
import pygame

import state_machine as StateMachine


def enter() -> None:
	print("enter", StateMachine.state)
	StateMachine.change_state(StateMachine.GAME)
	print("enter", StateMachine.state)


def update(delta: float) -> None:
	pass


def exit() -> None:
	pass

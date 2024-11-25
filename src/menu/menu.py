#TODO: To finish
import pygame

import main as Main


def enter() -> None:
	print("enter", Main.state)
	Main.change_state(Main.GAME)
	print("enter", Main.state)


def update(delta: float) -> None:
	pass


def exit() -> None:
	pass

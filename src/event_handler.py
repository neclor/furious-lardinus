from typing import List
import pygame



events: List[Event]


def update() -> None:
	global events
    events = pygame.event.get()

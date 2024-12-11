import pygame


def create_button(rect: pygame.Rect, text: str = "") -> dict:
    button: dict = {
		"rect": rect,
		"hover": False,
		"font": None,
		"text": text,
	}
    return button

from typing import Tuple
import pygame

import settings as Settings
import game.rendering.renderer_2d as Renderer2D
import game.rendering.renderer_3d as Renderer3D
import game.rendering.hud as HUD


surface: pygame.Surface


def init() -> None:
	global surface
	surface = pygame.display.get_surface()

	Renderer2D.init()
	HUD.init()


def update() -> None:
	surface.fill(Settings.CLEAR_COLOR)

	Renderer2D.update()
	HUD.update()

	pygame.display.flip()

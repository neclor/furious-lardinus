import pygame

import settings as Settings
import game.rendering.renderer_3d_2 as Renderer3D
import game.rendering.hud as HUD


surface: pygame.Surface


def init() -> None:
	global surface
	surface = pygame.display.get_surface()

	#Renderer2D.init()
	HUD.init()


def update() -> None:
	surface.fill(Settings.CLEAR_COLOR)

	Renderer3D.update()
	#Renderer2D.update()
	HUD.update()

	pygame.display.flip()

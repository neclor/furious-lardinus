from typing import Tuple
import pygame

import game.game as Game


RED: Tuple[int, int, int] = (255, 0, 0)
GREEN: Tuple[int, int, int] = (0, 255, 0)
BLUE: Tuple[int, int, int] = (0, 0, 255)


surface: pygame.Surface

camera_position: pygame.Vector2 = pygame.Vector2(0.0, 0.0)
scale: float = 1.0


def init() -> None:
    global surface, camera_position, scale
    surface: pygame.Surface = pygame.display.get_surface()
    camera_position = Game.player["position"]
    scale = 1.0


def update() -> None:
    offset: pygame.Vector2 = Game.player["position"]






def draw_level(offset: pygame.Vector2) -> None:
    pass

def draw_objects() -> None:
    pass

def draw_enemies() -> None:
    pass

def draw_player() -> None:
    pass

import pygame
import inputs

def create_player() -> dict:
    return {
        'position':  pygame.Vector2(0.0, 0.0),
        'look_vec':  pygame.Vector2(0.0, 0.0),
        'direction': 0.0
    }



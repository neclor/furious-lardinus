# testing functions
import pygame

def keyboard(player: dict) -> None:
    keys = pygame.key.get_pressed()
    movement = pygame.Vector2(0.0, 0.0)
    if keys[pygame.K_z]:
        movement = player['look_vec'] * player['velocity']
    if keys[pygame.K_q]:
        player['position'] += 

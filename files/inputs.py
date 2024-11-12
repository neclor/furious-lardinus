# testing functions
import pygame

def keyboard(player: dict) -> None:
    keys = pygame.key.get_pressed()
    zero_vec = pygame.Vector2(0.0, 0.0)
    movement = zero_vec
    if keys[pygame.K_z]:
        movement += player['look_vec']
    if keys[pygame.K_q]:
        movement += pygame.Vector2(- player['look_vec'].y, player['look_vec'].x)
    if keys[pygame.K_d]:
        movement += pygame.Vector2(player['look_vec'].y, - player['look_vec'].x)
    if keys[pygame.K_s]:
        movement += - player['look_vec']
    if movement.x != 0.0 or movement.y != 0.0:
        movement = movement.normalize()
        player['position'] += player['velocity'] * movement


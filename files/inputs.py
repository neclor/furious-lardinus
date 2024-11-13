# testing functions
import pygame

TURNING_SPEED = 3.1416 * 2

def keyboard(player: dict, delta: float) -> None:
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
        player['position'] += delta * player['velocity'] * movement.normalize()

    if keys[pygame.K_RIGHT]:
        player['look_vec'] = player['look_vec'].rotate_rad(- TURNING_SPEED * delta)
    if keys[pygame.K_LEFT]:
        player['look_vec'] = player['look_vec'].rotate_rad(  TURNING_SPEED * delta)


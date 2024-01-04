import pygame
from src.settings import Config


class Controls:
    """ Initializes keyboard shortcuts as controls for the given object"""
    def __init__(self, object_to_control, move_left_px: int, move_right_px: int, move_up_px: int, move_down_px: int):

        self.pressed_keys = pygame.key.get_pressed()

        if self.pressed_keys[pygame.K_LEFT] and object_to_control.left > 0:
            object_to_control.move_ip(move_left_px, 0)

        if self.pressed_keys[pygame.K_RIGHT] and object_to_control.right < Config.WIDTH:
            object_to_control.move_ip(move_right_px, 0)

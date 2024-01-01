import pygame

from .settings import Config


class Controls:
    def __init__(self, object_to_control):
        self.keys = pygame.key.get_pressed()

        if self.keys[pygame.K_LEFT] and object_to_control.left > 0:
            object_to_control.move_ip(-5, 0)
        if self.keys[pygame.K_RIGHT] and object_to_control.right < Config.WIDTH:
            object_to_control.move_ip(5, 0)

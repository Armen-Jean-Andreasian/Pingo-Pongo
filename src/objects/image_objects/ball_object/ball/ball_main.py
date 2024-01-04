import pygame
from assets.images import BALL_IMAGE
from src.objects.image_objects.image_objects_interface import ImageObjects


class Ball(ImageObjects):
    image_path = BALL_IMAGE
    speed = [1, -1]

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(self.image_path)
        self.rect = self.image.get_rect()

    def get_figure(self):
        return self.rect

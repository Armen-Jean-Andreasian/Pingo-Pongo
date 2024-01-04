import pygame
from ..wall_top_size import WallTopSize


class WallTop(WallTopSize):
    def __init__(self):
        self.rect = pygame.Rect(self.left, self.top, self.width, self.height)

    def get_figure(self):
        return self.rect

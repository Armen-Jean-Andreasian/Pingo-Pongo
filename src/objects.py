import pygame
from .settings import Config
from images import BALL_IMAGE
from abc import ABC, abstractmethod


# Abstraction
class Objects(ABC):
    @abstractmethod
    def get_figure(self):
        pass


# Interfaces
class RectangularObjects(Objects):
    left: int
    top: int
    width: int
    height: int

    @abstractmethod
    def get_figure(self) -> pygame.Rect:
        pass


class ImageObjects(Objects):
    image_path: str

    @abstractmethod
    def get_figure(self) -> pygame.Rect:
        pass


# Classes
class Ball(ImageObjects):
    image_path = BALL_IMAGE
    speed = [1, -1]

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(self.image_path)
        self.rect = self.image.get_rect()

    def get_figure(self):
        return self.rect


class Slider(RectangularObjects):
    left = Config.WIDTH // 2 - 50
    top = Config.HEIGHT - 30
    width = 100
    height = 10

    def __init__(self):
        self.rect = pygame.Rect(self.left, self.top, self.width, self.height)

    def get_figure(self):
        return self.rect


class WallTop(RectangularObjects):
    left = 0
    top = 0
    width = Config.WIDTH
    height = 5

    def __init__(self):
        self.rect = pygame.Rect(self.left, self.top, self.width, self.height)

    def get_figure(self):
        return self.rect

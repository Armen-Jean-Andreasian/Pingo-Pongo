import pygame
from .settings import Config
from abc import ABC, abstractmethod


class GeometricObjects(ABC):
    @abstractmethod
    def get_rect(self):
        pass


class Ball(GeometricObjects):
    speed = [1, -1]

    def __init__(self):
        left = Config.WIDTH // 2 - 15
        top = Config.HEIGHT // 2 - 15
        width = 30
        height = 30
        self.rect = pygame.Rect(left, top, width, height)

    def get_rect(self):
        return self.rect


class Slider(GeometricObjects):
    def __init__(self):
        left = Config.WIDTH // 2 - 50
        top = Config.HEIGHT - 30
        width = 100
        height = 10
        self.rect = pygame.Rect(left, top, width, height)

    def get_rect(self):
        return self.rect


class WallTop(GeometricObjects):
    def __init__(self):
        left = 0
        top = 0
        width = Config.WIDTH
        height = 5
        self.rect = pygame.Rect(left, top, width, height)

    def get_rect(self):
        return self.rect

import pygame
from ..abs_objects import Objects
from abc import abstractmethod


class RectangularObjects(Objects):
    left: int
    top: int
    width: int
    height: int

    @abstractmethod
    def get_figure(self) -> pygame.Rect:
        pass

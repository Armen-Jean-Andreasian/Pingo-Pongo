import pygame
from ..abs_objects import Objects
from abc import abstractmethod


class ImageObjects(Objects):
    image_path: str

    @abstractmethod
    def get_figure(self) -> pygame.Rect:
        pass

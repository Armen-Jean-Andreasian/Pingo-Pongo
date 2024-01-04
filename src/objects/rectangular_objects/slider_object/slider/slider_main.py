import pygame
from src.objects.rectangular_objects.slider_object.slider_movement import SliderMovement
from src.objects.rectangular_objects.slider_object.slider_size import SliderSize


class Slider(SliderMovement, SliderSize):

    def __init__(self):
        self.rect = pygame.Rect(self.left, self.top, self.width, self.height)

    def get_figure(self):
        return self.rect

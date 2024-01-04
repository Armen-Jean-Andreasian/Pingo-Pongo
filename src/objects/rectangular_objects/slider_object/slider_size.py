from src.settings import Config
from .slider_base import SliderBase


class SliderSize(SliderBase):
    left = Config.WIDTH // 2 - 50
    top = Config.HEIGHT - 30
    width = 100
    height = 10

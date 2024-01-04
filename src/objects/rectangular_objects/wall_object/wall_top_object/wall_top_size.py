from src.settings import Config
from .wall_top_base import WallTopBase


class WallTopSize(WallTopBase):
    left = 0
    top = 0
    width = Config.WIDTH
    height = 5

import pygame
from .settings import Config


class Screen:
    def __init__(self, game_name):
        self.screen = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
        self.font = pygame.font.Font(None, 36)
        pygame.display.set_caption(game_name)
        self.clock = pygame.time.Clock()

    def update(self, figures: tuple, score: int, speed: int, speed_multiplier: float) -> None:
        self.screen.fill(Config.BLACK)

        for figure_type, figure_data in figures:
            if figure_type == 'rects':
                for rectangle_figure in figure_data:
                    pygame.draw.rect(self.screen, Config.WHITE, rectangle_figure)
            elif figure_type == 'images':
                for image_figure in figure_data:
                    self.screen.blit(image_figure.image, image_figure.rect)

        # Score Text
        score_text = self.font.render("Score: {}".format(score), True, Config.WHITE)
        self.screen.blit(score_text, (20, 20))

        # Multiplier Text
        multiplier_text = self.font.render("Multiplier: {}".format(speed_multiplier), True, Config.WHITE)
        self.screen.blit(multiplier_text, (310, 20))

        # Speed Text
        speed_text = self.font.render("Speed: {}".format(speed), True, Config.WHITE)
        self.screen.blit(speed_text, (650, 20))

        pygame.display.flip()

    def tick_fps(self, fps_count) -> None:
        self.clock.tick(fps_count)

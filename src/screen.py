import pygame
from .settings import Config
from images import BALL_IMAGE


class DisplayMessageOnScreen:
    text_message = str()
    antialias = True
    color = Config.WHITE
    text_position = (Config.WIDTH // 2 - 50, Config.HEIGHT // 2 - 20)

    def show(self, font: pygame.font.Font, screen: pygame.Surface):
        """Shows a message screen such as Game Over Screen, You Won Screen"""
        custom_text = font.render(self.text_message, self.antialias, self.color)
        screen.blit(custom_text, self.text_position)


class GameOverScreen(DisplayMessageOnScreen):
    text_message = "Game Over"

    def show(self, font: pygame.font.Font, screen: pygame.Surface):
        super().show(font=font, screen=screen)


class YouWonScreen(DisplayMessageOnScreen):
    text_message = "You Won!"

    def show(self, font: pygame.font.Font, screen: pygame.Surface):
        super().show(font=font, screen=screen)


class ScreenBase:
    def __init__(self, game_name):
        self.screen = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
        self.font = pygame.font.Font(None, 36)
        # game name : Pingo-pongo
        pygame.display.set_caption(game_name)
        # game window logo : Ball from images
        icon_image = pygame.image.load(BALL_IMAGE)
        pygame.display.set_icon(icon_image)
        self.clock = pygame.time.Clock()

    def display_text(self, static_text: str, dynamic_text: str | int | float,
                     color: tuple[int], dest: tuple[int, int], antialias: bool = True) -> None:
        text = f"{static_text}: {dynamic_text}"

        text_to_display = self.font.render(text, antialias, color)
        self.screen.blit(text_to_display, dest=dest)

    def tick_fps(self, fps_count) -> None:
        self.clock.tick(fps_count)


class Screen(ScreenBase):

    def update(self, figures: tuple, score: int, speed: int, speed_multiplier: float,
               game_over_status: bool = False, player_won_status: bool = False) -> None:

        self.screen.fill(Config.BLACK)

        for figure_type, figure_data in figures:
            if figure_type == 'rects':
                for rectangle_figure in figure_data:
                    pygame.draw.rect(self.screen, Config.WHITE, rectangle_figure)
            elif figure_type == 'images':
                for image_figure in figure_data:
                    self.screen.blit(image_figure.image, image_figure.rect)

        # Score Text
        self.display_text(static_text="Score", dynamic_text=score, color=Config.WHITE, dest=(20, 20))

        # Multiplier Text
        self.display_text(static_text="Multiplier", dynamic_text=speed_multiplier, color=Config.WHITE,
                          dest=(310, 20))

        # Speed Text
        self.display_text(static_text="Speed", dynamic_text=speed, color=Config.WHITE, dest=(650, 20))

        if game_over_status:
            self.screen.fill(Config.BLACK)
            GameOverScreen().show(font=self.font, screen=self.screen)

        if player_won_status:
            self.screen.fill(Config.BLACK)
            YouWonScreen().show(font=self.font, screen=self.screen)

        pygame.display.flip()

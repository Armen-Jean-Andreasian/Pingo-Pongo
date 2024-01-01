import pygame
from .settings import Config



class Screen:
    def __init__(self, game_name):
        self.screen = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
        self.font = pygame.font.Font(None, 36)
        pygame.display.set_caption(game_name)
        self.clock = pygame.time.Clock()

    def update(self, *objects, score):
        self.screen.fill(Config.BLACK)

        for object in objects:
            pygame.draw.rect(self.screen, Config.WHITE, object)

        score_text = self.font.render("Score: {}".format(score), True, Config.WHITE)
        self.screen.blit(score_text, (10, 10))
        pygame.display.flip()

    def tick_fps(self, fps_count):
        self.clock.tick(fps_count)



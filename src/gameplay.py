import pygame
import sys


class Game:
    def __init__(self, wall_width):
        self.wall_width = wall_width
        pygame.init()
        self.score = 0

    def start_playing(self, ball, ball_speed, slider, wall_top):
        ball.move_ip(ball_speed)

        # Bouncing from walls
        if ball.left < 0 or ball.right > self.wall_width:
            ball_speed[0] = -ball_speed[0]
        if ball.top < 0:
            ball_speed[1] = -ball_speed[1]

        # Bouncing from slider
        if ball.colliderect(slider) and ball_speed[1] > 0:
            ball_speed[1] = -ball_speed[1]
            self.score += 1

        # Bouncing from top wall
        if ball.colliderect(wall_top) and ball_speed[1] < 0:
            ball_speed[1] = -ball_speed[1]

    @staticmethod
    def exit_game():
        pygame.quit()
        sys.exit()

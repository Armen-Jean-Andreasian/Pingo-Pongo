import pygame
import sys


class Game:
    score = 0
    ball_speed_multiplier = 1.2

    def __init__(self, wall_width, ball_speed):
        self.wall_width = wall_width
        pygame.init()
        self.ball_speed = ball_speed
        self.current_ball_speed = 1.0

    def start_playing(self, ball, slider, wall_top):
        ball.move_ip(self.ball_speed)

        # Bouncing from walls
        if ball.left < 0 or ball.right > self.wall_width:
            self.ball_speed[0] = -self.ball_speed[0]
        if ball.top < 0:
            self.ball_speed[1] = -self.ball_speed[1]

        # Bouncing from slider
        if ball.colliderect(slider) and self.ball_speed[1] > 0:
            self.ball_speed[1] = -self.ball_speed[1]
            self.score += 1
            self.ball_speed[0] *= self.ball_speed_multiplier
            self.current_ball_speed = round(abs(self.ball_speed[0]), 1)

        # Bouncing from top wall
        if ball.colliderect(wall_top) and self.ball_speed[1] < 0:
            self.ball_speed[1] = -self.ball_speed[1]

    @staticmethod
    def exit_game():
        pygame.quit()
        sys.exit()

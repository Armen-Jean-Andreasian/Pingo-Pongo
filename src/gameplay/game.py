import sys

import pygame

from src import Config


class Game:
    score = 0
    ball_speed_multiplier = 1.2

    def __init__(self, wall_width, ball_speed):
        self.wall_width = wall_width
        pygame.init()
        self.ball_speed = ball_speed
        self.current_ball_speed = 1.0
        self.game_over = False

    def start_playing(self, ball, slider, wall_top):
        if not self.game_over:
            ball.move_ip(self.ball_speed)

            # Game over check
            if ball.bottom > Config.HEIGHT:
                self.game_over = True

            # Bouncing from walls
            if ball.left < 0 or ball.right > self.wall_width:
                self.ball_speed[0] = -self.ball_speed[0]
            if ball.top < 0:
                self.ball_speed[1] = -self.ball_speed[1]

            # Bouncing from slider
            if ball.colliderect(slider) and self.ball_speed[1] > 0:
                self.ball_speed[1] = -self.ball_speed[1]

                # increasing ball speed, counting total score
                self.ball_speed[0] *= self.ball_speed_multiplier
                self.current_ball_speed = round(abs(self.ball_speed[0]), 1)
                self.score += int(self.current_ball_speed)

            # Bouncing from top wall
            if ball.colliderect(wall_top) and self.ball_speed[1] < 0:
                self.ball_speed[1] = -self.ball_speed[1]

    def is_game_over(self):
        return self.game_over

    def is_win(self):
        return self.current_ball_speed > 15

    @staticmethod
    def exit_game():
        pygame.quit()
        sys.exit()

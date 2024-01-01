import pygame

from src import Game, Config, Screen, Controls, Ball, Slider, WallTop

game = Game(wall_width=Config.WIDTH)
screen = Screen(game_name=Config.GAME_TITLE)

ball = Ball().get_rect()
slider = Slider().get_rect()
wall_top = WallTop().get_rect()
ball_speed = Ball.speed

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game.exit_game()

    Controls(object_to_control=slider)

    game.start_playing(ball=ball, ball_speed=ball_speed, slider=slider, wall_top=wall_top)

    screen.update(ball, slider, wall_top, score=game.score)
    screen.tick_fps(Config.FPS_COUNT)

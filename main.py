import pygame
from src import Game, Config, Screen, Controls, Ball, Slider, WallTop

ball_obj = Ball()

ball_figure = Ball().get_figure()
slider_figure = Slider().get_figure()
wall_top_figure = WallTop().get_figure()

game = Game(wall_width=Config.WIDTH, ball_speed=ball_obj.speed)
screen = Screen(game_name=Config.GAME_TITLE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game.exit_game()

    # Initializing controls
    Controls(object_to_control=slider_figure, move_left_px=Slider.move_left_px, move_right_px=Slider.move_right_px,
             move_up_px=Slider.move_up_px, move_down_px=Slider.move_down_px)

    # Update the game state
    game.start_playing(ball=ball_obj.get_figure(), slider=slider_figure, wall_top=wall_top_figure)

    # Draw the screen
    figures = (
        ('rects', (slider_figure, wall_top_figure)),
        ('images', (ball_obj,))
    )
    screen.update(figures=figures, score=game.score, speed=game.current_ball_speed,
                  speed_multiplier=game.ball_speed_multiplier, game_over_status=game.is_game_over(),
                  player_won_status=game.is_win())

    screen.tick_fps(Config.FPS_COUNT)

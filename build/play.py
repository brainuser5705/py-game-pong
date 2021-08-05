import pygame
from . import player
from . import ball
from . import settings
from . import util

from pygame.locals import (
    QUIT,
    K_SPACE,
    KEYDOWN,
)

pygame.init()
pygame.font.init()

'''
GAME VARIABLES
'''
font = pygame.font.SysFont('Comic Sans MS', 30)
screen = pygame.display.set_mode([settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT])
clock = pygame.time.Clock()

score = {
    1: 0,
    2: 0,
}

'''
SPRITES
'''
player1 = player.Player(1)
player2 = player.Player(2)
ball_sprite = ball.Ball()

'''
SPRITE GROUPS
'''
sprites_group = pygame.sprite.Group()
sprites_group.add(player1)
sprites_group.add(player2)
sprites_group.add(ball_sprite)

player_group = pygame.sprite.Group()
player_group.add(player1)
player_group.add(player2)

ball_group = pygame.sprite.Group()
ball_group.add(ball_sprite)

text = font.render(f'Press "SPACE" to start', False, settings.COLOR)


def reset_game(player):
    # text to display at start of new game
    global text
    score_text = f'p1: {score[1]}    p2: {score[2]}'
    text = font.render(f'{score_text}', False, settings.COLOR)

    # reset sprites position
    for entity in sprites_group:
        entity.reset()

    # change direction to whoever lost
    ball_sprite.direction = (player == 1)


def update_frame():
    # clear canvas
    screen.fill((0, 0, 0))

    # draw sprites
    for entity in sprites_group:
        screen.blit(entity.surf, entity.rect)
    pygame.display.flip()

    keys_pressed = pygame.key.get_pressed()

    # update sprites based on key moves and redraws canvas
    for entity in sprites_group:
        if type(entity) == player.Player:
            entity.update(keys_pressed)
        elif type(entity) == ball.Ball:
            entity.update()
        screen.blit(entity.surf, entity.rect)


def main():
    running = True  # for program/window loop
    playing = False  # for game loop
    while running:

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN and event.key == K_SPACE:
                # player must press SPACE to start playing
                playing = True

        # displays text if not playing
        if not playing:

            global text
            screen.blit(
                text,
                util.center(text.get_width(), text.get_height())
            )
            pygame.display.flip()

        # this part of the code will keep looping if playing
        else:

            update_frame()

            # collision between ball and player
            if pygame.sprite.spritecollideany(ball_sprite, player_group):
                ball_sprite.direction = not ball_sprite.direction
                ball_sprite.change_angle()

            # if ball reaches end of screen then game is over
            # 0 if the ball is still in play
            winner = ball_sprite.check()
            if winner != 0:

                score[winner] = score[winner] + 1
                reset_game(winner)

                # stop game
                playing = False

        clock.tick(30)

    pygame.quit()

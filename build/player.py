import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_w,
    K_s,
)

from . import settings


class Player(pygame.sprite.Sprite):

    def __init__(self, player_num):
        super(Player, self).__init__()

        self.surf = pygame.Surface((settings.PLAYER_WIDTH, settings.PLAYER_HEIGHT))
        self.surf.fill(settings.COLOR)
        self.rect = self.surf.get_rect()

        self.player_num = player_num

        # set starting position
        if self.player_num == 1:
            self.rect.move_ip(settings.PLAYER_PADDING, (settings.SCREEN_HEIGHT - settings.PLAYER_HEIGHT) / 2)
        elif self.player_num == 2:
            self.rect.move_ip(settings.SCREEN_WIDTH - (settings.PLAYER_WIDTH + settings.PLAYER_PADDING), (
                    settings.SCREEN_HEIGHT - settings.PLAYER_HEIGHT) / 2)

    # inherited from Sprite class
    def update(self, keys_pressed):
        if (self.player_num == 1 and keys_pressed[K_w]) or \
                (self.player_num == 2 and keys_pressed[K_UP]):
            self.rect.move_ip(0, -settings.MOVE_SPEED)

        if (self.player_num == 1 and keys_pressed[K_s]) or \
                (self.player_num == 2 and keys_pressed[K_DOWN]):
            self.rect.move_ip(0, settings.MOVE_SPEED)

        # border collision detection
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= settings.SCREEN_HEIGHT:
            self.rect.bottom = settings.SCREEN_HEIGHT

    def reset(self):
        self.__init__(self.player_num)
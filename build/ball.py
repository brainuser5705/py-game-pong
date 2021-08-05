import random

import pygame

from . import settings


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()

        self.surf = pygame.Surface((20, 20))
        self.surf.fill(settings.COLOR)
        self.rect = self.surf.get_rect()

        # starting position in the middle
        self.rect.move_ip(settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT / 2)

        # 0: moving towards player 1
        # 1: moving towards player 2
        self.direction = 0

        self.angle = random.randint(-settings.ANGLE_SIZE, settings.ANGLE_SIZE)

    def update(self):

        # moves either left or right depending on direction
        if self.direction == 0:
            self.rect.move_ip(-settings.MOVE_SPEED, self.angle)
        elif self.direction == 1:
            self.rect.move_ip(settings.MOVE_SPEED, self.angle)

        # changes angle if border collision
        if self.rect.top <= 0 or self.rect.bottom >= settings.SCREEN_HEIGHT:
            self.angle = -self.angle

    def change_angle(self):
        self.angle = random.randint(-10, 10)

    # checks if game is over and returns winner player num
    def check(self):
        if self.rect.left <= 0:
            return 2
        elif self.rect.right >= settings.SCREEN_WIDTH:
            return 1
        else:
            return 0

    def reset(self):
        # changes back to starting position in the middle
        self.__init__()

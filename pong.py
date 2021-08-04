import pygame
import random

pygame.init()

# Initalization variables
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

from pygame.locals import(
    K_UP,
    K_DOWN,
    K_w,
    K_s,
    QUIT,
)

class Player(pygame.sprite.Sprite):

    def __init__(self, player_num):
        super(Player, self).__init__()

        self.surf = pygame.Surface((20,100))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()

        self.player_num = player_num

        # set starting position
        if self.player_num  == 1:
            self.rect.move_ip(10, 0)
        elif self.player_num  == 2:
            self.rect.move_ip(SCREEN_WIDTH-30, 0) # screen width - (width size - 10)

    def update(self, keys_pressed): # inherited from Sprite class
        if (self.player_num == 1 and keys_pressed[K_w]) or\
                (self.player_num == 2 and keys_pressed[K_UP]):
            self.rect.move_ip(0,-5)

        if (self.player_num == 1 and keys_pressed[K_s]) or\
                (self.player_num ==2 and keys_pressed[K_DOWN]):
            self.rect.move_ip(0,5)

        # border collision detection
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()

        self.surf = pygame.Surface((20, 20))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()

        # starting position
        self.rect.move_ip(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

        # 0: moving towards player 1
        # 1: moving towards player 2
        self.direction = 0

        self.angle = random.randint(-1,1)

    def update(self):

        # changes player direction
        if self.direction == 0:
            self.rect.move_ip(-5, self.angle)
        elif self.direction == 1:
            self.rect.move_ip(5, self.angle)

        # changes angle if border collision
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.angle = -self.angle

    def change_angle(self):
        self.angle = random.randint(-1,1)

    # returns winner player num
    def check(self):
        if self.rect.left <= 0:
            return 2
        elif self.rect.right >= SCREEN_WIDTH:
            return 1
        else:
            return 0


# Game variables
player1 = Player(1)
player2 = Player(2)
ball = Ball()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

clock = pygame.time.Clock()

sprites_group = pygame.sprite.Group()
sprites_group.add(player1)
sprites_group.add(player2)
sprites_group.add(ball)

player_group = pygame.sprite.Group()
player_group.add(player1)
player_group.add(player2)

ball_group = pygame.sprite.Group()
ball_group.add(ball)

def main():
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        screen.fill((0,0,0))

        keys_pressed = pygame.key.get_pressed()

        for entity in sprites_group:
            if type(entity) == Player:
                entity.update(keys_pressed)

            elif type(entity) == Ball:
                entity.update()

            screen.blit(entity.surf, entity.rect)

        status = ball.check()
        if status != 0:
            print(f'Player {status} wins!')
            running = False

        if pygame.sprite.spritecollideany(ball, player_group):
            ball.direction = not ball.direction
            ball.change_angle()


        pygame.display.flip()

        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()





import sys, pygame
from random import randint
from pygame.locals import *


def main():
    pygame.init()

    clock = pygame.time.Clock()
    FPS = 20
    ground_position = 800

    size = width, height = 600, 1000

    background_color = 0, 0, 39

    screen = pygame.display.set_mode(size)

    class Player:
        def __init__(self):
            # jump movement
            self.y = 200
            self.base_velocity = 10
            self.velocity = self.base_velocity
            self.GRAVITY = 2
            self.JUMP_HEIGHT = 10
            self.MAX_VELOCITY = 30

            self.player_color = (255, 0, 0)

        def draw(self):
            pygame.draw.circle(screen, self.player_color, (250, int(self.y)), 15)

        def move(self):
            if not self.velocity >= self.MAX_VELOCITY:
                self.velocity += self.GRAVITY

            self.y += self.velocity

        def jump(self):
            print('before_jumping', self.y, self.velocity, end=' | ')
            self.velocity = -self.base_velocity * 1.5
            print('after_jumping', self.y, self.velocity)

    player = pygame.image.load("media/PacBoy.png")
    player_dest = player.get_rect()

    def game():
        player = Player()
        states = {1: 'running', 2: 'paused'}
        state = states[1]
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            screen.fill(background_color)
            if state == states[1]:  # game is running
                if pygame.key.get_pressed()[K_SPACE]:
                    player.jump()

                # loose detection
                if player.y > ground_position:
                    print(player.y)
                    state = states[2]

                player.move()

                pygame.draw.line(screen, (0, 0, 0), (0, ground_position + 50), (1000, ground_position + 50), 10)
                player.draw()

            elif state == states[2]:  # game is paused
                print('game paused')
                game()

            pygame.display.update()
            clock.tick(FPS)

    game()


if __name__ == '__main__':
    main()

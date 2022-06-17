import sys, pygame, os
from random import randint
from pygame.locals import *
from objects import *


def main():
    pygame.init()

    clock = pygame.time.Clock()
    FPS = 20
    ground_position = 800

    size = width, height = 600, 1000

    background_color = 1, 1, 76

    screen = pygame.display.set_mode(size)
    def game():
        player = Player()
        states = {1: 'running', 2: 'paused'}
        state = states[1]
        obstacles = []
        pygame.time.set_timer(USEREVENT+2, 2000)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == USEREVENT+2:
                    print('object created')
                    height = randint(400, 800)
                    obstacles.append(Blocker(600, height, 65, 666))  # lower wall
                    obstacles.append(Blocker(600, height-866, 65, 666))  # upper wall (right spawn point, height spawn(randomized), width, height

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

                for obstacle in obstacles:
                    if obstacle.x < obstacle.width * -1:
                        obstacles.pop(obstacles.index(obstacle))

                for obstacle in obstacles:
                    obstacle.x -= 8
                    obstacle.draw(screen)
                    if obstacle.collide(player.hitbox):



            elif state == states[2]:  # game is paused
                print('game paused')
                game()

            pygame.display.flip()
            #pygame.display.update()
            clock.tick(FPS)

    game()


if __name__ == '__main__':
    main()

import pygame, sys, time
from settings import *
from objects import Background, Player, Obstacle
from random import randint
class Game:
    def __init__(self):

        #setup
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Flappy Man')
        self.clock = pygame.time.Clock()
        self.is_active = True

        bg_height = pygame.image.load('media/Background.png').get_height()
        self.scale_factor = WINDOW_HEIGHT / bg_height

        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()


        Background(self.all_sprites)
        self.player = Player(self.all_sprites, 1.4)

        # timer
        self.obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer, 1400)

        # labels & menu
        self.menu_surf = pygame.image.load('media/retry.png').convert_alpha()
        self.menu_rect = self.menu_surf.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

        self.font =pygame.font.Font('media/CHERL___.TTF', 90)
        self.score = 0
        self.start_offset = 0

    def collisions(self):
        if pygame.sprite.spritecollide(self.player, self.collision_sprites, False, pygame.sprite.collide_mask) \
                or self.player.rect.top <= 0:
            for sprite in self.collision_sprites.sprites():
                if sprite.sprite_type == 'obstacle':
                    sprite.kill()
            self.is_active = False
            self.player.kill()

    def score_display(self):
        if self.is_active:
            self.score = (pygame.time.get_ticks() - self.start_offset) // 1000
            y = WINDOW_HEIGHT / 10
        else:
            y = WINDOW_HEIGHT / 2 + (self.menu_rect.height / 1.5)

        score_surf = self.font.render(str(self.score), True, (255, 255, 255))
        score_rect = score_surf.get_rect(midtop=(WINDOW_WIDTH / 2, y))
        self.screen.blit(score_surf, score_rect)

    def run(self):
        delta_time = time.time()
        while True:
            # set delta time
            dt = time.time() - delta_time
            delta_time = time.time()

            # Game Main Loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.is_active:
                        self.player.jump()
                    else:
                        self.player = Player(self.all_sprites, 1.4)
                        self.is_active = True
                        self.start_offset = pygame.time.get_ticks()
                if event.type == self.obstacle_timer and self.is_active:
                    spawn_x = WINDOW_WIDTH + 100
                    spawn_y = randint(200, 650)
                    Obstacle([self.all_sprites, self.collision_sprites], self.scale_factor * 1.2, spawn_x, spawn_y)
                    Obstacle([self.all_sprites, self.collision_sprites], self.scale_factor * 1.2, spawn_x, spawn_y+1100)


            self.screen.fill('black')
            self.all_sprites.update(dt)
            self.all_sprites.draw(self.screen)
            self.score_display()


            if self.is_active:
                self.collisions()
            else:
                self.screen.blit(self.menu_surf, self.menu_rect)

            pygame.display.update()
            #self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()

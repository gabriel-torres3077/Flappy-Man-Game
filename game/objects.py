import os, pygame
from settings import *
from random import randint, choice

class Background(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load('media/Background.png').convert()
        self.rect = self.image.get_rect(topleft=(0, 0))

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, scale_factor):
        super().__init__(groups)

        self.surface = pygame.image.load('media/PacBoy.png').convert_alpha()
        self.image = pygame.transform.scale(self.surface, pygame.math.Vector2(self.surface.get_size()) * scale_factor)
        # rect
        self.rect = self.image.get_rect(midleft=(WINDOW_WIDTH / 10, WINDOW_HEIGHT / 2))
        self.pos = pygame.math.Vector2(self.rect.topleft)

        # movement
        self.gravity = 800
        self.direction = 0

        # mask
        self.mask = pygame.mask.from_surface(self.image)


    def apply_gravity(self, dt):
        self.direction += self.gravity * dt
        self.pos.y += self.direction * dt
        self.rect.y = round(self.pos.y)

    def jump(self):
        self.direction = -400


    def update(self, dt):
        self.apply_gravity(dt)

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, groups, scale_factor, x, y):
        super().__init__(groups)
        self.sprite_type = 'obstacle'

        surf = pygame.image.load('media/Block.png').convert_alpha()
        self.image = pygame.transform.scale(surf, pygame.math.Vector2(surf.get_size()) * scale_factor)

        self.rect = self.image.get_rect(midbottom=(x, y))
        self.pos = pygame.math.Vector2(self.rect.topleft)

        # mask
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, dt):
        self.pos.x -= 450 * dt
        self.rect.x = round(self.pos.x)
        if self.rect.right <= -100:
            self.kill()


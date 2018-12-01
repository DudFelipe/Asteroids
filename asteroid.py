import pygame
import math
import random
from pygame.sprite import Sprite

class Asteroid(Sprite):
    def __init__(self, aiSettings, screen):
        super().__init__()
        self.screen = screen

        self.image = pygame.image.load('images\Asteroid.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = random.randint(0, aiSettings.screenWidth)
        self.rect.centery = random.randint(0, aiSettings.screenHeight)

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.speed_factorx = random.randint(-15, 15)
        self.speed_factory = random.randint(-15, 15)

    def update(self):
        self.x += self.speed_factorx
        self.y += self.speed_factory

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)

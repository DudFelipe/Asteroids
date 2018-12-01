import pygame
import math
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, aiSettings, screen, ship):
        super().__init__()
        self.screen = screen

        self.image = pygame.image.load('images\projetil.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.centery = ship.rect.centery

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.speed_factor = aiSettings.bullet_speed_factor
        self.sound = aiSettings.bullet_sound

        self.angle = aiSettings.angle

    def grausToRad(self, grau):
        return (math.pi * grau) / 180

    def rotate(self):
        newRect = pygame.rect

        newRect.centerx = float(math.cos(self.grausToRad(
            self.angle)) * self.speed_factor)
        newRect.centery = float(
            math.sin(self.grausToRad(self.angle)) * self.speed_factor)

        return newRect

    def update(self):

        newRect = self.rotate()

        self.x += newRect.centerx
        self.y += newRect.centery

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        old_center = self.rect.center
        imageAux = pygame.transform.rotate(self.image, self.angle * -1)
        self.rect = imageAux.get_rect()
        self.rect.center = old_center
        self.screen.blit(imageAux, self.rect)

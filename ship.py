import pygame
import math
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, aiSettings, screen):
        super().__init__()

        self.screen = screen;
        self.aiSettings = aiSettings

        self.image = pygame.image.load('images\ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery 

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.movingForward = False
        self.spiningLeft = False
        self.spiningRight = False


    def grausToRad(self, grau):
            return (math.pi * grau) / 180


    def rotate(self, aiSettings):
        newRect = pygame.rect

        newRect.centerx = float(math.cos(self.grausToRad(
            aiSettings.angle)) * aiSettings.shipSpeedFactor)
        newRect.centery = float(
            math.sin(self.grausToRad(aiSettings.angle)) * aiSettings.shipSpeedFactor)

        return newRect

    def update(self):
        newRect = self.rotate(self.aiSettings)

        if self.movingForward:
            self.centerx += newRect.centerx
            self.centery += newRect.centery

        if self.spiningLeft:
            self.aiSettings.angle -= 3

            if self.aiSettings.angle < 0:
                self.aiSettings.angle = 360

        if self.spiningRight:
            self.aiSettings.angle += 3

            if self.aiSettings.angle > 360:
                self.aiSettings.angle = 0

        if self.rect.right >= self.screen_rect.right + self.image.get_rect().right:
            self.centerx = self.screen_rect.left
        elif self.rect.left + self.image.get_rect().right <= 0:
            self.centerx = self.screen_rect.right - self.image.get_rect().right
        elif self.rect.top + self.image.get_rect().bottom <= 0:
            self.centery = self.screen_rect.bottom - self.image.get_rect().bottom
        elif self.rect.bottom >= self.screen_rect.bottom + self.image.get_rect().bottom:
            self.centery = self.screen_rect.top + self.image.get_rect().top

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        old_center = self.rect.center
        imageAux = pygame.transform.rotate(self.image, self.aiSettings.angle * -1)
        self.rect = imageAux.get_rect()
        self.rect.center = old_center
        #pygame.draw.rect(self.screen, (255, 255, 255), (self.rect.left, self.rect.top, self.rect.width, self.rect.height), 1)
        self.screen.blit(imageAux, self.rect)

    def center_ship(self):
        self.centerx = self.screen_rect.centerx
        self.centery = self.screen_rect.centery 

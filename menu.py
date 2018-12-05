import pygame.font
from button import Button

class Menu():
    def __init__(self, aiSettings, screen):
        self.aiSettings = aiSettings
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.textColor = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 72)

        self.btnPlay = Button(aiSettings, screen, "Play")
        self.btnOptions = Button(aiSettings, screen, "Options")
        self.btnExit = Button(aiSettings, screen, "Exit")

        self.prepTitle()
        self.prepButtons()

    def prepTitle(self):
        self.titleImage = self.font.render("Asteroids", True, self.textColor, None)
        
        self.titleRect = self.titleImage.get_rect()
        self.titleRect.centerx = self.screen_rect.centerx
        self.titleRect.top = 20

    def prepButtons(self):
        self.btnOptions.rect.centery += 65
        self.btnOptions.msg_image_rect.center = self.btnOptions.rect.center

        self.btnExit.rect.centery += 130
        self.btnExit.msg_image_rect.center = self.btnExit.rect.center

    def drawOptions(self):
        self.btnPlay.drawButton()
        self.btnOptions.drawButton()
        self.btnExit.drawButton()
        self.screen.blit(self.titleImage, self.titleRect)
import pygame.font
from button import Button

class Options():
    def __init__(self, aiSettings, screen):
        self.aiSettings = aiSettings
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.textColor = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 72)

        self.btnEasy = Button(aiSettings, screen, "Easy")
        self.btnMedium = Button(aiSettings, screen, "Medium")
        self.btnHard = Button(aiSettings, screen, "Hard")

        self.prepTitle()
        self.prepButtons()

    def prepTitle(self):
        self.titleImage = self.font.render(
            "Options", True, self.textColor, None)

        self.titleRect = self.titleImage.get_rect()
        self.titleRect.centerx = self.screen_rect.centerx
        self.titleRect.top = 20

    def prepButtons(self):
        self.btnMedium.rect.centery += 65
        self.btnMedium.msg_image_rect.center = self.btnMedium.rect.center

        self.btnHard.rect.centery += 130
        self.btnHard.msg_image_rect.center = self.btnHard.rect.center

    def drawOptions(self):
        self.btnEasy.drawButton()
        self.btnMedium.drawButton()
        self.btnHard.drawButton()
        self.screen.blit(self.titleImage, self.titleRect)

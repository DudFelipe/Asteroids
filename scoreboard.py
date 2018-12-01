import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():

    def __init__(self, aiSettings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.aiSettings = aiSettings
        self.stats = stats

        self.text_color = (0, 0, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.prepScore()
        self.prepHighScore()
        self.prepShips()

    def prepScore(self):
        self.score_image = self.font.render(str(self.stats.score), True, self.text_color, self.aiSettings.bgColor)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prepHighScore(self):
        self.highScoreImage = self.font.render(str(self.stats.highScore), True, self.text_color, self.aiSettings.bgColor)
        
        self.highScoreRect = self.highScoreImage.get_rect()
        self.highScoreRect.centerx = self.screen_rect.centerx
        self.highScoreRect.top = 20

    def prepShips(self):
        self.ships = Group()
        for shipNumber in range(self.stats.ships_left):
            ship = Ship(self.aiSettings, self.screen)
            ship.rect.x = 10 + shipNumber * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def showScore(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.highScoreImage, self.highScoreRect)

        self.ships.draw(self.screen)

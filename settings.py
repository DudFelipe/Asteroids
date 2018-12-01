import pygame

class Settings():

    def __init__(self):
        self.screenWidth = 800
        self.screenHeight = 600
        self.bgColor = (0, 0, 0)

        self.shipSpeedFactor = 10
        self.angle = 0

        self.bullet_speed_factor = 15
        self.bullet_sound = pygame.mixer.Sound('sounds\shot.wav')

        self.ship_limit = 3

        self.asteroidPoints = 10

        self.fileHighScore = "highscore.txt"


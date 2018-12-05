import pygame

class Settings():

    def __init__(self):
        self.screenWidth = 800
        self.screenHeight = 600
        self.bgColor = (0, 0, 0)

        #self.shipSpeedFactor = 10
        self.shipDestroySound = pygame.mixer.Sound('sounds\explosion.wav')
        #self.angle = 0

        #self.bullet_speed_factor = 15
        self.bullet_sound = pygame.mixer.Sound('sounds\shot.wav')

        self.ship_limit = 3

        #self.asteroidPoints = 10
        self.asteroidDestroySound = pygame.mixer.Sound('sounds\explosionAsteroid.wav')

        self.fileHighScore = "highscore.txt"

    def initializeGameSettings(self):
        self.shipSpeedFactor = 10
        self.angle = 0

        self.bullet_speed_factor = 15

        self.asteroidPoints = 10
        
    def easyDifficult(self):
        self.initializeGameSettings()


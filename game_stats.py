class GameStats():

    def __init__(self, aiSettings):
        self.aiSettings = aiSettings
        self.reset_stats()

        self.game_active = False
        self.game_options = False
        self.getHighScore()

    def getHighScore(self):
        filename = self.aiSettings.fileHighScore
        with open(filename) as file:
            self.highScore = file.read()

    def saveHighScore(self):
        filename = self.aiSettings.fileHighScore
        with open(filename, 'w') as file:
            file.write(str(self.highScore))

    def reset_stats(self):
        self.ships_left = self.aiSettings.ship_limit
        self.score = 0
        

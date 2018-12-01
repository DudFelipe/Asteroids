import sys
import pygame

from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from scoreboard import Scoreboard
import game_functions as gf

def run_game():
    pygame.init()

    clock = pygame.time.Clock()
    last = pygame.time.get_ticks() 
    cooldown = 2000

    aiSettings = Settings()
    screen = pygame.display.set_mode((aiSettings.screenWidth, aiSettings.screenHeight))

    pygame.display.set_caption("Asteroids")

    stats = GameStats(aiSettings)
    sb = Scoreboard(aiSettings, screen, stats)

    ship = Ship(aiSettings, screen)

    bullets = Group() 
    asteroids = Group()

    while True:
        clock.tick(60)
        gf.checkEvents(aiSettings, screen, ship, bullets, asteroids, stats, sb)

        if stats.game_active:
            ship.update()
            gf.updateBullets(bullets, asteroids, aiSettings, sb, stats)

            now = pygame.time.get_ticks()
            if now - last >= cooldown:
                last = now
                gf.create_asteroid(aiSettings, screen, asteroids)

            gf.update_asteroid(asteroids, aiSettings, stats, ship, bullets, sb)
            
        gf.updateScreen(aiSettings, screen, ship, bullets, asteroids, sb)
        
run_game()

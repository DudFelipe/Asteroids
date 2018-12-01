import sys
import pygame
from bullet import Bullet
from asteroid import Asteroid
from time import sleep    

def check_highscore(stats, sb):
    if stats.score > int(stats.highScore):
        stats.highScore = stats.score
        sb.prepHighScore()

def ship_hit(aiSettings, ship, stats, bullets, asteroids, sb):
    if stats.ships_left > 0:
        stats.ships_left -= 1

        sb.prepShips()

        bullets.empty()
        asteroids.empty()

        ship.center_ship()

        sleep(0.5)
    else:
        stats.saveHighScore()
        stats.game_active = False

def update_asteroid(asteroids, aiSettings, stats, ship, bullets, sb):
    for asteroid in asteroids:
        asteroid.update()
        if asteroid.rect.right >= aiSettings.screenWidth:
            asteroid.speed_factorx = asteroid.speed_factorx * -1
        elif asteroid.rect.left <= 0:
            asteroid.speed_factorx = asteroid.speed_factorx * -1
        
        if asteroid.rect.bottom >= aiSettings.screenHeight:
            asteroid.speed_factory = asteroid.speed_factory * -1
        elif asteroid.rect.top <= 0:
            asteroid.speed_factory = asteroid.speed_factory * -1

        if pygame.sprite.spritecollideany(ship, asteroids):
            ship_hit(aiSettings, ship, stats, bullets, asteroids, sb)

def create_asteroid(aiSettings, screen, asteroids):
    new_asteroid = Asteroid(aiSettings, screen)
    asteroids.add(new_asteroid)

def checkBulletCollision(aiSettings, stats, sb, bullets, asteroids):
    collisions = pygame.sprite.groupcollide(bullets, asteroids, True, True)

    if collisions:
        for asteroids in collisions.values():
            stats.score += aiSettings.asteroidPoints
            sb.prepScore()
        check_highscore(stats, sb)

def updateBullets(bullets, asteroids, aiSettings, sb, stats):
    for bullet in bullets:
        bullet.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0 or bullet.rect.top >= aiSettings.screenHeight or bullet.rect.left <= 0 or bullet.rect.right >= aiSettings.screenWidth:
            bullets.remove(bullet)

    checkBulletCollision(aiSettings, stats, sb, bullets, asteroids)

def fire_bullet(aiSettings, screen, ship, bullets):
    new_bullet = Bullet(aiSettings, screen, ship)
    bullets.add(new_bullet)
    new_bullet.sound.play()

def checkKeydownEvents(event, aiSettings, screen, ship, bullets, asteroids, stats, sb):
    if event.key == pygame.K_q:
        sys.exit()
    
    elif event.key == pygame.K_UP:
        ship.movingForward = True

    elif event.key == pygame.K_LEFT:
        ship.spiningLeft = True

    elif event.key == pygame.K_RIGHT:
        ship.spiningRight = True

    elif event.key == pygame.K_SPACE:
        fire_bullet(aiSettings, screen, ship, bullets)

    elif event.key == pygame.K_r:
        stats.reset_stats()
        stats.game_active = True

        sb.prepScore()
        sb.prepShips()

        asteroids.empty()
        bullets.empty()

        ship.center_ship()

def checkKeyupEvents(event, ship):
    if event.key == pygame.K_UP:
        ship.movingForward = False
    
    elif event.key == pygame.K_LEFT:
        ship.spiningLeft = False

    elif event.key == pygame.K_RIGHT:
        ship.spiningRight = False

def checkEvents(aiSettings, screen, ship, bullets, asteroids, stats, sb):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            checkKeydownEvents(event, aiSettings, screen, ship, bullets, asteroids, stats, sb)

        elif event.type == pygame.KEYUP:
            checkKeyupEvents(event, ship)

def updateScreen(aiSettings, screen, ship, bullets, asteroids, sb):
    screen.fill(aiSettings.bgColor)

    for bullet in bullets:
        bullet.blitme()

    for asteroid in asteroids:
        asteroid.blitme()

    sb.showScore()

    ship.blitme()

    pygame.display.flip()

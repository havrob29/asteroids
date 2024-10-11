import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (updateable, drawable, shots)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    asteroidfield = AsteroidField()

    Player.containers = (updateable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for obj in updateable:
            obj.update(dt)

        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.collision_check(bullet):
                    bullet.kill()
                    asteroid.split()
            if asteroid.collision_check(player):
                print("Game over!")
                sys.exit()

        screen.fill(color="black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        
        #limit framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()


import pygame 
import sys
from constants import *
from player import * 
from asteroid import * 
from asteroidfield import * 
from shot import * 

def main(): 
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group() 
    asteroids = pygame.sprite.Group() 
    shots = pygame.sprite.Group() 

    Player.containers = (updatable, drawable)
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    Shot.containers = (shots, updatable, drawable)

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))
        updatable.update(dt)

        for obj in asteroids: 
            if obj.collide(player):
                print("Game Over!")
                sys.exit()

        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.collide(bullet):
                    asteroid.split()
                    bullet.kill()
        
        for item in drawable: 
            item.draw(screen)
        pygame.display.flip()
        delta = clock.tick(60)
        dt = delta / 1000

if __name__ == "__main__":
    main()

import pygame
import sys
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH
from constants import LINE_WIDTH
from logger import log_state
from player import *
from asteroid import Asteroid
from asteroidfield import *
import circleshape
from logger import log_event
from circleshape import *
from shot import *


def main():
    print("Starting Asteroids with pygame version: 2.6.1")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0
   
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    Field1 = AsteroidField()
    
    while True:
        log_state()
        for event in pygame.event.get():
            pass
        
     
        updatable.update(dt)
        
        for item in asteroids:
            if item.collides_with(player1):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for rock in asteroids:
            for bullet in shots:
                
                if rock.collides_with(bullet):
                    log_event("asteroid_shot")
                    rock.split()
                    bullet.kill()

 
        screen.fill("black")

        for item in drawable:
            item.draw(screen)
        pygame.display.flip()   
        dt = clock.tick(60) / 1000                                                                                                                                          

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
    

if __name__ == "__main__":
    main()

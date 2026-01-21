from circleshape import *
from logger import *
import random

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        self.x = x 
        self.y = y
        self.radius = radius
        super().__init__(self.x, self.y, self.radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

        
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        
        angle = random.uniform(20,50)

        rotated = self.velocity.rotate(angle)
        neg_rotated = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        split_1 = Asteroid(self.position[0], self.position[1], new_radius)
        split_2 = Asteroid(self.position[0], self.position[1], new_radius)

        split_1.velocity = rotated * 1.2
        split_2.velocity = neg_rotated * 1.2




        
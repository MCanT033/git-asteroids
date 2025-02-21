import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.math.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen,"white", (self.position.x, self.position.y), self.radius, 2)

    
    def update(self, dt):
         self.position += self.velocity * dt
    
    def split(self):
        print("starting split")
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            print("asteroid too small to split")
            return
        angle = random.uniform(20, 50)
        new_vel_1 = self.velocity.rotate(angle) * 1.2
        new_vel_2 = self.velocity.rotate(-angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        print(f"creating new asteroids with radius: {new_radius}")
        Asteroid(self.position.x, self.position.y, new_radius).velocity = new_vel_1
        Asteroid(self.position.x, self.position.y, new_radius).velocity = new_vel_2
        
        
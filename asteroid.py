import pygame
import circleshape


class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen, "white", self.position, width=2, radius=self.radius        
        )


    def update(self, dt):
        self.position += self.velocity * dt




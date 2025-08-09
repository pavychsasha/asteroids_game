import pygame
import circleshape
import constants

class Bullet(circleshape.CircleShape):
    def __init__(self, x, y) -> None:
        super().__init__(x, y, constants.SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(
            screen, "white",
            self.position,
            width=1,
            radius=self.radius        
        )

    def update(self, dt):
        self.position += self.velocity * dt


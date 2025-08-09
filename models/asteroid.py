import random
import pygame
from models import CircleShape
from core import constants


class Asteroid(CircleShape):
    def __init__(self, x, y, radius) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position,
                           width=2, radius=self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def kill(self) -> None:
        super().kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return

        # asteroid is big enough to split it
        split_angle = random.uniform(20, 50)

        new_velocity_1 = self.velocity.rotate(split_angle) * 1.2
        new_velocity_2 = self.velocity.rotate(-split_angle) * 1.2

        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid_1.velocity = new_velocity_1
        asteroid_2.velocity = new_velocity_2

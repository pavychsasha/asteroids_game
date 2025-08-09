import pygame


# Base class for pygame objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius) -> None:
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        self.frames_to_collide = 0

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def is_colliding(self, other) -> bool:
        if self.frames_to_collide:
            self.frames_to_collide -= 1
            return False

        distance = self.position.distance_to(other.position)
        if distance <= self.radius + other.radius:
            return True

        # TODO: add frames_to_collide functionality to avoid redundant vector calculations

        return False

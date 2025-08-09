import pygame
import constants
import circleshape
from bullet import Bullet


class Player(circleshape.CircleShape):
    
    def __init__(self, x, y) -> None:
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.clock = 0


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5

        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(
            screen,
            color="white",
            points=self.triangle(),
            width=2
        )

    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and keys[pygame.K_d]:
            pass
        elif keys[pygame.K_a]:
            self.rotate(dt * -1)
        elif keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w] and keys[pygame.K_s]:
            pass
        elif keys[pygame.K_w]:
            self.move(dt)
        elif keys[pygame.K_s]:
            self.move(dt * -1)

        if keys[pygame.K_SPACE]:
            if self.clock > 0:
                self.clock -= dt
            else:
                self.shoot()

    def shoot(self):
        bullet = Bullet(self.position.x, self.position.y)

        bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation)
        bullet.velocity *= constants.PLAYER_SHOOT_SPEED

        self.clock = constants.PLAYER_SHOOT_COOLDOWN


import sys
import pygame

from core import containers, constants
from models import Player, Asteroid, AsteroidField, Bullet


class GameFactory:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        )
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.running = False
        self.player = None
        self.initialize_containers()
        self.player = Player(
            x=constants.SCREEN_WIDTH / 2, y=constants.SCREEN_HEIGHT / 2
        )

    def initialize_containers(self):
        Player.containers = (containers.drawable, containers.updatable)

        Asteroid.containers = (
            containers.asteroids,
            containers.updatable,
            containers.drawable,
        )
        AsteroidField.containers = containers.updatable
        Bullet.containers = (
            containers.shots,
            containers.updatable,
            containers.drawable,
        )

    def shut_down_if_closed_tab(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def check_asteroid_collision(self, asteroid):
        is_over = asteroid.is_colliding(self.player)
        if is_over:
            print("Game over!")
            sys.exit(1)

        for bullet in containers.shots:
            is_shot = asteroid.is_colliding(bullet)
            if is_shot:
                asteroid.kill()
                bullet.kill()
                break

    def update_containers(self):
        containers.updatable.update(self.dt)

        for asteroid in containers.asteroids:
            self.check_asteroid_collision(asteroid)

    def draw_and_update_screen(self):
        self.screen.fill("black")

        for obj in containers.drawable:
            obj.draw(self.screen)

        pygame.display.flip()
        self.dt = self.clock.tick(60) / 1000

    def running_loop(self):
        self.shut_down_if_closed_tab()
        self.update_containers()
        self.draw_and_update_screen()

    def run(self):
        self.running = True
        AsteroidField()
        while self.running:
            self.running_loop()

    @classmethod
    def greet(cls):
        print("Starting Asteroids!")
        print("Screen width:", constants.SCREEN_WIDTH)
        print("Screen height:", constants.SCREEN_HEIGHT)

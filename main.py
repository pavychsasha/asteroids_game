import sys
import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
import constants
from player import Player
from bullet import Bullet


def main():
    print("Starting Asteroids!")
    print("Screen width:", constants.SCREEN_WIDTH)
    print("Screen height:", constants.SCREEN_HEIGHT)

    pygame.init()
    screen = pygame.display.set_mode(
        (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    running = True

    # TODO: make it within a factory class instead
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (drawable, updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Bullet.containers = (shots, updatable, drawable)

    player = Player(x=constants.SCREEN_WIDTH / 2,
                    y=constants.SCREEN_HEIGHT / 2)

    AsteroidField()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        updatable.update(dt)

        for asteroid in asteroids:
            is_over = asteroid.is_colliding(player)
            if is_over:
                print("Game over!")
                sys.exit(1)

            for bullet in shots:
                is_shot = asteroid.is_colliding(bullet)
                if is_shot:
                    asteroid.kill()
                    bullet.kill()
                    break

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()

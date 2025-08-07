import pygame
import constants
from player import Player

def main():
    print("Starting Asteroids!")
    print("Screen width:", constants.SCREEN_WIDTH)
    print("Screen height:", constants.SCREEN_HEIGHT)

    pygame.init()
    screen = pygame.display.set_mode(
        (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
    )
    clock = pygame.time.Clock()
    dt = 0
    running = True

    player = Player(
        x = constants.SCREEN_WIDTH / 2,
        y = constants.SCREEN_HEIGHT / 2
    )

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update(dt)

        screen.fill("black")

        player.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

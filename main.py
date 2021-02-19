# gain access to pygame in our code
import pip
import pygame
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
# instruction of the game
FPS = 60

ENEMY_SPAWN_RATE = 2
ENEMY_MIN_SIZE = 5
ENEMY_MAX_SIZE = 20
ENEMY_MIN_SPEED = 4
ENEMY_MAX_SPEED = 15

PLAYER_SPEED = 5
PLAYER_SIZE = 12
PLAYER_MAX_UP = 150

BACKGROUND_COLOR = pygame.Color("black")
TEXT_COLOR = pygame.Color("white")
ENEMY_COLOR = pygame.Color("darkgreen")
PLAYER_COLOR = pygame.Colour("darkred")


# game loop
def run():
    pygame.init()

    # create game window
    Clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set.caption("Not dodger game")

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.OUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K.ESCAPE:
                running = False

        clock.tick(FPS)

        surface.fill(BLACKGROUND_COLOR)

        screen.blit(surface, (0, 0))

        pygame.display.update()




if __name__ == '__main__':
    run()
    pygame.quit()

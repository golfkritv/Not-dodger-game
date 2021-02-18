# gain access to pygame in our code
import pygame
#hello my name is golf
# initialize all pygame modules
pygame.init()

# create game window
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Not Dodger game")

# game loop
gameRunning = True
while gameRunning:

    # fill pur screen wth a colour
    screen.fill((255, 255, 255))

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False

    # update game when action occur
    pygame.display.update()

    FPS = 60

    ENEMY_SPAWN_RATE = 2
    ENEMY_MIN_SIZE = 5
    ENEMY_MAX_SIZE = 20
    ENEMY_MIN_SPEED = 4
    ENEMY_MAX_SPEED = 15

    PLAYER_SPEED = 5
    PLAYER_SIZE = 12
    PLAYER_MAX_UP = 100

    BACKGROUND.COLOR = pygame.Color("black")
    TEXT.COLOR = pygame.Color("white")


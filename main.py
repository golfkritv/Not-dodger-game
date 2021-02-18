# gain access to pygame in our code
import pygame
import random

# create game window
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Not Dodger game")

#instruction of the game
FPS = 60

ENEMY_SPAWN_RATE = 2
ENEMY_MIN_SIZE = 5
ENEMY_MAX_SIZE = 20
ENEMY_MIN_SPEED = 4
ENEMY_MAX_SPEED = 15

PLAYER_SPEED = 5
PLAYER_SIZE = 12
PLAYER_MAX_UP = 100

BACKGROUND_COLOR = pygame.Color("black")
TEXT_COLOR = pygame.Color("white")
ENEMY_COLOR = pygame.Color("darkgreen")
PLAYER_COLOR = pygame.Colour("darkred")


# game loop
def run():
    pass



if __name__ = '__main__'
    run()
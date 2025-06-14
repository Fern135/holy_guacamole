import pygame
from sys import exit

width  = 900
height = 900

pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

colors = {
    "red"   : (255, 0, 0),
    "green" : (0, 255, 0),
    "blue"  : (0, 0, 255),
    "black" : (0, 0, 0),
    "white" : (255, 255, 255),
}


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill(colors['black'])
    #game code


    pygame.display.update()
    clock.tick(60)
import pygame
from sys import exit

width  = 900
height = 900

pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


        #game code


        pygame.display.update()
        clock.tick(60)
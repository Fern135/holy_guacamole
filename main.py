import pygame
from sys import exit
from styles.colors import COLORS
from src.Player.Player import *

width  = 900
height = 900

pygame.init()
screen = pygame.display.set_mode(( width, height ))
clock = pygame.time.Clock()

player = Player().setConfig(screen, width, height)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill(COLORS['maroon'])
    # game code
    player.spawn(width / 2, height / 2).control()

    pygame.display.update()
    clock.tick(60)
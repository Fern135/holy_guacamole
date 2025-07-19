import pygame
from styles.colors import COLORS

class Player:
    def __init__(self):
        self.health     = 3
        self.jumpHeight = 5
        self.speed      = 5
        self.coin       = 0
        self.inv        = []
        self.playerSize = 10
        self.locationX  = 0.0
        self.locationY  = 0.0
        self.surface    = None
        self.height     = None
        self.width      = None


    def setConfig(self, surface, width, height):
        self.surface = surface
        self.width   = width
        self.height  = height
        return self

    def spawn(self, x, y):
        pygame.draw.circle(self.surface, COLORS['white'], (x, y), self.playerSize, width=0)
        self.locationX = x
        self.locationY = y
        return self

    def jump(self):
        ground = self.height - 352

        if self.locationY == ground:
            self.locationY = ground 

        else:
            self.locationY -= 0.5

    def control(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:   locationX -= self.speed
        if keys[pygame.K_RIGHT]:  locationX += self.speed
        if keys[pygame.K_UP]:     locationY -= self.speed
        if keys[pygame.K_DOWN]:   locationY += self.speed
        if keys[pygame.K_SPACE]:  self.jump() # jump

        return self
    

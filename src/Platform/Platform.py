import pygame
from styles.colors import COLORS

class Platform:
    def __init__(self, x, y, w, h, solid=True, color=COLORS['green']):
        """
        A rectangular platform.
        Params:
          x, y  : top-left coordinates
          w, h  : width & height
          solid : if True, player can stand on it (collidable floor)
          color : draw color
        """
        self.rect  = pygame.Rect(x, y, w, h)
        self.solid = solid
        self.color = color

    def draw(self, surface):
        """Draw the platform rectangle."""
        pygame.draw.rect(surface, self.color, self.rect)

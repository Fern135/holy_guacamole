import pygame
from styles.colors import COLORS

class Enemy:
    def __init__(self, x, y, w=30, h=30, damage=1, color=COLORS['red']):
        """
        Simple rectangular enemy that patrols left/right.
        Params:
          x, y   : initial top-left position
          w, h   : width/height
          damage : damage dealt to player on contact
          color  : draw color
        """
        self.rect   = pygame.Rect(x, y, w, h)
        self.damage = damage
        self.color  = color
        self.alive  = True

        # Basic patrol parameters
        self.vx     = 2
        self.min_x  = x - 60
        self.max_x  = x + 60

    def update(self):
        """Move left/right between min_x and max_x."""
        if not self.alive:
            return
        self.rect.x += self.vx
        # Reverse direction at bounds
        if self.rect.x <= self.min_x or self.rect.x >= self.max_x:
            self.vx *= -1

    def draw(self, surface):
        """Draw the enemy if alive."""
        if not self.alive:
            return
        pygame.draw.rect(surface, self.color, self.rect)

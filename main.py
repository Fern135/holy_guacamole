import pygame
from sys import exit
from styles.colors import COLORS
from src.Player.Player import Player
from src.Platform import Platform
from src.Enemies.Enemies import Enemy
from levels.levels import demo, level_1

WIDTH, HEIGHT = 900, 900

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock  = pygame.time.Clock()

# ----- Create objects -----
# Chain setConfig() → spawn() to attach the screen and set start position
player = Player().setConfig(screen, WIDTH, HEIGHT).spawn(120, 120)

# # Some demo platforms (x, y, w, h)
# platforms = [
#     Platform(100, 700, 300, 20, solid=True,  color=COLORS['green']),  # ground-ish
#     Platform(500, 500, 150, 20, solid=True,  color=COLORS['blue']),   # floating
#     Platform(400, 600, 100, 50, True),
#     Platform(200, 400, 150, 10, solid=False, color=COLORS['maroon']), # decorative
# ]

# A couple of patrolling enemies
enemies = [
    Enemy(550, 470, 30, 30),  # sits on the blue platform
    Enemy(150, 670, 30, 30),  # sits on the green one
]

def drawPlatforms(platform):
    for p in platform:
        p.draw(screen)

# ----- Game loop -----
while True:
    # Process events (quit, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Clear screen
    screen.fill(COLORS['black'])

    # Draw platforms
    drawPlatforms(demo)

    # Update and draw enemies
    for e in enemies:
        e.update()
        e.draw(screen)

    # Update player (handles input, gravity, collisions, drawing)
    player.update(demo, enemies)

    # Flip buffers
    pygame.display.update()
    clock.tick(60)  # cap FPS

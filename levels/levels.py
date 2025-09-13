from src.Platform.Platform import Platform
from styles.colors import COLORS


# Some demo platforms (x, y, w, h)
demo = [
    Platform(100, 700, 300, 20, solid=True,  color=COLORS['green']),  # ground-ish
    Platform(500, 500, 150, 20, solid=True,  color=COLORS['blue']),   # floating
    Platform(400, 600, 100, 50, True),
    Platform(200, 400, 150, 10, solid=False, color=COLORS['maroon']), # decorative
]


level_1 = [
    
]


levels = {
    "1" : level_1,
}
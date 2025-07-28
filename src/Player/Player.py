import pygame
from styles.colors import COLORS

# -------- Tunable physics constants --------
GRAVITY       = 0.4     # Downward acceleration each frame
JUMP_VELOCITY = -10     # Initial upward velocity when jumping (negative = up)

class Player:
    def __init__(self):
        # --- Gameplay stats ---
        self.health     = 3
        self.speed      = 5           # Horizontal movement speed (px/frame)
        self.radius     = 10          # Circle radius for drawing

        # --- Position & motion ---
        self.x          = 0.0         # Current x-position
        self.y          = 0.0         # Current y-position
        self.vy         = 0.0         # Vertical velocity (positive = down)
        self.on_ground  = False       # True if standing on something

        # --- Rendering / world refs ---
        self.surface    = None        # Pygame Surface to draw on
        self.width      = 0           # World/screen width
        self.height     = 0           # World/screen height

    # ---------- Helpers ----------
    def rect(self) -> pygame.Rect:
        """
        Treat the circular player as a bounding box Rect for collision checks.
        """
        return pygame.Rect(
            int(self.x - self.radius),
            int(self.y - self.radius),
            self.radius * 2,
            self.radius * 2
        )

    # ---------- Setup ----------
    def setConfig(self, surface, width, height):
        """
        Attach the screen surface and dimensions to the player.
        Returns self for method chaining.
        """
        self.surface = surface
        self.width   = width
        self.height  = height
        return self

    def spawn(self, x, y):
        """
        Set the player's starting position.
        Returns self for chaining.
        """
        self.x = x
        self.y = y
        return self

    # ---------- Actions ----------
    def jump(self):
        """
        Initiate a jump if on_ground. Set upward velocity and leave ground.
        """
        if self.on_ground:
            self.vy = JUMP_VELOCITY
            self.on_ground = False

    def control(self):
        """
        Poll keyboard and adjust horizontal position or jump.
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_SPACE]:
            self.jump()

    def physics(self, platforms):
        """
        Robust vertical collision:
        1) Apply gravity to vy
        2) Predict future rect
        3) If we cross a platform edge this frame, snap to it
        """
        prev_rect   = self.rect()              # where we were
        self.vy    += GRAVITY                  # accel down
        dy          = self.vy
        future_rect = prev_rect.move(0, dy)    # where we want to be

        landed = False

        if dy > 0:  # falling
            for plat in platforms:
                if not plat.solid:
                    continue
                # We were above the top last frame, and will be below/inside after move
                if (prev_rect.bottom <= plat.rect.top and
                    future_rect.bottom >= plat.rect.top and
                    future_rect.right  >  plat.rect.left and
                    future_rect.left   <  plat.rect.right):
                    # Land on top
                    self.y  = plat.rect.top - self.radius
                    self.vy = 0
                    self.on_ground = True
                    landed = True
                    break

        elif dy < 0:  # jumping up, check head hits
            for plat in platforms:
                if not plat.solid:
                    continue
                if (prev_rect.top    >= plat.rect.bottom and
                    future_rect.top  <= plat.rect.bottom and
                    future_rect.right > plat.rect.left and
                    future_rect.left  < plat.rect.right):
                    # Bonk head
                    self.y  = plat.rect.bottom + self.radius
                    self.vy = 0
                    # don't mark on_ground
                    break

        # If we didn’t land or bonk, just move
        if not landed:
            self.y += dy
            self.on_ground = False

        # Fallback floor
        ground_y = self.height - self.radius
        if self.y >= ground_y:
            self.y = ground_y
            self.vy = 0
            self.on_ground = True


    def check_enemy_hits(self, enemies):
        """
        Simple enemy collision logic:
          - If falling and hit from above: stomp enemy.
          - Else: take damage.
        """
        player_rect = self.rect()
        for enemy in enemies:
            if not enemy.alive:
                continue
            if player_rect.colliderect(enemy.rect):
                # Hit from above?
                if self.vy > 0 and player_rect.bottom - self.vy <= enemy.rect.top:
                    enemy.alive = False               # remove enemy
                    self.vy = JUMP_VELOCITY * 0.7     # little bounce
                else:
                    self.take_damage(1)

    def take_damage(self, amount):
        """
        Reduce health. Add knockback, invincibility frames, etc. if desired.
        """
        self.health -= amount
        # TODO: implement invincibility / knockback

    def draw(self):
        """
        Render the player as a white circle.
        """
        pygame.draw.circle(
            self.surface,
            COLORS['white'],
            (int(self.x), int(self.y)),
            self.radius
        )

    def update(self, platforms=None, enemies=None):
        platforms = platforms or []
        enemies   = enemies   or []
        self.control()
        self.physics(platforms)          # <- MUST run
        self.check_enemy_hits(enemies)
        self.draw()


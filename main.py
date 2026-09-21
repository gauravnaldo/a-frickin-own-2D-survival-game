import pygame
import random
import math

# 1. Setup
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Top-Down Survival")
clock = pygame.time.Clock()

DARK_GRAY = (40, 40, 40)
BLUE = (0, 100, 255)
RED = (255, 0, 0)

# 2. Classes
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 20
        self.speed = 5
        
    # yo fellas lets calibrate keyboard movements :)
    def move(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += self.speed

        # for Keeping the player inside the screen as to avoid going out of bounds like people (;
        self.x = max(0, min(WIDTH - self.size, self.x))
        self.y = max(0, min(HEIGHT - self.size, self.y))

    def draw(self, surface):
        pygame.draw.rect(surface, BLUE, (self.x, self.y, self.size, self.size))

# lets give class to OUR enemies
class Enemy:
    def __init__(self):
        # they spawn randomly on the edges of the screen
        if random.choice([True, False]):
            self.x = random.choice([-30, WIDTH + 30])
            self.y = random.randint(0, HEIGHT)
        else:
            self.x = random.randint(0, WIDTH)
            self.y = random.choice([-30, HEIGHT + 30])
            
        self.size = 20
        self.speed = 2

    def move_towards(self, target_x, target_y):
        dx = target_x - self.x
        dy = target_y - self.y
        dist = math.hypot(dx, dy)
        if dist > 0:
            self.x += (dx / dist) * self.speed
            self.y += (dy / dist) * self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, RED, (self.x, self.y, self.size, self.size))


# 3. Main game loop
def main():
    running = True
    player = Player(WIDTH // 2, HEIGHT // 2)
    enemies = []
    
    # Custom event to spawn an enemy every 1000 milliseconds (1 second)
    SPAWN_ENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(SPAWN_ENEMY, 1000)
    
    while running:
        screen.fill(DARK_GRAY)
        
        # Movement
        keys = pygame.key.get_pressed()
        player.move(keys)
        
        for enemy in enemies:
            enemy.move_towards(player.x, player.y)
        
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Listen for the timer and spawn an enemy
            if event.type == SPAWN_ENEMY:
                enemies.append(Enemy())
                
        # Rendering
        player.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

# 4. Triggering execution at the VERY bottom
if __name__ == "__main__":
    main()

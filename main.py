import pygame

# 1. Setup
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Top-Down Survival")
clock = pygame.time.Clock()

DARK_GRAY = (40, 40, 40)
BLUE = (0, 100, 255)

# 2. Define the Player class BEFORE calling it
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

# 3. Main game loop
def main():
    running = True
    player = Player(WIDTH // 2, HEIGHT // 2)
    
    while running:
        screen.fill(DARK_GRAY)
        
        # Movement
        keys = pygame.key.get_pressed()
        player.move(keys)
        
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        # Rendering
        player.draw(screen)
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

# 4. Triggering execution at the VERY bottom
if __name__ == "__main__":
    main()

#yo yo yo its our day 2 of updating the code ,lets begin
#lets code for spawning our enemies 

import pygame
import random 
import math   

BLUE = (0, 100, 255)
RED = (255, 0, 0)   

#lets give class to OUR enemies
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

    def draw(self, surface):
        pygame.draw.rect(surface, RED, (self.x, self.y, self.size, self.size))

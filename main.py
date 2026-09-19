import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Top-Down Survival")
clock = pygame.time.Clock()

DARK_GRAY = (40, 40, 40)

def main():
    running = True
    player = Player(WIDTH // 2, HEIGHT // 2)  # <-- Add this line here
    
    while running:
        screen.fill(DARK_GRAY)
        keys = pygame.key.get_pressed()
        player.move(keys)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        player.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

#setting up the character

BLUE = (0, 100, 255)

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 20
        self.speed = 5

def draw(self, surface):
        pygame.draw.rect(surface, BLUE, (self.x, self.y, self.size, self.size))

player = Player(WIDTH // 2, HEIGHT // 2)
player.draw(screen)

#yo fellas lets callibrate keyboard movements :)
def move(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += self.speed
            
#for concentrating the player on screen so it doesn't escape from the screen or jump off like some people :}
self.x = max(0, min(WIDTH - self.size, self.x))
        self.y = max(0, min(HEIGHT - self.size, self.y))

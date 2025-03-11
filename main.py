import pygame
import random

# Initialize pygame
pygame.init()

set "version=1.0"
echo Script Version: %version%

# Game Constants
WIDTH, HEIGHT = 400, 600
GRAVITY = 0.5
FLAP_STRENGTH = -8
PIPE_GAP = 150
PIPE_WIDTH = 70
PIPE_SPEED = 3

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Setup Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird Clone")

# Load Assets
bird_img = pygame.Surface((40, 30))
bird_img.fill(BLUE)

# Bird Class
class Bird:
    def __init__(self):
        self.x = 50
        self.y = HEIGHT // 2
        self.velocity = 0

    def flap(self):
        self.velocity = FLAP_STRENGTH

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity
        if self.y >= HEIGHT:
            self.y = HEIGHT - 1  # Prevent falling off

    def draw(self):
        screen.blit(bird_img, (self.x, self.y))

# Pipe Class
class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(100, HEIGHT - PIPE_GAP - 100)

    def update(self):
        self.x -= PIPE_SPEED

    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.x, 0, PIPE_WIDTH, self.height))
        pygame.draw.rect(screen, GREEN, (self.x, self.height + PIPE_GAP, PIPE_WIDTH, HEIGHT))

# Main Game Function
def game_loop():
    clock = pygame.time.Clock()
    bird = Bird()
    pipes = [Pipe(WIDTH + i * 200) for i in range(3)]
    running = True

    while running:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bird.flap()
        
        bird.update()
        bird.draw()

        for pipe in pipes:
            pipe.update()
            pipe.draw()
            if pipe.x < -PIPE_WIDTH:
                pipes.remove(pipe)
                pipes.append(Pipe(WIDTH))
        
        pygame.display.update()
        clock.tick(30)
    
    pygame.quit()

if __name__ == "__main__":
    game_loop()

import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CAR_WIDTH, CAR_HEIGHT = 40, 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Self-Driving Car Simulation")

# Initialize car position and velocity
car_x = WIDTH // 2
car_y = HEIGHT - 100
car_velocity = 5

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_x -= car_velocity
    if keys[pygame.K_RIGHT]:
        car_x += car_velocity

    # Clear the screen
    screen.fill(WHITE)

    # Draw the car
    pygame.draw.rect(screen, BLACK, (car_x, car_y, CAR_WIDTH, CAR_HEIGHT))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

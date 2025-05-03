import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Autonomous Parking Simulator")

# Colors
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
GREEN = (0, 255, 0)

# Load car image
car = pygame.image.load("assets/car.png")
car = pygame.transform.scale(car, (60, 30))
car_rect = car.get_rect()
car_rect.topleft = (100, 500)

# Parking slot
parking_slot = pygame.Rect(600, 100, 70, 35)

# Car speed
speed = 2

def move_car_to_parking(car_rect, target):
    if car_rect.x < target.x:
        car_rect.x += speed
    elif car_rect.x > target.x:
        car_rect.x -= speed

    if car_rect.y < target.y:
        car_rect.y += speed
    elif car_rect.y > target.y:
        car_rect.y -= speed

    return car_rect.colliderect(target)

# Main loop
clock = pygame.time.Clock()
parked = False

while True:
    screen.fill(WHITE)
    pygame.draw.rect(screen, GRAY, parking_slot)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not parked:
        parked = move_car_to_parking(car_rect, parking_slot)

    if parked:
        pygame.draw.rect(screen, GREEN, parking_slot)

    screen.blit(car, car_rect)
    pygame.display.update()
    clock.tick(60)

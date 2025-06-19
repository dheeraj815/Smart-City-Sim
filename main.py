import pygame
import os
from city_map import create_city_grid, get_random_nodes
from vehicle_agent import Vehicle

# Constants
GRID_SIZE = 5
CELL_SIZE = 100
SCREEN_SIZE = GRID_SIZE * CELL_SIZE
NUM_VEHICLES = 3

# Colors
COLOR_BG = (30, 30, 30)
COLOR_GRID = (200, 200, 200)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Smart City Simulation - Car Image")
clock = pygame.time.Clock()

# === Load Car Image ===
image_path = r"C:\Users\Dheeraj Muley\OneDrive\Desktop\MyAIProject\smart_city_sim\car.png"
if not os.path.exists(image_path):
    print("❌ car.png NOT FOUND at path!")
else:
    print("✅ car.png found!")

car_image = pygame.image.load(image_path)
car_image = pygame.transform.scale(car_image, (40, 40))  # Resize

# === Setup Grid and Vehicles ===
G = create_city_grid(GRID_SIZE)

vehicles = []
for _ in range(NUM_VEHICLES):
    start, end = get_random_nodes(G)
    vehicle = Vehicle(G, start, end)
    vehicles.append((vehicle, car_image))

# === Drawing Functions ===


def draw_grid():
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE,
                               CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, COLOR_GRID, rect, width=1)


def draw_paths():
    for vehicle, _ in vehicles:
        for node in vehicle.path:
            x, y = node
            center = (x * CELL_SIZE + CELL_SIZE // 2,
                      y * CELL_SIZE + CELL_SIZE // 2)
            pygame.draw.circle(screen, (100, 255, 100), center, 4)


def draw_vehicles():
    for vehicle, image in vehicles:
        x, y = vehicle.current_position
        screen_pos = (x * CELL_SIZE + CELL_SIZE // 2 - 20,
                      y * CELL_SIZE + CELL_SIZE // 2 - 20)
        screen.blit(image, screen_pos)


# === Main Game Loop ===
running = True
frame_count = 0
move_interval = 30

while running:
    screen.fill(COLOR_BG)
    draw_grid()
    draw_paths()
    draw_vehicles()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    frame_count += 1
    if frame_count % move_interval == 0:
        for vehicle, _ in vehicles:
            if not vehicle.has_arrived():
                vehicle.move()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

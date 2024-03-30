import pygame
import sys
import time
from pygame.locals import *
from random import randint

# Create a food class to handle food spawning.
class Food:
    def __init__(self):
        self.position = [0, 0]
        self.color = GREEN
        self.spawned = False
        self.last_spawn_time = pygame.time.get_ticks()

    def spawn(self):
        self.position[0] = randint(0, (WINDOW_WIDTH - 10) // 10) * 10
        self.position[1] = randint(0, (WINDOW_HEIGHT - 10) // 10) * 10
        self.spawned = True
        self.last_spawn_time = pygame.time.get_ticks()

# Initialize the game engine.
pygame.init()

# Initialize time for food spawn.
start_time = time.time()

# Set up the window for the game.
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake')

# Set up the colors for the game.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the directions for the snake.
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Set up the snake variables.
snake = [[200, 200], [210, 200], [220, 200]]
snake_direction = RIGHT

# Initialize new_head variable.
new_head = [0, 0]

# Set up the food variables.
food = [0, 0]
food_color = GREEN
food_spawned = False
food = Food()

# Set up the score font.
score = 0
score_font = pygame.font.Font(None, 36)

# Set up the clock for a decent frame rate.
clock = pygame.time.Clock()

# Main game loop
while True:
    # Check for events and update the snake's direction.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Spawn food if 5 seconds have passed since the last spawn
        if pygame.time.get_ticks() - food.last_spawn_time >= 5000:
            food.spawn()

        # Check for key presses and update the snake's direction.
        elif event.type == KEYDOWN:
            if event.key == K_UP and snake_direction != DOWN:
                snake_direction = UP
            elif event.key == K_DOWN and snake_direction != UP:
                snake_direction = DOWN
            elif event.key == K_LEFT and snake_direction != RIGHT:
                snake_direction = LEFT
            elif event.key == K_RIGHT and snake_direction != LEFT:
                snake_direction = RIGHT

    # Move the snake in the current direction.
    if snake_direction == UP:
        new_head = [snake[0][0], snake[0][1] - 10]
    elif snake_direction == DOWN:
        new_head = [snake[0][0], snake[0][1] + 10]
    elif snake_direction == LEFT:
        new_head = [snake[0][0] - 10, snake[0][1]]
    elif snake_direction == RIGHT:
        new_head = [snake[0][0] + 10, snake[0][1]]
    
    # Insert the new head of the snake.
    snake.insert(0, new_head)
    
    # Spawn food every 5 seconds if not already spawned.
    if not food_spawned:
        food = Food()
        food.spawn()
        food_spawned = True

    # If 5 seconds has elapsed spawn new food.
    if time.time() - start_time > 5:
        food = Food()
        food.spawn()
        start_time = time.time()
        
    # Check for collision with food and update score.
    if new_head == food.position:
        food_spawned = False
        score += 1
        
    # If food not eaten snake does not grow and last segment is removed.
    else:
        snake.pop()

    # Check for collision with walls and end the game if collided.
    if new_head[0] < 0 or new_head[0] >= WINDOW_WIDTH or new_head[1] < 0 or new_head[1] >= WINDOW_HEIGHT:
        pygame.time.wait(2000)  # Wait for 2000 milliseconds (2 seconds)
        #pygame.quit()
        #sys.exit()

    # Check for collision with snake itself and end the game if collided.
    for segment in snake[1:]:
        if new_head == segment:
            pygame.time.wait(2000)  # Wait for 2000 milliseconds (2 seconds)
            #pygame.quit()
            #sys.exit()

    # Draw everything on the screen.
    window.fill(BLACK)

    # Draw grid for debugging
    # for x in range(0, WINDOW_WIDTH, 10):
    #     pygame.draw.line(window, WHITE, (x, 0), (x, WINDOW_HEIGHT))
    # for y in range(0, WINDOW_HEIGHT, 10):
    #     pygame.draw.line(window, WHITE, (0, y), (WINDOW_WIDTH, y))

    # Draw the snake segments on the screen.
    for segment in snake:
        pygame.draw.rect(window, WHITE, (segment[0], segment[1], 10, 10))

    # Draw the food on the screen.
    pygame.draw.rect(window, food_color, (food.position[0], food.position[1], 10, 10))

    # Draw the score on the screen in the top left corner.
    score_text = score_font.render('Score: %d' % score, True, WHITE)
    window.blit(score_text, (10, 10))

    # Update the display.
    pygame.display.update()

    # Cap the frame rate.
    clock.tick(20)

# Quit the game engine.
pygame.quit()

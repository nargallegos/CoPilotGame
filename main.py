import pygame
import sys
from pygame.locals import *
from random import randint

# Initialize the game
pygame.init()

# Set up the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake')

# Set up the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the directions
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Set up the snake
snake = [[200, 200], [210, 200], [220, 200]]
snake_direction = RIGHT

# Initialize new_head
new_head = [0, 0]

# Set up the food
food = [0, 0]
food_color = GREEN
food_spawned = False

# Set up the score
score = 0
score_font = pygame.font.Font(None, 36)

# Set up the clock
clock = pygame.time.Clock()

# Main game loop
while True:
    # Check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_UP and snake_direction != DOWN:
                snake_direction = UP
            elif event.key == K_DOWN and snake_direction != UP:
                snake_direction = DOWN
            elif event.key == K_LEFT and snake_direction != RIGHT:
                snake_direction = LEFT
            elif event.key == K_RIGHT and snake_direction != LEFT:
                snake_direction = RIGHT

    # Move the snake
    if snake_direction == UP:
        new_head = [snake[0][0], snake[0][1] - 10]
    elif snake_direction == DOWN:
        new_head = [snake[0][0], snake[0][1] + 10]
    elif snake_direction == LEFT:
        new_head = [snake[0][0] - 10, snake[0][1]]
    elif snake_direction == RIGHT:
        new_head = [snake[0][0] + 10, snake[0][1]]

    snake.insert(0, new_head)

    # Check for collision with food
    if new_head == food:
        food_spawned = False
        score += 1
    else:
        snake.pop()

    # Spawn food if needed
    if not food_spawned:
        food[0] = randint(0, (WINDOW_WIDTH - 10) // 10) * 10
        food[1] = randint(0, (WINDOW_HEIGHT - 10) // 10) * 10
        food_spawned = True

    # Check for collision with walls
    if new_head[0] < 0 or new_head[0] >= WINDOW_WIDTH or new_head[1] < 0 or new_head[1] >= WINDOW_HEIGHT:
        pygame.time.wait(2000)  # Wait for 2000 milliseconds (2 seconds)
        #pygame.quit()
        #sys.exit()

    # Check for collision with snake
    for segment in snake[1:]:
        if new_head == segment:
            pygame.time.wait(2000)  # Wait for 2000 milliseconds (2 seconds)
            #pygame.quit()
            #sys.exit()

    # Draw everything
    window.fill(BLACK)

    for segment in snake:
        pygame.draw.rect(window, WHITE, (segment[0], segment[1], 10, 10))

    pygame.draw.rect(window, food_color, (food[0], food[1], 10, 10))

    score_text = score_font.render('Score: %d' % score, True, WHITE)
    window.blit(score_text, (10, 10))

    pygame.display.update()

    # Cap the frame rate
    clock.tick(20)

# Run the game
#pygame.quit()

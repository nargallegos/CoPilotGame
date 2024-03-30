import pygame
import sys
import time
from pygame.locals import *
from random import randint

# Create a apple class to handle apple spawning.
class Apple:
    def __init__(self):
        self.position = [randint(0, (WINDOW_WIDTH - 10) // 10) * 10, randint(0, (WINDOW_HEIGHT - 10) // 10) * 10]
        self.color = GREEN
        self.spawn_time = pygame.time.get_ticks()

# Initialize the game engine.
pygame.init()

# Initialize time for apple spawn.
start_time = time.time()

# Set up the window for the game.
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('worm')

# Set up the colors for the game.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the directions for the worm.
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Set up the worm variables.
worm = [[200, 200], [210, 200], [220, 200]]
worm_direction = RIGHT

# Initialize new_head variable.
new_head = [0, 0]

# Set up the apples list.
apples = [Apple(), Apple(), Apple()]

# Set up the score font.
score = 0
score_font = pygame.font.Font(None, 36)

# Set up the clock for a decent frame rate.
clock = pygame.time.Clock()

# Main game loop
while True:
    # Spawn apple if 5 seconds have passed since the last spawn
    if pygame.time.get_ticks() - apples[-1].spawn_time >= 5000:
    # if pygame.time.get_ticks() - apple.last_spawn_time >= 5000:
        apples.append(Apple())  

    # Check for events and update the worm's direction.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Check for key presses and update the worm's direction.
        elif event.type == KEYDOWN:
            if event.key == K_UP and worm_direction != DOWN:
                worm_direction = UP
            elif event.key == K_DOWN and worm_direction != UP:
                worm_direction = DOWN
            elif event.key == K_LEFT and worm_direction != RIGHT:
                worm_direction = LEFT
            elif event.key == K_RIGHT and worm_direction != LEFT:
                worm_direction = RIGHT

    # Move the worm in the current direction.
    if worm_direction == UP:
        new_head = [worm[0][0], worm[0][1] - 10]
    elif worm_direction == DOWN:
        new_head = [worm[0][0], worm[0][1] + 10]
    elif worm_direction == LEFT:
        new_head = [worm[0][0] - 10, worm[0][1]]
    elif worm_direction == RIGHT:
        new_head = [worm[0][0] + 10, worm[0][1]]
    
    # Insert the new head of the worm at the beginning of the worm list.
    # This gives the appearance of the worm moving.
    worm.insert(0, new_head)

    # Check for collision with apple and update the score.
    for apple in apples:
        if new_head == apple.position:
            apples.remove(apple)
            score += 1            
            # Add a new segment to the worm so it grows.
            worm.append(worm[-1])

    # If apple is not eaten the worm does not grow and last segment is removed.
    else:
        worm.pop()

    # Check for collision with walls and end the game if collided.
    if new_head[0] < 0 or new_head[0] >= WINDOW_WIDTH or new_head[1] < 0 or new_head[1] >= WINDOW_HEIGHT:
        pygame.time.wait(2000)  # Wait for 2000 milliseconds (2 seconds)
        #pygame.quit()
        #sys.exit()

    # Check for collision with worm itself and end the game if collided.
    for segment in worm[1:]:
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

    # Draw the worm segments on the screen.
    for segment in worm:
        pygame.draw.rect(window, WHITE, (segment[0], segment[1], 10, 10))

    # Draw the apple on the screen.
    for apple in apples:
        pygame.draw.rect(window, apple.color, (apple.position[0], apple.position[1], 10, 10))

    # Draw the score on the screen in the top left corner.
    score_text = score_font.render('Score: %d' % score, True, WHITE)
    window.blit(score_text, (10, 10))

    # Update the display.
    pygame.display.update()

    # Cap the frame rate.
    clock.tick(20)

# Quit the game engine.
#pygame.quit()

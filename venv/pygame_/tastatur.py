# 1 - Import library
import pygame
from pygame.locals import *

# 2 - Initialize the game
pygame.init()
pygame.font.init()  # you have to call this at the start,
# if you want to use this module.

width, height = 64 * 10, 64 * 8
screen = pygame.display.set_mode((width, height))
player_x = 0
player_y = 0
keys = [False, False, False, False]

# 3 - Load images
player = pygame.image.load("cookies.png")

# 4 - keep looping through
while 1:

    # 5 - clear the screen before drawing it again
    screen.fill((255, 255, 255))
    # 6 - draw the screen elements
    screen.blit(player, (player_x, player_y))

    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if  event.key == K_LEFT:
                keys[1] = True
            elif event.key == K_RIGHT:
                keys[3] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[1] = False
            elif event.key == pygame.K_RIGHT:
                keys[3] = False

    # Update x-position
    # If the left key is pressed
    if keys[1]:
        if player_x > 0:  # If the player is inside the playing field
            player_x -= 15  # Decrease x position. The player goes left
    # If the right key is pressed
    elif keys[3]:
        if player_x < width - 64:  # If the player is inside the playing field
            player_x += 15  # Increase x position. The player goes right
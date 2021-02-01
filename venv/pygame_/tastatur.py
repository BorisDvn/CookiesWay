__autor__ = 'Team4'

# Import and Initialization
import pygame
from pygame.locals import *
import random
from entity import *
#from facial_expression import *

pygame.init()

# Display
size = (300, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Cookies Way')

# Entities
cookie1 = Cookie(20)
cookie2 = Cookie(120)
cookie3 = Cookie(220)
corona1 = Corona(20)
corona2 = Corona(120)
corona3 = Corona(220)
barre = Barre()


sprite_group = pygame.sprite.Group()
sprite_group.add(cookie1)
sprite_group.add(cookie2)
sprite_group.add(cookie3)
sprite_group.add(corona1)
sprite_group.add(corona2)
sprite_group.add(corona3)
sprite_group.add(barre)

# Background
bg = pygame.image.load('bg.png')
bg = pygame.transform.scale(bg, (size))

# flash collision
bg_red = pygame.Surface(size)
bg_red = bg_red.convert()
bg_red.fill((25, 0, 0))

font = None
font = pygame.font.Font(None, 25)
# Actions ---> Alter
# Assign Variables
keepGoing = True
count = 0
#clock = pygame.time.Clock()
pygame.time.set_timer(USEREVENT, 30)

# Key _ Tastatur
keys = [False, False, False, False]

# Loop
i = random.randint(10, 250)
j = random.randint(5, 250)
k = random.randint(5, 250)

position = 3  # random.choice([1, 2, 3])

while keepGoing:

    #clock.tick(30)
    pygame.display.flip()
    # Event Handling
    for event in pygame.event.get():
        if event.type == QUIT:
            keepGoing = False
            break
        elif cookie1.collision(barre.rect.left,barre.rect.top) or cookie2.collision(barre.rect.left,barre.rect.top)\
                or cookie3.collision(barre.rect.left,barre.rect.top):
            cookie1.cry()
            count += 1
            screen.blit(bg_red, (0, 0))
        elif corona1.collision(barre.rect.left,barre.rect.top) or corona2.collision(barre.rect.left,barre.rect.top)\
                or corona3.collision(barre.rect.left,barre.rect.top):
            screen.blit(bg_red, (0, 0))
            text = font.render(' Game Over', True, Color('White'))
            screen.blit(text, (100, 200))
            break

        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                keys[1] = True
            elif event.key == K_RIGHT:
                keys[3] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[1] = False
            elif event.key == pygame.K_RIGHT:
                keys[3] = False
        if keys[1]:
            if barre.rect.left > 0:  # If the player is inside the playing field
                barre.rect.left -= 5  # Decrease x position. The player goes left
        # If the right key is pressed
        elif keys[3]:
            if barre.rect.left < 300 - 64:  # If the player is inside the playing field
                barre.rect.left += 5  # Increase x position. The player goes right

        elif event.type == USEREVENT:
            if position == 1:
                sprite_group.remove(cookie1)
                sprite_group.remove(corona2)
                sprite_group.remove(corona3)
                if (i < 475):
                    corona1.bouger(i)
                    i += 2
                else:
                    i = random.randint(10, 30)
                    sprite_group.add(cookie1)
                    sprite_group.add(corona2)
                    sprite_group.add(corona3)
                    position = random.choice([1, 2, 3])

                if (j < 475):
                    cookie2.bouger(j)
                    j += 2
                else:
                    j = random.randint(10, 20)

                if (k < 475):
                    cookie3.bouger(k)
                    k += 2
                else:
                    k = random.randint(10, 30)

            if position == 2:
                sprite_group.remove(cookie2)
                sprite_group.remove(corona1)
                sprite_group.remove(corona3)
                if (i < 475):
                    cookie1.bouger(i)
                    i += 2
                else:
                    i = random.randint(10, 30)

                if (j < 475):
                    corona2.bouger(j)
                    j += 2
                else:
                    j = random.randint(10, 20)
                    sprite_group.add(cookie2)
                    sprite_group.add(corona1)
                    sprite_group.add(corona3)
                    position = random.choice([1, 2, 3])

                if (k < 475):
                    cookie3.bouger(k)
                    k += 2
                else:
                    k = random.randint(10, 30)

            if position == 3:
                sprite_group.remove(cookie3)
                sprite_group.remove(corona1)
                sprite_group.remove(corona2)
                if (i < 470):
                    cookie1.bouger(i)
                    i += 2
                else:
                    i = random.randint(10, 30)

                if (j < 470):
                    cookie2.bouger(j)
                    j += 2
                else:
                    j = random.randint(10, 20)

                if (k < 470):
                    corona3.bouger(k)
                    k += 2
                else:
                    k = random.randint(10, 30)
                    sprite_group.add(cookie3)
                    sprite_group.add(corona1)
                    sprite_group.add(corona2)
                    position = random.choice([1, 2, 3])

            pygame.time.set_timer(USEREVENT, 30)
            screen.blit(bg, (0, 0))
            sprite_group.update()
            sprite_group.draw(screen)
            text = font.render(' Score: ' + str(count), True, Color('White'))
            screen.blit(text, (10, 10))

    # Redisplay
    pygame.display.flip()

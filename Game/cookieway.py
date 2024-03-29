__autor__ = 'Team4'

# Import and Initialization
import pygame
from pygame.locals import *
import random
from entity import *
from cortex import *
import time
import threading

# define request id
SUB_REQUEST_ID = 6

user = {
    "client_id": "your id",
    "client_secret": "your client_Secret",
    "debit": 100
}  # "license" : "your emotivpro license, which could use for third party app",

profile_name = 'Cookiesway'
cortex = Cortex(user)
cortex.do_prepare_steps()
status = 'load'
cortex.setup_profile(profile_name, status)
sub_request_json = {
    "jsonrpc": "2.0",
    "method": "subscribe",
    "params": {
        "cortexToken": cortex.auth,
        "session": cortex.session_id,
        "streams": ['com']
    },
    "id": SUB_REQUEST_ID
}

l, r, n = False, False, False  # left right neutral


def sub_request():
    cortex.ws.send(json.dumps(sub_request_json))
    while True:
        new_data = cortex.ws.recv()  # result of request
        print(new_data)
        try:
            global l, r, n  # get mental commands from HeadSet
            if json.loads(new_data)["com"][0] == 'left':
                n = False
                l = True
                r = False
            elif json.loads(new_data)["com"][0] == 'right':
                n = False
                l = False
                r = True
            elif json.loads(new_data)["com"][0] == 'neutral':
                n = True
                l = False
                r = False
        except:
            pass


# Thread for sub_request
sub_request_thread = threading.Thread(target=sub_request)
sub_request_thread.start()

# Initialization pygame
pygame.init()
pygame.mixer.init()

# Display
size = (300, 475)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Cookies Way')

# music
pygame.mixer.music.load('music.mp3')

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

# gameover
gameover = pygame.image.load('gameover.png')
gameover = pygame.transform.scale(gameover, (100,100))

# Font
font = None
font = pygame.font.SysFont('constantia', 25)

# Actions ---> Alter
# Assign Variables
keepGoing = True
count = 0

# Random position for Corona Cookies
i = random.randint(10, 250)
j = random.randint(5, 250)
k = random.randint(5, 250)
position = 3  # random.choice([1, 2, 3])

# Play Background music
pygame.mixer.music.play(-1)

while keepGoing:
    # Event Handling
    for event in pygame.event.get():
        if event.type == QUIT:
            keepGoing = False
            break
        elif cookie1.collision(barre.rect.left, barre.rect.top) or cookie2.collision(barre.rect.left, barre.rect.top) \
                or cookie3.collision(barre.rect.left, barre.rect.top):
            cookie1.cry()
            count += 1
        elif corona1.collision(barre.rect.left, barre.rect.top) or corona2.collision(barre.rect.left, barre.rect.top) \
                or corona3.collision(barre.rect.left, barre.rect.top):
            screen.blit(bg_red, (0, 0))
            score = font.render('Score:' + str(count), True, Color('White'))
            screen.blit(score, (100, 150))
            screen.blit(gameover, (100, 180))
            pygame.display.flip()
            cookie1.dead() # play deadsound
            # keepGoing = False
            break

        if l == True:
            print('left')
            if barre.rect.left > 0:  # If the player is inside the playing field
                barre.rect.left -= 5  # Decrease x position. The player goes left
        if r == True:
            print('right')
            if barre.rect.left < 300 - 100:  # If the player is inside the playing field
                barre.rect.left += 5  # Increase x position. The player goes right
        if n == True:
            print('neutral')
            barre.rect.left = 105  # center

        # Move: Cookies and Corona
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
        text = font.render('Score:' + str(count), True, Color('White'))
        screen.blit(text, (10, 5))

    # Redisplay
    pygame.display.flip()

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
    "client_id": "bNhy8kMvfbvi16uWqRL5VbGnHaKrFAESiyHi7y4G",
    "client_secret": "FPVm8V0fbBnXh8Mp5uQwB1jC3qMPWI2pqumAHUEc7l0h1rbgGci7APl3dA8qtLWewjsEZsEN9T4FIM6TAWC654864CqS7o6JLwkgOUFJtPwakjNk2JYi2qFkDGDcCd8U",
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

l, r, n = False, False, False #left right neutral

def sub_request():
    cortex.ws.send(json.dumps(sub_request_json))
    while True:
        new_data = cortex.ws.recv()  # result of request

        try:
            global l,r,n
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
            print(new_date)
        except:
            pass

#Thread for sub_request
sub_request_thread = threading.Thread(target=sub_request)
sub_request_thread.start()

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

# background
bg = pygame.image.load('bg.png')
bg = pygame.transform.scale(bg, (size))

#GameOver
#gameover = pygame.image.load('gameover.png').convert()
#gameover = pygame.transform.scale(gameover, (100,100))

font = None
font = pygame.font.Font(None, 25)
# Actions ---> Alter
# Assign Variables
keepGoing = True
count = 0
clock = pygame.time.Clock()

# Key _ Tastatur r , l , n, none
keys = [False, False, False, False]

# Loop
i = random.randint(10, 250)
j = random.randint(5, 250)
k = random.randint(5, 250)

position = 3  # random.choice([1, 2, 3])

while keepGoing:
    #print(t.newMethode())
    clock.tick(30)
    # Event Handling
    for event in pygame.event.get():
        if event.type == QUIT:
            keepGoing = False
            break
        elif cookie1.collision(barre.rect.left,barre.rect.top) or cookie2.collision(barre.rect.left,barre.rect.top)\
                or cookie3.collision(barre.rect.left,barre.rect.top):
            #cookie1.cry()
            count += 1
        elif corona1.collision(barre.rect.left, barre.rect.top) or corona2.collision(barre.rect.left,barre.rect.top) \
             or corona3.collision(barre.rect.left, barre.rect.top):
            keepGoing = False
            #cookie1.cry()
            break

        if l == True:
            print('left')
            keys[0] = True
            keys[1] = False
            keys[2] = False
            keys[3] = False
        if  r == True:
            print('right')
            keys[1] = True
            keys[0] = False
            keys[2] = False
            keys[3] = False
        if  n == True:
            print('neutral')
            keys[1] = False
            keys[0] = False
            keys[2] = True
            keys[3] = False

        # left
        if keys[0]:
            if barre.rect.left > 0:  # If the player is inside the playing field
                barre.rect.left -= 5  # Decrease x position. The player goes left
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
                #pygame.time.set_timer(USEREVENT, 30)
                screen.blit(bg, (0, 0))
                sprite_group.update()
                sprite_group.draw(screen)
                text = font.render(' Score: ' + str(count), True, Color('White'))
                screen.blit(text, (10, 10))
            else:
                keys[3] = True
        # right
        elif keys[1]:
            if barre.rect.left < 300 - 85:  # If the player is inside the playing field
                barre.rect.left += 5  # Increase x position. The player goes right
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
                #pygame.time.set_timer(USEREVENT, 30)
                screen.blit(bg, (0, 0))
                sprite_group.update()
                sprite_group.draw(screen)
                text = font.render(' Score: ' + str(count), True, Color('White'))
                screen.blit(text, (10, 10))
            else:
                keys[3] = True
        # Neutral
        if keys[2]:
            barre.rect.left = 105 #center
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

        # Empty
        if keys[3]:
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
__autor__ = 'Team4'

# Import and Initialization
import pygame
from pygame.locals import *
import random

pygame.init()

# Entities
class Cookie(pygame.sprite.Sprite):

    def __init__(self, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('cookies.png')
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.sound = pygame.mixer.Sound('son01.wav')
        self.rect = self.image.get_rect()
        self.rect.left = y

    def bouger(self, y):
        self.rect.top = y

    def cry(self):
        self.sound.play()

    def collision(self, pos_x, pos_y):
        if pos_x-2<=self.rect.left and pos_x+85>=self.rect.left and self.rect.top == pos_y :
            return True
        #return self.rect.collidepoint(pos)



class Corona(pygame.sprite.Sprite):

    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('cookies1.png')
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.left = x

    def bouger(self, y):
        self.rect.top = y

    def collision(self, pos_x, pos_y):
        if pos_x-2<=self.rect.left and pos_x+85>=self.rect.left and self.rect.top==pos_y:
            return True


class Barre(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('barre.png')
        self.image = pygame.transform.scale(self.image, (100, 80))
        self.rect = self.image.get_rect()
        self.rect.left = 20
        self.rect.top = 380

        # mouse oder tastatur
        #self.rect.center = pygame.mouse.get_pos()
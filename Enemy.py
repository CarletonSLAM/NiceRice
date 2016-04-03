import pygame
from Player import *
from Platform import *
import random
from GlobalVariables import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('Resources', "character.png"))
        self.rect = self.image.get_rect()

        # Set speed vector of enemy
        self.direction = -1

        # List of sprites we can bump against
        self.level = None
        self.rect.y = 540
        self.rect.x = 1000

    def update(self):
        randomNum = random.randint(-1, 1)
        if randomNum == self.direction:
            self.rect.move_ip(self.direction*6, 0)
        elif randomNum == 0:
            self.rect.move_ip(self.direction * 6, 0)
        else:
            self.direction = -1*self.direction
            self.rect.move_ip(self.direction * 6, 0)
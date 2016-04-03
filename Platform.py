import pygame,os
from GlobalVariables import *

class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super(Platform, self).__init__()

        self.image = pygame.Surface([width, height])
        self.image = pygame.image.load(os.path.join('Resources', "obstacle.png"))

        self.rect = self.image.get_rect()
import pygame
import sys
import math
import random

from pygame.locals import *

pygame.init()

pygame.display.set_caption('niceRice')



'''------Fonts, Colours & Screens------'''

Font1 = pygame.font.SysFont(None, 32)                                               #Variables for different font sizes
Font2 = pygame.font.SysFont(None, 60)
Font3 = pygame.font.SysFont(None, 24)
Font_Big = pygame.font.SysFont(None, 100)
Font_inst = pygame.font.SysFont(None, 18)

screen = pygame.display.set_mode((1000, 620), 0, 24)

Dark_Grey = (35, 35, 35)
Black = (0, 0, 0)
White = (255, 255, 255)
Dark_Red = (100,   0,   0)
Green = (0, 150,   0)
Dark_Green = (0, 50,   0)
Blue = (0,   0, 255)
Light_Blue = (0, 255, 255)
Red = (255, 0, 0)
Yellow = (255, 250, 205)


running = True
while running:                             #The main loop that does not break unless Esc is pressed
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == (K_ESCAPE):
                running = False
pygame.QUIT
import pygame


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 25
        self.height = 50
        self.velocity=0
        self.falling=True
        self.onGround=False

    def detectCollisions(self, x1, y1, w1, h1, x2, y2, w2, h2):
        if x2 + w2 >= x1 >= x2 and y2 + h2 >= y1 >= y2:
            return True
        elif x2 + w2 >= x1 + w1 >= x2 and y2 + h2 >= y1 >= y2:
            return True
        elif x2 + w2 >= x1 >= x2 and y2 + h2 >= y1 + h1 >= y2:
            return True
        elif x2 + w2 >= x1 + w1 >= x2 and y2 + h2 >= y1 + h1 >= y2:
            return True
        else:
            return False


    def update(self, gravity):
        if self.velocity<0:
            self.falling=True

        self.velocity+=gravity
        self.y-=self.velocity

    def render(self, window):
        pygame.draw.rect(window,(0,0,0),(self.x, self.y, self.width, self.height))
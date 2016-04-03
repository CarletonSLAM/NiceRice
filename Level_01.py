from Level import *
from Platform import *

class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.level_limit = -1000

        # Array with width, height, x, and y of platform
        level = [[210, 70, 500, 530],
                 [210, 30, 1000, 500],
                 [210, 30, 1000, 300],
                 [210, 30, 710, 400],
                 [210, 30, 1300, 150]
                 ]

        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
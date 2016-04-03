from Level import *
from Platform import *
from Enemy import *

class Level_01(Level):
    def __init__(self, player):
        # Call the parent constructor
        Level.__init__(self, player)

        self.level_limit = -1000

        # Array with width, height, x, and y of platform
        level = [[210, 70, 500, 530],
                 [210, 140, 710, 460],
                 ]

        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        # Add one enemies to the level
        # Set the height and width of the screen
        size = [SCREEN_WIDTH, SCREEN_HEIGHT]
        screen = pygame.display.set_mode(size)
        self.enemy_list.add(Enemy())
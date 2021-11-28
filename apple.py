import pygame
import random


# The Apple class initializes and draws Apple objects
# in random positions on the board/grid
class Apple:

    def __init__(self, snake_game):
        self.screen = snake_game.screen
        self.apple_color = snake_game.settings.apple_color
        self.apple_size = snake_game.settings.block_size
        g_size = snake_game.settings.grid_size
        cols = snake_game.settings.cols
        rows = snake_game.settings.rows
        mx, my = snake_game.settings.margins
        # Select random x and y position for apple
        self.x = random.randint(0, cols - 1) * g_size + mx + 1
        self.y = random.randint(0, rows - 1) * g_size + my + 1

    # Draws the apple on the board/grid
    def draw(self):
        pygame.draw.rect(self.screen, self.apple_color,
                         pygame.Rect(self.x, self.y, self.apple_size, self.apple_size))


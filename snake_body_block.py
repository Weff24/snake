import pygame


# SnakeBodyBlock initializes a single body block
# of the snake
class SnakeBodyBlock:

    def __init__(self, snake_game, grid_position, direction=None):
        self.screen = snake_game.screen
        self.settings = snake_game.settings
        self.pos_x = grid_position[0]
        self.pos_y = grid_position[1]

        self.direction = direction

    # Updates the position of the block depending on its movement direction.
    # self.direction = 1 (up), 2 (right), 3 (down), or 4 (left)
    def update_pos(self):
        g_size = self.settings.grid_size
        if self.direction == 1:
            self.pos_y -= g_size
        elif self.direction == 2:
            self.pos_x += g_size
        elif self.direction == 3:
            self.pos_y += g_size
        elif self.direction == 4:
            self.pos_x -= g_size

    # Draws the snake block on the board/grid
    def draw(self):
        size = self.settings.block_size
        pygame.draw.rect(self.screen, self.settings.snake_color,
                         pygame.Rect(self.pos_x, self.pos_y, size, size))

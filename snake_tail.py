import pygame

from snake_body_block import SnakeBodyBlock


# SnakeTail initializes the tail block of the snake.
# SnakeTail inherits the methods of SnakeBodyBlock.
class SnakeTail(SnakeBodyBlock):

    def __init__(self, snake_game, grid_position, direction):
        super().__init__(snake_game, grid_position, direction)

    # SnakeTail's draw method overrides SnakeBodyBlock's draw method
    # so the tail can be drawn uniquely.
    # Draws the tail with different orientations depending on movement direction. The shape of
    # the tail block is triangle.
    def draw(self):
        size = self.settings.block_size - 1
        color = self.settings.snake_color
        # Draws the triangle in different directions depending on movement direction.
        # self.direction = 1 (up), 2 (right), 3 (down), or 4 (left)
        if self.direction == 1:
            pygame.draw.polygon(self.screen, color,
                                [(self.pos_x, self.pos_y), (self.pos_x + size, self.pos_y),
                                 (self.pos_x + size / 2, self.pos_y + size)])
        elif self.direction == 2:
            pygame.draw.polygon(self.screen, color,
                                [(self.pos_x + size, self.pos_y), (self.pos_x + size, self.pos_y + size),
                                 (self.pos_x, self.pos_y + size / 2)])
        elif self.direction == 3:
            pygame.draw.polygon(self.screen, color,
                                [(self.pos_x, self.pos_y + size), (self.pos_x + size, self.pos_y + size),
                                 (self.pos_x + size / 2, self.pos_y)])
        elif self.direction == 4:
            pygame.draw.polygon(self.screen, color,
                                [(self.pos_x, self.pos_y), (self.pos_x, self.pos_y + size),
                                 (self.pos_x + size, self.pos_y + size / 2)])

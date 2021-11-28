import pygame

from snake_body_block import SnakeBodyBlock


# SnakeHead initializes the head block of the snake.
# SnakeHead inherits the methods of SnakeBodyBlock.
class SnakeHead(SnakeBodyBlock):

    def __init__(self, snake_game, grid_position, direction=None):
        super().__init__(snake_game, grid_position, direction)

    # SnakeHead's draw method overrides SnakeBodyBlock's draw method
    # so the head can be drawn uniquely.
    # Draws the head with different orientations depending on movement direction. The shape of
    # the head block is a half-circle with a rectangle along its diameter.
    # Also draws eyes on the head block.
    def draw(self):
        size = self.settings.block_size
        color = self.settings.snake_color
        pygame.draw.circle(self.screen, color,
                           (round(self.pos_x + size / 2), round(self.pos_y + size / 2)), size / 2)
# 2 of the 4 eyes will be covered by the rectangle so the snake only has 2 eyes
#        pygame.draw.circle(self.screen, self.settings.border_color,
#                           (round(self.pos_x + size / 4), round(self.pos_y + size / 4)), 3)
#        pygame.draw.circle(self.screen, self.settings.border_color,
#                           (round(self.pos_x + size / 4), round(self.pos_y + 3 * size / 4)), 3)
#        pygame.draw.circle(self.screen, self.settings.border_color,
#                           (round(self.pos_x + 3 * size / 4), round(self.pos_y + size / 4)), 3)
#        pygame.draw.circle(self.screen, self.settings.border_color,
#                           (round(self.pos_x + 3 * size / 4), round(self.pos_y + 3 * size / 4)), 3)
        # The rectangle and eyes have a different orientation depending on movement direction.
        # self.direction = 1 (up), 2 (right), 3 (down), or 4 (left)
        if self.direction == 1:
            pygame.draw.rect(self.screen, color,
                             pygame.Rect(self.pos_x, round(self.pos_y + size / 2), size, size / 2))
            pygame.draw.circle(self.screen, self.settings.border_color,
                               (round(self.pos_x + size / 4), round(self.pos_y + size / 4)), 3)
            pygame.draw.circle(self.screen, self.settings.border_color,
                               (round(self.pos_x + 3 * size / 4), round(self.pos_y + size / 4)), 3)
        elif self.direction == 2:
            pygame.draw.rect(self.screen, color,
                             pygame.Rect(self.pos_x, self.pos_y, size / 2, size))
            pygame.draw.circle(self.screen, self.settings.border_color,
                               (round(self.pos_x + 3 * size / 4), round(self.pos_y + size / 4)), 3)
            pygame.draw.circle(self.screen, self.settings.border_color,
                               (round(self.pos_x + 3 * size / 4), round(self.pos_y + 3 * size / 4)), 3)
        elif self.direction == 3:
            pygame.draw.rect(self.screen, color,
                             pygame.Rect(self.pos_x, self.pos_y, size, size / 2))
            pygame.draw.circle(self.screen, self.settings.border_color,
                               (round(self.pos_x + size / 4), round(self.pos_y + 3 * size / 4)), 3)
            pygame.draw.circle(self.screen, self.settings.border_color,
                               (round(self.pos_x + 3 * size / 4), round(self.pos_y + 3 * size / 4)), 3)
        elif self.direction == 4:
            pygame.draw.rect(self.screen, color,
                             pygame.Rect(round(self.pos_x + size / 2), self.pos_y, size / 2, size))
            pygame.draw.circle(self.screen, self.settings.border_color,
                               (round(self.pos_x + size / 4), round(self.pos_y + size / 4)), 3)
            pygame.draw.circle(self.screen, self.settings.border_color,
                               (round(self.pos_x + size / 4), round(self.pos_y + 3 * size / 4)), 3)


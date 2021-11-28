import pygame


# Scoreboard initializes a scoreboard for the snake_game
# and updates it as the game progresses
class Scoreboard:

    def __init__(self, snake_game):
        self.screen = snake_game.screen
        self.text_color = snake_game.settings.score_color
        self.border_color = snake_game.settings.border_color
        self.points_per_apple = snake_game.settings.points_per_apple
        self.font = snake_game.settings.font
        mx, my = snake_game.settings.margins

        # Scoreboard border
        cols = snake_game.settings.cols
        size = snake_game.settings.grid_size
        self.scoreboard = pygame.Rect(size * (cols + 1) + mx, my,
                                      snake_game.settings.font_size * 6, snake_game.settings.font_size * 2)

        # Scores on the scoreboard
        self.points = 0
        self.s_length = 1

    # Increments the score. Should be called when an apple is eaten.
    def increment(self):
        self.points += self.points_per_apple
        self.s_length += 1

    # Draws the scores on the screen
    def draw(self):
        points_surface, points_rect, length_surface, length_rect = self._prep_scores()
        # Draw the scoreboard components onto the screen
        pygame.draw.rect(self.screen, self.border_color, self.scoreboard, 3)
        self.screen.blit(points_surface, points_rect)
        self.screen.blit(length_surface, length_rect)

    # Renders the scores and aligns them in the scoreboard rectangle
    def _prep_scores(self):
        # Render the points text and left-align it in the scoreboard
        points_surface = self.font.render(f'Score: {self.points}', True, self.text_color)
        points_rect = points_surface.get_rect()
        points_rect.top = self.scoreboard.top + 10
        points_rect.left = self.scoreboard.left + 10
        # Render the length text and left-align it in the scoreboard under the points text
        length_surface = self.font.render(f'Length: {self.s_length}', True, self.text_color)
        length_rect = length_surface.get_rect()
        length_rect.topleft = points_rect.bottomleft
        return points_surface, points_rect, length_surface, length_rect

import pygame


# The PauseButton class will initialize and create the
# Pause Button that can be pressed by the user to pause the game
class PauseButton:

    def __init__(self, snake_game):
        self.screen = snake_game.screen
        self.border_color = snake_game.settings.border_color
        self.size = snake_game.settings.pause_size
        self.settings = snake_game.settings
        self.big_rect = None
        self.x = None
        self.y = None
        self.left_rect = None
        self.right_rect = None
        self.prep_rects()

    # Preps the pause button rectangles before drawing.
    # Updates rectangles when the window is resized.
    def prep_rects(self):
        mx, my = self.settings.margins
        # Creates the rect for the border of the button
        x_big, y_big = self.screen.get_rect().topright
        self.big_rect = pygame.Rect(x_big - self.size - mx,
                                    y_big + my,
                                    self.size,
                                    self.size)
        # Creates the rect for the pause icon (which looks like ||).
        # The fifths are used to split the pause button into 25 squares
        # so that the pause icon is even and symmetrical.
        self.x, self.y = self.big_rect.topleft
        self.left_rect = pygame.Rect(self.x + self.size / 5,
                                     self.y + self.size / 5,
                                     self.size / 5,
                                     3 * self.size / 5)
        self.right_rect = pygame.Rect(self.x + 3 * self.size / 5,
                                      self.y + self.size / 5,
                                      self.size / 5,
                                      3 * self.size / 5)

    # Draws the pause button on the screen
    def draw(self, paused):
        pygame.draw.rect(self.screen, self.border_color, self.big_rect, 2)
        if paused:
            # Draws a triangle for the continue playing icon
            pygame.draw.polygon(self.screen, self.border_color, [(self.x + self.size / 5, self.y + self.size / 5),
                                                                 (self.x + self.size / 5, self.y + 4 * self.size / 5),
                                                                 (self.x + 4 * self.size / 5, self.y + self.size / 2)])
        else:
            # Draws 2 rectangles for the pause icon
            pygame.draw.rect(self.screen, self.border_color, self.left_rect)
            pygame.draw.rect(self.screen, self.border_color, self.right_rect)

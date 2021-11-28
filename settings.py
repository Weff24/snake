import pygame


# The Settings class holds all the Snake game default settings
# and can be changed to the users preferences
class Settings:

    def __init__(self):
        # Window settings
        window_width = 1200
        window_height = 800
        self.window_dim = (window_width, window_height)
        self.window_margin_x = 10
        self.window_margin_y = 10
        self.margins = (self.window_margin_x, self.window_margin_y)

        # Board settings
        self.bg_color = (200, 200, 200)
        self.border_color = (0, 0, 0)
        self.grid_size = 30
        self.block_size = self.grid_size - 1
        self.rows = 20
        self.cols = 20

        # Snake settings
        self.snake_color = (0, 204, 0)
        self.speed = 4
        self.start_pos = (round(self.rows / 2) * self.grid_size + self.window_margin_x + 1,
                          round(self.cols / 2) * self.grid_size + self.window_margin_y + 1)

        # Apple settings
        self.apple_color = (204, 0, 0)

        # Text and font settings
        self.font_size = 40
        self.font = pygame.font.SysFont('default', self.font_size)

        # Scoreboard settings
        self.score_color = (0, 0, 0)
        self.points_per_apple = 250

        # 'Play' and 'Play Again' button settings
        self.button_width = 250
        self.button_height = 65
        self.button_bg_color = (0, 230, 0)
        self.message_color = (0, 0, 0)

        # Pause button settings
        self.pause_size = 50

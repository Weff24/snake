import pygame


# The StartButton class will initialize and create the
# Start Button that can be pressed by the user to start a game
class StartButton:

    def __init__(self, snake_game, text):
        self.screen = snake_game.screen
        self.bg_color = snake_game.settings.button_bg_color
        self.text_color = snake_game.settings.message_color
        self.border_color = snake_game.settings.border_color
        self.font = snake_game.settings.font
        self.width = snake_game.settings.button_width
        self.height = snake_game.settings.button_height

        self.text = text

        # Renders the button's text and centers the button's rectangle
        self.button_text = self.font.render(self.text, True, self.text_color)
        self.text_rect = self.button_text.get_rect()
        self.text_rect.center = self.screen.get_rect().center
        self.button_rect = pygame.Rect(0, 0, self.width, self.height)
        self.button_rect.center = self.screen.get_rect().center

    # Changes the text displayed on the button, renders the text, and
    # centers the text on the screen
    def set_text(self, new_text):
        self.text = new_text
        self.button_text = self.font.render(self.text, True, self.text_color)
        self.text_rect = self.button_text.get_rect()
        self.text_rect.center = self.screen.get_rect().center

    # Centers the text and play button after the window is resized
    def center_rects(self):
        self.button_rect.center = self.screen.get_rect().center
        self.text_rect.center = self.screen.get_rect().center

    # Draws the start button on the screen
    def draw(self):
        self.screen.fill(self.bg_color, self.button_rect)
        self.screen.blit(self.button_text, self.text_rect)
        pygame.draw.rect(self.screen, self.border_color, self.button_rect, 2)


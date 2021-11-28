import sys
import pygame

from settings import Settings
from snake_body_block import SnakeBodyBlock
from snake_head import SnakeHead
from snake_tail import SnakeTail
from apple import Apple
from scoreboard import Scoreboard
from start_button import StartButton
from pause_button import PauseButton


# SnakeGameRunner initializes and runs a game of Snake
class SnakeGameRunner:

    def __init__(self):
        pygame.init()

        # Initialize the game settings listed in the Settings class
        # and initialize the scoreboard
        self.settings = Settings()

        # Create and display the snake game window
        pygame.display.set_caption('Snake')
        self.screen = pygame.display.set_mode(self.settings.window_dim, pygame.RESIZABLE)
#        img = pygame.image.load('images/Viper_icon32.png')
#        pygame.display.set_icon(img)

        # Initialize snake game objects, flags, and buttons
        self.game_running = False
        self.paused = False
        self.was_block_added = False
        self.scoreboard = Scoreboard(self)
        self.play_button = StartButton(self, 'Play')
        self.pause_button = PauseButton(self)
        # Snake is represented by a list of snake blocks
        self.snake = [SnakeHead(self, self.settings.start_pos)]
        self.apple = Apple(self)

    # Runs the game, checks for events, and updates the screen
    def run(self):
        while True:
            self._check_events()
            if self.game_running and (not self.paused):
                self._update_snake()
                self._check_collision()
            self._update_screen()

    # Checks for mouse, keyboard, and window resize events by user
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_pause_button_click()
                self._check_play_button_click()
            elif event.type == pygame.VIDEORESIZE:
                self._update_window(event)

    # Checks for key press events
    def _check_keydown(self, event):
        # Doesn't process directional keydown events when paused
        if not self.paused:
            prev_dir = self.snake[0].direction
            # direction = 1 (up), 2 (right), 3 (down), or 4 (left) for snake block objects
            if prev_dir != 3 and (event.key == pygame.K_UP or event.key == pygame.K_w):
                self.snake[0].direction = 1
            elif prev_dir != 4 and (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                self.snake[0].direction = 2
            elif prev_dir != 1 and (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                self.snake[0].direction = 3
            elif prev_dir != 2 and (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                self.snake[0].direction = 4
        # Checks for Space Bar keydown events whether or not the game is paused
        if event.key == pygame.K_SPACE:
            self.paused = not self.paused

    # Checks if the Pause button is clicked and flags whether or not the
    # game is paused
    def _check_pause_button_click(self):
        button_clicked = self.pause_button.big_rect.collidepoint(pygame.mouse.get_pos())
        if self.game_running and button_clicked:
            self.paused = not self.paused

    # Checks if the 'Play' or 'Play Again' button is clicked
    def _check_play_button_click(self):
        button_clicked = self.play_button.button_rect.collidepoint(pygame.mouse.get_pos())
        if (not self.game_running) and button_clicked:
            # Starts a new game of Snake
            self._game_startup()

    # Starts/restarts a game of Snake by settings the dynamic values
    # back to their initial values
    def _game_startup(self):
        self.snake = [SnakeHead(self, self.settings.start_pos)]
        self.apple = Apple(self)
        self.scoreboard.points = 0
        self.scoreboard.s_length = 1
        self.play_button.set_text('Play Again')
        self.game_running = True
        self.paused = False

    # Updates the position of some game components when the window is resized
    def _update_window(self, event):
        screen_size = event.size
        self.screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
        self.pause_button.prep_rects()
        self.play_button.center_rects()

    # Updates the movement direction of each snake block
    def _update_snake(self):
        for block_i in reversed(range(len(self.snake))):
            if self.was_block_added:
                # Only move first/head block and update direction of added block
                # to the first/head block's new move
                if block_i == 0:
                    self.snake[block_i].update_pos()
                    self.snake[block_i + 1].direction = self.snake[block_i].direction
            else:
                self.snake[block_i].update_pos()
                # Update each block's direction using the previous block's direction
                if block_i > 0:
                    self.snake[block_i].direction = self.snake[block_i - 1].direction
        self.was_block_added = False

    # Checks for different types of collisions and responds accordingly
    def _check_collision(self):
        self._border_collision()
        self._apple_collision()
        self._self_collision()

    # Checks if the first/head block collides with the grid's border
    # and ends the game if there is a collision
    def _border_collision(self):
        rows = self.settings.rows
        cols = self.settings.cols
        size = self.settings.grid_size
        mx, my = self.settings.margins
        x = self.snake[0].pos_x
        y = self.snake[0].pos_y
        # Check if the snake's x or y position is outside the border
        if x < mx or x >= (cols * size) + mx or y < my or y >= (rows * size) + my:
            self.game_running = False

    # Checks if the first/head block collides with an apple object
    # and increases the length of the snake by 1 if there is a collision
    def _apple_collision(self):
        head_block = self.snake[0]
        if head_block.pos_x == self.apple.x and head_block.pos_y == self.apple.y:
            # Create new apple in random position
            self.apple = Apple(self)
            # Add new block to snake
            if len(self.snake) == 1:
                self.snake.insert(1, SnakeTail(self, [head_block.pos_x, head_block.pos_y], head_block.direction))
            else:
                self.snake.insert(1, SnakeBodyBlock(self, [head_block.pos_x, head_block.pos_y], head_block.direction))
            self.was_block_added = True
            # Increment score and length
            self.scoreboard.increment()

    # Checks if the first/head block collides with any snake blocks
    # and ends the game if there is a collision
    def _self_collision(self):
        # Snake head can't collide with blocks 1, 2, and 3
        for block_i in range(4, len(self.snake)):
            if self.snake[block_i].pos_x == self.snake[0].pos_x and \
                    self.snake[block_i].pos_y == self.snake[0].pos_y:
                self.game_running = False

    # Draws the game components, objects, and buttons
    def _update_screen(self):
        # If a game is running, draw game components and objects.
        # If a game is not running, draw a 'Play/Play Again' button.
        if self.game_running:
            self._draw_board()
            self._draw_snake()
            self.apple.draw()
            self.scoreboard.draw()
            self.pause_button.draw(self.paused)
        else:
            self.play_button.draw()

        # Update to the new screen frame
        pygame.display.flip()
        pygame.time.wait(int(500/self.settings.speed))

    # Draws the board/grid that the snake moves on
    def _draw_board(self):
        self.screen.fill(self.settings.bg_color)
        # Top left corner of grid
        mx, my = self.settings.margins
        # Draw grid with thick boarders
        size = self.settings.grid_size
        rows = self.settings.rows
        cols = self.settings.cols
        for col in range(1, cols):
            pygame.draw.line(self.screen, self.settings.border_color,
                             ((col * size) + mx, my),
                             ((col * size) + mx, (rows * size) + my))
        for row in range(1, rows):
            pygame.draw.line(self.screen, self.settings.border_color,
                             (mx, (row * size) + my),
                             ((cols * size) + mx, (row * size) + my))
        pygame.draw.rect(self.screen, self.settings.border_color,
                         pygame.Rect(mx - 2, my - 2, cols * size + 4, rows * size + 4),
                         4)

    # Draws the whole snake by drawing each individual snake block
    def _draw_snake(self):
        for block in self.snake:
            block.draw()


# Main method that creates and runs a game of Snake
if __name__ == '__main__':
    snake_game = SnakeGameRunner()
    snake_game.run()

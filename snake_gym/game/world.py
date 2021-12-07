
import pygame
import numpy as np
from .colors import Colors
from .snake import Snake

SCREEN_RATIO = 30


class World:
    """
    Class that represents the environment in which the game will be played
    """

    def __init__(self, snake: Snake, board: np.ndarray = np.zeros((20, 15))):

        # create game
        pygame.init()

        # multiply by SCREEN_RATIO pixels to get total screen size
        screen_size = (board.shape[0] * SCREEN_RATIO, board.shape[1] * SCREEN_RATIO)

        # create screen
        self.display = pygame.display.set_mode(screen_size, 0, 32)
        self.display.fill(Colors.BLACK)

        # store the variables
        self.snake = snake
        self.board = board

    def _clear(self):
        """
        Private method to clear the world of the previous state.
        We need this method because the snake will keep moving, so we should not remember it's previous
        locations
        """
        self.board = np.zeros(self.board.shape)

    def _process(self):
        """
        Function to process the location of the snake and food and draw it into the world
        """

        # start by clearing the board
        self._clear()

        # get head coordinates
        head = self.snake.head_coords

        # draw the snake head
        self.board[head[0]][head[1]] = 1

    def draw(self):
        """
        Method to draw the world using the pygame interface.
        """

        # process the world
        self._process()

        # start with black background
        self.display.fill(Colors.BLACK)

        # extract the shape
        x, y = self.board.shape

        # we set x-1 and y-1 to refrain from drawing the border
        for i in range(x):
            for j in range(y):

                # draw snake part
                if self.board[i, j] == 1:
                    pygame.draw.rect(self.display, Colors.WHITE,
                                     pygame.Rect(i*SCREEN_RATIO,
                                                 j*SCREEN_RATIO,
                                                 SCREEN_RATIO - 2, SCREEN_RATIO - 2))

                # draw food
                elif self.board[i, j] == 2:
                    pygame.draw.rect(self.display, Colors.RED,
                                     pygame.Rect(i * SCREEN_RATIO,
                                                 j * SCREEN_RATIO,
                                                 SCREEN_RATIO - 2, SCREEN_RATIO - 2))

        # update display
        pygame.display.update()

    def reset(self):
        """
        A function to reset the world
        """

        # todo implement

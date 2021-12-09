#
# File: game/world.py
# Desc: The world class describing the game state
# Auth: Oscar Ligthart
#
#####################################################

import pygame
import numpy as np
from .colors import Colors
from .snake import Snake
import random

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

        # store the variables
        self.snake = snake
        self.board = board

        # place food upon initialization
        self.food_location = None
        self.place_food()

    def run_tick(self):
        """
        Function to process the location of the snake and food and draw it into the world
        :return: boolean denoting whether the game has ended or not
        """

        ############################
        # Process game information #
        ############################

        # check if snake eats food
        self._check_food()

        # check if snake collides
        if self._check_collision():
            return True

        ############################
        # Process the board        #
        ############################

        # start by clearing the board
        self._clear()

        # get body coordinates
        for part in self.snake.body:
            self.board[part[0]][part[1]] = 1

        # get food location
        self.board[self.food_location[0]][self.food_location[1]] = 2

        ############################
        # Draw the board           #
        ############################

        self._draw()

        # if we reach this we can continue the game
        return False

    def place_food(self):
        """
        Method to place a bit of food on the board
        """

        # get all possible coordinates
        all_coords = [[x, y] for x in range(self.board.shape[0]) for y in range(self.board.shape[1])]

        # remove the snake bodt from all coords
        for part in self.snake.body:
            all_coords.remove(part)

        # pick one for placing food
        self.food_location = random.choice(all_coords)

    def _clear(self):
        """
        Private method to clear the world of the previous state.
        We need this method because the snake will keep moving, so we should not remember it's previous
        locations
        """
        self.board = np.zeros(self.board.shape)

    def _check_food(self):
        """
        Private method that checks if snake eats food
        """
        # check if snake hits food
        if self.snake.head_coords == self.food_location:

            # increase snake length
            self.snake.length += 1

            # place new food
            self.place_food()

    def _check_collision(self):
        """
        Private method to check if the snake collides with itself
        :return: boolean denoting whether the snake has collided or not
        """
        # check if the snake head hits any part of the body (that is not the head)
        return self.snake.head_coords in self.snake.body[1:]

    def _draw(self):
        """
        Method to draw the world using the pygame interface.
        """

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

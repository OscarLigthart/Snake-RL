#
# File: game/snake.py
# Desc: The snake class and podyparts
# Auth: Oscar Ligthart
#
########################

from .actions import action_space
import numpy as np


class Snake:
    """
        Class that represents the snake that can be controlled by the user
    """

    def __init__(self, initial_length=2, board: np.ndarray = np.zeros((20, 15))):
        """
        Initialization method
        """
        # store the board width and length
        self.width = board.shape[0]
        self.height = board.shape[1]

        # store head coordinates
        self.head_coords = [0, 7]
        self.length = initial_length

        # keep track of the past head coordinates to create the snake
        self.body = [self.head_coords]

    def move(self, action):
        """
        This function moves the snake head and lets the body follow
        :param action: integer denoting the action to take
        """

        # convert action to relative movement
        relative_movement = action_space[action]

        # move the head in the direction specified by changes in coordinates
        next_location = [sum(pair) for pair in zip(self.head_coords, relative_movement)]

        # clip the next location to get the new head coords
        self.head_coords = self._clip(next_location)

        # now move the body
        self.body.insert(0, self.head_coords)

        # trim the body
        self.body = self.body[:self.length]

    def _clip(self, next_location):
        """
        Clip the next movement based on the size of the board
        """

        # clip based on the location
        if next_location[0] == -1:
            next_location[0] = self.width
        elif next_location[0] == self.width:
            next_location[0] = 0
        elif next_location[1] == -1:
            next_location[1] = self.height
        elif next_location[1] == self.height:
            next_location[1] = 0

        return next_location

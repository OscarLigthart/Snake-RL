#
# File: game/snake.py
# Desc: The snake class and podyparts
# Auth: Oscar Ligthart
#
########################

from .world import World


class Snake:
    """
        Class that represents the snake that can be controlled by the user
    """

    def __init__(self, world : World):
        """
        Initialization method
        """
        # store the board
        self.board = world.board
        self.head_coords = [0, 0]

    def move(self, xy_move):
        """
        This function moves the snake head and lets the body follow
        """

        # move the head in the direction specified by changes in coordinates
        self.head_coords = [sum(pair) for pair in zip(self.head_coordinates, xy_move)]

        # todo implement


class Bodypart:
    """
        Class that represents the snake that can be controlled by the user
    """
    def __init__(self, screen, location):
        self.screen = screen
        self.location = location
        self.old_location = location

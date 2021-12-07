#
# File: game/snake.py
# Desc: The snake class and podyparts
# Auth: Oscar Ligthart
#
########################


class Snake:
    """
        Class that represents the snake that can be controlled by the user
    """

    def __init__(self):
        """
        Initialization method
        """

        # store head coordinates
        self.head_coords = [0, 7]

    def move(self, xy_move):
        """
        This function moves the snake head and lets the body follow
        """

        # move the head in the direction specified by changes in coordinates
        self.head_coords = [sum(pair) for pair in zip(self.head_coords, xy_move)]

        # todo implement


class Bodypart:
    """
    Class that represents the snake that can be controlled by the user
    """
    def __init__(self, location):
        self.location = location
        self.old_location = location

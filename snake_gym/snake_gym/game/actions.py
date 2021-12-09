#
#
#
######################
import enum
import numpy as np


class Actions(enum.Enum):
    """
    Actions that the human can take
    """
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class AgentActions:
    """
    Actions that the agent can take
    It takes them from ego perspective
    """
    def __init__(self):

        # these actions are relative
        self.RIGHT = 0
        self.FORWARD = 1
        self.LEFT = 2

    @staticmethod
    def convert(direction, action):
        """
        Method to convert relative action to absolute action
        :param direction: the current direction
        :param action: the relative action taken
        :return: array of relative movement
        """

        # map current direction to relative movement
        relative_movement = action_space[direction]

        # swap the actions if the snake turns left/right
        if action != 1:

            # check if index is on 0, if so we invert
            if not relative_movement.index(0):
                relative_movement = list(np.array(relative_movement) * -1)

            # change direction
            relative_movement = [relative_movement[1], relative_movement[0]]

        # if the snake turns right, we have the same operations as before (left), but we need to invert it
        if action == 0:
            relative_movement = list(np.array(relative_movement) * -1)

        # map back to action to get the absolute direction
        return relative_movement


# a dictionary that converts the action space to relative movement
action_space = {
    Actions.UP: [0, -1],
    Actions.DOWN: [0, 1],
    Actions.LEFT: [-1, 0],
    Actions.RIGHT: [1, 0],
}

movement_space = {
    (0, -1): Actions.UP,
    (0, 1): Actions.DOWN,
    (-1, 0): Actions.LEFT,
    (1, 0): Actions.RIGHT
}

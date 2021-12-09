#
#
#
######################
import enum


class Actions(enum.Enum):
    """
    Actions space
    """
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


# a dictionary that converts the action space to relative movement
action_space = {
    Actions.UP: [0, -1],
    Actions.DOWN: [0, 1],
    Actions.LEFT: [-1, 0],
    Actions.RIGHT: [1, 0],
}

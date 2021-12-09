#
#
#
######################

import math
from snake_gym.game.snake import Snake, AgentSnake
from snake_gym.game.world import World
from snake_gym.game.actions import Actions, AgentActions


class Env:
    """
    A gym environment for the Snake game
    """
    def __init__(self, human_player=True):

        # create snake
        if human_player:
            self.snake = Snake()
        else:
            self.snake = AgentSnake()

        # create world
        self.world = World(self.snake)

        # draw environment
        self.world.run_tick()

    def step(self, action):
        """
        Method to perform an action given a state
        :param action: the action to perform
        :return: [next_state, reward, done]
        """

        # get state
        current_state = self._get_state()

        # save snake head
        prev_location = self.snake.head_coords.copy()

        # move the snake
        self.snake.move(action)

        # run a game tick in the world
        food_capture, done = self.world.run_tick()

        reward = self._get_reward(prev_location, food_capture, done)

        # get next state, unless we're done, then we use the old one
        if done:
            next_state = current_state
        else:
            next_state = self._get_state()

        # return the environment information
        return next_state, reward, done

    def _get_state(self):
        """
        Function to get the state
        A state looks like this:
            [
                Angle of head to fruit,
                left neighbour,
                top neighbour,
                right neighbour
            ]
        """

        # create new state
        state = []

        # get the angle to the fruit
        angle = self._calc_food_angle()

        # add the angle to the state
        state.append(angle)

        # need to check whether there is a 1 on the top, left or right side of the snake at its current location
        x, y = self.snake.head_coords

        # check if we would collide upon taking any of the actions
        for a in range(3):

            # get coordinate difference wrt direction
            dir = AgentActions.convert(self.snake.direction, a)

            # add the direction
            coord = self.snake.clip([x + dir[0], y + dir[1]])

            # add coordinates to snake head and check if there is a 1 on the board
            # body collision
            body_col = self.world.board[coord[0], coord[1]] == 1

            # add the indicator to the state
            state.append(int(body_col))

        return state

    def _get_reward(self, old_coord, food_capture, done):
        """
        Function to calculate the reward given a state
        """

        # first we check if the snake managed to get food
        if food_capture:
            return 1

        # check for collision
        if done:
            return -1

        # set reward for moving closer/further from fruit
        old_dist = self._calc_food_distance(old_coord)
        new_dist = self._calc_food_distance(self.snake.head_coords)

        # check if closer or further from fruit
        if old_dist > new_dist:
            return 0.1
        else:
            return -0.2

    def _calc_food_angle(self):
        """
        Method to get the angle of the head to the food
        :return: angle (normalized)
        """

        # get coordinates of snake head
        snake_x, snake_y = self.snake.head_coords

        # get coordinates of food
        food_x, food_y = self.world.food_location

        # get direction to define starting point of angle
        # maybe dictionary to convert direction list to degrees
        rad = math.atan2(snake_y - food_y, snake_x - food_x)

        # convert radians to angle
        angle = math.degrees(rad)

        # keep angle in same domain
        angle = (angle + 360) % 360

        # convert direction to degrees
        dir_conv = {Actions.UP: 90, Actions.LEFT: -180, Actions.DOWN: -90, Actions.RIGHT: 0}

        # move origin
        angle += dir_conv[self.snake.direction]
        angle = (angle + 180) % 360

        # now normalize everything over 180 should be negative
        if angle > 180:
            angle = (angle - 180) * -1

            # normalize
            angle = -1 - (angle / 180)

        # normalize everything below 180
        else:
            angle = angle / 180

        return angle

    def _calc_food_distance(self, coords):
        """
        Method to calculate the distance to the food
        """
        return math.sqrt(
            abs(coords[0] - self.world.food_location[0]) ** 2
            + abs(coords[1] - self.world.food_location[1]) ** 2
        )

    def reset(self):
        """
        Method to reset the game and retrieve the first state
        :return: state
        """

        # todo implement

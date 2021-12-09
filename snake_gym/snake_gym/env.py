#
#
#
######################

import math
from snake_gym.game.snake import Snake
from snake_gym.game.world import World


class Env:
    """
    A gym environment for the Snake game
    """
    def __init__(self):

        # create snake
        self.snake = Snake()

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

        # save snake head
        prev_location = self.snake.head_coordinates.copy()

        # move the snake
        self.snake.move(action)

        # run a game tick in the world
        food_capture, done = self.world.run_tick()

        reward = self._get_reward(prev_location, food_capture, done)

        # return the environment information
        return 0, reward, done

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

        return []

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
        new_dist = self._calc_food_distance(self.snake.head_coordinates)

        # check if closer or further from fruit
        if old_dist > new_dist:
            return 0.1
        else:
            return -0.2

    def _calc_food_angle(self):
        """
        TODO MIGHT BE ABLE TO SPEED THIS UP
        Method to get the angle of the head to the food
        :return: angle (normalized)
        """

        # get coordinates of snake head
        snake_x, snake_y = self.snake.head_coordinates

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
        dir_conv = {(0, -1): 90, (-1, 0): -180, (0, 1): -90, (1, 0): 0}

        # move origin
        angle += dir_conv[tuple(self.direction)]
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

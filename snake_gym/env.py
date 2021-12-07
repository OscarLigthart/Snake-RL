#
#
#
######################

class SnakeEnv:
    """
    A gym environment for the Snake game
    """
    def __init__(self):
        return

    def step(self, action):
        """
        Method to perform an action given a state
        :param action: the action to perform
        :return: [next_state, reward, done]
        """

        # todo implement

    def state(self):
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

        # check if the snake is still alive, if not there is no state to return to
        if self.snake.dead:
            return []

        # create new state
        state = []

        # get the angle to the fruit
        angle = self.food_angle()

        # add the angle to the state
        state.append(angle)

        # need to check whether there is a 1 on the top, left or right side of the snake at its current location
        x, y = self.snake.head_coordinates

        # get the direction of left (action 0)
        for a in range(3):

            # get coordinate difference wrt direction
            dir = self.change_direction(a)

            # add coordinates to snake head and check if there is a 1 on the board
            # body collision
            body_col = self.board[x + dir[0], y + dir[1]] == 1

            # out of bounds
            oub = False
            if x + dir[0] < 0 or x + dir[0] > (self.board.shape[0] - 2)\
                    or y + dir[1] < 0 or y + dir[1] > (self.board.shape[1] - 2):
                oub = True

            # add the indicator to the state
            state.append(int(body_col or oub))

        return state

    def reward(self, old_coord, food):
        """
        Method to define the reward for the action given the state
        :return: reward
        """

        # first we check if the snake managed to get food
        if food:
            return 1

        # check for collision
        if collision_detector(self.snake, self):
            return -1

        # set reward for moving closer/further from fruit
        old_dist = self.food_distance(old_coord)
        new_dist = self.food_distance(self.snake.head_coordinates)

        # check if closer or further from fruit
        if old_dist > new_dist:
            return 0.1
        else:
            return -0.2

    def reset(self):
        """
        Method to reset the game and retrieve the first state
        :return: state
        """

        # todo implement

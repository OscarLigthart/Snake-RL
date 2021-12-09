import pygame
from pygame.locals import *
from snake_gym import Env
from snake_gym.game.actions import AgentActions
from snake_gym.agent import QNetwork


clock = pygame.time.Clock()


def main():
    """
    Main function to play the game
    """

    # initialize event
    env = Env()

    # start by going right
    action = AgentActions.FORWARD

    model = QNetwork()

    done = False
    while not done:
        df = clock.tick(4)

        # get agent


        # need to take a step here, keep track of
        _, _, done = env.step(action)


if __name__ == "__main__":
    main()

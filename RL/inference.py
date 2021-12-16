#
# File: RL/inference.py
# Desc: Inference script showing trained agent behaviour
# Auth: Oscar Ligthart
#
########################

import pygame
import os
from snake_gym import Env
from agent.qnetwork import QNetwork
from utils.helpers import select_action


clock = pygame.time.Clock()


def main():
    """
    Main program that loads a pretrained network
    :return:
    """

    # create board and randomly place food
    env = Env(human_player=False)
    in_channels = env.get_state_size()

    # create model and load weights
    model = QNetwork(in_channels, 128)

    # check if filepath exists
    filepath = os.path.dirname(os.path.realpath(__file__)) + "/agent/trained_agent.pt"
    if not os.path.isfile(filepath):
        raise RuntimeError(f"No pretrained weights found at: {filepath}")

    # load model
    model.load(filepath)

    # get the first state
    state = env.reset()
    done = False
    while not done:

        # create correct frame rate
        clock.tick(10)

        # perform a step in the environment
        action = select_action(model, state, 0)
        state, reward, done = env.step(action)


if __name__ == "__main__":
    main()

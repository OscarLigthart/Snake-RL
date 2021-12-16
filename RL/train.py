#
# File: RL/train.py
# Desc: Training script
#
#
#################

import pygame
import os
import torch
import torch.nn.functional as F
from torch import optim
from utils.helpers import compute_q_val, compute_target, select_action, get_epsilon
from utils.memory import ReplayMemory
from agent.qnetwork import QNetwork
from pygame.locals import *
from snake_gym.env import Env


clock = pygame.time.Clock()


def train(model, memory, optimizer, params):
    """
    Method to train the model for a single step
    """

    # don't learn without some decent experience
    if len(memory) < params.batch_size:
        return None

    # random transition batch is taken from experience replay memory
    transitions = memory.sample(params.batch_size)

    # transition is a list of 4-tuples, instead we want 4 vectors (as torch.Tensor's)
    state, action, reward, next_state, done = zip(*transitions)

    # convert to PyTorch and define types
    state = torch.tensor(state, dtype=torch.float)
    action = torch.tensor(action, dtype=torch.int64)  # Need 64 bit to use them as index
    next_state = torch.tensor(next_state, dtype=torch.float)
    reward = torch.tensor(reward, dtype=torch.float)
    done = torch.tensor(done, dtype=torch.bool)  # Boolean

    # compute the q value
    q_val = compute_q_val(model, state, action)

    with torch.no_grad():
        target = compute_target(model, reward, next_state, done, params.discount_factor)

    # loss is measured from error between current and newly expected Q values
    loss = F.smooth_l1_loss(q_val, target)

    # backpropagation of loss to Neural Network (PyTorch magic)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    return loss.item()


def run_episodes(model, env, memory, params):
    """
    Method to run an experiment for a set number of episodes. It performs
    the training end-to-end
    :param model: the DQN model to be trained
    :param env: the snake gym environment
    :param memory: the replaymemory used for training
    :param params: the hyperparameters of the experiment
    :return: list consisting of the duration of each of the episodes
    """

    optimizer = optim.Adam(model.parameters(), params.learn_rate)

    global_steps = 0  # Count the steps (do not reset at episode start, to compute epsilon)
    episode_durations = []  #
    for i in range(params.num_episodes):

        t = 0
        state = env.reset()

        # Take actions until end of episode
        for t in range(1000):

            # determine game speed
            if i % 25 == 0 and i != 0:
                df = clock.tick(25)
                epsilon = 0
            else:
                df = clock.tick(100)
                epsilon = get_epsilon(global_steps)

            # perform a step in the environment
            action = select_action(model, state, epsilon)
            next_state, reward, done = env.step(action)
            memory.push((state, action, reward, next_state, done))

            # only sample if there is enough memory
            if len(memory) > PARAMS.batch_size:
                loss = train(model, memory, optimizer, params)

            state = next_state
            global_steps += 1

            # stop if the game state was done
            if done:
                break

        episode_durations.append(t)

    return episode_durations


class PARAMS:
    """
    Class holding the hyperparameters used for this training
    """
    num_episodes = 100
    batch_size = 4
    discount_factor = 0.8
    learn_rate = 1e-3
    num_hidden = 128


def main():
    """
    Main program consisting of initialization of the experiment and running using helper
    functions and functions declared above
    :return:
    """

    # create game
    pygame.init()

    # create board and randomly place food
    env = Env(human_player=False)
    in_channels = env.get_state_size()

    # initialize the replay memory
    memory = ReplayMemory(1000)

    # create model
    model = QNetwork(in_channels, PARAMS.num_hidden)

    # train
    episode_durations = run_episodes(model, env, memory, PARAMS)

    # save the trained agent
    model.save(os.path.dirname(os.path.realpath(__file__)) + "/agent/trained_agent.pt")


if __name__ == "__main__":
    main()

#
# File: RL/train.py
# Desc: Training script
#
#
#################

import pygame
import torch
import torch.nn.functional as F
from torch import optim
from utils.helpers import compute_q_val, compute_target, select_action, get_epsilon
from utils.memory import ReplayMemory
from agent.qnetwork import QNetwork
from pygame.locals import *
from snake_gym.env import Env


clock = pygame.time.Clock()


def train(model, memory, optimizer, batch_size, discount_factor):
    """
    Method to train the model
    """

    # don't learn without some decent experience
    if len(memory) < batch_size:
        return None

    # random transition batch is taken from experience replay memory
    transitions = memory.sample(batch_size)

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
        target = compute_target(model, reward, next_state, done, discount_factor)

    # loss is measured from error between current and newly expected Q values
    loss = F.smooth_l1_loss(q_val, target)

    # backpropagation of loss to Neural Network (PyTorch magic)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    return loss.item()


def run_episodes(train, model, memory, env, num_episodes, batch_size, discount_factor, learn_rate, df):
    optimizer = optim.Adam(model.parameters(), learn_rate)

    global_steps = 0  # Count the steps (do not reset at episode start, to compute epsilon)
    episode_durations = []  #
    for i in range(num_episodes):

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

            action = select_action(model, state, epsilon)

            next_state, reward, done = env.step(action)

            memory.push((state, action, reward, next_state, done))

            # only sample if there is enough memory
            if len(memory) > batch_size:
                loss = train(model, memory, optimizer, batch_size, discount_factor)

            state = next_state
            global_steps += 1

            if done:
                break

        episode_durations.append(t)

    return episode_durations


def main():

    # create game
    pygame.init()

    # create board and randomly place food
    env = Env(human_player=False)

    # hyperparameters
    num_episodes = 100
    batch_size = 4 #32
    discount_factor = 0.8
    learn_rate = 1e-3
    memory = ReplayMemory(1000)
    num_hidden = 128
    df = 8

    # create model
    model = QNetwork(num_hidden)

    # train
    episode_durations = run_episodes(train, model, memory, env,
                                     num_episodes, batch_size,
                                     discount_factor, learn_rate, df)


main()

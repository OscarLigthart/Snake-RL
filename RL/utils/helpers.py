import torch
import random
import numpy as np


def get_epsilon(it):

    # random actions at first,
    if it >= 1000:
        epsilon = 0.05
    else:
        epsilon = 1 - 0.95 * it * (1 / 1000)

        # after 1000 iterations, e-greedy with epsilon being 0.5
    return epsilon


def select_action(model, state, epsilon):

    # feed state to model to extract action
    actions = model(torch.FloatTensor(state))
    values, indices = actions.max(0)

    # determine if the model explores or not
    if random.random() < epsilon:
        a = np.random.choice(range(len(actions))).item()
    else:
        a = indices.item()

    return a


def compute_q_val(model, state, action):

    # get the actions given a batch of states
    actions = model(state)

    # the output of the model represents the q-values
    q_val = torch.gather(actions, 1, action.view(-1, 1))

    return q_val


def compute_target(model, reward, next_state, done, discount_factor):
    """
    Method that uses the next state to compute the target
    """

    # get action
    actions = model(next_state)
    _, indices = actions.max(1)

    # convert to target
    indices = torch.gather(actions, 1, indices.view(-1, 1))
    target = reward.view(indices.shape) + (discount_factor * indices)

    # set target to just the reward if next_state is terminal
    target[done] = reward[done].view(target[done].shape)
    return target

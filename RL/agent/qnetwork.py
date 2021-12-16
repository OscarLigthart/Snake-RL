#
# File: RL/agent/qnetwork.py
# Desc: A simple DQN for learning Snake
# Auth: Oscar Ligthart
#
##########################

import torch
from torch import nn
import torch.nn.functional as F


class QNetwork(nn.Module):
    """
    Deep Q-network
    """

    def __init__(self, in_channels, num_hidden=128):
        nn.Module.__init__(self)
        self.l1 = nn.Linear(in_channels, num_hidden)
        self.l2 = nn.Linear(num_hidden, num_hidden)
        self.l3 = nn.Linear(num_hidden, 3)

    def forward(self, x):
        """
        Forward pass through the network
        :param x: input     [batch_size x in_channels]
        :return: prediction [batch_size x 3]
        """
        x = F.relu(self.l1(x))
        x = F.relu(self.l2(x))
        x = self.l3(x)
        return x

    def save(self, filename):
        """
        Method to save weights into a torch .pt file
        :param filename: the path and filenmae to which the model should be stored
        :return: None
        """
        torch.save(self.state_dict(), filename)

    def load(self, filepath):
        """
        Method to load pretrained weights into the network
        :param filepath:
        :return: None
        """
        # load the state dict
        self.load_state_dict(torch.load(filepath))
        self.eval()

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
        x = F.relu(self.l1(x))
        x = F.relu(self.l2(x))
        x = self.l3(x)
        return x

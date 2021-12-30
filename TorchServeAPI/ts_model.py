import torch
from torch import optim
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    """
    Neural Network Architecture for TorchServeAPI
    """
    def __init__(self):
        super(Net, self).__init__()
        self.nn = nn.Sequential(

        )
    
    def forward(self, x):
        x = self.nn(x)
        return x


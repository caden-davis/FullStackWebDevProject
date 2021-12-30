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
        """
        Input Features:
        1. 
        2. 
        3. 
        4.

        Output:

        These requirements lend themselves to the following pseudo-structure:
        1. 
        2. 
        """
        self.nn = nn.Sequential(

        )
    
    def forward(self, x):
        x = self.nn(x)
        return x


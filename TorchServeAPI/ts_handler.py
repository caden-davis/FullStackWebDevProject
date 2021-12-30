from ts_model import Net
import torch
import torch.nn.functional as F
from torchvision import transforms

class Handler:
    """
    Handler Class for TorchServe API
    """
    def __init__(self):
        self.initialized = False
        pass

    def initialize(self, context):
        # Connect to net via torchserve
        self.initialized = True
        pass

    def preprocess(self):
        pass

    def inference(self):
        pass

    def postprocess(self):
        pass

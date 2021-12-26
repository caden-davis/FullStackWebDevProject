from modelDef import Net
import torch
# Import torchserve

import logging
logger = logging.getLogger("TorchServeAPI Handler")

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


_service = Handler()

def handle(data, context):
    if not _service.initialized:
        _service.initialize(context)

    if data is None:
        return None

    data = _service.preprocess(data)
    data = _service.inference(data)
    data = _service.postprocess(data)

    return data


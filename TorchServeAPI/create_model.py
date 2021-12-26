from TorchServeAPI.modelDef import load_model, save_model
from modelDef import *
import torch
import os

if (os.path.exists("model.pt")):
    model = load_model("model.pt")
else:
    model = Net()
train(model)
test(model)

save_model(model)

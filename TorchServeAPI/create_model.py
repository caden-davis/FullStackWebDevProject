from ts_model import Net
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch import optim

def train(model, trainX, trainY, batch_size=16, epochs=30):
    if torch.cuda.is_available():
        device = torch.device('cuda:0')
    else:
        device = torch.device('cpu')
    model.to(device)
    train_loader = torch.utils.data.DataLoader((trainX, trainY), batch_size=batch_size, shuffle=True)
    model.train()

    optimizer = torch.optim.Adam(model.parameters())
    criterion = nn.MSELoss()
    for batch_x, batch_y in train_loader:
        batch_x, batch_y = batch_x.to(device), batch_y.to(device)

        optimizer.zero_grad()
        batch_yhat = model(batch_x)
        loss = criterion(batch_yhat, batch_y)
        loss.backward()
        optimizer.step()


def test(model, testX, testY, batch_size=16, visualize=True):
    if torch.cuda.is_available():
        device = torch.device('cuda:0')
    else:
        device = torch.device('cpu')
    model.to(device)
    test_loader = torch.utils.data.DataLoader((testX, testY), batch_size=batch_size, shuffle=True)
    model.eval()
    z_scores = []

    for batch_x, batch_y in test_loader:
        batch_x, batch_y = batch_x.to(device), batch_y.to(device)

        batch_yhats = model(batch_y)
        z_scores.append((batch_yhats - batch_y) / batch_y) # scikit-learn function?
        if visualize:
            pass
            # plot batch_y[0] vs batch_x[0] with batch_yhat[0] vs batch_x[0] overlaid
    return z_scores


model = Net()

# Load data to train model
# train(model, train_x, train_y)
# test(model, test_x, test_y)

m = torch.jit.script(model)
m.save("model.pt")
